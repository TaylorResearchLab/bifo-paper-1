## Supplementary Methods

### SM1 — Variant Processing and Gene Aggregation

**Kids First harmonized sequencing and alignment.** *[YOUR TEXT: KF harmonized GATK-haplotypecaller pipeline, GRCh38/GENCODE v39]*

**Variant quality filtering.** *[YOUR TEXT: GATK PASS, GQ≥20, DP≥10]*

**Pathogenicity classification.** *[YOUR TEXT: AutoGVP P/LP classification integrating ClinVar and modified InterVar/ACMG-AMP]*

**Population allele frequency filtering.** *[YOUR TEXT: gnomAD v3.1 MAF≤0.001 popmax threshold and rationale]*

**Gene aggregation.** For each cohort, genes harboring at least one qualifying P/LP variant in any proband were aggregated into a per-cohort gene list. Carrier count-filtered subsets requiring ≥2 or ≥3 independent probands carrying qualifying variants in the same gene were generated to assess signal stability under increasingly stringent filters.

**Background burden gene exclusion.** Twenty genes representing common carrier burden from well-characterized recessive Mendelian conditions were excluded from both cohort gene lists prior to pathway analysis. These genes are present at elevated carrier frequency in any unselected pediatric sequencing cohort at MAF ≤0.001 regardless of disease phenotype, and their inclusion would inflate background signal without contributing disease-specific biological information. The complete exclusion list is: ABCA4, BCHE, CD36, COL4A5, FLG, G6PD, GJB2, KRT71, KRT86, MYO15A, MYO1A, MYO3A, MYO7A, OBSCN, PADI3, PAH, TBL1Y, TCHH, TTN, USH2A.

**UMLS CUI resolution.** Gene symbols were mapped to UMLS Concept Unique Identifiers (CUIs) for use as pipeline seed inputs using `seed_cui_lookup.py`, which queries the DDKG for HGNC-SAB concept nodes matching each gene symbol. Of 1,287 CHD seed genes, 1,276 (99.1%) resolved to UMLS CUIs; of 1,406 NBL seed genes, 1,395 (99.2%) resolved. Genes failing CUI resolution were excluded from graph analysis. Final seed counts used in all reported analyses are 1,276 (KF-CHD) and 1,395 (KF-NBL).

**Output.** Seed gene files for both cohorts at all carrier-count filter levels are provided in the repository at `data/cohorts/chd/` and `data/cohorts/nbl/`.

---

### SM2 — Neo4j Export Queries

Graph neighborhoods for all benchmarks and cohort analyses were exported from the Data Distillery Knowledge Graph (DDKG) using Neo4j cypher-shell. Each export follows a four-query pattern: (1) a verification query confirming gene symbol-to-CUI resolution; (2) a node export collecting all concept nodes in the 1-hop neighborhood with SAB-priority resolution; (3) an edge export collecting seed↔neighbor edges; and (4) a targeted pathway membership edge export collecting gene-to-pathway edges within the neighborhood. Exported CSV files are cleaned using `clean_cypher_output.py` to remove cypher-shell formatting artifacts before pipeline ingestion.

All query files are provided in the repository at `cypher/`. The four-query structure is shared across all exports; cohort-specific files differ only in the seed CUI list and output file names.

**Node SAB priority ordering.** All node export queries resolve each concept to a single source vocabulary (SAB) using a CASE-ordered preference: HGNC (0) > NCBIGENE (1) > MSIGDB (2) > REACTOME (3) > GO (4) > MONDO (5) > OMIM (6) > all others (99). This ordering ensures that gene concepts resolve to their HGNC identifier when available, which is required for entity class assignment in `bifo_conditioning.py`.

**Edge filtering.** All edge export queries exclude `CODE`, `PREF_TERM`, `STY`, and `ISA` relationship types, which carry graph infrastructure rather than biological content. These are the same relationship types excluded during BIFO conditioning; excluding them at export reduces file size without affecting downstream results.

**Pathway membership edges.** Pathway membership edges connect two hop-1 nodes (a pathway concept and a gene concept) and are therefore absent from the seed↔hop1 edge export. They are collected in a separate targeted query using six membership predicates: `pathway_associated_with_gene`, `inverse_pathway_associated_with_gene`, `has_signature_gene`, `inverse_has_signature_gene`, `process_involves_gene`, and `gene_plays_role_in_process`. These predicates correspond to the Pathway Contribution flow class in BIFO and are the structural bridge edges between the mechanistic gene layer and the pathway annotation layer.

**Post-export merge.** After cleaning, edge files are merged using pandas concat (not shell cat) to preserve CSV headers and avoid duplicate header rows. For KF cohort runs the merge combines the raw edge file, the pathway membership edge file, and any NCC cilia membership edges into a single `edges_all.csv` input for `bifo_conditioning.py`. Merge commands are documented in comments at the end of each cypher file.

**Export files by benchmark:**

| File | Benchmark / cohort | Seed CUIs | Notes |
|------|--------------------|-----------|-------|
| `chd_curated_export_queries.cypher` | CHD curated benchmark | 15 CUIs (10 seeds + 5 heldout) | CUIs verified and listed in file header |
| `c4_notch_export_queries.cypher` | C4/Notch pathway-split control | 44 CUIs (30 seeds + 14 heldout) | REACTOME_SIGNALING_BY_NOTCH members |
| `c4_mapk_export_queries.cypher` | C4/MAPK pathway-split control | 91 CUIs (63 seeds + 28 heldout) | REACTOME_MAPK_FAMILY_SIGNALING_CASCADES members |
| `kf_chd_export_queries.cypher` | KF-CHD cohort | 1,276 seed CUIs | Generated by `generate_export_cypher.py` from seed list |
| `kf_nbl_export_queries.cypher` | KF-NBL cohort | 1,395 seed CUIs | Generated by `generate_export_cypher.py` from seed list |

**Note on KF cohort query generation.** The KF cohort cypher files were generated programmatically from CUI-resolved seed lists using `generate_export_cypher.py` rather than hand-authored, due to the large number of seed genes. The generated queries follow the same four-query structure as the curated benchmark files. The header comment in each KF query file records the MAF threshold and carrier-count filter parameters used to select the seed set.

---

## Supplementary Tables

*Tables ST1–ST4 will be populated from pipeline output files. ST5 consists of downloadable CSV files and is not typeset.*

### ST1 — Top-10 ranked pathways per propagation arm, curated CHD benchmark

Three-arm comparison: Full BIFO (94,309 propagating edges), Ablation (16,026 propagating edges, no Pathway Contribution bridge edges), and Mechanistic-only (9,710 edges). Pathway universe: 550 pathways (8–300 members). CHD reference set: 18 pathways. Reference pathways are indicated in the Ref. column. Full 550-pathway scores are available in `results/chd_benchmark/pathway_scores_*.csv`.

*[TABLE TO BE INSERTED — source: `BIFO_minimal_test_run_OptionC_V4/pathway_scores_*.csv`]*

Columns: Rank | Pathway name | Score (degree_norm) | Member count | Ref.

### ST2 — Full baseline enrichment comparison, curated CHD benchmark

Extends Table 4 in the main text. All five enrichment methods evaluated on the identical 550-pathway universe. Methods: B0 degree overlap, B1 seed Fisher, B2 neighborhood Fisher, B3 raw PPR GSEA, B3b conditioned PPR GSEA, B4 BIFO full-arm. CHD reference pathway membership indicated in the Ref. column.

*[TABLE TO BE INSERTED — source: `BIFO_minimal_test_run_OptionC_V4/baseline_comparison.csv`]*

Columns: Pathway name | B0 rank | B1 rank | B2 rank | B3 rank | B3b rank | B4 (BIFO) rank | Ref.

### ST3 — Top-20 ranked pathways per method, KF-CHD and KF-NBL cohorts

Five enrichment methods (BIFO full-arm, Conditioned PPR GSEA, Raw PPR GSEA, Neighborhood Fisher, Seed Fisher corrected) evaluated in discovery mode. KF-CHD (5,124 pathways scored) and KF-NBL (5,203 pathways scored) shown side by side. Cilia reference pathways indicated in the Cilia ref. column.

*[TABLE TO BE INSERTED — source: `kf_run_chd/baseline_comparison.csv` and `kf_run_nbl/baseline_comparison.csv`]*

Columns: Method | Rank | Pathway name | Score | Member count | Cilia ref.

### ST4 — Full cilia pathway cluster ranking under BIFO, KF-CHD and KF-NBL

All 22 native cilia, ciliopathy, and hedgehog pathway annotations in the scored universe, ordered by KF-CHD BIFO rank. Hub-flagged pathways (high-degree graph hubs not driven by specific cilia signal) are indicated.

*[TABLE TO BE INSERTED — source: `kf_run_chd/pathway_scores_standard.csv` and `kf_run_nbl/pathway_scores_standard.csv`]*

Columns: Pathway name | Source DB | KF-CHD BIFO rank | KF-CHD score | KF-NBL BIFO rank | KF-NBL score | Member count | Hub flag

### ST5 — Head-to-head rank comparison: seed Fisher vs. BIFO (downloadable data files)

Full ranked pathway lists for all pathways scored under both methods, for KF-CHD and KF-NBL independently. Provided as downloadable supplementary data files due to size (4,551 rows for KF-CHD; 4,633 rows for KF-NBL).

**ST5a** (`supplementary_data_ST5a_kf_chd_fisher_vs_bifo.csv`): KF-CHD, 4,551 pathways, sorted by BIFO rank.

**ST5b** (`supplementary_data_ST5b_kf_nbl_fisher_vs_bifo.csv`): KF-NBL, 4,633 pathways, sorted by BIFO rank.

Columns: pathway_name | source_db | member_count | bifo_rank | bifo_score | fisher_rank | fisher_bh_pvalue | cilia_ref_flag | hub_flag

*Source: `kf_run_chd/baseline_comparison.csv` and `kf_run_nbl/baseline_comparison.csv`*

---

## Supplementary: Code and Data Repository

All code, configuration, benchmark data, and pre-computed results supporting
this manuscript are available at:

**https://github.com/TaylorResearchLab/bifo-graph**

The repository is organized according to FAIR data principles: all benchmark
inputs are versioned and shipped with the repository; all analysis parameters
are documented in `config/bifo_ddkg_mapping.yaml` (v0.7.1); all pipeline
scripts are self-contained with documented inputs and outputs; and a
self-contained end-to-end test (`examples/minimal_test/`) is provided for
validation without requiring access to the full graph database.

### S6.1 Pipeline scripts (`pipeline/`)

| Script | Purpose | Paper section |
|--------|---------|---------------|
| `bifo_conditioning.py` | BIFO edge conditioning (entity resolution, flow class filtering) and PPR propagation. Primary analysis script. | Methods §2, §3 |
| `score_pathways.py` | Pathway scoring from PPR score vectors using degree_norm and alternative variants | Methods §4 |
| `baseline_enrichment.py` | Enrichment baselines B0–B3 (degree overlap, Fisher, neighborhood Fisher, preranked GSEA). Accepts `--kept-edges` and `--small-universe` flags | Methods §6 |
| `chd_resampling_exhaustive.py` | Exhaustive in-memory resampling over all C(15,10) = 3,003 possible 10-gene/5-gene partitions of the CHD gene pool | Methods §9 |
| `kf_resampling.py` | Bootstrap resampling for KF cohort analyses (500 draws × 3 seed sizes per cohort) | Methods §10.7 |
| `seed_cui_lookup.py` | Map HGNC gene symbols to UMLS CUIs for use as pipeline seed inputs | Methods §10.2 |
| `generate_export_cypher.py` | Generate cohort-specific Neo4j export Cypher queries from a seed gene list | Methods §10.3 |
| `build_ncc_membership_edges.py` | Build NCC/cilia pathway membership edge files from curated gene sets | Methods §10.4 |
| `build_cilia_reference.py` | Build the cilia pathway reference set by matching pathway names against cilia-related terms | Methods §10.4 |
| `clean_cypher_output.py` | Clean artifact characters introduced by cypher-shell CSV export | Methods §10.3 |

### S6.2 Shell pipeline wrappers (`scripts/`)

| Script | Stage | Purpose |
|--------|-------|---------|
| `run_full_pipeline.sh` | All | End-to-end pipeline for one cohort (chd or nbl). Calls all stage scripts in sequence |
| `setup_workspace.sh` | 0 | Create output directory structure |
| `run_kf_chd_export.sh` | 1 | Neo4j export for KF-CHD cohort |
| `run_kf_nbl_export.sh` | 1 | Neo4j export for KF-NBL cohort |
| `clean_files.sh` | 2.1 | Clean cypher-shell output CSVs |
| `build_ncc_edges.sh` | 2.2 | Build NCC/cilia membership edges |
| `merge_files.sh` | 2.3 | Merge edge CSV files into `edges_merged.csv` |
| `run_seed_lookup.sh` | 2.4 | Map gene symbols to CUIs |
| `run_conditioning.sh` | 3 | BIFO conditioning + PPR propagation |
| `run_scoring.sh` | 4 | Pathway scoring |
| `run_baseline.sh` | 5 | Baseline enrichment comparison |
| `run_resampling.sh` | 6 | Bootstrap resampling |

### S6.3 Configuration (`config/`)

| File | Description |
|------|-------------|
| `config/bifo_ddkg_mapping.yaml` | BIFO flow class definitions, v0.7.1. Contains 251 predicate-to-flow entries, 96 explicit non-flow designations, and 46 observational edge definitions across 5 classification tiers. This file is the primary scientific artifact of the BIFO framework; all conditioning results are determined by its contents |

### S6.4 Neo4j export queries (`cypher/`)

| File | Cohort/benchmark | Graph export |
|------|-----------------|--------------|
| `chd_curated_export_queries.cypher` | CHD curated benchmark | 1-hop neighborhood of 15 CHD seed and held-out genes |
| `c4_notch_export_queries.cypher` | C4/Notch control | REACTOME_SIGNALING_BY_NOTCH member neighborhood |
| `c4_mapk_export_queries.cypher` | C4/MAPK control | REACTOME_MAPK_FAMILY_SIGNALING_CASCADES member neighborhood |
| `kf_chd_export_queries.cypher` | KF-CHD cohort | 1-hop neighborhood of KF-CHD variant gene seeds |
| `kf_nbl_export_queries.cypher` | KF-NBL cohort | 1-hop neighborhood of KF-NBL variant gene seeds |

### S6.5 Benchmark and cohort data (`data/`)

**Curated CHD benchmark (`data/benchmark/`)**

| File | Description |
|------|-------------|
| `chd_curated_edges_raw.csv.zip` | 94,790 seed-centered mechanistic and association edges for the curated CHD benchmark graph |
| `chd_curated_pathway_membership_edges.csv.zip` | 79,562 gene-to-pathway membership edges (MSigDB, WikiPathways, GO) |
| `chd_pathway_reference.txt` | 18 CHD reference pathway CUIs used for evaluation |
| `c4_notch_seed_nodes.txt` | 30 HGNC gene CUIs — 70% split of REACTOME_SIGNALING_BY_NOTCH members (numpy seed=42) |
| `c4_notch_heldout_nodes.txt` | 14 held-out gene CUIs — 30% split of REACTOME_SIGNALING_BY_NOTCH |
| `c4_notch_pathway_reference.txt` | 11 Notch-family reference pathway CUIs |
| `c4_mapk_seed_nodes.txt` | 63 HGNC gene CUIs — 70% split of REACTOME_MAPK_FAMILY_SIGNALING_CASCADES |
| `c4_mapk_heldout_nodes.txt` | 28 held-out gene CUIs — 30% split of REACTOME_MAPK_FAMILY_SIGNALING_CASCADES |
| `c4_mapk_pathway_reference.txt` | 10 MAPK-family reference pathway CUIs |

**KF-CHD cohort (`data/cohorts/chd/`)**

| File | Description |
|------|-------------|
| `kf_chd_seeds_maf001.txt` | Primary seed gene list: 1,287 HGNC genes with AutoGVP P/LP variants at MAF ≤0.001, n≥1 carrier (primary analysis) |
| `kf_chd_seeds_maf001_n2.txt` | Carrier-filtered seeds: 387 genes with n≥2 carriers at MAF ≤0.001 |
| `kf_chd_seeds_maf001_n3.txt` | Carrier-filtered seeds: 146 genes with n≥3 carriers at MAF ≤0.001 |
| `kf_chd_seeds_maf01.txt` | Broader-filter seeds at MAF ≤0.01 |
| `kf_chd_seeds.txt` | Original unfiltered seed gene list |
| `kf_chd_seed_cuis.txt` | CUI-resolved seed list (pipeline input for conditioning) |
| `kf_chd_seed_nodes.csv.zip` | Full seed node metadata from DDKG export |
| `kf_chd_ncc_reference.txt` | NCC cilia pathway reference set for KF-CHD evaluation |

**KF-NBL cohort (`data/cohorts/nbl/`)**

| File | Description |
|------|-------------|
| `kf_nbl_seeds_maf001.txt` | Primary seed gene list: 1,406 HGNC genes with AutoGVP P/LP variants at MAF ≤0.001, n≥1 carrier |
| `kf_nbl_seeds_maf001_n2.txt` | Carrier-filtered seeds: 401 genes with n≥2 carriers at MAF ≤0.001 |
| `kf_nbl_seeds_maf001_n3.txt` | Carrier-filtered seeds: 147 genes with n≥3 carriers at MAF ≤0.001 |
| `kf_nbl_seeds_maf01.txt` | Broader-filter seeds at MAF ≤0.01 |
| `kf_nbl_seeds.txt` | Original unfiltered seed gene list |
| `kf_nbl_ncc_reference.txt` | NCC cilia pathway reference set for KF-NBL evaluation |

### S6.6 Pre-computed results (`results/`)

**CHD benchmark (`results/chd_benchmark/`)**

| File | Description |
|------|-------------|
| `chd_resampling_summary.json` | Summary statistics for all 3,003 exhaustive CHD seed-split results: per-metric distributions (mean, SD, min, P25, median, P75, max), robustness counts, and primary split percentile ranks |

**KF-CHD conditioning outputs (`results/kf_chd/`)**

| File | Description |
|------|-------------|
| `results.json` | Four-arm PPR gene-level recovery metrics (AUROC, AUPRC, entropy, nonzero fraction) |
| `results_node_index.json` | Node CUI → matrix index mapping for score vector interpretation |
| `results_kept_edges.csv.zip` | BIFO-conditioned kept edges with flow class and propagating flag annotations |
| `results_scores_cond.npy` | Conditioned (BIFO full-arm) PPR score vector |
| `results_scores_raw.npy` | Raw (unconditioned) PPR score vector |
| `results_scores_meta.npy` | Metadata-filtered PPR score vector |
| `results_scores_rand.npy` | Random sparsification control PPR score vector |

### S6.7 Minimal test (`examples/minimal_test/`)

A self-contained end-to-end validation run using a 15-gene CHD seed set. Does
not require a Neo4j connection for the scoring stages. Running `bash run_test.sh`
from this directory executes BIFO conditioning and pathway scoring and writes
outputs to `test_output/`. Expected outputs and success criteria are documented
in `examples/minimal_test/README.md`.

### S6.8 FAIR compliance notes

**Findable:** Repository is publicly available at
https://github.com/TaylorResearchLab/bifo-graph with a persistent DOI via
Zenodo (DOI: TBD at publication).

**Accessible:** All benchmark data and pre-computed results are available
without authentication. KF cohort variant data requires dbGaP authorization
(phs001138, phs001436) per Kids First data access policy.

**Interoperable:** Edge and node files use standard CSV format with documented
column headers. Score vectors use NumPy binary format (.npy). Configuration uses
YAML. All file formats are documented in this supplement and in the repository
README.

**Reusable:** The BIFO conditioning operator (`bifo_conditioning.py`) and YAML
mapping (`bifo_ddkg_mapping.yaml`) are graph-agnostic and can be applied to any
property graph whose edges carry DDKG-compatible predicates. Code is released
under MIT License; benchmark data under CC BY 4.0.
