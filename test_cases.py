# test_http_wrapper.py
import pytest
import requests
from unittest.mock import patch
from RestAPI import HttpWrapper

@pytest.fixture
def http_wrapper():
    return HttpWrapper(base_url="https://httpbin.org")

def test_get_success(http_wrapper):
    with patch("requests.get") as mocked_get:
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.json.return_value = {"key": "value"}

        response = http_wrapper.get("/get")
        assert response.status_code == 200
        assert response.json() == {"key": "value"}
        mocked_get.assert_called_once_with("https://httpbin.org/get", params=None, headers=None)

def test_post_success(http_wrapper):
    with patch("requests.post") as mocked_post:
        mocked_post.return_value.status_code = 201
        mocked_post.return_value.json.return_value = {"key": "value"}

        response = http_wrapper.post("/post", json={"data": "value"})
        assert response.status_code == 201
        assert response.json() == {"key": "value"}
        mocked_post.assert_called_once_with("https://httpbin.org/post", data=None, json={"data": "value"}, headers=None)

def test_get_with_delay(http_wrapper):
    delay_time = 3
    with patch("requests.get") as mocked_get:
        mocked_get.return_value.status_code = 200
        mocked_get.return_value.json.return_value = {"delayed": True}

        response = http_wrapper.get(f"/delay/{delay_time}")
        assert response.status_code == 200
        assert response.json() == {"delayed": True}
        mocked_get.assert_called_once_with(f"https://httpbin.org/delay/{delay_time}", params=None, headers=None)

def test_get_failure(http_wrapper):
    with patch("requests.get") as mocked_get:
        mocked_get.side_effect = requests.exceptions.RequestException("Error")

        response = http_wrapper.get("/endpoint")
        print(response)
        assert response is None
        mocked_get.assert_called_once_with("https://httpbin.org/endpoint", params=None, headers=None)

def test_unauthorized_access(http_wrapper):
    with patch("requests.get") as mocked_get:
        mocked_get.return_value.status_code = 401
        mocked_get.return_value.json.return_value = {"error": "Unauthorized"}

        response = http_wrapper.get("/protected-endpoint")
        assert response.status_code == 401
        assert response.json() == {"error": "Unauthorized"}
        mocked_get.assert_called_once_with("https://httpbin.org/protected-endpoint", params=None, headers=None)

