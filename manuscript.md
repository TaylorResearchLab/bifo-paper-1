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
date-meta: '2026-04-26'
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
  <meta name="dc.date" content="2026-04-26" />
  <meta name="citation_publication_date" content="2026-04-26" />
  <meta property="article:published_time" content="2026-04-26" />
  <meta name="dc.modified" content="2026-04-26T01:46:35+00:00" />
  <meta property="article:modified_time" content="2026-04-26T01:46:35+00:00" />
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
  <link rel="alternate" type="text/html" href="https://TaylorResearchLab.github.io/bifo-paper-1/v/c9acfda8da1d8113e9dd561f1fed551c324e7b3e/" />
  <meta name="manubot_html_url_versioned" content="https://TaylorResearchLab.github.io/bifo-paper-1/v/c9acfda8da1d8113e9dd561f1fed551c324e7b3e/" />
  <meta name="manubot_pdf_url_versioned" content="https://TaylorResearchLab.github.io/bifo-paper-1/v/c9acfda8da1d8113e9dd561f1fed551c324e7b3e/manuscript.pdf" />
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

Biological knowledge graphs integrate heterogeneous data across molecular, cellular, and phenotypic domains, but graph traversal treats mechanistic relationships, statistical associations, and annotation edges equivalently, propagating signal along biologically invalid paths and making causal and non-causal explanations computationally indistinguishable. Standard enrichment approaches compound this problem: they lose statistical power at small gene set sizes and collapse numerically at the large gene set sizes produced by rare variant aggregation.

We introduce the Biological Information Flow Ontology (BIFO), a formal specification of admissible biological entities, states, and the directional information flows between them. Applied to a heterogeneous knowledge graph, BIFO conditioning produces a constrained propagation substrate in which signal traverses only biologically valid paths. We implement this as BIFO-PPR, combining BIFO conditioning with Personalized PageRank propagation and degree-normalized pathway scoring. In a three-arm ablation, we establish that pathway inference in ontology-aligned knowledge graphs depends on a structurally distinct bridge layer: mechanistic-only propagation yields zero pathway scores because pathway nodes are unreachable through mechanistic edges alone, while BIFO-conditioned propagation with explicit bridge admission enables signal transfer between the molecular and pathway annotation layers.

Across a curated congenital heart disease benchmark, BIFO-PPR achieves P@10 = 0.70 versus 0.30 for correctly implemented Fisher enrichment and 0.10 for propagation-based baselines. In two independent rare variant cohorts from the Kids First program, BIFO-PPR recovers a coherent ciliopathy pathway cluster in both congenital heart disease and neuroblastoma. WP_CILIOPATHIES carries the strongest statistical enrichment signal among well-calibrated pathways in KF-CHD (null_z = 41.2, q = 0.008, rank 43 of 2,130) and ranks third in KF-NBL (null_z = 18.4, q = 0.014). Correctly implemented Fisher enrichment independently ranks WP_CILIOPATHIES first in both cohorts, supporting that the ciliopathy signal reflects underlying biology. BIFO-PPR additionally recovers this signal in the large gene set regime where Fisher enrichment loses discriminative power.

BIFO provides a principled approach to a problem that affects any inference task on heterogeneous biological graphs: the inability to distinguish biologically meaningful signal from incidental connectivity when edge types are treated equivalently.


## Introduction

Modern biology generates large-scale, multi-modal datasets spanning genomic variation, gene expression, chromatin architecture, protein interactions, metabolism, and disease phenotypes. Knowledge graphs have emerged as a leading framework for integrating these data types, representing biological entities and their relationships in a structure that supports cross-domain queries and biological reasoning [@doi:10.1016/j.csbj.2020.05.017; @doi:10.1038/s41597-024-04070-w; @doi:10.1101/2025.08.11.666099]. However, integration alone does not enable inference. One of the central challenges in using these graphs is understanding how interpretable biological signal can flow across a network from one domain of information to another: from gene-level molecular events to pathway-level biological programs, from genetic variants to disease phenotypes, or from drug targets to downstream cellular effects.

Biological function arises from directional, causal processes that are well established by decades of experimental observation: transcription proceeds from gene to RNA, signaling cascades propagate from upstream activators to downstream effectors, and metabolic transformations are constrained by biochemical feasibility and spatial context. These processes define not only which entities are connected, but which transformations between them are biologically meaningful. Individual entity classes in biomedical graphs are reasonably well specified by dedicated vocabularies: genes by HGNC [@doi:10.1093/nar/gkac888], transcripts by GENCODE [@doi:10.1093/nar/gkaa1113], proteins by UniProtKB [@doi:10.1093/nar/gkac1052], and phenotypes by HPO [@doi:10.1093/nar/gkad1005]. What has not existed is a unified definitional layer that ties these entity definitions together into a formal specification of admissible information flow between them: which transitions between entity classes are biologically valid, in which direction they operate, and what it means for signal to propagate from one domain to another. In heterogeneous knowledge graphs, this gap means that mechanistic relationships, statistical associations, and annotation edges are encoded within the same structure, and graph traversal treats them equivalently, collapsing causal and non-causal connections into a single topology. A path connecting a genetic variant to a disease phenotype may reflect a valid mechanistic process, an indirect regulatory association, or an incidental correlation; without a formal definition of admissibility, these possibilities are computationally indistinguishable.

Standard approaches to pathway enrichment analysis perform reliably on focused, biologically coherent gene sets, typically in the range of tens to a few hundred genes, but encounter hard statistical limits outside that range [@doi:10.1371/journal.pcbi.1002375]. For small gene sets, overlap statistics are unstable and dominated by incidental matches. For large gene sets, particularly those derived from rare variant aggregation across disease cohorts, p-values collapse to numerical limits and lose discriminative power regardless of implementation. Graph-based neighborhood expansion introduces a complementary problem. Biological knowledge graphs exhibit small-world and scale-free topology [@doi:10.1038/30918; @doi:10.1126/science.286.5439.509], meaning that any seed set reaches a large fraction of the full graph within just a few hops. In the DDKG, median shortest path lengths between gene concept nodes are on the order of three hops [@doi:10.1038/s41597-024-04070-w], which is why neighborhood-based enrichment on such graphs effectively queries the entire graph and loses all discriminating power. These are not failures of any particular tool but reflect the statistical and topological properties of the problem: overlap-based enrichment works best when the input gene set is small and coherent, and neighborhood expansion works best when the graph has meaningful local structure rather than near-universal connectivity.

Existing frameworks address parts of this problem but do not resolve it. Ontologies such as Gene Ontology and HPO provide structured representations of biological concepts but do not define propagation rules. Knowledge graph systems support typed traversal but rely on user-defined queries rather than biologically grounded constraints. Causal frameworks such as BEL [@doi:10.1016/j.drudis.2013.05.011] and GO-CAM [@doi:10.1038/s41588-019-0500-1] encode mechanistic relationships but operate within curated representations and do not provide a general protocol for conditioning arbitrary heterogeneous graphs. Graph machine learning approaches can operate over heterogeneous structures but learn propagation behavior from data rather than enforcing biologically interpretable constraints.

To address this gap, we introduce the Biological Information Flow Ontology (BIFO), an ontological framework that formally defines admissible biological entities, entity states, and the information flows between them. BIFO specifies what kinds of biological entities can exist in a flow-aware network, what transformations between those entities are biologically meaningful, and in which directions information can propagate. Within this framework, we distinguish three categories of relationships. Mechanistic relationships encode directional, state-changing biological transformations, such as signal transduction, transcriptional regulation, and biochemical catalysis, and participate in propagation. Observational relationships, such as statistical co-expression or text-mining co-occurrence, capture correlative associations without encoding causal state transitions and are excluded from propagation. Contextual relationships encode spatial, temporal, or structural constraints that restrict which transitions are feasible without themselves carrying signal. Applied to a heterogeneous knowledge graph, these definitions produce a constrained propagation substrate: the constraint is a consequence of the definitions, not their purpose. BIFO is not designed to restrict graphs; it is designed to formalize what biology is in terms of admissible entities and flows. We refer to the full implemented system combining BIFO conditioning with Personalized PageRank propagation and degree-normalized pathway scoring as BIFO-PPR throughout this paper, to distinguish the implemented pipeline from the ontology specification.

We show in this paper that biological inference can be improved by restricting propagation to the admissible transformations defined by BIFO, rather than by adding information to a graph. By constraining propagation to semantically valid paths, BIFO-PPR reduces the reachable state space and increases the identifiability of biologically meaningful signal, inducing a directed, non-symmetric adjacency operator that encodes the source-sink asymmetry inherent in biological processes. Although we evaluate BIFO-PPR here in a gene-to-pathway inference setting using rare variant cohort data, the underlying formalism applies to any feature-to-feature inference problem on a heterogeneous biological graph where the identifiability of causal from associative relationships limits inference.

We evaluate this framework using a controlled benchmark derived from the Data Distillery Knowledge Graph (DDKG) [@doi:10.1101/2025.08.11.666099], integrating curated congenital heart disease gene sets with pathway annotations. Through a three-arm ablation design, we show that mechanistic-only propagation is insufficient to recover pathway-level biological programs, as pathway nodes are structurally unreachable through mechanistic edges alone in this graph representation. This finding reflects a two-layer architecture in ontology-aligned biomedical knowledge graphs, in which mechanistic gene-gene relationships and curated pathway annotations occupy structurally distinct layers connected only through a formally defined bridge edge class. Introducing BIFO-conditioned propagation enables signal transfer across these layers, consistent with this architecture.

We further evaluate BIFO-PPR using rare variant cohorts from the Kids First program [@url:https://kidsfirstdrc.org]. In this regime, gene sets derived from variant aggregation are large and heterogeneous, and standard enrichment approaches become numerically unstable, implementation-sensitive, or lose discriminative power. BIFO-PPR concentrates distributed signal across the graph and recovers biologically relevant pathways without prior specification. In two independent pediatric cohorts representing congenital heart disease and neuroblastoma, diseases with known epidemiological co-occurrence and shared neural crest developmental origins [@doi:10.1002/1545-5017.70055], BIFO-PPR independently recovers a coherent ciliopathy pathway cluster, with convergent support from correctly implemented Fisher enrichment.

Together, these results establish BIFO as an ontological framework for formally defining admissible biological information flow, and BIFO-PPR as an implemented system that enables mechanistically grounded pathway inference where standard approaches fail.


## Methods

These Methods describe the BIFO framework and its application to benchmark evaluation and cohort analysis. All analyses follow a common pipeline: (1) BIFO conditioning defines an admissible edge set, (2) a directed propagation operator is constructed, (3) signal is propagated via Personalized PageRank, (4) pathway scores are computed at pathway concept nodes, and (5) significance is assessed using empirical null models. Parts I through III define this core pipeline: graph conditioning, propagation, and significance testing. Parts IV and V describe benchmark evaluation and cohort application. Across all analyses, pathway scores are evaluated against an empirical rewiring null that tests whether recovered signals exceed what is expected from graph topology alone. The specific analyses instantiated on this pipeline and their relationship to the paper's results are described in Section 2.

## Part I: Graph and conditioning

## 1 BIFO conditioning

### 1.1 Ontology design

BIFO transforms a heterogeneous knowledge graph into a propagation-ready structure by restricting information flow to edges consistent with biologically admissible transformations. Starting from an input graph $G = (V, E)$, each edge is classified according to a predefined mapping that assigns it to one of four categories: mechanistic, weak-mechanistic, observational, or contextual. This mapping is implemented through a fixed configuration (bifo_mapping.yaml v0.7.1; 251 predicate-to-flow entries, 96 explicit non-flow designations, 46 observational edge definitions) and is applied uniformly across all analyses.

Propagation is restricted to edges designated as **admissible**, defined as the union of mechanistic edges, selected weak-mechanistic relationships, and gene-to-pathway membership relationships. Edges classified as observational or contextual are retained in the conditioning output for completeness but are excluded from the propagation operator. This produces a conditioned graph $G_C = (V, E_C)$, where $E_C \subseteq E$ contains only admissible edges.

Within the admissible edge set, gene-to-pathway membership relationships are treated as a distinct class, referred to as **bridge edges**, which connect molecular entities to pathway-level representations. These edges do not represent direct mechanistic interactions; rather, they enable signal transfer between the molecular layer of the graph and the pathway annotation layer. Without them, signal propagating through mechanistic gene-gene relationships has no path to pathway nodes, making pathway-level inference structurally impossible regardless of how strong the molecular signal is. BIFO admits bridge edges as a formally defined propagation-eligible class, with signal flowing unidirectionally from gene nodes to pathway nodes. Only gene-to-pathway membership edges are admissible for propagation; the reverse direction (pathway-to-gene) is explicitly excluded and classified as nonpropagating in the conditioning output. All other admissible edges operate within the molecular layer and represent mechanistic or near-mechanistic biological relationships.

Mechanistic edges encode directional, state-changing biological transformations such as protein-protein signaling, transcriptional regulation, or biochemical reactions. Weak-mechanistic edges represent relationships with partial or indirect mechanistic support that may contribute to information transfer in specific contexts. Observational edges capture statistical or correlative associations without encoding state transitions and are excluded from propagation. Contextual edges encode spatial, temporal, or structural constraints; they are retained in the conditioning output for entity typing purposes but do not carry signal.

Rather than modeling a specific biological system, BIFO defines a set of permissible transformation paths between entities, allowing propagation behavior to be evaluated in terms of biologically grounded information flow across heterogeneous data sources.

BIFO classifies each predicate type into one of these categories and assigns a classification tier that determines its role in the propagation operator. The classification is deliberately conservative: when a predicate type has mixed evidence quality across its instances, the weaker classification applies. This prevents well-supported mechanistic relationships from being diluted by observational instances of the same predicate type in the same graph.

  ----------------------------------- ------------------ -------------------------------- ------------------------------------------------------------------------------------------------
  **Flow class**                      **N predicates**   **Classification(s)**            **Biological meaning**

  **Signal Transduction**             10                 mechanistic                      Phosphorylation, causal regulation, signal propagation

  **Transcription**                   9                  mechanistic / weak-mech          Gene expression, transcription factor binding

  **Translation**                     9                  mechanistic / weak-mech          Gene-protein encoding relationships

  **Protein Interaction**             20                 mechanistic / weak-mech          Binding, complex membership, molecular interaction

  **Signal Termination**              4                  mechanistic                      Dephosphorylation, inhibition, negative regulation

  **Perturbational Effect**           14                 mechanistic / weak-mech          Direct drug-target interactions (mechanistic); correlation predicates (weak-mech), see note

  **Genetic Regulatory Modulation**   11                 mechanistic / weak-mech / obs.   Variant-gene relationships, allele activity

  **Biochemical Transformation**      24                 mechanistic / weak-mech          Catalysis, synthesis, metabolic conversion

  **Pathway Contribution**            27                 mechanistic / weak-mech          Gene-to-pathway membership bridge edges, see note

  **Observational Association**       41                 observational                    Co-expression, text-mining, statistical association

  **Spatial constraint**              47                 contextual / non-propagating     Excluded from PPR operator; used for entity typing only

  **State Progression**               19                 mechanistic / weak-mech          Developmental and temporal transitions

  **Other (6 classes)**               15                 mechanistic                      Complex formation, transport, chromatin topology, etc.
  ----------------------------------- ------------------ -------------------------------- ------------------------------------------------------------------------------------------------

**Table M1.** *BIFO flow class definitions. N predicates = number of DDKG predicate types assigned to this class in v0.7.1. Classification(s) indicates which tier(s) apply within the class. Classes with mixed classifications contain predicates of different evidential quality, classified at the predicate level rather than the class level.*

> *Pathway Contribution edges encode curated gene-to-pathway membership relationships (inverse_pathway_associated_with_gene, inverse_has_signature_gene; gene-to-pathway direction only). Signal flows unidirectionally from gene nodes to pathway nodes, consistent with BIFO Specification v0.02 in which Pathway Contribution is defined as P or CM to PW.*
>
> *Perturbational Effect contains two distinct predicate groups: direct molecular interactions (bioactivity, chemical_or_drug_affects_gene_product, targets_expression_of_gene; classified mechanistic) and correlation-derived associations (positively/negatively_correlated_with_gene; classified weak-mechanistic). The mechanistic-only arm retains the mechanistic subset and excludes the correlation predicates, allowing the mechanistic operator to capture direct drug-target connectivity without admitting association noise.*

### 1.2 Entity resolution

Entity resolution maps each concept node to its source vocabulary, which is necessary to apply source-specific flow class rules and membership constraints. In a standards-compliant graph, nodes carry CURIE-formatted identifiers (e.g., HGNC:1100, GO:0007165) from which the source authority can be read directly from the prefix. Where CURIEs are not available, source authority base (SAB) identifiers or equivalent vocabulary tags serve the same role. The pipeline uses a two-level procedure: at Level 1, it attempts to resolve each node to a source vocabulary by reading its identifier prefix or SAB annotation; at Level 2, edges with at least one unresolvable endpoint are dropped rather than admitted with unknown classification.

Resolution rate depends on the scope of the graph export and the vocabulary coverage of the SAB selection. Nodes belonging to vocabularies outside the configured SAB set are treated as unresolvable and their edges are excluded from the propagating operator. This is conservative by design: admitting edges of unknown provenance would undermine the flow class guarantees that BIFO conditioning provides.

### 1.3 Propagating operator construction

The conditioned edge set $E_C$ is used to build a sparse directed adjacency matrix over the node set $V$. Edge weights are uniform (weight = 1); the pipeline supports evidence-tier weighting when confidence annotations are present in the edge file, but all analyses reported here use unit weights. Row normalization is applied before transpose to produce the column-stochastic matrix used in the PPR recurrence.

**Formal definition.** Let $G = (V, E)$ be the input property graph where each edge $e = (u, v, p)$ carries predicate $p$ and endpoint source vocabulary identifiers $s_u, s_v$. BIFO conditioning defines a constraint operator $C$ that produces the conditioned propagation graph $G_C = (V, E_C)$, where:

$$E_C = \{ e \in E : \operatorname{flow\_class}(\text{predicate}(e)) \in F_{\text{admissible}} \land \text{source}(u) \text{ resolved} \land \text{source}(v) \text{ resolved} \}$$ {#eq:operator}

$F_{\text{admissible}}$ is the set of flow classes designated as propagating in bifo_mapping.yaml (mechanistic and weak-mechanistic tiers, plus Pathway Contribution bridge edges; excluding Observational Association, contextual_constraint, and nonpropagating_context tiers). The operator's admissibility decisions depend only on the predicate-to-flow mapping and entity resolution rules, not on graph topology, so the same conditioning logic applies to any property graph whose edges carry compatible predicate vocabularies.

## 2 Knowledge graph source

The analyses in this paper use the Common Fund Data Ecosystem Data Distillery Knowledge Graph (DDKG), built on the Unified Biomedical Knowledge Graph (UBKG) and inheriting Petagraph infrastructure [@doi:10.1101/2025.08.11.666099; @doi:10.1038/s41597-024-04070-w]. DDKG integrates heterogeneous biological knowledge from multiple source ontologies and databases into a unified concept-and-relationship graph. Each concept node carries a SAB identifier and each edge carries a predicate drawn from the source ontology's relation vocabulary, making edge provenance fully traceable and satisfying the predicate-mapping and entity resolution requirements of BIFO conditioning.

For each analysis, the graph was queried as a 1-hop neighborhood centered on the relevant seed gene set, producing a mechanistic and association edge file and a separate gene-to-pathway membership edge file derived from MSigDB [@doi:10.1073/pnas.0506580102; @doi:10.1016/j.cels.2015.12.004], WikiPathways [@doi:10.1093/nar/gkaa1024], and Gene Ontology annotations. These were merged into a single edge file for conditioning. Node metadata was exported separately. The specific graph parameters, edge counts, and conditioning results for each analysis are described in the relevant benchmark and cohort sections.

The analyses described above are instantiated on a set of graph projections and gene sets constructed to isolate distinct properties of the method. All benchmarks and cohort analyses use the same underlying DDKG representation and BIFO conditioning procedure, with differences arising from the choice of seed sets, graph export scope, and evaluation regime.

The primary benchmark is defined on a controlled 1-hop projection of the DDKG centered on a curated set of congenital heart disease genes, producing a graph with fixed topology and known pathway reference structure (Section 6.3). Within this graph, separate benchmark cohorts are defined for discovery and recovery tasks, using curated disease genes and pathway-derived gene sets (Sections 6.1–6.4). This design allows evaluation of pathway inference under both indirect (discovery) and direct (recovery) signal regimes.

To evaluate robustness to input gene selection, an exhaustive resampling analysis is performed over all C(15,10) = 3,003 possible seed/held-out partitions of the CHD gene pool, holding the graph structure and propagation operators fixed while varying only the seed vector (Section 9). This isolates the contribution of seed composition to pathway-level inference independently of graph topology.

The same pipeline is then applied to two large-scale rare variant cohorts from the Kids First program (congenital heart disease and neuroblastoma), where gene sets are derived from germline variant aggregation and evaluated in discovery mode without predefined pathway targets (Sections 10–15). These cohort analyses represent a distinct regime from the curated benchmarks, characterized by large, heterogeneous gene sets and distributed biological signal, and are used to assess whether BIFO-conditioned propagation recovers coherent pathway structure under conditions where standard enrichment approaches lose discriminative power.

With the conditioned graph $G_C$ and propagation operator defined, Parts II and III describe how signal is propagated and scored.

## Part II: Propagation and pathway scoring

## 3 Personalized PageRank propagation

Signal propagation uses Personalized PageRank (PPR), also known as random walk with restart [@doi:10.1145/1148170.1148225]. PPR models the probability that a random walk starting from a set of seed nodes visits each other node in the graph, with a restart probability that returns the walk to the seeds at each step. Applied to a BIFO-conditioned graph, this concentrates signal in the neighborhood of the seeds while respecting the directional constraints imposed by the admissible edge set.

Given the column-stochastic adjacency matrix $\tilde{A}$ derived from $G_C$, a seed vector $\mathbf{s}$ with uniform mass $1/|S|$ over seed nodes and zero elsewhere, and restart probability $\alpha$, the PPR score vector $\mathbf{f}$ satisfies:

$$\mathbf{f} = (1 - \alpha) \cdot \tilde{A}^\top \cdot \mathbf{f} + \alpha \cdot \mathbf{s}$$ {#eq:ppr}

The fixed point is computed iteratively as $\mathbf{f}_{t+1} = (1-\alpha)\tilde{A}^\top\mathbf{f}_t + \alpha\mathbf{s}$, terminating when $\|\mathbf{f}_{t+1} - \mathbf{f}_t\|_1 < 10^{-10}$ or after 500 iterations.

The restart probability $\alpha$ controls the trade-off between local signal retention and global diffusion. High $\alpha$ keeps signal concentrated near the seeds; low $\alpha$ allows it to diffuse further into the graph. For pathway scoring, relevant pathway nodes may be several hops from the seed genes, so some diffusion is necessary. A value of $\alpha = 0.5$ was selected to balance these considerations and was fixed before any benchmark evaluation.

## 4 Pathway scoring

### 4.1 Membership map construction

Pathway scoring requires a map from gene nodes to the pathway nodes they belong to. Membership is determined from gene-to-pathway edges using the designated bridge edge predicate types, drawn from the pre-conditioning edge file. Because gene-to-pathway Pathway Contribution edges are admissible under BIFO by definition and are not selectively excluded, using the pre-conditioning edge file is equivalent to using the conditioned edge set for membership construction. Membership edges are source-vocabulary constrained: a gene is counted as a member of a pathway only if its SAB matches the pathway's source vocabulary, preventing cross-vocabulary membership contamination. Duplicate memberships are removed.

Pathways are filtered by size, retaining those with at least 8 and at most 300 members. Pathways below the minimum are too small for enrichment analysis to be meaningful; pathways above the maximum are too broad to be biologically informative. A name-pattern filter additionally excludes gene expression quantile sets and microRNA sets, which represent statistical partitions rather than curated biological programs. The resulting pathway universe is held constant across all scoring arms and baseline methods within a given analysis.

### 4.2 Pathway score computation

The primary scoring function, **degree_norm**, is defined as:

$$\text{score}(p) = \frac{f_{\text{direct}}(p)}{\sqrt{|\text{members}(p)|}}$$ {#eq:degreenorm}

where $f_{\text{direct}}(p)$ is the PPR score on the pathway concept node itself, representing signal mass that arrived via bridge edges, and $|\text{members}(p)|$ is the source-vocabulary-constrained member gene count. The square root penalty down-weights large generic pathways, which accumulate high PPR scores by virtue of having many members, without fully normalizing by size in a way that would over-penalize legitimate large biological programs. Pathways with no member genes receive a score of zero.

This scoring function was specified before benchmark evaluation and was not modified after the first successful run. A diagnostic scoring variant, **local_bg**, is computed as the direct PPR score minus the mean PPR score of the pathway node's immediate graph neighbors. This variant is included in output files for exploratory analysis but is not used in any reported evaluation metrics.

## Part III: Significance testing

## 5 Empirical significance via membership rewiring null

BIFO pathway scores are made actionable by comparison to an empirical null that tests whether a pathway's observed score exceeds what is expected given the propagated signal landscape. The null model uses degree-preserving rewiring of the bridge edge layer, keeping the seed set and propagation operator fixed while randomizing which genes are assigned as members of each pathway. For each permutation, bridge edges are rewired via random endpoint swaps that preserve each pathway's member count and each gene's pathway membership count exactly. PPR is rerun on the rewired graph with the same seeds and degree_norm scores are recomputed for all pathways. This process is repeated N = 1,000 times to build a per-pathway null distribution.

Statistical significance is assessed using the finite-sample-corrected empirical p-value (Phipson and Smyth 2010):

$$p = \frac{1 + \text{count}(\text{null} \geq \text{observed})}{1 + N}$$

BH correction is applied across all scored pathways to obtain q-values. The null_z score for each pathway is the number of standard deviations the observed degree_norm score sits above the mean of its null distribution. Rewiring is restricted to gene-to-pathway membership (bridge) edges; all mechanistic edges remain fixed across permutations. The null seed universe is restricted to genes connected to pathways retained after size and name-pattern filtering; genes connected only to excluded pathways do not contribute to null permutations.

### 5.1 Null calibration

The rewiring null can become degenerate for pathways where the null distribution mean is near zero. In this case all permutations produce scores far below the observed value, the null standard deviation collapses, and null_z inflates mechanically rather than reflecting biological enrichment. Pathways where the null mean is less than 10% of the observed score are excluded from BH correction and reported with null_z = NaN and empirical_q = NaN. The null_calibrated column in the output flags which pathways pass this filter.

### 5.2 Dependence on graph composition

The validity of the rewiring null depends on the ratio of bridge edges to non-bridge edges in the propagating graph. When non-bridge edges provide sufficient routing structure, rewired bridge assignments that do not match the biological signal in the seeds produce low pathway scores, and the null distribution is well separated from the observed score. When bridge edges dominate the propagating graph, rewiring effectively randomizes the primary routing structure, and random bridge assignments frequently inflate the null mean. The bridge edge fraction therefore determines whether the rewiring null is a meaningful calibration tool for a given analysis, and is reported alongside null calibration results for each analysis in Parts IV and V.

### 5.3 Member-level empirical null

A complementary null tests whether a pathway's constituent genes carry disproportionate propagated signal, without requiring PPR reruns. For each pathway, the observed mean PPR score across its member genes is compared against N = 1,000 matched random gene sets of the same size drawn from the pathway-connected gene universe. Null genes are matched to true pathway members on two structural features only: conditioned graph out-degree and pathway membership count, both log-binned into 10 quantile bins. Observed propagated score is intentionally excluded from matching to avoid conditioning the null on the quantity being tested.

Empirical p-values use the same finite-sample correction as above; BH correction is applied across all tested pathways. This null is less sensitive to bridge edge fraction than the pathway-node rewiring null because it operates on the fixed propagated signal rather than the propagation operator itself. The two nulls are complementary: the pathway-node rewiring null tests whether signal accumulates at the pathway node, while the member-level null tests whether the genes defining that pathway carry disproportionate propagated signal.

### 5.4 Stability analysis

Statistical significance under the rewiring null establishes that a pathway score exceeds topological expectation for a given seed set. It does not establish whether that score is a stable property of the underlying biology or an artifact of the specific genes provided as input. A pathway that ranks highly and passes significance testing under many different seed configurations is more credible than one that does so only for a particular input.

Stability is assessed by perturbing the seed set and measuring whether pathway recovery is preserved. For gene pools small enough to enumerate completely, all possible seed partitions are evaluated exhaustively. For large cohort gene sets where exhaustive enumeration is not feasible, bootstrap resampling draws random subsets of varying size from the full seed pool. In both cases, the primary question is whether the signal is a property of the biology represented in the gene set or a consequence of the specific input configuration. The implementations of these two approaches are described in the benchmark and cohort sections where they are applied.

## Part IV: Benchmark evaluation

## 6 Benchmark design

### 6.1 Task types

Two benchmark task types are defined. In a **discovery** benchmark, seed genes are not members of the target reference pathways; the evaluation tests whether BIFO can identify biologically relevant pathway families from a gene set that does not directly overlap those families. In a **recovery** benchmark, seed genes are drawn directly from target pathway members; the evaluation tests whether BIFO can recover the source pathway and related pathways from partial membership.

These task types produce systematically different results and must be interpreted separately. In the recovery setting, seed-overlap Fisher enrichment is naturally strong because the overlap between seeds and pathway members is direct and large. In the discovery setting, Fisher enrichment degrades because the overlap is indirect, requiring propagation to bridge the gap between the seed genes and the relevant pathway family. BIFO is designed primarily for the discovery setting, and its advantage over overlap-based methods is largest there.

### 6.2 Overview of benchmarks

Three benchmarks are evaluated against the same DDKG graph projection. Table M2 summarizes their key parameters; each is described in full in the sections below.

  ----------------- --------------- ----------- ------------- --------------- ------------------------------------------------------------------------------------------------------------
  **Benchmark**     **Task type**   **Seeds**   **Heldout**   **Reference**   **Seed source**

  **CHD curated**   Discovery       10          5             18 pathways     Hand-curated TF and structural genes: GATA4, NKX2-5, TBX5, NOTCH1, NOTCH2, HAND1, HAND2, MYH6, GATA6, TBX1

  **C4/Notch**      Recovery        30          14            11 pathways     70% random sample of REACTOME_SIGNALING_BY_NOTCH members (seed=42)

  **C4/MAPK**       Recovery        63          28            10 pathways     70% random sample of REACTOME_MAPK_FAMILY_SIGNALING_CASCADES members (seed=42)
  ----------------- --------------- ----------- ------------- --------------- ------------------------------------------------------------------------------------------------------------

**Table M2.** *Benchmark definitions. Task type: discovery = seeds not in reference pathway family; recovery = seeds drawn from source pathway members. C4 splits used numpy.random.seed(42). All CHD-pool CUIs verified in node index before freeze.*

### 6.3 Benchmark 1: CHD curated discovery benchmark

The CHD curated benchmark is the primary evaluation of BIFO pathway prioritization performance. It uses ten canonical transcription factor and structural genes from the CHD literature as seeds: GATA4, NKX2-5, TBX5, NOTCH1, NOTCH2, HAND1, HAND2, MYH6, GATA6, and TBX1. These genes were selected based on their established roles in cardiac development and CHD genetics and were not selected to maximize BIFO performance.

Five additional CHD-associated genes (ZFPM2, MYH7, PTPN11, JAG1, FLT4) are designated as held-out nodes. These genes receive no seed mass during propagation and are invisible to the PPR operator. After propagation, their scores are examined to ask whether the 10 seeds, propagating through the conditioned graph, drove score mass toward these 5 biologically relevant genes even though they were not seeded. This is a gene-level recovery test: the held-out genes serve as a positive control for signal localization, distinguishing biologically meaningful propagation from mass accumulating at high-degree hub nodes. Gene-level recovery is measured by AUPRC over the held-out genes versus all other non-seed, non-heldout nodes in the graph.

The pathway reference set consists of 36 literature-curated cardiac pathway CUIs; 18 are present in the scored pathway universe and serve as the pathway-level evaluation reference. Pathway scoring uses all 10 seeds and is evaluated independently of the held-out gene analysis.

Because the seed genes are transcription factors and structural cardiac genes rather than direct pathway members, this is a discovery task: BIFO must propagate signal from the seeds through the conditioned graph and across the bridge layer to reach and prioritize the relevant pathway family. The fixed 10/5 split described here defines the primary benchmark run. The relationship between this configuration and the exhaustive resampling across all possible 10/5 splits of the 15-gene pool is described in Section 9.

The graph for this benchmark was queried as a 1-hop neighborhood centered on the 15 CHD-associated genes, producing edges_raw.csv (94,790 mechanistic and association edges) and pathway_membership_edges.csv (79,562 gene-to-pathway membership edges), merged into edges_merged.csv (174,352 edges total). Node metadata was exported in nodes.csv (34,523 concept nodes). BIFO conditioning resolved 18,897 of 34,523 concept nodes (54.7%) to source vocabularies; the remaining 15,626 structurally peripheral nodes were treated as unresolvable and their edges dropped. The three-arm ablation design applied to this benchmark is described in Section 6.5.

### 6.4 Benchmarks 2 and 3: C4 pathway-split recovery controls

The C4 controls evaluate BIFO in the recovery setting, where seeds are drawn directly from the members of a known pathway. These benchmarks serve a different purpose from the CHD curated benchmark: they test whether BIFO can recover the source pathway and related pathway family from a partial membership set, and they establish a baseline expectation for rank improvement in the recovery regime.

Two pathway splits are used. **C4/Notch** uses a 70%/30% random split of REACTOME_SIGNALING_BY_NOTCH (MSigDB M10189; 44 total members), yielding 30 seed genes and 14 held-out genes. This pathway is cardiac-relevant and tests recovery within a coherent, well-annotated signaling family. **C4/MAPK** uses a 70%/30% random split of REACTOME_MAPK_FAMILY_SIGNALING_CASCADES (MSigDB M27565; 91 total members), yielding 63 seed genes and 28 held-out genes. This pathway is broader and less cohesive than the Notch pathway and is not related to the CHD seed set, providing a test of recovery in a less structured biological context. Both splits used numpy.random.seed(42) and all pathway members were verified to be present in the node index before splitting.

Because seeds in the recovery setting are drawn from pathway members, direct overlap with the reference pathway is high by construction. Fisher enrichment therefore performs well in this setting, and rank improvement relative to raw PPR is expected to be smaller or negative. Results from the C4 controls are reported separately from the CHD curated benchmark and interpreted accordingly.

### 6.5 Three-arm ablation design

The three-arm ablation design is applied to the CHD curated benchmark to isolate the contribution of specific edge classes to pathway scoring. The PPR operator is varied across three arms while the scoring stage (pathway membership map, pathway universe, and reference set) is held constant. Differences in scoring outcomes are therefore directly attributable to operator composition.

The three arms are constructed from the 105,192 edges retained after Level 2 conditioning of the CHD benchmark graph. The **full arm** uses all 57,005 propagating edges, including Pathway Contribution bridge edges in the gene-to-pathway direction. The **ablation arm** conditions the mechanistic and association edges independently of the membership edges, retaining 14,413 propagating edges with no Pathway Contribution bridge edges; this isolates the effect of removing the gene-to-pathway bridge while preserving all other admissible flow classes. The **mechanistic-only arm** retains only the 9,710 edges classified as strictly mechanistic (Signal Transduction 5,786, Transcription 1,568, Signal Termination 484, and minor mechanistic classes), excluding Pathway Contribution, Observational Association, and all weak-mechanistic edges.

Observational Association edges (9,909), Pathway Contribution edges in the pathway-to-gene direction (37,352), weak-mechanistic Genetic Regulatory Modulation edges (64), and Spatial constraint edges (862) are retained in kept_edges.csv but excluded from all three PPR adjacency matrices. Gene-level analyses additionally include raw propagation and random sparsification controls (Table 2); pathway-level ablation focuses on these three BIFO-derived operators.

## 7 Baseline enrichment methods

Baselines are designed to represent the strongest approaches a bioinformatician would realistically apply to the same data, not deliberately weak comparators. All baselines are evaluated on the identical pathway universe and reference set as the BIFO arms. When run alongside BIFO-PPR, baselines are additionally restricted to the BIFO-scored pathway universe to ensure direct comparability; pathways not present in the BIFO output are excluded from baseline evaluation.

**B0: Degree-weighted seed overlap.** For each pathway $p$, the score is the sum of conditioned-graph out-degrees of seed genes that are direct members of $p$, normalized by pathway size:

$$\text{score}(p) = \sum_{g \in \text{seeds} \cap \text{members}(p)} \text{degree}_{\text{cond}}(g) \;/\; \sqrt{|\text{members}(p)|}$$ {#eq:b0}

This baseline uses graph structure but not propagation: it scores pathways based on how well-connected the directly overlapping seed genes are within the conditioned graph, without running PPR. It isolates the contribution of propagation beyond local connectivity.

**B1: Seed-only hypergeometric enrichment.** A one-tailed hypergeometric test is applied for each pathway, testing whether seed genes are over-represented among pathway members relative to a background gene universe. P-values are BH-corrected across all pathways. This baseline represents what a bioinformatician would do with the seed gene list alone and no graph information.

The choice of gene universe matters substantially. For the curated benchmark (10 seeds against a universe of approximately 13,000 graph-connected genes), standard-precision computation is used and produces the honest result: non-specific hits dominate because a ten-gene query cannot discriminate against a large background. For large gene sets such as the KF cohort analyses (1,276 to 1,395 seeds against a universe of approximately 22,600 genes), standard-precision hypergeometric computation returns p = 0.0 for every pathway with any meaningful overlap, eliminating rank discrimination entirely. In this regime, log-space computation is required to recover correct relative ordering, and the gene universe is restricted to pathway member genes (excluding seed genes) rather than all graph-connected genes. These two modes test different statistical hypotheses and produce numerically incomparable results; the appropriate mode for each analysis is specified where results are reported.

**B2: 1-hop neighborhood hypergeometric enrichment.** The query set is expanded to include all gene-concept neighbors of the seed genes in the merged edge file, and the same hypergeometric test is applied to the expanded query. This represents the natural workflow of extracting a graph neighborhood and running standard enrichment. The neighborhood inflation problem, in which the expanded query covers the majority of the pathway gene universe and eliminates discriminative power, is itself an informative result about the limitations of this approach.

**B3 / B3b: Preranked GSEA on PPR scores.** Genes are ranked by their PPR scores (raw graph for B3; BIFO-conditioned graph for B3b) and a weighted running-sum enrichment score (using absolute PPR score weighting for hits) is computed following the preranked GSEA algorithm [@doi:10.1073/pnas.0506580102]. B3 tests whether propagation alone recovers pathway-relevant signal without BIFO conditioning. B3b tests whether BIFO-conditioned gene-level scores, used as input to GSEA, improve over raw propagation. The difference between B3b and the BIFO-PPR full arm isolates the contribution of the degree_norm pathway-level scoring function beyond what gene-level score ordering provides.

## 8 Evaluation metrics

Metrics are computed at two levels. Gene-level metrics evaluate how well PPR propagation recovers held-out disease genes, testing signal localization. Pathway-level metrics evaluate how well pathway scoring ranks disease-relevant pathways, which is the primary evaluation target.

  ------------------ ------------- -------------------------------------------------------------------------------------
  **Metric**         **Level**     **Definition**

  AUROC              Gene          Area under ROC curve for held-out gene recovery vs. all non-seed, non-heldout nodes

  AUPRC              Gene          Area under precision-recall curve for held-out gene recovery

  Entropy            Gene          Shannon entropy of PPR score distribution; lower = more concentrated signal

  Nonzero fraction   Gene          Fraction of graph nodes with PPR score > 0

  P@k                Pathway       Precision at rank k: fraction of top-k pathways in the reference set

  Enrichment@k       Pathway       P@k divided by background rate (reference pathways / universe size)

  Recall@k           Pathway       Fraction of all reference pathways recovered in top-k

  NDCG@k             Pathway       Normalized discounted cumulative gain at rank k; accounts for rank position of hits

  Avg. Precision     Pathway       Area under precision-recall curve across all ranks; single-number ranking summary

  Mean ref. rank     Pathway       Mean rank of reference pathways under the conditioned score vector

  Rank improvement   Pathway       mean_rank(raw) minus mean_rank(conditioned); positive = conditioning helps
  ------------------ ------------- -------------------------------------------------------------------------------------

**Table M3.** *Evaluation metrics. Gene-level metrics are computed over held-out nodes vs. all non-seed, non-heldout nodes in the graph. Pathway-level metrics use the scored pathway universe against the benchmark-specific reference set.*

Average precision is defined as:

$$\text{AP} = \frac{1}{|R|} \sum_{r \in R} P@\text{rank}(r)$$

where $R$ is the reference set and $P@\text{rank}(r)$ is precision at the rank of reference pathway $r$. AP is preferred over P@k as a single-number summary because it accounts for both the number of reference pathways recovered and their rank positions.

Rank improvement is interpreted in the context of task type. In discovery benchmarks, conditioning substantially improves ranks because the raw graph places many non-specific high-degree pathways above the biologically relevant ones. In recovery benchmarks, rank improvement may be negative because the raw PPR arm already has direct proximity to the target pathway through the seed-member overlap; in these cases, average precision and source-pathway rank are the more informative metrics.

## 9 Exhaustive resampling

The CHD curated benchmark evaluates BIFO from a single fixed seed configuration, which raises the question of whether results are specific to that particular gene set. To address this, all C(15,10) = 3,003 possible 10-gene/5-gene partitions of the 15-gene CHD pool are evaluated, exhaustively implementing the stability analysis described in Section 5.4.

The PPR operators and pathway membership map are built once and held in memory. For each of the 3,003 splits only the seed vector is modified; the adjacency matrices, pathway universe, and reference set remain identical to the primary benchmark. Per-split metrics are accumulated in memory and written as a single output file at the end of the run, avoiding thousands of intermediate files.

For each split the following are computed: BIFO-PPR full-arm pathway metrics (P@10, P@20, enrichment@10, NDCG@10, average precision, mean reference pathway rank, and rank improvement); gene-level AUPRC for held-out gene recovery; and a seed-overlap Fisher baseline. The seed-overlap Fisher computed here uses the split seed genes directly as the query set, testing whether those specific genes are over-represented as pathway members. This is distinct from the B1 and B2 baselines in Section 7, which use the full seed set or its graph neighborhood; the two are not numerically comparable and address different questions.

The analysis is parallelized using Python multiprocessing; PPR operator components are serialized to worker processes at startup and each worker processes an assigned batch of splits independently. Results are summarized as distribution statistics across all 3,003 splits, robustness counts, and the primary benchmark split identified as an anchor point within the full distribution. The primary split corresponds to the first 10 genes in the defined CHD pool ordering. The pathway universe for resampling is filtered to the BIFO-scored pathway universe, ensuring direct comparability with the primary benchmark; the gene universe is derived from all C-prefixed nodes in the merged edge file. Membership construction applies the same size and name-pattern filters as the primary scoring pipeline; the BIFO universe restriction provides equivalent coverage of cross-vocabulary exclusions applied by the SAB-aware membership construction in the primary scoring pipeline.

## Part V: Kids First cohort application

## 10 The rare variant enrichment problem

Standard pathway enrichment methods were designed for gene sets produced by differential expression or GWAS association, where input lists are typically small, focused, and biologically coherent. Rare variant cohort analysis occupies a different regime. Aggregating pathogenic and likely pathogenic (P/LP) variants across a disease cohort using AutoGVP [@doi:10.1093/bioinformatics/btae114] typically produces gene lists of hundreds to thousands of genes, with biologically relevant signal distributed across a minority of genes embedded in a larger heterogeneous background.

This creates a fundamental tension for enrichment testing. When carrier frequency filters are strict, the gene list shrinks to tens of genes but becomes dominated by severe recessive disease genes incidentally present in the cohort (lysosomal storage disorders, hereditary hearing loss, retinal dystrophy), obscuring the distributed developmental signal of interest. When filters are relaxed to capture the full P/LP burden, the gene list expands to 1,000 to 1,500 genes, large enough that hypergeometric p-values collapse to zero for virtually every pathway with any overlap, eliminating rank discrimination entirely. As described in Section 7, log-space computation and a restricted gene universe recover correct relative ordering in this regime, but the fundamental problem remains: a gene list of this size and heterogeneity carries weak enrichment structure regardless of implementation.

BIFO addresses this directly. By propagating signal from all seeds simultaneously through the conditioned graph, coherent biological signal from a functionally related gene subset concentrates at relevant pathway nodes while incoherent background signal diffuses away. The approach does not require the input gene set to be small or homogeneous.

## 11 Cohort and variant selection

Germline variant data were obtained from two Kids First pediatric cohorts: KF-CHD (Pediatric Cardiac Genomics Consortium, phs001138, n=697 probands with congenital heart defects) and KF-NBL (Discovering the Genetic Basis of Human Neuroblastoma, phs001436, n=460 probands with neuroblastoma). Whole-genome sequencing was performed using Kids First harmonization pipelines aligned to GRCh38/GENCODE v39.

Variants were filtered retaining GATK PASS calls with genotype quality ≥20 and read depth ≥10. AutoGVP P/LP classification was applied integrating ClinVar and modified InterVar for hierarchical ACMG-AMP criteria assessment. Population allele frequency filtering used gnomAD v3.1 [@doi:10.1038/s41586-020-2308-7] at MAF ≤0.001, matching the companion U24 cross-cohort enrichment analysis (Stear et al., CFDE Meeting 2026). Genes harboring at least one qualifying variant in any proband were aggregated per cohort.

Twenty high-frequency background disease genes were excluded: genes among the most prevalent recessive carrier loci in population-scale sequencing (carrier frequency >1% in gnomAD) that represent incidental findings unrelated to the disease of interest. The excluded genes encode proteins associated with hereditary hearing loss (GJB2, MYO15A, MYO1A, MYO3A, MYO7A, USH2A), retinal dystrophy (ABCA4), skin barrier dysfunction (FLG, KRT71, KRT86, TCHH, PADI3), metabolic disease (G6PD, PAH, BCHE), and structural or connective tissue disorders (TTN, OBSCN, COL4A5, TBL1Y, CD36). This yielded 1,287 seed genes for KF-CHD and 1,406 seed genes for KF-NBL.

At the MAF ≤0.001, n≥1 threshold, 570 of 1,287 CHD seed genes (44.3%) are also present in the NBL seed set. This inter-cohort overlap reflects the shared background of Mendelian disease gene carriers present in any pediatric sequencing cohort at this allele frequency threshold and is not specific to either disease. Carrier count-filtered seed sets (n≥2: 387 CHD / 401 NBL genes, 30% overlap; n≥3: 146 CHD / 147 NBL genes, 27% overlap) show reduced but persistent overlap, consistent with shared rare variant burden being a property of the population rather than the disease.

## 12 Graph export and conditioning

Export queries were generated dynamically from each seed list. The KF-CHD export produced 815,248 concept nodes and 5,261,300 1-hop edges plus 486,642 gene-to-pathway membership edges; the KF-NBL export produced 880,456 concept nodes and similar edge counts. An additional export provided node metadata for 21,353 MSigDB pathway member genes not present in the 1-hop seed neighborhood, required for complete pathway membership resolution. Of 1,287 CHD seed genes, 1,276 (99.1%) resolved to UMLS CUIs; of 1,406 NBL seed genes, 1,395 (99.2%) resolved. BIFO conditioning used identical parameters to the curated benchmark (alpha=0.5, bifo_mapping.yaml v0.7.1), retaining 2,482,752 propagating edges for KF-CHD (43.9% of concept edges) and 2,647,055 for KF-NBL (45.1%).

## 13 Pathway scoring and reference set

Pathway scoring used degree_norm against a universe of 2,130 pathways for KF-CHD and 2,196 for KF-NBL, each passing the size, name-pattern, and canonical-collection filters described in Section 4.1. Canonical collections retained were Hallmarks, Reactome, WikiPathways, KEGG, BioCarta, and PID; C2.CGP author-named gene expression signature sets were excluded. All pathways were scored and ranked in discovery mode with no reference pathway set pre-specified. Full pathway-level scoring results for both cohorts, including per-pathway seed gene membership, PPR-normalized member scores, and influential node z-score summaries, are provided as Supplementary Data SD1 (KF-CHD) and SD2 (KF-NBL). Structured input documents for LLM-assisted biological interpretation of these results, including column definitions, analytical task instructions, and provenance records, are provided as Supplementary Tables ST8 (KF-CHD) and ST9 (KF-NBL); verbatim LLM responses are in Supplementary Section S1.

Results were evaluated post-hoc against a 16-pathway cilia reference set pre-specified before scoring, consisting of MSigDB canonical cilia, ciliopathy, and related pathway CUIs (ciliopathies, ciliary, intraflagellar transport, Joubert syndrome, Bardet-Biedl syndrome, primary ciliary dyskinesia, and related terms). Of 17 candidate reference pathways, 16 were present in the scored universe after canonical-collection filtering; this 16-pathway subset is used for all quantitative metrics. A broader 21-pathway expanded reference set including additional GO and Reactome cilia annotations is used for visualization in Figure 4 only.

## 14 Baseline comparisons and rank analysis

The same baseline methods described in Section 7 are applied to the KF cohort analyses using the cohort-appropriate settings: log-space hypergeometric computation and a gene universe restricted to pathway member genes (excluding seed genes), as described in Section 7 (B1). All methods are evaluated on identical pathway universes to enable direct rank comparison.

The primary comparison metric is the rank of WP_CILIOPATHIES and other cilia-related pathways under each method in full discovery mode. Secondary comparisons examine the top-20 ranked pathways per method, the head-to-head rank correlation between Fisher enrichment and BIFO across all pathways, and the full cilia pathway cluster ranking under BIFO-PPR. Concordance between BIFO and correctly implemented Fisher enrichment on the top cilia hit is reported as independent validation of the biological signal rather than a competitive comparison, for the reasons described in Section 6.1.

## 15 Bootstrap resampling

Stability of cilia pathway recovery across seed set sizes is assessed by bootstrap resampling, implementing the approach described in Section 5.4 for the large cohort setting where exhaustive enumeration is not feasible. For each of three seed sizes (n=10, 20, 30), 500 bootstrap draws were made by sampling uniformly without replacement from the full seed CUI pool. For each draw, BIFO scoring and seed-only Fisher enrichment were run using the identical pathway universe and cilia reference set as the primary analysis.

Performance was measured as Precision@10 against the 16-pathway cilia reference, average precision, and rank improvement. The full cohort run (1,276 seeds for KF-CHD; 1,395 for KF-NBL) was included as a reference point. All 1,500 bootstrap runs per cohort were parallelized across 192 cores; total runtime was approximately 150 seconds per cohort.

The bootstrap analysis addresses two questions: whether cilia pathway recovery requires the full cohort-scale variant burden or can emerge from small random gene subsets; and whether BIFO or Fisher enrichment is more sensitive for detecting cilia signal at reduced seed sizes. At bootstrap seed sizes of 10 to 30 genes against a pathway-member universe of approximately 22,600 genes, p-value floor collapse does not occur and standard-precision hypergeometric computation is sufficient. The gene universe consists of pathway-connected genes derived from membership edges in the merged edge file. The bootstrap uses the same BIFO-filtered pathway universe as the primary cohort analysis; membership construction applies the same size and name-pattern filters as the primary scoring pipeline, with SAB-constraint differences documented in Methods §9.


## Results

BIFO conditioning was evaluated across three controlled benchmarks and two independent pediatric rare variant cohorts. In the curated CHD benchmark, BIFO conditioning of a controlled DDKG graph projection produced a structured propagation substrate in which pathway nodes are reachable only through a formally defined bridge edge class; a three-arm ablation design established that this bridge layer is structurally necessary for pathway-level signal transfer. BIFO achieved P@10 = 0.70 against an 18-pathway CHD reference, outperforming all standard enrichment baselines in the curated CHD benchmark comparison, and the result was stable across all 3,003 possible seed configurations of the 15-gene CHD pool. Pathway-split recovery controls showed that the method generalizes beyond disease-gene curation. Applied to two independent Kids First rare variant cohorts, BIFO-PPR recovered a coherent ciliopathy pathway cluster in both congenital heart disease and neuroblastoma in full discovery mode, with WP_CILIOPATHIES carrying the strongest statistical enrichment signal among well-calibrated pathways in KF-CHD (null_z = 41.2, q = 0.008, rank 43 of 2,130) and ranking third in KF-NBL (null_z = 18.4, q = 0.014). Correctly implemented Fisher enrichment independently ranked WP_CILIOPATHIES first in both cohorts, supporting that the recovered signal reflects underlying biology rather than a propagation artifact. Bootstrap resampling established that this signal requires aggregate cohort-scale variant burden and is not recoverable from small random gene subsets.

## 1 Graph conditioning and coverage

The curated CHD benchmark graph was constructed by querying the DDKG as a 1-hop neighborhood centered on 15 CHD-associated genes, producing a mechanistic and association edge file and a separate gene-to-pathway membership edge file, merged into a single input for BIFO conditioning. Table 1 summarizes the full pipeline from query output through entity resolution to the three propagating operator variants used in downstream analyses.

  ------------------------------------- --------------- ----------------------- -------------------------------------------------------------
  **Graph query output**                **Count**       **Fraction**            **Notes**

  Concept nodes exported                34,523          ---                     Node metadata from nodes.csv

  Concept nodes resolved (SAB)          18,897          54.7%                   Level-1 entity resolution; SAB column fallback

  Concept nodes unresolvable            15,626          45.3%                   No SAB match; edges dropped at Level 2

  Seed-centered 1-hop edges             94,790          ---                     edges_raw.csv; mechanistic and association edges

  Gene-to-pathway membership edges      79,562          ---                     pathway_membership_edges.csv; MSigDB, WikiPathways, GO

  **Merged edge file**                  **174,352**     **100%**                **edges_merged.csv; input to BIFO conditioning**

  **BIFO conditioning**                 **Count**       **Fraction of input**   **Notes**

  Kept after conditioning               105,192         60.3%                   Biologically admissible (includes non-propagating retained)

  --- Propagating (conditioned arm)     57,005          32.7%                   Used in PPR operator

  --- Non-propagating retained          48,187          27.6%                   PC pathway-to-gene 37,352; Obs. Assoc. 9,909; Spatial 862; GRM 64

  Dropped: non-flow                     348             0.2%                    Structural/taxonomic predicates

  Dropped: unmapped predicate           36,598          21.0%                   No BIFO flow class assigned

  Dropped: unresolved entity            32,214          18.5%                   No SAB match at entity resolution

  **Propagating operator variants**     **Count**       **Fraction of input**   **Notes**

  Conditioned arm                       57,005          32.7%                   Full BIFO conditioning; all admissible classes

  Ablation arm                          14,413          8.3%                    edges_raw only; no bridge edges by construction

  Mechanistic-only arm                  9,710           5.6%                    Strictly mechanistic classification only
  ------------------------------------- --------------- ----------------------- -------------------------------------------------------------

**Table 1.** *Graph query output, entity resolution, BIFO conditioning, and propagating operator variants for the curated CHD benchmark (bifo_mapping.yaml v0.7.1, unidirectional pipeline, BIFO spec v0.02). The three operator variants share identical scoring stage parameters; differences in pathway-scoring outcomes are attributable to operator composition only.*

Of the 57,005 propagating edges in the conditioned arm, 43,698 (76.7%) are Pathway Contribution bridge edges in the gene-to-pathway direction. Signal Transduction accounted for 5,786 (10.1%) of propagating edges and Perturbational Effect for 5,392 (9.5%), with Transcription, Signal Termination, and minor classes comprising the remainder. The dominance of bridge edges in the propagating operator is a property of this graph's two-layer architecture; its significance for pathway scoring is established by the ablation experiment in Section 3.

![
**BIFO conditioning coverage, curated CHD benchmark graph.**
(**A**) Edge funnel from 174,352 merged input edges through entity resolution and flow-class conditioning to 57,005 propagating edges (32.7% of input) used by the PPR operator; 48,187 additional edges are retained as non-propagating.
(**B**) Dropped edges stratified by cause: unmapped predicates (36,598; 21.0%) and unresolved entities (32,214; 18.5%) account for nearly all losses; non-flow classifications contribute less than 1%.
(**C**) Flow-class distribution of propagating edges. Pathway Contribution bridge edges (43,698; 76.7%) are the architectural element enabling gene-to-pathway signal transfer; mechanistic classes comprise the remaining 23.3%.
(**D**) Concept-node entity resolution: 18,897 of 34,523 nodes (54.7%) resolve to a source vocabulary under the current SAB selection.
](images/fig1_conditioning.png){#fig:conditioning width="100%"}

## 2 Gene-level signal recovery

PPR propagation was evaluated at the gene level across four arms using the curated CHD benchmark graph. Gene-level metrics were computed by assessing recovery of the five held-out CHD-associated genes (ZFPM2, MYH7, PTPN11, JAG1, FLT4) against all other non-seed, non-heldout nodes in the 34,523-node graph.

  ---------------------------- ------------ ------------ ------------- -----------------------
  **Arm**                      **AUROC**    **AUPRC**    **Entropy**   **Nonzero nodes (%)**

  Raw (full graph)             1.000        0.2215       5.728         100.0%

  Conditioned (BIFO)           1.000        0.1947       4.934         ---

  Ablation (no bridge edges)   1.000        0.2215       4.919         ---

  Random sparsification        1.000        0.2173       5.590         64.6%
  ---------------------------- ------------ ------------ ------------- -----------------------

**Table 2.** *Four-arm gene-level recovery for the curated CHD benchmark. Entropy is the Shannon entropy of the PPR score distribution in nats (lower = more concentrated signal). AUROC is near-ceiling across all arms on this small benchmark; entropy is the informative discriminant at this scale.*

AUROC was 1.000 across all arms, reflecting ceiling performance on a benchmark with five held-out nodes in a strongly connected seed neighborhood. Entropy and nonzero fraction are the informative discriminants here. BIFO conditioning reduced entropy from 5.728 (raw) to 4.934, indicating that conditioning concentrates score mass into a smaller, more coherent node subset. The random sparsification control, which retained the same edge count as the conditioned arm through random selection, produced intermediate entropy (5.590), establishing that entropy reduction under BIFO is not simply a consequence of having fewer edges. The ablation arm (no bridge edges) achieved entropy comparable to the conditioned arm (4.919) with AUPRC equal to the raw arm (0.2215), showing that the core mechanistic signal is preserved without bridge edges at the gene level; the contribution of bridge edges is to pathway-level scoring rather than gene-level recovery, as shown in Section 3.

The mechanistic-only arm produced the lowest entropy (4.770) and lowest AUPRC (0.1486), consistent with a sparse subgraph that reaches fewer nodes than the random control. AUPRC declines from raw to conditioned (0.2215 to 0.1947) because conditioning concentrates signal on biologically coherent neighborhoods rather than optimizing for held-out gene recovery. These gene-level metrics become more discriminating at cohort scale with variant-derived seeds, as reported in Section 7.

![
**Four-arm gene-level recovery, curated CHD benchmark.**
Each panel compares four PPR propagation arms (Raw, Metadata-filtered, BIFO-conditioned, Random sparsification) across three graph configurations (Full with all BIFO flow classes, Ablation without Pathway Contribution bridge edges, Mechanistic-only).
(**A**) AUROC is near-ceiling across all arms and configurations and is not informative for this benchmark.
(**B**) AUPRC discriminates between arms; BIFO-conditioned on the mechanistic graph shows the expected drop (0.149) relative to Full (0.192).
(**C**) Localization (mean held-out rank normalized by graph size; lower = more concentrated near seeds). BIFO-conditioned is lowest across Full and Ablation graphs.
(**D**) PPR score entropy in nats. BIFO-conditioned achieves the lowest entropy in all three graph configurations, supporting that conditioning concentrates signal beyond what edge-count reduction alone achieves.
](images/fig2_gene_recovery.png){#fig:gene_recovery width="100%"}

## 3 Pathway prioritization and the role of bridge edges

The three-arm ablation design evaluated pathway prioritization by varying the PPR operator while holding the scoring stage constant across all arms: identical pathway universe (563 pathways), identical CHD reference set (18 pathways), and identical degree_norm scoring function. Differences in outcomes are therefore directly attributable to operator composition.

  -------------------------------- ----------------- ---------- ------------------ --------------- --------------------
  **Arm**                          **Prop. edges**   **P@10**   **Enrich.10**    **Mean rank**   **Rank imp.**

  **Full (BIFO conditioned)**      **57,005**        **0.70**   **21.4×**          **86.6**        **+125.4**

  **Ablation (no bridge edges)**   14,413            0.60       18.3×              86.3            +13.5

  Mechanistic-only                 9,710             0.00       0.0×               177             uninterpretable*
  -------------------------------- ----------------- ---------- ------------------ --------------- --------------------

**Table 3.** *Three-arm pathway prioritization for the curated CHD benchmark. Pathway universe: 563 pathways. CHD reference: 18 pathways. Background rate: 3.3%. Rank improvement = mean_rank(raw) minus mean_rank(conditioned); positive values indicate conditioning improves pathway rank relative to unconditioned propagation. *Mechanistic-only rank improvement is uninterpretable: all pathway scores are exactly zero and tie-ordering is arbitrary.*

### 3.1 Full arm

Under full BIFO conditioning, the top-10 pathways contained 7 of 18 CHD reference pathways (P@10 = 0.70; enrichment = 21.4× background). BRUNEAU_SEPTATION_VENTRICULAR and WP_HEART_DEVELOPMENT ranked first and second. Mean rank of CHD reference pathways under the conditioned score was 86.6, compared with 212.0 under the raw score, yielding rank improvement of +125.4. The top cardiac pathways showed strong separation from the rewiring null: BRUNEAU_SEPTATION_VENTRICULAR (null_z = 15.6, q = 0.034), WP_HEART_DEVELOPMENT (null_z = 16.3, q = 0.034), and WP_CARDIAC_PROGENITOR_DIFFERENTIATION (null_z = 12.3, q = 0.034). Of 563 scored pathways, 16 (2.9%) were significant at q < 0.05 after BH correction, with all top cardiac pathways showing null_z > 9. The member-level null independently supported these results: BRUNEAU_SEPTATION_VENTRICULAR showed member_mean null_z = 10.7 (q = 0.032), WP_HEART_DEVELOPMENT null_z = 10.1 (q = 0.032), and REACTOME_CARDIAC_CONDUCTION null_z = 8.6 (q = 0.032), with 7 of the 17 member-level significant pathways carrying CHD reference annotations.

### 3.2 Ablation arm

Removing Pathway Contribution bridge edges from the propagation operator while retaining the identical membership map for scoring reduced P@10 from 0.70 to 0.60 (enrichment = 18.3×). The top six CHD pathways were identical to those in the full arm. Rank improvement was +13.5, substantially smaller than the full arm's +125.4. The ablation arm improves modestly over the raw arm because mechanistic edges concentrate signal within cardiac-relevant gene neighborhoods prior to scoring; however, without bridge edges in the propagation operator, that pre-transfer signal organization cannot be converted into direct pathway-node signal. The gap between +13.5 and +125.4 isolates the contribution of bridge edges: the large majority of pathway-level conditioning gain comes from their presence in the operator, not from mechanistic edge organization alone.

### 3.3 Mechanistic-only arm

Restricting propagation to strictly mechanistic edges (9,710 edges: Signal Transduction 5,786, Transcription 1,568, Signal Termination 484, and minor mechanistic classes) produced exactly zero scores across all 563 pathways (P@10 = 0.00). This is a structural result, not a performance result. In the present benchmark graph, pathway nodes are not reachable from seed genes through mechanistic edges alone; connectivity between the molecular layer and the pathway annotation layer is mediated exclusively by Pathway Contribution bridge edges. No amount of mechanistic propagation can produce pathway scores in this graph representation without them. The significance of this finding for knowledge graph architecture more broadly is discussed in the Discussion.

### 3.4 Two-layer graph architecture

Together, the three arms identify a two-layer graph architecture with a structurally necessary bridge. The molecular layer encodes gene-gene signaling, transcription, and protein interaction through mechanistic edges. The pathway layer encodes curated gene-set annotations. These layers are structurally separated in this graph; direct connectivity between them is mediated exclusively by Pathway Contribution edges. BIFO's contribution is the principled, ontology-aligned admission of those bridge edges as a coherent propagation-eligible flow class. Without formally recognizing and admitting them, propagation operating on mechanistic edges alone cannot reach pathway concept nodes in this graph construction and scoring formulation.

This architectural property is a consequence of how curated pathway memberships are represented in the DDKG, not an artifact of incomplete edge coverage. Whether it persists under expanded SAB selections incorporating additional evidence layers remains an open question; the present result establishes it for the ontology-aligned mechanistic and pathway representation used here.

> *Scope: these conclusions apply to the present benchmark graph, constructed from a defined SAB subset that isolates ontology-aligned mechanistic and pathway representations from association-derived evidence layers.*

![
**BIFO conditioning enables pathway-level signal recovery.**
(**A**) Precision@10: Full 0.70, Ablation 0.60, Mechanistic 0.00. Mechanistic-only scores are zero because pathway nodes are not reached by propagation under this operator.
(**B**) Enrichment@10 over background rate: Full 21.4×, Ablation 18.3×, Mechanistic 0×.
(**C**) Rank improvement: Full +125.4, Ablation +13.5, Mechanistic uninterpretable (all scores zero).
(**D**) WP_CILIOPATHIES rank under five enrichment methods in the KF-CHD discovery cohort (1,276 variant genes, 2,130 pathways scored), shown here to illustrate performance across all methods including the KF cohort setting; full KF results are in §7. Seed Fisher (corrected) ranks WP_CILIOPATHIES first; BIFO-PPR full-arm ranks it 43rd (null_z = 41.2); Raw PPR GSEA, Conditioned PPR GSEA, and Neighborhood Fisher rank it 1,994, 456, and 2,126 respectively.
](images/fig3_ablation.png){#fig:ablation width="100%"}

![
**Two-layer graph architecture and the role of Pathway Contribution bridge edges.**
Schematic of the conditioned BIFO graph. The molecular layer (top) contains gene and protein concept nodes connected by mechanistic flow-class edges. The pathway layer (bottom) contains curated pathway concept nodes. The two layers are structurally separated in the mechanistic subgraph; connectivity between them is mediated by Pathway Contribution bridge edges (orange, dashed). Seed genes inject PPR probability mass into the molecular layer, which propagates through admissible bridge edges to the pathway layer. In the ablation arm, bridge edges are removed; pathway nodes cannot receive propagated mass directly and the modest rank improvement (+13.5) reflects pre-transfer signal organization in the molecular layer only. Mechanistic-only propagation yields exactly zero pathway scores, supporting that direct bridge transfer is required for pathway-level recovery in this graph construction.
](images/fig7_schematic.png){#fig:schematic width="100%"}

## 4 Comparison with standard enrichment methods

To place BIFO performance in context, four baseline enrichment methods were evaluated on the identical 563-pathway universe and 18-pathway CHD reference set used in Section 3. The baselines represent approaches a bioinformatician would realistically apply to the same graph-derived data: direct seed overlap with graph structure (B0), seed-only hypergeometric enrichment (B1), 1-hop neighborhood hypergeometric enrichment (B2), and preranked GSEA on PPR scores (B3/B3b). The goal is not to select the best method but to characterize where and why standard approaches fail, and what BIFO adds beyond them.

  --------------------------------- ----------- ----------- ------------- ---------------- ---------------
  **Method**                        **P@10**    **P@20**    **NDCG@10**   **Avg. Prec.**   **Mean rank**

  Degree overlap (B0)               0.400       0.400       0.492         0.343            84

  Seed-only Fisher (B1)             0.300       0.200       0.215         0.156            120

  1-hop neighborhood Fisher (B2)    0.000       0.000       0.000         0.036            243

  Raw PPR preranked GSEA (B3)       0.100       0.050       0.220         0.117            162

  Conditioned PPR GSEA (B3b)        0.100       0.050       0.220         0.088            260

  **BIFO-PPR full-arm (degree_norm)**   **0.700**   **0.350**   **0.753**     **0.408**        **87**
  --------------------------------- ----------- ----------- ------------- ---------------- ---------------

**Table 4.** *Baseline comparison for the curated CHD benchmark. All methods evaluated on identical 563-pathway universe (background rate 3.3%). P@10 = fraction of the top-10 ranked pathways that belong to the CHD reference set. NDCG@10 = normalized discounted cumulative gain at rank 10, which rewards recovering reference pathways at higher ranks more than lower ranks. Avg. Prec. = average precision, the area under the precision-recall curve across all ranks; a single-number summary of how well reference pathways are recovered throughout the full ranked list, not just in the top 10.*

BIFO-PPR full-arm outperformed all baselines across every metric: P@10 = 0.70, meaning 7 of the top 10 ranked pathways were disease-relevant; NDCG@10 = 0.753, reflecting that those hits were concentrated at the very top of the list rather than scattered through the top 10; and AP = 0.408, indicating that CHD reference pathways were recovered consistently throughout the full ranked list. These compare to the next best method (B0) at P@10 = 0.40, NDCG@10 = 0.492, and AP = 0.343.

**Seed-only Fisher (B1)** achieved P@10 = 0.30, meaning 3 of the top 10 were CHD-relevant, but the top hits included non-specific entries such as bladder cancer gene sets, TP63 targets, and TNF response pathways. With only ten seed genes, any pathway with even minimal overlap receives a low p-value, so cancer-associated gene sets that happen to share a gene or two with the seed set rank above biologically specific cardiac pathways. AP = 0.156 reflects that this non-specificity persists throughout the ranked list, not just at the top.

**Degree-weighted seed overlap (B0)** performed better than Fisher despite using no statistical test, recovering BRUNEAU_SEPTATION_VENTRICULAR and WP_HEART_DEVELOPMENT at ranks 1 and 2 through direct membership overlap (P@10 = 0.40, AP = 0.343). This result is informative: it shows that the top cardiac pathways are directly accessible from the seed genes through the membership map, and that graph connectivity alone (out-degree of overlapping seed genes) is enough to surface them. BIFO's advantage over B0 on both P@10 (0.70 vs. 0.40) and AP (0.408 vs. 0.343) reflects recovery of additional reference pathways that are connected to the seeds through the graph but do not directly overlap them, which requires propagation rather than local overlap scoring.

**Neighborhood Fisher (B2)** failed entirely, producing P@10 = 0.000 and AP = 0.036. The 1-hop gene neighborhood around the ten seed genes contained 11,146 genes, which is 86% of the full gene universe. At that coverage, virtually every pathway has substantial neighborhood overlap, and p-values are near-identical across pathways, eliminating all rank discrimination. This illustrates a fundamental problem with graph-derived gene sets: expanding to a neighborhood before enrichment testing inflates the query to the point where the test loses all power.

**Raw PPR GSEA (B3)** recovered BRUNEAU_SEPTATION_VENTRICULAR at rank 1 (P@10 = 0.10, AP = 0.117), showing that graph propagation carries pathway-relevant signal even before BIFO conditioning. However, gene-level PPR scores used as input to GSEA are not specific enough to rank more than one or two reference pathways highly; the method does not distinguish between pathways that accumulate signal because their member genes are biologically relevant and pathways that accumulate signal simply because their member genes are well-connected hubs. Conditioning PPR GSEA (B3b, AP = 0.088) shows that applying BIFO conditioning to the gene-level scores before GSEA does not substantially improve this, because the bottleneck is the gene-to-pathway scoring step rather than the propagation itself. The improvement from B3b (AP = 0.088) to BIFO-PPR full-arm (AP = 0.408) therefore isolates the specific contribution of scoring pathway nodes directly via the bridge layer rather than aggregating gene-level scores.

Taken together, standard enrichment methods fail at both ends of the gene set size spectrum for this benchmark: seed Fisher is unstable with ten genes, and neighborhood Fisher loses all discriminating power with 11,000. BIFO avoids both failure modes by concentrating signal through conditioned propagation before scoring, and by scoring pathway nodes directly rather than through gene-level intermediates.

## 5 Recovery controls: C4 pathway-split benchmarks

The CHD curated benchmark is a discovery task: seed genes are transcription factors and structural cardiac genes that do not directly overlap the target pathway family. To evaluate BIFO independently of disease-gene curation and in a setting where the answer is known by construction, two recovery benchmarks were added. In a recovery benchmark, seeds are drawn directly from the members of a known pathway, and the correct answer (that pathway and its family) is specified before the analysis runs. This design tests a different question from the CHD benchmark: not whether BIFO can find a biologically relevant pathway from disease genes, but whether it can correctly identify the source pathway when the seeds are already members of it. Because the seed genes overlap substantially with the target pathway by construction, the raw PPR arm already has direct proximity to the target, and negative rank improvement is expected. The relevant metrics in this setting are whether the source pathway ranks first and how coherently the broader pathway family is recovered.

  ----------------------------- ----------- ------------- ----------------- ---------- ------------------ ------------- -----------------
  **Context (task type)**       **Seeds**   **Heldout**   **Ref. paths.**   **P@10**   **Enrich.10**   **BIFO AP**   **Source rank**

  CHD curated (discovery)       10          5             18                0.70       21.4×              0.408         1

  C4/Notch (recovery)           30          14            11                0.50       25.0×              0.450         1

  C4/MAPK (recovery)            63          28            10                0.10       5.5×               0.174         1
  ----------------------------- ----------- ------------- ----------------- ---------- ------------------ ------------- -----------------

**Table 5.** *C4 pathway-split controls compared with the CHD curated benchmark. Task type: recovery = seeds drawn directly from target pathway members. Source rank: rank of the source pathway under BIFO-PPR full-arm scoring. Rank improvement is not shown for C4 controls because negative values are expected by design when seeds overlap the target pathway; see text.*

### 5.1 C4/Notch: recovering a coherent cardiac signaling pathway

Notch signaling was chosen as the first recovery control because it is a well-defined, biologically coherent pathway with clear cardiac relevance: Notch pathway mutations are among the best-characterized causes of congenital heart defects, making it a meaningful test of whether BIFO can recover a pathway family that is directly connected to the disease biology used in the CHD benchmark. Seeds were 30 genes drawn from REACTOME_SIGNALING_BY_NOTCH (44 total members), with 14 members withheld as held-out genes. If BIFO is working correctly, the source pathway should rank first and the broader Notch family should be coherently recovered in the top results.

BIFO-PPR ranked REACTOME_SIGNALING_BY_NOTCH first of 563 pathways, with three additional Notch-family pathways in the top 10 (P@10 = 0.50, enrichment = 25.0×, AP = 0.450). P@10 = 0.50 means 5 of the top 10 ranked pathways belong to the Notch reference family, at 25 times the background rate. AP = 0.450 indicates that Notch-family pathways are recovered coherently throughout the full ranked list, not just clustered at the top. Seed-only Fisher and neighborhood Fisher both produced P@10 = 0.000 in this setting, while raw PPR GSEA achieved P@10 = 0.40 but AP = 0.308. BIFO's AP advantage over raw GSEA (0.450 vs. 0.308) reflects more coherent ordering of the full Notch pathway family at deeper ranks.

### 5.2 C4/MAPK: recovering a broader, less cohesive pathway family

The MAPK control was designed to test BIFO under harder recovery conditions: MAPK signaling cascades form a broader, more heterogeneous family than Notch, with membership spread across many functionally distinct processes. Unlike the Notch control, which tests recovery within a tight, well-annotated signaling family with direct cardiac relevance, the MAPK control asks whether BIFO can recover a pathway family that is structurally diffuse and biologically unrelated to the CHD seed set. If BIFO is sensitive to pathway family cohesion in the way we expect, performance here should be weaker than in the Notch control.

Seeds were 63 genes from REACTOME_MAPK_FAMILY_SIGNALING_CASCADES (91 total members), with 28 held out. BIFO-PPR ranked the source pathway first, recovering it correctly, but P@10 = 0.10 and AP = 0.174, substantially weaker than the Notch control. A P@10 of 0.10 means only 1 of the top 10 ranked pathways belonged to the MAPK reference family, reflecting the structural diffuseness of the MAPK family across the graph. Neighborhood Fisher achieved P@10 = 0.10 with AP = 0.164, a rare case where neighborhood expansion is partially competitive. This occurs because MAPK pathway connectivity is partially accessible through the immediate graph neighborhood, unlike the CHD discovery task where neighborhood expansion inflates the query to the full gene universe and eliminates all discriminating power. BIFO's modest AP advantage (0.174 vs. 0.164) is consistent with the two methods drawing on overlapping information when the target pathway is structurally accessible without propagation.

### 5.3 Interpretation

In both C4 controls BIFO correctly identifies the source pathway at rank 1 regardless of pathway family cohesion. The contrast between C4/Notch and C4/MAPK is itself informative: tightly defined pathway families with coherent graph structure are recovered more completely than broad, heterogeneous ones, and this difference scales with biological cohesion rather than seed set size (C4/MAPK had more seeds than C4/Notch but lower recovery). Together with the CHD discovery benchmark, these results show that BIFO operates consistently across both task types, with its largest advantage over standard methods in the discovery setting where propagation must bridge the gap between seed genes and a pathway family that does not directly overlap them.

![
**C4 pathway-split controls, curated CHD benchmark.**
Two pathway-family controls using seeds drawn from curated pathway gene lists rather than CHD variant genes. C4/Notch: 30 Notch pathway seeds against 11 Notch reference pathways (recovery task). C4/MAPK: 63 MAPK seeds against 10 MAPK reference pathways (orthogonal control).
(**A**) Precision@10: Notch 0.50, MAPK 0.10.
(**B**) Enrichment@10 over background: Notch 25.0×, MAPK 5.5×.
(**C**) Mean rank of target pathways under BIFO-PPR-conditioned vs. raw PPR. Raw PPR achieves lower mean rank in both controls because seeds already have direct proximity to the target pathway.
(**D**) Rank improvement is negative in both controls (Notch -31.5, MAPK -54.4), as expected when seeds are drawn from the target pathway's own membership. This contrasts with the +125.4 rank improvement in the CHD discovery benchmark, where seeds are not pathway members and conditioning must bridge the gap between the molecular and pathway layers.
](images/fig5_c4_controls.png){#fig:c4_controls width="100%"}

## 6 Robustness to seed set composition: exhaustive resampling

The primary CHD benchmark used a single hand-curated 10-gene seed set. Any single seed configuration raises a legitimate question: are the results specific to those particular genes, or would BIFO-PPR recover CHD-relevant pathways from other reasonable starting points drawn from the same gene pool? To answer this directly, we evaluated all possible seed configurations rather than sampling a subset. The 15-gene CHD pool (10 original seeds plus 5 held-out genes) yields exactly C(15,10) = 3,003 possible 10-gene/5-gene partitions. Evaluating all 3,003 exhaustively, rather than bootstrapping a sample, means the stability result is exact rather than estimated.

  ------------------------ ----------- ---------- ----------- ----------- ------------ ------------ ------------
  **Metric**               **Mean**    **SD**     **Min**     **P25**     **Median**   **P75**      **Max**

  BIFO-PPR P@10            0.430       0.121      0.000       0.300       0.400        0.500        0.700

  BIFO-PPR Enrichment@10   13.46×      3.77       0.0×        9.4×        12.5×        15.6×        21.9×

  BIFO-PPR NDCG@10         0.518       0.131      0.000       0.447       0.542        0.605        0.757

  BIFO-PPR Avg. Precision  0.308       0.061      0.142       0.270       0.312        0.353        0.438

  Rank improvement         +118.3      16.8       +57.7       +107.4      +118.4       +129.8       +166.0

  Gene AUPRC               0.868       0.121      0.354       0.822       0.877        0.967        1.000

  Seed Fisher AP           0.351       0.062      0.171       0.308       0.350        0.394        0.532
  ------------------------ ----------- ---------- ----------- ----------- ------------ ------------ ------------

**Table 6.** *Distribution of BIFO-PPR pathway metrics across all 3,003 exhaustive seed partitions of the 15-gene CHD pool. All splits use identical conditioning (alpha=0.5), 563-pathway universe, and 18-pathway CHD reference. Rank improvement = mean_rank(raw) minus mean_rank(conditioned); positive values indicate conditioning improves pathway rank. Seed Fisher AP is an internal comparator within the split space and is not numerically comparable to the Table 4 Fisher baseline, which uses a different query construction.*

### 6.1 Rank improvement is positive across every split

Rank improvement was positive in all 3,003 splits, ranging from +57.7 to +166.0 with a mean of +118.3. This means that BIFO conditioning improved the relative position of CHD-relevant pathways compared to unconditioned propagation in every single seed configuration tested, not just in the primary benchmark split. The consistency of this result across the full partition space establishes that the conditioning benefit is a property of the graph and the BIFO flow class mapping, not of the specific genes that happened to be chosen as seeds.

### 6.2 Pathway precision is stable across nearly all configurations

Median P@10 across all 3,003 splits was 0.40, meaning the typical seed configuration recovers 4 of the top 10 ranked pathways from the 18-pathway CHD reference set. In 94.4% of splits (2,835 of 3,003), P@10 was at least 0.30, meaning at least 3 of the top 10 were disease-relevant. In 43.8% of splits (1,314 of 3,003), P@10 was at least 0.50. Even in the least favorable splits, where P@10 reached a minimum of 0.00, BIFO-PPR retained detectable pathway signal above background in nearly all configurations. Average precision ranged from 0.142 to 0.438 with a median of 0.312, indicating that CHD reference pathway recovery is consistent throughout the ranked list across essentially all seed configurations, not just at the top.

### 6.3 Position of the primary benchmark split

The primary split (GATA4, NKX2-5, TBX5, NOTCH1, NOTCH2, HAND1, HAND2, MYH6, GATA6, TBX1 as seeds) achieved P@10 = 0.70 and AP = 0.409, placing it at the maximum P@10 observed and at the 98th percentile of AP across all 3,003 splits. Rank improvement for the primary split was +128.9, at the 74th percentile (median +118.4). The primary split is therefore a favorable but not exceptional configuration: it represents what a well-chosen set of canonical disease genes can achieve, while the distribution shows that the method works robustly across a much broader range of starting points.

### 6.4 Relationship to seed-overlap Fisher enrichment

BIFO-PPR achieved higher average precision than seed-overlap Fisher in 24.0% of splits (722 of 3,003). Fisher is competitive in this setting because many of the 15 CHD pool genes are directly annotated to cardiac pathways, so direct overlap enrichment works well when those genes are in the seed set. BIFO-PPR's advantage lies in recovering pathways that are connected to the seeds through the graph but do not directly overlap them. Across all splits, rank improvement under BIFO-PPR is consistently positive regardless of whether BIFO-PPR or Fisher achieves higher AP on a given split, indicating that graph conditioning adds value beyond overlap-based enrichment even when Fisher is competitive on a specific configuration.

![
**BIFO-PPR pathway recovery is stable across 3,003 seed partitions, curated CHD benchmark.**
Each split: 10 seeds and 5 held-out genes drawn from the 15-gene CHD pool. Primary split shown as red dashed line in each panel.
(**A**) Precision@10 distribution across all 3,003 splits. 94.4% of splits achieve P@10 at least 0.30; 43.8% achieve P@10 at least 0.50; primary split P@10 = 0.70.
(**B**) BIFO-PPR Average Precision distribution (primary = 0.408).
(**C**) Seed Fisher Average Precision distribution (primary = 0.431).
(**D**) Rank improvement distribution: all 3,003 splits show positive rank improvement (100% positive); primary split +128.9. BIFO-PPR beats Seed Fisher on AP in 24.0% of splits. All splits use identical conditioning operators and pathway universe; only the seed vector varies.
](images/fig6_resampling.png){#fig:resampling width="100%"}

## 7 Kids First cohort analysis: discovery-mode pathway recovery

Applied to two independent pediatric rare variant cohorts from the Kids First program, BIFO-PPR recovered WP_CILIOPATHIES as a top-ranked pathway in both congenital heart disease and neuroblastoma in full discovery mode, without any pre-specification of a cilia reference. In KF-CHD, WP_CILIOPATHIES ranked 43rd of 2,130 pathways with the strongest statistical enrichment signal among all well-calibrated pathways (null_z = 41.2, q = 0.008). In KF-NBL, it ranked 3rd of 2,196 pathways (null_z = 18.4, q = 0.014). Correctly implemented Fisher enrichment ranked WP_CILIOPATHIES first in both cohorts independently. The convergence of two methods across two biologically distinct diseases, using independent variant sets, supports an underlying biological signal rather than a propagation artifact.

### 7.1 The enrichment challenge at cohort scale

Rare variant aggregation across a disease cohort typically produces gene lists of 1,000 to 1,500 genes, far larger than the gene sets standard enrichment methods were designed for. At this scale, hypergeometric p-values collapse to near-zero floor values for a large fraction of pathways, compressing rank discrimination. As described in Methods Section 10, this problem is not unique to naive implementations: even with correct log-space computation, a gene list of this size and heterogeneity carries distributed enrichment structure because the biologically relevant signal spans a small subset of genes embedded in a large background of incidental carriers. Fisher identifies the top-hit overlap when the signal is strong enough -- as it does for WP_CILIOPATHIES in both KF cohorts -- but does not provide pathway-level statistical specificity (distinguishing signal from graph-topology artifacts) or coherent cluster recovery across the full cilia pathway family. BIFO-PPR adds these through the rewiring null and pathway-node scoring, which are structurally independent of direct gene-pathway overlap and therefore provide complementary rather than redundant evidence.

BIFO-PPR addresses this by propagating signal from all seeds simultaneously through the conditioned graph. Coherent biological signal from a functionally related gene subset, such as the 22 cilia-associated genes in the KF-CHD seed pool, concentrates at relevant pathway nodes while incoherent background signal from the remaining 1,254 genes diffuses away. The approach does not require the input gene set to be small or homogeneous.

### 7.2 KF-CHD: ciliopathy signal in congenital heart disease

The KF-CHD analysis used 1,276 resolved seed genes from 697 probands with congenital heart defects, scored against a universe of 2,130 pathways in full discovery mode. No reference pathway set was pre-specified; all pathways were scored and ranked, and results were evaluated post-hoc against a 16-pathway cilia reference set.


![
**Baseline enrichment method comparison, KF-CHD and KF-NBL cohorts.**
Five enrichment methods evaluated against the 16-pathway quantitative cilia reference set (metrics); 21-pathway extended set used for visualization context only.
(**A**) KF-CHD heatmap: five methods × five metrics (P@10, P@20, P@50, Average Precision, Mean Cilia Ref Rank). Colour scaled within each metric column; darker = better. Mean Ref Rank colour is inverted so lower rank shows darker.
(**B**) KF-NBL heatmap, same layout as A.
(**C**) WP_CILIOPATHIES rank under BIFO-PPR full-arm and Seed Fisher (corrected). Seed Fisher ranks WP_CILIOPATHIES first in both cohorts. BIFO-PPR ranks WP_CILIOPATHIES 43rd in KF-CHD (null_z = 41.2) and 3rd in KF-NBL (null_z = 18.4). Seed Fisher results use log-space hypergeometric computation; standard implementations cause p-value floor collapse in the large-seed regime.
](images/fig4_baseline_heatmap.png){#fig:baseline_heatmap width="100%"}

**BIFO-PPR results.** WP_CILIOPATHIES ranked 43rd of 2,130 pathways by degree_norm (degree_norm = 8.51×10⁻⁶), placing it in the top 2% of the scored universe. WP_JOUBERT_SYNDROME, a closely related ciliopathy pathway sharing many structural members, ranked 34th. The top-ranked pathways by degree_norm (Protein phosphorylation, REACTOME_CROSS_PRESENTATION, WP_NAD_METABOLISM, and others) reflect broad high-degree graph structure; they are distinguishable from the ciliopathy cluster by their null_z values near zero, indicating that their high scores reflect generic graph topology rather than specific biological signal.

**Statistical enrichment.** The pathway-node rewiring null establishes that WP_CILIOPATHIES carries the strongest statistical signal among all well-calibrated pathways: null_z = 41.2 (q = 0.008), meaning the observed degree_norm score is 41.2 standard deviations above the mean of 1,000 degree-preserving membership rewiring permutations. This directly tests whether the specific gene membership of WP_CILIOPATHIES drives the signal, rather than graph topology alone. The member-level null (member_mean null_z = 1.39, p = 0.057) indicates that signal is concentrated primarily at the pathway node rather than distributed uniformly across all 170 member genes, consistent with a subset of cilia-associated variant genes driving mass to the ciliopathy cluster through the mechanistic network.

Degree_norm and null_z are complementary measures rather than interchangeable rankings. Degree_norm provides absolute prioritization across all pathways; null_z tests statistical specificity relative to a graph-specific null. WP_CILIOPATHIES ranks 43rd by degree_norm because large, highly connected hub pathways accumulate more absolute propagated signal, but it ranks first by null_z because its signal is specifically attributable to its gene membership rather than to graph structure. Both pieces of evidence are needed: rank alone does not establish specificity, and null_z alone does not establish that the pathway scores above the bulk of the universe.

**Ciliopathy cluster.** BIFO-PPR recovers a coherent cluster of cilia-related pathways. Of 16 matched cilia, ciliopathy, and related pathway annotations in the scored universe, 8 (50%) rank in the top half. The core ciliopathy pathways show the strongest enrichment: WP_JOUBERT_SYNDROME (rank 34), WP_CILIOPATHIES (rank 43, null_z = 41.2), REACTOME_ANCHORING_OF_THE_BASAL_BODY_TO_THE_PLASMA_MEMBRANE (rank 95, null_z = 30.0), REACTOME_CILIUM_ASSEMBLY (rank 163, null_z = 18.5), and WP_GENES_RELATED_TO_PRIMARY_CILIUM_DEVELOPMENT_BASED_ON_CRISPR (rank 171, null_z = 17.9). Notably, generic Hedgehog signaling pathways not specific to cilia show negative null_z values, indicating depletion rather than enrichment. The cilia signal in KF-CHD is therefore specific to ciliary structure and basal body function rather than reflecting broad Hedgehog transcriptional programs.

**Fisher as independent validation.** Seed-only Fisher enrichment, correctly implemented with log-space computation and a pathway-member gene universe (as described in Methods Section 7), ranked WP_CILIOPATHIES first of 2,130 pathways (BH p = 4.53×10⁻³¹, overlap = 61/170 members), with WP_GENES_RELATED_TO_PRIMARY_CILIUM_DEVELOPMENT_BASED_ON_CRISPR 3rd and WP_JOUBERT_SYNDROME 4th. The concordance between BIFO-PPR and Fisher on the top cilia hit is reported here as independent validation of the biological signal rather than a head-to-head competition: the two methods recover the same pathway by fundamentally different mechanisms (propagation vs. direct overlap), which strengthens the case that the signal reflects underlying biology. Neighborhood Fisher failed entirely because the 1-hop neighborhood expands to approximately 58,846 genes, eliminating all discriminating power. Preranked GSEA on raw and conditioned PPR scores ranked WP_CILIOPATHIES at positions 1,994 and 456 respectively, showing that gene-level PPR scores without pathway-node degree normalization do not concentrate signal on the ciliopathy cluster.

  ----------------------------- -------------------------- --------------------------- ---------------------------------------------
  **Method**                    **WP_CILIOPATHIES rank**   **Top-5 includes cilia?**   **Key statistic**

  Seed Fisher (B1, corrected)   1 / 2,130                  Yes (ranks 1, 3, 4)         BH p=4.53×10⁻³¹; overlap=61/170

  Neighborhood Fisher (B2)      not top-50                 No                          58,846-gene neighborhood; no discrimination

  Raw PPR GSEA (B3)             1,994 / 2,130              No                          Gene-level PPR insufficient

  Conditioned PPR GSEA (B3b)    456 / 2,130                No                          Conditioned scores insufficient

  BIFO-PPR (B4)                 43 / 2,130                 Yes (top 2%)                degree_norm=8.51×10⁻⁶; null_z=41.2; q=0.008
  ----------------------------- -------------------------- --------------------------- ---------------------------------------------

**Table 7.1.** *KF-CHD method comparison. WP_CILIOPATHIES rank and cilia pathway recovery under five enrichment methods. Fisher top-5: WP_CILIOPATHIES (1), REACTOME_DISEASES_OF_METABOLISM (2), WP_PRIMARY_CILIUM_CRISPR (3), WP_JOUBERT_SYNDROME (4), REACTOME_DISORDERS_TRANSMEMBRANE (5). BIFO-PPR top-5 by degree_norm: Protein phosphorylation (1), REACTOME_CROSS_PRESENTATION (2), WP_NAD_METABOLISM (3), REACTOME_FREE_FATTY_ACIDS (4), WP_ARYL_HYDROCARBON_RECEPTOR (5).*

### 7.3 KF-NBL: independent replication in neuroblastoma

The KF-NBL analysis used 1,395 resolved seed genes from 460 probands with neuroblastoma, scored against a universe of 2,196 pathways. The cohort is biologically distinct from KF-CHD: neuroblastoma is a tumor of neural crest origin, and the KF-NBL seed set contains a prominent DNA repair component (ATM, ATR, ATRX, BARD1, BLM, BRCA2, BRIP1, APTX) not present in the CHD cohort. The question is whether BIFO-PPR recovers the same ciliopathy signal in a different disease context using an independent variant set.

WP_CILIOPATHIES ranked 3rd of 2,196 pathways by degree_norm (degree_norm = 4.24×10⁻⁶, null_z = 18.4, q = 0.014), with WP_JOUBERT_SYNDROME ranking 17th. The top two pathways by degree_norm were GO terms reflecting broader membrane transport biology (Ionophore activity, Transmembrane Transport), consistent with the broader neuronal character of the NBL seed neighborhood. Seed-only Fisher ranked WP_CILIOPATHIES first of 2,196 pathways (BH p = 3.85×10⁻³²), replicating the KF-CHD Fisher result in an independent cohort.

The member-level null for KF-NBL shows significant signal (member_mean null_z = 2.43, p = 0.003), in contrast to KF-CHD where member-level signal did not reach significance (p = 0.057). This difference is consistent with the cilia signal being more distributed across pathway member genes in NBL than in CHD, reflecting a different composition of cilia-associated variant genes between the two cohorts rather than a stronger overall signal. The pathway-node null_z in KF-NBL (18.4) is lower than in KF-CHD (41.2), consistent with WP_CILIOPATHIES ranking higher by degree_norm in NBL (rank 3 vs. rank 43) and therefore having a smaller gap between its observed score and the scores of hub pathways above it.

### 7.4 Cross-cohort convergence

The choice of these two particular cohorts is not arbitrary. Children with congenital heart disease have elevated neuroblastoma risk, potentially due to shared neural crest developmental origins [@doi:10.1002/1545-5017.70055], and children with neural crest-origin birth defects including selected congenital heart defects are approximately three times as likely to be diagnosed with neuroblastoma compared to children without a birth defect [@doi:10.1002/pbc.30732]. GWAS analyses have identified shared genetic architecture between neuroblastoma and ventricular septal defect, with shared susceptibility loci regulating genes involved in neural crest cell formation including BARD1, MSX1, and SHOX2 [@doi:10.3390/genes10090663]. The epidemiological and genetic co-occurrence of these two diseases frames our cross-cohort comparison not as two unrelated diseases that happen to share a pathway hit, but as two manifestations of a shared developmental vulnerability in neural crest-derived tissues. Primary cilia are required for normal neural crest cell migration, cardiac septation, and left-right asymmetry, making them a biologically plausible shared mechanism. The convergent recovery of WP_CILIOPATHIES under both BIFO-PPR and correctly implemented Fisher enrichment in independent variant sets from both diseases is therefore consistent with a shared biological signal rather than coincidence.

Table 7.4 summarizes the key cross-cohort metrics.

  --------------------------------------------- ----------------------------- -----------------------------
  **Metric**                                    **KF-CHD**                    **KF-NBL**

  Seed genes (MAF≤0.001, n≥1)                   1,276                         1,395

  Conditioned edges                             2,482,752                     2,647,055

  Pathways scored                               2,130                         2,196

  WP_CILIOPATHIES rank (BIFO-PPR)               43 / 2,130 (null_z=41.2)      3 / 2,196 (null_z=18.4)

  WP_CILIOPATHIES rank (Fisher, corrected)      1 / 2,130 (BH p=4.53×10⁻³¹)  1 / 2,196 (BH p=3.85×10⁻³²)

  Cilia seed genes in pool                      22                            19

  Inter-cohort gene overlap                     570 / 1,287 (44.3%)           ---
  --------------------------------------------- ----------------------------- -----------------------------

**Table 7.4.** *Cross-cohort comparison. WP_CILIOPATHIES and cilia pathway recovery under BIFO-PPR and corrected Fisher enrichment in KF-CHD and KF-NBL.*

The two cohort seed sets share 570 genes (44.3% of the CHD set), reflecting shared rare Mendelian disease gene carrier burden at MAF ≤0.001 across pediatric sequencing cohorts rather than disease-specific biology. This overlap could in principle explain cross-cohort concordance if the cilia signal were driven entirely by the shared genes. At a stricter carrier count filter (n≥2 carriers), overlap decreases to 30% while both cohorts retain significant WP_CILIOPATHIES enrichment, indicating that the cilia signal is present in both the shared and cohort-specific variant components and is not an artifact of inter-cohort gene overlap.

The convergence on the same top pathway is also consistent with the companion U24 cross-cohort analysis (Stear et al. 2026), which independently identified cilia enrichment in Kids First cohorts using permutation-based GSEA, providing external replication from a methodologically distinct approach.

Figure 8 shows the full rank vs. null_z landscape for all scored pathways in both cohorts. The cilia cluster occupies the upper-left region of both plots: high null_z at moderate degree_norm rank, clearly separated from the bulk of pathways whose null_z values cluster near zero. WP_CILIOPATHIES sits at the extreme upper left in KF-CHD (rank 43, null_z = 41.2) and near the top left in KF-NBL (rank 3, null_z = 18.4). Pathways ranking near the top by degree_norm but with null_z near zero represent hub pathways whose scores reflect generic graph topology.

![**Rank vs. statistical enrichment landscape, KF-CHD and KF-NBL cohorts.**
Each point is a scored pathway (grey: all pathways; blue: 16-pathway cilia reference set). X-axis: degree_norm rank (lower = better). Y-axis: pathway-node rewiring null_z (N = 1,000 permutations; pathways with degenerate null excluded). WP_CILIOPATHIES ranks 43rd/2,130 in KF-CHD (null_z = 41.2, q = 0.008) and 3rd/2,196 in KF-NBL (null_z = 18.4, q = 0.014). Degree_norm rank and null_z are complementary: rank reflects absolute propagated signal; null_z reflects signal relative to a graph-specific null. They are not interchangeable and null_z is not used for primary ranking.
](images/fig9_rank_vs_nullz.png){#fig:rank_vs_nullz width="100%"}

Full top-20 ranked pathways per method for KF-CHD and KF-NBL are provided in Supplementary Table ST3. Full cilia pathway cluster rankings are provided in Supplementary Table ST4. Head-to-head rank comparison between Fisher and BIFO-PPR for all scored pathways is provided in Supplementary Table ST5. Complete scored pathway results for all 2,130 KF-CHD pathways and 2,196 KF-NBL pathways, including per-pathway seed gene membership sorted by PPR score, PPR-normalized member scores, influential node z-score summaries (local and global), and neighbor z-score distribution quantiles, are provided as Supplementary Data SD1 (KF-CHD) and SD2 (KF-NBL). LLM-structured interpretation input documents are provided as Supplementary Tables ST8 (KF-CHD) and ST9 (KF-NBL). Biological interpretation of these results by Claude Opus 4.7 and GPT-5.3 is provided in Supplementary Section S1 and in the main text file `08.llm_interpretation.md` in the manuscript repository.

### 7.5 Bootstrap resampling: cilia signal requires aggregate variant burden

The cohort-scale cilia signal raises a natural question: does recovery require the full 1,276 to 1,395-gene variant burden, or would a smaller random subset of genes be sufficient? To answer this, 500 bootstrap draws at each of three seed sizes (n=10, 20, 30) were made from each cohort's full seed pool, and both BIFO-PPR and Fisher were run on each draw using the identical pathway universe and cilia reference set.

  -------------------------- --------------- ----------------- ------------- --------------- ----------------------------- -------------------------------
  **Seed size**              **BIFO P@10**   **Fisher P@10**   **BIFO AP**   **Fisher AP**   **Any cilia top-10 (BIFO)**   **Any cilia top-10 (Fisher)**

  KF-CHD primary (n=1,276)   0.000           0.200             0.012         0.130           ---                           ---

  KF-CHD n=10 (500 runs)     0.008           0.018             0.013         0.013           6.6%                          13.0%

  KF-CHD n=20 (500 runs)     0.008           0.029             0.012         0.017           7.4%                          18.6%

  KF-CHD n=30 (500 runs)     0.011           0.035             0.014         0.021           9.0%                          21.0%

  KF-NBL primary (n=1,395)   0.100           0.200             0.044         0.099           ---                           ---

  KF-NBL n=10 (500 runs)     0.012           0.022             0.013         0.012           7.6%                          14.8%

  KF-NBL n=20 (500 runs)     0.012           0.025             0.013         0.016           9.0%                          15.6%

  KF-NBL n=30 (500 runs)     0.010           0.041             0.013         0.021           7.6%                          24.2%
  -------------------------- --------------- ----------------- ------------- --------------- ----------------------------- -------------------------------

**Table 7.5.** *Bootstrap resampling results. BIFO-PPR vs. Fisher cilia pathway recovery at reduced seed sizes (500 draws per seed size). P@10 and AP are computed against the 16-pathway cilia reference. Primary run rows use the full cohort seed set and are shown as reference points.*

Neither method reliably recovers cilia pathways from small random gene subsets, in contrast to the robust recovery observed at full cohort scale. At n=10 to 30 randomly drawn genes, P@10 is near zero for both methods (BIFO-PPR: 0.008 to 0.011; Fisher: 0.018 to 0.035 in KF-CHD). Fisher finds any cilia pathway in the top 10 in 13 to 21% of bootstrap runs at these seed sizes, compared to 7 to 9% for BIFO-PPR, making Fisher modestly more sensitive at small seed sizes. This reflects a mechanistic difference: Fisher recovers cilia pathways when seed genes directly overlap pathway members, which is more likely at small random samples than establishing distributed propagation signal across the cilia cluster. At cohort scale, both methods converge on WP_CILIOPATHIES as the top or near-top cilia pathway, but through fundamentally different mechanisms.

The core finding is that the cilia signal in these cohorts is distributed across many variant genes and requires aggregate cohort-scale burden to emerge reliably. No method recovers it consistently from 10 to 30 randomly drawn genes. This is itself a biological result: it means the signal is not driven by a single highly penetrant gene or a small cluster of genes, but by the collective contribution of many cilia-associated variant carriers across the cohort. BIFO-PPR's graph propagation and pathway-node scoring provide an independent view of that distributed signal, complementary to the direct overlap enrichment that Fisher uses to identify the strongest individual hit.

![
**Cross-cohort convergence: KF-CHD and KF-NBL independently recover cilia pathways.**
(**A**) WP_CILIOPATHIES ranks 43rd (KF-CHD) and 3rd (KF-NBL) under BIFO-PPR full-arm; ranks 1st under corrected Seed Fisher in both cohorts.
(**B**) BIFO-PPR pathway rank scatter (top 3,000 shown) with cilia pathways highlighted. Cilia pathways cluster in the top-left corner of both axes, indicating concordant prioritization across cohorts.
(**C**) Cilia pathway cluster: BIFO-PPR rank of each detected cilia-related pathway in KF-CHD (blue circle) vs. KF-NBL (orange triangle). Detected cilia pathways cluster in the upper portion of the scored pathway universe, with WP_CILIOPATHIES and the core ciliopathy cluster ranking highest in both cohorts.
(**D**) Bootstrap resampling against a 16-pathway cilia reference: P@10 distribution for BIFO-PPR (blue) and Seed Fisher (red) at seed sizes n=10, 20, 30 (500 runs per seed size). Cilia signal requires full cohort-scale seed sets; neither method recovers it reliably from 10 to 30 random genes.
](images/fig8_crosscohort.png){#fig:crosscohort width="100%"}


## Discussion

BIFO provides a formalism for functional inference from heterogeneous biomedical knowledge graphs, addressing two compounding problems that limit biological discovery in this setting. First, when mechanistic relationships, statistical associations, and annotation edges share a single graph structure, propagation treats them equivalently, making biologically meaningful signal indistinguishable from incidental connectivity. Second, standard enrichment methods fail at both extremes of the gene set sizes that modern genomics produces: small sets generate statistically unstable overlap, and large heterogeneous sets from rare variant aggregation cause p-value floor collapse or neighborhood inflation that eliminates all discriminating power. These problems compound in rare variant cohort analysis, where gene sets are large, signal is distributed, and the biological questions are most consequential. BIFO resolves the first problem by restricting propagation to edges that encode directed biological transformations and defining a formally distinct bridge class connecting the molecular layer to pathway annotations. It addresses the second by evaluating pathway-level signal at pathway concept nodes rather than through gene-level aggregation, remaining effective in regimes where standard methods lose discriminative power or pathway-level statistical specificity. In this paper we evaluate the framework in a gene-to-pathway inference setting using rare variant cohort data, but the underlying formalism applies to any feature-to-feature inference problem on a heterogeneous biological graph: drug-target inference, phenotype-to-pathway mapping, cross-species signal transfer, or any setting where the identifiability of causal from associative relationships limits inference.

A natural question is whether this complexity is necessary. If the goal is gene-to-pathway inference, why use a large heterogeneous knowledge graph rather than a simpler local network of genes and pathways? The ablation results provide a direct empirical answer. Removing mechanistic edges entirely (ablation arm, no bridge edges) still recovers pathway signal at P@10 = 0.60, but the full mechanistic-plus-bridge operator achieves P@10 = 0.70. The mechanistic layer contributes real signal: it structures the propagation substrate in a way that concentrates signal within biologically coherent gene neighborhoods before it transfers to the pathway layer through bridge edges. A flat gene-pathway bipartite graph, equivalent to running enrichment directly on pathway membership without propagation, would recover only what direct overlap provides, which is what the baseline comparisons show. The advantage of a richer graph is not complexity for its own sake but the ability to capture biological context that is not encoded in pathway membership alone. BIFO conditioning is what converts that complexity from a liability into an asset, by restricting traversal to biologically valid paths and preventing associative edges from diluting mechanistic signal.

A related question concerns the choice of graph substrate. Interaction databases such as STRING provide gene-gene edges and could in principle support a similar propagation approach when combined with pathway annotations. STRING predicates are classified in bifo_mapping.yaml and would be admitted as propagating edges if present in the graph. However, STRING was not included in the DDKG version used for these analyses, and the propagating edge set drawn from this graph spans ontology-aligned mechanistic sources (WikiPathways, GO, HGNC, GENCODE), disease-gene associations (OMIM, ClinGen), and drug-target relationships (LINCS), but not protein-protein interaction networks. Whether adding STRING or other interaction network sources to the propagation substrate improves pathway recovery is an open question that a planned STRING-augmented analysis will address directly. More broadly, the DDKG was chosen because its predicate-typed edges support the flow-class classification that BIFO conditioning requires; the same conditioning logic applies to any property graph whose edges carry compatible predicate annotations.

### The two-layer graph architecture

The three-arm ablation reveals something about the structure of ontology-aligned biomedical knowledge graphs that extends beyond this benchmark. In the present DDKG export, pathway nodes are structurally inaccessible from gene nodes through mechanistic edges alone. Signal propagating through gene-gene regulatory relationships, transcription, protein interactions, and disease-gene associations has no path to pathway concept nodes without bridge edges. This is not a gap in the mechanistic coverage of the graph. It is a consequence of how curated pathway knowledge is represented: pathway membership is encoded as a distinct relationship type that connects the molecular layer to the pathway annotation layer, and that relationship type occupies a structurally separate role from mechanistic gene-gene relationships.

This two-layer architecture has a practical implication for any graph-based inference method operating on similar representations. Propagation methods that do not explicitly admit bridge edges as a propagation-eligible class will produce zero pathway scores regardless of how rich the mechanistic layer is. The contribution of BIFO is not to add information to the graph but to make the admissibility decision explicit: bridge edges are formally defined as a propagation-eligible class, signal flows unidirectionally from gene nodes to pathway nodes, and the conditioning operator encodes this asymmetry in the adjacency matrix. Without this explicit admission, the two layers remain structurally disconnected for propagation purposes even when the edges connecting them are present in the graph.

The mechanistic-only arm establishes this result directly. It is not intended as a competitive baseline. Its purpose is to prove that the zero-score outcome is structural, which is what justifies BIFO's admission of bridge edges as a formally defined class rather than treating them as an implementation detail. A reviewer might ask: if mechanistic-only propagation yields zero pathway scores, what is the point of including mechanistic edges at all? The ablation arm answers this: mechanistic edges concentrate signal within biologically coherent gene neighborhoods before it transfers to the pathway layer through bridge edges, contributing a measurable improvement in pathway recovery (P@10 = 0.60 vs. 0.70 without vs. with bridge edges in the full arm). The mechanistic layer does not reach pathway nodes directly, but it shapes the signal that bridge edges ultimately transfer.

### Propagation and scoring as distinct contributions

The baseline comparisons isolate two separable contributions to pathway recovery performance. The first is signal concentration through conditioned propagation. The second is pathway-level scoring via direct accumulation at pathway concept nodes rather than aggregation of gene-level scores.

Conditioned PPR GSEA (B3b) uses BIFO-conditioned gene-level scores as input to standard GSEA, achieving AP = 0.088. BIFO-PPR full arm achieves AP = 0.408 on the same conditioned graph. The difference isolates the contribution of the degree_norm scoring function: scoring pathway nodes directly via the bridge layer is substantially more effective than aggregating conditioned gene-level scores through GSEA. This is because GSEA operates on a ranked gene list and does not require signal to accumulate at pathway concept nodes: it can find enrichment through any combination of member gene ranks. BIFO-PPR requires signal to travel through the bridge layer and arrive at the pathway node, which is more demanding but more specific. Pathways that score highly under BIFO-PPR have received propagated signal specifically because their member genes are connected to the seed neighborhood through admissible paths. Pathways that score highly under GSEA may do so because their member genes happen to rank well in the gene-level score distribution for reasons unrelated to pathway-specific signal.

The degree_norm normalization contributes a second specificity gain. Large, highly connected pathways accumulate more propagated signal simply by having more member genes contributing bridge edge mass to the pathway node. The square root penalty down-weights this size effect without fully normalizing it away, preserving signal in pathways that are both large and biologically coherent while suppressing generic hub pathways. The rank vs. null_z landscape in Figure 8 illustrates the result: degree_norm rank and null_z are complementary rather than redundant. Pathways at the top of the degree_norm ranking but with null_z near zero are hub pathways whose scores reflect graph topology. WP_CILIOPATHIES ranks 43rd by degree_norm but carries the highest null_z (41.2) in KF-CHD, indicating that its signal is specifically attributable to its gene membership rather than to its size or connectivity.

### The KF cohort finding and its biological interpretation

The recovery of WP_CILIOPATHIES as the top statistically enriched pathway in both KF-CHD and KF-NBL is consistent with shared developmental biology rather than a methodological artifact, for three independent reasons. First, the signal is recovered by two methods with fundamentally different mechanisms: BIFO-PPR through graph propagation and Fisher enrichment through direct gene-pathway overlap. Their concordance on the same top pathway supports that the result reflects the underlying gene set rather than propagation-specific behavior. Second, the signal requires aggregate cohort-scale variant burden: bootstrap resampling shows that neither method recovers cilia pathways reliably from 10 to 30 randomly drawn genes, establishing that the signal is distributed across many variant carriers rather than driven by a single gene or small cluster. Third, the cross-cohort convergence is biologically motivated: children with congenital heart disease have elevated neuroblastoma risk due to shared neural crest developmental origins [@doi:10.1002/1545-5017.70055], and shared genetic architecture between neuroblastoma and ventricular septal defect has been identified at loci regulating neural crest cell formation [@doi:10.3390/genes10090663]. Primary cilia are required for neural crest cell migration, cardiac septation, and left-right asymmetry, making them a mechanistically coherent shared vulnerability across both diseases.

The distinction between degree_norm rank and null_z is biologically important in interpreting the KF results. WP_CILIOPATHIES ranks 43rd in KF-CHD, placing it in the top 2% of 2,130 pathways, but it does not appear in the top 10. The top-ranked pathways by degree_norm include broad hub terms (protein phosphorylation, transmembrane transport, cross-presentation) that accumulate high propagated signal through graph connectivity rather than specific biological relevance to the seed set. WP_CILIOPATHIES has the highest null_z of any well-calibrated pathway (41.2), meaning its score is 41 standard deviations above what is expected from degree-preserving random rewiring of its membership. This establishes that the cilia signal is specific to the gene membership of WP_CILIOPATHIES rather than to its position in the graph. In KF-NBL, WP_CILIOPATHIES ranks 3rd by degree_norm and also carries the highest null_z (18.4), suggesting the NBL seed neighborhood has stronger direct cilia connectivity than the CHD neighborhood, consistent with the neural crest origin of neuroblastoma.

To illustrate the exploratory biological interpretation use case enabled by structured BIFO-PPR outputs, the complete scored pathway results for both KF cohorts, including per-pathway seed gene membership sorted by PPR score, PPR-normalized member scores, influential node z-score summaries (local and global), and a structured analytical task framework, were provided to two large language models (Claude Opus 4.7 and GPT-5.3) in isolated chat sessions.

LLM-based interpretation is not part of the BIFO-PPR pipeline and plays no role in the computation of pathway scores, ranking, or statistical significance. It represents a downstream, user-driven analysis step with BIFO-PPR structured output files. These interpretations are provided verbatim and are not edited or optimized, in order to preserve transparency of the interaction. In these sessions, we requested that the LLMs evaluate each cohort as independent evaluations without using other chats as reference.

Both GPT and Claude models independently identified ciliopathy signal as an important theme in both CHD and NBL cohorts, identified DNA repair burden as a secondary theme in KF-NBL, flagged non-obvious network driver genes (E2F1, CD36) in KF-CHD, and issued appropriate skeptical caveats about single-gene-dominated pathways and pathway redundancy. This indicates that BIFO-PPR outputs are structured in a way that supports automated or semi-automated biological interpretation, without requiring the method itself to incorporate any learned model.

LLM interpretations are prompt- and model-dependent and are included for illustrative purposes only, not as reproducible or statistical evidence. The structured output format and analytical task instructions are described in Supplementary Tables ST8 and ST9; verbatim LLM responses are in Supplementary Section S1.

The Hedgehog depletion finding adds biological precision. Generic Hedgehog signaling pathways show negative null_z values in KF-CHD, indicating depletion rather than enrichment, while cilia-specific pathway terms (basal body anchoring, cilium assembly, intraflagellar transport) show strong positive null_z values. This specificity, with cilia structure and trafficking enriched and broad Hedgehog transcriptional programs depleted, is consistent with the known biology: primary cilia are the cellular compartment in which Hedgehog signaling is transduced, but the developmental vulnerability in these cohorts appears to map to the structural and trafficking functions of the cilium rather than to downstream Hedgehog transcriptional output.

### Relationship to standard methods

BIFO-PPR is not a replacement for standard enrichment methods. It is most useful in settings where those methods lose specificity or coherent pathway-cluster recovery: when gene sets are large and heterogeneous, when relevant pathways are connected to seed genes indirectly through biological relationships rather than through direct membership overlap, and when the goal is discovery rather than confirmation of a pre-specified pathway family. In the curated CHD benchmark, correctly implemented Fisher enrichment achieves P@10 = 0.30, a meaningful result that identifies three of the top ten pathways correctly. BIFO-PPR improves on this substantially (P@10 = 0.70), but Fisher is not failing; it is operating at the limits of what direct overlap can provide with ten seed genes. In the KF cohort analyses, correctly implemented Fisher independently ranks WP_CILIOPATHIES first in both cohorts. BIFO-PPR and Fisher converge on the same top result through different mechanisms, which strengthens rather than undermines the biological conclusion.

The regime where BIFO-PPR provides the largest practical advantage is the large rare variant cohort setting, where standard enrichment collapses numerically under standard-precision computation and provides weaker statistical specificity and pathway-cluster coherence than graph-based approaches. At 1,276 to 1,395 seed genes, hypergeometric p-values collapse to zero for virtually every pathway with any overlap under standard-precision computation. Correctly implemented log-space Fisher recovers the top cilia hit in both cohorts but provides less pathway-cluster specificity and lacks a null model for distinguishing signal from graph-topology artifacts. BIFO-PPR addresses this by propagating signal from all seeds simultaneously through the conditioned graph, concentrating the coherent biological contribution of the cilia-associated gene subset at relevant pathway nodes while the incoherent background diffuses away. This is not the only setting where BIFO-PPR would be useful: any feature-to-feature inference problem on a heterogeneous graph with the same identifiability challenge would benefit from the same conditioning approach, but it is the setting where the advantage over standard methods is most clearly visible in this paper.

### Graph substrate and source vocabulary selection

The analyses reported here used a specific DDKG export that integrates ontology-aligned mechanistic and pathway sources while excluding association-derived evidence layers (age-stratified gene-disease associations, clinical mutation associations, genomic variant associations). This exclusion was deliberate: isolating mechanistic and pathway representations from association-derived layers enables clean attribution of pathway score changes to specific edge classes in the ablation design. Had association layers been included, the mechanistic-only arm result would have been less interpretable.

The propagating edge set in the benchmark analysis draws from WikiPathways gene-gene interactions, GO biological process annotations, HGNC and GENCODE gene-product relationships, OMIM and ClinGen disease-gene associations, LINCS drug-target correlations, and MSigDB and WikiPathways pathway membership edges. Notably absent are GTEx coexpression edges, which were exported in the 1-hop neighborhood but correctly classified as observational by BIFO conditioning and excluded from propagation. STRING protein-protein interaction edges are classified in bifo_mapping.yaml and would be admitted as propagating edges if present, but STRING was not included in the DDKG version used for these analyses. A STRING-augmented analysis is planned to directly test whether adding PPI edges to the propagation substrate improves pathway recovery.

The full attribution of propagating edges to source vocabularies (which SABs contributed which predicates at what counts) is provided in Supplementary Table ST6. This characterization is relevant to reproducibility: results may differ on DDKG versions with different SAB selections, and the edge composition of the propagating operator is a determinant of pathway scoring outcomes. Future analyses incorporating additional source vocabularies, including STRING, GTEx eQTLs, and expanded disease-gene association layers, will require re-evaluation of BIFO flow class assignments for the new predicate types introduced.

### Null calibration and statistical validity

BIFO-PPR pathway scores are made actionable by the membership rewiring null, which tests whether a pathway's observed score exceeds what is expected given the propagated signal landscape. A finding that emerges from these analyses is that statistical validity in graph-based inference depends not only on the scoring function but on the structure of the propagation operator itself. When bridge edges dominate the propagating graph, rewiring effectively randomizes the dominant routing structure and the null distribution inflates, reducing the discriminative power of the significance test. When non-bridge mechanistic edges provide sufficient routing constraint, rewired bridge assignments that do not match the biological structure of the seed set produce low pathway scores, and the null is well-separated from observed scores.

In the benchmark (76.7% bridge edges), the null is valid because with only 10 seeds, random rewirings rarely replicate specific cardiac signal regardless of bridge fraction. In KF-CHD (41.4% bridge edges under the corrected unidirectional pipeline), sufficient non-bridge routing constraint exists for valid null calibration, and WP_CILIOPATHIES achieves the highest null_z in the dataset (41.2, q = 0.008). The same holds for KF-NBL (null_z = 18.4, q = 0.014). These results indicate that the rewiring null provides valid statistical inference when the unidirectional bridge edge configuration is enforced.

The member-level stratified null provides complementary evidence that does not depend on bridge edge fraction, because it operates on the fixed propagated signal rather than the propagation operator. In KF-CHD, member-level null_z = 1.39 (p = 0.057), indicating signal concentrated primarily at the pathway node rather than distributed across member genes, consistent with a subset of cilia variant genes driving mass to the ciliopathy cluster through the mechanistic network. In KF-NBL, member_mean null_z = 2.43 (p = 0.003), suggesting more distributed signal across pathway member genes, consistent with the broader neural crest character of the NBL seed neighborhood. The two nulls are therefore not redundant: the pathway-node rewiring null tests direct signal accumulation at the pathway concept node; the member-level null tests whether that pathway's constituent genes carry disproportionate propagated signal. Their convergence in KF-NBL and partial convergence in KF-CHD together support that the ciliopathy signal is not explained by graph topology alone.

### Limitations and scope

The benchmark graph is a controlled 1-hop projection of the DDKG using a specific SAB selection. Results are specific to this graph slice and should not be generalized to the full DDKG without validation on expanded exports. The finding that pathway nodes are structurally inaccessible under mechanistic-only propagation applies to this graph configuration; it may change with additional SAB selections that introduce direct mechanistic gene-pathway edges from other source vocabularies.

The SAB selection used here was designed to isolate ontology-aligned mechanistic and pathway representations from association-derived evidence layers, enabling clean attribution in the ablation design. It was not a comprehensive survey of available DDKG content. The contribution of individual source vocabularies to pathway scoring outcomes (which SABs drive which signals) has not been fully characterized and is identified as a priority for future analysis (Supplementary Table ST6 provides the predicate-level breakdown as a starting point). Results may differ on DDKG versions with different SAB coverage, and characterizing BIFO conditioning behavior across graph substrates is a natural direction for follow-on work.

Gene-level recovery metrics are near ceiling in the curated benchmark due to the small held-out set and strongly connected seed neighborhood. These metrics become more discriminating at cohort scale with variant-derived seeds. BIFO as implemented here is best understood as a biologically constrained propagation framework with a reference DDKG implementation rather than a formal ontology in the description-logic sense; the flow class vocabulary and admissibility rules constitute an operational specification that can be extended or reconfigured for other graph representations.

The 15-gene CHD benchmark pool is curated from prior knowledge, which bounds generalization claims beyond this illustrative benchmark. The exhaustive 3,003-split resampling addresses seed-composition sensitivity within this pool but does not substitute for an independent benchmark on a different disease or knowledge graph. The Kids First cohort results provide independent biological validation in the large gene set regime but rely on the same underlying graph and BIFO configuration. Validation on additional disease cohorts, knowledge graph versions, and graph substrates remains important future work.

### Conclusion

BIFO provides a principled approach to a problem that affects any inference task on heterogeneous biological graphs: the inability to distinguish biologically meaningful signal from incidental connectivity when mechanistic, associative, and annotation edges are treated equivalently. By making admissibility explicit at the level of the propagation operator, BIFO converts graph complexity from a liability into a structured substrate for biological inference. The two-layer architecture finding establishes that ontology-aligned pathway annotations occupy a structurally distinct layer from mechanistic gene relationships, and that explicit bridge admission is necessary for pathway-level inference regardless of how rich the mechanistic layer is. The KF cohort results show that this framework recovers biologically coherent signal at a scale and in a regime where standard methods lose discriminative power. The convergence of graph-based propagation and direct overlap enrichment on the same ciliopathy signal, across two diseases with known shared developmental vulnerability, supports that the recovered biology is real. Extending BIFO to additional graph substrates, source vocabularies, and inference tasks is the natural direction for this work.


## Supplementary Methods

### SM1: Variant Processing and Gene Aggregation

**Kids First harmonized sequencing and alignment.** Whole-genome sequencing (WGS) data were obtained from two independent germline cohorts: NIH dbGAP phs001138 (congenital heart defects, n=1121 total probands; n=697 with complete WGS data used in this analysis) and NIH dbGAP phs001436 (neuroblastoma, n=554 total probands; n=460 used in this analysis). All samples were sequenced on Illumina platforms using paired-end protocols. Raw sequencing reads were processed by the Kids First Data Resource Center pipelines, aligned to the human reference genome build GRCh38 using BWA (Burrows-Wheeler alignment) algorithms, and variant discovery was performed with the Genome Analysis Toolkit (GATK) Best Practices workflow. Cohorts were harmonized to ensure consistent reference build, alignment parameters, and variant-calling procedures. For cohorts originally processed using joint genotyping in family-based designs (e.g., trios or duos), multi-sample VCFs were decomposed into proband-sample VCFs for downstream per-individual filtering and aggregation. Cohorts sequenced as proband-only were retained as individual-level VCFs. All variants analyzed represent germline calls.

**Variant quality filtering.** 
Multi-allelic sites were split into biallelic records to ensure consistent downstream filtering and annotation. Variant-level and genotype-level quality control was performed using bcftools (v1.30) to ensure consistency across all cohorts. Only variants annotated with FILTER=PASS, as determined by the GATK variant quality score recalibration (VQSR) or hard-filtering framework, were retained. At the genotype level, we required a minimum genotype quality (GQ) of 20, corresponding to an estimated posterior genotype accuracy of ≥99%, and a minimum read depth (DP) of 10 reads to ensure adequate sequencing support at each locus. An initial broad population frequency filter of MAF ≤1% in gnomAD was applied at this stage to remove common variants unlikely to be disease-relevant, consistent with standard rare disease variant processing pipelines. Genotype-level filtering was applied prior to aggregation across individuals to ensure that only high-confidence variant calls contributed to downstream analyses.

**Pathogenicity classification.** To enrich for variants with predicted functional impact, we implemented a complementary pathogenicity prioritization strategy integrating both consequence-based and model-based annotations. First, variants were functionally annotated using the Ensembl Variant Effect Predictor (VEP) [@doi:10.1186/s13059-016-0974-4], incorporating transcript consequence, gene assignment, and predicted functional impact categories. Variants annotated by Ensembl VEP as having HIGH impact (including predicted loss-of-function consequences such as stop-gain, frameshift, and canonical splice-site variants) were retained. 
Second, variants were evaluated using AutoGVP [@doi:10.1093/bioinformatics/btae114], a supervised pathogenicity prediction framework that integrates functional, evolutionary, and annotation-based features. Variants classified as “Pathogenic” or “Likely_Pathogenic” by AutoGVP were retained. Variants meeting either criterion (VEP HIGH impact or AutoGVP “Pathogenic/Likely pathogenic” classification) were included in the final analysis set. This approach enabled capture of canonical loss-of-function alleles as well as predicted deleterious missense or regulatory variants with strong pathogenic support. Both annotation steps were performed against the GRCh38 reference and corresponding Ensembl gene models. The final analytical dataset comprised high-confidence germline variants that passed GATK variant-level filters, met stringent genotype-level depth and quality thresholds, and were predicted to be deleterious by VEP and/or AutoGVP. This harmonized filtering framework ensured consistent variant quality across both cohorts and enriched the dataset for variants with a high prior probability of functional relevance. All downstream gene-level aggregation, cross-cohort comparisons, and enrichment analyses were performed using this curated set of high-confidence pathogenic variants. 

**Population allele frequency filtering.** Variants were filtered against population allele frequency estimates from the Genome Aggregation Database (gnomAD) v3.1 [@doi:10.1038/s41586-020-2308-7], which provides allele frequencies across diverse global populations aligned to GRCh38. For this study, we applied a more stringent analytical threshold of MAF ≤0.001 (0.1%) using the gnomAD v3.1 non-cancer popmax allele frequency (the maximum allele frequency observed across any gnomAD ancestry group, excluding cancer cohorts). This threshold is tenfold more stringent than the initial processing filter, restricts analyses to ultra-rare variants consistent with Mendelian or strong-effect rare disease genetics, and matches the filtering parameters used in the companion U24 cross-cohort enrichment analysis (Stear et al., CFDE Meeting 2026). Variants exceeding this frequency threshold in any gnomAD ancestry group were excluded regardless of their pathogenicity classification.

**Gene aggregation.** For each cohort, genes harboring at least one qualifying P/LP variant in any proband were aggregated into a per-cohort gene list. Carrier count-filtered subsets requiring ≥2 or ≥3 independent probands carrying qualifying variants in the same gene were generated to assess signal stability under increasingly stringent filters.

**Background burden gene exclusion.** Twenty genes representing common carrier burden from well-characterized recessive Mendelian conditions were excluded from both cohort gene lists prior to pathway analysis. These genes are present at elevated carrier frequency in any unselected pediatric sequencing cohort at MAF ≤0.001 regardless of disease phenotype, and their inclusion would inflate background signal without contributing disease-specific biological information. The complete exclusion list is: ABCA4, BCHE, CD36, COL4A5, FLG, G6PD, GJB2, KRT71, KRT86, MYO15A, MYO1A, MYO3A, MYO7A, OBSCN, PADI3, PAH, TBL1Y, TCHH, TTN, USH2A.

**UMLS CUI resolution.** Gene symbols were mapped to UMLS Concept Unique Identifiers (CUIs) for use as pipeline seed inputs using `seed_cui_lookup.py`, which queries the DDKG for HGNC-SAB concept nodes matching each gene symbol. Of 1,287 CHD seed genes, 1,276 (99.1%) resolved to UMLS CUIs; of 1,406 NBL seed genes, 1,395 (99.2%) resolved. Genes failing CUI resolution were excluded from graph analysis. Final seed counts used in all reported analyses are 1,276 (KF-CHD) and 1,395 (KF-NBL).

**Output.** Seed gene files for both cohorts at all carrier-count filter levels are provided in the repository at `data/cohorts/chd/` and `data/cohorts/nbl/`.

### SM2: Neo4j Export Queries

Graph neighborhoods for all benchmarks and cohort analyses were exported from the Data Distillery Knowledge Graph (DDKG) using Neo4j cypher-shell. Each export follows a four-query pattern: (1) a verification query checking gene symbol-to-CUI resolution; (2) a node export collecting all concept nodes in the 1-hop neighborhood with SAB-priority resolution; (3) an edge export collecting seed↔neighbor edges; and (4) a targeted pathway membership edge export collecting gene-to-pathway edges within the neighborhood. Exported CSV files are cleaned using `clean_cypher_output.py` to remove cypher-shell formatting artifacts before pipeline ingestion.

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

## Supplementary Tables

*ST5 consists of downloadable CSV files and is not typeset. ST6 and ST7 are provided as Supplementary Tables below.*

### ST1: Top-10 ranked pathways per propagation arm, curated CHD benchmark

Three-arm comparison: BIFO-PPR full-arm (57,005 propagating edges), Ablation (14,413 propagating edges, no Pathway Contribution bridge edges), and Mechanistic-only (9,710 edges). Pathway universe: 563 pathways (8-300 members). CHD reference pathways marked with ✓ in the Ref. column. Score = degree_norm (direct PPR score at pathway node / √member count). Note: the curated benchmark universe includes all MSigDB collections (HALLMARK_, REACTOME_, WP_, KEGG_, PID_, BIOCARTA_, and CGP author-named sets); the CGP exclusion filter applies only to KF cohort analyses (ST3-ST4). In the BIFO-PPR full-arm table, rows for WP_JOUBERT_SYNDROME (rank 34) and WP_CILIOPATHIES (rank 43) are shown out of sequence after rank 8 to highlight the top cilia pathway results alongside the top 10 ranked pathways.

**BIFO-PPR full-arm**

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

*All 563 pathway scores are exactly zero under mechanistic-only propagation. Pathway nodes are structurally unreachable from seed genes through mechanistic edges alone; gene-to-pathway connectivity requires Pathway Contribution bridge edges. P@10 = 0.00, Enrichment@10 = 0×.*

### ST2: Baseline enrichment method comparison, curated CHD benchmark

Top-20 ranked pathways under each enrichment method, evaluated on the identical 563-pathway universe (all MSigDB collections including CGP; CGP exclusion applies to KF analyses only). CHD reference pathways marked with ✓. Score/stat column: degree_norm for B0 and B4; hypergeometric stat for B1/B2; enrichment score for B3/B3b.

**B0: Degree-weighted seed overlap**

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

**B1: Seed-only Fisher (hypergeometric)**

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

**B2: 1-hop neighborhood Fisher**

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

**B3: Raw PPR preranked GSEA**

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

**B3b: Conditioned PPR preranked GSEA**

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

**B4: BIFO-PPR full-arm (degree_norm)**

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

### ST3: Top-20 ranked pathways per method, KF-CHD and KF-NBL cohorts

Five enrichment methods evaluated in discovery mode (no reference pathway pre-specified). KF-CHD: 2,130 pathways scored (canonical collections only); KF-NBL: 2,196 pathways scored. Cilia reference pathways marked with ✓. For BIFO-PPR, both the unfiltered degree_norm rank (all pathways) and the filtered rank (null-calibrated pathways only, signal_to_null_mean ≤ 10) are shown. †Pathways excluded from null calibration (signal_to_null_mean > 10): null_z is not interpretable and filtered rank is not assigned. In KF-CHD the entire top 20 by degree_norm consists of excluded pathways; WP_CILIOPATHIES ranks 43rd overall but 1st among null-calibrated pathways.

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

*BIFO-PPR full-arm (B4)*

| Rank | Pathway name | SAB | degree_norm | null_z | Filtered rank | Cilia ref. |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Protein phosphorylation | GO | 2.245e-05 | —† | —† | — |
| 2 | REACTOME_CROSS_PRESENTATION_OF_PARTICULATE_EXOGENOUS_ANTIGENS_PHAGOSOMES | MSIGDB | 2.115e-05 | —† | —† | — |
| 3 | WP_NAD_METABOLISM_SIRTUINS_AND_AGING | MSIGDB | 2.059e-05 | —† | —† | — |
| 4 | REACTOME_FREE_FATTY_ACIDS_REGULATE_INSULIN_SECRETION | MSIGDB | 1.804e-05 | —† | —† | — |
| 5 | WP_ARYL_HYDROCARBON_RECEPTOR_NETPATH | MSIGDB | 1.502e-05 | —† | —† | — |
| 6 | WP_FGF23_SIGNALLING_IN_HYPOPHOSPHATEMIC_RICKETS_AND_RELATED_DISORDERS | MSIGDB | 1.462e-05 | —† | —† | — |
| 7 | REACTOME_ACTIVATION_OF_PUMA_AND_TRANSLOCATION_TO_MITOCHONDRIA | MSIGDB | 1.361e-05 | —† | —† | — |
| 8 | BIOCARTA_FBW7_PATHWAY | MSIGDB | 1.361e-05 | —† | —† | — |
| 9 | Ionophore activity | GO | 1.357e-05 | —† | —† | — |
| 10 | REACTOME_REGULATION_OF_TLR_BY_ENDOGENOUS_LIGAND | MSIGDB | 1.338e-05 | —† | —† | — |
| 11 | BIOCARTA_SKP2E2F_PATHWAY | MSIGDB | 1.291e-05 | —† | —† | — |
| 12 | WP_MAMMARY_GLAND_DEVELOPMENT_PATHWAY_INVOLUTION_STAGE_4_OF_4 | MSIGDB | 1.291e-05 | —† | —† | — |
| 13 | cell motility | GO | 1.251e-05 | —† | —† | — |
| 14 | REACTOME_CDC6_ASSOCIATION_WITH_THE_ORC_ORIGIN_COMPLEX | MSIGDB | 1.231e-05 | —† | —† | — |
| 15 | REACTOME_REGULATION_OF_PYRUVATE_DEHYDROGENASE_PDH_COMPLEX | MSIGDB | 1.200e-05 | —† | —† | — |
| 16 | REACTOME_INHIBITION_OF_REPLICATION_INITIATION_OF_DAMAGED_DNA_BY_RB1_E2F1 | MSIGDB | 1.178e-05 | —† | —† | — |
| 17 | WP_GENES_CONTROLLING_NEPHROGENESIS | MSIGDB | 1.138e-05 | —† | —† | — |
| 18 | BIOCARTA_P27_PATHWAY | MSIGDB | 1.132e-05 | —† | —† | — |
| 19 | REACTOME_TRANSPORT_OF_ORGANIC_ANIONS | MSIGDB | 1.124e-05 | —† | —† | — |
| 20 | REACTOME_SLC_TRANSPORTER_DISORDERS | MSIGDB | 1.119e-05 | —† | —† | — |
| ... | | | | | | |
| 34 | WP_JOUBERT_SYNDROME | MSIGDB | 9.280e-06 | —† | —† | ✓ |
| ... | | | | | | |
| 43 | WP_CILIOPATHIES | MSIGDB | 8.509e-06 | 41.2 | 1 | ✓ |
| ... | | | | | | |
| 163 | REACTOME_CILIUM_ASSEMBLY | MSIGDB | 4.219e-06 | 18.5 | 59 | ✓ |
| ... | | | | | | |
| 171 | WP_GENES_RELATED_TO_PRIMARY_CILIUM_DEVELOPMENT_BASED_ON_CRISPR | MSIGDB | 3.977e-06 | 17.9 | 65 | ✓ |
| ... | | | | | | |
| 216 | REACTOME_HEDGEHOG_OFF_STATE | MSIGDB | 3.163e-06 | 14.4 | 103 | ✓ |

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

*BIFO-PPR full-arm (B4)*

| Rank | Pathway name | SAB | degree_norm | null_z | Filtered rank | Cilia ref. |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Ionophore activity | GO | 4.692e-06 | 17.8 | 1 | — |
| 2 | Transmembrane Transport | GO | 4.367e-06 | 16.3 | 2 | — |
| 3 | WP_CILIOPATHIES | MSIGDB | 4.241e-06 | 18.4 | 3 | ✓ |
| 4 | Regulation of Cell Shape | GO | 3.637e-06 | 13.4 | 4 | — |
| 5 | DNA Repair | GO | 3.558e-06 | 11.7 | 5 | — |
| 6 | REACTOME_DISEASES_OF_METABOLISM | MSIGDB | 3.256e-06 | 13.1 | 6 | — |
| 7 | Blood coagulation | GO | 3.250e-06 | 13.7 | 7 | — |
| 8 | Skeletal Development | GO | 2.863e-06 | 14.2 | 8 | — |
| 9 | Myogenesis | GO | 2.829e-06 | 10.4 | 9 | — |
| 10 | WP_AMINO_ACID_METABOLISM | MSIGDB | 2.706e-06 | 11.2 | 10 | — |
| 11 | Heparin Binding | GO | 2.703e-06 | 14.8 | 11 | — |
| 12 | Carbohydrate Metabolism | GO | 2.684e-06 | 9.0 | 12 | — |
| 13 | PID_CONE_PATHWAY | MSIGDB | 2.672e-06 | 13.8 | 13 | — |
| 14 | Vision | GO | 2.636e-06 | 10.1 | 14 | — |
| 15 | Xenobiotic Metabolism | GO | 2.609e-06 | 9.2 | 15 | — |
| 16 | Nucleotide Metabolism | GO | 2.545e-06 | 8.5 | 16 | — |
| 17 | WP_JOUBERT_SYNDROME | MSIGDB | 2.536e-06 | 9.9 | 17 | ✓ |
| 18 | REACTOME_DISORDERS_OF_TRANSMEMBRANE_TRANSPORTERS | MSIGDB | 2.467e-06 | 9.5 | 18 | — |
| 19 | Homeostasis | GO | 2.440e-06 | 8.4 | 19 | — |
| 20 | Amino Acid Biosynthesis | GO | 2.438e-06 | 9.4 | 20 | — |
| ... | | | | | | |
| 31 | WP_GENES_RELATED_TO_PRIMARY_CILIUM_DEVELOPMENT_BASED_ON_CRISPR | MSIGDB | 2.154e-06 | 8.3 | 31 | ✓ |
| 32 | REACTOME_CILIUM_ASSEMBLY | MSIGDB | 2.154e-06 | 6.7 | 32 | ✓ |
| ... | | | | | | |
| 228 | REACTOME_SIGNALING_BY_HEDGEHOG | MSIGDB | 1.134e-06 | 2.0 | 228 | ✓ |
| ... | | | | | | |
| 233 | WP_CILIARY_LANDSCAPE | MSIGDB | 1.125e-06 | 1.0 | 233 | ✓ |
| ... | | | | | | |
| 245 | REACTOME_INTRAFLAGELLAR_TRANSPORT | MSIGDB | 1.100e-06 | 3.4 | 245 | ✓ |

### ST4: Full cilia pathway cluster ranking under BIFO, KF-CHD and KF-NBL

All cilia, ciliopathy, and hedgehog pathway annotations from the scored universe (16 matched in KF-CHD, 16 in KF-NBL from the 16-pathway reference), ordered by KF-CHD BIFO rank. Score = degree_norm. Also shown: null_z (pathway-node rewiring null). One reference pathway (MSIGDB:M9331, a CGP collection gene expression signature set) was not present in the scored universe after canonical-collection filtering and is excluded from this table. †NaN: null distribution is degenerate (signal_to_null_mean > 10); null_z is not interpretable and the pathway is excluded from BH correction (see Methods §5.1).

| Pathway name | Source DB | KF-CHD rank | KF-CHD score | KF-CHD null_z | KF-NBL rank | KF-NBL score | KF-NBL null_z |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WP_JOUBERT_SYNDROME | MSIGDB | 34 | 9.280e-06 | NaN† | 17 | 2.536e-06 | 10.54 |
| WP_CILIOPATHIES | MSIGDB | 43 | 8.509e-06 | 41.19 | 3 | 4.241e-06 | 18.37 |
| REACTOME_ANCHORING_OF_THE_BASAL_BODY_TO_THE_PLASMA_MEMBRANE | MSIGDB | 95 | 6.049e-06 | 29.97 | 71 | 1.752e-06 | 5.65 |
| REACTOME_CILIUM_ASSEMBLY | MSIGDB | 163 | 4.219e-06 | 18.52 | 32 | 2.154e-06 | 6.12 |
| WP_GENES_RELATED_TO_PRIMARY_CILIUM_DEVELOPMENT_BASED_ON_CRISPR | MSIGDB | 171 | 3.977e-06 | 17.86 | 31 | 2.154e-06 | 8.94 |
| REACTOME_HEDGEHOG_OFF_STATE | MSIGDB | 216 | 3.163e-06 | 14.39 | 347 | 9.544e-07 | 0.13 |
| REACTOME_SIGNALING_BY_HEDGEHOG | MSIGDB | 239 | 2.740e-06 | 13.48 | 228 | 1.134e-06 | 0.52 |
| WP_CILIARY_LANDSCAPE | MSIGDB | 358 | 1.401e-06 | 1.08 | 233 | 1.125e-06 | -1.01 |
| WP_HEDGEHOG_SIGNALING_PATHWAY_NETPATH | MSIGDB | 921 | 1.895e-08 | -3.18 | 516 | 7.433e-07 | 2.74 |
| WP_HEDGEHOG_SIGNALING_PATHWAY | MSIGDB | 926 | 1.874e-08 | -4.86 | 359 | 9.307e-07 | 2.76 |
| HALLMARK_HEDGEHOG_SIGNALING | MSIGDB | 1110 | 1.471e-08 | -0.38 | 722 | 6.062e-07 | 15.90 |
| REACTOME_CARGO_TRAFFICKING_TO_THE_PERICILIARY_MEMBRANE | MSIGDB | 1457 | 9.213e-09 | -5.34 | 499 | 7.561e-07 | 0.98 |
| REACTOME_BBSOME_MEDIATED_CARGO_TARGETING_TO_CILIUM | MSIGDB | 1463 | 9.174e-09 | -3.60 | 867 | 5.303e-07 | 0.99 |
| REACTOME_INTRAFLAGELLAR_TRANSPORT | MSIGDB | 1592 | 7.794e-09 | -5.35 | 245 | 1.100e-06 | 3.45 |
| WP_INTRAFLAGELLAR_TRANSPORT_PROTEINS_BINDING_TO_DYNEIN | MSIGDB | 1634 | 7.254e-09 | -3.78 | 532 | 7.313e-07 | 1.61 |
| REACTOME_VXPX_CARGO_TARGETING_TO_CILIUM | MSIGDB | 1924 | 3.677e-09 | -3.26 | 1437 | 3.202e-07 | -0.58 |

*16 of 17 reference pathways matched in the scored universe (YAUCH_HEDGEHOG_SIGNALING_PARACRINE_UP not present after canonical-collection filtering). Null_z values from pathway-node membership rewiring null (N=1000 permutations). Negative null_z indicates depletion relative to null expectation.*

### ST5: Head-to-head rank comparison, seed Fisher vs. BIFO (downloadable data files)

Full ranked pathway lists for all pathways scored under both methods, for KF-CHD and KF-NBL independently. Provided as downloadable supplementary data files due to size (2,130 pathways for KF-CHD; 2,196 pathways for KF-NBL).

**ST5a** (`supplementary_data_ST5a_kf_chd_fisher_vs_bifo.csv`): KF-CHD, sorted by BIFO rank.

**ST5b** (`supplementary_data_ST5b_kf_nbl_fisher_vs_bifo.csv`): KF-NBL, sorted by BIFO rank.

Columns: pathway_name | source_db | member_count | bifo_rank | bifo_score | fisher_rank | fisher_bh_pvalue | cilia_ref_flag | hub_flag

*Source: `results/kf_chd/baseline_comparison.csv` and `results/kf_nbl/baseline_comparison.csv`*

### ST6: BIFO-PPR propagating edge composition: predicate, flow class, and source vocabulary attribution

All predicates present in BIFO-conditioned kept_edges files across the benchmark (CHD curated, 15-gene pool) and KF cohort analyses (KF-CHD: 1,276 seeds; KF-NBL: 1,395 seeds). Counts reflect edges from the source node perspective; forward and inverse predicate directions are listed separately. Source SABs are derived by joining kept_edges source node IDs to the DDKG node SAB field. UNKNOWN indicates nodes without a resolvable source vocabulary. Propagating=True edges enter the PPR adjacency matrix; Propagating=False edges are retained in kept_edges for reference only and excluded from propagation. Flow class and classification tier are sourced directly from bifo_mapping.yaml v0.7.1. Predicates with classification non_flow_edge are in the YAML non_flow_edges list and received observational fallthrough classification during conditioning. All analyses used the August 2025 DDKG release.

#### Propagating edges (Propagating=True; enter PPR operator)

| Predicate | Flow class | Classification tier | Source SAB(s) | Benchmark | KF-CHD | KF-NBL |
|-----------|-----------|--------------------|--------------|-----------:|-------:|-------:|
| inverse_pathway_associated_with_gene | Pathway Contribution | weak_mechanistic_or_observational | HGNC | 36,502 | 486,548 | 494,298 |
| regulated_by | Signal Transduction | mechanistic | HGNC | 2,675 | 218,281 | 249,602 |
| regulates | Signal Transduction | mechanistic | HGNC | 2,675 | 218,281 | 249,602 |
| expresses | Transcription | mechanistic | HGNC | 675 | 56,250 | 61,920 |
| expressed_in | Transcription | mechanistic | HGNC | 675 | 56,250 | 61,920 |
| inverse_targets_expression_of_gene | Perturbational Effect | mechanistic | HGNC | 900 | 42,529 | 57,752 |
| targets_expression_of_gene | Perturbational Effect | mechanistic | HGNC | 900 | 42,529 | 57,752 |
| positively_correlated_with_chemical_or_drug | Perturbational Effect | weak_mechanistic_or_observational | HGNC | 1,028 | 43,870 | 48,833 |
| inverse_positively_correlated_with_chemical_or_drug | Perturbational Effect | weak_mechanistic_or_observational | CHEBI, DRUGBANK, GS, HGNC, MMSL, MSH, NCI, PUBCHEM, SNOMEDCT_US | 1,028 | 43,870 | 48,833 |
| negatively_correlated_with_chemical_or_drug | Perturbational Effect | weak_mechanistic_or_observational | HGNC | 768 | 37,045 | 38,790 |
| inverse_negatively_correlated_with_chemical_or_drug | Perturbational Effect | weak_mechanistic_or_observational | CHEBI, DRUGBANK, GS, HGNC, MMSL, MSH, NCI, PUBCHEM, SNOMEDCT_US | 768 | 37,045 | 38,790 |
| gene_plays_role_in_process | Pathway Contribution | weak_mechanistic_or_observational | HGNC, MONDO, MSH, NCI, OMIM, PUBCHEM | 3,104 | 22,173 | 22,403 |
| process_involves_gene | Pathway Contribution | weak_mechanistic_or_observational | GO, HGNC, MSH, NCI, SNOMEDCT_US | 3,104 | 22,173 | 22,403 |
| transcribed_from | Transcription | mechanistic | HGNC | 109 | 17,153 | 18,089 |
| transcribed_to | Transcription | mechanistic | HGNC | 109 | 17,153 | 18,089 |
| positively_regulates | Signal Transduction | mechanistic | HGNC | 167 | 17,971 | 17,152 |
| positively_regulated_by | Signal Transduction | mechanistic | HGNC | 167 | 17,971 | 17,152 |
| negatively_regulates | Signal Termination | mechanistic | HGNC | 235 | 17,400 | 17,477 |
| negatively_regulated_by | Signal Termination | mechanistic | HGNC | 235 | 17,400 | 17,477 |
| inverse_has_signature_gene | Pathway Contribution | weak_mechanistic_or_observational | HGNC | 850 | 7,758 | 7,812 |
| gene_product_of | Translation | mechanistic | HGNC | 15 | 1,148 | 1,249 |
| has_gene_product | Translation | mechanistic | HGNC | 15 | 1,148 | 1,249 |
| causally_influences | Signal Transduction | mechanistic | HGNC | — | 976 | 1,199 |
| causally_influenced_by | Signal Transduction | mechanistic | HGNC | — | 976 | 1,199 |
| inverse_gene_has_variants | Genetic Regulatory Modulation | mechanistic | HGNC | 10 | 1,068 | 1,074 |
| gene_has_variants | Genetic Regulatory Modulation | mechanistic | HGNC | 10 | 1,068 | 1,074 |
| inverse_involved_in_pathway | Pathway Contribution | weak_mechanistic_or_observational | HGNC | 69 | 884 | 1,140 |
| involved_in_pathway | Pathway Contribution | weak_mechanistic_or_observational | HGNC | 69 | 884 | 1,140 |
| directedinteraction | Signal Transduction | mechanistic | HGNC | 87 | 648 | 890 |
| stimulation | Signal Transduction | mechanistic | HGNC | 15 | 174 | 225 |
| inhibition | Signal Termination | mechanistic | HGNC | 14 | 164 | 221 |
| binding | Protein Interaction | mechanistic | HGNC | 6 | 169 | 165 |
| gene_encodes_gene_product | Translation | mechanistic | HGNC | 8 | 64 | 64 |
| gene_product_encoded_by_gene | Translation | mechanistic | HGNC | 8 | 64 | 64 |
| transcriptiontranslation | Transcription | weak_mechanistic_or_observational | HGNC | 5 | 47 | 73 |
| part_of_a_fusion_gene_in | Genetic Regulatory Modulation | mechanistic | HGNC | — | 5 | 16 |
| conversion | Biochemical Transformation | mechanistic | HGNC | — | 7 | 9 |
| catalysis | Biochemical Transformation | mechanistic | HGNC | — | 3 | 4 |
| has_phenotype | Molecular → Phenotype | mechanistic | HGNC | — | 2 | 2 |
| phenotype_of | Molecular → Phenotype | mechanistic | HGNC | — | 2 | 2 |

#### Non-propagating edges (Propagating=False; retained in kept_edges, excluded from PPR)

| Predicate | Flow class | Classification tier | Source SAB(s) | Benchmark | KF-CHD | KF-NBL |
|-----------|-----------|--------------------|--------------|-----------:|-------:|-------:|
| pathway_associated_with_gene | Pathway Contribution | nonpropagating_context | HGNC | 36,502 | 486,548 | 494,298 |
| associated_with | Observational Association | observational | HGNC | 4,094 | 149,547 | 157,306 |
| inverse_associated_with | Observational Association | observational | GO, HGNC, HP, MONDO, MSH, NCI, OMIM, SNOMEDCT_US | 4,094 | 149,547 | 157,306 |
| overlaps | Spatial constraint | contextual_constraint | HGNC | 378 | 47,194 | 56,321 |
| inverse_overlaps | Spatial constraint | contextual_constraint | HGNC | 378 | 47,194 | 56,321 |
| located_in | Spatial constraint | contextual_constraint | HGNC | 13 | 42,009 | 35,161 |
| location_of | Spatial constraint | contextual_constraint | HGNC | 13 | 42,009 | 35,161 |
| inverse_gene_associated_with_disease_or_phenotype | Observational Association | observational | HGNC, HP, MONDO, OMIM | 551 | 16,196 | 18,133 |
| gene_associated_with_disease_or_phenotype | Observational Association | observational | HGNC | 551 | 16,196 | 18,133 |
| has_signature_gene | Pathway Contribution | nonpropagating_context | HGNC | 850 | 7,758 | 7,812 |
| inverse_has_marker_gene | Observational Association | observational | HGNC | 109 | 7,243 | 7,490 |
| has_marker_gene | Observational Association | observational | HGNC | 109 | 7,243 | 7,490 |
| in_1_to_1_orthology_relationship_with | Observational Association | observational | HGNC | 57 | 2,337 | 2,617 |
| inverse_in_1_to_1_orthology_relationship_with | Observational Association | observational | HGNC | 57 | 2,337 | 2,617 |
| has_human_ortholog | Observational Association | observational | HGNC | 27 | 2,068 | 2,240 |
| inverse_has_human_ortholog | Observational Association | observational | HGNC | 27 | 2,068 | 2,240 |
| disease_mapped_to_gene | Observational Association | observational | HGNC, MONDO | 42 | 935 | 1,896 |
| gene_mapped_to_disease | Observational Association | observational | HGNC | 42 | 935 | 1,896 |
| inverse_us_5_prime | Spatial constraint | nonpropagating_context | HGNC | 15 | 1,191 | 1,307 |
| ds_3_prime | Spatial constraint | nonpropagating_context | HGNC | 15 | 1,191 | 1,307 |
| inverse_ds_3_prime | Spatial constraint | nonpropagating_context | HGNC | 15 | 1,191 | 1,307 |
| us_5_prime | Spatial constraint | nonpropagating_context | HGNC | 15 | 1,191 | 1,307 |
| has_material_basis_in_germline_mutation_in | Genetic Regulatory Modulation | observational | HGNC, MONDO | 43 | 923 | 920 |
| gene_involved_in_molecular_abnormality | Observational Association | observational | HGNC | 41 | 814 | 778 |
| inverse_chr_band_contains_gene | Spatial constraint | contextual_constraint | HGNC | 10 | 733 | 803 |
| chr_band_contains_gene | Spatial constraint | contextual_constraint | HGNC | 10 | 733 | 803 |
| disease_causing_germline_mutation_s__in | Genetic Regulatory Modulation | observational | HGNC | 20 | 705 | 684 |
| related_to_genetic_biomarker | Observational Association | non_flow_edge | HGNC, MONDO, NCI, OMIM | 17 | 583 | 802 |
| genetic_biomarker_related_to | Observational Association | observational | HGNC | 17 | 583 | 802 |
| gene_found_in_organism | Observational Association | observational | HGNC | 13 | 607 | 658 |
| inverse_gene_disease_validity | Observational Association | observational | HGNC, MONDO | 19 | 466 | 529 |
| gene_disease_validity | Observational Association | observational | HGNC | 19 | 466 | 529 |
| gene_involved_in_pathogenesis_of_disease | Observational Association | observational | HGNC | 5 | 77 | 128 |
| gene_associated_with_disease | Observational Association | observational | HGNC | 1 | 94 | 100 |
| disease_has_associated_gene | Observational Association | observational | HGNC, MONDO | 1 | 94 | 100 |
| has_marker_gene_in_kidney | Observational Association | observational | HGNC | 1 | 64 | 63 |
| inverse_has_marker_gene_in_kidney | Observational Association | observational | HGNC | 1 | 64 | 63 |
| inverse_candidate_gene_tested_in | Observational Association | non_flow_edge | HGNC, MONDO | 4 | 43 | 42 |
| candidate_gene_tested_in | Observational Association | non_flow_edge | HGNC | 4 | 43 | 42 |
| major_susceptibility_factor_in | Observational Association | observational | HGNC | 2 | 42 | 34 |
| disease_causing_somatic_mutation_s__in | Genetic Regulatory Modulation | observational | HGNC | 1 | 9 | 35 |
| has_marker_gene_in_heart | Observational Association | observational | HGNC | 1 | 18 | 23 |
| inverse_has_marker_gene_in_heart | Observational Association | observational | HGNC | 1 | 18 | 23 |
| gene_has_abnormality | Observational Association | observational | HGNC | — | 15 | 13 |
| inverse_has_marker_gene_in_liver | Observational Association | observational | HGNC | 1 | 16 | 9 |
| has_marker_gene_in_liver | Observational Association | observational | HGNC | 1 | 16 | 9 |
| biomarker_tested_in | Observational Association | non_flow_edge | HGNC | — | 2 | 2 |
| inverse_biomarker_tested_in | Observational Association | non_flow_edge | HGNC | — | 2 | 2 |
| gene_in_chromosomal_location | Spatial constraint | contextual_constraint | HGNC | — | 1 | — |

### ST7: Source vocabulary (SAB) contributions to BIFO-PPR analyses

Source vocabularies (SABs) identified as source nodes in BIFO-conditioned kept_edges files. SAB attribution is based on the source node of each edge as resolved by the DDKG node SAB field. Only SABs with at least one edge across any analysis are shown. Predicate count reflects unique predicate types contributed by that SAB as source node. Edges where the source node SAB could not be resolved (UNKNOWN) are excluded. The dominant SAB is HGNC because gene concept nodes , the primary seed and propagation entity , resolve to HGNC identifiers under the node SAB priority ordering used in the Cypher export queries.

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

### ST8: BIFO-PPR LLM interpretation input document, KF-CHD

Structured input document generated by `pipeline/summarize_results.py` and provided to large language models (Claude Opus 4.7 and GPT-5.3) for biological interpretation of KF-CHD pathway results. The document includes: a full column guide with definitions for all output fields (`rank`, `pathway_name`, `source`, `n_members`, `degree_norm`, `null_calibrated`, `null_z`, `empirical_q`, `member_mean_null_z`, `member_mean_q`, `in_reference`, `seed_members`, `seed_member_scores`, `influential_nodes_local`, `influential_nodes_global`, `neighbor_z_local`, `neighbor_z_global`); a structured set of analytical task instructions including investigation of non-obvious network drivers, convergent process analysis, cross-check against cohort phenotype, skeptical pass for single-gene-dominated signals, and drill-down into top pathway score distributions; a data provenance and FAIR assessment section with explicit LLM instructions to assess completeness before interpreting results; an analysis summary with run-level metadata; the full list of 1,276 resolved seed genes as gene symbols; and the top-50 pathways by BIFO score in tabular format. The full input document is available as Supplementary Data SD1 alongside the complete pathway results table. Verbatim LLM responses to this document are provided in Supplementary Section S1 and in `content/08.llm_interpretation.md` in the manuscript repository.

---

### ST9: BIFO-PPR LLM interpretation input document, KF-NBL

Structured input document generated by `pipeline/summarize_results.py` and provided to large language models (Claude Opus 4.7 and GPT-5.3) for biological interpretation of KF-NBL pathway results. The document has identical structure to ST8 but reflects the KF-NBL cohort: 1,395 resolved seed genes from 460 neuroblastoma probands, 2,196 scored pathways, and a provenance record specifying germline rare variant analysis with explicit notation that canonical somatic neuroblastoma drivers (MYCN amplification, TERT rearrangements, LIN28B, somatic ALK) are not expected in the seed list. The document includes the analytical task instructions described in ST8, with the additional context that the large seed set (1,395 genes) is expected to saturate the global influential-node threshold, such that non-seed network drivers may not emerge in this run, an expected regime property rather than a method failure, noted explicitly in the provenance and column guide. The full input document is available as Supplementary Data SD2 alongside the complete pathway results table. Verbatim LLM responses to this document are provided in Supplementary Section S1 and in `content/08.llm_interpretation.md` in the manuscript repository.

---

### S1: LLM biological interpretation of KF cohort BIFO-PPR results

Verbatim biological interpretation responses from Claude Opus 4.7 and GPT-5.3 (instant), run in parallel on isolated chat sessions using the input documents described in ST8 and ST9. Both models were instructed to follow the analytical task framework defined in the input documents, including FAIR provenance assessment, investigation of non-obvious network drivers, cross-check against cohort phenotype, skeptical pass, and drill-down into top pathway scores. Full verbatim responses for KF-CHD and KF-NBL from both models are provided in `content/08.llm_interpretation.md` in the manuscript repository. These outputs are illustrative of the exploratory biological interpretation use case enabled by the structured BIFO-PPR output format and are not part of the quantitative evaluation of BIFO-PPR.

---

### S6.1 Pipeline scripts (`pipeline/`)

| Script | Purpose | Paper section |
|--------|---------|---------------|
| `bifo_conditioning.py` | BIFO edge conditioning (entity resolution, flow class filtering) and PPR propagation. Primary analysis script. | Methods §2, §3 |
| `score_pathways.py` | Pathway scoring from PPR score vectors using degree_norm and alternative variants; implements pathway-node membership rewiring null and stratified member-level null (Methods §4, §5) |
| `baseline_enrichment.py` | Enrichment baselines B0-B3 (degree overlap, Fisher, neighborhood Fisher, preranked GSEA). Accepts `--kept-edges` and `--small-universe` flags | Methods §7 |
| `chd_resampling_exhaustive.py` | Exhaustive in-memory resampling over all C(15,10) = 3,003 possible 10-gene/5-gene partitions of the CHD gene pool | Methods §9 |
| `kf_resampling.py` | Bootstrap resampling for KF cohort analyses (500 draws × 3 seed sizes per cohort) | Methods §15 |
| `seed_cui_lookup.py` | Map HGNC gene symbols to UMLS CUIs for use as pipeline seed inputs | Methods §11 |
| `generate_export_cypher.py` | Generate cohort-specific Neo4j export Cypher queries from a seed gene list | Methods §11 |
| `build_cilia_reference.py` | Build the cilia pathway reference set by matching pathway names against cilia-related terms | Methods §13 |
| `clean_cypher_output.py` | Clean artifact characters introduced by cypher-shell CSV export | Methods §11 |

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
| `chd_curated_nodes.csv` | Node list for the CHD curated benchmark; used as `--nodes` input to the scoring pipeline (`results_node_index.json` is the `--node-index` input) |
| `chd_curated_edges_raw.csv.zip` | 94,790 seed-centered mechanistic and association edges for the curated CHD benchmark graph |
| `chd_curated_pathway_membership_edges.csv.zip` | 79,562 gene-to-pathway membership edges (MSigDB, WikiPathways, GO) |
| `chd_pathway_reference.txt` | 18 CHD reference pathway CUIs used for evaluation |
| `c4_notch_seed_nodes.txt` | 30 HGNC gene CUIs; 70% split of REACTOME_SIGNALING_BY_NOTCH members (numpy seed=42) |
| `c4_notch_heldout_nodes.txt` | 14 held-out gene CUIs; 30% split of REACTOME_SIGNALING_BY_NOTCH |
| `c4_notch_pathway_reference.txt` | 11 Notch-family reference pathway CUIs |
| `c4_mapk_seed_nodes.txt` | 63 HGNC gene CUIs; 70% split of REACTOME_MAPK_FAMILY_SIGNALING_CASCADES |
| `c4_mapk_heldout_nodes.txt` | 28 held-out gene CUIs; 30% split of REACTOME_MAPK_FAMILY_SIGNALING_CASCADES |
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
| `kf_chd_cilia_reference.txt` | MSigDB cilia pathway reference set for KF-CHD evaluation (16 CUIs) |

**KF-NBL cohort (`data/cohorts/nbl/`)**

| File | Description |
|------|-------------|
| `kf_nbl_seeds_maf001.txt` | Primary seed gene list: 1,406 HGNC genes with AutoGVP P/LP variants at MAF ≤0.001, n≥1 carrier |
| `kf_nbl_seeds_maf001_n2.txt` | Carrier-filtered seeds: 401 genes with n≥2 carriers at MAF ≤0.001 |
| `kf_nbl_seeds_maf001_n3.txt` | Carrier-filtered seeds: 147 genes with n≥3 carriers at MAF ≤0.001 |
| `kf_nbl_seeds_maf01.txt` | Broader-filter seeds at MAF ≤0.01 |
| `kf_nbl_seeds.txt` | Original unfiltered seed gene list |
| `kf_nbl_cilia_reference.txt` | MSigDB cilia pathway reference set for KF-NBL evaluation (16 CUIs) |

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
| `baseline_comparison.json` | Baseline enrichment method comparison metrics (B0-B4) |
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
| `baseline_comparison.json` | Baseline enrichment method comparison metrics (B1-B4) |
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


## LLM Interpretation of BIFO-PPR Pathway Results

GPT-4o (GPT-5.3) interpretations of BIFO-PPR pathway prioritization results for KF-CHD and KF-NBL cohorts, generated from `pathway_results_llm.md` and `pathway_results_summary.tsv` output files produced by `pipeline/summarize_results.py`. Output files include `contributing_seeds` (seed genes whose PPR signal contributed to each pathway score via graph propagation) and `seed_members` (seed genes that are direct annotated members of each pathway). These outputs are illustrative of the exploratory biological interpretation use case and are not part of the quantitative evaluation of BIFO-PPR.

---

### KF-CHD Cohort

**User:** I am working on characterizing genes in a list of about 1200 genes with predicted deleterious germline variants from a congenital heart defects cohort. I'm trying to understand what pathways are activated based on a graph-enrichment method. Can you read the markdown file, review the tsv table, and follow the instructions?

**GPT-5.3:** Yes. The results point to a coherent CHD-relevant signal, with the strongest interpretable themes being:

1. **Cilia / basal body biology.** Top calibrated hit: WP_CILIOPATHIES, with related basal body anchoring. This is highly plausible for CHD because cilia affect left-right patterning, developmental signaling, and organ morphogenesis.

2. **Ion and transmembrane transport.** Strong hits include transmembrane transport, SLC-mediated transport, cation/anion/amino acid transport, sensory sound processing, and transporter disorders. This may reflect channel/transporter genes in the variant set, including cardiac excitability and developmental signaling components.

3. **Cell shape, cytoskeleton, motility, and muscle development.** Regulation of cell shape, myogenesis, striated muscle contraction, actin cytoskeleton, and cell motility appear as a connected theme. This fits heart development because morphogenesis depends on cell migration, epithelial/mesenchymal dynamics, contractile differentiation, and tissue remodeling.

4. **Immune/inflammatory signaling.** Inflammatory response, IL-4/IL-13, IL18, complement, TLR, and antigen presentation are enriched. I would treat this cautiously as a secondary theme unless supported by tissue-specific or developmental expression, but it could reflect extracellular matrix remodeling, injury-like developmental programs, or pleiotropic immune genes.

5. **Metabolism and lipid/energy pathways.** Adipogenesis, fatty acid metabolism, PPARα regulation, lipid metabolism, carbohydrate metabolism, and energy integration are frequent. This may reflect cardiac metabolic maturation or broad developmental/metabolic constraint.

Important table issue: many high absolute-rank pathways above rank 43 are marked `null_calibrated = False`, so I would not foreground them statistically. The markdown correctly focuses on well-calibrated pathways. Also, many significant MSigDB pathways have empty `seed_members` but shared `contributing_seeds`, especially CEP290, PKD1L1, ASPM, CC2D2A, and ROS1, suggesting the graph propagation is recovering indirect biological neighborhoods rather than simple gene-set overlap. That is biologically useful, but it means the cilia/transport/cell-shape interpretation should be validated by checking the paths from these contributors into the pathway nodes.

**One-sentence interpretation:** The CHD variant gene set appears enriched for developmental morphogenesis programs centered on cilia/basal body function, transmembrane and ion transport, cell-shape/cytoskeletal regulation, muscle differentiation, and metabolic remodeling, with immune/inflammatory pathways as a likely secondary or pleiotropic signal.

I would next prioritize: cilia/basal body genes, ion/channel/transporter genes, and cytoskeletal/myogenesis genes, then ask whether these are expressed in embryonic heart, cardiac neural crest, second heart field, endocardium, or outflow tract-relevant cell types.

---

### KF-NBL Cohort

**User:** I am working on characterizing genes in a list of about 1200 genes with predicted deleterious germline variants from a neuroblastoma cohort. I'm trying to understand what pathways are activated based on a graph-enrichment method. Can you read the markdown file, review the tsv table, and follow the instructions?

**GPT-5.3:** Yes. I read the markdown instructions and reviewed the TSV. The strongest biological signal is not one single pathway, but a cluster of related processes:

1. **Cilia / centrosome / developmental patterning.** WP_CILIOPATHIES is rank 3 and has the highest null_z among the top pathways. Related significant hits include Joubert syndrome, primary cilium development, cilium assembly, and basal body anchoring. This is highly plausible for neuroblastoma because neural crest development depends on tightly regulated morphogenesis, migration, and signaling.

2. **Ion transport / transmembrane transport.** The top two pathways are Ionophore activity and Transmembrane Transport. These include many channel and transporter genes. In neuroblastoma, this could connect to neural excitability, calcium signaling, membrane potential, differentiation state, and drug response.

3. **DNA repair / genome maintenance.** DNA Repair is rank 5, with additional hits for recombinational repair, mismatch repair, Fanconi pathway, homologous recombination, and nucleotide excision repair. This is one of the most disease-relevant signals for germline deleterious variants in a cancer cohort.

4. **Metabolism.** Amino acid metabolism, carbohydrate metabolism, nucleotide metabolism, mitochondrial tRNA aminoacylation, xenobiotic metabolism, and broader Reactome metabolism pathways are all significant. This suggests altered cellular growth, biosynthetic demand, mitochondrial function, or detoxification biology.

5. **Cell shape / ECM / adhesion.** Regulation of Cell Shape is rank 4, and later significant pathways include extracellular matrix organization, collagen formation/degradation, cell-matrix junction, and integrin pathways. This fits a neural crest tumor context because migration, adhesion, and invasion are central to neuroblastoma biology.

Main caution: many top pathways show the same contributing seeds -- TP53, JAK1, MAPK1, TSHR, and JAK2. That means the graph-propagation signal may be strongly routed through a small set of high-connectivity signaling genes. I would interpret the repeated pathway themes as useful, but I would not over-interpret individual pathway ranks without checking whether these genes dominate the signal.

**Most biologically compelling follow-up shortlist:**

- Cilia/centrosome biology
- DNA repair and homologous recombination
- Ion/transporter biology
- ECM/cell-shape/neural crest migration
- Mitochondrial and amino acid metabolism

The analysis used 1,395 resolved seed genes from the KF-NBL cohort, scored 2,196 pathways, and found 296 significant pathways at q < 0.05.


## References {.page_break_before}

