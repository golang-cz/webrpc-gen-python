import pytest
from client import TestApi

# Initialize the API client
test_api_client = TestApi("http://localhost:8000")

# Test scenario for testing server interoperability
def test_interoperability():
    # Test successful retrieval of an empty type
    assert test_api_client.GetEmpty() == {}

    # Test error handling
    with pytest.raises(Exception):
        test_api_client.GetError()

    # Test retrieval of a simple type and successful sending back
    complex_data = test_api_client.GetOne()
    assert test_api_client.SendOne(complex_data, {}) == {}

    # Test retrieval of multiple simple types and successful sending back
    multi_data = test_api_client.GetMulti()
    assert test_api_client.SendMulti(multi_data, {}) == {}

    # Test retrieval of a complex type and successful sending back
    complex_data = test_api_client.GetComplex()
    assert test_api_client.SendComplex(complex_data, {}) == {}

if __name__ == "__main__":
    pytest.main()
