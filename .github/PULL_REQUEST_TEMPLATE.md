## What I built
- Metabase dashboard (Week 11 Submissions collection): <link>
- Streamlit app: `week11-streamlit/app.py` (KPIs, hour-of-day trend, freshness, payment-type filter)
- Presentation recording (private, hosted in the Azure `student-submissions` container): <link>

## How to review
- Metabase: open the dashboard link above, or see the committed screenshots / PDF export.
- Streamlit: see the committed screenshots, or run it yourself with the steps below.
- Metric definitions: `week11-streamlit/metric_definitions.md`
- AI usage: `AI_ASSIST.md`

## How to run the Streamlit app
From a clean clone, with your own Postgres access:

```bash
cd week11-streamlit
uv sync
cp .env.example .env      # set your own POSTGRES_URL (with ?sslmode=require) + DB_SCHEMA
uv run streamlit run app.py
```

Prerequisite: your own `fct_trips` mart populated in your `dev_<name>` schema (from Week 10).

> Data dependency: these run steps need **your own** Week 10 mart. A reviewer who does not have that data cannot rebuild your numbers, so the committed **screenshots / PDF export are the canonical evidence** of a working submission.

## What reviewers should see (expected results)
Fill in the numbers your dashboard and app actually show, so a reviewer can tell at a glance whether the result looks correct:
- Total trips (`fct_trips` row count): <e.g. ~57k>
- Busiest hour of day: <e.g. 18:00>
- Top payment type by share: <e.g. credit card, ~70%>
- Data freshness (latest trip date shown): <e.g. 2023-01-31>

## Known limitations / out of scope
- <e.g. auto-refresh not implemented; dashboard covers January 2023 only; one Metabase filter still hardcoded>
- Write "none" if everything in the assignment is done and working.

## Extra completed
- [ ] Metabase date filter on >=2 Questions
- [ ] Streamlit auto-refresh

## Self-check
- [ ] `bash .hyf/test.sh` passes
- [ ] No credentials committed (no password in `app.py`, `.env` is gitignored)
- [ ] Screenshots of the Metabase dashboard and the running Streamlit app are committed
