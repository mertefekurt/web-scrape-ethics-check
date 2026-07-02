# web-scrape-ethics-check

> Review scraping plans for robots, rate limits, and data-use constraints.

## Runbook Overview

Review scraping plans for robots, rate limits, and data-use constraints. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract 46

Accepts scraping plan. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough 46

```bash
python -m pip install -e ".[dev]"
web-scrape-ethics-check examples/sample.txt
web-scrape-ethics-check examples/sample.txt --json --fail-on medium
python -m web_scrape_ethics_check --help
```

## Rule Surface 46

| Rule | Severity | Meaning |
|---|---:|---|
| `robots-unknown` | high | robots policy unknown |
| `no-rate-limit` | medium | rate limit missing |
| `personal-data` | low | personal data may be scraped |

## Validation Notes 46

```bash
ruff check .
pytest
python -m web_scrape_ethics_check --help
```

Example risky input:

```text
robots unknown rate_limit none personal_data true
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
