# Table 1 Complete hand calculation and typography errors in the original text

## Settings

\[
K=4,
\qquad
\boldsymbol q^*=1110.
\]

item really needs the first three attributes. Only when the first three attributes are fully mastered, the success probability is \(.725\), and the rest are \(.225\).

Table 1 gives the weights of the 16 complete patterns. After collapsing attribute 4:

| \(\boldsymbol\alpha_{1:3}\) |weight|Probability of success|
| --- | ---: | ---: |
| \(000-\) | .090 | .225 |
| \(100-\) | .157 | .225 |
| \(010-\) | .112 | .225 |
| \(001-\) | .112 | .225 |
| \(110-\) | .125 | .225 |
| \(101-\) | .130 | .225 |
| \(011-\) | .137 | .225 |
| \(111-\) | .137 | .725 |

## Collapse a group

Pattern \(000-\) merges \(0000\) with \(0001\):

\[
w(000-)
=
.053+.037
=
.090.
\]

\[
\begin{aligned}
p(000-)
&=
\frac{.053(.225)+.037(.225)}
{.053+.037}\\
&=.225.
\end{aligned}
\]

## Original typography error

The denominator of this equation is printed on page 259 of the official PDF.

\[
.225+.225.
\]

The denominator should consist of the two mode weights:

\[
.053+.037.
\]

Both the in-table merge weight \(.090\) and the final probability \(.225\) support this correction.

## Correct GDI for q-vector

Overall average success rate:

\[
\bar p
=
.225(1-.137)+.725(.137)
=
.2935
\approx .294.
\]

\[
\begin{aligned}
\varsigma^2_{1:3}
&=
\sum w(\boldsymbol\alpha_{1:3})
p^2(\boldsymbol\alpha_{1:3})
-\bar p^2\\
&\approx .116-.294^2\\
&=.030.
\end{aligned}
\]

Using the cell-by-cell calculation of the original table without rounding, the script on this site obtains:

\[
\varsigma^2_{1:3}=0.029558.
\]

## Add attributes

Candidate \(1111\) Divides each homogeneous group into two groups according to attribute 4. The subgroup success probabilities remain the same, so

\[
\varsigma^2_{1:4}
=
\varsigma^2_{1:3}
=
0.029558.
\]

The maximum GDI itself cannot distinguish between \(1110\) and \(1111\), and the simplest rule selects \(1110\).

## Simultaneous omission and addition

Candidate \(0111\) omits the really required attribute 1 and adds irrelevant attribute 4. Table 1 gives the folding success probability:

\[
.225,\ .225,\ .225,\ .225,\ .492,\ .225,\ .225,\ .456.
\]

This site calculates grid by grid:

\[
\varsigma^2_{2:4}=0.012524\approx .013.
\]

Omitted attributes Averaging several \(.225\) and \(.725\) categories, the differences between groups are significantly reduced.

## Runnable verification

```bash
python3 tools/de_la_torre_chiu_2016_gdi_validation.py --demo-only
```

Core output:

```text
correct q=1110 GDI=0.029558
overspecified q=1111 GDI=0.029558
under+over q=0111 GDI=0.012524
selected at epsilon=0.950: q=1110
```
