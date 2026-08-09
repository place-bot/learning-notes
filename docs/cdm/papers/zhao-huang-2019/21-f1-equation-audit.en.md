# weighted F1 audit of Equation (9)

## 1. Original text variable

Thesis definition:

- \(p_O\): The number of questions predicted to be O;
- \(tp_O\): the number of questions in which the true value is O;
- \(fp_O\): the number of questions in which the true value is M;
- \(t_O\): Total number of real O questions.

The same applies to category M.

So

\[
p_O=tp_O+fp_O.
\]

## 2. Original text printing formula

Equation (9) is

\[
F1
=
\frac{tp_O+fp_O}{t_O+t_M}F1_O
+
\frac{tp_M+fp_M}{t_O+t_M}F1_M.
\]

Substitute \(p_c\):

\[
F1_{\text{Eq.9}}
=
\frac{p_O}{N}F1_O
+
\frac{p_M}{N}F1_M.
\]

It is weighted by **predicted class size**.

## 3. Definition of scikit-learn

`f1_score(..., average="weighted")` uses real support:

\[
F1_{\text{sklearn}}
=
\frac{t_O}{N}F1_O
+
\frac{t_M}{N}F1_M.
\]

The two formulas are only available in

\[
p_O=t_O,
\qquad
p_M=t_M
\]

times are equal.

## 4. Verify with compatible confusion matrix

Consider:

|real\prediction| O | M |
| --- | ---: | ---: |
| O | 60 | 7 |
| M | 5 | 9 |

Get:

\[
t_O=67,\quad t_M=14,
\]

\[
p_O=65,\quad p_M=16.
\]

The standard weighted F1 is

\[
85.57\%\approx85.6\%.
\]

Equation (9) gives

\[
84.80\%.
\]

85.6% of the tables are consistent with the standard definition and incompatible with the printed formula.

## 5. all-O counterexample

If all questions are predicted to be O:

\[
p_O=N,\qquad p_M=0.
\]

Equation (9) degenerates into

\[
F1_{\text{Eq.9}}=F1_O=90.55\%.
\]

This would make the F1 of the constant prediction majority class higher than the paper's best 85.6%, which obviously deviates from the common purpose of weighted F1 to combine the performance of the two classes.

The standard weighted result is:

\[
F1_{\text{sklearn}}=74.92\%.
\]

## 6. Most likely explanation

The paper explains that the experiment was completed using sklearn. Combining 85.6% with the compatible confusion matrix, a more reasonable inference is:

1. The actual calculation uses sklearn’s support-weighted F1;
2. Equation (9) miswrites the true support in the weight as the predicted quantity.

This is an inference based on numerical consistency, and neither the source code nor the prediction files are made public.

## 7. Processing when referencing result

You can cite 85.6% of the table and indicate:

> The Equation (9) printed in the paper is inconsistent with the definition of scikit-learn weighted F1; the table value is closer to the latter.

## 8. Website code

[`zhao_huang_2019_audit.py`](https://github.com/place-bot/Psychometrics-and-R-Shiny/blob/main/tools/zhao_huang_2019_audit.py) Implements two definitions at the same time and outputs a compatible confusion matrix.
