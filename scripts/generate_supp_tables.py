#!/usr/bin/env python3
"""
generate_supp_tables.py
Generates Supplementary Tables ST1–ST4 as markdown from BIFO pipeline outputs.

Usage (on HPC):
    cd /mnt/isilon/taylor_lab/data/projects/BIFO_2026/
    python3 generate_supp_tables.py

Output:
    supp_tables_ST1_ST4.md  — review, then paste sections into 07.supplementary.md
"""

import pandas as pd
import json
import os
import sys

# =============================================================================
# PATHS
# =============================================================================

CHD_BENCHMARK  = "/mnt/isilon/taylor_lab/data/projects/BIFO_2026/results/chd_curated"
KF_CHD_RESULTS = "/mnt/isilon/taylor_lab/data/projects/BIFO_2026/bifo_run_chd/kf_chd_results"
KF_NBL_RESULTS = "/mnt/isilon/taylor_lab/data/projects/BIFO_2026/bifo_run_nbl/kf_nbl_results"

OUTPUT_FILE = "supp_tables_ST1_ST4.md"

# =============================================================================
# HELPERS
# =============================================================================

def check_path(path, label):
    if not os.path.exists(path):
        print(f"ERROR: {label} not found at:\n  {path}", file=sys.stderr)
        sys.exit(1)

def fmt_score(val):
    try:
        f = float(val)
        if abs(f) < 0.001:
            return f"{f:.3e}"
        return f"{f:.4f}"
    except (ValueError, TypeError):
        return str(val)

def yes_no(val):
    try:
        if str(val).strip().lower() in ('true', '1', 'yes'):
            return "✓"
        return "—"
    except:
        return "—"

def md_table(headers, rows):
    lines = []
    lines.append("| " + " | ".join(str(h) for h in headers) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    return "\n".join(lines)

# =============================================================================
# ST1 — Top-10 ranked pathways per arm, curated CHD benchmark
# top_50 entry fields: concept_id, name, sab, degree_norm, member_gene_count,
#                      degree_flag, in_chd_set, contributing_seeds
# =============================================================================

def build_ST1():
    print("Building ST1...")
    lines = []
    lines.append("### ST1 — Top-10 ranked pathways per propagation arm, curated CHD benchmark\n")
    lines.append(
        "Three-arm comparison: Full BIFO (94,309 propagating edges), "
        "Ablation (16,026 propagating edges, no Pathway Contribution bridge edges), "
        "and Mechanistic-only (9,710 edges). Pathway universe: 550 pathways (8–300 members). "
        "CHD reference pathways marked with ✓ in the Ref. column. "
        "Score = degree_norm (direct PPR score at pathway node / √member count).\n"
    )

    arm_configs = [
        ('full',     'Full BIFO',                    False),
        ('ablation', 'Ablation (no bridge edges)',   False),
        ('mech',     'Mechanistic-only',             True),
    ]

    for arm, label, is_mech in arm_configs:
        metrics_path = os.path.join(CHD_BENCHMARK, f"pathway_metrics_{arm}.json")
        check_path(metrics_path, f"pathway_metrics_{arm}.json")

        with open(metrics_path) as f:
            metrics = json.load(f)

        lines.append(f"**{label}**\n")

        if is_mech:
            lines.append(
                "*All 550 pathway scores are exactly zero under mechanistic-only propagation. "
                "Pathway nodes are structurally unreachable from seed genes through mechanistic "
                "edges alone; gene-to-pathway connectivity requires Pathway Contribution bridge "
                "edges. P@10 = 0.00, Enrichment@10 = 0×.*\n"
            )
            continue

        ranked = metrics.get('top_50', [])
        if not ranked:
            lines.append(f"*[No top_50 entries found in {arm} metrics file.]*\n")
            continue

        headers = ["Rank", "Pathway name", "SAB", "Score (degree_norm)", "Members", "Ref."]
        rows = []
        for i, entry in enumerate(ranked[:10], 1):
            rows.append([
                i,
                entry['name'],
                entry.get('sab', '—'),
                fmt_score(entry['degree_norm']),
                entry.get('member_gene_count', '—'),
                yes_no(entry.get('in_chd_set', False))
            ])
        lines.append(md_table(headers, rows))
        lines.append("\n")

    return "\n".join(lines)

# =============================================================================
# ST2 — Baseline enrichment comparison, curated CHD benchmark
# Source: baseline_comparison.csv
# Columns: method, rank, concept_id, name, sab, in_chd_set, stat,
#          bh_adjusted_p, neg_log10_bh_p, overlap_or_es, pathway_size
# =============================================================================

def build_ST2():
    print("Building ST2...")
    lines = []
    lines.append("### ST2 — Baseline enrichment method comparison, curated CHD benchmark\n")
    lines.append(
        "Top-20 ranked pathways under each enrichment method, evaluated on the identical "
        "550-pathway universe. CHD reference pathways marked with ✓. "
        "Score/stat column: degree_norm for B0 and B4; hypergeometric stat for B1/B2; "
        "enrichment score for B3/B3b.\n"
    )

    bc_path = os.path.join(CHD_BENCHMARK, "baseline_comparison.csv")
    check_path(bc_path, "chd baseline_comparison.csv")
    bc = pd.read_csv(bc_path)

    print(f"  Available methods: {sorted(bc['method'].unique().tolist())}")

    method_order = [
        ('degree_overlap',      'B0 — Degree-weighted seed overlap'),
        ('seed_fisher',         'B1 — Seed-only Fisher (hypergeometric)'),
        ('neighborhood_fisher', 'B2 — 1-hop neighborhood Fisher'),
        ('raw_ppr_gsea',        'B3 — Raw PPR preranked GSEA'),
        ('cond_ppr_gsea',       'B3b — Conditioned PPR preranked GSEA'),
        ('bifo_full',           'B4 — BIFO full-arm (degree_norm)'),
    ]

    headers = ["Rank", "Pathway name", "SAB", "Score / stat", "Members", "Ref."]

    for method_key, method_label in method_order:
        subset = bc[bc['method'] == method_key].sort_values('rank').head(20)
        if subset.empty:
            lines.append(f"**{method_label}**\n")
            lines.append(f"*[Method key '{method_key}' not found. "
                        f"Available: {sorted(bc['method'].unique().tolist())}]*\n")
            continue

        lines.append(f"**{method_label}**\n")
        rows = []
        for _, row in subset.iterrows():
            # Use stat if available, else overlap_or_es
            score = row.get('stat') if pd.notna(row.get('stat', float('nan'))) \
                    else row.get('overlap_or_es', '—')
            rows.append([
                int(row['rank']),
                row['name'],
                row.get('sab', '—'),
                fmt_score(score),
                int(row['pathway_size']) if pd.notna(row.get('pathway_size', float('nan'))) else '—',
                yes_no(row.get('in_chd_set', False))
            ])
        lines.append(md_table(headers, rows))
        lines.append("\n")

    return "\n".join(lines)

# =============================================================================
# ST3 — Top-20 ranked pathways per method, KF-CHD and KF-NBL
# Source: baseline_comparison.csv from each cohort results directory
# =============================================================================

def build_ST3():
    print("Building ST3...")
    lines = []
    lines.append("### ST3 — Top-20 ranked pathways per method, KF-CHD and KF-NBL cohorts\n")
    lines.append(
        "Five enrichment methods evaluated in discovery mode (no reference pathway "
        "pre-specified). KF-CHD: 5,124 pathways scored; KF-NBL: 5,203 pathways scored. "
        "Cilia reference pathways marked with ✓.\n"
    )

    method_order = [
        ('seed_fisher',         'Seed Fisher corrected (B1)'),
        ('neighborhood_fisher', 'Neighborhood Fisher (B2)'),
        ('raw_ppr_gsea',        'Raw PPR GSEA (B3)'),
        ('cond_ppr_gsea',       'Conditioned PPR GSEA (B3b)'),
        ('bifo_full',           'BIFO full-arm (B4)'),
    ]

    cohorts = [
        ('KF-CHD', KF_CHD_RESULTS),
        ('KF-NBL', KF_NBL_RESULTS),
    ]

    headers = ["Rank", "Pathway name", "SAB", "Score / stat", "Members", "Cilia ref."]

    for cohort_label, results_dir in cohorts:
        bc_path = os.path.join(results_dir, "baseline_comparison.csv")
        check_path(bc_path, f"{cohort_label} baseline_comparison.csv")
        bc = pd.read_csv(bc_path)
        print(f"  {cohort_label} methods: {sorted(bc['method'].unique().tolist())}")

        lines.append(f"**{cohort_label}**\n")

        for method_key, method_label in method_order:
            subset = bc[bc['method'] == method_key].sort_values('rank').head(20)
            if subset.empty:
                lines.append(f"*{method_label}* — method key '{method_key}' not found\n")
                continue

            lines.append(f"*{method_label}*\n")
            rows = []
            for _, row in subset.iterrows():
                score = row.get('stat') if pd.notna(row.get('stat', float('nan'))) \
                        else row.get('overlap_or_es', '—')
                # cilia ref flag — try in_chd_set (present in both cohort files per header)
                cilia = yes_no(row.get('in_chd_set', False))
                rows.append([
                    int(row['rank']),
                    row['name'],
                    row.get('sab', '—'),
                    fmt_score(score),
                    int(row['pathway_size']) if pd.notna(row.get('pathway_size', float('nan'))) else '—',
                    cilia
                ])
            lines.append(md_table(headers, rows))
            lines.append("\n")

    return "\n".join(lines)

# =============================================================================
# ST4 — Full cilia pathway cluster ranking under BIFO, KF-CHD and KF-NBL
# Source: pathway_scores_standard.csv from each cohort
# Columns: concept_id, name, sab, direct, member_mean, member_max, degree_norm,
#          local_bg, direct_raw, raw_vs_cond_delta, member_gene_count, degree,
#          degree_flag, in_chd_set, contributing_seeds
# Cilia pathways identified by in_chd_set flag OR name pattern
# =============================================================================

CILIA_TERMS = [
    'ciliopath', 'ciliar', 'intraflagellar', 'joubert', 'bardet-biedl',
    'bardet biedl', 'primary ciliary', 'cilium assembly', 'cilium',
    ' cilia', 'hedgehog signaling', 'hedgehog pathway',
    'nephronophthisis', 'meckel', 'alstrom', 'senior-loken',
    'bbsome', 'leber congenital amaurosis'
]

def is_cilia(name):
    n = str(name).lower()
    return any(t in n for t in CILIA_TERMS)

def build_ST4():
    print("Building ST4...")
    lines = []
    lines.append("### ST4 — Full cilia pathway cluster ranking under BIFO, KF-CHD and KF-NBL\n")
    lines.append(
        "All cilia, ciliopathy, and hedgehog pathway annotations in the scored universe "
        "identified by name pattern matching, ordered by KF-CHD BIFO rank. "
        "Score = degree_norm. Hub-flagged pathways (degree_flag = True) are high-degree "
        "graph hubs not driven by specific cilia signal.\n"
    )

    chd_path = os.path.join(KF_CHD_RESULTS, "pathway_scores_standard.csv")
    nbl_path = os.path.join(KF_NBL_RESULTS, "pathway_scores_standard.csv")
    check_path(chd_path, "KF-CHD pathway_scores_standard.csv")
    check_path(nbl_path, "KF-NBL pathway_scores_standard.csv")

    chd = pd.read_csv(chd_path)
    nbl = pd.read_csv(nbl_path)

    # Rank by degree_norm descending
    chd = chd.sort_values('degree_norm', ascending=False).reset_index(drop=True)
    chd['bifo_rank'] = chd.index + 1

    nbl = nbl.sort_values('degree_norm', ascending=False).reset_index(drop=True)
    nbl['bifo_rank'] = nbl.index + 1

    # Identify cilia pathways: in_chd_set==True OR name matches pattern
    chd_cilia = chd[chd['name'].apply(is_cilia) | chd['in_chd_set'].astype(str).str.lower().eq('true')].copy()

    print(f"  CHD cilia pathways identified: {len(chd_cilia)}")

    if chd_cilia.empty:
        lines.append("*[No cilia pathways identified. Check CILIA_TERMS in script.]*\n")
        return "\n".join(lines)

    # NBL lookup by concept_id
    nbl_idx = nbl.set_index('concept_id')

    headers = [
        "Pathway name", "Source DB",
        "KF-CHD rank", "KF-CHD score",
        "KF-NBL rank", "KF-NBL score",
        "Members", "Hub"
    ]
    rows = []
    for _, row in chd_cilia.sort_values('bifo_rank').iterrows():
        cui = row['concept_id']
        if cui in nbl_idx.index:
            nbl_rank  = int(nbl_idx.loc[cui, 'bifo_rank'])
            nbl_score = fmt_score(nbl_idx.loc[cui, 'degree_norm'])
        else:
            nbl_rank  = '—'
            nbl_score = '—'
        hub = yes_no(row.get('degree_flag', False))
        rows.append([
            row['name'],
            row.get('sab', '—'),
            int(row['bifo_rank']),
            fmt_score(row['degree_norm']),
            nbl_rank,
            nbl_score,
            int(row['member_gene_count']) if pd.notna(row.get('member_gene_count', float('nan'))) else '—',
            hub
        ])

    lines.append(md_table(headers, rows))
    lines.append("\n")
    lines.append(
        f"*{len(rows)} cilia-related pathways identified across "
        f"{len(chd):,} scored pathways (KF-CHD universe).*\n"
    )

    return "\n".join(lines)

# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    out = []
    out.append("## Supplementary Tables ST1–ST4\n")
    out.append("*Generated by generate_supp_tables.py — review before pasting into 07.supplementary.md*\n")
    out.append("\n---\n")
    out.append(build_ST1())
    out.append("\n---\n")
    out.append(build_ST2())
    out.append("\n---\n")
    out.append(build_ST3())
    out.append("\n---\n")
    out.append(build_ST4())

    with open(OUTPUT_FILE, 'w') as f:
        f.write("\n".join(out))

    print(f"\nDone. Output written to: {OUTPUT_FILE}")
    print("Check for any lines containing '[' which indicate missing data or key mismatches.")
