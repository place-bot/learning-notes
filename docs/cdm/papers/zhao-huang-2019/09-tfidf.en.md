# TF--IDF item vector

## 1. Goal

After filtering the top-\(k\) words, you need to turn each question into a value vector:

\[
\boldsymbol x_j
=
(x_{j1},\ldots,x_{jk}).
\]

The paper uses term frequency--inverse document frequency.

## 2. Term Frequency

Suppose feature \(r\) appears \(c_{jr}\) times in question \(j\). The simplest word frequency is

\[
\operatorname{tf}_{jr}=c_{jr}.
\]

Logarithmic scaling can also be used:

\[
\operatorname{tf}_{jr}
=
\begin{cases}
1+\log c_{jr},&c_{jr}>0,\\
0,&c_{jr}=0.
\end{cases}
\]

The paper did not specify the specific version.

## 3. Inverse Document Frequency

Suppose the training set has \(n\) questions, and feature \(r\) appears in \(df_r\) questions. A common definition is

\[
\operatorname{idf}_r
=
\log\frac{n}{df_r}.
\]

scikit-learn has smoothing by default:

\[
\operatorname{idf}_r
=
\log\frac{1+n}{1+df_r}+1.
\]

## 4. TF--IDF weight

\[
x_{jr}
=
\operatorname{tf}_{jr}
\operatorname{idf}_r.
\]

Features that appear frequently in the current question and rarely in other questions receive higher weights.

## 5. Vector normalization

scikit-learn often performs L2 normalization on each question:

\[
\widetilde{\boldsymbol x}_j
=
\frac{\boldsymbol x_j}
{\|\boldsymbol x_j\|_2}.
\]

This will allow long questions and short questions to have similar overall measurement scales.

## 6. Differences in responsibilities from information gain

|components|Answered questions|
| --- | --- |
|information gain|Which words are most useful for category distinction?|
| TF--IDF |How much weight should a certain reserved word have in the current question?|

Information gain uses tags; TF--IDF uses word frequency and document frequency.

## 7. Fitting range

Vocabulary and IDF should only be determined by the training set:

\[
\widehat{\operatorname{idf}}_r
=
\log
\frac{1+n_{\mathcal T}}
{1+df_{r,\mathcal T}}
+1.
\]

The validation set and test set only call `transform`.

## 8. The paper does not report details

- `TfidfVectorizer` is still calculated manually;
- `smooth_idf`；
- `sublinear_tf`；
- `norm`；
- `min_df/max_df`；
- Unregistered word processing;
- Should I do IG first or TF--IDF first?

These gaps make value-by-value replication impossible.
