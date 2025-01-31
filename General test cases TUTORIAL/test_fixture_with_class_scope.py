
# Sharing a fixture across multiple tests within a class.
# pytest -v test_fixture_with_class_scope.py

import pytest

@pytest.fixture(scope="class")
def setup_class():
    return {"status": "setup started", "status2": "setup completed"}

class TestExample:
    def test_one(self, setup_class):
        assert setup_class["status"] == "setup started"

    def test_two(self, setup_class):
        assert setup_class["status2"] == "setup completed"
