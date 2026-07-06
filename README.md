<p align="center">
  <img src="assets/readme-cover.svg" alt="Web Scrape Ethics Check cover" width="100%" />
</p>

# Web Scrape Ethics Check

![stack](https://img.shields.io/badge/stack-Python-2563eb?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-16a34a?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-dc2626?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-7c3aed?style=flat-square)

Review scraping plans for robots, rate limits, and data-use constraints.

## Why it exists

Small review tasks are easy to skip when the signal lives in notes, spreadsheets, or loosely formatted exports. `web-scrape-ethics-check` turns those checks into a repeatable command with plain findings and CI-friendly exit codes.

## Quick run

```bash
python -m pip install -e ".[dev]"
web-scrape-ethics-check examples/sample.txt
web-scrape-ethics-check examples/sample.txt --json --fail-on medium
```

## Rule set

| Rule | Severity | What it catches |
| --- | --- | --- |
| `robots-unknown` | high | robots policy unknown |
| `no-rate-limit` | medium | rate limit missing |
| `personal-data` | low | personal data may be scraped |

## Input

The reader accepts plain text, JSON, JSONL, and CSV. That keeps it useful for hand-written notes, review exports, and small automation jobs.

## Sample risky input

```text
robots unknown rate_limit none personal_data true
```

## Development

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m web_scrape_ethics_check --help
```

`cli.py` handles arguments, `core.py` reads and evaluates records, and `rules.py` keeps the Web Scrape Ethics Check policy easy to review.
