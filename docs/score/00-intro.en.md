# 0. Introduction: Why can’t the ability estimate only look at scores?

## 0.1 Raw score problem: just looking at right and wrong is not precise enough

In a traditional test, we score the examinee by simply counting the number of correct items. This approach seems intuitive, but there are fundamental problems:

core issues

- Do students who answer 10 easy items correctly and students who answer 10 difficult items correctly really have the same ability?
- If two students answer 5 questions correctly, but on different items, are their abilities really the same?
- How do we accurately assess a student's ability when they get all answers correct or all answers wrong?

Why are there not enough raw scores?

The raw score does not take into account the nature of the item. In reality, the difficulty and sensitivity (discrimination) of different items are different.
For example, if one student answers a very difficult question correctly and another student answers an extremely easy question correctly, they are equivalent in terms of "raw score", but they are very different in terms of ability assessment.

The **more serious problem** is: once the examinee is all right or all wrong, we cannot judge his/her real ability through the raw score number - because of the lack of "gradient".

---

## 0.2 The revolutionary concept of IRT scoring: not only depends on how many questions you get right, but also what questions you get right

Item Response Theory (IRT) provides a new scoring method that not only considers the number of items answered correctly, but also considers:

Core considerations for IRT scoring

- **item difficulty**: Correctly answering difficult items is a better indicator of ability than correctly answering easy items.
- **item discrimination**: Some items are better than other items in distinguishing examinees with different abilities
- **Response Mode**: The specific items answered correctly provide important information about the ability level.

Why is reactive pattern valuable?

Both examinees answered 5 questions correctly if:

- A answered the first 5 questions correctly (easy)
- B answered the last 5 questions correctly (difficult)

Then B's ability is higher. This detail is ignored in raw score numbers, but IRT explicitly exploits these "response structures" to infer ability.

---

## 0.3 What can you do after studying this chapter?

By studying this chapter, you will master:

learning objectives

1. **Three main IRT scoring methods**: maximum likelihood estimation (ML), maximum a posteriori estimation (MAP) and expected a posteriori estimation (EAP)
2. **Principles of Scoring Algorithms**: Understand the statistical reasoning process behind each method
3. **Practical application considerations**: When to choose which method, the advantages and disadvantages of different methods
4. **Measurement Accuracy Assessment**: Understand how standard error and test information functions measure measurement uncertainty

Where can this knowledge be applied?

- Educational assessment: scoring students and stratifying their abilities
- psychometrics: understanding personality or ability structures
- Data science: used for accurate modeling and personalized recommendations

---

## 0.4 Two sample quizzes: To understand the scoring mechanism

To illustrate the various concepts concretely, we will use two carefully crafted example quizzes:

Sample quiz design

**Test A (Rasch Type Test)**

- 10 items, all items have the same discrimination: \(\alpha_i = 1.50\)
- Symmetrical distribution of item difficulty: \(\beta_i = [-2.0, -1.5, -1.0, -0.5, 0.0, 0.0, 0.5, 1.0, 1.5, 2.0]\)
- **For illustration**: When the discrimination is the same, the difference in information value of correctly answering items of different difficulty

**Test B (Variable Discrimination Test)**

- 10 items, all items have the same difficulty: \(\beta_i = 0.0\)
- The discrimination gradually increases: \(\alpha_i = [1.0, 1.0, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]\)
- **For illustration**: When the difficulty is the same, how the item's ability to distinguish abilities will affect the score result.

Why design such a practice test?

We want to "control one variable and observe the effect of another variable", which is the classic way of understanding statistical models.

---

## 0.5 Prerequisites for establishing IRT scoring

Before further discussion, several important assumptions need to be made clear:

key assumptions

**arbitrariness of scale**

- The capability scale (\(\theta\)) in IRT is a "relative scale" that cannot be directly observed and must be fixed through some kind of "anchoring" method.
- It is usually assumed that \(\theta \sim N(0, 1)\), that is, standard normal distribution, is for numerical stability and ease of interpretation.

**Explanation of parameters**

- \(\theta = -1.0\): participant ability is one standard deviation below average
- \(\theta = 0.0\): participant is of average ability
- \(\theta = 1.5\): participant ability is one and a half standard deviations above average

**Model settings**

- This chapter uses the logistic model uniformly (not normal ogive)
- The constant \(D = 1.7\) has been absorbed into the \(\alpha_i\) distinction to facilitate concise derivation

Summary: From scores to ability estimates

This chapter will guide you to establish a systematic understanding of ability estimates, scoring algorithms, and accuracy analysis starting from the "original right and wrong scores". What you will find:
**Scoring is not just a calculation, it is a process of information extraction. **
