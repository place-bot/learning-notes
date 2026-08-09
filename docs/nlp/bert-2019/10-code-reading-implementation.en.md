# Intensive reading of Google’s original code and modern implementation

## 1. File map

|File|Responsibilities|
|---|---|
| `modeling.py` | BertConfig、embedding、Transformer encoder |
| `create_pretraining_data.py` |Document slicing, NSP, 15% mask, TFRecord|
| `run_pretraining.py` |MLM/NSP heads and joint loss|
| `optimization.py` |AdamW, warmup, linear attenuation|
| `run_classifier.py` |GLUE class classification|
| `run_squad.py` |span start and end prediction|
| `tokenization.py` |BasicTokenizer and WordPiece|

The repository is archived and the code is based on TensorFlow 1.x.

## 2. Data generation

Default parameters include:

```text
dupe_factor = 10
masked_lm_prob = 0.15
short_seq_prob = 0.1
```

`create_masked_lm_predictions` excludes special tokens, scrambles candidate positions, and generates input and original labels according to 80/10/10.

## 3. Model input

`BertModel` Receive:

- `input_ids [B,T]`；
- `input_mask [B,T]`；
- `token_type_ids [B,T]`。

The embedding postprocessor adds token-type and position embedding, followed by LayerNorm and dropout.

## 4. pretraining header

`get_masked_lm_output` gathers only the selected positions, performs dense + GELU + LayerNorm, and shares the input embedding weights. `get_next_sentence_output` makes a Class 2 classification for pooled `[CLS]`. The total losses are added directly.

## 5. Modern MLM collator pseudocode

```python
selected = random_uniform(tokens.shape) < 0.15
selected &= ~special_token_mask
labels = tokens.clone()
labels[~selected] = -100

branch = random_uniform(tokens.shape)
tokens[selected & (branch < 0.80)] = mask_id
tokens[selected & (branch >= 0.80) & (branch < 0.90)] = random_ids
#The last 10% keep the original token, and the labels are still retained.
```

## 6. Minimal fine-tuning

```python
class BertClassifier(nn.Module):
    def __init__(self, bert, hidden, classes):
        super().__init__()
        self.bert = bert
        self.classifier = nn.Linear(hidden, classes)

    def forward(self, input_ids, attention_mask, token_type_ids):
        output = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
        )
        cls = output.last_hidden_state[:, 0]
        return self.classifier(cls)
```

## 7. Verification Checklist

- tokenizer/cased configuration matches checkpoint;
- `[CLS]/[SEP]` and segment id are correct;
- padding does not enter attention and loss;
- MLM labels retain the original token;
- Calculate MLM only at 15% position;
- 10% of retained items from 80/10/10 still have tags;
- Long sequences do not exceed position embedding;
- SQuAD offset maps back to original text from WordPiece;
- fine-tuning learning rate, seed and restart strategy are documented.
