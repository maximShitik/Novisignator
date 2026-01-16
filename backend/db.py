import sqlite3
from pathlib import Path

# Path to the SQLite file (repo_root/db/app.db)
DB_PATH = Path(__file__).resolve().parent.parent / "db" / "app.db"


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # allows dict-like access by column name
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def fetch_all(query: str, params: tuple = ()):
    conn = get_conn()
    cur = conn.execute(query, params)
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]


def fetch_one(query: str, params: tuple = ()):
    conn = get_conn()
    cur = conn.execute(query, params)
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None


def execute(query: str, params: tuple = ()):
    conn = get_conn()
    conn.execute(query, params)
    conn.commit()
    conn.close()
