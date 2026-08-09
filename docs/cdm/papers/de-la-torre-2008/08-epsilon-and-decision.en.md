# Threshold and final decision

## Why threshold is needed

In an ideal hypothetical question, adding irrelevant attributes after correcting the q-vector will cause \(\delta\) to decrease. Real data will be affected by:

- Sampling error;
- Posterior estimation error;
- DINA approximation error;
- The proportion of attribute profile is unbalanced;
- Multiple problem-solving strategies within item;
- Initial Q error propagation.

Therefore, adding irrelevant attributes may also bring small positive increments. If only request

\[
\widehat\delta^{(s)}
>
\widehat\delta^{(s-1)},
\]

Sequential search makes it easy to continue adding attributes.

## Original text stopping criteria

To be accepted, new attributes must meet the following requirements:

\[
\widehat\delta_j^{(s)}
-
\widehat\delta_j^{(s-1)}
>
\varepsilon.
\]

\(\varepsilon\) indicates how much distinction the new attribute must contribute at least.

## Threshold direction

| \(\varepsilon\) |search behavior|Main risks|
| ---: | --- | --- |
|0 or very small|Minor improvements are acceptable|q-vector is too dense|
|medium|Ignore small random fluctuations|Might be better balanced|
|very big|Only accept strong improvements|q-vector is too thin|

The paper calls the small \(\varepsilon\) liberal and the large \(\varepsilon\) stringent.

## How to choose the threshold in the original text

The authors did not give a fixed \(\varepsilon\) for all data. The process is:

1. Get a series of thresholds;
2. Each threshold generates a set of candidate Q;
3. Add EM under candidate Q;
4. Compare \(\bar g+\bar s\);
5. Compare the consistency rate of the grid and the entire row with the original Q;
6. Review the revised content explanation.

Three experiments in the original article were used:

|experiment|threshold|
| --- | --- |
|Simulation| .00、.01、.05、.10、.20 |
|Fraction subtraction|.000 to .050 in steps of .001|
| NAEP |.000 to .100 in steps of .001|

## Conservatism principle

The author puts forward two practical constraints:

1. The current Q is only one of many Qs that may fit the data; a Q that fits the data better may lack interpretability.
2. Establishing Q usually involves a lot of content analysis and expert work; when there is no strong evidence, a more conservative attitude towards the original specification should be adopted.

This means that a candidate that slightly lowers \(\bar g+\bar s\) should not automatically overwrite existing content evidence.

## Suggested Modern Decision Table

|Statistical improvements|content evidence|Suggestions|
| --- | --- | --- |
|Big|Support modification|Modify and cross-validate|
|Big|Oppose modification|Check for missing attributes, item clues, and model mismatches|
|small|Support modification|Collect more samples or process data|
|small|Oppose modification|Keep the original Q|
|worsen|arbitrary|Usually keep the original Q and check the estimation stability|

## Additional reporting required

In order to prevent pursuing lower \(s+g\) only on training samples, subsequent research can add:

- Leave the log-likelihood of the sample;
- attribute classification stability;
- How often row Q is recommended in bootstrap;
- Consistency with multiple starting points and different initial Q;
- Inter-expert agreement;
- The external criterion relationship before and after modification.

These items exceed the original experiments in 2008, but can extend the threshold selection from single-sample fitting to stability and validity.

