# Open weight model family: Command R, Mistral, Phi and Llama

This set of features explains four model families that often appear side by side: Cohere's Command R, Mistral AI's Mistral, Microsoft's Phi, and Meta's Llama. They all allow developers to access the model in some form, but the scope of exposure, license, model size and product positioning are different.

!!! warning "Correct a common expression first"
    "Command R, Mistral, Phi and Llama are all open source models" is too general. A more reliable statement is: **These four families have all had versions with downloadable weights, but the license and openness of each specific checkpoint must be checked separately. **

    - Cohere Labs research weighting for Command R is CC-BY-NC, with acceptable use requirements and commercial use restricted;
    - Mistral has both Apache 2.0 checkpoints in the same family, as well as models available under research license or via API only;
    - Multiple official checkpoints of Phi adopt the MIT license, and the open scope is relatively loose;
    - Llama releases weights and code, but under a Meta custom community license, not the standard OSI open source license.

## What problems are these four families solving?

|family|The most distinctive design orientation|representative ability|Risk points to check first|
|---|---|---|---|
| Command R |For enterprise search and tool invocation|RAG, references, long context, multi-step tool usage|Non-Commercial License and API Version Differences|
| Mistral |Covering small dense to sparse MoE with efficient architecture|Local deployment, MoE, code and multi-modal branches|Licenses vary greatly between models|
| Phi |Improve small model capability density with high-quality and synthetic data|Small deployment, inference, client-side applications|Knowledge coverage and reliability boundaries of small models|
| Llama |Form a common basic model, command model and ecological tool chain|Multi-size, multi-language, fine-tuning and deployment ecology|Custom community licenses and generational differences|

## Reading route

1. [How to distinguish open source code, open weights and open training](01-open-source-open-weight.md)
2. [Command R: Model](02-command-r.md) designed around RAG and tool usage
3. [Mistral: dense, MoE and multi-branch model family](03-mistral.md)
4. [Phi: Data quality in exchange for small model capability density](04-phi.md)
5. [Llama: From research release to universal open weight ecosystem](05-llama.md)
6. [Horizontal comparison of architecture, context, training objectives and deployment](06-technical-comparison.md)
7. [How to select model](07-selection-guide.md) by task, computing power and license
8. [Conclusion, limitations and continuous update method](08-conclusion.md)
9. [Official information and representative paper](references.md)

## Scope of this topic

The model family continues to be updated. Instead of listing every date version on the official website into a product catalog, we select representative nodes that can explain the evolution of the family, and record the data verification date as **August 4, 2026**. When the item actually lands, the model card and license of the target checkpoint should be opened again.

