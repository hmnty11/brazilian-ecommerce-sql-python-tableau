import os
import pytest
import pandas as pd
from sqlalchemy import create_engine, text

@pytest.fixture
def db_engine():
    # Mengambil URL database MySQL dari pipeline environment
    database_url = os.getenv("DATABASE_URL", "mysql+pymysql://root:root_password@127.0.0.1:3306/olist_test")
    return create_engine(database_url)

def test_mysql_connection(db_engine):
    # Menguji apakah koneksi ke server MySQL di GitHub Actions berhasil berjalan
    with db_engine.connect() as conn:
        result = conn.execute("SELECT 1")
        assert result.fetchone()[0] == 1