# 13. nominal response model (NRM)

## 13.1 Development background

**Developed by:** Bock (1972)

**Model Features:**

- Common divide-by-total or direct IRT models
- Can be used to characterize item responses when the responses do not have to be ordered along a trait continuum

**Important status:**

All of the above categorical-total or direct models are special cases of the nominal response model (Thissen & Steinberg, 1986)

## 13.2 Starting engines and applications

**Initial motivation:**

- Allow distractors in multiple-choice tests to be characterized by characteristic lines
- Handle cases where error options can also provide useful information

**Widely used:**

- Can be used on any item with multiple reaction options
- Includes applications in personality and attitude assessment (see Thissen, 1993)

## 13.3 Expression of NRM

**Formula 5.11:** Probability of subject responding in category x

\[
P_{ix}(\theta) = \frac{\exp(\alpha_{ix} \theta + c_{ix})}{\sum_{x=0}^{m_i}\exp(\alpha_{ix} \theta + c_{ix})} \tag{5.11}
\]

## 13.4 Parameter explanation

Each reaction category requires two parameters:

Parameter meaning

**\(\alpha_{ix}\) parameter:** Related to the slope (i.e. discrimination) of the characteristic line of category x

**\(c_{ix}\) parameter:** Intercept parameter for category x

## 13.5 Model identification constraints

In order to identify the model (i.e. estimate the parameters), constraints must be set:

**Method 1:** \(\sum \alpha_{ix} = \sum c_{ix} = 0\)

**Method 2:** Set the parameters of the lowest response category to \(\alpha_{i1} = c_{i1} = 0\)

## 13.6 Practical application examples of NRM

### 13.6.1 Thissen’s (1993) study on bulimia

**Question item:** "I like to eat:"

**Options:**

- (a) When alone at home
- (b) When at home with others
- (c) In a public restaurant
- (d) At a friend's house
- (e) Doesn’t matter

**Why use NRM? ** These options have no obvious "low to high" order and are not ordered categories.

**Parameter estimation result:**

Slope parameter (α):

- \(\alpha_a = -0.39\) (Home Alone)
- \(\alpha_b = -0.39\) (at home with others)
- \(\alpha_c = 0.24\) (public restaurant)
- \(\alpha_d = -0.39\) (friend’s house)
- \(\alpha_e = 0.93\) (doesn’t matter)

![Figure 5.13: NRMresponse probability curve of bulimia item](../assets/images/ch5_fig5.13.png)

Figure 5.13 shows the NRMresponse probability curve for the bulimia item.

Important findings

Only response option (a) "Home alone" was associated with an increased risk of bulimia.
People at high risk for bulimia are more likely to choose to eat "when alone at home."
This is consistent with the clinical features of bulimia (avoidance of eating in front of others).
