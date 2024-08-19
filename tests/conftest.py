import pytest

from stonfi import APIClient



@pytest.fixture(scope="function")
def stonfi_test_client():
    return APIClient()
