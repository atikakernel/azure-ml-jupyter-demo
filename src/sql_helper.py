import os, pandas as pd, pyodbc

_CONN = os.getenv(SQL_CONN)     # se inyectará en AML

def query(sql: str) -> pd.DataFrame:
    with pyodbc.connect(_CONN) as cn:
        return pd.read_sql(sql, cn)

