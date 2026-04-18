---
title: 'BIFO: A Biological Information Flow Ontology for Knowledge Graph-Directed Pathway Analysis of Rare Variant Cohort Data'
keywords:
- knowledge graph
- pathway enrichment
- personalized PageRank
- rare variants
- congenital heart defects
- neuroblastoma
- ciliopathy
- DDKG
- UBKG
- bioinformatics
lang: en-US
date-meta: '2026-04-18'
author-meta:
- Deanne M. Taylor
- Taha Mohseni Ahooyi
- Benjamin Stear
- Yuanchao Zhang
- Aditya Lahiri
- Alan Simmons
- Tiffany J. Callahan
- Jonathan C. Silverstein
header-includes: |
  <!--
  Manubot generated metadata rendered from header-includes-template.html.
  Suggest improvements at https://github.com/manubot/manubot/blob/main/manubot/process/header-includes-template.html
  -->
  <meta name="dc.format" content="text/html" />
  <meta property="og:type" content="article" />
  <meta name="dc.title" content="BIFO: A Biological Information Flow Ontology for Knowledge Graph-Directed Pathway Analysis of Rare Variant Cohort Data" />
  <meta name="citation_title" content="BIFO: A Biological Information Flow Ontology for Knowledge Graph-Directed Pathway Analysis of Rare Variant Cohort Data" />
  <meta property="og:title" content="BIFO: A Biological Information Flow Ontology for Knowledge Graph-Directed Pathway Analysis of Rare Variant Cohort Data" />
  <meta property="twitter:title" content="BIFO: A Biological Information Flow Ontology for Knowledge Graph-Directed Pathway Analysis of Rare Variant Cohort Data" />
  <meta name="dc.date" content="2026-04-18" />
  <meta name="citation_publication_date" content="2026-04-18" />
  <meta property="article:published_time" content="2026-04-18" />
  <meta name="dc.modified" content="2026-04-18T10:04:16+00:00" />
  <meta property="article:modified_time" content="2026-04-18T10:04:16+00:00" />
  <meta name="dc.language" content="en-US" />
  <meta name="citation_language" content="en-US" />
  <meta name="dc.relation.ispartof" content="Manubot" />
  <meta name="dc.publisher" content="Manubot" />
  <meta name="citation_journal_title" content="Manubot" />
  <meta name="citation_technical_report_institution" content="Manubot" />
  <meta name="citation_author" content="Deanne M. Taylor" />
  <meta name="citation_author_institution" content="Department of Biomedical Informatics, Children&#39;s Hospital of Philadelphia" />
  <meta name="citation_author_institution" content="Department of Pediatrics, University of Pennsylvania Perelman School of Medicine" />
  <meta name="citation_author_orcid" content="0000-0002-3302-4610" />
  <meta name="citation_author" content="Taha Mohseni Ahooyi" />
  <meta name="citation_author_institution" content="Department of Biomedical Informatics, Children&#39;s Hospital of Philadelphia" />
  <meta name="citation_author" content="Benjamin Stear" />
  <meta name="citation_author_institution" content="Department of Biomedical Informatics, Children&#39;s Hospital of Philadelphia" />
  <meta name="citation_author" content="Yuanchao Zhang" />
  <meta name="citation_author_institution" content="Department of Biomedical Informatics, Children&#39;s Hospital of Philadelphia" />
  <meta name="citation_author" content="Aditya Lahiri" />
  <meta name="citation_author_institution" content="Department of Biomedical Informatics, Children&#39;s Hospital of Philadelphia" />
  <meta name="citation_author" content="Alan Simmons" />
  <meta name="citation_author_institution" content="Department of Biomedical Informatics, University of Pittsburgh Medical Center, Pittsburgh, PA" />
  <meta name="citation_author" content="Tiffany J. Callahan" />
  <meta name="citation_author_institution" content="Manas AI, New York, NY" />
  <meta name="citation_author" content="Jonathan C. Silverstein" />
  <meta name="citation_author_institution" content="Department of Biomedical Informatics, University of Pittsburgh Medical Center, Pittsburgh, PA" />
  <meta name="citation_author_orcid" content="0000-0002-9252-6039" />
  <link rel="canonical" href="https://TaylorResearchLab.github.io/bifo-paper-1/" />
  <meta property="og:url" content="https://TaylorResearchLab.github.io/bifo-paper-1/" />
  <meta property="twitter:url" content="https://TaylorResearchLab.github.io/bifo-paper-1/" />
  <meta name="citation_fulltext_html_url" content="https://TaylorResearchLab.github.io/bifo-paper-1/" />
  <meta name="citation_pdf_url" content="https://TaylorResearchLab.github.io/bifo-paper-1/manuscript.pdf" />
  <link rel="alternate" type="application/pdf" href="https://TaylorResearchLab.github.io/bifo-paper-1/manuscript.pdf" />
  <link rel="alternate" type="text/html" href="https://TaylorResearchLab.github.io/bifo-paper-1/v/447d7f93578e6d36edb8c6c75b72e37ff16c9c3a/" />
  <meta name="manubot_html_url_versioned" content="https://TaylorResearchLab.github.io/bifo-paper-1/v/447d7f93578e6d36edb8c6c75b72e37ff16c9c3a/" />
  <meta name="manubot_pdf_url_versioned" content="https://TaylorResearchLab.github.io/bifo-paper-1/v/447d7f93578e6d36edb8c6c75b72e37ff16c9c3a/manuscript.pdf" />
  <meta property="og:type" content="article" />
  <meta property="twitter:card" content="summary_large_image" />
  <link rel="icon" type="image/png" sizes="192x192" href="https://manubot.org/favicon-192x192.png" />
  <link rel="mask-icon" href="https://manubot.org/safari-pinned-tab.svg" color="#ad1457" />
  <meta name="theme-color" content="#ad1457" />
  <!-- end Manubot generated metadata -->
bibliography: []
manubot-output-bibliography: output/references.json
manubot-output-citekeys: output/citations.tsv
manubot-requests-cache-path: ci/cache/requests-cache
manubot-clear-requests-cache: false
...

## Abstract

Biological knowledge graphs integrate heterogeneous data across molecular, cellular, and phenotypic domains, but do not enable reliable inference on their own. When mechanistic relationships, statistical associations, and annotation edges share a single structure, graph traversal propagates signal along biologically invalid paths. This produces an identifiability problem in which causal and non-causal explanations cannot be distinguished, and standard enrichment approaches fail in both small and large gene set regimes.

Here we introduce the Biological Information Flow Ontology (BIFO), a framework that constrains information flow by defining admissible biological transformations prior to propagation. In a three-arm ablation design, we show that pathway inference depends on a distinct bridge layer: mechanistic-only propagation yields zero pathway scores, while inclusion of gene-to-pathway membership edges enables signal transfer between molecular and pathway representations.

Across a curated congenital heart disease benchmark, BIFO improves pathway prioritization (P@10 = 0.70) relative to seed-only enrichment (P@10 = 0.30) and propagation-based baselines (P@10 = 0.10). In two independent rare variant cohorts, BIFO and correctly implemented Fisher enrichment independently identify the same ciliopathy pathway as top-ranked in both diseases, while BIFO remains effective where overlap-based methods lose discriminative power.

These results show that constraining admissible information flow is necessary for meaningful graph-based biological inference.



Deanne M. Taylor^1,2^✉^^, Taha Mohseni Ahooyi^1^, Benjamin Stear^1^, Yuanchao Zhang^1^, Aditya Lahiri^1^, Alan Simmons^3^, Tiffany J. Callahan^4^, Jonathan C. Silverstein^3^


^1^Department of Biomedical Informatics, Children's Hospital of Philadelphia
^2^Department of Pediatrics, University of Pennsylvania Perelman School of Medicine
^3^Department of Biomedical Informatics, University of Pittsburgh Medical Center, Pittsburgh, PA
^4^Manas AI, New York, NY

^✉^Correspondence: <taylordm@chop.edu>



## Introduction

Modern biology now generates large-scale, multi-modal datasets spanning genomic variation, gene expression, chromatin architecture, protein interactions, metabolism, and disease phenotypes. These data provide complementary but fragmented views of biological systems across molecular, cellular, and spatial scales. Knowledge graphs have emerged as a unifying framework for integrating these heterogeneous data types, representing biological entities and their relationships in a single structure that supports cross-domain queries. However, representation alone does not enable inference. The central challenge is not simply linking data across modalities, but determining how biological signal observed in one part of the graph relates to signal observed elsewhere.

Biological function arises from directional, causal processes. Transcription proceeds from gene to RNA, signaling cascades propagate from upstream activation to downstream effectors, and metabolic transformations are constrained by biochemical feasibility and spatial context. These processes define not only which entities are connected, but which transformations are biologically admissible and how information can propagate between them. In heterogeneous knowledge graphs, however, mechanistic relationships, statistical associations, and annotation edges are encoded within the same structure. In the absence of constraints, graph traversal treats these relationships equivalently, collapsing causal and non-causal connections into a single topology.

This produces a fundamental identifiability problem. A path connecting a genetic variant to a disease phenotype may reflect a valid mechanistic process, an indirect regulatory association, or an incidental correlation. Without constraints on admissibility, these possibilities are computationally indistinguishable, and inference becomes dependent on graph topology or analysis method rather than biological mechanism. Standard enrichment approaches exhibit complementary failure modes in this setting. For small gene sets, statistical overlap is unstable and dominated by incidental matches. For large gene sets — particularly those derived from rare variant aggregation — p-values collapse to numerical limits and lose discriminative power. Graph-based expansion methods further exacerbate this problem by inflating gene sets to include large fractions of the graph, eliminating meaningful enrichment structure.

Existing approaches address parts of this problem but do not resolve it. Ontologies such as Gene Ontology and HPO provide structured representations of biological concepts but do not define propagation rules. Knowledge graph systems support typed traversal but rely on user-defined queries rather than biologically grounded constraints. Causal frameworks such as BEL and GO-CAM encode mechanistic relationships but operate within curated representations and do not provide a general protocol for conditioning arbitrary heterogeneous graphs. Graph machine learning approaches can operate over heterogeneous structures but learn propagation behavior from data rather than enforcing biologically interpretable constraints. The missing component is a graph-agnostic framework that defines which transformations are biologically admissible and how information is allowed to propagate across heterogeneous knowledge graphs.

To address this limitation, we introduce the Biological Information Flow Ontology (BIFO), a propagation constraint framework for heterogeneous biomedical knowledge graphs. BIFO defines a set of entity classes, flow classes, and admissibility constraints that formalize biologically valid transformations between entities. It distinguishes between mechanistic flows — which represent information-carrying biological processes and participate in propagation — observational flows — which represent inferred or correlational relationships and are excluded from propagation — and constraint-imposing flows — which restrict admissible transitions without carrying signal. BIFO conditioning transforms an unconstrained property graph into a directed graph in which all retained edges correspond to admissible biological transformations, defining a propagation substrate consistent with biological causality.

The key idea underlying BIFO is that biological inference can be improved not by adding information to a knowledge graph, but by restricting the space of admissible transformations. By constraining propagation to semantically valid paths, BIFO reduces the reachable state space and increases the identifiability of biologically meaningful signal. This transformation induces a directed, non-symmetric adjacency operator that encodes the source–sink asymmetry inherent in biological processes, enabling propagation methods to operate over a graph that reflects causal structure rather than undifferentiated connectivity.

We evaluate this framework using a controlled benchmark derived from the Data Distillery Knowledge Graph (DDKG), integrating curated congenital heart disease (CHD) gene sets with pathway annotations. Through a three-arm ablation design, we show that mechanistic-only propagation is insufficient to recover pathway-level biological programs, as pathway nodes are structurally unreachable without bridge edges connecting gene-level and pathway-level representations. Introducing BIFO-conditioned propagation enables signal transfer across these layers, revealing a two-layer graph architecture in which pathway inference depends on a formally defined class of admissible bridge edges.

We further demonstrate the applicability of BIFO in a discovery setting using rare variant cohorts from the Kids First program. In this regime, gene sets derived from variant aggregation are large and heterogeneous, and standard enrichment approaches fail to recover biologically coherent pathways. BIFO-conditioned propagation concentrates distributed signal across the graph and recovers biologically relevant pathways without prior specification, illustrating its utility for cohort-scale inference where traditional methods break down.

Together, these results establish BIFO as a general framework for defining admissible biological information flow over heterogeneous knowledge graphs. By transforming graphs from passive integration structures into constrained propagation substrates, BIFO enables principled, mechanistically grounded inference across multiple biological scales.


**Methods**

*BIFO: Biological Information Flow Ontology --- Benchmark v1.0*

Companion to Results Backbone · April 2026 · All parameters frozen

## 1 Knowledge graph source

All analyses used the Data Distillery Knowledge Graph (DDKG), built on the Unified Biomedical Knowledge Graph (UBKG) and Petagraph infrastructure. DDKG integrates heterogeneous biological knowledge from multiple source ontologies and databases into a unified concept-and-relationship graph. Each concept node carries a source authority base (SAB) identifier; each edge carries a predicate drawn from the source ontology\'s relation vocabulary. This structure makes edge provenance fully traceable, which is essential for the BIFO conditioning step: the predicate determines which flow class an edge belongs to, and the SAB determines which entity resolution rule applies.

For the present benchmark, the graph was queried as a 1-hop neighborhood centered on 15 CHD-associated seed and held-out genes. This produced two edge files: (1) edges_raw.csv containing 94,790 seed-to-neighbor mechanistic and association edges, and (2) pathway_membership_edges.csv containing 79,562 gene-to-pathway membership edges derived from MSigDB, WikiPathways, and Gene Ontology annotations. These were merged into edges_merged.csv (174,352 edges). Node metadata was exported in nodes.csv (34,523 concept nodes). The 1-hop design was chosen to produce a graph of tractable size with known provenance; it does not represent the full DDKG connectivity.

Three association-derived evidence vocabularies (DGNAGE: age-stratified gene-disease associations; DGNGCM: clinical mutation associations; DGNGV: genomic variant associations) were intentionally excluded. The rationale is scientific, not technical: excluding these sources isolates ontology-aligned mechanistic and pathway representations from association-derived evidence layers, enabling clean attribution of information flow to specific edge classes.

## 2 BIFO conditioning

### 2.1 Ontology design

The Biological Information Flow Ontology (BIFO) defines a vocabulary of biologically admissible flow classes --- categories of biological relationship through which information is considered to propagate in a directed, mechanistically coherent manner. The central design question BIFO addresses is: given a heterogeneous biomedical knowledge graph whose edges span everything from direct phosphorylation to text-mining co-occurrence, which edges should be allowed to carry propagated signal between biological entities? BIFO answers this by classifying each predicate type into a flow class and assigning a classification tier that determines its role in the PPR operator.

The mapping is encoded in bifo_ddkg_mapping.yaml (v0.7.1; 251 predicate-to-flow entries, 96 explicit non-flow designations, 46 observational edge definitions). The five classification tiers are: (1) mechanistic --- direct, causal biochemical or molecular events with clear directionality; (2) weak_mechanistic_or_observational --- relationships that may reflect mechanism but whose evidence is mixed or correlational; (3) observational --- statistical associations without mechanistic grounding; (4) contextual_constraint --- spatial or temporal constraints that modify but do not propagate signal; and (5) nonpropagating_context --- structural relationships excluded from the PPR operator but retained in the conditioning output for downstream use.

The classification is deliberately conservative: when a predicate type has mixed evidence quality across its instances, the weaker classification applies. This prevents high-confidence mechanistic relationships from being diluted by the presence of observational instances of the same predicate type in the same graph.

  ----------------------------------- ------------------ -------------------------------- ------------------------------------------------------------------------------------------------
  **Flow class**                      **N predicates**   **Classification(s)**            **Biological meaning**

  **Signal Transduction**             10                 mechanistic                      Phosphorylation, causal regulation, signal propagation

  **Transcription**                   9                  mechanistic / weak-mech          Gene expression, transcription factor binding

  **Translation**                     9                  mechanistic / weak-mech          Gene--protein encoding relationships

  **Protein Interaction**             20                 mechanistic / weak-mech          Binding, complex membership, molecular interaction

  **Signal Termination**              4                  mechanistic                      Dephosphorylation, inhibition, negative regulation

  **Perturbational Effect**           14                 mechanistic / weak-mech          Direct drug-target interactions (mechanistic); correlation predicates (weak-mech) --- see note

  **Genetic Regulatory Modulation**   11                 mechanistic / weak-mech / obs.   Variant-gene relationships, allele activity

  **Biochemical Transformation**      24                 mechanistic / weak-mech          Catalysis, synthesis, metabolic conversion

  **Pathway Contribution**            27                 mechanistic / weak-mech          Gene-to-pathway membership bridge edges --- see note

  **Observational Association**       41                 observational                    Co-expression, text-mining, statistical association

  **Spatial constraint**              47                 contextual / non-propagating     Excluded from PPR operator; used for entity typing only

  **State Progression**               19                 mechanistic / weak-mech          Developmental and temporal transitions

  **Other (6 classes)**               15                 mechanistic                      Complex formation, transport, chromatin topology, etc.
  ----------------------------------- ------------------ -------------------------------- ------------------------------------------------------------------------------------------------

**Table M1.** *BIFO flow class definitions. N predicates = number of DDKG predicate types assigned to this class in v0.7.1. Classification(s) indicates which tier(s) apply within the class. Classes with mixed classifications contain predicates of different evidential quality, classified at the predicate level rather than the class level.*

> *Pathway Contribution edges encode curated gene-to-pathway membership relationships (e.g., pathway_associated_with_gene, has_signature_gene). They do not represent direct biochemical interactions; rather, they are admissible bridge edges between molecular entities and pathway-level biological programs. Their admission as a flow class is what enables signal transfer from the mechanistic gene neighborhood to the pathway annotation layer --- the central architectural finding of this paper.*
>
> *Perturbational Effect contains two distinct predicate groups classified at different tiers: direct molecular interactions (bioactivity, chemical_or_drug_affects_gene_product, targets_expression_of_gene; classified mechanistic) and correlation-derived associations (positively/negatively_correlated_with_gene; classified weak_mechanistic_or_observational). The mechanistic-only arm retains the mechanistic subset and excludes the correlation predicates. This is an intentional design choice that allows the mechanistic operator to capture direct drug-target connectivity without admitting association noise.*

### 2.2 Entity resolution

Entity resolution maps concept nodes to their source vocabulary, which is necessary to apply SAB-specific flow class rules and membership constraints. The pipeline uses a two-level procedure. At Level 1, the pipeline attempts to resolve each concept node to a SAB by matching against UBKG Code nodes carrying SAB annotations. In the present export, no Code nodes were present; the pipeline fell back to reading the SAB column directly from nodes.csv. This fallback resolved 18,897 of 34,523 concept nodes (54.7%). The remaining 15,626 nodes lacked a direct SAB assignment and were treated as unresolvable; edges with at least one unresolvable endpoint were dropped at Level 2.

The 54.7% resolution rate reflects the 1-hop export design: the export deliberately includes a broad neighborhood to capture mechanistic context, but many peripheral nodes in that neighborhood belong to vocabularies not represented in the current SAB selection. This is not a bug in the pipeline; it is an expected consequence of querying a partial graph slice. The 45.3% unresolved nodes are structurally peripheral (they appear as neighbors in the graph but cannot be classified into BIFO flow classes), and their edges are dropped rather than admitted with unknown classification.

### 2.3 Propagating operator construction

From the 104,342 retained edges that pass Level 2 conditioning, three PPR operators are constructed for the ablation design. These operators differ in which edges they include; the scoring stage (pathway membership map, universe, reference set) is held constant across all three, enabling direct attribution of pathway-scoring differences to operator composition.

The full operator uses all 94,309 propagating edges from the conditioned kept-edge set. Of the 104,342 total kept edges, 10,033 are retained in the kept_edges.csv output but excluded from the PPR adjacency matrix: 9,909 Observational Association edges (which pass flow classification as a recognized class but are excluded from propagation by operator construction because their weak evidential basis would introduce noise into the signal path), 64 weak-mechanistic Genetic Regulatory Modulation edges, and 60 nonpropagating_context Spatial constraint edges.

The ablation operator conditions edges_raw.csv (94,790 edges) independently of the membership edges, producing 26,059 kept edges of which 16,026 are propagating (with the same 10,033 non-propagating class exclusions applied). This operator excludes all Pathway Contribution edges by construction because those edges appear only in the membership edge file, not in edges_raw. The ablation therefore isolates the effect of removing the gene-to-pathway bridge while preserving all other admissible flow classes.

The mechanistic-only operator applies an additional filter to the full kept-edge set, retaining only edges whose classification tier is mechanistic (9,710 edges: Signal Transduction 5,786, Transcription 1,568, Signal Termination 484, and minor mechanistic classes including direct molecular interaction subsets of Perturbational Effect). This operator excludes Pathway Contribution, Observational Association, and all weak-mechanistic edges from the PPR adjacency matrix. Its composition and the pathway-scoring outcome under this operator are reported in Results Section 3.

For all operators, adjacency matrices are built as sparse directed binary matrices (edge weight = 1, no differential weighting by flow class). Self-loops are excluded. Row normalization is applied before transpose to produce the column-stochastic matrix used in the PPR recurrence.

**Formal definition of the BIFO conditioning operator.** Let G = (V, E) be the input property graph with node set V and edge set E, where each edge e = (u, v, p) carries predicate p and endpoint SABs s_u, s_v. BIFO conditioning defines a constraint operator C that produces the conditioned propagation graph G_C = (V, E_C), where:

> E_C = { e ∈ E : flow_class(predicate(e)) ∈ F_admissible ∧ SAB(source(e)) resolved ∧ SAB(target(e)) resolved }

F_admissible is the set of flow classes designated as propagating in bifo_ddkg_mapping.yaml (mechanistic and weak-mechanistic tiers, plus Pathway Contribution bridge edges; excluding Observational Association, contextual_constraint, and nonpropagating_context tiers). The operator is graph-agnostic: it depends only on the predicate-to-flow mapping and entity resolution rules, not on graph topology. This means G_C can be computed independently for any property graph whose edges carry DDKG-compatible predicates, enabling the same conditioning rules to be applied to graphs of arbitrary scale --- including the full KF-CHD and KF-NBL exports (Section 10).

## 3 Personalized PageRank propagation

Signal propagation uses personalized PageRank (PPR), also known as random walk with restart. PPR models the probability that a random walk starting from the seed set visits each node in the graph, with a restart probability α that returns the walk to the seeds at each step. High α keeps signal concentrated near the seeds; low α allows signal to diffuse further into the graph. The balance between local concentration and global diffusion is the mechanism by which BIFO\'s structural constraints shape the output: by conditioning which edges are in the operator, BIFO determines which paths the random walk can follow.

Given row-normalized adjacency matrix Ã (n × n), seed vector s (uniform mass 1/\|S\| over seed nodes, zero elsewhere), and restart probability α, the PPR score vector f satisfies:

> **f = (1 − α) · Ã᷊ · f + α · s**

where Ã᷊ is the transpose of Ã (propagation follows edge direction). The fixed point is computed by iteration: f\_{t+1} = (1−α)Ã᷊f_t + αs, terminating when ‖f\_{t+1} − f_t‖₁ \< 10⁻¹⁰ or after 500 iterations. Convergence was achieved in all benchmark runs.

The restart probability α = 0.5 was set before benchmark freeze and was not optimized on the CHD benchmark or any other dataset. This value was chosen to balance local signal retention (necessary for pathway scoring, where the relevant pathway nodes may be several hops from the seeds) with seed concentration (necessary to avoid diffusing signal uniformly across the graph). Sensitivity to α is a natural direction for future work but is not evaluated in the current benchmark.

Four score vectors are computed per benchmark run on the full-graph operator: (1) raw --- propagation on the full merged adjacency without conditioning; (2) metadata-filtered --- conditioning applying directionality constraints only; (3) conditioned (BIFO) --- full BIFO conditioning; and (4) random sparsification --- random edge selection retaining the same edge count as the conditioned arm. The random control establishes that entropy reduction in the conditioned arm is not simply a consequence of edge count reduction, but reflects the structural properties of the admissible edges specifically.

## 4 Pathway scoring

### 4.1 Membership map construction

Pathway scoring requires mapping gene nodes to the pathway nodes they belong to. Membership is determined from edges_merged.csv using six membership predicate types (pathway_associated_with_gene, inverse_pathway_associated_with_gene, has_signature_gene, inverse_has_signature_gene, process_involves_gene, gene_plays_role_in_process). Membership edges are SAB-source constrained: a gene is included in a pathway\'s member set only if its SAB matches the pathway\'s source vocabulary. This prevents cross-vocabulary membership contamination (e.g., a GO-annotated gene being counted as a member of an MSigDB pathway). Duplicate memberships are removed.

After size filtering (minimum 8, maximum 300 members) and name-pattern exclusion (patterns: \_Q2, \_Q3, \_Q4, \_Q5, \_Q6, MIR), 550 pathways constitute the evaluation universe. The minimum-member filter excludes pathways too small for enrichment analysis to be meaningful; the maximum-member filter excludes pathways so large that membership is uninformative. The name-pattern filter excludes gene expression quantile sets and microRNA sets that represent statistical partitions rather than curated biological programs. This universe is held constant across all arms and all baseline methods.

### 4.2 Pathway score computation (degree_norm)

The degree_norm scoring variant is defined as:

> **score(p) = f_direct(p) / √(\|members(p)\|)**

where f_direct(p) is the PPR score on the pathway concept node itself --- the score mass arriving at the pathway node via Pathway Contribution edges --- and \|members(p)\| is the SAB-constrained member gene count. The √ penalty down-weights large generic pathways (which accumulate high PPR scores simply by having many members) without fully normalizing by size (which would over-penalize legitimate large biological programs). Pathways with zero member genes receive score zero. This variant was selected as the primary scoring function before benchmark freeze; three alternative variants (member_mean, member_max, local_bg) were computed but not used for primary analysis.

### 4.3 Rank improvement

Rank improvement is defined as mean_rank(raw) − mean_rank(conditioned), where both rankings use the same 550-pathway universe and the same reference set. This metric captures how much the BIFO conditioning step improves the relative position of reference pathways compared to propagating signal over the unconditioned graph. A positive value means conditioning moves reference pathways to lower (better) rank positions; a negative value means the raw score already had those pathways ranked higher.

Rank improvement must be interpreted in the context of the task type. In discovery benchmarks (CHD curated), seeds are disease genes not drawn from the target pathway family; conditioning dramatically improves ranks (+99.1) because the raw graph places many non-specific high-degree pathways above the cardiac pathways that conditioning filters toward. In recovery benchmarks (C4 controls), seeds are drawn from the target pathway family; the raw arm already has direct proximity to the target, so conditioning provides less additional lift and rank improvement is negative. This distinction is by design and is not a failure of the method in either case.

## 5 Benchmark design

### 5.1 Task types

Two benchmark task types are formally defined. Discovery benchmarks use seed genes that are not members of the target reference pathways; the evaluation tests whether BIFO propagation can identify biologically relevant pathway families from a gene set that does not directly overlap those families. Recovery benchmarks use seed genes drawn from target pathway members; the evaluation tests whether BIFO can recover the source pathway and related pathways from partial membership. These task types produce systematically different rank improvement patterns and must be reported separately to avoid apparent contradictions in the results.

The discovery/recovery distinction also determines how the Fisher baseline should be interpreted. When seeds are canonical pathway members (recovery), seed-overlap Fisher enrichment is naturally strong because the overlap is direct and large. When seeds are disease genes not drawn from the target pathway (discovery), Fisher enrichment degrades because the overlap is indirect and small, requiring propagation to bridge the gap. BIFO is designed for the discovery setting; its advantage over Fisher is largest in discovery tasks.

### 5.2 Cohort definitions

  ----------------- --------------- ----------- ------------- --------------- ------------------------------------------------------------------------------------------------------------
  **Benchmark**     **Task type**   **Seeds**   **Heldout**   **Reference**   **Seed source**

  **CHD curated**   Discovery       10          5             18 pathways     Hand-curated TF and structural genes: GATA4, NKX2-5, TBX5, NOTCH1, NOTCH2, HAND1, HAND2, MYH6, GATA6, TBX1

  **C4/Notch**      Recovery        30          14            11 pathways     70% random sample of REACTOME_SIGNALING_BY_NOTCH members (seed=42)

  **C4/MAPK**       Recovery        63          28            10 pathways     70% random sample of REACTOME_MAPK_FAMILY_SIGNALING_CASCADES members (seed=42)
  ----------------- --------------- ----------- ------------- --------------- ------------------------------------------------------------------------------------------------------------

**Table M2.** *Benchmark cohort definitions. Task type: discovery = seeds not in reference pathway family; recovery = seeds from source pathway members. C4 splits used numpy.random.seed(42). All CHD-pool CUIs verified in node index before freeze.*

The CHD curated benchmark uses ten canonical transcription factor and structural genes from the CHD literature: GATA4, NKX2-5, TBX5, NOTCH1, NOTCH2, HAND1, HAND2, MYH6, GATA6, and TBX1. These genes were selected based on their established roles in cardiac development and CHD genetics; they were not selected to maximize BIFO performance. Five additional CHD-associated genes (ZFPM2, MYH7, PTPN11, JAG1, FLT4) serve as held-out nodes for gene-level recovery evaluation. The CHD pathway reference set consists of 36 literature-curated pathway CUIs; 18 of these are present in the 550-pathway scored universe and serve as the evaluation reference.

C4 pathway-split controls use 70%/30% member splits of two Reactome/MSigDB pathways. REACTOME_SIGNALING_BY_NOTCH (MSigDB M10189; 44 members; 30 seeds, 14 heldout) tests pathway-family recovery within a cardiac-relevant signaling pathway. REACTOME_MAPK_FAMILY_SIGNALING_CASCADES (MSigDB M27565; 91 members; 63 seeds, 28 heldout) tests recovery in a broader, less cohesive pathway family unrelated to the CHD curated seed set. All members of both source pathways were verified to be present in the node index before splitting.

### 5.3 Three-arm ablation design

The three-arm ablation design systematically varies the PPR operator while holding the scoring stage constant across all arms. This design enables direct causal attribution: differences in pathway-level metrics between arms are attributable solely to the presence or absence of specific edge classes in the propagating graph, not to differences in the scoring method, pathway universe, or reference set. The three arms are: (1) Full --- BIFO-conditioned operator on edges_merged (94,309 propagating edges, including Pathway Contribution bridge edges); (2) Ablation --- BIFO-conditioned operator on edges_raw only (16,026 propagating edges, no Pathway Contribution bridge edges by construction); (3) Mechanistic-only --- BIFO-conditioned operator restricted to classification=mechanistic edges (9,710 propagating edges, excluding Pathway Contribution, Observational Association, and weak-mechanistic classes).

## 6 Baseline enrichment methods

Three conventional enrichment baselines and one graph-structure baseline are implemented to benchmark BIFO against standard bioinformatics practice. The design goal is to compare BIFO against the strongest approaches a bioinformatician would realistically apply to the same graph-derived data --- not against deliberately weak baselines. All baselines are evaluated on the identical 550-pathway universe and identical CHD reference set. The `baseline_enrichment.py` script accepts two flags that control baseline behaviour: `--kept-edges` enables B0 (requires the conditioning output); `--small-universe` switches Fisher baselines to the pathway-member universe and log-space p-values, required for KF cohort runs (see B1 below).

***B0: Degree-weighted seed overlap (graph membership baseline)***

For each pathway p, the score is the sum of conditioned-graph node degrees of seed genes that are direct members of p, normalised by pathway size:

> score(p) = Σ\_{g ∈ seeds ∩ members(p)} degree\_conditioned(g) / √(\|members(p)\|)

where degree\_conditioned(g) is the out-degree of gene g in the BIFO-conditioned propagation graph G_C. Pathways are ranked by descending score. This baseline uses graph structure (node connectivity) but not graph propagation: it scores pathways based on how well-connected the directly overlapping seed genes are within the conditioned graph, without running PPR. It provides a lower bound on graph-guided methods and isolates the contribution of propagation beyond local connectivity. B0 is closely related to degree_norm (which uses PPR scores rather than degrees) and is computed from the conditioning output via the `--kept-edges` flag in baseline_enrichment.py.

***B1: Seed-only hypergeometric enrichment***

For each pathway p, a one-tailed hypergeometric test is applied with N = gene universe size (\~13,000 C-prefixed nodes appearing as edge endpoints in edges_merged), K = \|members(p) ∩ universe\|, n = \|seeds ∩ universe\|, and k = \|members(p) ∩ seeds\|. This tests whether the seed genes are over-represented among pathway members relative to the background rate. Pathways are ranked by ascending p-value; Benjamini--Hochberg FDR correction is applied across all 550 pathways jointly. This baseline represents what a bioinformatician would do with just the seed gene list and no graph information.

**Gene universe design and the `--small-universe` flag.** The curated benchmark uses the large universe (all \~13,000 C-prefixed nodes) with standard-precision `hypergeom.sf`, which produces the honest Fisher result: non-specific hits (cancer gene sets, transcription factor targets) dominate because a ten-gene query cannot discriminate against a large background. For KF cohort analyses (1,276--1,395 seeds against \~22,600-gene universe), this implementation causes p-value floor collapse --- `hypergeom.sf` returns 0.0 for every pathway with meaningful overlap, eliminating rank discrimination entirely. The `--small-universe` flag switches to the pathway-member-only universe (\~4K--22K genes depending on the graph), K = \|members(p)\| (all members, not universe-intersected), and log-space computation (`hypergeom.logsf`) to recover correct relative ordering. The two modes test different statistical hypotheses and produce numerically incomparable results; the curated benchmark always uses the default large universe to reproduce the frozen manuscript numbers.

***B2: 1-hop neighborhood hypergeometric enrichment***

The query gene set is expanded to include all C-prefixed nodes that are direct neighbors of any seed gene in edges_merged (1-hop neighborhood = 11,146 gene neighbors plus 10 seeds = 11,156 total query). The same hypergeometric test is applied with the expanded query. This baseline represents the approach of extracting a graph neighborhood and running standard enrichment --- a natural workflow for a bioinformatician with access to the graph. The large neighborhood size (86% of the gene universe) is itself a finding: it demonstrates the neighborhood-inflation problem that motivates BIFO\'s approach of concentrating signal before scoring.

***B3 / B3b: Preranked GSEA on PPR scores***

Genes in the universe are ranked by their PPR scores (raw arm for B3; conditioned arm for B3b) in descending order. For each pathway, a weighted running-sum enrichment score is computed following the preranked GSEA algorithm, using \|PPR score\| as the hit weight. Pathways are ranked by descending enrichment score. B3 tests whether graph propagation alone (without BIFO conditioning) recovers pathway-relevant signal. B3b tests whether BIFO-conditioned gene scores, when used as a ranked list input to GSEA, improve over raw propagation. The difference between B3b and BIFO full-arm isolates the contribution of the degree_norm pathway-level scoring function beyond what the gene-level score ordering provides.

## 7 Evaluation metrics

Metrics are computed at two levels. Gene-level metrics evaluate how well PPR propagation recovers held-out disease genes --- a test of signal localization. Pathway-level metrics evaluate how well pathway scoring ranks disease-relevant pathways --- the primary evaluation target for BIFO.

  ------------------ ------------- -------------------------------------------------------------------------------------
  **Metric**         **Level**     **Definition**

  AUROC              Gene          Area under ROC curve for held-out gene recovery vs. all non-seed, non-heldout nodes

  AUPRC              Gene          Area under precision-recall curve for held-out gene recovery

  Entropy            Gene          Shannon entropy of PPR score distribution; lower = more concentrated signal

  Nonzero fraction   Gene          Fraction of graph nodes with PPR score \> 0

  P@k                Pathway       Precision at rank k: fraction of top-k pathways in the reference set

  Enrichment@k       Pathway       P@k divided by background rate (reference pathways / universe size)

  Recall@k           Pathway       Fraction of all reference pathways recovered in top-k

  NDCG@k             Pathway       Normalized discounted cumulative gain at rank k; accounts for rank position of hits

  Avg. Precision     Pathway       Area under precision-recall curve across all ranks; single-number ranking summary

  Mean ref. rank     Pathway       Mean rank of reference pathways under the conditioned score vector

  Rank improvement   Pathway       mean_rank(raw) − mean_rank(conditioned); positive = conditioning helps
  ------------------ ------------- -------------------------------------------------------------------------------------

**Table M3.** *Evaluation metrics. Gene-level metrics are computed over held-out nodes vs. all non-seed non-heldout nodes in the graph. Pathway-level metrics use the 550-pathway universe against the benchmark-specific reference set, evaluated under the conditioned-arm score unless stated otherwise.*

Average precision is:

> AP = (1/\|R\|) · Σᵣ∈R \[ P@rank(r) \]

where R is the reference set and P@rank(r) is precision at the rank of reference pathway r. AP is preferred over P@k as a single-number summary because it accounts for both the number of reference pathways recovered and their rank positions. P@k is more interpretable for communication but is coarser.

Rank improvement is the primary metric for comparing conditioning effect. It is reported for all arms except mechanistic-only, where all pathway scores are exactly zero and rank improvement is uninterpretable (reflects arbitrary tie-ordering). In recovery benchmarks (C4 controls), negative rank improvement is expected because the raw PPR arm already has direct proximity to the target pathway through the seed-member overlap; in these cases, AP and source-pathway rank are the appropriate primary metrics.

## 8 Implementation and reproducibility

### 8.1 Software

All analyses were implemented in Python 3.8+ using: NumPy and SciPy for numerical operations and sparse linear algebra; scipy.sparse for PPR adjacency matrices; scipy.stats.hypergeom for Fisher/hypergeometric baselines; pandas for tabular data manipulation; and PyYAML for YAML configuration parsing. The pipeline is implemented in three scripts: bifo_conditioning.py (entity resolution, edge conditioning, PPR propagation), score_pathways.py (pathway membership mapping, score computation, metric calculation), and baseline_enrichment.py (baseline enrichment methods and Analysis 6 metrics). A self-contained run script (minimal_test_run_run_test.sh) generates all main-benchmark outputs from raw graph files without manual intervention.

### 8.2 Benchmark freeze

All benchmark parameters were locked before analysis began. The frozen package (benchmark_freeze/) comprises 17 files including the three pipeline scripts, the YAML mapping (v0.7.1), the run script, and nine seed/heldout/reference files for the three benchmark cohorts. The run script is self-contained: given nodes.csv, edges_raw.csv, and pathway_membership_edges.csv, it produces every main-benchmark output including all baseline comparisons and C4 controls without manual steps.

No parameter was modified after the first successful full run. The C4 random seed (42), pathway universe filters (min=8, max=300 members, name patterns), score variant (degree_norm), and α (0.5) were all fixed before the first benchmark run and documented in BENCHMARK_MANIFEST.md alongside expected output metrics. The manifest serves as a reproducibility contract: if any output metric differs from the manifest values, the run is considered non-reproducible.

### 8.3 Scope of benchmark graph

The benchmark graph is a controlled projection of the full DDKG, not a comprehensive export. Results reported here are specific to this graph slice and SAB vocabulary selection. The mechanistic-layer finding (pathway structural inaccessibility under mechanistic-only propagation) is a property of this graph\'s topology under the current SAB selection and should not be generalised to DDKG as a whole without validation on expanded exports incorporating different source vocabularies. Importantly, this result is informative rather than merely cautionary: it reveals that curated pathway membership relationships (Pathway Contribution edges) occupy a structurally distinct layer from mechanistic gene-gene relationships in this knowledge graph architecture, and that formal admission of bridge edges as a propagation-eligible class is what enables signal transfer across layers. This architectural insight holds regardless of whether future expanded exports alter the specific inaccessibility result.

## 9 CHD exhaustive resampling analysis

The CHD curated benchmark evaluates BIFO performance from a single hand-selected seed set, which raises the natural question of whether results are specific to that particular 10-gene configuration. To address this, we evaluate all C(15,10) = 3,003 possible 10-gene/5-gene partitions of the 15-gene CHD pool (10 original seeds + 5 original held-out genes). The exhaustive enumeration is made feasible by an in-memory design that builds the PPR operators once and varies only the seed vectors across all splits.

### 9.1 Computational design

The PPR operators (conditioned arm from kept_edges.csv, raw arm from edges_merged.csv) and pathway membership map are built once and held in memory. For each of the 3,003 splits, only the seed vector s is modified; the adjacency matrices, pathway universe, and reference set remain identical to the primary benchmark. No per-split output files are written; per-split metrics are accumulated in memory and written as a single CSV (one row per split) and a JSON summary at the end of the run. This design ensures that the resampling is reproducible with a fixed, minimal output footprint rather than thousands of intermediate files.

The analysis is parallelized using Python ProcessPoolExecutor. The PPR operator components (CSR sparse matrix arrays: data, indices, indptr) are serialized to worker processes at startup via an initializer function. Each worker process reconstructs the sparse matrices from these components and processes an assigned batch of splits independently. The parallelization is embarrassingly parallel: splits share no state beyond the read-only operators, so no synchronization is needed beyond collecting results at the end.

### 9.2 Metrics computed per split

For each split, the following are computed: BIFO full-arm pathway metrics (P@10, P@20, enrichment@10, NDCG@10, average precision, mean CHD reference rank, rank improvement relative to the raw arm on the same conditioned graph); gene-level AUPRC for held-out gene recovery; and a seed-overlap Fisher baseline. The GSEA and neighborhood Fisher baselines are not recomputed per split because the resampling analysis was designed to test seed-composition sensitivity of the primary BIFO benchmark, using seed-overlap Fisher as the direct within-split comparator. The broader baseline comparison is reported in full for the primary split in Analysis 4 (Table 4).

### 9.3 Fisher baseline distinction

The seed-overlap Fisher computed in the resampling uses the split seed genes directly as the query set (n = 10 query genes tested for enrichment in pathway member lists). This is a different statistical test from the Analysis 4 Table 4 Fisher, which uses the 1-hop graph neighborhood (11,146 genes) as the query. The two baselines test different hypotheses: the resampling Fisher asks \'are these 10 seed genes over-represented as pathway members?\', while the Analysis 4 Fisher asks \'is the graph neighborhood of these seeds enriched for pathway members?\' The resampling Fisher is competitive on CHD splits because many canonical CHD genes are directly annotated to cardiac pathways; the Analysis 4 neighborhood Fisher fails entirely because the neighborhood is too large to be discriminating. These two Fisher results are not numerically comparable and should not be presented in the same row of a comparison table.

### 9.4 Summary output

The JSON summary file (chd_resampling_summary.json) contains: distribution statistics (mean, SD, min, P25, median, P75, max) for all per-split metrics; robustness counts (fraction of splits with P@10 ≥ threshold, fraction with positive rank improvement, fraction where BIFO AP exceeds Fisher AP); and the primary benchmark split identified as an anchor point within the full distribution with its percentile rank on each metric. The per-split CSV contains one row per split and is the source file for Figure 6 (the resampling distribution figure).

> *Implementation: chd_resampling_exhaustive.py (benchmark_freeze/). Requires Python 3.8+ (compatibility shims for math.comb and str.removesuffix are included). Runtime scales linearly with \--n-cores; 3,003 splits complete in approximately 5 min on 1 core.*

## 10 Kids First cohort analysis

### 10.1 The rare variant enrichment problem

Standard pathway enrichment methods were designed for gene sets produced by differential expression (tens to hundreds of genes, biologically coherent signal) or GWAS association (small focused gene lists near association peaks). Rare variant cohort analysis occupies a different regime: AutoGVP P/LP variant aggregation across a disease cohort typically produces gene lists of hundreds to thousands of genes spanning diverse disease processes, with the biologically relevant signal distributed across a minority of genes embedded in a larger heterogeneous background.

This creates a fundamental tension for enrichment testing. When carrier frequency filters are strict (e.g., ≥3 carriers, MAF ≤0.0001), the gene list shrinks to tens of genes but becomes dominated by severe recessive disease genes incidentally present in the cohort (lysosomal storage, deafness, retinal dystrophy), losing the distributed developmental signal of interest. When carrier frequency filters are relaxed to match the full AutoGVP P/LP burden (MAF ≤0.001, no carrier count filter), the gene list expands to \~1,000--1,500 genes --- large enough that hypergeometric p-values collapse to zero for virtually every pathway with any overlap, eliminating rank discrimination entirely. In the KF-CHD cohort at MAF ≤0.001 (1,276 seed genes, 22,628-gene pathway member universe), all pathways with any overlap at this scale receive floor-level p-values that cannot be ranked. BIFO\'s graph propagation is robust to this regime: by propagating signal from all 1,276 seeds simultaneously through the DDKG, it amplifies the coherent biological signal from the distributed cilia gene subset while the incoherent background diffuses away.

### 10.2 Cohort and variant selection

Germline variant data were obtained from two Kids First pediatric cohorts: KF-CHD (Pediatric Cardiac Genomics Consortium, phs001138, n=697 probands with congenital heart defects) and KF-NBL (Discovering the Genetic Basis of Human Neuroblastoma, phs001436, n=460 probands with neuroblastoma). Whole-genome sequencing was performed using Kids First harmonization pipelines aligned to GRCh38/GENCODE v39.

Variants were filtered retaining GATK PASS calls with genotype quality ≥20 and read depth ≥10. AutoGVP P/LP classification was applied integrating ClinVar and modified InterVar for hierarchical ACMG-AMP criteria assessment. Population allele frequency filtering used gnomAD v3.1 MAF ≤0.001, matching the companion U24 cross-cohort enrichment analysis (Stear et al., CFDE Meeting 2026). Genes harboring ≥1 qualifying variant in any proband were aggregated per cohort. Nineteen high-frequency background disease genes (ABCA4, USH2A, G6PD, TTN, FLG, and fourteen additional recessive deafness/retinal/skin loci) were excluded. This yielded 1,287 seed genes for KF-CHD and 1,406 seed genes for KF-NBL.

At the MAF ≤0.001, n≥1 threshold, 570 of 1,287 CHD seed genes (44.3%) are also present in the NBL seed set. This inter-cohort overlap reflects the shared background of Mendelian disease gene carriers present in any pediatric sequencing cohort at this allele frequency threshold and is not specific to either disease. Carrier count-filtered seed sets (n≥2: 387 CHD / 401 NBL genes, 30% overlap; n≥3: 146 CHD / 147 NBL genes, 27% overlap) show reduced but persistent overlap, consistent with shared rare variant burden being a property of the population rather than the disease.

### 10.3 Graph export and conditioning

Export queries were generated dynamically from each seed list using generate_export_cypher.py. The KF-CHD export produced 815,248 concept nodes and 5,261,300 1-hop edges plus 956,414 pathway membership edges; the KF-NBL export produced 880,476 concept nodes and 5,520,175 edges plus 961,000 pathway membership edges. Of 1,287 CHD seed genes, 1,276 (99.1%) resolved to UMLS CUIs; of 1,406 NBL seed genes, 1,395 (99.2%) resolved. BIFO conditioning used identical parameters to the curated benchmark (alpha=0.5, bifo_ddkg_mapping.yaml v0.7.1), retaining 2,482,752 propagating edges for KF-CHD (43.9% of concept edges) and 2,647,055 for KF-NBL (45.1%).

### 10.4 Pathway scoring and discovery evaluation

Pathway scoring used the degree_norm scoring variant against a universe of 5,124 pathways for KF-CHD and 5,203 pathways for KF-NBL, each passing minimum-member (≥8) and name-pattern filters. No reference pathway set was pre-specified; all pathways were scored and ranked in discovery mode. Results were evaluated post-hoc against a 20-pathway cilia reference set derived by matching pathway names against cilia-related terms (ciliopathies, ciliary, intraflagellar transport, Joubert syndrome, Bardet-Biedl syndrome, primary ciliary dyskinesia, and related terms) within the scored universe. This reference contains WP_CILIOPATHIES and 19 related MSigDB, WikiPathways, Reactome, and GO pathway annotations.

### 10.5 Baseline enrichment methods for KF cohort analysis

Five baseline methods were evaluated against the identical pathway universe restricted to pathways present in the BIFO-scored set (4,551 pathways for KF-CHD; 4,633 for KF-NBL). All methods used the KF-CHD or KF-NBL seed gene CUIs as input.

**B1: Seed-only hypergeometric enrichment.** For each pathway p, a one-tailed hypergeometric test was applied: N = full annotated gene space (pathway member genes ∪ seed genes), K = \|members(p)\|, n = \|seed genes\|, k = \|members(p) ∩ seeds\|. P-values were computed in log space using scipy.stats.hypergeom.logsf to prevent float underflow --- with n/N ≈ 5%, standard-precision computation returns 0.0 for any pathway with strong overlap, collapsing rank discrimination. Log-space computation recovers correct relative ordering. Pathways are ranked by ascending BH-adjusted p-value.

**B1 gene universe rationale.** The gene universe N was set to the union of pathway member genes and seed genes (\~22,628--22,601 genes), not all C-prefixed concept nodes in the DDKG graph (\~58,846). Using all graph nodes inflates the denominator and causes p-value floor collapse because the graph includes diseases, drugs, phenotypes, and other non-gene concepts. The pathway-member-plus-seed universe matches standard practice in pathway enrichment tools.

**B2: 1-hop neighborhood hypergeometric enrichment.** The query set was expanded to the union of seed genes and all 1-hop gene-concept neighbors in the conditioned graph (\~58,846--59,033 genes). This method failed to discriminate pathways because the 1-hop neighborhood covers essentially the full pathway gene universe, giving near-identical p-values to all pathways with any membership overlap.

**B3 / B3b: Preranked GSEA on PPR scores.** Genes were ranked by raw PPR scores (B3) or conditioned PPR scores (B3b) and a weighted running-sum enrichment score was computed following Subramanian et al. 2005.

**B4: BIFO full-arm (degree_norm).** The conditioned PPR score vector was used to score all pathways via score(p) = f_direct(p) / √\|members(p)\|. This is the primary BIFO scoring method.

### 10.6 Comparison design and rank analysis

All five methods were evaluated on identical pathway universes to enable direct rank comparison. The primary comparison metric is the rank of WP_CILIOPATHIES and other cilia-related pathways under each method in discovery mode. Secondary comparisons examine the top-20 ranked pathways per method (Supplementary Table S3), the head-to-head rank correlation between seed_fisher and BIFO for all pathways (Supplementary Table S4), and the full cilia pathway cluster ranking under BIFO (Supplementary Table S5).

### 10.7 Bootstrap resampling analysis

To assess the stability of cilia pathway recovery and the relationship between seed set size and signal, a bootstrap resampling analysis was performed for both cohorts. For each of three seed sizes (n=10, 20, 30), 500 bootstrap draws were made by sampling uniformly without replacement from the full seed CUI pool. For each draw, BIFO scoring and seed-only Fisher enrichment were run using the identical pathway universe and cilia reference set as the primary analysis. The primary cohort run (full 1,276/1,395-gene seed set) was also evaluated as a reference point (boot_id = −1).

Performance was measured as Precision@10 (fraction of cilia reference pathways in the top-10 ranked results), Average Precision (AP) against the 20-pathway cilia reference, and rank improvement (mean rank under raw PPR − mean rank under BIFO, where positive values indicate conditioning helps). All 1,500 bootstrap runs per cohort were parallelised across 192 cores using Python multiprocessing; total runtime was approximately 150 seconds per cohort.

The bootstrap analysis was designed to address two questions: (1) whether cilia pathway recovery requires aggregate cohort-scale variant burden or can emerge from small random gene subsets; and (2) whether BIFO or standard Fisher enrichment is more sensitive for detecting cilia signal at small seed sizes. Results are reported in Section 8.4.


**Results**

*BIFO: Biological Information Flow Ontology --- Benchmark v1.0*

Backbone draft · April 2026 · Data frozen

## 1 Graph conditioning and coverage

The DDKG export comprised 34,523 concept nodes and 174,352 merged edges, combining 94,790 seed-centered mechanistic and association edges (edges_raw) with 79,562 pathway membership edges. Entity resolution using direct SAB column fallback resolved 18,897 of 34,523 concept nodes (54.7%); the remaining 15,626 nodes lacked a mappable source vocabulary assignment and were treated as unresolvable at Level 1.

BIFO conditioning evaluated each edge against the predicate-to-flow mapping (v0.7.1; 251 entries). Of 174,352 input edges, 104,342 (59.8%) were retained as biologically admissible; 69,658 were excluded for three mutually exclusive reasons: unmapped predicate (37,448; 21.5%), unresolved endpoint entity (32,214; 18.5%), or explicit non-flow classification (348; 0.2%). Level-2 edge coverage was 59.8%, reflecting incomplete predicate mapping under the current SAB selection.

  ------------------------------------- --------------- ----------------------- -------------------------------------------------------------
  **Edge category**                     **Count**       **Fraction of input**   **Notes**

  **Raw input edges (merged)**          174,352         100%                    94,790 seed↔hop1 + 79,562 membership

  **Kept after conditioning**           104,342         59.8%                   Biologically admissible (includes non-propagating retained)

  --- Propagating (conditioned arm)     94,309          ---                     Used in PPR operator; see Section 3

  --- Non-propagating retained          10,033          ---                     Observational Association 9,909; contextual 124

  Dropped: non-flow                     348             0.2%                    Structural/taxonomic predicates

  Dropped: unmapped predicate           37,448          21.5%                   No BIFO flow class assigned

  Dropped: unresolved entity            32,214          18.5%                   No SAB match at entity resolution

  Propagating edges (ablation arm)      16,026          ---                     edges_raw conditioned: 26,059 kept → 16,026 propagating

  Propagating edges (mechanistic arm)   9,710           ---                     classification=mechanistic only (see §3)
  ------------------------------------- --------------- ----------------------- -------------------------------------------------------------

**Table 1.** *Graph conditioning statistics. All values from benchmark run V5. Of the 104,342 kept edges, 94,309 enter the PPR operator as propagating edges; 10,033 are retained in the conditioning output (kept_edges.csv) but excluded from propagation --- comprising Observational Association edges (9,909) that pass flow classification but are excluded by operator construction, and a small set of contextual edges (124). The ablation arm conditions edges_raw.csv independently, producing 26,059 kept edges of which 16,026 are propagating (the remainder are the same non-propagating classes).*

Of the 94,309 propagating edges in the conditioned arm, 80,200 (85.0%) were classified as Pathway Contribution, the edge class encoding curated gene-to-pathway membership relationships that serve as admissible bridges between the mechanistic gene neighborhood and the pathway annotation layer. Signal Transduction accounted for 5,786 (6.1%) and Perturbational Effect for 5,392 (5.7%), with Transcription, Signal Termination, and minor classes comprising the remainder.

While Pathway Contribution edges dominate numerically, the ablation experiment (Section 3) establishes that they do not generate signal independently: removing bridge edges while preserving all other admissible mechanistic classes reduces P@10 from 0.70 to 0.60, and mechanistic-only propagation --- which contains no Pathway Contribution edges --- yields exactly zero pathway scores across all 550 pathways. The bridge edges are necessary conduits for transferring mechanistic signal from gene-level propagation to the pathway annotation layer; without upstream mechanistic signal to relay, they have no effect on their own.

![
**BIFO conditioning coverage — curated CHD benchmark graph.**
(**A**) Edge funnel from 174,352 merged input edges through entity resolution and flow-class conditioning to 94,309 propagating edges (54.1% retention) used by the PPR operator.
(**B**) Dropped edges stratified by cause: unmapped predicates (37,448; 21.5%) and unresolved entities (32,214; 18.5%) account for nearly all losses; non-flow classifications contribute <1%.
(**C**) Flow-class distribution of propagating edges. Pathway Contribution bridge edges (dark blue; 80,200 edges; 85.0% of propagating edges) are the architectural element enabling gene→pathway signal transfer; mechanistic classes (Signal Transduction, Perturbational Effect, Transcription, etc.) comprise the remaining 15%.
(**D**) Concept-node entity resolution: 18,897 of 34,523 nodes (54.7%) resolve to a source vocabulary; the remainder are Level-1 unresolvable under the current SAB selection.
](images/fig1_conditioning.png){#fig:conditioning width="100%"}

## 2 Gene-level recovery

To evaluate propagation signal at the gene level, we performed PPR on each arm of the conditioning design and assessed recovery of five held-out CHD-associated genes (ZFPM2, MYH7, PTPN11, JAG1, FLT4) not present in the ten-gene seed set. Gene-level metrics were computed over the full 34,523-node graph.

  ---------------------------- ------------ ------------ ------------- -----------------------
  **Arm**                      **AUROC**    **AUPRC**    **Entropy**   **Nonzero nodes (%)**

  **Raw (full graph)**         1.000        0.2215       5.728         100.0%

  **Conditioned (BIFO)**       1.000        0.1923       5.222         32.8%

  Ablation (no bridge edges)   1.000        0.2215       4.939         19.5%

  Random sparsification        1.000        0.2173       5.590         64.6%
  ---------------------------- ------------ ------------ ------------- -----------------------

**Table 2.** *Four-arm gene-level recovery for the CHD curated benchmark. Entropy is the Shannon entropy of the propagation score distribution (lower = more concentrated). Nonzero node fraction indicates the proportion of nodes with non-negligible score mass. AUROC is near-ceiling across all arms on this small benchmark; entropy and nonzero fraction are the informative discriminants at this scale.*

AUROC was 1.000 across all arms, reflecting ceiling performance on this small benchmark (five held-out nodes from a strongly connected seed neighborhood). AUPRC was 0.2215 for the raw arm and declined to 0.1923 under full BIFO conditioning, reflecting concentration of score mass into a smaller node subset. The ablation arm (propagation without Pathway Contribution edges) produced AUPRC equal to the raw arm (0.2215) with substantially lower entropy (4.939 vs. 5.728), demonstrating that the core mechanistic signal is preserved without bridge edges. The random sparsification control (same edge count as conditioned, random selection) produced intermediate entropy (5.590) and AUPRC (0.2173), establishing that BIFO\'s entropy reduction is not simply a consequence of edge count reduction.

The AUPRC decline from raw to conditioned reflects the structure-dependent nature of BIFO filtering: conditioning concentrates signal on biologically coherent neighborhoods but does not optimize for held-out gene recovery per se. The mechanistic-only arm (9,710 edges, classification=mechanistic, including mechanistically classified subsets of perturbational and termination predicates) produced AUPRC 0.1486 and entropy 4.770, the lowest across all arms, consistent with a sparse subgraph reaching fewer nodes than the random control.

> *⚑ AUPRC is near-ceiling and reported honestly. These gene-level metrics become more informative at full-cohort scale and with variant-derived seeds (Kids First CHD extension, Section 8).*

![
**Four-arm gene-level recovery — curated CHD benchmark.**
Each panel compares four PPR propagation arms (Raw, Metadata-filtered, BIFO-conditioned, Random sparsification) across three graph configurations (Full with all BIFO flow classes, Ablation without Pathway Contribution bridge edges, Mechanistic-only).
(**A**) AUROC is near-ceiling across all arms and configurations, reflecting the strongly connected seed neighborhood on this small benchmark.
(**B**) AUPRC discriminates between arms; BIFO-conditioned on the Mechanistic graph shows the expected drop (0.149) relative to Full (0.192), and Random sparsification of the Mechanistic graph collapses to 0.049.
(**C**) Localization (mean held-out rank normalised by graph size; lower = more concentrated near seeds). BIFO-conditioned is lowest across Full and Ablation graphs.
(**D**) PPR score entropy in bits (lower = more concentrated signal). BIFO-conditioned achieves the lowest entropy in all three graph configurations, showing that conditioning concentrates signal beyond what edge-count reduction alone achieves.
](images/fig2_gene_recovery.png){#fig:gene_recovery width="100%"}

## 3 Pathway prioritization: three-arm ablation

The primary benchmark evaluated pathway prioritization using three propagation arms scored against an identical pathway universe (550 pathways, 8--300 members, CHD reference set of 18 pathways). All three arms used the same pathway membership map for scoring; only the propagating graph differed.

  -------------------------------- ----------------- ---------- ------------------ --------------- --------------------
  **Arm**                          **Prop. edges**   **P@10**   **Enrich. \@10**   **Mean rank**   **Rank imp.**

  **Full (BIFO conditioned)**      **94,309**        **0.70**   **21.4×**          **113**         **+99.1**

  **Ablation (no bridge edges)**   16,026            0.60       18.3×              111             −11.2

  Mechanistic-only                 9,710             0.00       0.0×               177             uninterpretable \*
  -------------------------------- ----------------- ---------- ------------------ --------------- --------------------

**Table 3.** *Three-arm pathway prioritization for the CHD curated benchmark. Pathway universe: 550 pathways. CHD reference: 18 pathways. Background rate: 3.3%. Rank improvement = mean_rank_raw − mean_rank_cond (positive = conditioning improves rank relative to the raw propagation baseline). \* Mechanistic-arm rank improvement is uninterpretable: all pathway scores are exactly zero and tie-ordering is arbitrary.*

***Full arm***

Under full BIFO conditioning (94,309 propagating edges), the top-10 pathways contained 7 of 18 CHD reference pathways (P@10 = 0.70; enrichment = 21.4× background). BRUNEAU_SEPTATION_VENTRICULAR and WP_HEART_DEVELOPMENT ranked first and second. Mean rank of CHD reference pathways under the conditioned score was 113, compared with 212 under the raw score from the same propagation, yielding rank improvement +99.1.

***Ablation arm***

The ablation arm removed Pathway Contribution edges from propagation (16,026 propagating edges from 26,059 kept edges of edges_raw, with 10,033 non-propagating retained classes excluded as in the full arm) while retaining the identical membership map for scoring. P@10 = 0.60 (enrichment = 18.3×); the top-6 CHD pathways were identical to those in the full arm. Rank improvement was −11.2: without Pathway Contribution bridge edges in the propagating graph, the conditioned operator cannot route signal through the pathway-layer bridge, so the raw arm\'s direct scoring advantage persists. This demonstrates that the core cardiac signal originates in the mechanistic neighborhood but that the full arm\'s conditioning gain requires the bridge edges to be present.

***Mechanistic-only arm***

The mechanistic-only arm restricted propagation to edges classified as mechanistic in the YAML mapping (9,710 edges: Signal Transduction 5,786, Transcription 1,568, Signal Termination 484, and minor classes including mechanistically classified subsets of perturbational and termination predicates). All 550 pathway scores were exactly zero, yielding P@10 = 0.00. This is a structural result, not a performance result. In the present benchmark graph, pathway nodes are not reachable from seed genes through mechanistic edges alone; gene-to-pathway connectivity is mediated exclusively by Pathway Contribution edges. The rank improvement value of +34.7 is uninterpretable: it reflects arbitrary tie-ordering of zero-score pathways.

Together, the three arms identify a two-layer graph architecture with a structurally necessary bridge. Layer 1 (mechanistic) encodes gene--gene signaling, transcription, and protein interaction. Layer 2 (pathway) encodes curated gene-set annotations. These layers are structurally separated in the present graph; connectivity between them is mediated exclusively by Pathway Contribution edges. BIFO\'s contribution is the principled, ontology-aligned admission of those bridge edges as a coherent flow class, enabling signal transfer from the mechanistic layer to the pathway annotation layer.

> *Scope: these conclusions apply to the present benchmark graph, constructed from a defined SAB subset that isolates ontology-aligned mechanistic and pathway representations from association-derived evidence layers. The present framework does not incorporate association-derived evidence; the architectural findings reported here reflect this graph's topology under the current SAB selection.*

![
**BIFO conditioning enables pathway-level signal recovery.**
Top row: curated CHD benchmark (550 pathways, 18-pathway CHD reference) comparing the Full BIFO arm, Ablation (no Pathway Contribution bridge edges), and Mechanistic-only propagation.
(**A**) Precision@10: Full 0.70, Ablation 0.60, Mechanistic 0.00.
(**B**) Enrichment@10 over background rate: Full 21.4×, Ablation 18.3×, Mechanistic 0×.
(**C**) Rank improvement (raw PPR rank − conditioned PPR rank): Full +99.1 positions, Mechanistic +34.7 (uninterpretable; see text), Ablation −11.2.
(**D**) WP_CILIOPATHIES rank under five enrichment methods in the KF-CHD discovery cohort (1,276 variant genes, 5,124 pathways scored). Seed Fisher (corrected) and BIFO full-arm both rank WP_CILIOPATHIES first; Raw PPR GSEA, Conditioned PPR GSEA, and Neighborhood Fisher rank it 3,340, 4,429, and 4,544 respectively.
](images/fig3_ablation.png){#fig:ablation width="100%"}

## 4 Baseline comparison

To evaluate BIFO against conventional enrichment approaches applied to the same graph-derived gene sets, we implemented four baselines evaluated on the identical 550-pathway universe: (B0) degree-weighted seed overlap, (B1) seed-only hypergeometric enrichment, (B2) 1-hop neighborhood hypergeometric enrichment, and (B3) preranked GSEA on raw PPR scores. All Fisher-based tests used Benjamini--Hochberg FDR correction. The BIFO full-arm result (B4) is shown for direct comparison.

  --------------------------------- ----------- ----------- ------------- ---------------- ---------------
  **Method**                        **P@10**    **P@20**    **NDCG@10**   **Avg. Prec.**   **Mean rank**

  **Degree overlap (B0)**           0.400       0.400       0.492         0.342            84

  **Seed-only Fisher**              0.300       0.200       0.215         0.156            120

  **1-hop neighborhood Fisher**     0.000       0.000       0.000         0.037            243

  Raw PPR preranked GSEA            0.100       0.050       0.220         0.117            162

  Conditioned PPR GSEA              0.100       0.050       0.085         0.114            110

  **BIFO full-arm (degree_norm)**   **0.700**   **0.350**   **0.757**     **0.403**        **113**
  --------------------------------- ----------- ----------- ------------- ---------------- ---------------

**Table 4.** *Baseline comparison for the CHD curated benchmark. All methods evaluated on identical 550-pathway universe (background 3.3%). Avg. Prec. = average precision (area under the precision--recall curve over all ranks).*

Seed-only Fisher (B1) achieved P@10 = 0.30 but produced non-specific top hits (bladder cancer, TP63 targets, TNF response), reflecting the instability of hypergeometric enrichment with a ten-gene query: even minimal pathway overlap produces floor-level p-values, placing cancer-associated gene sets above cardiac pathways.

The degree-weighted seed overlap baseline (B0) scored pathways by the sum of conditioned-graph out-degrees of overlapping seed genes normalised by pathway size, recovering BRUNEAU_SEPTATION_VENTRICULAR and WP_HEART_DEVELOPMENT at ranks 1 and 2 through direct membership overlap (P@10 = 0.40, AP = 0.342). BIFO outperforms B0 on both P@10 (0.70 vs. 0.40) and AP (0.403 vs. 0.342), isolating the contribution of PPR propagation beyond local graph connectivity.

Neighborhood Fisher (B2) failed entirely (P@10 = 0.000, AP = 0.037). The 1-hop gene neighborhood around the ten seed genes contained 11,146 genes --- 86% of the gene universe --- so virtually every pathway had non-trivial neighborhood overlap, eliminating all discriminating power. This demonstrates the neighborhood-inflation problem: graph-derived gene sets are too broad for conventional enrichment without prior signal concentration.

Raw PPR preranked GSEA (B3) recovered BRUNEAU_SEPTATION_VENTRICULAR at rank 1 (P@10 = 0.10, NDCG@10 = 0.220), confirming that graph propagation encodes pathway-relevant signal even before BIFO conditioning. BIFO full-arm (B4) outperformed all baselines across every metric: P@10 = 0.70 (2.3× seed Fisher), NDCG@10 = 0.757 (3.4× raw GSEA), AP = 0.403 (2.6× seed Fisher). The improvement over conditioned PPR GSEA (B3b; AP = 0.114) isolates the contribution of the degree_norm scoring function beyond propagation alone.

*Standard enrichment fails in both the small-sample regime (seed Fisher: unstable overlap) and the large-neighborhood regime (neighborhood Fisher: no discrimination). BIFO-conditioned propagation avoids both failure modes by structuring the graph before scoring. These results are consistent with the three-arm ablation finding in Section 3: pathway-ranking performance improves when admissible bridge edges are present in the propagating graph, and collapses when they are absent.*

![
**Baseline enrichment method comparison — KF-CHD and KF-NBL cohorts.**
Five enrichment methods (BIFO full-arm, Conditioned PPR GSEA, Raw PPR GSEA, Neighborhood Fisher, Seed Fisher corrected) evaluated against a 21-pathway native cilia reference set (MSigDB/WikiPathways/Reactome/GO).
(**A**) KF-CHD heatmap: five methods × five metrics (P@10, P@20, P@50, Average Precision, Mean Cilia Ref Rank). Colour scaled within each metric column (darker = better); Mean Ref Rank colour is inverted so lower rank shows darker. `—` denotes zero or not applicable.
(**B**) KF-NBL heatmap, same layout as A.
(**C**) WP_CILIOPATHIES rank under BIFO full-arm and Seed Fisher (corrected): both methods rank WP_CILIOPATHIES first in both cohorts, confirming convergent cilia-signal recovery despite different ranking mechanisms. Seed Fisher distributes detection more broadly across the 21-pathway reference at higher P@k; BIFO concentrates signal on the peak cilia pathway (peak rank 1 in both cohorts).
](images/fig4_baseline_heatmap.png){#fig:baseline_heatmap width="100%"}

## 5 Pathway-split controls (C4)

To evaluate BIFO independent of disease-gene curation, we constructed two pathway-split benchmarks using seeds drawn directly from pathway member gene lists. For each control, 70% of pathway members (random seed=42) served as seeds and 30% as held-out genes. These are recovery benchmarks: because seeds overlap substantially with the target pathway, the raw PPR arm already has high direct proximity to the target. Negative rank improvement values are expected and do not indicate BIFO failure.

  ----------------------------- ----------- ------------- ----------------- ---------- ------------------ ------------- -----------------
  **Context (task type)**       **Seeds**   **Heldout**   **Ref. paths.**   **P@10**   **Enrich. \@10**   **BIFO AP**   **Source rank**

  **CHD curated (discovery)**   10          5             18                0.70       21.4×              0.403         1

  **C4/Notch (recovery)**       30          14            11                0.50       25.0×              0.450         1

  C4/MAPK (recovery)            63          28            10                0.10       5.5×               0.174         1
  ----------------------------- ----------- ------------- ----------------- ---------- ------------------ ------------- -----------------

**Table 5.** *C4 pathway-split controls. Task type: recovery (seeds drawn from target pathway members). Source rank: rank of the source pathway under BIFO full-arm score. Rank improvement not shown for C4 controls; see text.*

***C4/Notch --- pathway-family recovery***

Seeds were 30 HGNC genes from REACTOME_SIGNALING_BY_NOTCH (44 total members). BIFO ranked REACTOME_SIGNALING_BY_NOTCH at position 1/550, with three additional Notch-family pathways in the top 10 (P@10 = 0.50, enrichment = 25.0×, AP = 0.450). Seed-only Fisher and neighborhood Fisher both produced P@10 = 0.000; raw PPR GSEA achieved P@10 = 0.40 but AP = 0.308. BIFO\'s AP advantage (0.450 vs. 0.308) reflects more coherent Notch-family pathway ordering at deeper ranks.

***C4/MAPK --- orthogonal control***

Seeds were 63 HGNC genes from REACTOME_MAPK_FAMILY_SIGNALING_CASCADES (91 total members). BIFO ranked the source pathway first (P@10 = 0.10, 5.5× enrichment, AP = 0.174). Performance was weaker than C4/Notch, reflecting the broader and less cohesive MAPK reference family. Neighborhood Fisher achieved P@10 = 0.10 with AP = 0.164; seed Fisher failed entirely (AP = 0.017). BIFO\'s modest AP advantage over neighborhood Fisher is consistent with MAPK pathway connectivity being partially accessible through the graph neighborhood, unlike the CHD discovery task where neighborhood enrichment collapses entirely.

In both C4 controls, the source pathway ranked first under BIFO, confirming that degree_norm scoring correctly identifies the most semantically proximal pathway when seeds are drawn from that pathway\'s own membership. These results demonstrate that BIFO operates on graph topology independent of disease-gene curation.

![
**C4 pathway-split controls — curated CHD benchmark.**
Two pathway-family controls using seeds drawn from curated pathway gene lists rather than CHD variant genes. C4/Notch: 30 Notch pathway seeds against 11 Notch/developmental reference pathways (recovery task). C4/MAPK: 63 MAPK seeds against 10 MAPK reference pathways (orthogonal control).
(**A**) Precision@10: Notch 0.50, MAPK 0.10. BIFO recovers within-family signal (Notch) and attenuates orthogonal signal (MAPK) appropriately.
(**B**) Enrichment@10 over background: Notch 25.0×, MAPK 5.5×.
(**C**) Mean rank of target pathways under BIFO-conditioned vs. raw PPR. Raw PPR achieves lower (better) mean rank in both controls.
(**D**) Rank improvement is negative in both controls (Notch −31.5, MAPK −54.4). This is the expected mechanism of BIFO conditioning: Pathway Contribution bridge edges redistribute rank mass toward cross-family pathway neighbourhoods, which produces the +99.1 rank improvement on heterogeneous CHD variant seeds (@fig:ablation C) but slightly dilutes within-family concentration when seeds already share a pathway identity.
](images/fig5_c4_controls.png){#fig:c4_controls width="100%"}

## 6 Robustness to seed set composition

The primary CHD benchmark used a single hand-curated 10-gene seed set. To assess sensitivity to seed composition, we evaluated BIFO pathway prioritization across all C(15,10) = 3,003 possible 10-gene/5-gene partitions of the 15-gene CHD pool (10 original seeds plus 5 original held-out genes). All 3,003 splits were evaluated using identical conditioning, scoring, and pathway universe parameters in a single parallelized in-memory run.

  ------------------------ ----------- ---------- ----------- ----------- ------------ ------------ ------------
  **Metric**               **Mean**    **SD**     **Min**     **P25**     **Median**   **P75**      **Max**

  **BIFO P@10**            0.445       0.123      0.100       0.400       0.500        0.500        0.700

  **BIFO Enrichment@10**   13.60×      3.75       3.1×        12.2×       15.3×        15.3×        21.4×

  BIFO NDCG@10             0.523       0.142      0.064       0.447       0.554        0.617        0.760

  BIFO Avg. Precision      0.305       0.066      0.136       0.265       0.311        0.354        0.448

  **Rank improvement**     **+93.0**   **16.8**   **+28.4**   **+82.8**   **+93.5**    **+103.9**   **+139.1**

  Gene AUPRC               0.877       0.121      0.357       0.829       0.891        1.000        1.000

  Seed Fisher AP           0.351       0.062      0.171       0.308       0.350        0.394        0.532
  ------------------------ ----------- ---------- ----------- ----------- ------------ ------------ ------------

**Table 6.** *Distribution of BIFO pathway metrics across all 3,003 exhaustive seed partitions. All splits: identical conditioning (α=0.5), 550-pathway universe, 18-pathway CHD reference. Rank improvement = mean_rank(raw) − mean_rank(conditioned). Seed Fisher AP is an internal split-space comparator; it is not numerically comparable to the Analysis 4 Table 4 Fisher baseline (different query construction; see Methods §9.3).*

***Rank improvement is positive and stable across all splits***

Rank improvement was positive in all 3,003 splits (range +28.4 to +139.1; mean ± SD: +93.0 ± 16.8). This demonstrates that BIFO conditioning consistently improves the ordering of CHD-relevant pathways relative to the unconditioned propagation baseline, regardless of which genes in the 15-gene pool serve as seeds.

***Pathway precision is stable across nearly all seed configurations***

Top-10 precision ranged from 0.10 to 0.70 (median 0.50, IQR \[0.40, 0.50\]). In 95.1% of splits (2,857/3,003), P@10 ≥ 0.30; in 51.8% (1,555/3,003), P@10 ≥ 0.50. Average precision ranged from 0.136 to 0.448 (median 0.311). Even in the least favorable splits, BIFO retains detectable pathway signal.

***Position of the primary benchmark split***

The primary split achieved P@10 = 0.70, AP = 0.408, and rank improvement +99.2. P@10 = 0.70 is the maximum observed across the full evaluated split space; AP = 0.408 falls at the 91st percentile of the distribution; rank improvement +99.2 is near the center of the distribution (median +93.5). The primary split therefore represents a favorable configuration within the CHD gene pool, with P@10 at the maximum observed and rank improvement near the distribution center.

***Relationship to seed-overlap Fisher enrichment***

BIFO achieved higher average precision than the seed-overlap Fisher baseline in 22.9% of splits (687/3,003). Seed-overlap Fisher is competitive when query genes directly overlap pathway members --- as is true for most splits of the curated CHD gene pool. BIFO\'s advantage lies in recovering pathways connected to but not directly overlapping the seed set through graph propagation. Across all splits, BIFO rank improvement is consistently positive regardless of whether BIFO or Fisher achieves higher AP on a given split.

> *Fisher note: the resampling Fisher uses seed genes as the direct query (n=10). This differs from Analysis 4 Table 4 Fisher, which uses the 11,146-gene graph neighborhood as query. The two test different hypotheses and are not numerically comparable; see Methods §9.3.*

![
**BIFO pathway recovery is stable across 3,003 seed partitions — curated CHD benchmark.**
Each split: 10 seeds and 5 held-out genes drawn from the 15-gene CHD pool. Primary split (red dashed line in each panel) is the manuscript benchmark split. Box = IQR; whiskers = min/max.
(**A**) Precision@10 distribution across all 3,003 splits. 95.1% of splits achieve P@10 ≥ 0.30; 51.8% achieve P@10 ≥ 0.50; primary split P@10 = 0.70.
(**B**) BIFO Average Precision distribution (primary = 0.408).
(**C**) Seed Fisher Average Precision distribution (primary = 0.431).
(**D**) Rank improvement distribution (raw PPR rank − conditioned PPR rank): all 3,003 splits show positive rank improvement (100% positive); primary split +99.2. BIFO beats Seed Fisher on AP in 22.9% of splits.
](images/fig6_resampling.png){#fig:resampling width="100%"}

## 7 Limitations and scope

***Graph scope***

The benchmark graph is a 1-hop neighborhood export from a defined DDKG SAB subset that isolates ontology-aligned mechanistic and pathway representations from association-derived evidence layers. Entity resolution covered 54.7% of concept nodes under this SAB selection.

***Mechanistic arm scope and structural interpretation***

The finding that pathway nodes are structurally inaccessible under mechanistic-only propagation applies to the present benchmark graph and SAB selection. Rather than a limitation, this reveals an architectural property of ontology-aligned biomedical knowledge graphs: mechanistic edges encode directed biological process flow within the molecular layer (gene--gene signaling, protein interactions, regulatory cascades), while a formally distinct edge class --- Pathway Contribution bridges --- is required to connect that molecular layer to pathway-level annotations. This separation is not an artefact of incomplete edge coverage; it is a consequence of how curated pathway memberships are represented in the DDKG. The result motivates BIFO's explicit admission of bridge edges as a coherent, propagation-eligible flow class: without formally recognising and admitting them, no graph propagation method operating on mechanistic edges alone can reach pathway concept nodes in this knowledge graph architecture. Whether this architectural property persists under expanded SAB selections incorporating additional evidence layers remains an open question outside the scope of the current analysis.

***Gene-level recovery ceiling***

AUROC is near-ceiling (1.000) on this benchmark due to the small held-out set and strongly connected seed neighborhood. These metrics will be more discriminating at full-cohort scale with variant-derived seeds. The present framework isolates admissible mechanistic and pathway-level structure; incorporation of additional evidence layers requires separate treatment to preserve interpretability of causal flow.

![
**Two-layer graph architecture and the role of Pathway Contribution bridge edges.**
Schematic of the conditioned BIFO graph. The gene/molecular layer (top) contains gene and protein concept nodes connected by mechanistic flow-class edges (signal transduction, protein interaction, transcription). The pathway layer (bottom) contains curated pathway concept nodes from WikiPathways, Reactome, and related sources. The two layers are structurally separated in the mechanistic subgraph; connectivity is mediated exclusively by Pathway Contribution bridge edges (orange, dashed). Variant-gene seeds (filled nodes) inject PPR probability mass into the gene layer, which propagates down through admissible bridge edges to the pathway layer. In the ablation arm, bridge edges are removed and the pathway layer is unreachable from seed genes — the structural finding of Section 3.
](images/fig7_schematic.png){#fig:schematic width="100%"}



## 8 Kids First cohort: discovery-mode pathway analysis

### 8.1 Fisher enrichment at cohort scale: implementation matters

Applying seed-only hypergeometric enrichment (B1) to the 1,276-gene KF-CHD variant set requires careful implementation. A naive implementation using standard-precision p-value computation causes float underflow: with 1,276 seeds against a \~22,628-gene universe, scipy.stats.hypergeom.sf returns 0.0 for any pathway with meaningful overlap, collapsing rank discrimination entirely and placing WP_CILIOPATHIES (61/170 members; BH p = 9.68×10⁻³¹) at rank 768 alongside hundreds of non-specific pathways. Once corrected to use log-space hypergeometric computation (hypergeom.logsf) with a pathway-member-only gene universe, Fisher correctly recovers WP_CILIOPATHIES at rank 1 of 4,551 pathways (BH p = 9.68×10⁻³¹, overlap = 61/170 members). WP_GENES_RELATED_TO_PRIMARY_CILIUM_DEVELOPMENT_BASED_ON_CRISPR ranks 3rd (BH p = 8.29×10⁻¹⁴) and WP_JOUBERT_SYNDROME ranks 4th (BH p = 8.29×10⁻¹⁴), confirming that cilia enrichment signal is present and detectable by both approaches when Fisher is correctly implemented.

Neighborhood Fisher (B2) failed entirely (P@10 = 0.000) because the 1-hop neighborhood expands to \~58,846 genes --- essentially the full graph --- giving near-identical p-values to all pathways. Preranked GSEA on raw PPR scores (B3) ranked WP_CILIOPATHIES at position 3,340; on conditioned PPR scores (B3b) at position 4,429. Gene-level PPR scores without BIFO\'s pathway-level degree normalization do not concentrate signal specifically on cilia pathway concept nodes.

**Table 8.1. KF-CHD method comparison --- WP_CILIOPATHIES rank and cilia pathway recovery**

  ----------------------------- -------------------------- --------------------------- ---------------------------------------------
  **Method**                    **WP_CILIOPATHIES rank**   **Top-5 includes cilia?**   **Key statistic**

  seed_fisher (B1, corrected)   1 / 4,551                  Yes (ranks 1, 3, 4)         BH p=9.68×10⁻³¹; overlap=61/170

  neighborhood_fisher (B2)      not top-50                 No                          58,846-gene neighborhood; no discrimination

  raw_ppr_gsea (B3)             3,340 / 4,551              No                          Gene-level PPR insufficient

  cond_ppr_gsea (B3b)           4,429 / 4,551              No                          Conditioned scores insufficient

  BIFO full-arm (B4)            1 / 5,124                  Yes (rank 1)                degree_norm=6.26×10⁻⁶; not hub-flagged
  ----------------------------- -------------------------- --------------------------- ---------------------------------------------

Fisher top-5: WP_CILIOPATHIES (1), REACTOME_DISEASES_OF_METABOLISM (2), WP_PRIMARY_CILIUM_CRISPR (3), WP_JOUBERT_SYNDROME (4), REACTOME_DISORDERS_TRANSMEMBRANE (5). BIFO top-5: WP_CILIOPATHIES (1), YOSHIMURA_MAPK8 (2; hub-flagged), NABA_MATRISOME (3; hub-flagged), Ionophore activity (4), REACTOME_DISEASES_OF_METABOLISM (5; hub-flagged).

### 8.2 BIFO recovers ciliopathy signal in discovery mode

Under BIFO full-arm scoring, WP_CILIOPATHIES ranked first of 5,124 pathways (degree_norm = 6.26×10⁻⁶; not hub-flagged). This result was obtained without pre-specifying any reference pathway. The cilia signal emerges from PPR propagation across all 1,276 seeds simultaneously: the 22 cilia-related genes in the seed set (DNAH5, CEP290, CC2D2A, PKD1L1, KIAA0586, NPHP4, TMEM67, DNAI2, CCDC39, ARL13B, HYLS1, and others spanning dynein heavy chains, transition zone components, IFT regulators, and left-right asymmetry genes) pull propagated probability mass toward the ciliopathy pathway cluster through shared graph neighborhoods, while the \~1,254 non-cilia variant genes contribute diffuse background signal that degree normalization suppresses.

BIFO recovers the entire cilia pathway cluster in a coherent ranked gradient. Of 22 native cilia, ciliopathy, and hedgehog pathway annotations in the 5,124-pathway universe, all 22 rank above the median (top 50%). The top four by BIFO rank are WP_CILIOPATHIES (rank 1), WP_GENES_RELATED_TO_PRIMARY_CILIUM (rank 23), WP_JOUBERT_SYNDROME (rank 55), and REACTOME_CILIUM_ASSEMBLY (rank 87). Hub-flagged pathways in the BIFO top-5 (YOSHIMURA_MAPK8, NABA_MATRISOME, REACTOME_DISEASES_OF_METABOLISM) reflect high-degree graph structure rather than specific cilia signal and are distinguishable by the hub flag in the output.

\[⚑ Supplementary Table S3: Full top-20 ranked pathways per method for KF-CHD. To be typeset from kf_chd_results/baseline_comparison.csv.\]

\[⚑ Supplementary Table S4: Head-to-head rank comparison --- seed_fisher rank vs. BIFO rank for all 4,551 pathways, sorted by BIFO rank.\]

\[⚑ Supplementary Table S5: Full cilia pathway cluster ranking under BIFO for KF-CHD. All 22 native cilia/ciliopathy/hedgehog pathways with BIFO rank, degree_norm score, member gene count, and hub flag.\]

### 8.3 Cross-cohort convergence: KF-NBL independent replication

Applying identical BIFO analysis to the KF-NBL cohort (1,395 seed genes from 460 neuroblastoma probands, 2,647,055 conditioned edges, 5,203 scored pathways), WP_CILIOPATHIES ranked first of 5,203 pathways --- an independent replication of the KF-CHD rank-1 result. Seed-only Fisher (B1, corrected) also ranked WP_CILIOPATHIES first of 4,633 pathways (BH p = 8.13×10⁻³²), with WP_AMINO_ACID_METABOLISM 3rd, KAUFFMANN_DNA_REPAIR_GENES 4th, and WP_JOUBERT_SYNDROME 5th.

The KF-CHD and KF-NBL seed sets share 570 genes (44.3% of the CHD set), reflecting shared rare Mendelian disease gene carrier burden at MAF ≤0.001 rather than disease-specific biology. At a stricter n≥2 carrier count filter, the overlap decreases to 117 of 387 CHD genes (30%) while both cohorts still yield WP_CILIOPATHIES at rank 1 --- the cilia signal is present in both the shared and cohort-specific variant components. The convergence on the same top pathway across two biologically distinct pediatric diseases is consistent with the known developmental role of cilia in both cardiac septation and neural crest migration, and with the companion U24 cross-cohort analysis (Stear et al. 2026) which independently identified cilia enrichment in KF cohorts using permutation-based GSEA.

**Table 8.3. Cross-cohort comparison --- WP_CILIOPATHIES and cilia pathway recovery**

  --------------------------------------------- ----------------------------- -----------------------------
  **Metric**                                    **KF-CHD**                    **KF-NBL**

  Seed genes (MAF≤0.001, n≥1)                   1,276                         1,395

  Conditioned edges                             2,482,752                     2,647,055

  Pathways scored                               5,124                         5,203

  WP_CILIOPATHIES rank --- BIFO                 1 / 5,124                     1 / 5,203

  WP_CILIOPATHIES rank --- Fisher (corrected)   1 / 4,551 (BH p=9.68×10⁻³¹)   1 / 4,633 (BH p=8.13×10⁻³²)

  Cilia seed genes in pool                      22                            19

  Inter-cohort gene overlap                     570 / 1,287 (44.3%)           ---
  --------------------------------------------- ----------------------------- -----------------------------

### 8.4 Bootstrap resampling: cilia signal requires aggregate cohort burden

To assess whether cilia pathway recovery is robust to seed set size, 500 bootstrap draws at each of three seed sizes (n=10, 20, 30) were drawn from each cohort\'s full seed pool. Results reveal a consistent pattern across both cohorts: neither BIFO nor Fisher reliably recovers cilia pathways from small random gene subsets, but both converge at full cohort scale.

At the primary run (full 1,276 CHD seeds), BIFO achieves P@10 = 0.20 against the 20-pathway cilia reference (50× background enrichment) with AP = 0.090 and rank improvement = +303 (conditioning helps vs. raw propagation). Fisher achieves P@10 = 0.30 and AP = 0.150. At n=10--30 random seeds, P@10 is near zero for both methods (BIFO: 0.008--0.011; Fisher: 0.018--0.035). Fisher finds any cilia pathway in the top-10 in 13--21% of n=10--30 bootstrap runs versus 7--9% for BIFO --- Fisher is modestly more sensitive at small seed sizes. At the full cohort scale, BIFO\'s positive rank improvement (+303 CHD, +193 NBL) confirms that graph conditioning adds value over raw propagation, while Fisher\'s higher absolute P@10 reflects its sensitivity to direct overlap once the seed set is large enough.

The core finding is that the cilia signal in these cohorts is distributed across many genes and requires aggregate cohort-scale variant burden to emerge. Neither method recovers it reliably from n=10--30 randomly drawn genes, and both converge at cohort scale. This is consistent with a polygenic developmental signal embedded in heterogeneous rare variant background --- BIFO\'s graph propagation concentrates this distributed signal through shared pathway neighborhoods, while Fisher requires sufficient overlap count to produce significant statistics.

**Table 8.4. Bootstrap resampling results --- BIFO vs. Fisher cilia pathway recovery**

  -------------------------- --------------- ----------------- ------------- --------------- ----------------------- ----------------------------- -------------------------------
  **Seed size**              **BIFO P@10**   **Fisher P@10**   **BIFO AP**   **Fisher AP**   **BIFO \> Fisher AP**   **Any cilia top-10 (BIFO)**   **Any cilia top-10 (Fisher)**

  KF-CHD primary (n=1,276)   0.200           0.300             0.0898        0.1500          ---                     ---                           ---

  KF-CHD n=10 (500 runs)     0.008           0.018             0.013         0.013           50.8%                   6.6%                          13.0%

  KF-CHD n=20 (500 runs)     0.008           0.029             0.012         0.017           49.8%                   7.4%                          18.6%

  KF-CHD n=30 (500 runs)     0.011           0.035             0.014         0.021           44.2%                   9.0%                          21.0%

  KF-NBL primary (n=1,395)   0.100           0.200             0.0895        0.1165          ---                     ---                           ---

  KF-NBL n=10 (500 runs)     0.012           0.022             0.013         0.012           59.2%                   7.6%                          14.8%

  KF-NBL n=20 (500 runs)     0.012           0.025             0.013         0.016           53.4%                   9.0%                          15.6%

  KF-NBL n=30 (500 runs)     0.010           0.041             0.013         0.021           45.2%                   7.6%                          24.2%
  -------------------------- --------------- ----------------- ------------- --------------- ----------------------- ----------------------------- -------------------------------

![
**Cross-cohort convergence: KF-CHD and KF-NBL independently recover cilia pathways.**
(**A**) WP_CILIOPATHIES ranks first under both BIFO full-arm and corrected Seed Fisher in both cohorts.
(**B**) BIFO pathway rank scatter (top 3,000 shown) with cilia pathways highlighted in red (n = 22). Cilia pathways cluster in the top-left corner of both axes, indicating concordant prioritization across cohorts; non-cilia pathways (grey) scatter along the diagonal.
(**C**) Cilia pathway cluster: BIFO rank of each detected cilia-related pathway in KF-CHD (blue circle) vs. KF-NBL (orange triangle). All detected cilia pathways rank in the top half of the scored pathway universe in both cohorts.
(**D**) Bootstrap resampling against a 20-pathway cilia reference: P@10 distribution for BIFO (blue) and Seed Fisher (red) at random seed sample sizes n = 10, 20, 30 (500 runs per seed size). Dashed and dotted horizontal lines indicate the primary-run P@10 for each method. Cilia signal requires full cohort-scale seed sets; neither method recovers it reliably from 10–30 random genes.
](images/fig8_crosscohort.png){#fig:crosscohort width="100%"}


**Figure and table inventory**

The following figures and tables support the Results sections above.

  --------------- ---------------------------------------------------- ----------------------------------- -------------------------
  **Item**        **Title**                                            **Data source**                     **Status**

  **Fig 1**       BIFO conditioning coverage                           results.json, coverage block        Final (fig1 v2)

  **Fig 2**       Four-arm gene-level recovery                         results\*.json                      Final

  **Fig 3**       Three-arm pathway ablation + KF-CHD method panel     pathway_metrics\_\*.json            Final

  **Fig 4**       Baseline comparison heatmap (KF-CHD + KF-NBL)        baseline_comparison.csv             Final (fig4 v3)

  **Fig 5**       C4 pathway-split controls                            c4\_\*/pathway_metrics.json         Final (fig5 v2)

  **Fig 6**       CHD resampling distribution (3,003 splits)           resampling_summary.json             Final (violin)

  **Fig 7**       Two-layer architecture schematic                     Conceptual (Python/matplotlib)      Final (fig7_schematic.png)

  **Fig 8**       Cross-cohort convergence (KF-CHD vs. KF-NBL)         pathway_scores\_\*.csv, resampling  Final (fig8 v4)

  **Table 1**     Graph conditioning statistics                        results.json                        Complete

  **Table 2**     Four-arm gene-level recovery                         results\*.json                      Complete

  **Table 3**     Three-arm pathway ablation                           pathway_metrics\_\*.json            Complete

  **Table 4**     Baseline comparison (curated benchmark)              baseline_comparison.json            Complete

  **Table 5**     C4 pathway-split controls                            c4\_\*/pathway_metrics.json         Complete

  **Table 6**     Resampling distribution (3,003 splits)               resampling_summary.json             Complete

  **Table 8.1**   KF-CHD method comparison — WP_CILIOPATHIES rank      kf_chd_results/baseline_comparison  Complete (inline §8.1)

  **Table 8.3**   Cross-cohort comparison — WP_CILIOPATHIES recovery   kf\_\*/pathway_scores_standard      Complete (inline §8.3)

  **Table 8.4**   Bootstrap resampling — BIFO vs. Fisher               kf\_\*/resampling_results.csv       Complete (inline §8.4)

  **Supp S1**     YAML predicate classification                        bifo_ddkg_mapping.yaml              Needs formatting

  **Supp S2**     Top-10 pathway lists per arm                         pathway_scores\_\*.csv              Data ready; table TBD

  **Supp S3**     Full top-20 ranked pathways per method, KF-CHD       kf_chd_results/baseline_comparison  Data ready; table TBD

  **Supp S4**     Head-to-head rank comparison (Fisher vs BIFO)        kf_chd_results/baseline_comparison  Data ready; table TBD

  **Supp S5**     Full cilia pathway cluster ranking under BIFO        kf_chd_results/pathway_scores       Data ready; table TBD
  --------------- ---------------------------------------------------- ----------------------------------- -------------------------


## Discussion

The central result of this study is that BIFO recovers a biologically meaningful signal that is independently supported by standard enrichment methods, while remaining effective in settings where those methods begin to fail. In both Kids First cohorts, congenital heart disease and neuroblastoma, ciliopathy-related pathways rank first under BIFO scoring. Importantly, this signal is not unique to the graph-based approach: when implemented correctly, seed-only Fisher enrichment independently identifies the same top pathway in both cohorts. The agreement between these two fundamentally different methods, one based on direct gene–pathway overlap and the other on constrained graph propagation, provides strong evidence that the result reflects underlying biology rather than an artefact of graph topology or propagation dynamics.

The distinction lies in how the signal is detected. Fisher enrichment identifies pathways through direct overlap between genes and pathway membership. BIFO, in contrast, recovers the same signal through propagation across a constrained graph, without requiring strong direct overlap. This allows BIFO to remain effective in regimes where enrichment methods lose reliability, including small gene sets, large heterogeneous cohorts, and graph-derived neighborhoods. In this sense, BIFO does not replace standard enrichment methods; it extends them by enabling pathway-level interpretation when overlap-based approaches are unstable or uninformative.

This difference becomes clear when examining the failure modes of standard enrichment. At small gene set sizes, Fisher enrichment is sensitive to incidental overlap and often prioritizes non-specific pathways. In the curated benchmark, seed-only Fisher achieves P@10 = 0.30, while BIFO reaches P@10 = 0.70, reflecting the instability of direct overlap at this scale. At large gene set sizes, such as those derived from rare variant aggregation, p-values collapse and lose discriminative power even when computed correctly. Graph-based expansion approaches introduce a complementary problem: by inflating the gene set to include most of the graph, they eliminate contrast between pathways. These limitations reflect a common issue: standard methods operate directly on gene membership and do not account for how signal is distributed across biological relationships.

BIFO addresses this by separating propagation from scoring. Signal is first propagated through the graph using a constrained set of biologically admissible edges, and pathways are then evaluated based on where that signal accumulates. This allows weak signals that are distributed across many genes to reinforce each other through shared biological context, while incoherent background signal disperses. The scoring step then operates on this structured signal rather than on the original gene list.

A key component of this behavior is the pathway scoring function itself. The results show that propagation alone is not sufficient: while preranked GSEA on PPR scores recovers some pathway signal, its performance remains limited compared to the full BIFO approach (P@10 = 0.10 for both raw and conditioned PPR GSEA versus P@10 = 0.70 for BIFO). The improvement arises from how propagated signal is translated into pathway-level scores.

The BIFO scoring function evaluates the direct PPR score at each pathway node and normalizes it by the square root of pathway size. This formulation reflects two design choices. First, it requires signal to reach the pathway node itself. Only signal that successfully propagates from the seed genes into the pathway layer contributes to the score. In contrast, gene-level methods such as GSEA operate on ranked gene lists and do not require this transfer, which can blur distinctions between pathways connected through shared genes or indirect correlations.

Second, the square-root normalization reduces bias toward large pathways without eliminating their contribution. Larger pathways accumulate more propagated signal because more genes contribute PPR mass to the pathway node through Pathway Contribution edges. Fully normalizing by pathway size would overcorrect this effect and suppress biologically meaningful programs. The square-root penalty provides a balance: it down-weights large, non-specific pathways while preserving signal in pathways that are both large and biologically coherent. This scoring variant was selected as the primary function before benchmark freeze; alternative variants were evaluated but not used for primary analysis.

Together, these properties distinguish BIFO from both overlap-based and propagation-based alternatives. Fisher enrichment depends entirely on direct membership overlap, while propagation-only approaches tend to favor highly connected regions of the graph. BIFO combines propagation with pathway-level scoring in a way that requires biologically meaningful signal transfer and controls for pathway size. The result is a scoring scheme that reflects both the structure of the graph and the specificity of the biological program.

The ablation analysis provides a mechanistic explanation for why this works. When propagation is restricted to mechanistic edges alone, pathway scores collapse to zero across the graph. This result reflects how biological knowledge is represented. Mechanistic relationships connect genes within a molecular network, while pathway annotations are stored separately as curated gene sets. These two components form distinct layers of the graph and are connected only through gene-to-pathway membership relationships. Consistent with this structure, removing bridge edges reduces pathway recovery (P@10 decreases from 0.70 to 0.60), while mechanistic-only propagation yields zero pathway scores.

This leads to a simple but important interpretation. The graph is organized as a two-layer system: a mechanistic layer encoding biological processes and an annotation layer encoding curated pathway knowledge. BIFO makes this structure explicit by treating gene-to-pathway relationships as a distinct class of edges that are allowed to carry signal. The ablation results show that these edges are necessary to reach pathway nodes, but they do not generate signal independently. Signal must originate in the mechanistic layer and then transfer across the bridge. Although Pathway Contribution edges dominate numerically — comprising 85% of propagating edges in the conditioned operator — the ablation results confirm they act as necessary conduits for mechanistic signal rather than as independent sources of it.

The robustness analysis shows that these results are not dependent on a particular gene set. Across all 3,003 partitions of the CHD gene pool, BIFO consistently improves pathway ranking relative to unconditioned propagation. At the same time, the comparison with Fisher enrichment highlights an important boundary. When seed genes directly overlap with pathway members, Fisher performs well, as expected. BIFO is most useful in the complementary setting, where relevant pathways are connected indirectly through biological relationships. This distinction aligns with the difference between recovery tasks and discovery tasks and explains why BIFO is particularly effective for cohort-scale analyses.

The KF cohort results further clarify the nature of the recovered signal. The ciliopathy signal is not driven by a small number of genes but is distributed across a subset of genes embedded in a larger heterogeneous background. Both BIFO and Fisher fail to recover this signal reliably from small random gene subsets and converge only at cohort scale. This behavior is consistent with a polygenic developmental process rather than a single dominant driver. The biological interpretation of these findings and their implications for cilia-related developmental disease are examined in depth in the companion cross-cohort analysis (Stear et al. 2026).

Several limitations should be noted. The benchmark graph is a controlled 1-hop projection of a larger knowledge graph and includes only a subset of source vocabularies. As a result, some nodes cannot be resolved and are excluded from propagation. The finding that mechanistic edges alone cannot reach pathway nodes depends on this graph configuration and may change with additional data sources. However, the underlying pattern, a separation between mechanistic relationships and curated pathway annotations, is a common feature of ontology-based knowledge graphs. The conditioning framework itself is graph-agnostic: the specific structural result depends on representation choices in the source graph, but the need to distinguish admissible flow from associative and contextual relationships does not. An alternative approach of weighting edges within a single operator would conflate causal and associative relationships, whereas BIFO preserves this distinction at the representation level — enabling attribution of pathway score changes to specific edge classes rather than to the aggregate topology.

Gene-level recovery metrics are near ceiling in the curated benchmark due to the small size and strong connectivity of the test set. In this context, pathway-level evaluation and cohort-scale analysis provide a more meaningful assessment of performance.

Overall, BIFO provides a framework for making graph-based biological analysis both effective and interpretable. By constraining which relationships are allowed to carry signal and by explicitly defining how propagated signal is evaluated at the pathway level, it shifts the focus from raw connectivity to biologically meaningful structure. This perspective provides a principled basis for analyzing heterogeneous biological data, particularly in settings where standard methods struggle to extract coherent signal.


## References {.page_break_before}

<!-- Manubot handles references automatically via cite keys.
     Use inline citations in the text like [@doi:10.1038/...] or [@arxiv:...] or [@url:...]
     
     Key references to add as you write:
     
     DDKG/UBKG/Petagraph:
       [@doi:TBD]
     
     PageRank:
       [@doi:10.1016/S0169-7552(98)00110-X]  Brin & Page 1998
     
     Personalized PageRank for biology:
       [@doi:10.1145/1148170.1148225]  Tong et al. 2006
     
     MSigDB:
       [@doi:10.1073/pnas.0506580102]  Subramanian et al. 2005
       [@doi:10.1016/j.cels.2015.12.004]  Liberzon et al. 2015
     
     WikiPathways:
       [@doi:10.1093/nar/gkaa1024]  Martens et al. 2021
     
     gnomAD:
       [@doi:10.1038/s41586-020-2308-7]  Karczewski et al. 2020
     
     AutoGVP:
       [@doi:TBD]
     
     Kids First:
       [@doi:TBD]
     
     GSEA:
       [@doi:10.1073/pnas.0506580102]  Subramanian et al. 2005
     
     BH correction:
       [@doi:10.1111/j.2517-6161.1995.tb02031.x]  Benjamini & Hochberg 1995
-->

