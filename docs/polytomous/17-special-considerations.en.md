# 17. Special considerations for multinomial IRT models

## 17.1 Questions highly related to the number of subjects

**1. The importance of heterogeneous samples:**

It is strongly recommended that researchers estimate parameters based on heterogeneous samples to avoid the second problem of fitting multinomial models.

**2. Each reaction category requires a reaction: **

Researchers must have item responses in each response category.

zero frequency problem

If response categories have zero or few responses, programs that estimate parameters will not be able to make good estimates between category thresholds or crossover points.

## 17.2 Actual problems encountered

**Common situations:**
We have seen many samples where subjects did not choose a specific item category

**Possible reasons:**

- Due to the quasi-categorical nature of traits
- Certain extreme categories are rarely selected

## 17.3 Solution

**Method 1: Merge Categories**

- Merge rarely selected categories with adjacent categories

**Method 2: Rewrite item (better method)**

- Reduce the number of categories
- Redesigned category labels

Important note

Some special considerations are required when merging categories, see Andrich (1995)

## 17.4 Practical recommendations

sample planning

- Ensure sufficient sample size (at least 500 people)
- Ensure sample heterogeneity
- Pre-test checks distribution of responses across categories
-Adjust item design if necessary
