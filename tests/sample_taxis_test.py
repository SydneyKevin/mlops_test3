import pytest

# Skip this test when not running inside a Databricks runtime (e.g., local GitHub Actions runner).
pytest.importorskip("databricks.sdk.runtime", reason="Requires Databricks runtime")

from databricks.sdk.runtime import spark
from pyspark.sql import DataFrame
from test_jobs import taxis


def test_find_all_taxis():
    results = taxis.find_all_taxis()
    assert results.count() > 5
