# pretraining data, tokenizer and optimization

## 1. Data source

The paper describes the training corpus as a "new mixture of publicly available sources" and does not include user data from Meta products or services. The authors removed certain websites known to contain large amounts of private individual information and upsampled highly factual sources in the hope of improving knowledge quality and reducing hallucination.

The exact corpus list and proportion of each source have not been made public. This limits external contamination audits, bias reviews, and full reproducibility.

## 2. Selection of 2T token

Llama 2 trains 2 trillion tokens at full scale. The paper states that this is a compromise between performance and cost; the training curve has not yet been significantly saturated at 2T.

Relative to Llama 1:

- 7B/13B increased from 1.0T to 2.0T;
- Large model increased from 1.4T to 2.0T;
- Context increased from 2048 to 4096.

## 3. Tokenizer

Following Llama 1’s SentencePiece BPE:

- vocabulary size is 32K;
- All numbers are broken down into single digits;
- unknown UTF-8 characters are further split into bytes;
- Reserve BOS and EOS special tokens.

Number splitting example:

\[
2026\longrightarrow 2,0,2,6.
\]

This reduces unseen number combinations, but lengthens the numerical sequence and does not automatically give the model precise arithmetic capabilities.

## 4. Optimizer and scheduling

Pretraining uses AdamW:

\[
\beta_1=0.9,
\quad
\beta_2=0.95,
\quad
\epsilon=10^{-5}.
\]

Other configurations:

- warmup 2000 steps；
- cosine learning-rate decay；
- The final learning rate is 10% of peak;
- weight decay 0.1；
- gradient clipping 1.0；
- global batch size 4M token。

The peak learning rate of 7B/13B is \(3\times10^{-4}\), and the peak learning rate of 34B/70B is \(1.5\times10^{-4}\).

## 5. Training hardware

Using Meta Research SuperCluster with in-house production clusters, both equipped with NVIDIA A100. The two clusters use InfiniBand and RoCE networks respectively, with endpoint bandwidth of 200 Gbps; the upper limit of GPU power consumption is 400W or 350W.

The paper states that RoCE can approach the scaling performance of the more expensive InfiniBand up to about 2000 GPUs, which is an empirical result at the infrastructure level.

## 6. GPU hours and carbon emission estimation

|model| GPU hours |Estimated power consumption| tCO2eq |
|---|---:|---:|---:|
| 7B | 184,320 | 400W | 31.22 |
| 13B | 368,640 | 400W | 62.44 |
| 34B | 1,038,336 | 350W | 153.90 |
| 70B | 1,720,320 | 400W | 291.42 |
|total| 3,311,616 | — | 539.00 |

Estimates do not include interconnect, non-GPU servers, cooling, and hardware manufacturing. Meta means that 100% of emissions are directly offset through sustainable items; offset does not eliminate the actual energy consumed by training.

## 7. Data analysis

fastText language recognition result is approximately:

- English 89.70%；
- unknown 8.38%, partly from code;
- Most of the remaining individual languages are below 0.2%.

The paper uses HateBERT to score 10% of random samples of the corpus, and the toxicity likelihood of about 0.2% of the documents is not less than 0.5. The author does not scrub toxic data on a large scale, for reasons including downstream generalization, avoiding demographic erasure, and making the base model usable for harmful content identification; the cost is that the base model must be additionally security tuned before deployment.

## 8. Basic model and data targets

Upsampling the source of truth, not excessively sanitizing sensitive text, and subsequent safe alignment together form the strategy. It requires a clear distinction: the basic model pursues broad coverage; the chat model then adjusts acceptable output behavior through alignment.
