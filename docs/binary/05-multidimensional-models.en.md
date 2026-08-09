# 5. Multidimensional model

## 5.1 Why is multidimensional IRT needed?

Multidimensional IRT models contain two or more parameters to represent each person.

**Real needs:**

Consider a reading comprehension test:

- Vocabulary knowledge required
- Requires grammatical understanding
- Requires reasoning skills
- Requires background knowledge

A single score cannot adequately describe a student's ability structure!

**Application:**

- Individuals have systematic differences in which items are difficult or easy
- Multiple abilities jointly affect item performance
- Need to measure multiple constructs simultaneously

**Example:**

Application questions:

- Student A: strong in calculation, weak in understanding (cannot understand the questions)
- Student B: Strong in understanding, weak in calculation (understands but calculates incorrectly)
- Unidimensional models cannot differentiate between these two situations

## 5.2 Symbol system of multidimensional model

- \(X_{is}\): The response of individual \(s\) to item \(i\) (0 or 1)
- \(\theta_{sm}\): The trait level of individual \(s\) on dimension \(m\)
- \(\beta_i\): The difficulty of item \(i\)
- \(\delta_i\): Ease intercept of item \(i\)
- \(\alpha_{im}\): Discrimination of item \(i\) in dimension \(m\)
- \(\gamma_i\): Lower asymptote of item \(i\) (guess)

Note: The ease \(\delta_i\) is commonly used in multidimensional models to replace the difficulty parameter.

**Why use ease instead? **

In a multidimensional space, the concept of "difficulty" becomes complex, and it is more natural to use "ease".

## 5.3 Model classification

Multidimensional models are divided into two categories:

**Exploratory Model**:

- Similar to factor analysis
- Estimate multidimensional parameters to improve fit
- No default dimension meaning

**Applicable scenario:** "I know the test measures multiple abilities, but I'm not sure what"

**Confirmatory Model**:

- Estimate parameters for specified dimensions
- Default item and dimension relationship
- Test theoretical hypotheses

**Applicable scenario:** "I think this test measures two abilities: calculation and reasoning. Let me verify it."
