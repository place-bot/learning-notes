# PPO, combination rewards and KL constraints

## 1. Policy optimization goal

prompt \(p\sim\mathcal D\), answer \(g\sim\pi_\theta(\cdot\mid p)\). The ideal goal is to:

\[
\max_\pi
\mathbb E_{p,g}
[R(g\mid p)].
\]

Rewards come from trained RMs, and you don’t have to ask people to grade them on the spot every time.

## 2. Choice of Helpfulness and Safety

First define the combination reward:

\[
R_c(g\mid p)=
\begin{cases}
R_s(g\mid p),
&\operatorname{is\_safety}(p)
\ \text{or}\ R_s(g\mid p)<0.15,\\
R_h(g\mid p),&\text{otherwise}.
\end{cases}
\]

The threshold 0.15 corresponds to precision 0.89 and recall 0.55 on the Meta Safety test set. Safety rewards are given priority when the potential danger prompt or safety score is very low.

## 3. Reward whitening

The paper first performs inverse logit transformation and whitening on \(R_c\):

\[
\widetilde R_c
=
\operatorname{whiten}
\left(
\operatorname{logit}(R_c)
\right).
\]

The purpose includes balancing the reward scale, improving PPO stability, and making it more consistent with the KL penalty value.

## 4. KL constraints

Final reward:

\[
R(g\mid p)
=
\widetilde R_c(g\mid p)
-
\beta D_{\mathrm{KL}}
\left(
\pi_\theta(\cdot\mid p)
\parallel
\pi_0(\cdot\mid p)
\right).
\]

\(\pi_0\) is the original reference policy. KL penalty prevents the policy from excessively deviating from the readable language distribution in pursuit of high RM scores, reducing training instability and reward hacking.

## 5. PPO clipped objective

Let old policy be \(\pi_{\mathrm{old}}\), token action ratio:

\[
\rho_t(\theta)
=
\frac{
\pi_\theta(a_t\mid s_t)
}{
\pi_{\mathrm{old}}(a_t\mid s_t)
}.
\]

PPO uses:

\[
\mathcal L_{\mathrm{PPO}}
=
-\mathbb E_t
\left[
\min
\left(
\rho_tA_t,
\operatorname{clip}(\rho_t,1-\epsilon,1+\epsilon)A_t
\right)
\right].
\]

clip limits the scope of a single update. The paper clip threshold is

\[
\epsilon=0.2.
\]

## 6. Training hyperparameter

- AdamW：\(\beta_1=0.9,\beta_2=0.95,\epsilon=10^{-5}\)；
- weight decay 0.1；
- gradient clipping 1.0；
- constant learning rate \(10^{-6}\)；
- PPO batch 512；
- mini-batch 64；
- One gradient step per mini-batch;
- 7B/13B：\(\beta=0.01\)；
- 34B/70B：\(\beta=0.005\)；
- Training for about 200–400 iterations, held-out prompt early stopping.

## 7. System implementation

70B Each PPO iteration averages about 330 seconds. FSDP is used for training; FSDP is effective for a small amount of forward/backward, but makes generation about 20 times slower. The team integrates the model weights into each node before generation, releases them after generation, and then continues the training process.

## 8. Reward hacking and Goodhart risks

When the RM score becomes the direct optimization target, the policy may find patterns that humans do not like but have high RM scores. Thesis relief includes:

- KL penalty；
- on-policy new preference data;
- Two independent RMs;
- Open data hybrids enhance generalization;
- GPT-4 cross-checking with human evaluation;
- Each new version continues into the next round of comparison.

These measures reduce risk without mathematically guaranteeing that rewards will always align with real human preferences.
