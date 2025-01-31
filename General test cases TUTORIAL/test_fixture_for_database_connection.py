#Fixture for Database Connection (Setup and Teardown)
# Using yield to clean up after the test.

# pytest test_fixture_for_database_connection.py
# pytest -v test_fixture_for_database_connection.py
# 

import pytest

@pytest.fixture
def db_connection():
    connection = "Database Connected"  # Simulate connection
    yield connection  # Provide the fixture value
    connection = "Database Disconnected"  # Cleanup after test

def test_db_connection(db_connection):
    assert db_connection == "Database Connected"


# TDOD: stablish real db connection using sql and test the resposne of real queries later on