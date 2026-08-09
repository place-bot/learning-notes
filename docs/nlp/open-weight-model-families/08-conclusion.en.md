# Conclusion, limitations and continuous updates

## 1. The main technical lines of the four families

- **Command R** Centers RAG, references and tool calls on the training target;
- **Mistral** demonstrates the efficiency combination of dense, local attention, GQA and sparse MoE;
- **Phi** Study how high-quality and synthetic data can improve the capability density of small models;
- **Llama** forms a broad open weight ecosystem covering pretraining, alignment, fine-tuning, quantification and deployment.

They can be candidates for each other in the same item, or they can assume different roles. For example, use small Phi for local classification, Command R for knowledge base Q&A with citations, and Llama or Mistral for parts that require more general generation.

## 2. Conclusion of the most important terms

"Callable", "code public", "weights downloadable", "commercial use allowed" and "training reproducible" are five different issues. A model brand is not a license either. Accurate writing should always include specific checkpoints and permission status.

## 3. Unsolved parts of this topic

- Not exhaustive of all date versions and regional API aliases in 2026;
- There is no re-scoring of the four families on unified hardware;
- The license description is for preliminary screening of research and projects and does not constitute legal advice;
- The details of the officially disclosed training data are different, making it impossible to make a completely symmetrical comparison of data sources;
- The base, instruct, reasoning and multimodal version abilities of the same family are not interchangeable.

## 4. Method of continuously updating model cards

Appending only the "latest model" with each update will cause the page to lose structure quickly. A more reliable maintenance method is:

1. Preserve stable comparison dimensions: architecture, data, alignment, context, deployment and license;
2. Each family chooses a milestone version that explains the paradigm change;
3. Only link to the official model overview for rapidly changing product lists;
4. Attach the model card date or version to all precise figures;
5. When the old version is retired, its academic role will be retained, and the service status will be noted;
6. Put new models into the same review protocol rather than just accept incomparable rankings between vendors.

In this way, readers can not only understand why the model is designed in this way, but also continue to use the same analysis framework after future versions appear.

