# Provenance and Reproducibility Scope

This reviewer package reproduces paper-facing values, regression tables, and
release-supported figures from released derived measured CSV tables where
redistribution permits. It does not redistribute raw third-party source files
and does not rebuild the private raw-source pipeline.

The upstream sources are listed in `metadata/source_data_manifest.csv` with
URLs, source roles, and redistribution notes. Raw files are omitted because
provider terms are mixed, the Hosseini Maasoum and Lichtinger source has no
verified standalone open-data redistribution license for transformed score
vectors, and the raw research workspace contains local paths and non-anonymized
draft material. Microsoft AI Diffusion country/economy values are included from
Microsoft's official MIT-licensed GitHub data release after ISO alpha-3 matching.

This package is therefore scoped to reviewer verification: validate released
tables, recompute headline quantities, and regenerate value-equivalent paper
tables and supported figures from anonymized derived measured data. Microsoft
paper claims are supported by the released Microsoft country/economy adoption
table, aggregate regression summaries, and source-linked documentation.
Hosseini Maasoum and Lichtinger robustness claims are supported through
aggregate summary statistics and source-linked documentation rather than
redistributed transformed score vectors.
