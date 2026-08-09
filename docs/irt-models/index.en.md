# IRT model

This part organizes the model family of Item Response Theory (IRT). Currently, it is divided into dichotomous item models (binary item models) and polytomous item models (polytomous item models).

## Learning sequence

1. [Dichotomous item model](../binary/index.md): First learn 1PL, 2PL, 3PL, normal Ogive, multidimensional model and other data models used for true and false questions.
2. [Multiple item model](../polytomous/index.md): Re-learn GRM, PCM, GPCM, RSM, NRM and other data models for grade scoring or multi-category responses.

## dichotomous item model

The dichotomous item model handles \(0/1\) response data, such as wrong/correct, no/yes, fail/pass. The core question is how item difficulty (difficulty), discrimination (discrimination), guessing parameter (guessing) and latent ability (latent ability) jointly determine the probability of correct answer.

## Multiple item model

Multinomial item models handle more than two response categories, such as Likert scale, partially rated items, graded items, and nominal category responses. The core issue is how category thresholds, step parameters, and category response curves explain the reaction process.

## Issues that need to be looked at uniformly when reading models

|question|Description|
| --- | --- |
|data type|Does the model fit dichotomous, hierarchical, multicategory, or continuous responses?|
|latent variable structure|Unidimensional, multidimensional, exploratory or confirmatory?|
|Parameter meaning|Difficulty, Discrimination, Guess, Threshold or Step Parameters|
|Interpretability|Can model parameters serve test interpretation and item diagnosis?|
|Estimate requirements|sample size, local independence, unidimensionality and model fit requirements|
