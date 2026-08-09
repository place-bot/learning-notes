# Study 1: Five reduction models

## Success probability conditions

The zero attribute group and full control group are set to:

\[
(p_0,p_1)=(.1,.9)
\quad\text{or}\quad
(.2,.8).
\]

Intermediate mode probabilities are determined from the response functions of the five models. Table 4 in the main body of the paper reports the \((.2,.8)\) condition; the authors use this as the primary comparison for the relatively lower item quality condition.

## Table 4 complete result

Values are percentages.

|Generate model|Hierarchy|error corrected|error still exists|correct to be changed|Keep it right|
| --- | --- | ---: | ---: | ---: | ---: |
| DINA | entry | 88.4 | 11.6 | 0.8 | 99.2 |
| DINA | vector | 84.3 | 15.7 | 2.1 | 97.9 |
| DINA/A-CDM | entry | 79.9 | 20.1 | 0.4 | 99.6 |
| DINA/A-CDM | vector | 76.8 | 23.2 | 1.6 | 98.4 |
| A-CDM | entry | 81.9 | 18.1 | 0.2 | 99.8 |
| A-CDM | vector | 80.1 | 19.9 | 0.8 | 99.2 |
| DINO/A-CDM | entry | 78.4 | 21.6 | 0.3 | 99.7 |
| DINO/A-CDM | vector | 75.8 | 24.2 | 0.9 | 99.1 |
| DINO | entry | 88.4 | 11.6 | 0.8 | 99.2 |
| DINO | vector | 83.1 | 16.9 | 2.0 | 98.0 |

## result 1: Correct protection Q

Across all models:

- Correct entry retention rate is at least 99.2%;
- Correct vector retention rate is at least 97.9%.

This shows that the \(.95\) threshold is highly conservative under these conditions and rarely destroys correct input.

## Result 2: Most errors can be corrected

- Entry layer correction rate: 78.4%--88.4%;
- Vector layer correction rate: 75.8%--84.3%.

Full line-by-line recovery is more difficult than block-by-block recovery because a row needs only one error to be counted as unrecovered.

## result 3: The simpler the response process, the higher the recovery.

The error entry correction rates of DINA and DINO are both 88.4%, which is higher than the three models containing additive components. The two-terminal model forms a sharper grouping of success probabilities, and missing a valid attribute has a greater impact on GDI.

## Worst conditions still lead to improvements

Thesis report:

- The worst overall correct recovery rate of the entry layer is 98.6%, and the chance-adjusted improvement relative to the baseline is 72.1%;
- The worst overall correct recovery rate for the vector layer is 93.6%, and the chance-adjusted improvement is 71.1%.

Baseline refers to retaining the original Q with approximately 5% error. Adjusted improvement measures how many otherwise correctable errors have been eliminated.

## Scope of application of conclusion

These results support:

- \(K=5,J=30,N=2000\)；
- High-order related attributes;
- About 5% random entry errors;
- Success probability of two endpoints;
- Fixed \(\varepsilon=.95\).

They do not cover systematic misconfiguration concentrated on a few key items, missing attribute definitions, or a larger attribute space.
