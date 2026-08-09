# Objective function and implementation ambiguity of C-SVM

## 1. Decision hyperplane

Binary classification labels

\[
y_j\in\{-1,+1\},
\]

Linear SVM usage

\[
f(\boldsymbol x_j)
=
\boldsymbol w^\top\boldsymbol x_j+b.
\]

Predicted to be

\[
\widehat y_j
=
\operatorname{sign}
\left(
\boldsymbol w^\top\boldsymbol x_j+b
\right).
\]

## 2. Objective function for paper printing

The original Equation (2) is

\[
\min_{\boldsymbol w,b,\boldsymbol\xi}
\left\{
\frac12\boldsymbol w^\top\boldsymbol w
+
\frac C2\sum_{j=1}^{n}\xi_j^2
\right\}
\]

satisfy

\[
y_j
\left(
\boldsymbol w^\top\boldsymbol x_j+b
\right)
\ge 1-\xi_j,
\]

\[
\xi_j\ge0.
\]

This is an L2 slack / squared-hinge style soft-margin linear SVM.

## 3. The role of \(C\)

\[
C\uparrow
\]

It will increase the cost of violating the interval constraint and tend to fit the training data better;

\[
C\downarrow
\]

The relative constraints on \(\|\boldsymbol w\|_2\) will be strengthened.

The paper uses \(C=1\) and says it is a common value in applications.

## 4. Why linear SVM is commonly used in text classification?

The TF--IDF vector has:

- high dimensionality;
- sparse;
- A large number of local keywords;
- Categories can often be distinguished by linear combinations.

Linear SVM can directly learn the positive and negative weights of each word and has low computational cost.

## 5. Implementation ambiguity in the original text

The author says "use sklearn default parameters", but does not specify the class name:

- `sklearn.svm.SVC` usually defaulted to the RBF kernel at the time;
- `sklearn.svm.LinearSVC` is closer to the linear squared hinge target for paper printing.

There are obvious differences in the models, computational complexity and prediction results between the two.

## 6. Choice of website reconstruction

Independent implementation uses:

```python
LinearSVC(
    C=1.0,
    loss="squared_hinge",
    random_state=2019
)
```

The reason is that it has the closest structure to Equation (2). This choice is a reconstruction decision, and the author's specific call cannot be determined based on this.

## 7. Paper result

The best accuracy of SVM under the three feature ranges is:

|Features|Have IG|Full features|
| --- | ---: | ---: |
| unigram | 74.3% | 71.1% |
| unigram+bigram | 74.9% | 71.1% |
| unigram+bigram+trigram | 74.9% | 71.3% |

IG brings improvements of 3.2, 3.8, and 3.6 percentage points.

## 8. Unreported diagnostics

The paper does not give:

- Verification curve of \(C\);
- Number of support vectors;
- Category weight;
- Word weight;
- confusion matrix;
- Minority class recall.

Therefore, it is impossible to determine which category the SVM's 74% accuracy mainly comes from.
