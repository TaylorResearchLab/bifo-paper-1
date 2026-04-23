### ST6: BIFO-PPR propagating edge composition — predicate, flow class, and source vocabulary attribution


All predicates present in BIFO-conditioned kept_edges files across the benchmark (CHD curated, 15-gene pool) and KF cohort analyses (KF-CHD: 1,276 seeds; KF-NBL: 1,395 seeds). Counts reflect edges from the source node perspective; forward and inverse predicate directions are listed separately. Source SABs are derived by joining kept_edges source node IDs to the DDKG node SAB field. UNKNOWN indicates nodes without a resolvable source vocabulary. Propagating=True edges enter the PPR adjacency matrix; Propagating=False edges are retained in kept_edges for reference only and excluded from propagation. Flow class and classification tier are sourced directly from bifo_mapping.yaml v0.7.1. Predicates with classification non_flow_edge are in the YAML non_flow_edges list and received observational fallthrough classification during conditioning. All analyses used the August 2025 DDKG release.

---

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

---

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