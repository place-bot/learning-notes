# Complete pipeline of basic model and Chat model

## 1. Five stages

### Phase A: pretraining

Learn on 2T token:

\[
\mathcal L_{\mathrm{PT}}(\theta)
=
-\sum_t\log p_\theta(x_t\mid x_{<t}).
\]

Output Llama 2 base checkpoints.

### Stage B: Supervised Fine-Tuning

Enter a human-written prompt-answer pair and calculate the loss only on the assistant answer token:

\[
\mathcal L_{\mathrm{SFT}}(\theta)
=
-\sum_{t\in\mathcal A}
\log p_\theta(y_t\mid p,y_{<t}),
\]

Among them, \(\mathcal A\) is the answer token location collection.

### Phase C: Reward Modeling

Two responses are generated for the same prompt, and the annotator chooses the preferred response. reward model learns scalars:

\[
r_\phi(p,y)\in\mathbb R.
\]

### Phase D: RLHF iteration

Use both routes:

- Rejection sampling: Each prompt samples multiple responses, the reward model selects the best one, and then performs supervised updates;
- PPO: Treat the chat model as a policy, and use reward and KL constraints to directly optimize the generated policy.

### Phase E: Special safety training

Continuously add adversarial prompts, security demonstrations, security preferences, context distillation and red-teaming discovery to the iteration.

## 2. Data closed loop

The paper emphasizes that reward data must be updated with the model:

```text
Current Chat model
   ↓ Generate answer pairs for new prompts
Human comparison answer
   ↓
Update reward model
   ↓
Train the next version of the Chat model
   ↓ The distribution changes
Collect a new round of preferences
```

If the reward model has only seen the answers of the old model, the new policy may deviate from its training distribution, the scoring accuracy may decrease, or reward hacking may occur.

## 3. Density of three supervision signals

|signal|what humans offer|What the model learned|
|---|---|---|
| SFT |complete ideal answer|token level imitation|
| Preference |Which of the two answers is better?|sequence level sorting|
| Safety label |safe/unsafe and risk categories|Security identification and denial policies|

SFT's token signal is dense, but it requires the annotator to write high-quality long answers in person; the preference comparison signal is sparse, but it allows the model to explore good answers that humans may not be able to write quickly.

## 4. Why two reward models are needed?

"Follow requests as much as possible" and "avoid dangerous output" sometimes conflict. An answer may be detailed, direct, and technically useful, but violate safety regulations.

Thesis training:

\[
r_h(p,y)=\text{helpfulness score},
\]

\[
r_s(p,y)=\text{safety score}.
\]

In the PPO stage, which reward to use is selected based on prompts and safety thresholds to reduce the difficulty of a single model learning two sets of conflict judgments at the same time.

## 5. Iterative version

The authors trained RLHF-V1 to RLHF-V5. V4 used to mainly use rejection sampling; later, PPO was added to the rejection-sampling checkpoint and then continued to sample the next round of data.

This process is not a static training, but a co-evolution of the model, preference data and reward model.
