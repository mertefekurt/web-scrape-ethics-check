# Web Scrape Ethics Check

![Web Scrape Ethics Check cover](assets/readme-cover.svg)

Review scraping plans for robots, rate limits, and data-use constraints. In practice it is a narrow guardrail for small developer checks: one command, a concrete report, and very little ceremony.

## Web Scrape Ethics Check catches

- `robots-unknown` (high): robots policy unknown. Fix: check robots and terms.
- `no-rate-limit` (medium): rate limit missing. Fix: set polite crawl rate.
- `personal-data` (low): personal data may be scraped. Fix: review privacy basis.

## A normal pass

```bash
git clone https://github.com/mertefekurt/web-scrape-ethics-check.git
cd web-scrape-ethics-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
web-scrape-ethics-check examples/sample.txt
web-scrape-ethics-check examples/sample.txt --json
```

The input can be text, JSON, JSONL, or CSV. Use `--json` when another script needs the result instead of a Markdown report.

## A deliberately bad line

```text
robots unknown rate_limit none personal_data true
```

## Maintainer loop

```bash
ruff check .
pytest
python -m web_scrape_ethics_check --help
```
