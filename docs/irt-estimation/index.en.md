#IRT Estimation and Evaluation

This part puts the most critical work after IRT model fit: parameter estimation, trait scale, examinee scoring (scoring) and model fit assessment (model fit assessment).

## Learning sequence

1. [IRT parameter estimation](../estimate.md): Understand how item parameters are estimated from reaction data.
2. [IRT trait scale](../scale/index.md): Understand the units, interpretation and specific objectivity of \(\theta\) scale.
3. [examinee score](../score/index.md): Compare MLE, MAP, EAP and score transformation.
4. [model fit evaluation](../assess.md): Check whether the model assumptions adequately support the interpretation.

## The core issue of this part

- Whether item parameters and ability parameters can be estimated stably.
- What does the numerical unit of \(\theta\) represent?
- Why does the same raw score need to be converted by the model to become a comparable scale score?
- How item information and test information determine measurement accuracy at different ability levels.
- When the model fit is not good, where will the score interpretation fail?

## Output

|output|Purpose|
| --- | --- |
|item parameters|Describe item difficulty, discrimination, and other model parameters|
|ability estimate|Position the participant on the latent traitscale|
|standard error|Represents uncertainty in individual scores|
|information function|Determine at which ability ranges the test is most accurate|
|fit index|Determine whether the model assumptions are compatible with the data|
