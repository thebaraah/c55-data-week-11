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

## Extra completed
- [ ] Metabase date filter on >=2 Questions
- [ ] Streamlit auto-refresh

## Self-check
- [ ] `bash .hyf/test.sh` passes
- [ ] No credentials committed (no password in `app.py`, `.env` is gitignored)
- [ ] Screenshots of the Metabase dashboard and the running Streamlit app are committed
