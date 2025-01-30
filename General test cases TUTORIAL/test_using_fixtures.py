# Fixtures are reusable pieces of setup code for tests. For example, if all your tests need a database connection or a sample object, you can use a fixture.

import pytest

# The @pytest.fixture decorator marks the function as a fixture.
@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 30}

# Fixtures are passed as arguments to test functions.
def test_sample_data(sample_data): 
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30
