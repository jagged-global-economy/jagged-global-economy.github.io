# Data Card

## Dataset Description

The release contains derived aggregate CSV tables for a national AI exposure
analysis. The central metric aggregates occupation-level AI exposure scores
over national occupational employment shares.

## Data Sources

Upstream sources include Gmyrek et al. occupational exposure scores, ILOSTAT
occupational employment and wage/labor-share inputs, World Bank national
indicators and classifications, KNOMAD bilateral remittance matrices, and
provider-published aggregate AI usage/adoption statistics. The release includes
a project-authored country-level extraction from the Microsoft AI Diffusion
public report table for website replication and validation plots. Hosseini
Maasoum and Lichtinger transformed score vectors are not redistributed; the
release includes aggregate robustness statistics and source links only.

## Responsible AI Notes

- No synthetic data are included.
- No individual-level records or direct personal identifiers are included.
- Country-level and occupation-level aggregates can still be sensitive in
  policy contexts and should be interpreted carefully.
- Exposure is a structural measure of economic relevance, not a job-loss
  measure.
- Missing major economies and uneven source-data coverage limit
  generalization.

## Redistribution

This release redistributes derived aggregate tables and selected
provider-reported values where included. Raw upstream source files and API
mirrors are not included. For Microsoft AI Diffusion, the release includes a
project-authored extraction from the public report table; users should consult
the source-data manifest and Microsoft source terms before downstream reuse. For
Hosseini Maasoum and Lichtinger, transformed score vectors are omitted. Users
should consult the source-data manifest for original provider terms and
citations.
