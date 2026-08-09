# symbol table

## Dimensions and individuals

|symbol|meaning|
| --- | --- |
| \(N\) |Number of students|
| \(m\) |number of items|
| \(k\) |Number of attributes|
| \(r\) |student index|
| \(i,h\) |item index|
| \(j\) |Property index|

## Potential properties and reactions

|symbol|meaning|
| --- | --- |
| \(\boldsymbol A\) |A \(k\) dimensional binary attribute profile|
| \(A^j\) |Whether to master the attribute \(j\)|
| \(\boldsymbol A_r\) |Attribute profile of student \(r\)|
| \(\boldsymbol R\) |A \(m\) dimensional binary reaction vector|
| \(R^i\) |Response to question \(i\)|
| \(\boldsymbol R_r\) |Response vector of student \(r\)|
| \(\xi^i\) |Whether it has all the attributes required by question \(i\)|

## Q and sets

|symbol|meaning|
| --- | --- |
| \(Q\) |True \(m\times k\) Q matrix|
| \(Q'\) |Universal Candidate Q|
| \(Q_{ij}\) |Does question \(i\) require the attribute \(j\)?|
| \(\boldsymbol q_i\) |Line \(i\) of Q|
| \(Q\sim Q'\) |The only difference between the two Qs is attribute column substitution.|
| \(Q\not\sim Q'\) |Two Qs do not belong to the same column permutation equivalence class|
| \(\mathcal R_Q\) |The set of row vectors Q|
| \(I_i\) |Question \(i\) is responding to the event|
| \(\wedge\) |Multiple positive response events occur simultaneously|

## Attribute distribution

|symbol|meaning|
| --- | --- |
| \(p_{\boldsymbol A}^*\) |The probability of attribute profile \(\boldsymbol A\) in the population|
| \(p_{\boldsymbol0}^*\) |All-zero attribute profile probability|
| \(\boldsymbol p^*\) |All non-zero attribute profile probability vectors|
| \(\boldsymbol p_0^*\) |Complete probability vector containing all-zero patterns|
| \(\widehat p_{\boldsymbol A}\) |Proportion of pattern \(\boldsymbol A\) in sample|
| \(\widetilde{\boldsymbol p}\) |Attribute distribution estimates derived from moment distance|

## T-matrix and empirical moment

|symbol|meaning|
| --- | --- |
| \(B_Q(I_i)\) |Row vector of ideal abilities for a single question|
| \(B_Q(I_{i_1}\wedge\cdots)\) |Row vector of ideal abilities for question set|
| \(\Upsilon\) |Element-wise vector multiplication|
| \(T(Q)\) |Noiseless T-matrix, columns exclude all-zero patterns|
| \(\boldsymbol\alpha\) |Experience joint correct answer rate vector|
| \(N_{I_{i_1}\wedge\cdots}\) |The number of people who answered all questions correctly|
| \(\mathcal C(M)\) |column space of matrix M|
| \(\mathcal R_M\) |the set of row vectors of matrix M|

## DINA parameters and matrices

|symbol|meaning|
| --- | --- |
| \(s_i\) |Probability of error when capable|
| \(c_i=1-s_i\) |Probability of being correct when you have the ability|
| \(g_i\) |Correct probability when not having ability|
| \(\boldsymbol c,\boldsymbol g\) |Parameter vectors of all items|
| \(D_c\) |By question group \(c_i\) Diagonal matrix composed of products|
| \(T_c(Q)\) |Guess-free, error-containing T-matrix|
| \(T_{c,g}(Q)\) |Non-zero pattern T-matrix with errors and guesses|
| \(\boldsymbol g_{\mathrm{joint}}\) |Guess probability column for each question group in all-zero mode|
| \(\widetilde T_{c,g}(Q)\) |Augmented matrix with all-zero pattern columns and probability sum rows|
| \(T_{c-g}(Q)\) |Guess-free matrix with row scaling parameter \(c_i-g_i\)|
| \(D\) |Row transformation matrix that eliminates known guess baselines|

## Estimators and conditions

|symbol|meaning|
| --- | --- |
| \(S(Q')\) |Profile moment distance of candidate Q without noise|
| \(S_{c,g}(Q')\) |Profile moment distance of candidate Q under DINA|
| \(\widehat Q\) |Noise-free Q estimate|
| \(\widehat Q(c,g)\) |Given the Q estimate of \(c,g\)|
| \(\widetilde c(Q,g)\) |General estimate for optimization of all \(c\) profiles|
| \(\overline c_i(Q,g)\) |Moment estimation based on question group inclusion relationship|
| \(\widehat c(Q,g)\) |Combination of moment estimation and profile estimation|
| \(\widehat Q_{\widehat c}(g)\) |Q estimate for known g, unknown c|
| C1 |Q complete|
| C2 |T saturated|
| C3 |attribute profile independent and identically distributed|
| C4 |The probability of all attribute profiles is strictly positive|
| C5 |Each attribute is required by at least two questions|

## Three sets of symbols that are easily confused

### \(\boldsymbol A\) and \(\boldsymbol\alpha\)

\(\boldsymbol A\) is the potential attribute profile of a single student; \(\boldsymbol\alpha\) is the joint answer rate vector calculated for all samples.

### \(p_{\boldsymbol0}\) and \(\boldsymbol p\)

\(p_{\boldsymbol0}\) is a scalar; \(\boldsymbol p\) stacks all non-zero attribute profile probabilities.

### \(T_{c,g}\) and \(\widetilde T_{c,g}\)

\(T_{c,g}\) contains only non-zero pattern columns; \(\widetilde T_{c,g}\) also contains an all-zero pattern guess column and a final all-1 constraint row.

[Next page: Summary and follow-up reading](28-summary.md)
