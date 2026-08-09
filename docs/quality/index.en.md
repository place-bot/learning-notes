# Quality and Maintenance

This section records the proofreading, reference materials and subsequent maintenance of website content. It's not a thread of knowledge, but it's important for ensuring the long-term usability of the web page.

## Current page

1. [Content verification record](content-review.md): Record pages that have been checked, problems that have been fixed, and content that still needs to be reviewed.
2. [References](../references.md): Centralize general references and sources that can be supplemented later.

## Maintenance focus

|item|Check content|
| --- | --- |
|rendering|Whether Markdown tables, code blocks, formulas and pictures are displayed normally|
|content|Are concepts, formulas, terms, and examples accurate?|
|Navigation|Whether the newly added page enters `mkdocs.yml` and whether it can be accessed from the sidebar|
|structure|Is the single page too long and needs to be split into smaller chapters?|
|Reference|Whether the sources for papers, books, and software documents are complete|

## Follow-up rules

- When adding a topic, create an overview page first, and then gradually add sub-pages.
- Check in-site links after each page move.
- Run `mkdocs build --strict` before each commit.
- Formulas, tables and code blocks must be actually rendered for inspection after modification.
