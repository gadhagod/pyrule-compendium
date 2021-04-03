from requests import get

api_req = lambda url, timeout: get(url, timeout=timeout).json()["data"]