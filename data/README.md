# Data

Start with `country_exposure_adoption_snapshot.csv` if you want a quick
country-level table in one place. It combines national exposure scores, exposure
rank, employment, reliability, region and income metadata, white-collar
structure, observed Anthropic/OpenAI/Microsoft adoption measures where
available, and remittance exposure fields.

The remaining folders contain the full release tables:

- `core/`: canonical exposure tables and ISCO-08 occupation exposure scores.
- `aggregates/`: map-ready country data and region/income summaries.
- `mechanisms/`: white-collar, gender, wage, labor-share, and occupation
  contribution tables.
- `validation/`: observed adoption/usage validation tables and appendix
  regression inputs.
- `indirect/`: remittance-accounted exposure and selected corridor evidence.
- `robustness/`: alternative exposure and boundary-sensitivity checks.
- `coverage/`: sample accounting and excluded-country categories.
- `paper_tables/`: compact tables used directly by the paper or website.

See `../DATA_GUIDE.md`, `../manifest.csv`, and `../data_dictionary.csv` for
merge logic, row counts, checksums, and column definitions.
