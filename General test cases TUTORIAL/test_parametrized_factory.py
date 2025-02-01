# pytest -v test_parametrized_factory.py
# How Does @pytest.mark.parametrize Work with user_factory?

import pytest

@pytest.fixture
def user_factory():
    def create_user(name, age, email=None):
        return {"name": name, "age": age, "email": email}
    return create_user

def test_user_email(user_factory):
    user = user_factory("Alice", 30, "alice@example.com")
    assert user["email"] == "alice@example.com"




# Supports Parameterization & Scalability
# Using user_factory, we can easily integrate pytest parametrize to test different scenarios.

@pytest.mark.parametrize("name, age", [("Alice", 30), ("Bob", 25), ("Charlie", 40)])
# Pytest automatically injects each combination of name and age into the test.

def test_users(user_factory, name, age):
    user = user_factory(name, age)
    assert user["name"] == name
    assert user["age"] == age

"""
Step-by-Step Explanation
    1️⃣ @pytest.mark.parametrize("name, age", [...])
        This tells pytest to run test_users multiple times with different values of name and age.
        It will pass each tuple as arguments to the test function.

    2️⃣ user_factory is a fixture
        Pytest automatically provides the fixture when calling the test.
        This means user_factory is available inside test_users, allowing dynamic object creation.

    3️⃣ Pytest runs the test three times with different inputs
        First run: name="Alice", age=30
        Second run: name="Bob", age=25
        Third run: name="Charlie", age=40

"""