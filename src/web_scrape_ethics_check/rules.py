from __future__ import annotations

from web_scrape_ethics_check.models import Rule

PROJECT_NAME = 'web-scrape-ethics-check'
SUMMARY = 'Review scraping plans for robots, rate limits, and data-use constraints.'
SAMPLE_RISK = 'robots unknown rate_limit none personal_data true'
SAMPLE_CLEAN = 'robots allowed rate_limit 1/sec personal_data false'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='robots-unknown',
        severity='high',
        pattern='robots\\s+(unknown|missing|none)',
        message='robots policy unknown',
        recommendation='check robots and terms',
    ),
    Rule(
        code='no-rate-limit',
        severity='medium',
        pattern='rate_limit\\s+(none|missing|unknown)',
        message='rate limit missing',
        recommendation='set polite crawl rate',
    ),
    Rule(
        code='personal-data',
        severity='low',
        pattern='personal_data\\s+true',
        message='personal data may be scraped',
        recommendation='review privacy basis',
    ),
)
