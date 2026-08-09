# 0. Introduction

## 0.1 What is a multinomial IRT model?

**What is IRT? **

- IRT = Item Response Theory (Item Response Theory)
- This is a method used in psychometrics to analyze tests and questionnaires

**What is "multiple"? **

Imagine two different items:

1. **Biary item**: True/False, Yes/No (only 2 options)
2. **Multiple items**: Strongly disagree/disagree/neutral/agree/strongly agree (with multiple options)

**Why is a multinomial IRT model needed? **

The traditional IRT model can only handle true and false questions, but in reality many psychological tests (such as personality tests and attitude surveys) use multiple levels of scoring, such as:

- Likert scale of 1-5
- Options from "Strongly Disagree" to "Strongly Agree"

## 0.2 Background and Objectives

**Background Questions:**

The IRT model introduced in Chapter 4 can only handle dichotomous items (true or false), but this has a limitation: many test formats commonly used by psychologists cannot be simply scored as true or false.

**Actual demand:**

- Many measurement tools, especially attitude and personality assessments, contain items with multiple ordinal response categories
- Main reasons why researchers use these formats: more informative and more reliable than dichotomous scores
- For these multi-category item response data, a multinomial IRT model is needed to represent the non-linear relationship between subject trait levels and category-specific response probability

**Goal of this chapter:**

- Not a comprehensive summary of all existing models
- Instead, it provides a description of the basic psychometrics properties of six well-known multinomial models
- Readers interested in more extensive coverage are referred to van der Linden and Hambleton (1996)

## 0.3 The model to be introduced in this chapter

1. **Graded Response Model (GRM)**
   **Rank Response Model**
   Samejima, Fumiko (1969) proposed
   It is an extension of the 2-parameter logistic model (2PL) and is suitable for ordered multi-category items.
2. **Modified Graded Response Model (M-GRM)**
   **Modified Grade Response Model**
   Muraki, Eiji (1992) proposed
   Introducing flexible threshold settings based on GRM is more suitable for asymmetric scoring standards in actual measurements.
3. **Partial Credit Model (PCM)**
   **partial credit model**
   Presented by Masters, Geoffrey N. (1982)
   It is an extension of the Rasch model (1PL) for multi-level scoring items, and each item can have an independent threshold.
4. **Generalized Partial Credit Model (GPCM)**
   **generalized partial credit model**
   Muraki, Eiji (1990) proposed
   Add itemdiscrimination parameter (similar to 2PL) based on PCM to model item differences more flexibly.
5. **Rating Scale Model (RSM)**
   **Assess scale model**
   Andrich, David (1978a, 1978b) proposed
   The simplification of PCM assumes that the threshold structure of all items is the same and is suitable for scales with fixed scoring standards.
6. **Nominal Response Model (NRM)**
   **nominal response model**
   Bock, R. Darrell (1972) proposed
   Suitable for unordered polytomous items, allowing each category to have independent attraction and discrimination parameters.

**Model classification:**

- **"Indirect" model**: requires a two-step process to determine the conditional probability of a subject's response in a particular category (first two models)
- **"Direct" model**: only one equation describes the relationship between subject trait level and response probability of a specific category (later model)
