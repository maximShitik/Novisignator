# infrastructure/db.py
import psycopg2.pool

def create_db_pool(database_url):
    return psycopg2.pool.SimpleConnectionPool(1, 10, database_url)