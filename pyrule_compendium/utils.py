from typing import Union
from requests import get

def api_req(url: str, timeout: Union[int, float]): return get(url, timeout=timeout).json()["data"]

class types:
    entry = Union[int, str]
    timeout = Union[int, float, None]

class api():
    def __init__(self, base_url: str): self.base_url=base_url
    def endpoint(self, target_endpoint: str): return f"{self.base_url}{target_endpoint}"
    def request(self, endpoint: str, timeout: Union[int, float]): return api_req(f"{self.endpoint(endpoint)}", timeout)