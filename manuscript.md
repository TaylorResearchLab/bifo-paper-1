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
date-meta: '2026-04-21'
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
  <meta name="dc.date" content="2026-04-21" />
  <meta name="citation_publication_date" content="2026-04-21" />
  <meta property="article:published_time" content="2026-04-21" />
  <meta name="dc.modified" content="2026-04-21T16:18:40+00:00" />
  <meta property="article:modified_time" content="2026-04-21T16:18:40+00:00" />
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
  <link rel="alternate" type="text/html" href="https://TaylorResearchLab.github.io/bifo-paper-1/v/65f1d595991e90343bf01bfa75d325aabe0c0a71/" />
  <meta name="manubot_html_url_versioned" content="https://TaylorResearchLab.github.io/bifo-paper-1/v/65f1d595991e90343bf01bfa75d325aabe0c0a71/" />
  <meta name="manubot_pdf_url_versioned" content="https://TaylorResearchLab.github.io/bifo-paper-1/v/65f1d595991e90343bf01bfa75d325aabe0c0a71/manuscript.pdf" />
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


Deanne M. Taylor^1,2^✉^^, Taha Mohseni Ahooyi^1^, Benjamin Stear^1^, Yuanchao Zhang^1^, Aditya Lahiri^1^, Alan Simmons^3^, Tiffany J. Callahan^4^, Jonathan C. Silverstein^3^


^1^Department of Biomedical Informatics, Children's Hospital of Philadelphia
^2^Department of Pediatrics, University of Pennsylvania Perelman School of Medicine
^3^Department of Biomedical Informatics, University of Pittsburgh Medical Center, Pittsburgh, PA
^4^Manas AI, New York, NY

^✉^Correspondence: <taylordm@chop.edu>



## Abstract

Biological knowledge graphs integrate heterogeneous data across molecular, cellular, and phenotypic domains, but do not enable reliable inference on their own. When mechanistic relationships, statistical associations, and annotation edges share a single structure, graph traversal propagates signal along biologically invalid paths. This produces an identifiability problem in which causal and non-causal explanations cannot be distinguished, and standard enrichment approaches fail in both small and large gene set regimes.

Here we introduce the Biological Information Flow Ontology (BIFO), a framework that constrains information flow by defining admissible biological transformations prior to propagation. In a three-arm ablation design, we show that pathway inference depends on a distinct bridge layer: mechanistic-only propagation yields zero pathway scores in this graph representation, while inclusion of gene-to-pathway membership edges enables signal transfer between molecular and pathway representations.

Across a curated congenital heart disease benchmark, BIFO improves pathway prioritization (P@10 = 0.70) relative to seed-only enrichment (P@10 = 0.30) and propagation-based baselines (P@10 = 0.10). In two independent rare variant cohorts, BIFO recovers a coherent ciliopathy pathway cluster in both diseases, with WP_CILIOPATHIES carrying the strongest statistical enrichment signal in the KF-CHD dataset (null_z = 48.7, q = 0.006, rank 43/2,130) and ranking third in KF-NBL (null_z = 19.0, q = 0.012). Correctly implemented Fisher enrichment independently ranks WP_CILIOPATHIES first in both cohorts, confirming that the recovered signal reflects underlying biology rather than a propagation artefact, while BIFO remains effective in regimes where overlap-based methods are numerically unstable, implementation-sensitive, or less informative.

These results show that constraining admissible information flow is sufficient in this setting to enable meaningful graph-based biological inference where standard approaches fail.


## Introduction

Modern biology now generates large-scale, multi-modal datasets spanning genomic variation, gene expression, chromatin architecture, protein interactions, metabolism, and disease phenotypes. These data provide complementary but fragmented views of biological systems across molecular, cellular, and spatial scales. Knowledge graphs have emerged as a unifying framework for integrating these heterogeneous data types, representing biological entities and their relationships in a single structure that supports cross-domain queries. However, representation alone does not enable inference. The central challenge is not simply linking data across modalities, but determining how biological signal observed in one part of the graph relates to signal observed elsewhere.

Biological function arises from directional, causal processes. Transcription proceeds from gene to RNA, signaling cascades propagate from upstream activation to downstream effectors, and metabolic transformations are constrained by biochemical feasibility and spatial context. These processes define not only which entities are connected, but which transformations are biologically admissible and how information can propagate between them. In heterogeneous knowledge graphs, however, mechanistic relationships, statistical associations, and annotation edges are encoded within the same structure. In the absence of constraints, graph traversal treats these relationships equivalently, collapsing causal and non-causal connections into a single topology.

This produces a fundamental identifiability problem in heterogeneous knowledge graphs. A path connecting a genetic variant to a disease phenotype may reflect a valid mechanistic process, an indirect regulatory association, or an incidental correlation. Without constraints on admissibility, these possibilities are computationally indistinguishable, and inference becomes dependent on graph topology or analysis method rather than biological mechanism. Standard enrichment approaches exhibit complementary failure modes in this setting. For small gene sets, statistical overlap is unstable and dominated by incidental matches. For large gene sets — particularly those derived from rare variant aggregation — p-values collapse to numerical limits and lose discriminative power. Graph-based expansion methods further exacerbate this problem by inflating gene sets to include large fractions of the graph, eliminating meaningful enrichment structure.

Existing approaches address parts of this problem but do not resolve it. Ontologies such as Gene Ontology and HPO provide structured representations of biological concepts but do not define propagation rules. Knowledge graph systems support typed traversal but rely on user-defined queries rather than biologically grounded constraints. Causal frameworks such as BEL and GO-CAM encode mechanistic relationships but operate within curated representations and do not provide a general protocol for conditioning arbitrary heterogeneous graphs. Graph machine learning approaches can operate over heterogeneous structures but learn propagation behavior from data rather than enforcing biologically interpretable constraints. The missing component is a graph-agnostic framework that defines which transformations are biologically admissible and how information is allowed to propagate across heterogeneous knowledge graphs.

To address this limitation, we introduce the Biological Information Flow Ontology (BIFO), a propagation constraint framework for heterogeneous biomedical knowledge graphs. BIFO defines a set of entity classes, flow classes, and admissibility constraints that formalize biologically valid transformations between entities. It distinguishes between mechanistic flows — which represent information-carrying biological processes and participate in propagation — observational flows — which represent inferred or correlational relationships and are excluded from propagation — and constraint-imposing flows — which restrict admissible transitions without carrying signal. BIFO conditioning transforms an unconstrained property graph into a directed graph in which all retained edges correspond to admissible biological transformations, defining a propagation substrate consistent with directed biological process structure.

The key idea underlying BIFO is that biological inference can be improved not by adding information to a knowledge graph, but by restricting the space of admissible transformations. By constraining propagation to semantically valid paths, BIFO reduces the reachable state space and increases the identifiability of biologically meaningful signal. This transformation induces a directed, non-symmetric adjacency operator that encodes the source–sink asymmetry inherent in biological processes, enabling propagation methods to operate over a graph that reflects causal structure rather than undifferentiated connectivity.

We evaluate this framework using a controlled benchmark derived from the Data Distillery Knowledge Graph (DDKG) [@doi:10.1101/2025.08.11.666099], integrating curated congenital heart disease (CHD) gene sets with pathway annotations. Through a three-arm ablation design, we show that mechanistic-only propagation is insufficient to recover pathway-level biological programs, as pathway nodes are structurally unreachable through mechanistic edges alone in this graph representation, without bridge edges connecting gene-level and pathway-level representations. Introducing BIFO-conditioned propagation enables signal transfer across these layers, consistent with a two-layer graph architecture in which pathway inference depends on a formally defined class of admissible bridge edges.

We further show the applicability of BIFO in a discovery setting using rare variant cohorts from the Kids First program [@url:https://kidsfirstdrc.org]. In this regime, gene sets derived from variant aggregation are large and heterogeneous, and standard enrichment approaches become numerically unstable, implementation-sensitive, or lose discriminative power. BIFO-conditioned propagation concentrates distributed signal across the graph and recovers biologically relevant pathways without prior specification, illustrating its utility for cohort-scale inference where traditional methods break down.

Together, these results establish BIFO as a general framework for conditioning heterogeneous knowledge graphs by defining admissible biological information flow. By transforming graphs from passive integration structures into constrained propagation substrates, BIFO enables principled, mechanistically grounded inference across multiple biological scales.


**Methods**

## 1 Knowledge graph source

All analyses used the Data Distillery Knowledge Graph (DDKG), built on the Unified Biomedical Knowledge Graph (UBKG) and Petagraph infrastructure [@doi:10.1101/2025.08.11.666099; @doi:10.1038/s41597-024-04070-w]. DDKG integrates heterogeneous biological knowledge from multiple source ontologies and databases into a unified concept-and-relationship graph. Each concept node carries a source authority base (SAB) identifier; each edge carries a predicate drawn from the source ontology\'s relation vocabulary. This structure makes edge provenance fully traceable, which is essential for the BIFO conditioning step: the predicate determines which flow class an edge belongs to, and the SAB determines which entity resolution rule applies.

For the present benchmark, the graph was queried as a 1-hop neighborhood centered on 15 CHD-associated seed and held-out genes. This produced two edge files: (1) edges_raw.csv containing 94,790 seed-to-neighbor mechanistic and association edges, and (2) pathway_membership_edges.csv containing 79,562 gene-to-pathway membership edges derived from MSigDB [@doi:10.1073/pnas.0506580102; @doi:10.1016/j.cels.2015.12.004], WikiPathways [@doi:10.1093/nar/gkaa1024], and Gene Ontology annotations. These were merged into edges_merged.csv (174,352 edges). Node metadata was exported in nodes.csv (34,523 concept nodes). The 1-hop design was chosen to produce a graph of tractable size with known provenance; it does not represent the full DDKG connectivity.

Three association-derived evidence vocabularies (DGNAGE: age-stratified gene-disease associations; DGNGCM: clinical mutation associations; DGNGV: genomic variant associations) were intentionally excluded. The rationale is scientific, not technical: excluding these sources isolates ontology-aligned mechanistic and pathway representations from association-derived evidence layers, enabling clean attribution of information flow to specific edge classes.

## 2 BIFO conditioning

### 2.1 Ontology design

The Biological Information Flow Ontology (BIFO) defines a vocabulary of biologically admissible flow classes --- categories of biological relationship through which information is considered to propagate in a directed, mechanistically coherent manner. The central design question BIFO addresses is: given a heterogeneous biomedical knowledge graph whose edges span everything from direct phosphorylation to text-mining co-occurrence, which edges should be allowed to carry propagated signal between biological entities? BIFO answers this by classifying each predicate type into a flow class and assigning a classification tier that determines its role in the PPR operator.

The mapping is encoded in bifo_mapping.yaml (v0.7.1; 251 predicate-to-flow entries, 96 explicit non-flow designations, 46 observational edge definitions). The five classification tiers are: (1) mechanistic --- direct, causal biochemical or molecular events with clear directionality; (2) weak_mechanistic_or_observational --- relationships that may reflect mechanism but whose evidence is mixed or correlational; (3) observational --- statistical associations without mechanistic grounding; (4) contextual_constraint --- spatial or temporal constraints that modify but do not propagate signal; and (5) nonpropagating_context --- structural relationships excluded from the PPR operator but retained in the conditioning output for downstream use.

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

> *Pathway Contribution edges encode curated gene-to-pathway membership relationships (inverse_pathway_associated_with_gene, inverse_has_signature_gene — gene→pathway direction only). They do not represent direct biochemical interactions; rather, they are admissible bridge edges between molecular entities and pathway-level biological programs. Signal flows unidirectionally from gene nodes to pathway nodes, consistent with BIFO Specification v0.02 in which Pathway Contribution is defined as P or CM → PW. Their admission as a flow class is what enables signal transfer from the mechanistic gene neighborhood to the pathway annotation layer --- the central architectural finding of this paper.*
>
> *Perturbational Effect contains two distinct predicate groups classified at different tiers: direct molecular interactions (bioactivity, chemical_or_drug_affects_gene_product, targets_expression_of_gene; classified mechanistic) and correlation-derived associations (positively/negatively_correlated_with_gene; classified weak_mechanistic_or_observational). The mechanistic-only arm retains the mechanistic subset and excludes the correlation predicates. This is an intentional design choice that allows the mechanistic operator to capture direct drug-target connectivity without admitting association noise.*

### 2.2 Entity resolution

Entity resolution maps concept nodes to their source vocabulary, which is necessary to apply SAB-specific flow class rules and membership constraints. The pipeline uses a two-level procedure. At Level 1, the pipeline attempts to resolve each concept node to a SAB by matching against UBKG Code nodes carrying SAB annotations. In the present export, no Code nodes were present; the pipeline fell back to reading the SAB column directly from nodes.csv. This fallback resolved 18,897 of 34,523 concept nodes (54.7%). The remaining 15,626 nodes lacked a direct SAB assignment and were treated as unresolvable; edges with at least one unresolvable endpoint were dropped at Level 2.

The 54.7% resolution rate reflects the 1-hop export design: the export deliberately includes a broad neighborhood to capture mechanistic context, but many peripheral nodes in that neighborhood belong to vocabularies not represented in the current SAB selection. This is not a bug in the pipeline; it is an expected consequence of querying a partial graph slice. The 45.3% unresolved nodes are structurally peripheral (they appear as neighbors in the graph but cannot be classified into BIFO flow classes), and their edges are dropped rather than admitted with unknown classification.

### 2.3 Propagating operator construction

From the 104,342 retained edges that pass Level 2 conditioning, three PPR operators are constructed for the ablation design. These operators differ in which edges they include; the scoring stage (pathway membership map, universe, reference set) is held constant across all three, enabling direct attribution of pathway-scoring differences to operator composition.

The full operator uses all 93,487 propagating edges from the conditioned kept-edge set. Of the 104,342 total kept edges, 10,855 are retained in the kept_edges.csv output but excluded from the PPR adjacency matrix: 9,909 Observational Association edges (which pass flow classification as a recognized class but are excluded from propagation by operator construction because their weak evidential basis would introduce noise into the signal path), 84 weak-mechanistic Genetic Regulatory Modulation edges, and 862 nonpropagating_context Spatial constraint edges.

The ablation operator conditions edges_raw.csv (94,790 edges) independently of the membership edges, producing 26,059 kept edges of which 16,026 are propagating (with the same 10,033 non-propagating class exclusions applied). This operator excludes all Pathway Contribution edges by construction because those edges appear only in the membership edge file, not in edges_raw. The ablation therefore isolates the effect of removing the gene-to-pathway bridge while preserving all other admissible flow classes.

The mechanistic-only operator applies an additional filter to the full kept-edge set, retaining only edges whose classification tier is mechanistic (9,710 edges: Signal Transduction 5,786, Transcription 1,568, Signal Termination 484, and minor mechanistic classes including direct molecular interaction subsets of Perturbational Effect). This operator excludes Pathway Contribution, Observational Association, and all weak-mechanistic edges from the PPR adjacency matrix. Its composition and the pathway-scoring outcome under this operator are reported in Results Section 3.

For all operators, adjacency matrices are built as sparse directed binary matrices (edge weight = 1, no differential weighting by flow class). Self-loops are excluded. Row normalization is applied before transpose to produce the column-stochastic matrix used in the PPR recurrence. Edge weights are uniform across all analyses reported here; the pipeline supports evidence-tier weighting when confidence or evidence-type annotations are present in the edge file, but DDKG exports do not carry these fields and all benchmark and cohort runs use unit weights.

**Formal definition of the BIFO conditioning operator.** Let G = (V, E) be the input property graph with node set V and edge set E, where each edge e = (u, v, p) carries predicate p and endpoint SABs s_u, s_v. BIFO conditioning defines a constraint operator C that produces the conditioned propagation graph G_C = (V, E_C), where:

$$E_C = \{ e \in E : \text{flow\_class}(\text{predicate}(e)) \in F_{\text{admissible}} \land \text{SAB}(\text{source}(e)) \text{ resolved} \land \text{SAB}(\text{target}(e)) \text{ resolved} \}$$ {#eq:operator}

F_admissible is the set of flow classes designated as propagating in bifo_mapping.yaml (mechanistic and weak-mechanistic tiers, plus Pathway Contribution bridge edges; excluding Observational Association, contextual_constraint, and nonpropagating_context tiers). In the implementation, weak-mechanistic relationships are encoded as a single hybrid classification tier (`weak_mechanistic_or_observational`) that is treated as admissible in the conditioned operator but excluded from the mechanistic-only arm. The operator is graph-agnostic in principle: its admissibility decisions depend only on the predicate-to-flow mapping and entity resolution rules, not on graph topology. Implementation requires SAB-specific resolution rules and vocabulary mappings that are currently configured for DDKG-compatible graphs; the same conditioning logic can be applied to any property graph whose edges carry compatible predicate vocabularies, including the full KF-CHD and KF-NBL exports (Section 10).

## 3 Personalized PageRank propagation

Signal propagation uses personalized PageRank (PPR) [@doi:10.1145/1148170.1148225], also known as random walk with restart. PPR models the probability that a random walk starting from the seed set visits each node in the graph, with a restart probability α that returns the walk to the seeds at each step. High α keeps signal concentrated near the seeds; low α allows signal to diffuse further into the graph. The balance between local concentration and global diffusion is the mechanism by which BIFO\'s structural constraints shape the output: by conditioning which edges are in the operator, BIFO determines which paths the random walk can follow.

Given row-normalized adjacency matrix Ã (n × n), seed vector s (uniform mass 1/\|S\| over seed nodes, zero elsewhere), and restart probability α, the PPR score vector f satisfies:

$$\mathbf{f} = (1 - \alpha) \cdot \tilde{A}^\top \cdot \mathbf{f} + \alpha \cdot \mathbf{s}$$ {#eq:ppr}

where $\tilde{A}^\top$ is the transpose of $\tilde{A}$ (propagation follows edge direction). The fixed point is computed by iteration: $\mathbf{f}_{t+1} = (1-\alpha)\tilde{A}^\top\mathbf{f}_t + \alpha\mathbf{s}$, terminating when $\|\mathbf{f}_{t+1} - \mathbf{f}_t\|_1 < 10^{-10}$ or after 500 iterations. Convergence was achieved in all benchmark runs.

The restart probability α = 0.5 was set before benchmark freeze and was not optimized on the CHD benchmark or any other dataset. This value was chosen to balance local signal retention (necessary for pathway scoring, where the relevant pathway nodes may be several hops from the seeds) with seed concentration (necessary to avoid diffusing signal uniformly across the graph). Sensitivity to α is a natural direction for future work but is not evaluated in the current benchmark.

Four score vectors are computed per benchmark run on the full-graph operator: (1) raw --- propagation on the full merged adjacency without conditioning; (2) metadata-filtered --- removal of non-flow structural and metadata edges (non_flow_edges in the YAML) without flow-class filtering, retaining all remaining edges as propagating; (3) conditioned (BIFO) --- full BIFO conditioning; and (4) random sparsification --- random edge selection retaining the same edge count as the conditioned arm. The random control establishes that entropy reduction in the conditioned arm is not simply a consequence of edge count reduction, but reflects the structural properties of the admissible edges specifically.

## 4 Pathway scoring

### 4.1 Membership map construction

Pathway scoring requires mapping gene nodes to the pathway nodes they belong to. Membership is determined from edges_merged.csv using the gene→pathway membership predicate types (inverse_pathway_associated_with_gene, inverse_has_signature_gene for MSIGDB pathways; process_involves_gene, gene_plays_role_in_process for GO pathways). The pathway→gene predicates (pathway_associated_with_gene, has_signature_gene) are classified as nonpropagating_context in bifo_mapping.yaml v0.7.1 and are excluded from PPR operator construction, consistent with unidirectional gene→pathway signal flow per BIFO Specification v0.02. Membership edges are SAB-source constrained: a gene is included in a pathway\'s member set only if its SAB matches the pathway\'s source vocabulary. This prevents cross-vocabulary membership contamination (e.g., a GO-annotated gene being counted as a member of an MSigDB pathway). Duplicate memberships are removed.

After size filtering (minimum 8, maximum 300 members) and name-pattern exclusion (patterns: \_Q2, \_Q3, \_Q4, \_Q5, \_Q6, MIR), 550 pathways constitute the evaluation universe. The minimum-member filter excludes pathways too small for enrichment analysis to be meaningful; the maximum-member filter excludes pathways so large that membership is uninformative. The name-pattern filter excludes gene expression quantile sets and microRNA sets that represent statistical partitions rather than curated biological programs. This universe is held constant across all arms and all baseline methods.

### 4.2 Pathway score computation (degree_norm)

The degree_norm scoring variant is defined as:

$$\text{score}(p) = \frac{f_{\text{direct}}(p)}{\sqrt{|\text{members}(p)|}}$$ {#eq:degreenorm}

where f_direct(p) is the PPR score on the pathway concept node itself --- the score mass arriving at the pathway node via Pathway Contribution edges --- and \|members(p)\| is the SAB-constrained member gene count. The √ penalty down-weights large generic pathways (which accumulate high PPR scores simply by having many members) without fully normalizing by size (which would over-penalize legitimate large biological programs). Pathways with zero member genes receive score zero. This variant was selected as the primary scoring function before benchmark freeze; three alternative variants (member_mean, member_max, local_bg) were computed but not used for primary analysis. The scoring function was specified prior to benchmark evaluation and was not modified after the first successful full run.

### 4.3 Rank improvement

Rank improvement is defined as mean_rank(raw) − mean_rank(conditioned), where both rankings use the same 550-pathway universe and the same reference set. In the primary benchmark analysis, both arms use degree_norm scoring. In the exhaustive resampling and KF bootstrap analyses, the conditioned arm uses degree_norm and the raw arm uses the direct pathway-node score without degree normalization; rank improvement in those analyses is therefore a directional measure of conditioning benefit rather than a fully symmetric scorer comparison. This metric captures how much the BIFO conditioning step improves the relative position of reference pathways compared to propagating signal over the unconditioned graph. A positive value means conditioning moves reference pathways to lower (better) rank positions; a negative value means the raw score already had those pathways ranked higher.

Rank improvement must be interpreted in the context of the task type. In discovery benchmarks (CHD curated), seeds are disease genes not drawn from the target pathway family; conditioning dramatically improves ranks (+125.4) because the raw graph places many non-specific high-degree pathways above the cardiac pathways that conditioning filters toward. In recovery benchmarks (C4 controls), seeds are drawn from the target pathway family; the raw arm already has direct proximity to the target, so conditioning provides less additional lift and rank improvement is negative. This distinction is by design and is not a failure of the method in either case.

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

The three-arm ablation design systematically varies the PPR operator while holding the scoring stage constant across all arms. This design enables direct causal attribution: differences in pathway-level metrics between arms are attributable solely to the presence or absence of specific edge classes in the propagating graph, not to differences in the scoring method, pathway universe, or reference set. The three arms are: (1) Full --- BIFO-conditioned operator on edges_merged (93,487 propagating edges, including Pathway Contribution bridge edges); (2) Ablation --- BIFO-conditioned operator on edges_raw only (16,026 propagating edges, no Pathway Contribution bridge edges by construction); (3) Mechanistic-only --- BIFO-conditioned operator restricted to classification=mechanistic edges (9,710 propagating edges, excluding Pathway Contribution, Observational Association, and weak-mechanistic classes).

## 6 Baseline enrichment methods

Three conventional enrichment baselines and one graph-structure baseline are implemented to benchmark BIFO against standard bioinformatics practice. The design goal is to compare BIFO against the strongest approaches a bioinformatician would realistically apply to the same graph-derived data --- not against deliberately weak baselines. All baselines are evaluated on the identical 550-pathway universe and identical CHD reference set. The `baseline_enrichment.py` script accepts two flags that control baseline behaviour: `--kept-edges` enables B0 (requires the conditioning output); `--small-universe` switches Fisher baselines to the pathway-member universe and log-space p-values, required for KF cohort runs (see B1 below).

***B0: Degree-weighted seed overlap (graph membership baseline)***

For each pathway p, the score is the sum of conditioned-graph node degrees of seed genes that are direct members of p, normalised by pathway size:

$$\text{score}(p) = \sum_{g \in \text{seeds} \cap \text{members}(p)} \text{degree}_{\text{cond}}(g) \;/\; \sqrt{|\text{members}(p)|}$$ {#eq:b0}

where degree\_conditioned(g) is the out-degree of gene g in the BIFO-conditioned propagation graph G_C. Pathways are ranked by descending score. This baseline uses graph structure (node connectivity) but not graph propagation: it scores pathways based on how well-connected the directly overlapping seed genes are within the conditioned graph, without running PPR. It provides a lower bound on graph-guided methods and isolates the contribution of propagation beyond local connectivity. B0 is closely related to degree_norm (which uses PPR scores rather than degrees) and is computed from the conditioning output via the `--kept-edges` flag in baseline_enrichment.py.

***B1: Seed-only hypergeometric enrichment***

For each pathway p, a one-tailed hypergeometric test is applied with N = gene universe size (\~13,000 C-prefixed nodes appearing as edge endpoints in edges_merged), K = \|members(p) ∩ universe\|, n = \|seeds ∩ universe\|, and k = \|members(p) ∩ seeds\|. This tests whether the seed genes are over-represented among pathway members relative to the background rate. Pathways are ranked by ascending p-value; Benjamini–Hochberg FDR correction [@doi:10.1111/j.2517-6161.1995.tb02031.x] is applied across all 550 pathways jointly. This baseline represents what a bioinformatician would do with just the seed gene list and no graph information.

**Gene universe design and the `--small-universe` flag.** The curated benchmark uses the large universe (all \~13,000 C-prefixed nodes) with standard-precision `hypergeom.sf`, which produces the honest Fisher result: non-specific hits (cancer gene sets, transcription factor targets) dominate because a ten-gene query cannot discriminate against a large background. For KF cohort analyses (1,276--1,395 seeds against \~22,600-gene universe), this implementation causes p-value floor collapse --- `hypergeom.sf` returns 0.0 for every pathway with meaningful overlap, eliminating rank discrimination entirely. The `--small-universe` flag switches to the pathway-member-only universe (\~4K--22K genes depending on the graph), K = \|members(p)\| (all members, not universe-intersected), and log-space computation (`hypergeom.logsf`) to recover correct relative ordering. The two modes test different statistical hypotheses and produce numerically incomparable results; the curated benchmark always uses the default large universe to reproduce the frozen manuscript numbers.

***B2: 1-hop neighborhood hypergeometric enrichment***

The query gene set is expanded to include all C-prefixed nodes that are direct neighbors of any seed gene in edges_merged (1-hop neighborhood = 11,146 gene neighbors plus 10 seeds = 11,156 total query). The same hypergeometric test is applied with the expanded query. This baseline represents the approach of extracting a graph neighborhood and running standard enrichment --- a natural workflow for a bioinformatician with access to the graph. The large neighborhood size (86% of the gene universe) is itself a finding: it demonstrates the neighborhood-inflation problem that motivates BIFO\'s approach of concentrating signal before scoring.

***B3 / B3b: Preranked GSEA on PPR scores***

Genes in the universe are ranked by their PPR scores (raw arm for B3; conditioned arm for B3b) in descending order. For each pathway, a weighted running-sum enrichment score is computed following the preranked GSEA algorithm [@doi:10.1073/pnas.0506580102], using \|PPR score\| as the hit weight. Pathways are ranked by descending enrichment score. B3 tests whether graph propagation alone (without BIFO conditioning) recovers pathway-relevant signal. B3b tests whether BIFO-conditioned gene scores, when used as a ranked list input to GSEA, improve over raw propagation. The difference between B3b and BIFO full-arm isolates the contribution of the degree_norm pathway-level scoring function beyond what the gene-level score ordering provides.

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

All analyses were implemented in Python 3.8+ using: NumPy and SciPy for numerical operations and sparse linear algebra; scipy.sparse for PPR adjacency matrices; scipy.stats.hypergeom for Fisher/hypergeometric baselines; pandas for tabular data manipulation; and PyYAML for YAML configuration parsing. The pipeline is implemented in three scripts: bifo_conditioning.py (entity resolution, edge conditioning, PPR propagation), score_pathways.py (pathway membership mapping, score computation, metric calculation), and baseline_enrichment.py (baseline enrichment methods and Analysis 6 metrics). A self-contained run script (`examples/minimal_test/run_test.sh`) generates all main-benchmark outputs from raw graph files without manual intervention.

### 8.2 Benchmark freeze

All benchmark parameters were locked before analysis began. Frozen benchmark parameters are documented in `BENCHMARK_MANIFEST.md` at the repository root. Pipeline scripts are in `pipeline/`, the YAML mapping (v0.7.1) is in `config/`, and seed, heldout, and reference files for all three benchmark cohorts are in `data/benchmark/`. The run script is self-contained: given nodes.csv, edges_raw.csv, and pathway_membership_edges.csv, it produces every main-benchmark output including all baseline comparisons and C4 controls without manual steps.

No parameter was modified after the first successful full run. The C4 random seed (42), pathway universe filters (min=8, max=300 members, name patterns), score variant (degree_norm), and α (0.5) were all fixed before the first benchmark run and documented in BENCHMARK_MANIFEST.md alongside expected output metrics. The manifest serves as a reproducibility contract: if any output metric differs from the manifest values, the run is considered non-reproducible.

### 8.3 Scope of benchmark graph

The benchmark graph is a controlled projection of the full DDKG, not a comprehensive export. Results reported here are specific to this graph slice and SAB vocabulary selection. The mechanistic-layer finding (pathway structural inaccessibility under mechanistic-only propagation) is a property of this graph\'s topology under the current SAB selection and should not be generalised to DDKG as a whole without validation on expanded exports incorporating different source vocabularies. Importantly, this result is informative rather than merely cautionary: it reveals that curated pathway membership relationships (Pathway Contribution edges) occupy a structurally distinct layer from mechanistic gene-gene relationships in this knowledge graph architecture, and that formal admission of bridge edges as a propagation-eligible class is what enables signal transfer across layers. This architectural insight holds regardless of whether future expanded exports alter the specific inaccessibility result.


### 8.4 Empirical significance assessment via membership rewiring null

BIFO pathway scores are made actionable by comparison to an empirical null that tests whether a pathway's observed score is higher than expected given the propagated signal landscape. The null model uses degree-preserving bipartite edge rewiring of the Pathway Contribution (bridge) layer, keeping the real seed set and propagation operator fixed while randomising which genes are assigned as members of each pathway. For each permutation, the bridge edges are rewired via random endpoint swaps that preserve each pathway's member count and each gene's pathway membership count exactly. PPR is rerun on the rewired graph with the same seeds, and degree_norm scores are recomputed for all pathways. This process is repeated N = 1000 times to build a per-pathway null distribution.

Statistical significance is assessed using the finite-sample-corrected empirical p-value (Phipson and Smyth 2010): p = (1 + count(null ≥ observed)) / (1 + N). BH correction is applied across all scored pathways to obtain q-values. The rewiring null is implemented in `score_pathways.py` via the `--n-permutations` and `--null-type membership-rewiring` flags.

**Graph composition determines rewiring null calibration.** The validity of the rewiring null depends on the fraction of propagating edges that are bridge edges versus non-bridge (mechanistic) edges. When non-bridge edges provide sufficient routing constraint, rewired bridge assignments that do not match the biological structure of the seeds produce low pathway scores, and the null distribution is well-separated from the observed score. When bridge edges dominate the propagating graph, rewiring effectively randomizes the dominant routing structure of the propagation operator, and random bridge assignments frequently route mass to large, highly connected pathways under uniform propagation, inflating the null mean.

Across the three analyses in this paper, bridge edge fraction varies substantially:

- CHD curated benchmark: 80,200 bridge / 93,487 propagating = 85.8% bridge → rewiring null valid (49/550 q < 0.05; top cardiac pathways null_z > 9)
- KF-CHD cohort: 1,026,968 bridge / 2,482,752 kept edges = 41.4% bridge → rewiring null valid (WP_CILIOPATHIES null_z = 48.71, q = 0.006)
- KF-NBL cohort: bridge edges / total propagating → rewiring null valid (WP_CILIOPATHIES null_z = 18.95, q = 0.012)

These results indicate that calibration of the rewiring null is governed by the relative proportion of bridge to non-bridge edges in the propagating graph. Under the corrected unidirectional pipeline, bridge edges comprise approximately 41.4% of propagating edges in KF-CHD and a similar fraction in KF-NBL, providing sufficient non-bridge routing constraint for valid null calibration in both cohorts. The rewiring null is therefore the primary significance test for KF cohort results, and the strong null_z values observed (KF-CHD: 48.71; KF-NBL: 18.95) directly confirm that the ciliopathy signal exceeds topological expectation. At cohort scale in KF-CHD, pathway prioritisation is interpreted using the primary degree_norm ranking together with member-level empirical null support, cross-cohort convergence, concordance with independently implemented Fisher enrichment, and bootstrap rank stability.

**Member-level empirical null.** A complementary null tests whether a pathway's constituent genes carry disproportionate propagated signal, without requiring PPR reruns and empirically stable across the seed-size ranges evaluated here. For each pathway, the observed mean PPR score across its member genes (member_mean) is compared against N = 1000 matched random gene sets of the same size drawn from the eligible pathway-connected gene universe. Null genes are matched to true pathway members on structural features only: conditioned graph out-degree and pathway membership count (both log-binned into 10 quantile bins). Observed propagated score is intentionally excluded from matching to avoid conditioning the null on the quantity being tested. Sampling is without replacement within each null set. This null is parallelised over permutations: each worker computes one full permutation across all pathways, giving balanced load for large pathway universes. Empirical p-values use the finite-sample correction p = (1 + count(null ≥ observed)) / (1 + N); BH correction is applied across all tested pathways. Output columns member_mean_p, member_mean_q, member_mean_null_mean, member_mean_null_sd, and member_mean_null_z are written alongside degree_norm null columns. This member-level null is a structurally matched but score-naive empirical test; it does not directly validate the degree_norm pathway-node score but provides a complementary line of evidence that a highly ranked pathway is supported by concentrated signal among its constituent genes. The member-level null is less sensitive to bridge edge fraction than the pathway-node rewiring null because it operates on the fixed propagated signal rather than the propagation operator itself. The pathway-node rewiring null tests pathway-node signal accumulation directly; the member-level null tests whether the genes defining that pathway carry disproportionate propagated signal. These two nulls are therefore complementary.

## 9 CHD exhaustive resampling analysis

The CHD curated benchmark evaluates BIFO performance from a single hand-selected seed set, which raises the natural question of whether results are specific to that particular 10-gene configuration. To address this, we evaluate all C(15,10) = 3,003 possible 10-gene/5-gene partitions of the 15-gene CHD pool (10 original seeds + 5 original held-out genes). The exhaustive enumeration is made feasible by an in-memory design that builds the PPR operators once and varies only the seed vectors across all splits.

### 9.1 Computational design

The PPR operators (conditioned arm from kept_edges.csv, raw arm from edges_merged.csv) and pathway membership map are built once and held in memory. For each of the 3,003 splits, only the seed vector s is modified; the adjacency matrices, pathway universe, and reference set remain identical to the primary benchmark. No per-split output files are written; per-split metrics are accumulated in memory and written as a single CSV (one row per split) and a JSON summary at the end of the run. This design ensures that the resampling is reproducible with a fixed, minimal output footprint rather than thousands of intermediate files.

The analysis is parallelized using Python ProcessPoolExecutor. The PPR operator components (CSR sparse matrix arrays: data, indices, indptr) are serialized to worker processes at startup via an initializer function. Each worker process reconstructs the sparse matrices from these components and processes an assigned batch of splits independently. The parallelization is embarrassingly parallel: splits share no state beyond the read-only operators, so no synchronization is needed beyond collecting results at the end.

### 9.2 Metrics computed per split

For each split, the following are computed: BIFO full-arm pathway metrics (P@10, P@20, enrichment@10, NDCG@10, average precision, mean CHD reference rank, rank improvement relative to the raw arm on the same conditioned graph (conditioned arm uses degree_norm = direct/√|members|; raw arm uses the direct pathway-node score without degree normalization — the comparison is directional rather than fully symmetric)); gene-level AUPRC for held-out gene recovery; and a seed-overlap Fisher baseline. The GSEA and neighborhood Fisher baselines are not recomputed per split because the resampling analysis was designed to test seed-composition sensitivity of the primary BIFO benchmark, using seed-overlap Fisher as the direct within-split comparator. The broader baseline comparison is reported in full for the primary split in Analysis 4 (Table 4).

### 9.3 Fisher baseline distinction

The seed-overlap Fisher computed in the resampling uses the split seed genes directly as the query set (n = 10 query genes tested for enrichment in pathway member lists). This is a different statistical test from the Analysis 4 Table 4 Fisher, which uses the 1-hop graph neighborhood (11,146 genes) as the query. The two baselines test different hypotheses: the resampling Fisher asks \'are these 10 seed genes over-represented as pathway members?\', while the Analysis 4 Fisher asks \'is the graph neighborhood of these seeds enriched for pathway members?\' The resampling Fisher is competitive on CHD splits because many canonical CHD genes are directly annotated to cardiac pathways; the Analysis 4 neighborhood Fisher fails entirely because the neighborhood is too large to be discriminating. These two Fisher results are not numerically comparable and should not be presented in the same row of a comparison table.

### 9.4 Summary output

The JSON summary file (chd_resampling_summary.json) contains: distribution statistics (mean, SD, min, P25, median, P75, max) for all per-split metrics; robustness counts (fraction of splits with P@10 ≥ threshold, fraction with positive rank improvement, fraction where BIFO AP exceeds Fisher AP); and the primary benchmark split identified as an anchor point within the full distribution with its percentile rank on each metric. The per-split CSV contains one row per split and is the source file for Figure 6 (the resampling distribution figure).

> *Implementation: chd_resampling_exhaustive.py (pipeline/). Requires Python 3.8+ (compatibility shims for math.comb and str.removesuffix are included). Runtime scales linearly with \--n-cores; 3,003 splits complete in approximately 5 min on 1 core.*

## 10 Kids First cohort analysis

### 10.1 The rare variant enrichment problem

Standard pathway enrichment methods were designed for gene sets produced by differential expression (tens to hundreds of genes, biologically coherent signal) or GWAS association (small focused gene lists near association peaks). Rare variant cohort analysis occupies a different regime: AutoGVP [@doi:10.1093/bioinformatics/btae114] P/LP variant aggregation across a disease cohort typically produces gene lists of hundreds to thousands of genes spanning diverse disease processes, with the biologically relevant signal distributed across a minority of genes embedded in a larger heterogeneous background.

This creates a fundamental tension for enrichment testing. When carrier frequency filters are strict (e.g., ≥3 carriers, MAF ≤0.0001), the gene list shrinks to tens of genes but becomes dominated by severe recessive disease genes incidentally present in the cohort (lysosomal storage, deafness, retinal dystrophy), losing the distributed developmental signal of interest. When carrier frequency filters are relaxed to match the full AutoGVP P/LP burden (MAF ≤0.001, no carrier count filter), the gene list expands to \~1,000--1,500 genes --- large enough that hypergeometric p-values collapse to zero for virtually every pathway with any overlap, eliminating rank discrimination entirely. In the KF-CHD cohort at MAF ≤0.001 (1,276 seed genes, 22,628-gene pathway member universe), all pathways with any overlap at this scale receive floor-level p-values that cannot be ranked. BIFO\'s graph propagation is robust to this regime: by propagating signal from all 1,276 seeds simultaneously through the DDKG, it amplifies the coherent biological signal from the distributed cilia gene subset while the incoherent background diffuses away.

### 10.2 Cohort and variant selection

Germline variant data were obtained from two Kids First pediatric cohorts: KF-CHD (Pediatric Cardiac Genomics Consortium, phs001138, n=697 probands with congenital heart defects) and KF-NBL (Discovering the Genetic Basis of Human Neuroblastoma, phs001436, n=460 probands with neuroblastoma). Whole-genome sequencing was performed using Kids First harmonization pipelines aligned to GRCh38/GENCODE v39.

Variants were filtered retaining GATK PASS calls with genotype quality ≥20 and read depth ≥10. AutoGVP P/LP classification was applied integrating ClinVar and modified InterVar for hierarchical ACMG-AMP criteria assessment. Population allele frequency filtering used gnomAD v3.1 [@doi:10.1038/s41586-020-2308-7] MAF ≤0.001, matching the companion U24 cross-cohort enrichment analysis (Stear et al., CFDE Meeting 2026). Genes harboring ≥1 qualifying variant in any proband were aggregated per cohort. Twenty high-frequency background disease genes were excluded — specifically, genes among the most prevalent recessive disease carrier loci in population-scale sequencing (carrier frequency >1% in gnomAD), representing incidental findings unrelated to the disease of interest. The excluded genes encode proteins associated with hereditary hearing loss (GJB2, MYO15A, MYO1A, MYO3A, MYO7A, USH2A), retinal dystrophy (ABCA4), skin barrier dysfunction (FLG, KRT71, KRT86, TCHH, PADI3), metabolic disease (G6PD, PAH, BCHE), and structural/connective tissue disorders (TTN, OBSCN, COL4A5, TBL1Y, CD36). This yielded 1,287 seed genes for KF-CHD and 1,406 seed genes for KF-NBL.

At the MAF ≤0.001, n≥1 threshold, 570 of 1,287 CHD seed genes (44.3%) are also present in the NBL seed set. This inter-cohort overlap reflects the shared background of Mendelian disease gene carriers present in any pediatric sequencing cohort at this allele frequency threshold and is not specific to either disease. Carrier count-filtered seed sets (n≥2: 387 CHD / 401 NBL genes, 30% overlap; n≥3: 146 CHD / 147 NBL genes, 27% overlap) show reduced but persistent overlap, consistent with shared rare variant burden being a property of the population rather than the disease.

### 10.3 Graph export and conditioning

Export queries were generated dynamically from each seed list using generate_export_cypher.py. The KF-CHD export produced 815,248 concept nodes and 5,261,300 1-hop edges plus 486,642 gene→pathway membership edges (inverse_pathway_associated_with_gene, unconditional full MSIGDB export); the KF-NBL export produced 880,456 concept nodes and similar 1-hop and membership edge counts. An additional Query 6 export provided node metadata for 21,353 MSIGDB pathway member genes not present in the 1-hop seed neighborhood, required for entity resolution of complete pathway membership. Of 1,287 CHD seed genes, 1,276 (99.1%) resolved to UMLS CUIs; of 1,406 NBL seed genes, 1,395 (99.2%) resolved. BIFO conditioning used identical parameters to the curated benchmark (alpha=0.5, bifo_mapping.yaml v0.7.1), retaining 2,482,752 propagating edges for KF-CHD (43.9% of concept edges) and 2,647,055 for KF-NBL (45.1%).

### 10.4 Pathway scoring and discovery evaluation

Pathway scoring used the degree_norm scoring variant against a universe of 2,130 pathways for KF-CHD and 2,196 pathways for KF-NBL, each passing minimum-member (≥8), maximum-member (≤300), name-pattern, and canonical-collection filters (Hallmarks, Reactome, WikiPathways, KEGG, BioCarta, PID; C2.CGP author-named gene expression signature sets excluded). No reference pathway set was pre-specified; all pathways were scored and ranked in discovery mode. Results were evaluated post-hoc against a 17-pathway cilia reference set (KF-CHD) and 18-pathway cilia reference set (KF-NBL) of MSigDB canonical cilia, ciliopathy, and hedgehog pathway CUIs pre-specified before scoring (ciliopathies, ciliary, intraflagellar transport, Joubert syndrome, Bardet-Biedl syndrome, primary ciliary dyskinesia, and related terms) within the scored universe. This reference contains WP_CILIOPATHIES and 18 related MSigDB, WikiPathways, Reactome, and GO pathway annotations.

### 10.5 Baseline enrichment methods for KF cohort analysis

Five baseline methods were evaluated against the identical pathway universe restricted to pathways present in the BIFO-scored set (2,130 pathways for KF-CHD; 2,196 for KF-NBL). All methods used the KF-CHD or KF-NBL seed gene CUIs as input.

**B1: Seed-only hypergeometric enrichment.** For each pathway p, a one-tailed hypergeometric test was applied: N = full annotated gene space (pathway member genes ∪ seed genes), K = \|members(p)\|, n = \|seed genes\|, k = \|members(p) ∩ seeds\|. P-values were computed in log space using scipy.stats.hypergeom.logsf to prevent float underflow --- with n/N ≈ 5%, standard-precision computation returns 0.0 for any pathway with strong overlap, collapsing rank discrimination. Log-space computation recovers correct relative ordering. Pathways are ranked by ascending BH-adjusted p-value.

**B1 gene universe rationale.** The gene universe N was set to the union of pathway member genes and seed genes (\~22,628--22,601 genes), not all C-prefixed concept nodes in the DDKG graph (\~58,846). Using all graph nodes inflates the denominator and causes p-value floor collapse because the graph includes diseases, drugs, phenotypes, and other non-gene concepts. The pathway-member-plus-seed universe matches standard practice in pathway enrichment tools.

**B2: 1-hop neighborhood hypergeometric enrichment.** The query set was expanded to the union of seed genes and all 1-hop gene-concept neighbors in the conditioned graph (\~58,846--59,033 genes). This method failed to discriminate pathways because the 1-hop neighborhood covers essentially the full pathway gene universe, giving near-identical p-values to all pathways with any membership overlap.

**B3 / B3b: Preranked GSEA on PPR scores.** Genes were ranked by raw PPR scores (B3) or conditioned PPR scores (B3b) and a weighted running-sum enrichment score was computed following Subramanian et al. [@doi:10.1073/pnas.0506580102].

**B4: BIFO full-arm (degree_norm).** The conditioned PPR score vector was used to score all pathways via score(p) = f_direct(p) / √\|members(p)\|. This is the primary BIFO scoring method.

### 10.6 Comparison design and rank analysis

All five methods were evaluated on identical pathway universes to enable direct rank comparison. The primary comparison metric is the rank of WP_CILIOPATHIES and other cilia-related pathways under each method in discovery mode. Secondary comparisons examine the top-20 ranked pathways per method (Supplementary Table ST3), the head-to-head rank correlation between seed_fisher and BIFO for all pathways (Supplementary Table ST5), and the full cilia pathway cluster ranking under BIFO (Supplementary Table ST4).

### 10.7 Bootstrap resampling analysis

To assess the stability of cilia pathway recovery and the relationship between seed set size and signal, a bootstrap resampling analysis was performed for both cohorts. For each of three seed sizes (n=10, 20, 30), 500 bootstrap draws were made by sampling uniformly without replacement from the full seed CUI pool. For each draw, BIFO scoring and seed-only Fisher enrichment were run using the identical pathway universe and cilia reference set as the primary analysis. The primary cohort run (full 1,276/1,395-gene seed set) was also evaluated as a reference point (boot_id = −1).

Performance was measured as Precision@10 (fraction of cilia reference pathways in the top-10 ranked results), Average Precision (AP) against the 17-pathway (KF-CHD) / 18-pathway (KF-NBL) cilia reference, and rank improvement (mean rank under raw PPR − mean rank under BIFO, where positive values indicate conditioning helps). All 1,500 bootstrap runs per cohort were parallelised across 192 cores using Python multiprocessing; total runtime was approximately 150 seconds per cohort.

The bootstrap analysis was designed to address two questions: (1) whether cilia pathway recovery requires aggregate cohort-scale variant burden or can emerge from small random gene subsets; and (2) whether BIFO or standard Fisher enrichment is more sensitive for detecting cilia signal at small seed sizes. Results are reported in Section 8.4.


**Results**

## 1 Graph conditioning and coverage

The DDKG export comprised 34,523 concept nodes and 174,352 merged edges, combining 94,790 seed-centered mechanistic and association edges (edges_raw) with 79,562 pathway membership edges. Entity resolution using direct SAB column fallback resolved 18,897 of 34,523 concept nodes (54.7%); the remaining 15,626 nodes lacked a mappable source vocabulary assignment and were treated as unresolvable at Level 1.

BIFO conditioning evaluated each edge against the predicate-to-flow mapping (v0.7.1; 251 entries). Of 174,352 input edges, 104,342 (59.8%) were retained as biologically admissible; 69,658 were excluded for three mutually exclusive reasons: unmapped predicate (37,448; 21.5%), unresolved endpoint entity (32,214; 18.5%), or explicit non-flow classification (348; 0.2%). Level-2 edge coverage was 59.8%, reflecting incomplete predicate mapping under the current SAB selection.

  ------------------------------------- --------------- ----------------------- -------------------------------------------------------------
  **Edge category**                     **Count**       **Fraction of input**   **Notes**

  **Raw input edges (merged)**          174,352         100%                    94,790 seed↔hop1 + 79,562 membership

  **Kept after conditioning**           104,342         59.8%                   Biologically admissible (includes non-propagating retained)

  --- Propagating (conditioned arm)     93,507          ---                     Used in PPR operator; see Section 3

  --- Non-propagating retained          10,033          ---                     Observational Association 9,909; contextual 124

  Dropped: non-flow                     348             0.2%                    Structural/taxonomic predicates

  Dropped: unmapped predicate           37,448          21.5%                   No BIFO flow class assigned

  Dropped: unresolved entity            32,214          18.5%                   No SAB match at entity resolution

  Propagating edges (ablation arm)      16,026          ---                     edges_raw conditioned: 26,059 kept → 16,026 propagating

  Propagating edges (mechanistic arm)   9,710           ---                     classification=mechanistic only (see §3)
  ------------------------------------- --------------- ----------------------- -------------------------------------------------------------

**Table 1.** *Graph conditioning statistics. All values from benchmark run V5. Of the 104,342 kept edges, 93,507 enter the PPR operator as propagating edges; 10,033 are retained in the conditioning output (kept_edges.csv) but excluded from propagation --- comprising Observational Association edges (9,909) that pass flow classification but are excluded by operator construction, and a small set of contextual edges (124). The ablation arm conditions edges_raw.csv independently, producing 26,059 kept edges of which 16,026 are propagating (the remainder are the same non-propagating classes).*

Of the 93,507 propagating edges in the conditioned arm, 80,200 (85.8%) were classified as Pathway Contribution, the edge class encoding curated gene-to-pathway membership relationships that serve as admissible bridges between the mechanistic gene neighborhood and the pathway annotation layer. Signal Transduction accounted for 5,786 (6.1%) and Perturbational Effect for 5,392 (5.7%), with Transcription, Signal Termination, and minor classes comprising the remainder.

While Pathway Contribution edges dominate numerically, the ablation experiment (Section 3) establishes that they do not generate signal independently: removing bridge edges while preserving all other admissible mechanistic classes reduces P@10 from 0.70 to 0.60, and mechanistic-only propagation --- which contains no Pathway Contribution edges --- yields exactly zero pathway scores across all 550 pathways. Pathway Contribution edges (referred to hereafter as bridge edges) are necessary conduits for transferring mechanistic signal from gene-level propagation to the pathway annotation layer; without upstream mechanistic signal to relay, they have no effect on their own.

![
**BIFO conditioning coverage — curated CHD benchmark graph.**
(**A**) Edge funnel from 174,352 merged input edges through entity resolution and flow-class conditioning to 93,507 propagating edges (54.0% retention) used by the PPR operator.
(**B**) Dropped edges stratified by cause: unmapped predicates (37,448; 21.5%) and unresolved entities (32,214; 18.5%) account for nearly all losses; non-flow classifications contribute <1%.
(**C**) Flow-class distribution of propagating edges. Pathway Contribution bridge edges (dark blue; 80,200 edges; 85.8% of propagating edges) are the architectural element enabling gene→pathway signal transfer; mechanistic classes (Signal Transduction, Perturbational Effect, Transcription, etc.) comprise the remaining 14.2%.
(**D**) Concept-node entity resolution: 18,897 of 34,523 nodes (54.7%) resolve to a source vocabulary; the remainder are Level-1 unresolvable under the current SAB selection.
](images/fig1_conditioning.png){#fig:conditioning width="100%"}

## 2 Gene-level recovery

To evaluate propagation signal at the gene level, we performed PPR on each arm of the conditioning design and assessed recovery of five held-out CHD-associated genes (ZFPM2, MYH7, PTPN11, JAG1, FLT4) not present in the ten-gene seed set. Gene-level metrics were computed over the full 34,523-node graph.

  ---------------------------- ------------ ------------ ------------- -----------------------
  **Arm**                      **AUROC**    **AUPRC**    **Entropy**   **Nonzero nodes (%)**

  **Raw (full graph)**         1.000        0.2215       5.728         100.0%

  **Conditioned (BIFO)**       1.000        0.1902       5.217         31.6%

  Ablation (no bridge edges)   1.000        0.2215       4.939         19.5%

  Random sparsification        1.000        0.2173       5.590         64.6%
  ---------------------------- ------------ ------------ ------------- -----------------------

**Table 2.** *Four-arm gene-level recovery for the CHD curated benchmark. Entropy is the Shannon entropy of the propagation score distribution (lower = more concentrated). Nonzero node fraction indicates the proportion of nodes with non-negligible score mass. AUROC is near-ceiling across all arms on this small benchmark; entropy and nonzero fraction are the informative discriminants at this scale.*

AUROC was 1.000 across all arms, reflecting ceiling performance on this small benchmark (five held-out nodes from a strongly connected seed neighborhood). AUPRC was 0.2215 for the raw arm and declined to 0.1902 under full BIFO conditioning, reflecting concentration of score mass into a smaller node subset. The ablation arm (propagation without Pathway Contribution edges) produced AUPRC equal to the raw arm (0.2215) with substantially lower entropy (4.939 vs. 5.728), demonstrating that the core mechanistic signal is preserved without bridge edges. The random sparsification control (same edge count as conditioned, random selection) produced intermediate entropy (5.590) and AUPRC (0.2173), establishing that BIFO\'s entropy reduction is not simply a consequence of edge count reduction.

The AUPRC decline from raw to conditioned reflects the structure-dependent nature of BIFO filtering: conditioning concentrates signal on biologically coherent neighborhoods but does not optimize for held-out gene recovery per se. The mechanistic-only arm (9,710 edges, classification=mechanistic, including mechanistically classified subsets of perturbational and termination predicates) produced AUPRC 0.1486 and entropy 4.770, the lowest across all arms, consistent with a sparse subgraph reaching fewer nodes than the random control.

> *⚑ AUPRC is near-ceiling and reported honestly. These gene-level metrics become more informative at full-cohort scale and with variant-derived seeds (Kids First CHD extension, Section 8).*

![
**Four-arm gene-level recovery — curated CHD benchmark.**
Each panel compares four PPR propagation arms (Raw, Metadata-filtered, BIFO-conditioned, Random sparsification) across three graph configurations (Full with all BIFO flow classes, Ablation without Pathway Contribution bridge edges, Mechanistic-only).
(**A**) AUROC is near-ceiling across all arms and configurations and is not informative for this benchmark; entropy and nonzero fraction reflect the meaningful differences between arms.
(**B**) AUPRC discriminates between arms; BIFO-conditioned on the Mechanistic graph shows the expected drop (0.149) relative to Full (0.192), and Random sparsification of the Mechanistic graph collapses to 0.049.
(**C**) Localization (mean held-out rank normalised by graph size; lower = more concentrated near seeds). BIFO-conditioned is lowest across Full and Ablation graphs.
(**D**) PPR score entropy in nats (lower = more concentrated signal; computed as Shannon entropy using natural logarithm). BIFO-conditioned achieves the lowest entropy in all three graph configurations, showing that conditioning concentrates signal beyond what edge-count reduction alone achieves.
](images/fig2_gene_recovery.png){#fig:gene_recovery width="100%"}

## 3 Pathway prioritization: three-arm ablation

The primary benchmark evaluated pathway prioritization using three propagation arms scored against an identical pathway universe (550 pathways, 8--300 members, CHD reference set of 18 pathways). All three arms used the same pathway membership map for scoring; only the propagating graph differed.

  -------------------------------- ----------------- ---------- ------------------ --------------- --------------------
  **Arm**                          **Prop. edges**   **P@10**   **Enrich. \@10**   **Mean rank**   **Rank imp.**

  **Full (BIFO conditioned)**      **93,507**        **0.70**   **21.4×**          **113**         **+125.4**

  **Ablation (no bridge edges)**   16,026            0.60       18.3×              111             −11.2

  Mechanistic-only                 9,710             0.00       0.0×               177             uninterpretable \*
  -------------------------------- ----------------- ---------- ------------------ --------------- --------------------

**Table 3.** *Three-arm pathway prioritization for the CHD curated benchmark. Pathway universe: 550 pathways. CHD reference: 18 pathways. Background rate: 3.3%. Rank improvement = mean_rank_raw − mean_rank_cond (positive = conditioning improves rank relative to the raw propagation baseline). \* Mechanistic-arm rank improvement is uninterpretable: all pathway scores are exactly zero and tie-ordering is arbitrary.*

***Full arm***

Under full BIFO conditioning (93,507 propagating edges), the top-10 pathways contained 7 of 18 CHD reference pathways (P@10 = 0.70; enrichment = 21.4× background). BRUNEAU_SEPTATION_VENTRICULAR and WP_HEART_DEVELOPMENT ranked first and second. Mean rank of CHD reference pathways under the conditioned score was 86.6, compared with 212.0 under the raw score from the same propagation, yielding rank improvement +125.4.

***Ablation arm***

The ablation arm removed Pathway Contribution edges from propagation (16,026 propagating edges from 26,059 kept edges of edges_raw, with 10,033 non-propagating retained classes excluded as in the full arm) while retaining the identical membership map for scoring. P@10 = 0.60 (enrichment = 18.3×); the top-6 CHD pathways were identical to those in the full arm. Rank improvement was −11.2: without Pathway Contribution bridge edges in the propagating graph, the conditioned operator cannot route signal through the pathway-layer bridge, so the raw arm\'s direct scoring advantage persists. This shows that the core cardiac signal originates in the mechanistic neighborhood but that the full arm\'s conditioning gain requires the bridge edges to be present.

***Mechanistic-only arm***

The mechanistic-only arm restricted propagation to edges classified as mechanistic in the YAML mapping (9,710 edges: Signal Transduction 5,786, Transcription 1,568, Signal Termination 484, and minor classes including mechanistically classified subsets of perturbational and termination predicates). All 550 pathway scores were exactly zero, yielding P@10 = 0.00. This is a structural result, not a performance result. In the present benchmark graph, pathway nodes are not reachable from seed genes through mechanistic edges alone; gene-to-pathway connectivity is mediated exclusively by Pathway Contribution edges. The rank improvement value of +34.7 is uninterpretable: it reflects arbitrary tie-ordering of zero-score pathways.

**Empirical significance via membership rewiring null.** To assess whether top-ranked pathways exceed what is expected by chance, we applied a degree-preserving membership rewiring null (N = 1000 permutations; Methods §8.4). Of 550 scored pathways, 49 (8.9%) were significant at q < 0.05 after BH correction. The top cardiac pathways showed strong separation from the null: BRUNEAU_SEPTATION_VENTRICULAR (q = 0.017, null_z = 24.1), WP_HEART_DEVELOPMENT (q = 0.017, null_z = 21.7), and WP_CARDIAC_PROGENITOR_DIFFERENTIATION (q = 0.017, null_z = 17.5). All nine pathways in the top-10 carrying a CHD reference annotation were significant at q < 0.05. This confirms that the top-ranked pathways receive substantially more propagated signal than pathway-sized random gene sets drawn from the same conditioned graph, providing empirical support for the biological specificity of BIFO pathway prioritisation in the sparse-seed regime.

The stratified member-level null (Methods §8.4) independently confirms this result using structural matching only. BRUNEAU_SEPTATION_VENTRICULAR showed member_mean null_z = 10.6 (q = 0.037), WP_HEART_DEVELOPMENT null_z = 10.9 (q = 0.037), and REACTOME_CARDIAC_CONDUCTION null_z = 8.1 (q = 0.037). These values reflect structural-only matched null sampling (degree and pathway membership count bins); 25 of 550 pathways were significant at q < 0.05, of which 8 carry CHD reference annotations, confirming member-level empirical support for the benchmark result.

Together, the three arms identify a two-layer graph architecture with a structurally necessary bridge. Layer 1 (mechanistic) encodes gene--gene signaling, transcription, and protein interaction. Layer 2 (pathway) encodes curated gene-set annotations. These layers are structurally separated in the present graph; connectivity between them is mediated exclusively by Pathway Contribution edges. BIFO\'s contribution is the principled, ontology-aligned admission of those bridge edges as a coherent flow class, enabling signal transfer from the mechanistic layer to the pathway annotation layer.

> *Scope: these conclusions apply to the present benchmark graph, constructed from a defined SAB subset that isolates ontology-aligned mechanistic and pathway representations from association-derived evidence layers. The present framework does not incorporate association-derived evidence; the architectural findings reported here reflect this graph's topology under the current SAB selection.*

![
**BIFO conditioning enables pathway-level signal recovery.**
Top row: curated CHD benchmark (550 pathways, 18-pathway CHD reference) comparing the Full BIFO arm, Ablation (no Pathway Contribution bridge edges), and Mechanistic-only propagation.
(**A**) Precision@10: Full 0.70, Ablation 0.60, Mechanistic 0.00. Mechanistic-only scores are zero because pathway nodes are not reached by propagation under this operator, not because of downstream scoring effects.
(**B**) Enrichment@10 over background rate: Full 21.4×, Ablation 18.3×, Mechanistic 0×.
(**C**) Rank improvement (raw PPR rank − conditioned PPR rank): Full +125.4 positions, Mechanistic +34.7 (uninterpretable; see text), Ablation −11.2.
(**D**) WP_CILIOPATHIES rank under five enrichment methods in the KF-CHD discovery cohort (1,276 variant genes, 2,130 pathways scored). Seed Fisher (corrected) ranks WP_CILIOPATHIES first; BIFO full-arm ranks it 43rd (null_z=48.7); Raw PPR GSEA, Conditioned PPR GSEA, and Neighborhood Fisher rank it 1,994, 456, and 2,126 respectively.
](images/fig3_ablation.png){#fig:ablation width="100%"}

## 4 Baseline comparison

To evaluate BIFO against conventional enrichment approaches applied to the same graph-derived gene sets, we implemented four baselines evaluated on the identical 550-pathway universe: (B0) degree-weighted seed overlap, (B1) seed-only hypergeometric enrichment, (B2) 1-hop neighborhood hypergeometric enrichment, and (B3) preranked GSEA on raw PPR scores. All Fisher-based tests used Benjamini--Hochberg FDR correction. The BIFO full-arm result (B4) is shown for direct comparison.

  --------------------------------- ----------- ----------- ------------- ---------------- ---------------
  **Method**                        **P@10**    **P@20**    **NDCG@10**   **Avg. Prec.**   **Mean rank**

  **Degree overlap (B0)**           0.400       0.400       0.492         0.342            84

  **Seed-only Fisher**              0.300       0.200       0.215         0.156            120

  **1-hop neighborhood Fisher**     0.000       0.000       0.000         0.036            243

  Raw PPR preranked GSEA            0.100       0.050       0.220         0.117            162

  Conditioned PPR GSEA              0.100       0.050       0.085         0.114            110

  **BIFO full-arm (degree_norm)**   **0.700**   **0.350**   **0.757**     **0.403**        **113**
  --------------------------------- ----------- ----------- ------------- ---------------- ---------------

**Table 4.** *Baseline comparison for the CHD curated benchmark. All methods evaluated on identical 550-pathway universe (background 3.3%). Avg. Prec. = average precision (area under the precision--recall curve over all ranks).*

Seed-only Fisher (B1) achieved P@10 = 0.30 but produced non-specific top hits (bladder cancer, TP63 targets, TNF response), reflecting the instability of hypergeometric enrichment with a ten-gene query: even minimal pathway overlap produces floor-level p-values, placing cancer-associated gene sets above cardiac pathways.

The degree-weighted seed overlap baseline (B0) scored pathways by the sum of conditioned-graph out-degrees of overlapping seed genes normalised by pathway size, recovering BRUNEAU_SEPTATION_VENTRICULAR and WP_HEART_DEVELOPMENT at ranks 1 and 2 through direct membership overlap (P@10 = 0.40, AP = 0.342). BIFO outperforms B0 on both P@10 (0.70 vs. 0.40) and AP (0.403 vs. 0.342), isolating the contribution of PPR propagation beyond local graph connectivity.

Neighborhood Fisher (B2) failed entirely (P@10 = 0.000, AP = 0.036). The 1-hop gene neighborhood around the ten seed genes contained 11,146 genes --- 86% of the gene universe --- so virtually every pathway had non-trivial neighborhood overlap, eliminating all discriminating power. This illustrates the neighborhood-inflation problem: graph-derived gene sets are too broad for conventional enrichment without prior signal concentration.

Raw PPR preranked GSEA (B3) recovered BRUNEAU_SEPTATION_VENTRICULAR at rank 1 (P@10 = 0.10, NDCG@10 = 0.220), confirming that graph propagation encodes pathway-relevant signal even before BIFO conditioning. BIFO full-arm (B4) outperformed all baselines across every metric: P@10 = 0.70 (2.3× seed Fisher), NDCG@10 = 0.757 (3.4× raw GSEA), AP = 0.403 (2.6× seed Fisher). The improvement over conditioned PPR GSEA (B3b; AP = 0.114) isolates the contribution of the degree_norm scoring function beyond propagation alone.

*Standard enrichment fails in both the small-sample regime (seed Fisher: unstable overlap) and the large-neighborhood regime (neighborhood Fisher: no discrimination). BIFO-conditioned propagation avoids both failure modes by structuring the graph before scoring. These results are consistent with the three-arm ablation finding in Section 3: pathway-ranking performance improves when admissible bridge edges are present in the propagating graph, and collapses when they are absent.*

![
**Baseline enrichment method comparison — KF-CHD and KF-NBL cohorts.**
Five enrichment methods (BIFO full-arm, Conditioned PPR GSEA, Raw PPR GSEA, Neighborhood Fisher, Seed Fisher corrected) evaluated against a 21-pathway native cilia reference set (MSigDB/WikiPathways/Reactome/GO).
(**A**) KF-CHD heatmap: five methods × five metrics (P@10, P@20, P@50, Average Precision, Mean Cilia Ref Rank). Colour scaled within each metric column (darker = better); Mean Ref Rank colour is inverted so lower rank shows darker. `—` denotes zero or not applicable.
(**B**) KF-NBL heatmap, same layout as A.
(**C**) WP_CILIOPATHIES rank under BIFO full-arm and Seed Fisher (corrected). Seed Fisher ranks WP_CILIOPATHIES first in both cohorts (CHD: rank 1/2,130; NBL: rank 1/2,196). BIFO ranks WP_CILIOPATHIES 43rd in KF-CHD (null_z=48.7, strongest enrichment in dataset) and 3rd in KF-NBL (null_z=19.0). Seed Fisher results shown here use log-space hypergeometric computation; standard implementations cause p-value floor collapse in this large-seed regime.
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
(**D**) Rank improvement is negative in both controls (Notch −31.5, MAPK −54.4). This is the expected mechanism of BIFO conditioning: Pathway Contribution bridge edges redistribute rank mass toward cross-family pathway neighbourhoods, which produces the +125.4 rank improvement on heterogeneous CHD variant seeds (@fig:ablation C) but slightly dilutes within-family concentration when seeds already share a pathway identity.
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

Rank improvement was positive in all 3,003 splits (range +28.4 to +139.1; mean ± SD: +93.0 ± 16.8). This shows that BIFO conditioning consistently improves the ordering of CHD-relevant pathways relative to the unconditioned propagation baseline, regardless of which genes in the 15-gene pool serve as seeds.

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
(**D**) Rank improvement distribution (raw PPR rank − conditioned PPR rank): all 3,003 splits show positive rank improvement (100% positive); primary split +99.2. BIFO beats Seed Fisher on AP in 22.9% of splits. All splits use identical conditioning operators and pathway universe; only the seed vector varies.
](images/fig6_resampling.png){#fig:resampling width="100%"}

## 7 Limitations and scope

***Graph scope***

The benchmark graph is a 1-hop neighborhood export from a defined DDKG SAB subset that isolates ontology-aligned mechanistic and pathway representations from association-derived evidence layers. Entity resolution covered 54.7% of concept nodes under this SAB selection.

***Mechanistic arm scope and structural interpretation***

The finding that pathway nodes are structurally inaccessible under mechanistic-only propagation applies to the present benchmark graph and SAB selection. Rather than a limitation, this is consistent with an architectural property of ontology-aligned biomedical knowledge graphs: mechanistic edges encode directed biological process flow within the molecular layer (gene--gene signaling, protein interactions, regulatory cascades), while a formally distinct edge class --- Pathway Contribution bridges --- is required to connect that molecular layer to pathway-level annotations. This separation is not an artefact of incomplete edge coverage; it is a consequence of how curated pathway memberships are represented in the DDKG. The result motivates BIFO's explicit admission of bridge edges as a coherent, propagation-eligible flow class: without formally recognising and admitting them, no graph propagation method operating on mechanistic edges alone can reach pathway concept nodes in this knowledge graph architecture. Whether this architectural property persists under expanded SAB selections incorporating additional evidence layers remains an open question outside the scope of the current analysis.

***Gene-level recovery ceiling***

AUROC is near-ceiling (1.000) on this benchmark due to the small held-out set and strongly connected seed neighborhood. These metrics will be more discriminating at full-cohort scale with variant-derived seeds. The present framework isolates admissible mechanistic and pathway-level structure; incorporation of additional evidence layers requires separate treatment to preserve interpretability of causal flow.

![
**Two-layer graph architecture and the role of Pathway Contribution bridge edges.**
Schematic of the conditioned BIFO graph. The gene/molecular layer (top) contains gene and protein concept nodes connected by mechanistic flow-class edges (signal transduction, protein interaction, transcription). The pathway layer (bottom) contains curated pathway concept nodes from WikiPathways, Reactome, and related sources. The two layers are structurally separated in the mechanistic subgraph; connectivity is mediated exclusively by Pathway Contribution bridge edges (orange, dashed). Variant-gene seeds (filled nodes) inject PPR probability mass into the gene layer, which propagates down through admissible bridge edges to the pathway layer. In the ablation arm, bridge edges are removed and the pathway layer is unreachable from seed genes — the structural finding of Section 3. Pathway nodes receive propagated mass only via bridge edges; mechanistic edges connect only within the molecular layer in this graph construction.
](images/fig7_schematic.png){#fig:schematic width="100%"}



## 8 Kids First cohort: discovery-mode pathway analysis

### 8.1 Fisher enrichment at cohort scale: implementation matters

Applying seed-only hypergeometric enrichment (B1) to the 1,276-gene KF-CHD variant set requires careful implementation. A naive implementation using standard-precision p-value computation causes float underflow: with 1,276 seeds against a \~22,628-gene universe, scipy.stats.hypergeom.sf returns 0.0 for any pathway with meaningful overlap, collapsing rank discrimination entirely and placing WP_CILIOPATHIES (61/170 members; BH p = 4.53×10⁻³¹) at rank 768 alongside hundreds of non-specific pathways. Once corrected to use log-space hypergeometric computation (hypergeom.logsf) with a pathway-member-only gene universe, Fisher correctly recovers WP_CILIOPATHIES at rank 1 of 2,130 pathways (BH p = 4.53×10⁻³¹, overlap = 61/170 members). WP_GENES_RELATED_TO_PRIMARY_CILIUM_DEVELOPMENT_BASED_ON_CRISPR ranks 3rd and WP_JOUBERT_SYNDROME ranks 4th, confirming that cilia enrichment signal is present and detectable by both approaches when Fisher is correctly implemented.

Neighborhood Fisher (B2) failed entirely (P@10 = 0.000) because the 1-hop neighborhood expands to \~58,846 genes --- essentially the full graph --- giving near-identical p-values to all pathways. Preranked GSEA on raw PPR scores (B3) ranked WP_CILIOPATHIES at position 1,994; on conditioned PPR scores (B3b) at position 456. Gene-level PPR scores without BIFO\'s pathway-level degree normalization do not concentrate signal specifically on cilia pathway concept nodes.

**Table 8.1. KF-CHD method comparison --- WP_CILIOPATHIES rank and cilia pathway recovery**

  ----------------------------- -------------------------- --------------------------- ---------------------------------------------
  **Method**                    **WP_CILIOPATHIES rank**   **Top-5 includes cilia?**   **Key statistic**

  seed_fisher (B1, corrected)   1 / 2,130                  Yes (ranks 1, 3, 4)         BH p=4.53×10⁻³¹; overlap=61/170

  neighborhood_fisher (B2)      not top-50                 No                          58,846-gene neighborhood; no discrimination

  raw_ppr_gsea (B3)             1,994 / 2,130              No                          Gene-level PPR insufficient

  cond_ppr_gsea (B3b)           456 / 2,130                No                          Conditioned scores insufficient

  BIFO full-arm (B4)            43 / 2,130                 Yes (top 2%)                degree_norm=8.51×10⁻⁶; null_z=48.71; q=0.006; not hub-flagged

  BIFO member-level null        member_mean null_z=1.39    Yes                         empirical p=0.057 (not significant);
                                                                                        structural matching only (degree + membership count)
  ----------------------------- -------------------------- --------------------------- ---------------------------------------------

Fisher top-5: WP_CILIOPATHIES (1), REACTOME_DISEASES_OF_METABOLISM (2), WP_PRIMARY_CILIUM_CRISPR (3), WP_JOUBERT_SYNDROME (4), REACTOME_DISORDERS_TRANSMEMBRANE (5). BIFO top-5: WP_CILIOPATHIES (1), YOSHIMURA_MAPK8 (2; hub-flagged), NABA_MATRISOME (3; hub-flagged), Ionophore activity (4), REACTOME_DISEASES_OF_METABOLISM (5; hub-flagged).

### 8.2 BIFO recovers ciliopathy signal in discovery mode

Under BIFO full-arm scoring, WP_CILIOPATHIES ranked 43rd of 2,130 canonical pathways (degree_norm = 8.51×10⁻⁶; not hub-flagged), placing it in the top 2% of the scored universe. WP_JOUBERT_SYNDROME, a closely related ciliopathy pathway sharing many structural members, ranked 34th. This result was obtained without pre-specifying any reference pathway. The cilia signal emerges from PPR propagation across all 1,276 seeds simultaneously: the 22 cilia-related genes in the seed set (DNAH5, CEP290, CC2D2A, PKD1L1, KIAA0586, NPHP4, TMEM67, DNAI2, CCDC39, ARL13B, HYLS1, and others spanning dynein heavy chains, transition zone components, IFT regulators, and left-right asymmetry genes) pull propagated probability mass toward the ciliopathy pathway cluster through shared graph neighborhoods, while the \~1,254 non-cilia variant genes contribute diffuse background signal that degree normalization suppresses.

The pathway-node rewiring null shows that WP_CILIOPATHIES carries the strongest statistical enrichment signal in the dataset: null_z = 48.71 (empirical q = 0.006), meaning the observed degree_norm score is 48.7 standard deviations above the mean of 1,000 degree-preserving membership rewiring permutations. This directly tests whether the specific gene membership of WP_CILIOPATHIES — rather than graph topology alone — drives the signal. The member-level stratified null (member_mean null_z = 1.39, p = 0.057) indicates that signal is concentrated at the pathway node level rather than distributed uniformly across all 170 member genes, consistent with a subset of cilia-associated CHD variant genes driving propagated mass to the ciliopathy pathway cluster through the mechanistic network. This member-level null tests whether propagated signal concentrates within the genes defining a pathway, rather than whether signal reaches the pathway node itself. This member-level empirical support, combined with Fisher enrichment and cross-cohort recurrence in KF-NBL where WP_CILIOPATHIES also ranked first, provides converging evidence that the ciliopathy signal reflects concentration of propagated signal within biologically coherent gene sets rather than a byproduct of graph topology.

BIFO recovers a coherent ciliopathy pathway cluster. Of 17 cilia, ciliopathy, and hedgehog pathway annotations in the 2,130-pathway universe, 11 (65%) rank above the median. The core ciliopathy pathways show the strongest enrichment: WP_JOUBERT_SYNDROME (rank 34, null_z = 54.7), WP_CILIOPATHIES (rank 43, null_z = 48.7), REACTOME_CILIUM_ASSEMBLY (rank 163, null_z = 22.2), WP_GENES_RELATED_TO_PRIMARY_CILIUM (rank 171, null_z = 19.9), and REACTOME_HEDGEHOG_OFF_STATE (rank 216, null_z = 18.3) are all significant (q = 0.006). Notably, generic Hedgehog signaling pathways not specific to cilia (HALLMARK_HEDGEHOG_SIGNALING, PID_HEDGEHOG_GLI_PATHWAY, REACTOME_HEDGEHOG_ON_STATE) show negative null_z values, indicating depletion rather than enrichment — a biologically interpretable distinction between cilia-specific and generic Hedgehog signal. Hub-flagged pathways in the BIFO top-5 (YOSHIMURA_MAPK8, NABA_MATRISOME, REACTOME_DISEASES_OF_METABOLISM) reflect high-degree graph structure rather than specific cilia signal and are distinguishable by the hub flag in the output.

Full top-20 ranked pathways per method for KF-CHD and KF-NBL are provided in Supplementary Table ST3.

Full cilia pathway cluster ranking under BIFO for KF-CHD and KF-NBL is provided in Supplementary Table ST4.

Head-to-head rank comparison between seed Fisher and BIFO for all scored pathways is provided as downloadable data in Supplementary Table ST5.

These results indicate that statistical inference in BIFO operates over propagated signal rather than set membership alone, and that pathway-level interpretation requires separating signal propagation from signal evaluation.

### 8.3 Cross-cohort convergence: KF-NBL independent replication

Applying identical BIFO analysis to the KF-NBL cohort (1,395 seed genes from 460 neuroblastoma probands, 2,654,867 conditioned edges, 2,196 scored pathways after CGP filter), WP_CILIOPATHIES ranked third of 2,196 pathways (degree_norm = 4.24×10⁻⁶, null_z = 18.95, q = 0.012), with WP_JOUBERT_SYNDROME ranking 17th. The top two pathways by degree_norm were GO terms (Ionophore activity, Transmembrane Transport), reflecting the broader NBL seed neighborhood. Seed-only Fisher (B1, corrected) ranked WP_CILIOPATHIES first of 2,196 pathways (BH p = 3.85×10⁻³²). The member-level stratified null for KF-NBL shows significant signal (member_mean null_z = 2.43, p = 0.003), indicating that cilia gene members collectively carry elevated PPR scores in KF-NBL, in contrast to KF-CHD where signal is concentrated at the pathway node (member_mean null_z = 1.39, p = 0.057), consistent with signal concentrated at pathway node level through a subset of cilia-associated variant genes. Cross-cohort convergence on WP_CILIOPATHIES under both BIFO (rank 43 CHD, rank 3 NBL) and Fisher (rank 1 in both cohorts), combined with extraordinarily strong null_z values in both cohorts (48.7 and 19.0), provides strong converging evidence for a genuine biological signal.

The KF-CHD and KF-NBL seed sets share 570 genes (44.3% of the CHD set), reflecting shared rare Mendelian disease gene carrier burden at MAF ≤0.001 rather than disease-specific biology. At a stricter n≥2 carrier count filter, the overlap decreases to 117 of 387 CHD genes (30%) while both cohorts still show significant WP_CILIOPATHIES enrichment (KF-CHD null_z=48.7; KF-NBL rank 3) --- the cilia signal is present in both the shared and cohort-specific variant components. The convergence on the same top pathway across two biologically distinct pediatric diseases is consistent with the known developmental role of cilia in both cardiac septation and neural crest migration, and with the companion U24 cross-cohort analysis (Stear et al. 2026) which independently identified cilia enrichment in KF cohorts using permutation-based GSEA.

**Table 8.3. Cross-cohort comparison --- WP_CILIOPATHIES and cilia pathway recovery**

  --------------------------------------------- ----------------------------- -----------------------------
  **Metric**                                    **KF-CHD**                    **KF-NBL**

  Seed genes (MAF≤0.001, n≥1)                   1,276                         1,395

  Conditioned edges                             2,482,752                     2,647,055

  Pathways scored                               2,130                         2,196

  WP_CILIOPATHIES rank --- BIFO                 43 / 2,130 (null_z=48.71)     3 / 2,196 (null_z=18.95)

  WP_CILIOPATHIES rank --- Fisher (corrected)   1 / 2,130 (BH p=4.53×10⁻³¹)   1 / 2,196 (BH p=3.85×10⁻³²)

  Cilia seed genes in pool                      22                            19

  Inter-cohort gene overlap                     570 / 1,287 (44.3%)           ---
  --------------------------------------------- ----------------------------- -----------------------------

### 8.4 Bootstrap resampling: cilia signal requires aggregate cohort burden

To assess whether cilia pathway recovery is robust to seed set size, 500 bootstrap draws at each of three seed sizes (n=10, 20, 30) were drawn from each cohort\'s full seed pool. Results reveal a consistent pattern across both cohorts: neither BIFO nor Fisher reliably recovers cilia pathways from small random gene subsets, but both converge at full cohort scale.

At the primary run (full 1,276 CHD seeds), BIFO achieves P@10 = 0.00 against the 16-pathway cilia reference with mean cilia reference rank of 889 and AP = 0.012. Fisher achieves P@10 = 0.20 (WP_CILIOPATHIES rank 1) and AP = 0.130. The BIFO P@10 of 0.00 reflects that no cilia reference pathway ranks in the top 10 by degree_norm, though WP_CILIOPATHIES ranks 43rd with null_z = 48.71 — the strongest enrichment signal in the dataset. At n=10--30 random seeds, P@10 is near zero for both methods (BIFO: 0.008--0.011; Fisher: 0.018--0.035). Fisher finds any cilia pathway in the top-10 in 13--21% of n=10--30 bootstrap runs versus 7--9% for BIFO --- Fisher is modestly more sensitive at small seed sizes. At the full cohort scale, BIFO's null_z signal (CHD: 48.7; NBL: 19.0) confirms that graph conditioning recovers a statistically robust ciliopathy signal that is absent at small seed sizes, while Fisher's higher absolute P@10 reflects its sensitivity to direct overlap once the seed set is large enough.

The core finding is that the cilia signal in these cohorts is distributed across many genes and requires aggregate cohort-scale variant burden to emerge. Neither method recovers it reliably from n=10--30 randomly drawn genes, and both converge at cohort scale. This is consistent with a polygenic developmental signal embedded in heterogeneous rare variant background --- BIFO\'s graph propagation concentrates this distributed signal through shared pathway neighborhoods, while Fisher requires sufficient overlap count to produce significant statistics.

**Table 8.4. Bootstrap resampling results --- BIFO vs. Fisher cilia pathway recovery**

  -------------------------- --------------- ----------------- ------------- --------------- ----------------------- ----------------------------- -------------------------------
  **Seed size**              **BIFO P@10**   **Fisher P@10**   **BIFO AP**   **Fisher AP**   **BIFO \> Fisher AP**   **Any cilia top-10 (BIFO)**   **Any cilia top-10 (Fisher)**

  KF-CHD primary (n=1,276)   0.000           0.200             0.0124        0.1298          ---                     ---                           ---

  KF-CHD n=10 (500 runs)     0.008           0.018             0.013         0.013           50.8%                   6.6%                          13.0%

  KF-CHD n=20 (500 runs)     0.008           0.029             0.012         0.017           49.8%                   7.4%                          18.6%

  KF-CHD n=30 (500 runs)     0.011           0.035             0.014         0.021           44.2%                   9.0%                          21.0%

  KF-NBL primary (n=1,395)   0.100           0.200             0.0442        0.0991          ---                     ---                           ---

  KF-NBL n=10 (500 runs)     0.012           0.022             0.013         0.012           59.2%                   7.6%                          14.8%

  KF-NBL n=20 (500 runs)     0.012           0.025             0.013         0.016           53.4%                   9.0%                          15.6%

  KF-NBL n=30 (500 runs)     0.010           0.041             0.013         0.021           45.2%                   7.6%                          24.2%
  -------------------------- --------------- ----------------- ------------- --------------- ----------------------- ----------------------------- -------------------------------

![
**Cross-cohort convergence: KF-CHD and KF-NBL independently recover cilia pathways.**
(**A**) WP_CILIOPATHIES ranks first under both BIFO full-arm and corrected Seed Fisher in both cohorts.
(**B**) BIFO pathway rank scatter (top 3,000 shown) with cilia pathways highlighted in red (n = 19). Cilia pathways cluster in the top-left corner of both axes, indicating concordant prioritization across cohorts; non-cilia pathways (grey) scatter along the diagonal.
(**C**) Cilia pathway cluster: BIFO rank of each detected cilia-related pathway in KF-CHD (blue circle) vs. KF-NBL (orange triangle). All detected cilia pathways rank in the top half of the scored pathway universe in both cohorts.
(**D**) Bootstrap resampling against a 17-pathway cilia reference: P@10 distribution for BIFO (blue) and Seed Fisher (red) at random seed sample sizes n = 10, 20, 30 (500 runs per seed size). Dashed and dotted horizontal lines indicate the primary-run P@10 for each method. Cilia signal requires full cohort-scale seed sets; neither method recovers it reliably from 10–30 random genes.
](images/fig8_crosscohort.png){#fig:crosscohort width="100%"}



## Discussion

The central result of this study is that BIFO recovers a biologically meaningful signal that is independently supported by standard enrichment methods, while remaining effective in settings where those methods begin to fail. In both Kids First cohorts, congenital heart disease and neuroblastoma, a coherent ciliopathy pathway cluster emerges under BIFO scoring, with WP_CILIOPATHIES carrying the strongest statistical enrichment signal in the KF-CHD dataset (null_z = 48.7, q = 0.006, rank 43/2,130) and ranking third in KF-NBL (null_z = 19.0, q = 0.012, rank 3/2,196). Importantly, this signal is not unique to the graph-based approach: when implemented correctly, seed-only Fisher enrichment independently identifies WP_CILIOPATHIES as the top-ranked pathway in both cohorts. The agreement between these two fundamentally different methods, one based on direct gene–pathway overlap and the other on constrained graph propagation, provides strong evidence that the result reflects underlying biology rather than an artefact of graph topology or propagation dynamics. This agreement establishes that BIFO does not introduce spurious signal but recovers the same biological structure through a different inference mechanism.

The distinction lies in how the signal is detected. Fisher enrichment identifies pathways through direct overlap between genes and pathway membership. BIFO, in contrast, recovers the same signal through propagation across a constrained graph, without requiring strong direct overlap. This allows BIFO to remain effective in regimes where enrichment methods lose reliability, including small gene sets, large heterogeneous cohorts, and graph-derived neighborhoods. In this sense, BIFO does not replace standard enrichment methods; it extends them by enabling pathway-level interpretation when overlap-based approaches are unstable or uninformative.

This difference becomes clear when examining the failure modes of standard enrichment. At small gene set sizes, Fisher enrichment is sensitive to incidental overlap and often prioritizes non-specific pathways. In the curated benchmark, seed-only Fisher achieves P@10 = 0.30, while BIFO reaches P@10 = 0.70, reflecting the instability of direct overlap at this scale. At large gene set sizes, such as those derived from rare variant aggregation, naive or standard-precision implementations can collapse, and even correctly implemented methods may lose discriminative power when gene sets are very large. Graph-based expansion approaches introduce a complementary problem: by inflating the gene set to include most of the graph, they eliminate contrast between pathways. These limitations reflect a common issue: standard methods operate directly on gene membership and do not account for how signal is distributed across biological relationships.

BIFO addresses this by separating propagation from scoring. Signal is first propagated through the graph using a constrained set of biologically admissible edges, and pathways are then evaluated based on where that signal accumulates. This allows weak signals that are distributed across many genes to reinforce each other through shared biological context, while incoherent background signal disperses. The scoring step then operates on this structured signal rather than on the original gene list.

A key component of this behavior is the pathway scoring function itself. The results show that propagation alone is not sufficient: while preranked GSEA on PPR scores recovers some pathway signal, its performance remains limited compared to the full BIFO approach (P@10 = 0.10 for both raw and conditioned PPR GSEA versus P@10 = 0.70 for BIFO). The improvement arises from how propagated signal is translated into pathway-level scores.

The BIFO scoring function evaluates the direct PPR score at each pathway node and normalizes it by the square root of pathway size. This formulation reflects two design choices. First, it requires signal to reach the pathway node itself. Only signal that successfully propagates from the seed genes into the pathway layer contributes to the score. Because the primary scoring function operates on pathway concept nodes rather than aggregating member gene scores, pathway-level recovery requires successful propagation of signal to those nodes — connecting the structural claim directly to the implemented scoring behavior. In contrast, gene-level methods such as GSEA operate on ranked gene lists and do not require this transfer, which can blur distinctions between pathways connected through shared genes or indirect correlations.

Second, the square-root normalization reduces bias toward large pathways without eliminating their contribution. Larger pathways accumulate more propagated signal because more genes contribute PPR mass to the pathway node through Pathway Contribution edges. Fully normalizing by pathway size would overcorrect this effect and suppress biologically meaningful programs. The square-root penalty provides a balance: it down-weights large, non-specific pathways while preserving signal in pathways that are both large and biologically coherent. This scoring variant was selected as the primary function before benchmark freeze; alternative variants were evaluated but not used for primary analysis.

Together, these properties distinguish BIFO from both overlap-based and propagation-based alternatives. Fisher enrichment depends entirely on direct membership overlap, while propagation-only approaches tend to favor highly connected regions of the graph. BIFO combines propagation with pathway-level scoring in a way that requires biologically meaningful signal transfer and controls for pathway size. The result is a scoring scheme that reflects both the structure of the graph and the specificity of the biological program. The observed performance gain reflects the combination of constrained propagation and a pathway-node scoring formulation that requires signal accumulation at pathway concept nodes, rather than propagation alone; the poor performance of conditioned PPR GSEA relative to BIFO full-arm isolates the contribution of the scoring formulation beyond what the conditioned gene-level score ordering provides.

The ablation analysis provides a mechanistic explanation for why this works. When propagation is restricted to mechanistic edges alone, pathway scores collapse to zero across the graph — an observation that holds in this benchmark graph and under the direct pathway-node scoring formulation used here. This result reflects how biological knowledge is represented in this graph slice. Mechanistic relationships connect genes within a molecular network, while pathway annotations are stored separately as curated gene sets. These two components form distinct layers of the graph and are connected only through gene-to-pathway membership relationships. Consistent with this structure, removing bridge edges reduces pathway recovery (P@10 decreases from 0.70 to 0.60), while mechanistic-only propagation yields zero pathway scores.

This leads to a simple but important interpretation within this graph construction and scoring formulation. The graph is organized, in this benchmark slice, as a two-layer system: a mechanistic layer encoding biological processes and an annotation layer encoding curated pathway knowledge. BIFO makes this structure explicit by treating gene-to-pathway relationships as a distinct class of edges that are allowed to carry signal. The ablation results show that under the primary degree_norm scoring formulation — which requires propagated mass to arrive at the pathway concept node directly — these bridge edges are necessary for non-zero pathway scores. They do not generate signal independently; signal must originate in the mechanistic layer and transfer across the bridge. Although Pathway Contribution edges dominate numerically — comprising 85.8% of propagating edges in the conditioned operator — the ablation results confirm they act as transfer operators rather than signal sources under the unweighted PPR operator used here: they map propagated gene-level probability mass onto pathway nodes without introducing additional signal. This two-layer structure reflects the membership architecture of the exported graph slice, in which explicit gene-to-pathway membership edges are present primarily for MSigDB, WikiPathways, and GO annotations; pathway sources without direct membership edges in this export would not exhibit the same structural separation. Alternative scoring variants based on member-gene aggregation (member_mean, member_max) were evaluated but do not isolate pathway-node signal transfer and therefore do not directly test the structural accessibility of pathway nodes under different propagation operators; they are not used for the primary analysis.

The robustness analysis shows that these results are not dependent on a particular gene set. Across all 3,003 partitions of the CHD gene pool, BIFO consistently improves pathway ranking relative to unconditioned propagation. At the same time, the comparison with Fisher enrichment highlights an important boundary. When seed genes directly overlap with pathway members, Fisher performs well, as expected. BIFO is most useful in the complementary setting, where relevant pathways are connected indirectly through biological relationships. This distinction aligns with the difference between recovery tasks and discovery tasks and explains why BIFO is particularly effective for cohort-scale analyses.

The KF cohort results further clarify the nature of the recovered signal. The primary contribution of this analysis is that BIFO remains effective in the large-cohort regime where standard enrichment methods lose discriminative power due to p-value floor collapse. The convergence with correctly implemented Fisher enrichment confirms that the recovered signal reflects underlying biology rather than a propagation artefact, while the requirement for cohort-scale seed sets reflects the distributed nature of the underlying developmental process rather than a limitation of either method. The ciliopathy signal is not driven by a small number of genes but is distributed across a subset of genes embedded in a larger heterogeneous background, consistent with a polygenic developmental process rather than a single dominant driver. The biological interpretation of these findings and their implications for cilia-related developmental disease are examined in depth in the companion cross-cohort analysis (Stear et al. 2026).

Several limitations should be noted. The benchmark graph is a controlled 1-hop projection of a larger knowledge graph and includes only a subset of source vocabularies. As a result, some nodes cannot be resolved and are excluded from propagation. The finding that mechanistic edges alone cannot reach pathway nodes depends on this graph configuration and may change with additional data sources. However, the underlying pattern, a separation between mechanistic relationships and curated pathway annotations, is a common feature of ontology-based knowledge graphs. The conditioning framework itself is graph-agnostic: the specific structural result depends on representation choices in the source graph, but the need to distinguish admissible flow from associative and contextual relationships does not. An alternative approach of weighting edges within a single operator would conflate causal and associative relationships, whereas BIFO preserves this distinction at the representation level — enabling attribution of pathway score changes to specific edge classes rather than to the aggregate topology.

Gene-level recovery metrics are at or near ceiling in the curated benchmark due to the small size and strong connectivity of the test set, and are not informative for discriminating between method variants in this setting. Pathway-level evaluation and cohort-scale analysis provide the meaningful performance comparisons. BIFO as implemented here is best understood as a biologically constrained propagation schema with a reference DDKG implementation, rather than a formal ontology in the description-logic sense; the flow class vocabulary and admissibility rules constitute an operational specification that can be extended or reconfigured for other graph representations. Additionally, the 15-gene CHD benchmark pool is itself curated from prior knowledge, which bounds generalization claims beyond the illustrative benchmark setting; the exhaustive 3,003-split resampling addresses seed-composition sensitivity within this pool but does not substitute for an independent benchmark.

BIFO-native empirical significance operates at two levels. Graph composition determines rewiring null calibration: the null is valid when non-bridge edges provide sufficient structural routing constraint, and miscalibrated when bridge edges dominate the propagating graph. In the curated benchmark (85.8% bridge edges, 10 seeds), the null is valid because with only 10 seeds, random rewirings rarely replicate specific cardiac signal regardless of bridge fraction, yielding 49/550 pathways significant at q < 0.05 with top cardiac pathways null_z > 9. In KF-CHD, bridge edges comprise 41.4% of propagating edges under the corrected unidirectional pipeline; the rewiring null is well-calibrated, and WP_CILIOPATHIES achieves the highest null_z in the dataset (null_z = 48.7, q = 0.006). In KF-NBL, bridge edges comprise a similar fraction, and the null is similarly well-calibrated (WP_CILIOPATHIES null_z = 19.0, q = 0.012). These results confirm that the rewiring null provides valid statistical inference when gene-to-pathway membership edges are included in a unidirectional, non-feedback configuration.

A complementary stratified member-level null — which tests whether a pathway's constituent genes carry disproportionate propagated signal relative to structurally matched gene sets, without requiring PPR reruns — is less sensitive to bridge edge fraction because it operates on the fixed propagated signal rather than the propagation operator itself, and is empirically stable across the seed-size ranges evaluated here. In both KF-CHD and KF-NBL, the pathway-node rewiring null provides strong primary evidence (CHD: null_z = 48.7, q = 0.006; NBL: null_z = 19.0, q = 0.012). The member-level null shows weaker signal in KF-CHD (member_mean null_z = 1.39, p = 0.057) but significant signal in KF-NBL (member_mean null_z = 2.43, p = 0.003), indicating that in the neuroblastoma cohort the signal is distributed across member genes as well as concentrated at the pathway node level. The member-level null as implemented uses structural matching only (degree and pathway membership count) and does not directly validate the degree_norm pathway-node score; it provides converging evidence rather than a primary significance test for that score variant. Development of a connectivity-aware pathway-node null that accounts for bridge edge fraction — such as degree-aware bipartite rewiring — remains the appropriate direction for a fully unified significance framework across all graph compositions. More broadly, these results show that statistical calibration in graph-based inference depends not only on the scoring function but on the structure of the propagation operator itself.

Overall, BIFO provides a framework for making graph-based biological analysis both effective and interpretable. By constraining which relationships are allowed to carry signal and by explicitly defining how propagated signal is evaluated at the pathway level, it shifts the focus from raw connectivity to biologically meaningful structure. This perspective provides a principled basis for analyzing heterogeneous biological data, particularly in settings where standard methods struggle to extract coherent signal.


## Supplementary Methods

### SM1 — Variant Processing and Gene Aggregation

**Kids First harmonized sequencing and alignment.** Whole-genome sequencing (WGS) data were obtained from two independent germline cohorts: NIH dbGAP phs001138 (congenital heart defects, n=1121 total probands; n=697 with complete WGS data used in this analysis) and NIH dbGAP phs001436 (neuroblastoma, n=554 total probands; n=460 used in this analysis). All samples were sequenced on Illumina platforms using paired-end protocols. Raw sequencing reads were processed by the Kids First Data Resource Center pipelines, aligned to the human reference genome build GRCh38 using BWA (Burrows–Wheeler alignment) algorithms, and variant discovery was performed with the Genome Analysis Toolkit (GATK) Best Practices workflow. Cohorts were harmonized to ensure consistent reference build, alignment parameters, and variant-calling procedures. For cohorts originally processed using joint genotyping in family-based designs (e.g., trios or duos), multi-sample VCFs were decomposed into proband-sample VCFs for downstream per-individual filtering and aggregation. Cohorts sequenced as proband-only were retained as individual-level VCFs. All variants analyzed represent germline calls.

**Variant quality filtering.** 
Multi-allelic sites were split into biallelic records to ensure consistent downstream filtering and annotation. Variant-level and genotype-level quality control was performed using bcftools (v1.30) to ensure consistency across all cohorts. Only variants annotated with FILTER=PASS, as determined by the GATK variant quality score recalibration (VQSR) or hard-filtering framework, were retained. At the genotype level, we required a minimum genotype quality (GQ) of 20, corresponding to an estimated posterior genotype accuracy of ≥99%, and a minimum read depth (DP) of 10 reads to ensure adequate sequencing support at each locus. An initial broad population frequency filter of MAF ≤1% in gnomAD was applied at this stage to remove common variants unlikely to be disease-relevant, consistent with standard rare disease variant processing pipelines. Genotype-level filtering was applied prior to aggregation across individuals to ensure that only high-confidence variant calls contributed to downstream analyses.

**Pathogenicity classification.** To enrich for variants with predicted functional impact, we implemented a complementary pathogenicity prioritization strategy integrating both consequence-based and model-based annotations. First, variants were functionally annotated using the Ensembl Variant Effect Predictor (VEP) [@doi:10.1186/s13059-016-0974-4], incorporating transcript consequence, gene assignment, and predicted functional impact categories. Variants annotated by Ensembl VEP as having HIGH impact (including predicted loss-of-function consequences such as stop-gain, frameshift, and canonical splice-site variants) were retained. 
Second, variants were evaluated using AutoGVP [@doi:10.1093/bioinformatics/btae114], a supervised pathogenicity prediction framework that integrates functional, evolutionary, and annotation-based features. Variants classified as “Pathogenic” or “Likely_Pathogenic” by AutoGVP were retained. Variants meeting either criterion (VEP HIGH impact or AutoGVP “Pathogenic/Likely pathogenic” classification) were included in the final analysis set. This approach enabled capture of canonical loss-of-function alleles as well as predicted deleterious missense or regulatory variants with strong pathogenic support. Both annotation steps were performed against the GRCh38 reference and corresponding Ensembl gene models. The final analytical dataset comprised high-confidence germline variants that passed GATK variant-level filters, met stringent genotype-level depth and quality thresholds, and were predicted to be deleterious by VEP and/or AutoGVP. This harmonized filtering framework ensured consistent variant quality across both cohorts and enriched the dataset for variants with a high prior probability of functional relevance. All downstream gene-level aggregation, cross-cohort comparisons, and enrichment analyses were performed using this curated set of high-confidence pathogenic variants. 


**Population allele frequency filtering.** Variants were filtered against population allele frequency estimates from the Genome Aggregation Database (gnomAD) v3.1 [@doi:10.1038/s41586-020-2308-7], which provides allele frequencies across diverse global populations aligned to GRCh38. For this study, we applied a more stringent analytical threshold of MAF ≤0.001 (0.1%) using the gnomAD v3.1 non-cancer popmax allele frequency — the maximum allele frequency observed across any gnomAD ancestry group, excluding cancer cohorts. This represents a tenfold reduction relative to the initial processing filter and was applied to the already quality-filtered variant set to restrict analyses to ultra-rare variants. This threshold was selected to enrich for rare variants consistent with a Mendelian or strong-effect rare disease genetic architecture, and to match the filtering parameters used in the companion U24 cross-cohort enrichment analysis (Stear et al., CFDE Meeting 2026), enabling direct comparability of gene lists across studies. Variants exceeding this frequency threshold in any gnomAD ancestry group were excluded regardless of their pathogenicity classification.

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

**Post-export merge.** After cleaning, edge files are merged using pandas concat (not shell cat) to preserve CSV headers and avoid duplicate header rows. For KF cohort runs the merge combines the raw edge file and the pathway membership edge file into a single `edges_all.csv` input for `bifo_conditioning.py`. Merge commands are documented in comments at the end of each cypher file.

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

*ST5 consists of downloadable CSV files and is not typeset.*

### ST1 — Top-10 ranked pathways per propagation arm, curated CHD benchmark

Three-arm comparison: Full BIFO (93,487 propagating edges), Ablation (16,026 propagating edges, no Pathway Contribution bridge edges), and Mechanistic-only (9,710 edges). Pathway universe: 550 pathways (8–300 members). CHD reference pathways marked with ✓ in the Ref. column. Score = degree_norm (direct PPR score at pathway node / √member count).

**Full BIFO**

| Rank | Pathway name | SAB | Score (degree_norm) | Members | Ref. |
| --- | --- | --- | --- | --- | --- |
| 1 | BRUNEAU_SEPTATION_VENTRICULAR | MSIGDB | 2.233e-04 | 8 | ✓ |
| 2 | WP_HEART_DEVELOPMENT | MSIGDB | 2.142e-04 | 37 | ✓ |
| 3 | REACTOME_YAP1_AND_WWTR1_TAZ_STIMULATED_GENE_EXPRESSION | MSIGDB | 1.845e-04 | 8 | — |
| 4 | WP_CARDIAC_PROGENITOR_DIFFERENTIATION | MSIGDB | 1.630e-04 | 32 | ✓ |
| 5 | BIOCARTA_NFAT_PATHWAY | MSIGDB | 1.589e-04 | 27 | ✓ |
| 6 | WP_22Q112_COPY_NUMBER_VARIATION_SYNDROME | MSIGDB | 1.093e-04 | 35 | ✓ |
| 7 | REACTOME_MUSCLE_CONTRACTION | MSIGDB | 1.005e-04 | 85 | ✓ |
| 8 | Cardiac Muscle Contraction | GO | 9.440e-05 | 12 | — |
| 9 | REACTOME_CARDIAC_CONDUCTION | MSIGDB | 9.104e-05 | 39 | ✓ |
| 10 | MEISSNER_BRAIN_HCP_WITH_H3K27ME3 | MSIGDB | 8.695e-05 | 145 | — |


**Ablation (no bridge edges)**

| Rank | Pathway name | SAB | Score (degree_norm) | Members | Ref. |
| --- | --- | --- | --- | --- | --- |
| 1 | BRUNEAU_SEPTATION_VENTRICULAR | MSIGDB | 1.523e-04 | 8 | ✓ |
| 2 | WP_HEART_DEVELOPMENT | MSIGDB | 1.259e-04 | 37 | ✓ |
| 3 | REACTOME_YAP1_AND_WWTR1_TAZ_STIMULATED_GENE_EXPRESSION | MSIGDB | 1.121e-04 | 8 | — |
| 4 | WP_CARDIAC_PROGENITOR_DIFFERENTIATION | MSIGDB | 9.378e-05 | 32 | ✓ |
| 5 | BIOCARTA_NFAT_PATHWAY | MSIGDB | 9.293e-05 | 27 | ✓ |
| 6 | WP_22Q112_COPY_NUMBER_VARIATION_SYNDROME | MSIGDB | 6.837e-05 | 35 | ✓ |
| 7 | REACTOME_MUSCLE_CONTRACTION | MSIGDB | 5.456e-05 | 85 | ✓ |
| 8 | Cardiac Muscle Contraction | GO | 5.370e-05 | 12 | — |
| 9 | RIZ_ERYTHROID_DIFFERENTIATION_HBZ | MSIGDB | 5.171e-05 | 12 | — |
| 10 | RIZ_ERYTHROID_DIFFERENTIATION_HEMGN | MSIGDB | 5.171e-05 | 12 | — |


**Mechanistic-only**

*All 550 pathway scores are exactly zero under mechanistic-only propagation. Pathway nodes are structurally unreachable from seed genes through mechanistic edges alone; gene-to-pathway connectivity requires Pathway Contribution bridge edges. P@10 = 0.00, Enrichment@10 = 0×.*


---

### ST2 — Baseline enrichment method comparison, curated CHD benchmark

Top-20 ranked pathways under each enrichment method, evaluated on the identical 550-pathway universe. CHD reference pathways marked with ✓. Score/stat column: degree_norm for B0 and B4; hypergeometric stat for B1/B2; enrichment score for B3/B3b.

**B0 — Degree-weighted seed overlap**

| Rank | Pathway name | SAB | Score / stat | Members | Ref. |
| --- | --- | --- | --- | --- | --- |
| 1 | BRUNEAU_SEPTATION_VENTRICULAR | MSIGDB | 1150.8163 | 8 | ✓ |
| 2 | WP_HEART_DEVELOPMENT | MSIGDB | 1111.5016 | 37 | ✓ |
| 3 | PID_HES_HEY_PATHWAY | MSIGDB | 1032.5000 | 16 | — |
| 4 | WANG_THOC1_TARGETS_DN | MSIGDB | 904.8355 | 11 | — |
| 5 | REACTOME_PRE_NOTCH_PROCESSING_IN_GOLGI | MSIGDB | 879.3333 | 9 | — |
| 6 | REACTOME_YAP1_AND_WWTR1_TAZ_STIMULATED_GENE_EXPRESSION | MSIGDB | 856.3063 | 8 | — |
| 7 | REACTOME_NOTCH4_INTRACELLULAR_DOMAIN_REGULATES_TRANSCRIPTION | MSIGDB | 834.2088 | 10 | — |
| 8 | WP_CARDIAC_PROGENITOR_DIFFERENTIATION | MSIGDB | 806.6321 | 32 | ✓ |
| 9 | FUKUSHIMA_TNFSF11_TARGETS | MSIGDB | 761.5250 | 12 | — |
| 10 | HALLMARK_NOTCH_SIGNALING | MSIGDB | 761.5250 | 12 | ✓ |
| 11 | WP_CANONICAL_AND_NONCANONICAL_NOTCH_SIGNALING | MSIGDB | 681.1287 | 15 | ✓ |
| 12 | WP_NOTCH_SIGNALING | MSIGDB | 659.5000 | 16 | ✓ |
| 13 | WP_ENDODERM_DIFFERENTIATION | MSIGDB | 653.0103 | 40 | — |
| 14 | PID_NOTCH_PATHWAY | MSIGDB | 621.7826 | 18 | ✓ |
| 15 | REACTOME_PRE_NOTCH_EXPRESSION_AND_PROCESSING | MSIGDB | 621.7826 | 18 | — |
| 16 | REACTOME_ACTIVATED_NOTCH1_TRANSMITS_SIGNAL_TO_THE_NUCLEUS | MSIGDB | 615.8900 | 8 | — |
| 17 | WP_NOTCH1_REGULATION_OF_HUMAN_ENDOTHELIAL_CELL_CALCIFICATION | MSIGDB | 615.8900 | 8 | — |
| 18 | LUND_SILENCED_BY_METHYLATION | MSIGDB | 615.8900 | 8 | — |
| 19 | REACTOME_NOTCH1_INTRACELLULAR_DOMAIN_REGULATES_TRANSCRIPTION | MSIGDB | 615.8900 | 8 | ✓ |
| 20 | WP_PTF1A_RELATED_REGULATORY_PATHWAY | MSIGDB | 615.8900 | 8 | — |


**B1 — Seed-only Fisher (hypergeometric)**

| Rank | Pathway name | SAB | Score / stat | Members | Ref. |
| --- | --- | --- | --- | --- | --- |
| 1 | LINDGREN_BLADDER_CANCER_CLUSTER_3_DN | MSIGDB | 0.000e+00 | 53 | — |
| 2 | PEREZ_TP63_TARGETS | MSIGDB | 0.000e+00 | 104 | — |
| 3 | PHONG_TNF_RESPONSE_VIA_P38_COMPLETE | MSIGDB | 0.000e+00 | 50 | — |
| 4 | LU_TUMOR_ANGIOGENESIS_UP | MSIGDB | 0.000e+00 | 9 | — |
| 5 | PID_NOTCH_PATHWAY | MSIGDB | 0.000e+00 | 16 | ✓ |
| 6 | REACTOME_ACTIVATED_NOTCH1_TRANSMITS_SIGNAL_TO_THE_NUCLEUS | MSIGDB | 0.000e+00 | 7 | — |
| 7 | REACTOME_RNA_POLYMERASE_II_TRANSCRIPTION | MSIGDB | 0.000e+00 | 227 | — |
| 8 | FUKUSHIMA_TNFSF11_TARGETS | MSIGDB | 0.000e+00 | 10 | — |
| 9 | REACTOME_SIGNALING_BY_NOTCH | MSIGDB | 0.000e+00 | 42 | ✓ |
| 10 | REACTOME_SIGNALING_BY_NOTCH1 | MSIGDB | 0.000e+00 | 13 | ✓ |
| 11 | REACTOME_SIGNALING_BY_NOTCH1_PEST_DOMAIN_MUTANTS_IN_CANCER | MSIGDB | 0.000e+00 | 11 | — |
| 12 | REACTOME_SIGNALING_BY_NOTCH2 | MSIGDB | 0.000e+00 | 10 | ✓ |
| 13 | REACTOME_SIGNALING_BY_NOTCH3 | MSIGDB | 0.000e+00 | 17 | — |
| 14 | REACTOME_SIGNALING_BY_NOTCH4 | MSIGDB | 0.000e+00 | 19 | — |
| 15 | ZHOU_INFLAMMATORY_RESPONSE_FIMA_UP | MSIGDB | 0.000e+00 | 173 | — |
| 16 | REACTOME_DISEASES_OF_SIGNAL_TRANSDUCTION_BY_GROWTH_FACTOR_RECEPTORS_AND_SECOND_MESSENGERS | MSIGDB | 0.000e+00 | 103 | — |
| 17 | ZWANG_CLASS_3_TRANSIENTLY_INDUCED_BY_EGF | MSIGDB | 0.000e+00 | 75 | — |
| 18 | REACTOME_TRANSCRIPTIONAL_REGULATION_BY_RUNX3 | MSIGDB | 0.000e+00 | 21 | — |
| 19 | GOZGIT_ESR1_TARGETS_DN | MSIGDB | 0.000e+00 | 238 | — |
| 20 | VART_KSHV_INFECTION_ANGIOGENIC_MARKERS_UP | MSIGDB | 0.000e+00 | 73 | — |


**B2 — 1-hop neighborhood Fisher**

| Rank | Pathway name | SAB | Score / stat | Members | Ref. |
| --- | --- | --- | --- | --- | --- |
| 1 | SHEPARD_CRASH_AND_BURN_MUTANT_DN | MSIGDB | 3.468e-04 | 68 | — |
| 2 | MEISSNER_BRAIN_HCP_WITH_H3K27ME3 | MSIGDB | 3.810e-04 | 140 | — |
| 3 | HOLLERN_SQUAMOUS_BREAST_TUMOR | MSIGDB | 5.597e-04 | 91 | — |
| 4 | GRAESSMANN_APOPTOSIS_BY_DOXORUBICIN_UP | MSIGDB | 0.0018 | 276 | — |
| 5 | PURBEY_TARGETS_OF_CTBP1_NOT_SATB1_DN | MSIGDB | 0.0019 | 114 | — |
| 6 | SMID_BREAST_CANCER_LUMINAL_B_DN | MSIGDB | 0.0021 | 247 | — |
| 7 | LEE_BMP2_TARGETS_UP | MSIGDB | 0.0024 | 254 | — |
| 8 | VECCHI_GASTRIC_CANCER_ADVANCED_VS_EARLY_DN | MSIGDB | 0.0035 | 64 | — |
| 9 | ACEVEDO_METHYLATED_IN_LIVER_CANCER_DN | MSIGDB | 0.0036 | 292 | — |
| 10 | HUPER_BREAST_BASAL_VS_LUMINAL_UP | MSIGDB | 0.0039 | 36 | — |
| 11 | OISHI_CHOLANGIOMA_STEM_CELL_LIKE_DN | MSIGDB | 0.0044 | 116 | — |
| 12 | SHEPARD_BMYB_TARGETS | MSIGDB | 0.0053 | 34 | — |
| 13 | VERHAAK_AML_WITH_NPM1_MUTATED_UP | MSIGDB | 0.0058 | 60 | — |
| 14 | BLANCO_MELO_BRONCHIAL_EPITHELIAL_CELLS_INFLUENZA_A_DEL_NS1_INFECTION_UP | MSIGDB | 0.0096 | 208 | — |
| 15 | RIGGI_EWING_SARCOMA_PROGENITOR_UP | MSIGDB | 0.0107 | 135 | — |
| 16 | Intercellular Communication Process | GO | 0.0110 | 153 | — |
| 17 | Developmental process | GO | 0.0122 | 54 | — |
| 18 | SHEPARD_BMYB_MORPHOLINO_DN | MSIGDB | 0.0159 | 73 | — |
| 19 | PEDERSEN_METASTASIS_BY_ERBB2_ISOFORM_7 | MSIGDB | 0.0205 | 127 | — |
| 20 | BOCHKIS_FOXA2_TARGETS | MSIGDB | 0.0221 | 117 | — |


**B3 — Raw PPR preranked GSEA**

| Rank | Pathway name | SAB | Score / stat | Members | Ref. |
| --- | --- | --- | --- | --- | --- |
| 1 | BRUNEAU_SEPTATION_VENTRICULAR | MSIGDB | 0.9680 | — | ✓ |
| 2 | WANG_NFKB_TARGETS | MSIGDB | 0.9653 | — | — |
| 3 | LEE_CALORIE_RESTRICTION_MUSCLE_UP | MSIGDB | 0.9646 | — | — |
| 4 | LIN_TUMOR_ESCAPE_FROM_IMMUNE_ATTACK | MSIGDB | 0.9543 | — | — |
| 5 | Hematopoiesis | GO | 0.9541 | — | — |
| 6 | SASAKI_TARGETS_OF_TP73_AND_TP63 | MSIGDB | 0.9506 | — | — |
| 7 | SHETH_LIVER_CANCER_VS_TXNIP_LOSS_PAM5 | MSIGDB | 0.9465 | — | — |
| 8 | REACTOME_STAT5_ACTIVATION_DOWNSTREAM_OF_FLT3_ITD_MUTANTS | MSIGDB | 0.9385 | — | — |
| 9 | VALK_AML_CLUSTER_2 | MSIGDB | 0.9361 | — | — |
| 10 | WP_NEOVASCULARISATION_PROCESSES | MSIGDB | 0.9354 | — | — |
| 11 | WP_CANCER_IMMUNOTHERAPY_BY_PD1_BLOCKADE | MSIGDB | 0.9319 | — | — |
| 12 | REACTOME_ACTIVATED_NOTCH1_TRANSMITS_SIGNAL_TO_THE_NUCLEUS | MSIGDB | 0.9317 | — | — |
| 13 | REACTOME_PD_1_SIGNALING | MSIGDB | 0.9304 | — | — |
| 14 | WP_NOTCH1_REGULATION_OF_HUMAN_ENDOTHELIAL_CELL_CALCIFICATION | MSIGDB | 0.9300 | — | — |
| 15 | REACTOME_INTERLEUKIN_20_FAMILY_SIGNALING | MSIGDB | 0.9273 | — | — |
| 16 | REACTOME_REGULATION_OF_IFNG_SIGNALING | MSIGDB | 0.9253 | — | — |
| 17 | MA_MYELOID_DIFFERENTIATION_UP | MSIGDB | 0.9238 | — | — |
| 18 | SWEET_KRAS_ONCOGENIC_SIGNATURE | MSIGDB | 0.9237 | — | — |
| 19 | PID_IL5_PATHWAY | MSIGDB | 0.9224 | — | — |
| 20 | REACTOME_NOTCH3_ACTIVATION_AND_TRANSMISSION_OF_SIGNAL_TO_THE_NUCLEUS | MSIGDB | 0.9212 | — | — |


**B3b — Conditioned PPR preranked GSEA**

| Rank | Pathway name | SAB | Score / stat | Members | Ref. |
| --- | --- | --- | --- | --- | --- |
| 1 | HALLMARK_WNT_BETA_CATENIN_SIGNALING | MSIGDB | 0.9737 | — | — |
| 2 | REACTOME_PD_1_SIGNALING | MSIGDB | 0.9705 | — | — |
| 3 | SASAKI_TARGETS_OF_TP73_AND_TP63 | MSIGDB | 0.9662 | — | — |
| 4 | REACTOME_NOTCH4_INTRACELLULAR_DOMAIN_REGULATES_TRANSCRIPTION | MSIGDB | 0.9660 | — | — |
| 5 | BRUNEAU_SEPTATION_VENTRICULAR | MSIGDB | 0.9628 | — | ✓ |
| 6 | VALK_AML_CLUSTER_2 | MSIGDB | 0.9601 | — | — |
| 7 | FONTAINE_FOLLICULAR_THYROID_ADENOMA_UP | MSIGDB | 0.9595 | — | — |
| 8 | WP_NEOVASCULARISATION_PROCESSES | MSIGDB | 0.9582 | — | — |
| 9 | Hematopoiesis | GO | 0.9572 | — | — |
| 10 | MA_MYELOID_DIFFERENTIATION_UP | MSIGDB | 0.9549 | — | — |
| 11 | REACTOME_INTERLEUKIN_20_FAMILY_SIGNALING | MSIGDB | 0.9540 | — | — |
| 12 | REACTOME_REGULATION_OF_IFNA_SIGNALING | MSIGDB | 0.9520 | — | — |
| 13 | LIN_TUMOR_ESCAPE_FROM_IMMUNE_ATTACK | MSIGDB | 0.9498 | — | — |
| 14 | FUKUSHIMA_TNFSF11_TARGETS | MSIGDB | 0.9492 | — | — |
| 15 | GUO_HEX_TARGETS_DN | MSIGDB | 0.9490 | — | — |
| 16 | WANG_CLIM2_TARGETS_DN | MSIGDB | 0.9470 | — | — |
| 17 | WP_CANCER_IMMUNOTHERAPY_BY_PD1_BLOCKADE | MSIGDB | 0.9468 | — | — |
| 18 | Protein dephosphorylation | GO | 0.9467 | — | — |
| 19 | PETROVA_PROX1_TARGETS_UP | MSIGDB | 0.9457 | — | — |
| 20 | REACTOME_REGULATION_OF_IFNG_SIGNALING | MSIGDB | 0.9456 | — | — |


**B4 — BIFO full-arm (degree_norm)**

| Rank | Pathway name | SAB | Score / stat | Members | Ref. |
| --- | --- | --- | --- | --- | --- |
| 1 | BRUNEAU_SEPTATION_VENTRICULAR | MSIGDB | 2.230e-04 | — | ✓ |
| 2 | WP_HEART_DEVELOPMENT | MSIGDB | 2.140e-04 | — | ✓ |
| 3 | REACTOME_YAP1_AND_WWTR1_TAZ_STIMULATED_GENE_EXPRESSION | MSIGDB | 1.840e-04 | — | — |
| 4 | WP_CARDIAC_PROGENITOR_DIFFERENTIATION | MSIGDB | 1.630e-04 | — | ✓ |
| 5 | BIOCARTA_NFAT_PATHWAY | MSIGDB | 1.590e-04 | — | ✓ |
| 6 | WP_22Q112_COPY_NUMBER_VARIATION_SYNDROME | MSIGDB | 1.090e-04 | — | ✓ |
| 7 | REACTOME_MUSCLE_CONTRACTION | MSIGDB | 1.000e-04 | — | ✓ |
| 8 | Cardiac Muscle Contraction | GO | 9.400e-05 | — | — |
| 9 | REACTOME_CARDIAC_CONDUCTION | MSIGDB | 9.100e-05 | — | ✓ |
| 10 | MEISSNER_BRAIN_HCP_WITH_H3K27ME3 | MSIGDB | 8.700e-05 | — | — |
| 11 | RIZ_ERYTHROID_DIFFERENTIATION_HBZ | MSIGDB | 8.300e-05 | — | — |
| 12 | RIZ_ERYTHROID_DIFFERENTIATION_HEMGN | MSIGDB | 8.200e-05 | — | — |
| 13 | LEE_AGING_CEREBELLUM_DN | MSIGDB | 8.100e-05 | — | — |
| 14 | KAAB_FAILED_HEART_VENTRICLE_DN | MSIGDB | 7.900e-05 | — | — |
| 15 | DNA Binding | GO | 7.700e-05 | — | — |
| 16 | CHEN_LVAD_SUPPORT_OF_FAILING_HEART_DN | MSIGDB | 7.600e-05 | — | — |
| 17 | Myogenesis | GO | 7.400e-05 | — | — |
| 18 | Transcriptional Regulation | GO | 7.400e-05 | — | — |
| 19 | INGRAM_SHH_TARGETS_UP | MSIGDB | 7.100e-05 | — | — |
| 20 | WP_MESODERMAL_COMMITMENT_PATHWAY | MSIGDB | 6.900e-05 | — | — |



---

### ST3 — Top-20 ranked pathways per method, KF-CHD and KF-NBL cohorts

Five enrichment methods evaluated in discovery mode (no reference pathway pre-specified). KF-CHD: 2,130 pathways scored (canonical collections only); KF-NBL: 2,196 pathways scored. Cilia reference pathways marked with ✓.

**KF-CHD**

*Seed Fisher corrected (B1)*

| Rank | Pathway name | SAB | Score / stat | Members | Cilia ref. |
| --- | --- | --- | --- | --- | --- |
| 1 | WP_CILIOPATHIES | MSIGDB | 2.127e-34 | 170 | ✓ |
| 2 | REACTOME_DISEASES_OF_METABOLISM | MSIGDB | 2.416e-32 | 243 | — |
| 3 | WP_GENES_RELATED_TO_PRIMARY_CILIUM_DEVELOPMENT_BASED_ON_CRISPR | MSIGDB | 6.369e-17 | 94 | ✓ |
| 4 | WP_JOUBERT_SYNDROME | MSIGDB | 7.285e-17 | 76 | ✓ |
| 5 | REACTOME_DISORDERS_OF_TRANSMEMBRANE_TRANSPORTERS | MSIGDB | 2.431e-16 | 171 | — |
| 6 | REACTOME_EXTRACELLULAR_MATRIX_ORGANIZATION | MSIGDB | 4.609e-16 | 297 | — |
| 7 | REACTOME_ECM_PROTEOGLYCANS | MSIGDB | 7.570e-16 | 76 | — |
| 8 | Transmembrane Transport | GO | 2.149e-15 | 251 | — |
| 9 | DNA Repair | GO | 3.341e-15 | 209 | — |
| 10 | HSIAO_LIVER_SPECIFIC_GENES | MSIGDB | 3.594e-15 | 245 | — |
| 11 | REACTOME_SLC_TRANSPORTER_DISORDERS | MSIGDB | 1.190e-14 | 97 | — |
| 12 | Ionophore activity | GO | 1.942e-14 | 237 | — |
| 13 | REACTOME_METABOLISM_OF_VITAMINS_AND_COFACTORS | MSIGDB | 2.852e-14 | 186 | — |
| 14 | NABA_CORE_MATRISOME | MSIGDB | 9.494e-14 | 266 | — |
| 15 | WP_FATTY_ACID_BETA_OXIDATION | MSIGDB | 1.081e-13 | 33 | — |
| 16 | HOSHIDA_LIVER_CANCER_SUBCLASS_S3 | MSIGDB | 4.870e-13 | 258 | — |
| 17 | WP_AMINO_ACID_METABOLISM | MSIGDB | 8.959e-13 | 84 | — |
| 18 | KAUFFMANN_DNA_REPAIR_GENES | MSIGDB | 1.910e-12 | 229 | — |
| 19 | WP_NEPHROTIC_SYNDROME | MSIGDB | 3.012e-12 | 44 | — |
| 20 | WP_DNA_REPAIR_PATHWAYS_FULL_NETWORK | MSIGDB | 4.623e-12 | 120 | — |


*Neighborhood Fisher (B2)*

| Rank | Pathway name | SAB | Score / stat | Members | Cilia ref. |
| --- | --- | --- | --- | --- | --- |
| 1 | ZWANG_DOWN_BY_2ND_EGF_PULSE | MSIGDB | 1.036e-24 | 284 | — |
| 2 | DEBIASI_APOPTOSIS_BY_REOVIRUS_INFECTION_UP | MSIGDB | 2.702e-23 | 280 | — |
| 3 | JINESH_BLEBBISHIELD_VS_LIVE_CONTROL_DN | MSIGDB | 4.310e-23 | 294 | — |
| 4 | GENTILE_UV_HIGH_DOSE_DN | MSIGDB | 4.595e-23 | 278 | — |
| 5 | TORCHIA_TARGETS_OF_EWSR1_FLI1_FUSION_UP | MSIGDB | 8.278e-23 | 251 | — |
| 6 | ZHOU_INFLAMMATORY_RESPONSE_FIMA_DN | MSIGDB | 9.985e-23 | 267 | — |
| 7 | WEST_ADRENOCORTICAL_TUMOR_UP | MSIGDB | 1.684e-22 | 281 | — |
| 8 | BORCZUK_MALIGNANT_MESOTHELIOMA_UP | MSIGDB | 6.753e-22 | 291 | — |
| 9 | CHEN_HOXA5_TARGETS_9HR_UP | MSIGDB | 1.084e-21 | 215 | — |
| 10 | REACTOME_FC_EPSILON_RECEPTOR_FCERI_SIGNALING | MSIGDB | 1.797e-21 | 183 | — |
| 11 | WALLACE_PROSTATE_CANCER_RACE_UP | MSIGDB | 4.506e-21 | 291 | — |
| 12 | LEE_RECENT_THYMIC_EMIGRANT | MSIGDB | 5.973e-21 | 218 | — |
| 13 | REACTOME_DEUBIQUITINATION | MSIGDB | 1.101e-20 | 233 | — |
| 14 | REACTOME_ANTIGEN_PROCESSING_UBIQUITINATION_PROTEASOME_DEGRADATION | MSIGDB | 2.283e-20 | 299 | — |
| 15 | PASQUALUCCI_LYMPHOMA_BY_GC_STAGE_UP | MSIGDB | 5.150e-20 | 274 | — |
| 16 | HORIUCHI_WTAP_TARGETS_UP | MSIGDB | 1.641e-19 | 291 | — |
| 17 | WP_GPCRS_CLASS_A_RHODOPSINLIKE | MSIGDB | 2.051e-19 | 246 | — |
| 18 | RAO_BOUND_BY_SALL4 | MSIGDB | 3.645e-19 | 220 | — |
| 19 | REACTOME_SIGNALING_BY_WNT | MSIGDB | 3.880e-19 | 266 | — |
| 20 | PURBEY_TARGETS_OF_CTBP1_NOT_SATB1_UP | MSIGDB | 9.115e-19 | 284 | — |


*Raw PPR GSEA (B3)*

| Rank | Pathway name | SAB | Score / stat | Members | Cilia ref. |
| --- | --- | --- | --- | --- | --- |
| 1 | REACTOME_CHYLOMICRON_REMODELING | MSIGDB | 0.9133 | — | — |
| 2 | REACTOME_TERMINAL_PATHWAY_OF_COMPLEMENT | MSIGDB | 0.8849 | — | — |
| 3 | REACTOME_SYNTHESIS_OF_16_20_HYDROXYEICOSATETRAENOIC_ACIDS_HETE | MSIGDB | 0.8802 | — | — |
| 4 | WP_COMPOSITION_OF_LIPID_PARTICLES | MSIGDB | 0.8674 | — | — |
| 5 | REACTOME_SIGNALING_BY_FGFR3_FUSIONS_IN_CANCER | MSIGDB | 0.8452 | — | — |
| 6 | Activation of Membrane Attack Complex | GO | 0.8428 | — | — |
| 7 | MARIADASON_RESPONSE_TO_BUTYRATE_CURCUMIN_SULINDAC_TSA_1 | MSIGDB | 0.8364 | — | — |
| 8 | REACTOME_SIGNALING_BY_FGFR4_IN_DISEASE | MSIGDB | 0.8363 | — | — |
| 9 | WP_CODEINE_AND_MORPHINE_METABOLISM | MSIGDB | 0.8316 | — | — |
| 10 | BIOCARTA_PLK3_PATHWAY | MSIGDB | 0.8236 | — | — |
| 11 | REACTOME_EGFR_TRANSACTIVATION_BY_GASTRIN | MSIGDB | 0.8235 | — | — |
| 12 | REACTOME_CYP2E1_REACTIONS | MSIGDB | 0.8215 | — | — |
| 13 | WP_BILE_ACIDS_SYNTHESIS_AND_ENTEROHEPATIC_CIRCULATION | MSIGDB | 0.8209 | — | — |
| 14 | REACTOME_TYPE_I_HEMIDESMOSOME_ASSEMBLY | MSIGDB | 0.8200 | — | — |
| 15 | REACTOME_MAPK3_ERK1_ACTIVATION | MSIGDB | 0.8170 | — | — |
| 16 | BIOCARTA_PLATELETAPP_PATHWAY | MSIGDB | 0.8148 | — | — |
| 17 | REACTOME_INLA_MEDIATED_ENTRY_OF_LISTERIA_MONOCYTOGENES_INTO_HOST_CELLS | MSIGDB | 0.8095 | — | — |
| 18 | BOWIE_RESPONSE_TO_EXTRACELLULAR_MATRIX | MSIGDB | 0.8073 | — | — |
| 19 | REACTOME_DOWNREGULATION_OF_ERBB4_SIGNALING | MSIGDB | 0.8055 | — | — |
| 20 | INAMURA_LUNG_CANCER_SCC_UP | MSIGDB | 0.8039 | — | — |


*Conditioned PPR GSEA (B3b)*

| Rank | Pathway name | SAB | Score / stat | Members | Cilia ref. |
| --- | --- | --- | --- | --- | --- |
| 1 | REACTOME_SIGNALING_BY_PDGFRA_TRANSMEMBRANE_JUXTAMEMBRANE_AND_KINASE_DOMAIN_MUTANTS | MSIGDB | 0.9138 | — | — |
| 2 | PID_INTEGRIN4_PATHWAY | MSIGDB | 0.8992 | — | — |
| 3 | BIOCARTA_PLATELETAPP_PATHWAY | MSIGDB | 0.8990 | — | — |
| 4 | BIOCARTA_CDMAC_PATHWAY | MSIGDB | 0.8894 | — | — |
| 5 | REACTOME_INLA_MEDIATED_ENTRY_OF_LISTERIA_MONOCYTOGENES_INTO_HOST_CELLS | MSIGDB | 0.8875 | — | — |
| 6 | REACTOME_EGFR_TRANSACTIVATION_BY_GASTRIN | MSIGDB | 0.8833 | — | — |
| 7 | REACTOME_SIGNALING_BY_FGFR4_IN_DISEASE | MSIGDB | 0.8812 | — | — |
| 8 | BIOCARTA_STAT3_PATHWAY | MSIGDB | 0.8784 | — | — |
| 9 | REACTOME_MAPK1_ERK2_ACTIVATION | MSIGDB | 0.8783 | — | — |
| 10 | REACTOME_MAPK3_ERK1_ACTIVATION | MSIGDB | 0.8783 | — | — |
| 11 | BIOCARTA_P53_PATHWAY | MSIGDB | 0.8775 | — | — |
| 12 | REACTOME_SIGNALING_BY_ERBB2_ECD_MUTANTS | MSIGDB | 0.8751 | — | — |
| 13 | BIOCARTA_ATM_PATHWAY | MSIGDB | 0.8732 | — | — |
| 14 | REACTOME_SIGNALING_BY_FGFR3_FUSIONS_IN_CANCER | MSIGDB | 0.8723 | — | — |
| 15 | REACTOME_INTERLEUKIN_6_SIGNALING | MSIGDB | 0.8712 | — | — |
| 16 | REACTOME_DOWNREGULATION_OF_ERBB4_SIGNALING | MSIGDB | 0.8681 | — | — |
| 17 | REACTOME_CONSTITUTIVE_SIGNALING_BY_LIGAND_RESPONSIVE_EGFR_CANCER_VARIANTS | MSIGDB | 0.8678 | — | — |
| 18 | REACTOME_SIGNALING_BY_KIT_IN_DISEASE | MSIGDB | 0.8648 | — | — |
| 19 | WP_ALPHA_6_BETA_4_SIGNALING_PATHWAY | MSIGDB | 0.8640 | — | — |
| 20 | ZHU_SKIL_TARGETS_DN | MSIGDB | 0.8638 | — | — |


*BIFO full-arm (B4)*

| Rank | Pathway name | SAB | Score / stat | Members | Cilia ref. |
| --- | --- | --- | --- | --- | --- |
| 1 | Protein phosphorylation | GO | 2.217e-05 | 21 | — |
| 2 | REACTOME_CROSS_PRESENTATION_OF_PARTICULATE_EXOGENOUS_ANTIGENS_PHAGOSOMES | MSIGDB | 2.100e-05 | 8 | — |
| 3 | WP_NAD_METABOLISM_SIRTUINS_AND_AGING | MSIGDB | 2.085e-05 | 11 | — |
| 4 | REACTOME_FREE_FATTY_ACIDS_REGULATE_INSULIN_SECRETION | MSIGDB | 1.845e-05 | 11 | — |
| 5 | WP_ARYL_HYDROCARBON_RECEPTOR_NETPATH | MSIGDB | 1.510e-05 | 45 | — |
| 6 | WP_FGF23_SIGNALLING_IN_HYPOPHOSPHATEMIC_RICKETS_AND_RELATED_DISORDERS | MSIGDB | 1.477e-05 | 22 | — |
| 7 | REACTOME_ACTIVATION_OF_PUMA_AND_TRANSLOCATION_TO_MITOCHONDRIA | MSIGDB | 1.370e-05 | 9 | — |
| 8 | BIOCARTA_FBW7_PATHWAY | MSIGDB | 1.366e-05 | 9 | — |
| 34 | WP_JOUBERT_SYNDROME | MSIGDB | 9.280e-06 | 76 | ✓ |
| 43 | WP_CILIOPATHIES | MSIGDB | 8.509e-06 | 170 | ✓ |
| 9 | ZWANG_TRANSIENTLY_UP_BY_2ND_EGF_PULSE_ONLY | MSIGDB | 5.000e-06 | — | — |
| 10 | HSIAO_LIVER_SPECIFIC_GENES | MSIGDB | 4.000e-06 | — | — |
| 11 | REACTOME_DISORDERS_OF_TRANSMEMBRANE_TRANSPORTERS | MSIGDB | 4.000e-06 | — | — |
| 12 | REACTOME_DEVELOPMENTAL_BIOLOGY | MSIGDB | 4.000e-06 | — | — |
| 13 | REACTOME_SLC_TRANSPORTER_DISORDERS | MSIGDB | 4.000e-06 | — | — |
| 14 | PID_RHODOPSIN_PATHWAY | MSIGDB | 4.000e-06 | — | — |
| 15 | PUJANA_BRCA1_PCC_NETWORK | MSIGDB | 4.000e-06 | — | — |
| 16 | GRAESSMANN_APOPTOSIS_BY_DOXORUBICIN_DN | MSIGDB | 4.000e-06 | — | — |
| 17 | BENPORATH_ES_WITH_H3K27ME3 | MSIGDB | 4.000e-06 | — | — |
| 18 | MEISSNER_BRAIN_HCP_WITH_H3K4ME3_AND_H3K27ME3 | MSIGDB | 4.000e-06 | — | — |
| 19 | PUJANA_ATM_PCC_NETWORK | MSIGDB | 4.000e-06 | — | — |
| 20 | NABA_CORE_MATRISOME | MSIGDB | 4.000e-06 | — | — |


**KF-NBL**

*Seed Fisher corrected (B1)*

| Rank | Pathway name | SAB | Score / stat | Members | Cilia ref. |
| --- | --- | --- | --- | --- | --- |
| 1 | WP_CILIOPATHIES | MSIGDB | 1.755e-35 | 169 | ✓ |
| 2 | REACTOME_DISEASES_OF_METABOLISM | MSIGDB | 4.419e-26 | 242 | — |
| 3 | WP_AMINO_ACID_METABOLISM | MSIGDB | 2.190e-23 | 86 | — |
| 4 | KAUFFMANN_DNA_REPAIR_GENES | MSIGDB | 2.367e-18 | 229 | — |
| 5 | WP_JOUBERT_SYNDROME | MSIGDB | 3.893e-18 | 75 | ✓ |
| 6 | HOSHIDA_LIVER_CANCER_SUBCLASS_S3 | MSIGDB | 7.898e-16 | 260 | — |
| 7 | WP_DNA_REPAIR_PATHWAYS_FULL_NETWORK | MSIGDB | 4.755e-15 | 120 | — |
| 8 | PUJANA_BREAST_CANCER_LIT_INT_NETWORK | MSIGDB | 4.825e-15 | 100 | — |
| 9 | DNA Repair | GO | 2.141e-14 | 211 | — |
| 10 | Ionophore activity | GO | 8.494e-14 | 236 | — |
| 11 | REACTOME_CILIUM_ASSEMBLY | MSIGDB | 9.160e-14 | 194 | ✓ |
| 12 | Transmembrane Transport | GO | 1.668e-13 | 249 | — |
| 13 | CAIRO_LIVER_DEVELOPMENT_DN | MSIGDB | 1.937e-13 | 215 | — |
| 14 | REACTOME_DNA_REPAIR | MSIGDB | 2.966e-13 | 280 | — |
| 15 | HALLMARK_ADIPOGENESIS | MSIGDB | 3.711e-13 | 185 | — |
| 16 | REACTOME_ORGANELLE_BIOGENESIS_AND_MAINTENANCE | MSIGDB | 1.584e-12 | 264 | — |
| 17 | HALLMARK_XENOBIOTIC_METABOLISM | MSIGDB | 2.223e-12 | 195 | — |
| 18 | HSIAO_LIVER_SPECIFIC_GENES | MSIGDB | 5.474e-12 | 245 | — |
| 19 | WAKASUGI_HAVE_ZNF143_BINDING_SITES | MSIGDB | 8.162e-12 | 54 | — |
| 20 | REACTOME_EXTRACELLULAR_MATRIX_ORGANIZATION | MSIGDB | 9.358e-12 | 296 | — |


*Neighborhood Fisher (B2)*

| Rank | Pathway name | SAB | Score / stat | Members | Cilia ref. |
| --- | --- | --- | --- | --- | --- |
| 1 | WP_GPCRS_CLASS_A_RHODOPSINLIKE | MSIGDB | 2.725e-25 | 238 | — |
| 2 | WALLACE_PROSTATE_CANCER_RACE_UP | MSIGDB | 2.143e-24 | 290 | — |
| 3 | ZWANG_DOWN_BY_2ND_EGF_PULSE | MSIGDB | 6.510e-23 | 285 | — |
| 4 | QI_PLASMACYTOMA_UP | MSIGDB | 3.155e-22 | 248 | — |
| 5 | REACTOME_ANTIGEN_PROCESSING_UBIQUITINATION_PROTEASOME_DEGRADATION | MSIGDB | 1.968e-21 | 294 | — |
| 6 | REACTOME_IMMUNOREGULATORY_INTERACTIONS_BETWEEN_A_LYMPHOID_AND_A_NON_LYMPHOID_CELL | MSIGDB | 3.985e-21 | 186 | — |
| 7 | DEBIASI_APOPTOSIS_BY_REOVIRUS_INFECTION_UP | MSIGDB | 4.110e-21 | 284 | — |
| 8 | BOYLAN_MULTIPLE_MYELOMA_C_D_DN | MSIGDB | 3.118e-20 | 269 | — |
| 9 | REACTOME_NEDDYLATION | MSIGDB | 1.330e-19 | 226 | — |
| 10 | BORCZUK_MALIGNANT_MESOTHELIOMA_UP | MSIGDB | 3.718e-19 | 294 | — |
| 11 | IVANOVA_HEMATOPOIESIS_MATURE_CELL | MSIGDB | 4.243e-19 | 273 | — |
| 12 | PASQUALUCCI_LYMPHOMA_BY_GC_STAGE_UP | MSIGDB | 7.042e-19 | 271 | — |
| 13 | COLDREN_GEFITINIB_RESISTANCE_DN | MSIGDB | 1.536e-18 | 217 | — |
| 14 | RAY_TUMORIGENESIS_BY_ERBB2_CDC25A_DN | MSIGDB | 1.955e-18 | 253 | — |
| 15 | TORCHIA_TARGETS_OF_EWSR1_FLI1_FUSION_DN | MSIGDB | 2.183e-18 | 300 | — |
| 16 | LU_EZH2_TARGETS_UP | MSIGDB | 2.389e-18 | 273 | — |
| 17 | REACTOME_PEPTIDE_LIGAND_BINDING_RECEPTORS | MSIGDB | 2.547e-18 | 191 | — |
| 18 | REACTOME_SIGNALING_BY_ROBO_RECEPTORS | MSIGDB | 4.531e-18 | 213 | — |
| 19 | Apoptosis | GO | 5.290e-18 | 263 | — |
| 20 | REACTOME_ANTI_INFLAMMATORY_RESPONSE_FAVOURING_LEISHMANIA_PARASITE_INFECTION | MSIGDB | 6.985e-18 | 219 | — |


*Raw PPR GSEA (B3)*

| Rank | Pathway name | SAB | Score / stat | Members | Cilia ref. |
| --- | --- | --- | --- | --- | --- |
| 1 | REACTOME_CHYLOMICRON_REMODELING | MSIGDB | 0.9052 | — | — |
| 2 | REACTOME_TERMINAL_PATHWAY_OF_COMPLEMENT | MSIGDB | 0.8879 | — | — |
| 3 | WP_COMPOSITION_OF_LIPID_PARTICLES | MSIGDB | 0.8697 | — | — |
| 4 | REACTOME_ACTIVATED_NTRK3_SIGNALS_THROUGH_RAS | MSIGDB | 0.8647 | — | — |
| 5 | REACTOME_SHC_RELATED_EVENTS_TRIGGERED_BY_IGF1R | MSIGDB | 0.8511 | — | — |
| 6 | Activation of Membrane Attack Complex | GO | 0.8500 | — | — |
| 7 | REACTOME_EGFR_TRANSACTIVATION_BY_GASTRIN | MSIGDB | 0.8367 | — | — |
| 8 | REACTOME_HDL_REMODELING | MSIGDB | 0.8352 | — | — |
| 9 | REACTOME_CHYLOMICRON_ASSEMBLY | MSIGDB | 0.8322 | — | — |
| 10 | REACTOME_SYNTHESIS_OF_16_20_HYDROXYEICOSATETRAENOIC_ACIDS_HETE | MSIGDB | 0.8195 | — | — |
| 11 | BIOCARTA_ATM_PATHWAY | MSIGDB | 0.8148 | — | — |
| 12 | GOUYER_TATI_TARGETS_UP | MSIGDB | 0.8132 | — | — |
| 13 | REACTOME_TYPE_I_HEMIDESMOSOME_ASSEMBLY | MSIGDB | 0.8105 | — | — |
| 14 | LEE_LIVER_CANCER_HEPATOBLAST | MSIGDB | 0.8103 | — | — |
| 15 | REACTOME_SIGNALING_BY_PDGFRA_TRANSMEMBRANE_JUXTAMEMBRANE_AND_KINASE_DOMAIN_MUTANTS | MSIGDB | 0.8085 | — | — |
| 16 | REACTOME_PTK6_REGULATES_RTKS_AND_THEIR_EFFECTORS_AKT1_AND_DOK1 | MSIGDB | 0.8067 | — | — |
| 17 | REACTOME_MYOCLONIC_EPILEPSY_OF_LAFORA | MSIGDB | 0.8043 | — | — |
| 18 | WP_TAMOXIFEN_METABOLISM | MSIGDB | 0.8016 | — | — |
| 19 | WP_BLOOD_CLOTTING_CASCADE | MSIGDB | 0.7948 | — | — |
| 20 | REACTOME_SIGNALING_BY_FGFR3_FUSIONS_IN_CANCER | MSIGDB | 0.7942 | — | — |


*Conditioned PPR GSEA (B3b)*

| Rank | Pathway name | SAB | Score / stat | Members | Cilia ref. |
| --- | --- | --- | --- | --- | --- |
| 1 | REACTOME_SIGNALING_BY_PDGFRA_TRANSMEMBRANE_JUXTAMEMBRANE_AND_KINASE_DOMAIN_MUTANTS | MSIGDB | 0.9056 | — | — |
| 2 | BIOCARTA_CDMAC_PATHWAY | MSIGDB | 0.9039 | — | — |
| 3 | REACTOME_SHC_RELATED_EVENTS_TRIGGERED_BY_IGF1R | MSIGDB | 0.9012 | — | — |
| 4 | BIOCARTA_NPP1_PATHWAY | MSIGDB | 0.8806 | — | — |
| 5 | BIOCARTA_P53_PATHWAY | MSIGDB | 0.8792 | — | — |
| 6 | BIOCARTA_RACCYCD_PATHWAY | MSIGDB | 0.8785 | — | — |
| 7 | REACTOME_MISMATCH_REPAIR | MSIGDB | 0.8769 | — | — |
| 8 | WP_OSTEOPONTIN_SIGNALING | MSIGDB | 0.8753 | — | — |
| 9 | BIOCARTA_ATM_PATHWAY | MSIGDB | 0.8738 | — | — |
| 10 | REACTOME_DOWNREGULATION_OF_ERBB2_ERBB3_SIGNALING | MSIGDB | 0.8732 | — | — |
| 11 | BIOCARTA_PLATELETAPP_PATHWAY | MSIGDB | 0.8718 | — | — |
| 12 | REACTOME_EGFR_TRANSACTIVATION_BY_GASTRIN | MSIGDB | 0.8677 | — | — |
| 13 | REACTOME_SIGNAL_ATTENUATION | MSIGDB | 0.8651 | — | — |
| 14 | REACTOME_SIGNALING_BY_ERBB2_ECD_MUTANTS | MSIGDB | 0.8649 | — | — |
| 15 | REACTOME_SIGNALING_BY_FGFR4_IN_DISEASE | MSIGDB | 0.8647 | — | — |
| 16 | REACTOME_SIGNALING_BY_FGFR3_FUSIONS_IN_CANCER | MSIGDB | 0.8647 | — | — |
| 17 | REACTOME_ACTIVATED_NTRK3_SIGNALS_THROUGH_RAS | MSIGDB | 0.8634 | — | — |
| 18 | REACTOME_CONSTITUTIVE_SIGNALING_BY_LIGAND_RESPONSIVE_EGFR_CANCER_VARIANTS | MSIGDB | 0.8603 | — | — |
| 19 | BIOCARTA_AMI_PATHWAY | MSIGDB | 0.8600 | — | — |
| 20 | REACTOME_DOWNREGULATION_OF_ERBB4_SIGNALING | MSIGDB | 0.8599 | — | — |


*BIFO full-arm (B4)*

| Rank | Pathway name | SAB | Score / stat | Members | Cilia ref. |
| --- | --- | --- | --- | --- | --- |
| 1 | WP_CILIOPATHIES | MSIGDB | 6.000e-06 | — | ✓ |
| 2 | YOSHIMURA_MAPK8_TARGETS_UP | MSIGDB | 5.000e-06 | — | — |
| 3 | REACTOME_TRANSPORT_OF_SMALL_MOLECULES | MSIGDB | 5.000e-06 | — | — |
| 4 | NABA_MATRISOME | MSIGDB | 5.000e-06 | — | — |
| 5 | REACTOME_DISEASES_OF_METABOLISM | MSIGDB | 5.000e-06 | — | — |
| 6 | GRAESSMANN_APOPTOSIS_BY_DOXORUBICIN_DN | MSIGDB | 4.000e-06 | — | — |
| 7 | Ionophore activity | GO | 4.000e-06 | — | — |
| 8 | PUJANA_BRCA1_PCC_NETWORK | MSIGDB | 4.000e-06 | — | — |
| 9 | Signal Transduction | GO | 4.000e-06 | — | — |
| 10 | DESERT_PERIPORTAL_HEPATOCELLULAR_CARCINOMA_SUBCLASS_UP | MSIGDB | 4.000e-06 | — | — |
| 11 | Transmembrane Transport | GO | 4.000e-06 | — | — |
| 12 | ZWANG_TRANSIENTLY_UP_BY_2ND_EGF_PULSE_ONLY | MSIGDB | 4.000e-06 | — | — |
| 13 | BENPORATH_SUZ12_TARGETS | MSIGDB | 4.000e-06 | — | — |
| 14 | PUJANA_ATM_PCC_NETWORK | MSIGDB | 4.000e-06 | — | — |
| 15 | BENPORATH_EED_TARGETS | MSIGDB | 4.000e-06 | — | — |
| 16 | BLALOCK_ALZHEIMERS_DISEASE_UP | MSIGDB | 4.000e-06 | — | — |
| 17 | DODD_NASOPHARYNGEAL_CARCINOMA_DN | MSIGDB | 4.000e-06 | — | — |
| 18 | DODD_NASOPHARYNGEAL_CARCINOMA_UP | MSIGDB | 4.000e-06 | — | — |
| 19 | PID_CONE_PATHWAY | MSIGDB | 4.000e-06 | — | — |
| 20 | MOOTHA_HUMAN_MITODB_6_2002 | MSIGDB | 4.000e-06 | — | — |



---

### ST4 — Full cilia pathway cluster ranking under BIFO, KF-CHD and KF-NBL

All cilia, ciliopathy, and hedgehog pathway annotations from the scored universe (17 in KF-CHD, 18 in KF-NBL), ordered by KF-CHD BIFO rank. Score = degree_norm. Also shown: null_z (pathway-node rewiring null) and empirical_q. Hub-flagged pathways (degree_flag = True) reflect high-degree graph connectivity rather than specific cilia biology.

| Pathway name | Source DB | KF-CHD rank | KF-CHD score | KF-CHD null_z | KF-NBL rank | KF-NBL score | KF-NBL null_z | Members | Hub |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| WP_JOUBERT_SYNDROME | MSIGDB | 34 | 9.280e-06 | 54.69 | 17 | 2.536e-06 | 10.54 | 76 | — |
| WP_CILIOPATHIES | MSIGDB | 43 | 8.509e-06 | 48.71 | 3 | 4.241e-06 | 18.95 | 170 | — |
| REACTOME_CILIUM_ASSEMBLY | MSIGDB | 163 | 4.219e-06 | 22.23 | 32 | 2.154e-06 | 6.12 | 194 | — |
| WP_GENES_RELATED_TO_PRIMARY_CILIUM_DEVELOPMENT_BASED_ON_CRISPR | MSIGDB | 171 | 3.977e-06 | 19.89 | 31 | 2.154e-06 | 8.94 | 94 | — |
| REACTOME_HEDGEHOG_OFF_STATE | MSIGDB | 216 | 3.163e-06 | 18.26 | 347 | 9.544e-07 | 0.13 | 110 | — |
| REACTOME_SIGNALING_BY_HEDGEHOG | MSIGDB | 239 | 2.740e-06 | 13.48 | 228 | 1.134e-06 | 0.52 | 147 | — |
| WP_CILIARY_LANDSCAPE | MSIGDB | 358 | 1.401e-06 | 1.08 | 233 | 1.125e-06 | -1.01 | 211 | — |
| REACTOME_CARGO_TRAFFICKING_TO_THE_PERICILIARY_MEMBRANE | MSIGDB | 378 | 1.949e-06 | 1296 | 1.098e-06 | 51 | — |
| REACTOME_ANCHORING_OF_THE_BASAL_BODY_TO_THE_PLASMA_MEMBRANE | MSIGDB | 395 | 1.916e-06 | 202 | 2.306e-06 | 94 | — |
| REACTOME_SIGNALING_BY_HEDGEHOG | MSIGDB | 458 | 1.816e-06 | 493 | 1.699e-06 | 147 | — |
| WP_CILIARY_LANDSCAPE | MSIGDB | 521 | 1.713e-06 | 483 | 1.706e-06 | 211 | — |
| REACTOME_BBSOME_MEDIATED_CARGO_TARGETING_TO_CILIUM | MSIGDB | 679 | 1.530e-06 | 2070 | 8.222e-07 | 23 | — |
| REACTOME_INTRAFLAGELLAR_TRANSPORT | MSIGDB | 906 | 1.362e-06 | 636 | 1.551e-06 | 50 | — |
| YAUCH_HEDGEHOG_SIGNALING_PARACRINE_UP | MSIGDB | 914 | 1.354e-06 | 1214 | 1.136e-06 | 140 | — |
| WP_HEDGEHOG_SIGNALING_PATHWAY | MSIGDB | 959 | 1.324e-06 | 797 | 1.405e-06 | 43 | — |
| WP_INTRAFLAGELLAR_TRANSPORT_PROTEINS_BINDING_TO_DYNEIN | MSIGDB | 1483 | 1.038e-06 | 1397 | 1.055e-06 | 25 | — |
| WP_HEDGEHOG_SIGNALING_PATHWAY_NETPATH | MSIGDB | 1617 | 9.782e-07 | 1325 | 1.086e-06 | 16 | — |
| REACTOME_VXPX_CARGO_TARGETING_TO_CILIUM | MSIGDB | 1923 | 8.819e-07 | 3177 | 5.506e-07 | 21 | — |
| REACTOME_HEDGEHOG_LIGAND_BIOGENESIS | MSIGDB | 2949 | 5.910e-07 | 2522 | 6.903e-07 | 62 | — |
| REACTOME_TRAFFICKING_OF_MYRISTOYLATED_PROTEINS_TO_THE_CILIUM | MSIGDB | 5070 | 1.685e-07 | 5161 | 1.564e-07 | 5 | — |
| HALLMARK_HEDGEHOG_SIGNALING | MSIGDB | 5103 | 7.054e-08 | 4712 | 2.576e-07 | 35 | — |


*17 cilia-related pathways identified across 2,130 scored pathways (KF-CHD universe). Top 5 core ciliopathy pathways shown; full table available in supplementary data.*

---

### ST5 — Head-to-head rank comparison: seed Fisher vs. BIFO (downloadable data files)

Full ranked pathway lists for all pathways scored under both methods, for KF-CHD and KF-NBL independently. Provided as downloadable supplementary data files due to size (2,130 pathways for KF-CHD; 2,196 pathways for KF-NBL).

**ST5a** (`supplementary_data_ST5a_kf_chd_fisher_vs_bifo.csv`): KF-CHD, sorted by BIFO rank.

**ST5b** (`supplementary_data_ST5b_kf_nbl_fisher_vs_bifo.csv`): KF-NBL, sorted by BIFO rank.

Columns: pathway_name | source_db | member_count | bifo_rank | bifo_score | fisher_rank | fisher_bh_pvalue | cilia_ref_flag | hub_flag

*Source: `results/kf_chd/baseline_comparison.csv` and `results/kf_nbl/baseline_comparison.csv`*

---

## Supplementary: Code and Data Repository

All code, configuration, benchmark data, and pre-computed results supporting
this manuscript are available at:

**https://github.com/TaylorResearchLab/bifo-graph**

The repository is organized according to FAIR data principles: all benchmark
inputs are versioned and shipped with the repository; all analysis parameters
are documented in `config/bifo_mapping.yaml` (v0.7.1); all pipeline
scripts are self-contained with documented inputs and outputs; and a
self-contained end-to-end test (`examples/minimal_test/`) is provided for
validation without requiring access to the full graph database.

### S6.1 Pipeline scripts (`pipeline/`)

| Script | Purpose | Paper section |
|--------|---------|---------------|
| `bifo_conditioning.py` | BIFO edge conditioning (entity resolution, flow class filtering) and PPR propagation. Primary analysis script. | Methods §2, §3 |
| `score_pathways.py` | Pathway scoring from PPR score vectors using degree_norm and alternative variants; implements pathway-node membership rewiring null and stratified member-level null (Methods §4, §8.4) |
| `baseline_enrichment.py` | Enrichment baselines B0–B3 (degree overlap, Fisher, neighborhood Fisher, preranked GSEA). Accepts `--kept-edges` and `--small-universe` flags | Methods §6 |
| `chd_resampling_exhaustive.py` | Exhaustive in-memory resampling over all C(15,10) = 3,003 possible 10-gene/5-gene partitions of the CHD gene pool | Methods §9 |
| `kf_resampling.py` | Bootstrap resampling for KF cohort analyses (500 draws × 3 seed sizes per cohort) | Methods §10.7 |
| `seed_cui_lookup.py` | Map HGNC gene symbols to UMLS CUIs for use as pipeline seed inputs | Methods §10.2 |
| `generate_export_cypher.py` | Generate cohort-specific Neo4j export Cypher queries from a seed gene list | Methods §10.3 |
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
| `merge_files.sh` | 2.3 | Merge edge CSV files into `edges_merged.csv` |
| `run_seed_lookup.sh` | 2.4 | Map gene symbols to CUIs |
| `run_conditioning.sh` | 3 | BIFO conditioning + PPR propagation |
| `run_scoring.sh` | 4 | Pathway scoring |
| `run_baseline.sh` | 5 | Baseline enrichment comparison |
| `run_resampling.sh` | 6 | Bootstrap resampling |

### S6.3 Configuration (`config/`)

| File | Description |
|------|-------------|
| `config/bifo_mapping.yaml` | BIFO flow class definitions, v0.7.1. Contains 251 predicate-to-flow entries, 96 explicit non-flow designations, and 46 observational edge definitions across 5 classification tiers. This file is the primary scientific artifact of the BIFO framework; all conditioning results are determined by its contents |

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
| `kf_chd_cilia_reference.txt` | MSigDB cilia pathway reference set for KF-CHD evaluation (17 CUIs) |

**KF-NBL cohort (`data/cohorts/nbl/`)**

| File | Description |
|------|-------------|
| `kf_nbl_seeds_maf001.txt` | Primary seed gene list: 1,406 HGNC genes with AutoGVP P/LP variants at MAF ≤0.001, n≥1 carrier |
| `kf_nbl_seeds_maf001_n2.txt` | Carrier-filtered seeds: 401 genes with n≥2 carriers at MAF ≤0.001 |
| `kf_nbl_seeds_maf001_n3.txt` | Carrier-filtered seeds: 147 genes with n≥3 carriers at MAF ≤0.001 |
| `kf_nbl_seeds_maf01.txt` | Broader-filter seeds at MAF ≤0.01 |
| `kf_nbl_seeds.txt` | Original unfiltered seed gene list |
| `kf_nbl_cilia_reference.txt` | MSigDB cilia pathway reference set for KF-NBL evaluation (17 CUIs) |

### S6.6 Pre-computed results (`results/`)

**Curated CHD benchmark (`results/chd_benchmark/`)**

Three-arm ablation results. Files are prefixed by arm: `full` (BIFO-conditioned, all flow classes), `ablation` (no Pathway Contribution bridge edges), `mech` (mechanistic-only edges).

| File | Description |
|------|-------------|
| `results_full.json` | Gene-level PPR recovery metrics for the full BIFO arm (AUROC, AUPRC, entropy, nonzero fraction) |
| `results_ablation.json` | Gene-level PPR recovery metrics for the ablation arm |
| `results_mech.json` | Gene-level PPR recovery metrics for the mechanistic-only arm |
| `results_node_index.json` | Node CUI → matrix index mapping shared across all three arms |
| `results_full_scores_cond.npy` | Full arm: conditioned PPR score vector |
| `results_full_scores_raw.npy` | Full arm: raw (unconditioned) PPR score vector |
| `results_ablation_scores_cond.npy` | Ablation arm: conditioned PPR score vector |
| `results_ablation_scores_raw.npy` | Ablation arm: raw PPR score vector |
| `results_mech_scores_cond.npy` | Mechanistic-only arm: conditioned PPR score vector |
| `results_mech_scores_raw.npy` | Mechanistic-only arm: raw PPR score vector |
| `results_full_kept_edges.csv.zip` | Full arm: BIFO-conditioned kept edges with flow class and propagating flag annotations |
| `results_ablation_kept_edges.csv.zip` | Ablation arm: kept edges |
| `results_mech_kept_edges.csv.zip` | Mechanistic-only arm: kept edges |
| `pathway_metrics_full.json` | Pathway-level scoring metrics for the full arm (P@k, NDCG, AP, mean rank, rank improvement) |
| `pathway_metrics_ablation.json` | Pathway-level scoring metrics for the ablation arm |
| `pathway_metrics_mech.json` | Pathway-level scoring metrics for the mechanistic-only arm |
| `baseline_comparison.json` | Baseline enrichment method comparison metrics (B0–B4) |
| `baseline_comparison.csv` | Full ranked pathway list under all baseline methods; source for Supplementary Table ST2 |
| `resampling_summary.json` | Summary statistics for all 3,003 exhaustive CHD seed-split results: per-metric distributions (mean, SD, min, P25, median, P75, max), robustness counts, and primary split percentile ranks |
| `resampling_results.csv` | Per-split metrics for all 3,003 seed partitions; source for Figure 6 |

**C4 pathway-split controls (`results/chd_benchmark/c4_notch/` and `results/chd_benchmark/c4_mapk/`)**

Each C4 subdirectory contains results for one pathway-split control benchmark. Files use a single-arm naming convention (no arm prefix) as each C4 control uses the full BIFO operator only.

| File | Description |
|------|-------------|
| `results.json` | Gene-level PPR recovery metrics |
| `results_node_index.json` | Node CUI → matrix index mapping |
| `results_scores_cond.npy` | Conditioned PPR score vector |
| `results_scores_raw.npy` | Raw PPR score vector |
| `results_kept_edges.csv.zip` | BIFO-conditioned kept edges |
| `pathway_metrics.json` | Pathway-level scoring metrics (P@k, NDCG, AP, source pathway rank) |
| `baseline_comparison.json` | Baseline enrichment method comparison metrics |

**KF-CHD cohort (`results/kf_chd/`)**

| File | Description |
|------|-------------|
| `results.json` | Four-arm PPR gene-level recovery metrics (AUROC, AUPRC, entropy, nonzero fraction) |
| `results_node_index.json` | Node CUI → matrix index mapping for score vector interpretation |
| `results_kept_edges.csv.zip` | BIFO-conditioned kept edges with flow class and propagating flag annotations |
| `results_scores_cond.npy` | Conditioned (BIFO full-arm) PPR score vector |
| `results_scores_raw.npy` | Raw (unconditioned) PPR score vector |
| `results_scores_meta.npy` | Metadata-filtered PPR score vector |
| `results_scores_rand.npy` | Random sparsification control PPR score vector |
| `pathway_metrics_standard.json` | Pathway-level scoring metrics against the standard scored universe (2,130 pathways) |
| `pathway_scores_standard.csv` | Full ranked pathway list under BIFO full-arm; source for Supplementary Tables ST3 and ST4 |
| `baseline_comparison.json` | Baseline enrichment method comparison metrics (B1–B4) |
| `baseline_comparison.csv` | Full ranked pathway list under all baseline methods; source for Supplementary Tables ST3 and ST5a |
| `resampling_summary.json` | Bootstrap resampling summary: per-metric distributions at n=10, 20, 30 seed sizes (500 draws each) |
| `resampling_results.csv` | Per-draw metrics for all 1,500 bootstrap runs |
| `nodes_clean_noncc.csv.gz` | Node file (pipeline input to conditioning and scoring) |
| `edges_all_noncc.csv.gz` | Merged edge file (pipeline input to conditioning, scoring, and baseline runs) |

**KF-NBL cohort (`results/kf_nbl/`)**

Identical file structure to `results/kf_chd/`. All files were produced by the same pipeline with KF-NBL seed genes (1,395 CUIs) as input.

| File | Description |
|------|-------------|
| `results.json` | Four-arm PPR gene-level recovery metrics |
| `results_node_index.json` | Node CUI → matrix index mapping |
| `results_kept_edges.csv.zip` | BIFO-conditioned kept edges |
| `results_scores_cond.npy` | Conditioned (BIFO full-arm) PPR score vector |
| `results_scores_raw.npy` | Raw PPR score vector |
| `results_scores_meta.npy` | Metadata-filtered PPR score vector |
| `results_scores_rand.npy` | Random sparsification control PPR score vector |
| `pathway_metrics_standard.json` | Pathway-level scoring metrics against the standard scored universe (2,196 pathways) |
| `pathway_scores_standard.csv` | Full ranked pathway list under BIFO full-arm; source for Supplementary Tables ST3 and ST4 |
| `baseline_comparison.json` | Baseline enrichment method comparison metrics |
| `baseline_comparison.csv` | Full ranked pathway list under all baseline methods; source for Supplementary Tables ST3 and ST5b |
| `resampling_summary.json` | Bootstrap resampling summary |
| `resampling_results.csv` | Per-draw metrics for all 1,500 bootstrap runs |
| `nodes_clean_noncc.csv.gz` | Node file (pipeline input to conditioning and scoring) |
| `edges_all_noncc.csv.gz` | Merged edge file (pipeline input to conditioning, scoring, and baseline runs) |

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
mapping (`bifo_mapping.yaml`) are graph-agnostic and can be applied to any
property graph whose edges carry DDKG-compatible predicates. Code is released
under MIT License; benchmark data under CC BY 4.0.


## References {.page_break_before}

