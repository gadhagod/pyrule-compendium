from http.client import HTTPMessage
from typing import Union
from . import objects
from . import exceptions
from .utils import *

class compendium(object):
    """
    Base class for pyrule compendium.

    Parameters:
        * `base_url`: The base URL for the API.
            - default: "https://botw-compendium.herokuapp.com/api/v2"
            - type: string
            - notes: Manipulate with `compendium.api.base_url`
        * `default_timeout`: Default seconds to wait for response for all API calling functions until raising `requests.exceptions.ReadTimeout`
            - default: `None` (no timeout)
            - type: integer, float, tuple (for connect and read timeouts)
            - notes: If an API calling function has a parameter `timeout`, it will overide this
    """

    def __init__(self, base_url: str="https://botw-compendium.herokuapp.com/api/v2", default_timeout: Union[int, float, None]=None):
        self.api: api = api(base_url)
        self.default_timeout = default_timeout

    def get_entry(self, entry: types.entry, timeout: types.timeout=None) -> dict:
        """
        Gets an entry from the compendium.

        Parameters:
            * `entry`: The entry to be retrieved.
                - type: str, int
            * `timeout`: Seconds to wait for response until raising `requests.exceptions.ReadTimeout`
                - default: `compendium.default_timeout`
                - type: int, float, tuple (for connect and read timeouts)

        Returns: Metadata on the entry
            - type: dict
        """

        if not timeout:
            timeout = self.default_timeout

        res: dict = self.api.request(f"/entry/{entry}", timeout)
        if res == {}:
            raise exceptions.NoEntryError(entry)

        return res

    def get_category(self, category: str, timeout: types.timeout=None) -> Union[dict, list]:
        """
        Gets all entries from a category in the compendium.

        Parameters:
            * `category`: The name of the category to be retrieved. Must be one of the compendium categories.
                - type: string
                - notes: must be in ["creatures", "equipment", "materials", "monsters", "treasure"]
            * `timeout`: Seconds to wait for response until raising `requests.exceptions.ReadTimeout`
                - default: `compendium.default_timeout`
                - type: integer, float, tuple (for connect and read timeouts)

        Returns: All entries in the category. 
            - type: list, dict (for creatures)
            - notes: the response schema of `creatures` is different from the others, as it has two sub categories: food and non_food
        """

        if not timeout:
            timeout = self.default_timeout

        if category not in ["creatures", "equipment", "materials", "monsters", "treasure"]:
            raise exceptions.NoCategoryError(category)

        return self.api.request(f"/category/{category}", timeout)

    def get_all(self, timeout: types.timeout=None) -> Union[dict, list]:
        """
        Get all entries from the compendium.

        Parameters:
            * `timeout`: Seconds to wait for response until raising `requests.exceptions.ReadTimeout`
                - default: `compendium.default_timeout`
                - type: integer, float, tuple (for connect and read timeouts)

        Returns: all items in the compendium with their metadata nested in categories.
            - type: dict
        """

        if not timeout:
            timeout = self.default_timeout

        return api_req(self.api.base_url, timeout)

    def get_image(self, entry: types.entry) -> objects.entry_image:
        """
        Retrieves the image of a compendium entry.

        Parameters:
            * `entry`: The ID or name of the entry.
                - type: str, int

        Returns: Entry image object
            - type: `objects.entry_image`
        """

        return objects.entry_image(self.get_entry(entry), self.api)