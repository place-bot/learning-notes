# computerized adaptive testing (CAT)

Computerized adaptive testing (Computerized Adaptive Testing, CAT) gradually determines the next question based on the examinee's previous answers. Its core loop is:

\[
\text{Current answer history}
\longrightarrow
\text{Update examinee status}
\longrightarrow
\text{Select the next question from the remaining item bank}
\longrightarrow
\text{Get new answers}.
\]

Therefore, CAT papers are often not fully fixed before administration. Even if two examinees start from the same starting point, as long as the answer to a certain step is different, subsequent items may diverge. This closed loop of “re-decision after each answer” is the key to understanding the difference between CAT and generating the entire set of recommendation sequences at once.

## How to organize this column

This site uses CAT as a topic at the same level as CDM. Each specific method establishes an independent sub-module under CAT to facilitate the subsequent addition of traditional Fisher information topic selection, cognitive diagnostic CAT, constrained CAT, and generative CAT.

Currently included:

- [Adaptive Testing with Self-Evaluation](adaptive-testing-self-evaluation/index.md): Let the examinee's self-judgment participate in topic selection or initialization, and study whether this additional information can improve the cold start, test experience and efficiency of CAT.
- [BOBCAT](bobcat/index.md): Use double-layer optimization to learn adaptive topic selection strategies from historical response data.
- [NCAT](ncat/index.md): Write topic selection as a reinforcement learning problem, and use dual-channel attention and Q-learning to learn the long-term value of topic selection.
- [Deep RL adaptive learning](adaptive-learning-drl/index.md): Use continuous latent ability as state and learning materials as actions, use DQN to learn closed-loop teaching paths, and use transition model to improve small sample data utilization.

## The place of two data-driven approaches in CAT

Traditional IRT-CAT usually estimates ability first and then selects the next question based on Fisher information or posterior uncertainty. BOBCAT retains the topic-by-topic interactive CAT process, while transforming the topic selection criteria into strategies that can be trained by data:

\[
\Pi_\phi\!\left(x_i^{(t)}\right)
\longrightarrow
j_i^{(t)}.
\]

Among them, \(x_i^{(t)}\) summarizes the answer history of students \(i\) up to step \(t\), and \(\Pi_\phi\) outputs the distribution or question number of the next question. New answers will be written back to the status immediately, and then the strategy will be re-run, so what BOBCAT learns is a closed-loop question selection rule.

NCAT uses the same question-by-question feedback structure and writes the long-term question selection value as a Q function:

\[
Q_\phi(s_t,\cdot)
\longrightarrow
q_t
\longrightarrow
a_t
\longrightarrow
s_{t+1}.
\]

It constructs reward based on the prediction loss on held-out query questions and trains the strategy through Q-learning; correct and incorrect answers are encoded by dual-channel attention. BOBCAT and NCAT will reselect the next question after each true answer arrives. The difference is mainly in the solution method and status representation of the training target.

Deep RL adaptive learning studies the outer layer of instructional decisions. The material will change the student's ability. After learning, re-estimate the ability through a test or CAT before selecting the next material. Both it and NCAT use Q-learning, but the former optimizes the path required to achieve learning goals, while the latter optimizes the quality of measurement.
