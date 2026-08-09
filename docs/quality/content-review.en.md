#Content verification record

Update time: 2026-06-08

## This round has been processed

- Restore maintainable MkDocs source code from the `gh-pages` release product to avoid the problem that the main branch only has README and the content only exists in the release branch.
- Split the four large files `score`, `polytomous`, `binary`, and `scale` into chapter directories and subsection files according to secondary themes.
- Corrected the local independence formula, dichotomous response mode likelihood notation, Q3 baseline explanation, and expression of alpha and dimensionality in the IRT model fit page.
- Updated the Shiny official link to the current entrance of Posit Shiny, and adjusted the topic suggestion from the single `shinythemes` to the priority description `bslib`.
- Fixed examples of easily misleading practices such as runtime installation packages, Chinese encoding, hard-coded passwords, and GitHub Actions executing R code in the Shiny deployment page.
- Clean up the obviously colloquial titles and descriptions on the Shiny entry page and Day 1/Day 2.
- Clean up missing image references; retained images have been checked by browser loading.
- Unify MathJax syntax, disable `$...$` inline formula parsing to avoid Shiny code misjudgments, and standardize blank lines before and after block-level formulas.
- Correct the code fence configuration to prevent code block tags such as ` ```r `, ` ```text ` from appearing directly in the page body.
- Adjust the CSS of tables, code blocks, block-level formulas and inline formulas so that they can be read normally on both desktop and mobile devices.
- Remove the CAT partition and its three old manuscripts according to maintenance requirements to prevent low-quality content from continuing to be published.

## This round of rendering verification

- `mkdocs build --strict`: Passed.
- Desktop viewport `1280×720`: The browser actually loaded 74 internal pages and found no broken images, MathJax errors, exposed LaTeX syntax, exposed code fences, CAT old page links, or page-level overflows.
- Mobile viewport `390×844`: The browser actually loads the same 74 internal pages, and no broken images, MathJax errors, exposed LaTeX syntax, exposed code fences, CAT old page links or page-level overflows are found; wide tables and long formulas are handled with local horizontal scrolling.

##Partition status

|Partition|Status of this round|Remarks|
| --- | --- | --- |
|psychometrics basics|Preliminary review of structure and terminology has been done|It is recommended to provide supplementary textbook page numbers or DOIs for key definitions in the future.|
|Bipartite IRT model|Split and retained formula|Follow-up suggestions are to check the source of the chart item by item.|
|multinomial IRT model|Split and retained formula|The model formula needs to be reviewed according to the original text of Samejima, Masters and Muraki|
| R Shiny |Major practical issues fixed|`renv` sample item can be added later|
|CTT/IRT rules|Source code restored|You can continue to change the rule into a three-stage formula of "Conclusion-Condition-Example"|

## Subsequent proofreading standards

Every time you add or modify a knowledge point, it is recommended to check in the following order:

1. Whether the definition comes from traceable textbooks, papers or official documents.
2. Whether the formula mark is consistent with the context of the current page.
3. Whether the sample code can run under the current recommended version.
4. Whether the statement explains the applicable conditions and avoid writing empirical rules into absolute conclusions.
5. Does the page need to include references or "note" prompts?
