# Intensive reading of official simulation code

## 1. Main text Figure 1

`id_Q_DINA_basis_Q42.m` and `get_Q24_nonid.m` construct multiple equivalent DINA parameters for four questions and two attributes, calculate the marginal probabilities of 16 reaction modes, and draw parameter and probability comparisons.

The code fixes the random seed to reproducibly construct the path.

## 2. Main text Figures 2--3

`get_Q24_single_MSE.m` is the core function:

- 100 sets of true parameters;
- 200 reps per set;
- 10 EM initial values each time;
- The maximum likelihood initial value wins;
- Returns the average element-wise MSE of \(\boldsymbol p,\boldsymbol c,\boldsymbol g\).

`Q24_MSE_main.m` is closer to the analysis draft:

- First call `get_MSE` that does not exist in the warehouse;
- Use workspace variables such as `p_mse100` before loading the result file;
- Load `MSE_*.mat` in the second half;
- These precomputed MSE files are not included in the repository.

The function signature of `get_Q24_final_MSE.m` has no parameters, but the undefined `N` is used in the function body. To run directly, you need to change the signature to

```matlab
function [] = get_Q24_final_MSE(N)
```

Or define sample size within the function.

## 3. DINA exhaustive

`exhaus_dina.m`：

1. Get true Q from `Q_aa.mat`;
2. Generate Dirichlet latent class proportion and \(c,g\);
3. Generate \(N=10^5\) data;
4. Conduct 5 random initial value EMs on 121 Q cards;
5. Save the best log-likelihood of each Q.

`get_cg.m` implements DINA EM. The stopping condition only checks the parameter difference:

```matlab
while (max(abs(old_c-c_i))+max(abs(old_g-g_i)))>1e-6
```

There is no maximum iteration protection. Long runs are possible with extreme data or value stagnation.

`exhaus_dina_main.m` is responsible for reading in the precomputed `.mat` and drawing. The warehouse does not include these output files, and the default file names also need to be modified by the user according to the scenario.

## 4. G-DINA exhaustive

The process of `exhaus_gdina.m` is similar to DINA:

- 5 random initial values;
- G-DINA EM up to 5000 times;
- The convergence thresholds are \(\Theta\) element absolute change and \(10^{-5}\);
- Check monotonicity after fitting;
- Save strongly monotonic candidate markers.

`get_GDINAprob_mono.m` First execute unconstrained EM, and then check whether the result satisfies monotonicity. It does not impose monotonic constraints in each M-step, so "failed" candidates are filtered by the drawing program.

## 5. Study VII

`id_Q_GDINA_attr2_K3.m` and `id_Q_GDINA_attr2_K5.m`:

- construct true Q with substitution \(\bar Q\);
- Generate perturbations with random seed numbers;
- Check probability ranges and monotonicity;
- Take the first 70 legal seeds;
- Enumerate the complete response probability and calculate the maximum difference.

K=3 At the end of the file, the result is saved as a file name containing `K5`, which is a naming typo. The Figure numbering at the top of the file also retains the earlier version number and is inconsistent with Figures 11--12 of the final supplementary material.

## 6. Recurrence threshold

Code dependencies:

- MATLAB；
- `gamrnd` in Statistics and Machine Learning Toolbox;
- Share the current directory and `.mat` file between multiple scripts;
- Precomputed result files and manually selected plot entries.

The warehouse is sufficient for intensive reading of algorithms and re-running core functions. It has not yet formed a single command pipeline to execute all seven groups of studies from scratch.
