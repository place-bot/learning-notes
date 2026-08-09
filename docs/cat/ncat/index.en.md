# NCAT: Use neural reinforcement learning to learn topic-by-topic selection strategies

NCAT (Neural Computerized Adaptive Testing) was proposed by Zhuang et al. at AAAI 2022. It writes the question-by-question selection process of CAT as a reinforcement learning question: the system reads the questions that the current student has answered correctly and incorrectly, estimates the long-term value of each candidate question, and selects a question; after the student answers, the status is updated immediately, and the system determines the next question.

\[
\text{Current answer history}s_t
\xrightarrow{Q_\phi}
\text{Select item}q_t
\xrightarrow{\text{students answer}a_t}
s_{t+1}.
\]

Therefore, what NCAT learns is a **closed-loop strategy**. The strategy will be re-run at each step during the test, and subsequent items depend on the real feedback just given by the student.

!!! info "What is the difference between "generating a complete set of questions in advance""

    NCAT learns function \(Q_\phi(s,q)\) during training and only selects one question at a time during deployment. The student's answer in step \(t\) will be entered into \(s_{t+1}\), and the Q value of each candidate question in step \(t+1\) will be changed. The term “fully adaptive” in the paper refers to this closed loop of question-by-question feedback.

## See the complete process in one picture

```text
History Student Log
    │
    ├── Support questions for each student: allows strategy to select question by question and read historical answers
    └── Each student’s query question: only used to test the current ability estimate
             │
             ▼
Correct/wrong dual channel status ──► NCAT Q Network ──► Next question
             ▲                              │
             │                              ▼
             └──────── New answer ◄──── Response model updates student parameters
                                            │
                                            ▼
                              The opposite number of query BCE is used as reward
                                            │
                                            ▼
                                  Experience replay and TD updates
```

There are three cooperating objects here:

|object|mark|function|
|---|---:|---|
|response model| \(M\) |Predict the probability of correct answers based on student parameters and update student parameters with selected questions|
|Topic selection network| \(Q_\phi\) |Calculate long-term value for each candidate question based on current answer history|
|historical response environment| \(\mathcal D\) |Provide offline "If this question is selected, the student answered it correctly or incorrectly at that time"|

The paper collectively refers to student response models such as IRT, MIRT, and NCDM as CDM. This site follows the paper notation \(M\), and uses the broader term "response model" when strict distinction is required.

## NCAT’S CORE INNOVATIONS

Advancement of NCAT occurs at three levels.

1. **Target level**: Use the prediction loss on unselected query questions to evaluate whether a selected question really helps measurement, and include the query loss of all test steps into the target.
2. **Algorithm level**: Model topic-by-topic selection as MDP, and use Q-learning to learn the long-term value of topic selection.
3. **Representation level**: Divide the correct answers and wrong answers into two channels, first perform Performance Learning within the channel, and then perform Contradiction Learning across channels to identify response combinations caused by guesses, mistakes, or inconsistent knowledge structures.

## Recommended reading route

When reading for the first time, just follow the following order:

1. [Question, CAT and offline data](01-cat-and-data.md)
2. [Two-tier goals, MDP and rewards](02-objective-and-mdp.md)
3. [Q-learning and experience playback](03-q-learning.md)
4. [State encoding and dual-channel attention](04-neural-encoder.md)
5. [Training with real student deployment](05-training-and-deployment.md)
6. [Complete hand calculation example](06-worked-example.md)

Read on when preparing for replication or research:

- [Experimental design, complete results and result analysis](07-experiments.md)
- [Official code intensive reading and minimum implementation](08-implementation.md)
- [Limitations, method comparison and future work](09-limitations-comparison-future.md)
- [Symbol table with FAQ](10-symbols-faq.md)

## Questions you should be able to answer after reading

- How does support/query segmentation turn historical logs into an offline CAT environment?
- Why can query BCE be used to supervise topic selection, but training reward does not need to be calculated during deployment?
- \(Q_\phi(s_t,q)\) Why is it neither the probability of correct answer nor Fisher information?
- Every time a student answers a question, how does NCAT change the next question?
- How does dual-channel attention represent correct answers, incorrect answers, and the contradiction between them?
- What conclusions do the results of the paper support, and which constraints still need to be dealt with separately?

## Connection with BOBCAT

[BOBCAT](../bobcat/index.md) and NCAT both learn topic-by-topic selection strategies from historical response data, and both use predicted performance on held-out questions to evaluate selected topics. The training paths of the two are different:

- BOBCAT seeks meta-gradient for the two-layer calculation of "adapting to student parameters after selecting the topic";
- NCAT regards each topic selection as an action, uses query prediction loss to construct reward, and uses Q-learning to learn the cumulative reward.

For a more complete side-by-side comparison, see [Limitations, Methods Comparison, and Future Work](09-limitations-comparison-future.md).
