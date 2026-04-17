# bifo-paper-1

**BIFO: A Biological Information Flow Ontology for Knowledge Graph-Directed Pathway Analysis of Rare Variant Cohort Data**

Deanne M. Taylor, Benjamin Stear, Taha Mohseni Ahooyi, Yuanchao Zhang, Aditya Lahiri

Department of Biomedical Informatics, Children's Hospital of Philadelphia  
Department of Pediatrics, University of Pennsylvania Perelman School of Medicine (DMT)

---

## Manuscript

This repository uses [Manubot](https://manubot.org/) for collaborative manuscript management.
All content is in the `content/` directory as Markdown files.
The manuscript is built automatically on every push via GitHub Actions.

| File | Content |
|------|---------|
| `content/01.abstract.md` | Abstract |
| `content/02.introduction.md` | Introduction |
| `content/03.methods.md` | Methods (Sections 1–10) |
| `content/04.results.md` | Results (Sections 1–8) |
| `content/05.discussion.md` | Discussion |
| `content/06.references.md` | References |
| `content/metadata.yaml` | Authors, title, keywords |

## Code

All pipeline code is in the companion repository:
[TaylorResearchLab/bifo-graph](https://github.com/TaylorResearchLab/bifo-graph)

## Status

| Section | Status |
|---------|--------|
| Methods 1–9 (curated CHD benchmark) | Complete |
| Methods 10 (KF cohort) | Complete |
| Results 1–7 (curated CHD benchmark) | Complete |
| Results 8.1–8.2 (KF-CHD) | Complete — pending Supp tables S3–S5 |
| Results 8.3 (cross-cohort) | Pending NBL pipeline results |
| Introduction | Outline only |
| Abstract | Pending |
| Discussion | Outline only |

## Building locally

```bash
# Install manubot
pip install manubot

# Build the manuscript
manubot process --content-directory=content --output-directory=output --cache-directory=ci/cache

# Or just view the auto-built version at the GitHub Pages URL after CI runs
```

## Citation

<!-- To be added upon preprint/publication -->
