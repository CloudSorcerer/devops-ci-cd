import pytest

@pytest.fixture(scope="session")
def sample_data():
    return {"hello": "world"}
