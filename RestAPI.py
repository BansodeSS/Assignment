# http_wrapper.py
import requests

class HttpWrapper:
    def __init__(self, base_url):
        self.base_url = base_url

    def _full_url(self, endpoint):
        return f"{self.base_url}{endpoint}"

    def get(self, endpoint, params=None, headers=None):
        try:
            response = requests.get(self._full_url(endpoint), params=params, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"GET request failed: {e}")
            return None

    def post(self, endpoint, data=None, json=None, headers=None):
        try:
            response = requests.post(self._full_url(endpoint), data=data, json=json, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"POST request failed: {e}")
            return None

    def put(self, endpoint, data=None, json=None, headers=None):
        try:
            response = requests.put(self._full_url(endpoint), data=data, json=json, headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"PUT request failed: {e}")
            return None

    def delete(self, endpoint, headers=None):
        try:
            response = requests.delete(self._full_url(endpoint), headers=headers)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"DELETE request failed: {e}")
            return None
