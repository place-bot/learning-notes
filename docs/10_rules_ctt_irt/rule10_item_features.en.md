# Detailed explanation of Rule 10: The importance of item stimulus characteristics

Rule comparison

| CTT | IRT |
| --- | --- |
|Compared with psychometrics attributes, item stimulus characteristics are not important|Item stimulus features can be directly related to psychometrics attributes|

## 1. Definition and classification of item stimulus characteristics

Item Stimulus Features

**Definition**: Various specific characteristics of the item that may affect individual reactions

**Hierarchy of features**:

1. **Surface Features**: Directly observable physical properties
2. **Structural Characteristics**: The logical or cognitive structure of the item
3. **Content Characteristics**: Knowledge areas or topics covered
4. **Process Characteristics**: Cognitive processes required to solve problems

### 1.1 Characteristic system in cognitive ability tests

**Surface Features**:

- Presentation modality: visual vs. auditory, text vs. graphics vs. symbols
- Number of elements: the number of information units contained in the item
- Time pressure: limited time vs unlimited time
- Response format: selection vs construction, single choice vs multiple choice

**Structural Features**:

- Logical relationships: analogy, classification, sequence, matrix
- Transformation rules: rotation, flipping, size change, color change
- Distraction factors: amount and type of irrelevant information
- Degree of abstraction: concrete graphics vs abstract symbols

**Cognitive Process Characteristics**:

- Working memory load: the amount of information that needs to be held simultaneously
- Attention control: the amount of interfering information that needs to be suppressed
- Fluid Reasoning: Complexity of patterns to be discovered
- Processing speed: the number of basic operations required to complete

## 2. Marginalization of item features under CTT framework

### 2.1 The "black box" model of traditional test development

Typical process of CTT test development

**Phase 1: Content Specification**
- How to: Develop broad content descriptions
- Problem: The specification is too abstract and lacks operability

**Phase 2: item writing**
- Method: Rely on the subjective experience of the writer
- Problem: Lack of scientific guidance, unstable quality

**Phase 3: Trial Test Screening**
- Method: Use statistical indicators to filter items
- Problem: Only focus on statistical performance and ignore the feature-performance relationship

**Phase 4: Final Selection**
- Method: Based on statistical indicators and content balance
- Problem: Unable to predict or control item performance

### 2.2 The problem of high dimensionality of feature space

Assume that the item feature space is \(\mathcal{F} = \mathbb{R}^n\) (\(n\) is very large), and the specification can only describe \(k\) dimensions (\(k \ll n\)), then:

\[
\text{Specification coverage} = \frac{k}{n} \to 0
\]

Item performance is often determined by complex interactions of features:

\[
\text{Performance} = f(x_1, x_2, \ldots, x_n) + \sum_{i<j} g_{ij}(x_i, x_j) + \sum_{i<j<k} h_{ijk}(x_i, x_j, x_k) + \cdots
\]

## 3. Item feature modeling in IRT: Linear Logistic Test Model (LLTM)

### 3.1 Basic framework of LLTM

Linear Logistic Test Model (LLTM)

**Core idea**: Decompose item difficulty into a linear combination of basic cognitive operations

**Basic Model**:

\[
P_i(\theta) = \frac{\exp(\theta - \sum_{k=1}^K q_{ik}\eta_k)}{1 + \exp(\theta - \sum_{k=1}^K q_{ik}\eta_k)}
\]

**Difficulty breakdown**:

\[
b_i = \sum_{k=1}^K q_{ik}\eta_k
\]

### 3.2 Detailed derivation of parameter estimates

**likelihood function**：

For individual \(j\)'s response to item \(i\) \(u_{ij}\):

\[
L_{ij} = P_i(\theta_j)^{u_{ij}}[1-P_i(\theta_j)]^{1-u_{ij}}
\]

**Log-likelihood**:

\[
\ln L = \sum_{i=1}^I \sum_{j=1}^J \left[u_{ij}\ln P_i(\theta_j) + (1-u_{ij})\ln(1-P_i(\theta_j))\right]
\]

**Log-likelihood under LLTM constraints**:

Substitute \(b_i = \sum_{k=1}^K q_{ik}\eta_k\) into:

\[
\ln L = \sum_{i=1}^I \sum_{j=1}^J \left[u_{ij}(\theta_j - \sum_{k=1}^K q_{ik}\eta_k) - \ln(1 + \exp(\theta_j - \sum_{k=1}^K q_{ik}\eta_k))\right]
\]

**Derivative with respect to \(\eta_k\)**:

\[
\frac{\partial \ln L}{\partial \eta_k} = -\sum_{i=1}^I \sum_{j=1}^J q_{ik}\left[u_{ij} - P_i(\theta_j)\right]
\]

**Derivative with respect to \(\theta_j\)**:

\[
\frac{\partial \ln L}{\partial \theta_j} = \sum_{i=1}^I \left[u_{ij} - P_i(\theta_j)\right]
\]

### 3.3 Newton-Raphson iteration

**Hessian Matrix Elements**:

\[
\frac{\partial^2 \ln L}{\partial \eta_k \partial \eta_l} = -\sum_{i=1}^I \sum_{j=1}^J q_{ik}q_{il}P_i(\theta_j)[1-P_i(\theta_j)]
\]

\[
\frac{\partial^2 \ln L}{\partial \theta_j \partial \theta_m} = -\delta_{jm}\sum_{i=1}^I P_i(\theta_j)[1-P_i(\theta_j)]
\]

\[
\frac{\partial^2 \ln L}{\partial \eta_k \partial \theta_j} = -\sum_{i=1}^I q_{ik}P_i(\theta_j)[1-P_i(\theta_j)]
\]

**UPDATE FORMULA**:

\[
\begin{pmatrix}
\mathbf{\eta}^{(t+1)} \
\mathbf{\theta}^{(t+1)}
\end{pmatrix} =
\begin{pmatrix}
\mathbf{\eta}^{(t)} \
\mathbf{\theta}^{(t)}
\end{pmatrix} - \mathbf{H}^{-1}\mathbf{g}
\]

Where \(\mathbf{H}\) is the Hessian matrix and \(\mathbf{g}\) is the gradient vector.

### 3.4 model fit test

**Likelihood Ratio Test**:

Compare LLTM to the standard Rasch model:

\[
\chi^2 = 2[\ln L_{\text{Rasch}} - \ln L_{\text{LLTM}}]
\]

Degrees of freedom:

\[
df = (I-1) - K
\]

Among them, \(I\) is the number of items, and \(K\) is the number of features.

**The condition is**: \(K < I-1\), otherwise LLTM will be over-parameterized.

## 4. cognitive diagnosis model

### 4.1 Basic framework

cognitive diagnosis models (CDMs)

**Individual attribute vector**:

\[
\mathbf{\alpha}_j = (\alpha_{j1}, \alpha_{j2}, \ldots, \alpha_{jK})'
\]

Among them, \(\alpha_{jk} \in \{0, 1\}\) indicates whether the individual \(j\) has the attribute \(k\)

**Q matrix**:

\[
Q = (q_{ik})_{I \times K}
\]

Among them, \(q_{ik} \in \{0, 1\}\) indicates whether the item \(i\) requires the attribute \(k\)

### 4.2 Detailed analysis of DINA model

**DINA (Deterministic Input, Noisy And gate) model**:

**ideal response**：

\[
\eta_{ij} = \prod_{k=1}^K \alpha_{jk}^{q_{ik}}
\]

\(\eta_{ij} = 1\) if and only if the individual masters all the attributes required by the item.

**response probability**:

\[
P(u_{ij} = 1 | \mathbf{\alpha}_j) = (1-s_i)^{\eta_{ij}} g_i^{1-\eta_{ij}}
\]

Among them:

- \(s_i\): slip parameter - the probability of mastering all skills but answering incorrectly
- \(g_i\): guessing parameter (guessing parameter) - the probability of answering correctly without mastering all skills

**Parameter constraints**:

\[
0 < g_i < 1-s_i < 1
\]

### 4.3 Likelihood function of DINA model

**Individual Likelihood**:

\[
L_j = \prod_{i=1}^I P(u_{ij}|\mathbf{\alpha}_j)
\]

**marginal likelihood**:

\[
L_j = \sum_{\mathbf{\alpha} \in \{0,1\}^K} \left[\prod_{i=1}^I P(u_{ij}|\mathbf{\alpha})\right] P(\mathbf{\alpha})
\]

Among them, \(P(\mathbf{\alpha})\) is the priority distribution of attribute profile.

**Log-likelihood**:

\[
\ln L = \sum_{j=1}^J \ln\left[\sum_{\mathbf{\alpha} \in \{0,1\}^K} \left[\prod_{i=1}^I P(u_{ij}|\mathbf{\alpha})\right] P(\mathbf{\alpha})\right]
\]

### 4.4 EM algorithm estimation

**E step**: Calculate the posterior probability of attribute profile

\[
P(\mathbf{\alpha}_c|\mathbf{u}_j) = \frac{\prod_{i=1}^I P(u_{ij}|\mathbf{\alpha}_c) P(\mathbf{\alpha}_c)}{\sum_{\mathbf{\alpha} \in \{0,1\}^K} \prod_{i=1}^I P(u_{ij}|\mathbf{\alpha}) P(\mathbf{\alpha})}
\]

**M step**: Update parameters

Error parameters:

\[
\hat{s}_i = \frac{\sum_{j:u_{ij}=0} P(\eta_{ij}=1|\mathbf{u}_j)}{\sum_{j=1}^J P(\eta_{ij}=1|\mathbf{u}_j)}
\]

guessing parameter:

\[
\hat{g}_i = \frac{\sum_{j:u_{ij}=1} P(\eta_{ij}=0|\mathbf{u}_j)}{\sum_{j=1}^J P(\eta_{ij}=0|\mathbf{u}_j)}
\]

### 4.5 Extended model

**DINO model** (Deterministic Input, Noisy Or gate):

\[
\eta_{ij} = 1 - \prod_{k=1}^K (1-\alpha_{jk})^{q_{ik}}
\]

Just master any required attribute.

**G-DINA model** (Generalized DINA):

\[
P(u_{ij}=1|\mathbf{\alpha}_j^*) = \delta_{i0} + \sum_{k=1}^{K_i^*} \delta_{ik}\alpha_{jk}^* + \sum_{k<l} \delta_{ikl}\alpha_{jk}^*\alpha_{jl}^* + \cdots
\]

Main effect and interaction effect are allowed.

## 5. Practical application examples

### 5.1 Analysis of characteristics of practical problem solving

Consider a fraction addition problem: \(\frac{2}{3} + \frac{3}{4} = ?\)

**Cognitive Properties**:

1. Identify the denominator (\(\alpha_1\))
2. Find the least common multiple (\(\alpha_2\))
3. Tongfen (\(\alpha_3\))
4. Molecular addition (\(\alpha_4\))
5. Simplify (\(\alpha_5\))

**Q matrix construction**:

|item| \(\alpha_1\) | \(\alpha_2\) | \(\alpha_3\) | \(\alpha_4\) | \(\alpha_5\) |
| --- | --- | --- | --- | --- | --- |
| \(\frac{1}{2}+\frac{1}{2}\) | 1 | 0 | 0 | 1 | 0 |
| \(\frac{1}{2}+\frac{1}{3}\) | 1 | 1 | 1 | 1 | 0 |
| \(\frac{2}{3}+\frac{3}{4}\) | 1 | 1 | 1 | 1 | 0 |
| \(\frac{2}{4}+\frac{3}{6}\) | 1 | 0 | 0 | 1 | 1 |

### 5.2 Model comparison

**Information Guidelines**:

\[
\text{AIC} = -2\ln L + 2p
\]

\[
\text{BIC} = -2\ln L + p\ln N
\]

Among them:

- LLTM: \(p = K + J\)
- DINA: \(p = 2I + 2^K - 1\)
- Rasch: \(p = I + J - 1\)

Select suggestions

**Use LLTM when**:

- Characteristic effects can be assumed to be linear
- Need to predict new item difficulty
-The number of items is much greater than the number of features

**When using CDMs**:

- Requires specific diagnostic skills to be mastered
- Attributes are discrete (mastered/unmastered)
- Focus on the individual’s cognitive profile
