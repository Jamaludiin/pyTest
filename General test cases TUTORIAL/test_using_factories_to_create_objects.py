# Using a factory function to generate test data dynamically.

# pytest -v test_using_factories_to_create_objects.py

import pytest

@pytest.fixture
def user_factory():
    def create_user(name, age):
        return {"name": name, "age": age}
    return create_user

def test_user(user_factory):
    user = user_factory("Alice", 30)
    assert user["name"] == "Alice"
    assert user["age"] == 30

def test_another_user(user_factory):
    user2 = user_factory("Jamal", 29)
    assert user2["name"] == "Jamal"
    assert user2["age"] == 29


