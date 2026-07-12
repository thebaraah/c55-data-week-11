# Week 11 Assignment: Build Two Dashboards

HackYourFuture Data Track, Week 11. The full brief (scenario, all three tiers, and submission steps) lives in the curriculum: **Week 11 → Assignment** in the HackYourFuture learning platform. Read it first; this repo only gets you started.

## What you build

Two dashboards reading the same `fct_trips` / `fct_daily_borough_stats` marts from Week 10, on Azure PostgreSQL:

- A **Metabase** analytical dashboard: point-and-click Questions and a shared Dashboard.
- A **Streamlit** metrics app: a code-first page with KPI, trend, and freshness panels.

Both get documented in `metric_definitions.md` so nobody argues about what a number means.

## What this repo gives you

This repo is a **ready-to-run Streamlit project** for the code-first dashboard, plus a destination for your Metabase deliverables:

```text
.
├── README.md                       <- TODO: your Metabase dashboard link / screenshots go here
├── AI_ASSIST.md                     <- TODO: template, document one LLM session
├── metric_definitions.template.md   <- copy into week11-streamlit/ (see below)
├── week11-streamlit/                <- ready-to-run: project config wired up, KPI panel is a TODO stub
│   ├── app.py                       <- TODO: implement the headline KPIs panel
│   ├── pyproject.toml
│   ├── uv.lock
│   └── .env.example                 <- copy to .env, fill in your credentials
└── .hyf/                            <- autograder, do not edit
```

- **Metabase**: build it directly in the HYF-managed Metabase instance. There is nothing to scaffold here: put the dashboard link (or screenshots, if the public link is unavailable) in this `README.md`, under "My submission" below.
- **Streamlit**: `week11-streamlit/` is already wired up (same `run_query` caching pattern taught in "Building a Metrics Dashboard", Week 11 Chapter 5) with page setup done and the headline-KPIs panel stubbed as `raise NotImplementedError(...)`. Your job is the query and the three `.metric()` tiles, not the project scaffolding:

```bash
cd week11-streamlit
uv sync
cp .env.example .env   # fill in your credentials
uv run streamlit run app.py
```

Once your KPI panel runs, copy the template into place and fill it in:

```bash
cp metric_definitions.template.md week11-streamlit/metric_definitions.md
```

Fill in `week11-streamlit/metric_definitions.md`: a five-field definition (name, description, calculation, data source, refresh frequency) for **every Metabase Question and every Streamlit panel** you build.

## My submission

<!-- TODO: paste your Metabase dashboard link, or add screenshots to this repo and reference them here. -->

TODO

## Check your score locally

The autograder runs static checks (required files present, secrets hygiene, Streamlit code patterns, metric-definition coverage):

```bash
bash .hyf/test.sh
cat .hyf/score.json
```

Passing score: 60/100. This covers the **Required** tier only: it cannot verify your dashboards render real data (that needs a live Azure Postgres connection CI does not have), so a passing score is necessary but not sufficient. Your teacher reviews the actual dashboards and presentation for Required/Extra credit.

## Submitting

Follow the Submission section of the assignment chapter: branch `week11/your-name`, commit, push, open a PR, and note in the PR description whether you also completed any Extra items plus your Metabase dashboard link.
