from typing import Union, Any
from requests import get

class types:
    entry = Union[int, str]
    timeout = Union[int, float, None]

def api_req(url: str, timeout: types.timeout=None) -> Union[list, dict]: return get(url, timeout=timeout).json()["data"]

class api():
    def __init__(self, base_url: str): self.base_url = base_url
    def endpoint(self, target_endpoint: str) -> str: return f"{self.base_url}{target_endpoint}"
    def request(self, endpoint: str, timeout: types.timeout=None) -> Any: return api_req(f"{self.endpoint(endpoint)}", timeout)