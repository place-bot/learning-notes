# Summary and further reading

## A main line

\[
Y,Q_0
\longrightarrow
\widehat P(\boldsymbol\alpha_i\mid\boldsymbol Y_i)
\longrightarrow
\widehat w_l,\widehat p_{jl}
\longrightarrow
\widehat{\varsigma}_j^2(\boldsymbol q)
\longrightarrow
\operatorname{PVAF}
\longrightarrow
\text{The simplest suggestion q-vector}.
\]

## Five core formulas

### Complete mode success probability

\[
\widehat p_{jl}
=
\frac{\sum_i\tau_{il}Y_{ij}}
{\sum_i\tau_{il}}.
\]

### Folding success probability

\[
p_j(G)
=
\frac{\sum_{\boldsymbol\alpha\in G}
w(\boldsymbol\alpha)p_j(\boldsymbol\alpha)}
{\sum_{\boldsymbol\alpha\in G}w(\boldsymbol\alpha)}.
\]

### GDI

\[
\varsigma_j^2(\boldsymbol q)
=
\sum_Gw(G)[p_j(G)-\bar p_j]^2.
\]

### Main Theorem

\[
\varsigma_j^2(\boldsymbol q)
\le
\varsigma_j^2(\boldsymbol q^*).
\]

### PVAF

\[
\operatorname{PVAF}_j(\boldsymbol q)
=
\frac{\widehat{\varsigma}_j^2(\boldsymbol q)}
{\widehat{\varsigma}_j^2(\boldsymbol1)}.
\]

## The most important logic

Missing valid attributes merges categories with different success probabilities:

\[
\frac{w_0w_1}{w_0+w_1}(p_0-p_1)^2
\]

This inter-group variation disappears with folding.

Adding extraneous attributes only subdivides the homogeneous group and the GDI remains unchanged. From this:

\[
\text{Maximum GDI}
+
\text{Minimum attributes}.
\]

## Original evidence

|evidence|Conclusion|
| --- | --- |
| Table 1 |The correct vector is juxtaposed with the added vector, and the missing vector has a smaller GDI.|
| Study 1 |Correct Q is highly retained under five reduction models, and most errors are corrected.|
| Study 2 |Recovery is more difficult under unconstrained G-DINA|
|Fraction subtraction|8/11 reserved, 3/11 recommended to delete simplified attributes|
|2017 Comments and Responses|Initial Q, fixed thresholds and consistency still require additional theory|

## 2008 and 2016 positions

|Paper|main object|key indicators|
| --- | --- | --- |
| de la Torre (2008) |DINA Q Verification| \(\delta=1-s-g\) |
| de la Torre & Chiu (2016) |G-DINA Family Q Verification|\(\varsigma^2\) and PVAF|

The 2016 method retains the idea of "using student posterior expectation count to re-evaluate candidate Q" and extends the two-group distinction to multi-group variance.

## Practical usage checklist

1. Explain the source of provisional Q;
2. Fit saturated G-DINA;
3. Check the posterior category sparsity;
4. Report GDI/PVAF path;
5. Make \(\varepsilon\) sensitivity;
6. Compare single and iterative suggestions;
7. Refit the suggestion Q;
8. Check model fit and classification stability;
9. Topic-by-topic review by experts in the field;
10. Keep uncertain candidates.

## Next article

[Liu, Xu & Ying (2012)：Data-driven Learning of Q-matrix](../liu-xu-ying-2012/index.md)

Reading highlights:

- From “verifying a generally credible Q” to “data-driven learning of Q”;
- How to define the objective function;
- How to search and update;
- What guarantees are provided for initial values, identifiability and consistency;
- How the candidate evaluation differs from GDI/PVAF.

## Interface with CAT

Q Verify the quality of the item bank attribute label. CAT then uses this structure to update the student's status in real time and select the next question:

\[
\text{validated Q}
\rightarrow
\text{posterior update}
\rightarrow
\text{item utility}
\rightarrow
\text{next item}.
\]

This chain illustrates that Q errors propagate all the way to adaptive decision.
