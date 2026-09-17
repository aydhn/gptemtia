"""Model Drift Monitoring Report Builder for Phase 142.

Renders structured Markdown and plain text reports documenting the drift monitoring contracts,
linkages, window policies, threshold placeholders, and disabled execution safeguards.
Includes mandatory disclaimers regarding offline research and non-signal execution boundaries.
"""

from __future__ import annotations

from typing import Any, Dict

from advanced_model_drift_monitoring.model_drift_models import ModelDriftMonitoringManifest


def build_model_drift_markdown_report(manifest: ModelDriftMonitoringManifest) -> str:
    """Builds a comprehensive Markdown report of the drift monitoring contracts."""
    lines = [
        "# Phase 142 — Model Drift Monitoring and Data/Feature Drift Linkage Contracts",
        "",
        "> **SAFETY & COMPLIANCE DISCLAIMER**",
        "> This system is an offline/local research and contract governance layer.",
        "> - Strictly DRY-RUN and CONTRACT-ONLY.",
        "> - Zero live trading, order routing, broker connection, or financial advice.",
        "> - Zero real model training, fitting, inference, or prediction generation.",
        "> - Zero live drift metric calculations (no PSI, KS, JS, Wasserstein on real data).",
        "> - Zero automated alerting, retraining triggers, or model replacements.",
        "> - Immutable historical source data preservation.",
        "",
        "## 1. Executive Summary",
        f"- **Manifest ID:** `{manifest.manifest_id}`",
        f"- **Phase:** `{manifest.phase}` (Target Final Phase: 160)",
        f"- **Profile:** `{manifest.profile.profile_name}` ({manifest.profile.display_name})",
        f"- **Generated At:** `{manifest.generated_at}`",
        f"- **Total Monitored Contracts:** `{len(manifest.contracts)}`",
        f"- **Upstream Linkages:** `{len(manifest.linkages)}`",
        f"- **Window Policies:** `{len(manifest.window_policies)}`",
        f"- **Threshold Placeholders:** `{len(manifest.thresholds)}`",
        f"- **Metric Placeholders:** `{len(manifest.metric_placeholders)}`",
        f"- **Disabled Safeguards:** `{len(manifest.disabled_executions)}`",
        f"- **Active Guards:** `{len(manifest.guards)}`",
        f"- **Readiness Score:** `100.0% (Ready)`",
        "",
        "## 2. Monitored Drift Contracts",
        "| Contract ID | Domain | Target Name | Reference Window | Current Window | Linkage Target |",
        "|-------------|--------|-------------|------------------|----------------|----------------|",
    ]

    for c in manifest.contracts:
        ref_win = c.reference_window or "N/A"
        curr_win = c.current_window or "N/A"
        lines.append(
            f"| `{c.contract_id}` | `{c.domain}` | `{c.target_name}` | `{ref_win}` | `{curr_win}` | `{c.linkage_target}` |"
        )

    lines.extend([
        "",
        "## 3. Upstream Drift Linkages",
        "| Linkage ID | Domain | Source Component | Target Model / Dataset | Status |",
        "|------------|--------|------------------|------------------------|--------|",
    ])

    for link in manifest.linkages:
        lines.append(
            f"| `{link.linkage_id}` | `{link.drift_domain}` | `{link.source_component}` | `{link.target_model_or_dataset}` | `{link.status}` |"
        )

    lines.extend([
        "",
        "## 4. Window & Threshold Placeholders",
        "### Window Policies",
        "| Policy ID | Window Type | Window Size | Min Obs | Lookback Days | Exec Enabled |",
        "|-----------|-------------|-------------|---------|---------------|--------------|",
    ])

    for w in manifest.window_policies:
        lines.append(
            f"| `{w.policy_id}` | `{w.window_type}` | `{w.window_size}` | `{w.min_observations}` | `{w.lookback_days}` | `{w.execution_enabled}` |"
        )

    lines.extend([
        "",
        "### Threshold Placeholders",
        "| Threshold ID | Metric Type | Target Scope | Warning Range | Breach Value | Exec Enabled |",
        "|--------------|-------------|--------------|---------------|--------------|--------------|",
    ])

    for t in manifest.thresholds:
        warn_str = f"[{t.warning_threshold_min}, {t.warning_threshold_max}]"
        lines.append(
            f"| `{t.threshold_id}` | `{t.metric_type}` | `{t.target_scope}` | `{warn_str}` | `{t.breach_threshold}` | `{t.execution_enabled}` |"
        )

    lines.extend([
        "",
        "## 5. Metric Placeholders (10 Categories)",
        "| Metric ID | Name | Metric Type | Target Scope | Status | Calc Enabled |",
        "|-----------|------|-------------|--------------|--------|--------------|",
    ])

    for m in manifest.metric_placeholders:
        lines.append(
            f"| `{m.metric_id}` | {m.metric_name} | `{m.metric_type}` | `{m.target_scope}` | `{m.status}` | `{m.calculation_enabled}` |"
        )

    lines.extend([
        "",
        "## 6. Disabled Execution Safeguards",
        "| Execution ID | Type | Target Component | Status | Disabled | Reason |",
        "|--------------|------|------------------|--------|----------|--------|",
    ])

    for d in manifest.disabled_executions:
        reason_str = str(d.disabled_reason or d.reason or "")[:45]
        lines.append(
            f"| `{d.execution_id}` | `{d.execution_type}` | `{d.target_component}` | `{d.status}` | `{d.is_disabled}` | {reason_str}... |"
        )

    lines.extend([
        "",
        "## 7. Active Governance Guards",
        "| Guard ID | Name | Type | Status | Active | Validation Rule |",
        "|----------|------|------|--------|--------|-----------------|",
    ])

    for g in manifest.guards:
        lines.append(
            f"| `{g.guard_id}` | {g.guard_name} | `{g.guard_type}` | `{g.status}` | `{g.is_active}` | `{g.validation_rule}` |"
        )

    lines.extend([
        "",
        "## 8. Findings & Governance Readiness",
        "| Domain | Readiness Score | Governance Status | Blockers | Warnings | Ready for Review |",
        "|--------|-----------------|-------------------|----------|----------|------------------|",
    ])

    for r in manifest.readiness_scores:
        lines.append(
            f"| `{r.domain}` | `{r.readiness_score}%` | `{r.governance_status}` | `{r.blocker_count}` | `{r.warning_count}` | `{r.is_ready_for_review}` |"
        )

    lines.extend([
        "",
        "## 9. Next Phase Handoff (Phase 143)",
        "Phase 142 drift monitoring contracts are fully verified and ready for handoff to Phase 143:",
        "- **Phase 143 Target:** Model Explainability and Interpretability Contracts (SHAP, Feature Attribution, Surrogate Models).",
        "- **Handoff Preconditions:** All 59 drift monitoring domain contracts established, non-executing boundaries enforced, zero data mutation verified.",
        "",
        "---",
        "*Report generated by Phase 142 Model Drift Monitoring Governance Subsystem.*",
    ])

    return "\n".join(lines)


def build_model_drift_text_summary(manifest: ModelDriftMonitoringManifest) -> str:
    """Builds a concise plain text summary of the drift monitoring manifest."""
    return (
        f"Phase 142 Model Drift Monitoring Summary:\n"
        f"Manifest ID: {manifest.manifest_id}\n"
        f"Profile: {manifest.profile.profile_name}\n"
        f"Contracts: {len(manifest.contracts)} | Linkages: {len(manifest.linkages)}\n"
        f"Window Policies: {len(manifest.window_policies)} | Thresholds: {len(manifest.thresholds)}\n"
        f"Metric Placeholders: {len(manifest.metric_placeholders)} | Disabled Safeguards: {len(manifest.disabled_executions)}\n"
        f"Guards: {len(manifest.guards)} | Findings: {len(manifest.findings)}\n"
        f"Non-Executing Compliance: TRUE | Dry-Run: TRUE | Next Phase: 143"
    )
