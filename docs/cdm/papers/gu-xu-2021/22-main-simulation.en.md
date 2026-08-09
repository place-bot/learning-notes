#Experiment: Main text pan-recognition simulation

## 1. Goal

Main text Section 3.1 Use

\[
Q=
\begin{pmatrix}
1&0\\
0&1\\
1&0\\
0&1
\end{pmatrix}
\]

Show three things:

1. There are multiple sets of completely equivalent parameters on the zero test set;
2. MLE outside the zero measurement set converges as the sample size increases;
3. The convergence slows down significantly when approaching the zero measurement set.

## 2. Scenario (a): Exactly unrecognizable

settings

\[
s_j=g_j=0.2,\qquad j=1,\ldots,4,
\]

\[
\boldsymbol p=(0.25,0.25,0.25,0.25).
\]

At this time

\[
p_{01}p_{10}=p_{00}p_{11}.
\]

The author constructs another two sets of legal DINA parameters according to the proof of Theorem 2(b.2). Figure 1(a) shows that the three sets of parameters are obviously different, and Figure 1(b) shows that the 16 reaction mode probabilities completely overlap.

## 3. Scenario (b): Random parameters

Generate \(B=100\) group true parameters:

\[
s_j\sim U(0.1,0.3),
\qquad
g_j\sim U(0.1,0.3),
\]

\[
\boldsymbol p\sim
\operatorname{Dirichlet}(3,3,3,3).
\]

Official code actually used

\[
c_j=1-s_j\sim U(0.7,0.9).
\]

## 4. sample size and repetition

For each set of true parameters, in each

\[
N\in\{10^2,10^3,10^4,10^5\}
\]

200 independent data sets are generated.

The total number of fittings is

\[
100\times4\times200=80,000
\]

data set. Each data set then runs EM with 10 random initial values, so the number of candidate EM runs reaches

\[
800,000.
\]

## 5. Estimates and Indicators

The EM solution with the largest log likelihood is retained for each data set. For a set of true parameters, calculate the average element-wise squared error for 200 repetitions:

\[
\operatorname{MSE}(\hat{\boldsymbol p})
=
\frac{1}{200\cdot2^K}
\sum_{b=1}^{200}
\|\hat{\boldsymbol p}^{(b)}-\boldsymbol p\|_2^2,
\]

\[
\operatorname{MSE}(\hat{\boldsymbol c})
=
\frac{1}{200J}
\sum_{b=1}^{200}
\|\hat{\boldsymbol c}^{(b)}-\boldsymbol c\|_2^2,
\]

\[
\operatorname{MSE}(\hat{\boldsymbol g})
=
\frac{1}{200J}
\sum_{b=1}^{200}
\|\hat{\boldsymbol g}^{(b)}-\boldsymbol g\|_2^2.
\]

Figure 2 draws a boxplot of MSE for 100 sets of true parameters.

## 6. result

As \(N\) increases from \(10^2\) to \(10^5\), the bins and medians of the three types of MSE shrink toward 0, supporting widespread identification and consistent estimation outside the zero measurement set.

The boxplots still contain slowly converging outliers. In Figure 3, the 20% of parameter settings with the largest \(\boldsymbol p\) MSE at \(N=10^5\) are marked in red; these red points lie closer to

\[
p_{00}p_{11}=p_{01}p_{10}
\]

the corresponding diagonal.

## 7. How to interpret result

Experiments support "recognition difficulty has a continuous gradient":

\[
\left|
p_{00}p_{11}-p_{01}p_{10}
\right|
\downarrow
\quad\Longrightarrow\quad
\text{Limited sample MSE rises}.
\]

The paper does not report a numerical table for each boxplot, so the results that can be accurately quoted are the trend, outlier proportion, and experimental settings.
