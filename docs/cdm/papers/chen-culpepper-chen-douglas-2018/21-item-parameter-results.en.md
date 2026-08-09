# Experiment: item parameters MSE and convergence

## Figures 1--2 show what

The original text is drawn separately according to item q-vector.

\[
\operatorname{MSE}(\widehat s_j)
\quad\text{and}\quad
\operatorname{MSE}(\widehat g_j).
\]

The three symbols correspond to MH, CGibbs and unconstrained Gibbs. The horizontal axis represents 0/1 in the q-vector with open/filled circles.

Figure 1 covers:

- \(\rho=0\)；
- \(K=3,4\)；
- \(N=500,2000\)；
- slipping and guessing.

Figure 2 covers:

- \(K=3\)；
- \(\rho=.05,.25\)；
- \(N=500,2000\)；
- slipping and guessing.

## Overall result

The order given in the original article is:

\[
\text{CGibbs MSE usually lowest},
\qquad
\text{Unconstrained Gibbs MSE is usually the highest}.
\]

The recovery of item parameters by constrained MH and CGibbs is generally better than that of unconstrained methods.

## Specific mode

The author points out:

- When \(K=3,N=2000,\rho=0\), the guessing MSE of unconstrained Gibbs for single-attribute questions is particularly large;
- When \(K=4\), the slipping MSE of unconstrained Gibbs is larger;
- The restricted method still maintains a low MSE under the relevant attribute conditions of \(\rho=.05,.25\).

## Explanation

Unconstrained Gibbs can access states not recognized by Q. At this time, different item parameter groups may correspond to the same observation distribution, and the posterior average spans multiple modes, increasing MSE. The restricted method allows each Q sample to meet the identification design, and the item parameters have a more stable correspondence.

## Report boundary of graphic result

The paper only presents the question-by-question MSE in figures, without accompanying numerical tables or data files to generate figures. This site retains the relative conclusions reported by the author, does not approximate digitization of low-resolution figures, and does not fabricate question-by-question decimals.

## Acceptance rate comparison

Pre-experiment report:

|propose|acceptance rate|
| --- | ---: |
|independent proposal| \(<0.5\%\) |
| DS1 | \(<5\%\) |
| DS2 | \(18\%\)--\(25\%\) |

Formal simulation uses \(B=2K\), with an acceptance rate of approximately 20%.

## Geweke Convergence Diagnostics

The author is right

\[
-2\log p(
\boldsymbol Y,\Theta)
\]

Use Geweke diagnostics and check for 15,000--30,000 iterations.

Reported at \(N=4000\):

| \(K\) | MH Z | CGibbs Z |
| ---: | ---: | ---: |
| 3 | -0.218 | -0.628 |
| 4 | -1.36 | -0.705 |

The authors accordingly conclude that there is no evidence against convergence of the joint posterior chain.

## Diagnostics still not covered

The four Z values only cover the joint posterior scalar for the two large sample conditions. They are not checked one by one:

- each \(q_{jk}\);
- Jump to different Q modes;
- The effective sample size of \(s_j,g_j,\pi_c\);
- Initial value sensitivity of multiple chains;
- Q Is the mode stable?

Modern reproduction should add multi-chain, R-hat, ESS, Q-mode frequency trajectories and chain length sensitivity.

[Next page: Experiment—Fraction Subtraction Data and Analysis Design](22-fraction-data.md)
