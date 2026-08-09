# Finite sample error bound

## 1. Idealization of identification analysis

The identification problem assumes that the complete population response distribution is known. The actual data is only

\[
\boldsymbol R_1,\ldots,\boldsymbol R_N.
\]

The paper further gives an exponential bound on the finite sample error probability in Discussion.

## 2. Sparse B parameterization

Generally, RLCM can write the item probability as main effect and interaction effect:

\[
\theta_{j,\boldsymbol\alpha}
=
\sum_{S\subseteq\{1,\ldots,K\}}
\beta_{j,S}
\prod_{k\in S}\alpha_k.
\]

Arrange all \(\beta_{j,S}\) into matrix \(B\). Q specifies which effects are allowed to be non-zero, so identifying Q can be translated into identifying the non-zero support of \(B\):

\[
\mathcal S_0=\operatorname{supp}(B^0).
\]

## 3. Separation constant

For support \(\mathcal S\ne\mathcal S_0\) and

\[
|\mathcal S|\le|\mathcal S_0|,
\]

Compare the Hellinger distance of the candidate distribution to the true distribution. Thesis definition

\[
C_{\min}(\eta^0)
=
\inf_{\substack{\mathcal S\ne\mathcal S_0\\
|\mathcal S|\le|\mathcal S_0|}}
\frac{h^2(\eta^0,\eta)}
{|\mathcal S_0\setminus\mathcal S|}.
\]

It measures the minimum probability separation between true structures and false sparse structures.

## 4. Proposition 4

If true Q satisfies the sufficient conditions for strict joint identification, then there exists

\[
c_0>0
\]

make

\[
C_{\min}(\eta^0)\ge c_0.
\]

For the joint MLE \(\hat\eta\) with support constraint \(L_0\) and the oracle MLE \(\hat\eta^0\) with known true Q,

\[
\Pr(\hat Q\nsim Q^0)
\le
\Pr(\hat\eta\ne\hat\eta^0)
\le
c_2\exp\{-c_1NC_{\min}(\eta^0)\}.
\]

## 5. Explanation

Strict identification leads to a positive separation between false and true structures:

\[
\text{structural error probability}
\lesssim
e^{-cN}.
\]

When recognition fails,

\[
C_{\min}=0,
\]

The upper bound degenerates to \(O(1)\), and increasing the sample size cannot guarantee that erroneous structures will be eliminated.

## 6. Pan-recognition nearby

The \(C_{\min}\) of a general recognition parameter point depends on its distance to the unrecognizable zero measurement set. When the distance approaches 0,

\[
C_{\min}\downarrow0,
\]

The \(N\) required to achieve the same accuracy increases.

This is completely consistent with the four-question two-attribute simulation: close

\[
p_{00}p_{11}=p_{01}p_{10}
\]

has slower MSE convergence.

## 7. Boundaries

This proposition provides a theoretical probability bound, but does not give \(c_1,c_2,c_0\) that can be directly calculated, nor does it convert it into a sample size formula. It connects "overall uniqueness" and "limited sample structure recovery" and does not replace specific algorithm analysis.
