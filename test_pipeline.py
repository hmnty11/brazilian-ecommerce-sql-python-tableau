import os
import pytest
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

@pytest.fixture
def db_engine():
    # Mengambil URL database MySQL dari pipeline environment
    database_url = os.getenv("DATABASE_URL", "mysql+pymysql://root:root_password@127.0.0.1:3306/olist_test")
    return create_engine(database_url)

def test_mysql_connection(db_engine):
    # Menguji apakah koneksi ke server MySQL di GitHub Actions berhasil berjalan
    try:
        with db_engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            assert result.fetchone()[0] == 1
    except OperationalError:
        pytest.skip("No local MySQL database available for testing")

def test_invalid_database_url(monkeypatch):
    # Menguji apakah koneksi ke server MySQL dengan URL yang salah gagal dengan OperationalError
    monkeypatch.setenv("DATABASE_URL", "mysql+pymysql://invalid_user:invalid_password@127.0.0.1:3306/invalid_db")

    database_url = os.getenv("DATABASE_URL")
    engine = create_engine(database_url)

    with pytest.raises(OperationalError):
        with engine.connect() as conn:
            pass