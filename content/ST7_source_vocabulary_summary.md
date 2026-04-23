### ST7: Source vocabulary (SAB) contributions to BIFO-PPR analyses


Source vocabularies (SABs) identified as source nodes in BIFO-conditioned kept_edges files. SAB attribution is based on the source node of each edge as resolved by the DDKG node SAB field. Only SABs with at least one edge across any analysis are shown. Predicate count reflects unique predicate types contributed by that SAB as source node. Edges where the source node SAB could not be resolved (UNKNOWN) are excluded. The dominant SAB is HGNC because gene concept nodes — the primary seed and propagation entity — resolve to HGNC identifiers under the node SAB priority ordering used in the Cypher export queries.

| Source SAB | Source description | Unique predicates | Benchmark edges | KF-CHD edges | KF-NBL edges |
|------------|-------------------|:-----------------:|----------------:|-------------:|-------------:|
| HGNC | Hugo Gene Nomenclature Committee | 89 | 52,516 | 2,014,741 | 2,176,916 |
| GO | Gene Ontology | 2 | 2,044 | 13,341 | 13,394 |
| NCI | NCI Thesaurus | 6 | 1,083 | 7,703 | 7,831 |
| SNOMEDCT_US | SNOMED CT | 4 | 70 | 247 | 253 |
| MSH | MeSH (Medical Subject Headings) | 5 | 37 | 89 | 82 |
| OMIM | Online Mendelian Inheritance in Man | 4 | 1,248 | 4 | 16 |
| PUBCHEM | PubChem | 3 | 379 | 7 | 7 |
| MONDO | MONDO Disease Ontology | 9 | 980 | — | 1 |
| GS | Gene Symbol vocabulary | 2 | 18 | — | — |
| MMSL | Multum MediSource Lexicon | 2 | 22 | — | — |
| CHEBI | ChEBI | 2 | 24 | — | — |
| HP | Human Phenotype Ontology | 2 | 1,831 | — | — |
| DRUGBANK | DrugBank | 2 | 44 | — | — |