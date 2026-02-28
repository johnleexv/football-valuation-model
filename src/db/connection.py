"""DuckDB connection management."""

import duckdb
from pathlib import Path

DB_PATH = Path(__file__).resolve().parents[2] / "data" / "analyst.duckdb"


def get_connection(read_only: bool = False) -> duckdb.DuckDBPyConnection:
    """Return a DuckDB connection to the main database."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return duckdb.connect(str(DB_PATH), read_only=read_only)
