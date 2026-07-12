"""NYC Taxi metrics dashboard — Week 11 assignment starter.

Reads the Week 10 dbt mart ``fct_trips`` from Azure Postgres. The page
setup and the ``run_query`` caching helper are already wired up (same
pattern taught in "Building a Metrics Dashboard"). Your job: implement the
three TODO-stubbed KPI queries below with your own SQL, then (Required tier)
add the hour-of-day trend, freshness panel, and payment-type filter
described in the assignment brief.
"""

import os

import pandas as pd
import sqlalchemy
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # reads .env file if present

POSTGRES_URL = os.environ["POSTGRES_URL"]
DB_SCHEMA = os.environ.get("DB_SCHEMA", "dev_yourname")

st.set_page_config(page_title="NYC Taxi Metrics", layout="wide")
st.title("NYC Taxi Metrics")


@st.cache_data(ttl=300)
def run_query(sql: str) -> pd.DataFrame:
    engine = sqlalchemy.create_engine(POSTGRES_URL)
    with engine.connect() as conn:
        return pd.read_sql(sql, conn)


st.subheader("Headline KPIs")

# TODO: query total trip count, average trip_distance, and average
# fare_per_mile from {DB_SCHEMA}.fct_trips through run_query(), then
# render three tiles side by side with st.columns(3) and .metric().
# This is deliberately not the total-trips/avg-fare/total-revenue trio
# from the chapter: trip_distance and fare_per_mile are different columns,
# so copying the chapter's SQL verbatim will not answer this.
raise NotImplementedError(
    "TODO: implement the headline KPIs panel (total trips, avg trip "
    "distance, avg fare per mile) from fct_trips."
)
