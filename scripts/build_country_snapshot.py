#!/usr/bin/env python3
"""Build a GitHub-previewable country snapshot table for the website Data link."""

from __future__ import annotations

import csv
import math
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
DATA_DIR = REPO_ROOT / "data"
OUT_PATH = DATA_DIR / "country_exposure_adoption_snapshot.csv"

ADOPTION_COLUMNS = {
    "anthropic": "anthropic_claude_usage_per_100k_wap",
    "signals": "openai_signals_rank_percentile",
    "microsoft": "microsoft_genai_adoption_pct_wap",
}

FIELDNAMES = [
    "country_code",
    "country_name",
    "region",
    "income_group",
    "reliability",
    "national_ai_exposure",
    "exposure_rank_1_highest",
    "exposure_percentile_100_highest",
    "total_employment_m_workers",
    "white_collar_worker_share",
    "white_collar_ai_exposure",
    "other_worker_ai_exposure",
    "gni_per_capita_ppp",
    "anthropic_claude_usage_per_100k_wap",
    "openai_signals_rank_percentile",
    "microsoft_genai_adoption_pct_wap",
    "remittance_pct_gdp",
    "remittance_accounted_exposure",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def as_float(value: str | None) -> float | None:
    if value is None or value == "":
        return None
    try:
        parsed = float(value)
    except ValueError:
        return None
    return parsed if math.isfinite(parsed) else None


def fmt(value: float | None, digits: int) -> str:
    if value is None:
        return ""
    return f"{value:.{digits}f}"


def build_adoption_lookup() -> dict[str, dict[str, float]]:
    rows = read_csv(DATA_DIR / "validation/observed_outcomes_vs_exposure.csv")
    lookup: dict[str, dict[str, float]] = {}
    for row in rows:
        column = ADOPTION_COLUMNS.get(row["source_key"])
        value = as_float(row["outcome_value"])
        if not column or value is None:
            continue
        lookup.setdefault(row["country_code"], {})[column] = value
    return lookup


def main() -> None:
    core_rows = read_csv(DATA_DIR / "core/nation_exposure_enriched.csv")
    map_lookup = {
        row["country_code"]: row for row in read_csv(DATA_DIR / "aggregates/national_exposure_map_data.csv")
    }
    adoption_lookup = build_adoption_lookup()
    remittance_lookup = {
        row["country_code"]: row for row in read_csv(DATA_DIR / "indirect/remittance_weighted_exposure.csv")
    }

    exposures = sorted(
        (
            (row["country_code"], as_float(row["weighted_exposure"]))
            for row in core_rows
        ),
        key=lambda item: (item[1] is None, -(item[1] or -1)),
    )
    ranks = {code: rank for rank, (code, _value) in enumerate(exposures, start=1)}
    n = len(exposures)

    output_rows: list[dict[str, str]] = []
    for row in sorted(core_rows, key=lambda item: ranks[item["country_code"]]):
        code = row["country_code"]
        map_row = map_lookup.get(code, {})
        remittance = remittance_lookup.get(code, {})
        adoption = adoption_lookup.get(code, {})
        rank = ranks[code]
        percentile = 100 * (n - rank) / (n - 1) if n > 1 else None
        employment_k = as_float(row["total_employment_k"])

        output_rows.append(
            {
                "country_code": code,
                "country_name": row["country_name"],
                "region": map_row.get("region", ""),
                "income_group": map_row.get("income_group", ""),
                "reliability": row["reliability"],
                "national_ai_exposure": fmt(as_float(row["weighted_exposure"]), 4),
                "exposure_rank_1_highest": str(rank),
                "exposure_percentile_100_highest": fmt(percentile, 1),
                "total_employment_m_workers": fmt(employment_k / 1000 if employment_k is not None else None, 1),
                "white_collar_worker_share": fmt(as_float(row["wc_share"]), 4),
                "white_collar_ai_exposure": fmt(as_float(row["wc_exposure"]), 4),
                "other_worker_ai_exposure": fmt(as_float(row["bc_exposure"]), 4),
                "gni_per_capita_ppp": fmt(as_float(row["gni_ppp"]), 0),
                "anthropic_claude_usage_per_100k_wap": fmt(
                    adoption.get("anthropic_claude_usage_per_100k_wap"), 3
                ),
                "openai_signals_rank_percentile": fmt(adoption.get("openai_signals_rank_percentile"), 3),
                "microsoft_genai_adoption_pct_wap": fmt(adoption.get("microsoft_genai_adoption_pct_wap"), 3),
                "remittance_pct_gdp": fmt(as_float(remittance.get("remittance_pct_gdp")), 2),
                "remittance_accounted_exposure": fmt(as_float(remittance.get("remit_weighted_exposure")), 4),
            }
        )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Wrote {OUT_PATH.relative_to(REPO_ROOT)} with {len(output_rows)} rows and {len(FIELDNAMES)} columns")


if __name__ == "__main__":
    main()
