# Independent code reconstruction: strict separation of training, verification and testing

## 1. File

This site provides:

[`tools/zhao_huang_2019_reimplementation.py`](https://github.com/place-bot/Psychometrics-and-R-Shiny/blob/main/tools/zhao_huang_2019_reimplementation.py)

It is a modern reproducible pipeline reconstructed from the paper description, without using the author's data or source code.

## 2. Input format

UTF-8 CSV：

```csv
text,label
"Calculate the sum of 38 and 17.","O"
"Choose the correct quantitative relationship according to the chart.","M"
```

At least two categories and 20 questions are required.

## 3. Data partitioning

Code first:

```python
train_test_split(
    texts,
    labels,
    test_size=0.20,
    random_state=seed,
    stratify=labels
)
```

Then divide the 20% temporary set equally into validation set and test set. This results in a tier split close to 80/10/10.

## 4. Chinese tokenization

```python
" ".join(jieba.lcut(text))
```

The space string after tokenization is given to `TfidfVectorizer`. Explicit setting:

```python
tokenizer=str.split
lowercase=False
ngram_range=(1, ngram_max)
```

## 5. Anti-leakage TF--IDF

```python
x_train = vectorizer.fit_transform(train_x)
x_validation = vectorizer.transform(validation_x)
x_test = vectorizer.transform(test_x)
```

Vocabulary and IDF are only fitted by the training set.

## 6. Information gain reconstruction

The paper explains IG as information between discrete variables. This site first converts TF--IDF into an occurrence matrix:

\[
z_{jr}=\mathbb I(x_{jr}>0),
\]

Then use:

```python
mutual_info_classif(
    occurrence,
    y_train,
    discrete_features=True,
    random_state=seed
)
```

Sorting also only uses training labels.

## 7. Model mapping

|Paper title|This site realizes|
| --- | --- |
| LR + L2 | `LogisticRegression(penalty="l2", solver="liblinear")` |
| C-SVM | `LinearSVC(C=1, loss="squared_hinge")` |
| Gaussian NB | `GaussianNB()` |

Gaussian NB requires dense input. Since up to 300 dimensions are retained after filtering, the memory size is controllable.

## 8. Selection of \(k\)

Yes

\[
k=5,10,\ldots,300
\]

Calculate the validation set standard weighted F1 and retain the \(k\) with the highest score.

If there are less than 300 vocabulary, the search stops at all available features.

## 9. Final output

Each model reports:

- `selected_k`；
- validation weighted F1；
- test accuracy；
- test weighted F1；
- test macro-F1；
- test balanced accuracy；
- precision/recall/F1 per category;
- top 30 mutual information features.

## 10. Operation mode

```bash
python -m pip install jieba numpy scipy scikit-learn
python tools/zhao_huang_2019_reimplementation.py items.csv \
  --seed 2019 \
  --output zhao_huang_report.json
```

## 11. Improvements over the paper

- All random steps have seeds;
- All model parameters are explicit;
- train/validation/test handles strict separation;
- Added category imbalance indicator;
- Save machine-readable JSON;
- Output the final \(k\) and keywords;
- Can be replaced with your own multi-category data.

## 12. Still need data level work

The script works, but cannot generate the raw numbers for Tables 1--3 of the paper because the 805 questions and their labels are not publicly available.
