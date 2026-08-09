# Open source code, open weights and open training

## 1. "Model open" contains at least six layers

When discussing software, "whether the source code is public" is often enough to form a preliminary judgment. Modern language models also contain weights, data, training methods, licenses, and service interfaces, so they need to be viewed hierarchically.

|level|Objects to be checked|what does it allow us to do|
|---|---|---|
|Model interface|API, web page or SDK|Call the model, but generally cannot inspect or modify the weights|
|Reasoning code|Transformer implementation, sample code|Understand and run the architecture, assuming compatibility weights can be obtained|
|Model weight|Parameter tensor and tokenizer|Local inference, quantization, fine-tuning or continued training|
|training code|pretraining, SFT, preference optimization pipeline|Study the training process, but still need data and computing power|
|training data|Data source, matching ratio, filtering rules or complete corpus|Assess data bias and improve reproducibility|
|license|Code license, weight license, acceptable use policy|Determine legal boundaries for research, commercial use, redistribution, and derivative models|

A model may expose inference code and weights, but only the categories of training data; it may also provide APIs and technical reports, but not weights. To lump these situations together as "fully open source" would be to miss the most important message.

## 2. Three practical terms

### Open-source software

Usually refers to source code released under an open source license. Described here are software such as tokenizers, inference servers, and training frameworks. Code licenses do not automatically override model weights.

### Open-weight model

Refers to parameter weights that can be downloaded. This term only indicates that the weights are available and does not automatically mean:

- Can be used in any business scenario;
- Can be freely redistributed;
- Training data is made public;
- The complete training code is made public;
- Meet a certain strict definition of open source.

### API-access model

Users send input and get output through the service interface. API facilitates quick use and unified maintenance, but cannot provide local weight control. Price, data governance and version stability are also determined by the terms of service.

## 3. Why it is necessary to implement specific checkpoints

"Mistral" or "Command" are family names, not a license. In the case of Mistral, early Mistral 7B and Mixtral 8x7B weights feature Apache 2.0; other models from the same company may use a research license or be available as a hosted service only. Cohere's API product names are also not directly interchangeable with Cohere Labs' Open Weight Research version.

Therefore, the minimum unit of license judgment should be written as:

```text
Release organization / Exact model ID / Date or version / Weight license / Code license
```

For example:

```text
CohereLabs/c4ai-command-r-08-2024
Attribution: CC-BY-NC and subject to the Acceptable Use Policy
```

This provides executable information than "Command R is open source".

## 4. Checklist before starting item

1. Accurately record model ID, revision and tokenizer revision;
2. Read the LICENSE, model card and acceptable use policy of the weight warehouse respectively;
3. Determine whether commercial use, hosting services, redistribution and derivative models are allowed;
4. Check whether the input and output data can leave the local environment;
5. Check context length, quantification support, hardware requirements and chat templates;
6. Save the evaluation version to avoid result drift caused by silent upgrades by suppliers.

License content is subject to change. This topic provides a technical reading framework, and actual legal judgments should be based on the official terms of the target version.

