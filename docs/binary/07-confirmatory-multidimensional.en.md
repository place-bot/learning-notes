# 7. Validation multidimensional model

Validation models contain design structures that link items to specified traits. Applies to situations where the theory has elucidated the underlying process.

**Core idea:**

Not "see what the data tells us" but "check whether my theory is correct".

## 7.1 Non-compensatory dimensional model

### 7.1.1 Multi-component latent trait model (MLTM)

Whitely (1980) proposed multiple processing components for measuring item solutions.

**Core Assumption:** The success of item requires the success of all components. If any one component fails, the whole fails.

**Realistic example:**

Solving word problems requires:

1. Understand the meaning of the question (reading)
2. Establish equations (modelling)
3. Solve equations (calculation)

If any step fails, the entire question will be wrong!

**Expression:**

\[
P(X_{isT} = 1|\theta_s,\beta_i) = \prod_m \frac{\exp(\theta_{sm} - \beta_{im})}{1 + \exp(\theta_{sm} - \beta_{im})} \tag{4.21}
\]

Note: Use product (\(\prod\)) instead of summation to reflect non-compensation.

**Parameter meaning:**

- \(\theta_{sm}\) = trait level of individual s on component m
- \(\beta_{im}\) = difficulty of item i on component m

**Why use product? **

The product of probabilities represents the probability of "all events occurring":

- P(comprehension) × P(modelling) × P(calculation) = P(all pairs)

### 7.1.2 General component latent trait model (GLTM)

An extension of Embretson (1984) to incorporate a model of component difficulty:

\[
P(X_{isT} = 1|\theta_s,\beta_i) = \prod_m \frac{\exp(\theta_{sm} - (\sum_k \tau_{km} q_{ikm} + q_{0m}))}{1 + \exp(\theta_{sm} - (\sum_k \tau_{km} q_{ikm} + q_{0m}))} \tag{4.22}
\]

Among them:

- \(\tau_{km}\) = weight of stimulus k in component m
- \(q_{ikm}\) = score of stimulus k on component m of item i

**Advantages:**

1. Control constructs by selecting component-specific difficulty modes
2. Measuring an individual’s underlying processing components

**Application example:**

Component breakdown of the spatial rotation task:

1. Encoding phase: remember the original graphics
2. Rotation stage: mental rotation
3. Comparison stage: Compare with options

Items can be designed to emphasize different ingredients!

## 7.2 Learning and change models

### 7.2.1 Multidimensional Rasch Learning and Change Model (MRMLC)

Developed by Embretson (1991) to measure change.

**Wiener Process Structure:**

For four measurements:

\[
\Lambda_{k \times m} =
\begin{pmatrix}
1 & 0 & 0 & 0 \
1 & 1 & 0 & 0 \
1 & 1 & 1 & 0 \
1 & 1 & 1 & 1
\end{pmatrix} \tag{4.23}
\]

Meaning:

- \(\theta_1\) = Initial trait level (Participate in all occasions)
- \(\theta_2\) = Changes from the 1st to the 2nd occasion
- \(\theta_3\) = Changes from the 2nd to the 3rd occasion
- and so on

**Intuitive understanding:**

Like climbing stairs:

- First measurement: standing on level 1
- Second measurement: Level 1 + how much climbed
- Third measurement: height in front + how much more you climbed
- Each θ represents an increment

**Model expression:**

\[
P(X_{i(k)s} = 1|\theta_s,\beta_i) = \frac{\exp(\sum_m^k \theta_{sm} - \beta_i)}{1 + \exp(\sum_m^k \theta_{sm} - \beta_i)} \tag{4.24}
\]

The summation symbol \(\sum_m^k\) controls the participation of the appropriate dimensions in condition k.

**Application scenario:**

-Evaluation of the effectiveness of educational intervention
- Treatment effect tracking
- Skill learning curve

## 7.3 Models with specified trait structures

### 7.3.1 General structural latent trait model (SLTM)

Embretson (1995, 1997) proposed that the design structure includes:

\[
P(X_{i(k)s} = 1|\theta_s,\beta_{ik},\lambda_{i(k)m}) = \frac{\exp(\sum_m \lambda_{i(k)m} \theta_{sm} - \sum_k \beta_{ik})}{1 + \exp(\sum_m \lambda_{i(k)m} \theta_{sm} - \sum_k \beta_{ik})} \tag{4.25}
\]

**Features:**

- Weights can be fixed to zero (verification)
- Similar to confirmatory factor analysis
- Allows complex constraint structures

**Example Design Matrix:**

\[
\Lambda =
\begin{pmatrix}
\lambda_{11} & 0 & 0 & 0 \
\lambda_{21} & \lambda_{22} & 0 & 0 \
\lambda_{31} & \lambda_{32} & \lambda_{33} & 0 \
\lambda_{41} & \lambda_{42} & \lambda_{43} & \lambda_{44}
\end{pmatrix} \tag{4.26}
\]

**Explanation:**

This matrix structure represents:

- item1 only measures capacity 1
- item2 measurement capabilities 1 and 2
- item3 measurement capabilities 1, 2 and 3
- item4 measures all four abilities

## 7.4 Models for different categories of people

### 7.4.1 SALTUS model

Wilson (1985) proposed it for developmental data.

**Core idea:** After reaching a certain stage, the success rate of related items suddenly increases.

**Realistic example:**

Piaget’s stages of cognitive development:

- Children in the concrete operational stage suddenly understand conservation
- Teenagers in the formal operations stage suddenly able to reason abstractly

**Model:**

\[
P(X_{is} = 1|\theta_s,\beta_i) = \prod_m \frac{\exp(\theta_s - \beta_i + \zeta_{h(s)k(i)})}{1 + \exp(\theta_s - \beta_i + \zeta_{h(s)k(i)})} \tag{4.27}
\]

Where \(\zeta_{h(s)k(i)}\) = successful addition of item type k in stage h.

### 7.4.2 Mixed Population Rasch Model (MIRA)

Rost (1990) combined IRT and latent class analysis:

\[
P(X_{is} = 1|\theta_s,\beta_i) = \sum_h \gamma_h \frac{\exp(\theta_{sh} - \beta_{ih})}{1 + \exp(\theta_{sh} - \beta_{ih})} \tag{4.28}
\]

**Features:**

- \(\gamma_h\) = proportion of latent classh
- item difficulty varies within categories
- Estimate class membership probabilities

**Application example:**

- Spatial vs verbal strategies
- Different knowledge structures
- Qualitative individual differences

**Specific example:**

When solving problems:

- Category 1: Using the first method (60% of students)
- Category 2: Using the second method (40% of students)
- Different methods lead to different difficulties of different items!
