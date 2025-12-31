import os
import importlib
import pytest

# Skip entirely when instructed (e.g., on CI without Databricks auth/runtime).
if os.environ.get("SKIP_DATABRICKS_TESTS") == "1":
    pytest.skip("Skipping Databricks-dependent tests", allow_module_level=True)

# Best-effort check that the Databricks runtime is actually available.
try:
    importlib.import_module("databricks.sdk.runtime")
except Exception:
    pytest.skip("Databricks runtime not available", allow_module_level=True)

from databricks.sdk.runtime import spark
from pyspark.sql import DataFrame
from test_jobs import taxis


def test_find_all_taxis():
    results = taxis.find_all_taxis()
    assert results.count() > 5
