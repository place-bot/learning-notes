# symbol table

|symbol|meaning|
| --- | --- |
| \(N\) |number of participants|
| \(J\) |number of items|
| \(K\) |Number of binary potential attributes|
| \(\boldsymbol R\) |\(J\) dimensional binary reaction vector|
| \(\boldsymbol r\) |a specific response pattern|
| \(\boldsymbol\alpha\) |\(K\) dimension attribute profile|
| \(p_{\boldsymbol\alpha}\) |Overall proportion of attribute profile \(\boldsymbol\alpha\)|
| \(\boldsymbol p\) |All \(2^K\) latent class proportions|
| \(Q\) |\(J\times K\) item--attribute design matrix|
| \(\boldsymbol q_j\) |Line \(j\) of Q|
| \(q_{jk}\) |Question \(j\) Is the attribute \(k\) required?|
| \(\Theta\) |\(J\times2^K\) itemresponse probability matrix|
| \(\theta_{j,\boldsymbol\alpha}\) |The positive response probability of the latent class \(\boldsymbol\alpha\) to the question \(j\)|
| \(\Gamma_{j,\boldsymbol\alpha}\) |DINA ideal response \(I(\boldsymbol\alpha\succeq\boldsymbol q_j)\)|
| \(s_j\) |DINA error probability|
| \(c_j=1-s_j\) |DINA ability type positive response probability|
| \(g_j\) |DINA non-ability category guessing probability|
| \(I_K\) |\(K\times K\) identity matrix|
| \(Q^\star\) |Remaining Q after deleting the specified structure block|
| \(Q_1,Q_2\) |Two universal holon matrices in Theorem 4|
| \(T(Q,\Theta)\) |\(2^J\times2^K\) Observable joint positive reaction moment matrix|
| \(\vartheta_Q\) |Given the free parameter space of Q|
| \(\vartheta_{\mathrm{non}}\) |Unrecognized parameter subset|
| \(\sim\) |Column permutation equivalent of Q|
| \(\succeq\) |Element-wise partial ordering|
| \(\odot\) |Element-wise product|
| \(B\) |Sparse matrix composed of G-DINA effect coefficients|
| \(\mathcal S_0\) |Non-zero support for true \(B^0\)|
| \(h^2(\eta^0,\eta)\) |Squared Hellinger distance of two response distributions|
| \(C_{\min}(\eta^0)\) |Minimum separation constant between true structure and false support|
| A |Completeness: Contains \(I_K\)|
| B |Column reciprocity for \(Q^\star\)|
| C |Repeatability: at least three 1's per column|
| D |Two non-overlapping pan-complete \(K\times K\) submatrices|
| E |Remaining \(Q^\star\) At least one 1 per column|

## Three "complete" concepts

|Name|request|
| --- | --- |
|complete|Includes one set \(I_K\)|
|double complete|Contains two sets of non-overlapping \(I_K\)|
|Pan-complete|There is a complete match of attributes to different questions; the diagonal of the corresponding square matrix can be replaced by all 1's|

## Three recognition levels

|Name|meaning|
| --- | --- |
|strict identification|Each legal parameter point is unique|
|global recognition|Except for the zero test set, it is unique in the entire parameter space|
|Local pan-recognition|Except for the zero test set, it is unique in the neighborhood of the true parameters.|
