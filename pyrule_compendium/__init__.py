from http.client import HTTPMessage
from urllib.request import urlretrieve
from typing import Union, Tuple
from . import exceptions
from .utils import *

class compendium(object):
    """
    Base class for pyrule compendium.

    Parameters:
        * `url`: The base URL for the API.
            - default: "https://botw-compendium.herokuapp.com/api/v2"
            - type: string
        * `default_timeout`: Default seconds to wait for response for all API calling functions until raising `requests.exceptions.ReadTimeout`
            - default: `None` (meaning no timeout)
            - type: integer, float, tuple (for connect and read timeouts)
            - notes: If a API calling function has a parameter `timeout`, it will overide this
    """

    def __init__(self, url: str="https://botw-compendium.herokuapp.com/api/v2", default_timeout: Union[int, float, None]=None):
        self.url = url
        self.default_timeout = default_timeout

    def get_entry(self, entry: Union[str, int], timeout: Union[float, int, None]=None) -> dict:
        """
        Gets an entry from the compendium.

        Parameters:
            * `entry`: The entry to be retrieved.
                - type: string, int
            * `timeout`: Seconds to wait for response until raising `requests.exceptions.ReadTimeout`
                - default: `self.default_timeout`
                - type: integer, float, tuple (for connect and read timeouts)

        Returns: Metadata on the entry
            - type: dict
        """

        if not timeout:
            timeout = self.default_timeout

        res: dict = api_req(f"{self.url}/entry/{entry}", timeout=timeout)
        if res == {}:
            raise exceptions.NoEntryError(entry)

        return res

    def get_category(self, category: str, timeout: Union[float, int, None]=None) -> Union[dict, list]:
        """
        Gets all entries from a category in the compendium.

        Parameters:
            * `category`: The name of the category to be retrieved. Must be one of the compendium categories.
                - type: string
                - notes: must be in ["creatures", "equipment", "materials", "monsters", "treasure"]
            * `timeout`: Seconds to wait for response until raising `requests.exceptions.ReadTimeout`
                - default: `self.default_timeout`
                - type: integer, float, tuple (for connect and read timeouts)

        Returns: All entries in the category. 
            - type: list, dict (for creatures)
            - notes: the response schema of `creatures` is different from the others, as it has two sub categories: food and non_food
        """

        if not timeout:
            timeout = self.default_timeout

        if category not in ["creatures", "equipment", "materials", "monsters", "treasure"]:
            raise exceptions.NoCategoryError(category)

        return api_req(f"{self.url}/category/{category}", timeout=timeout)

    def get_all(self, timeout: Union[float, int, None]=None) -> dict:
        """
        Get all entries from the compendium.

        Parameters:
            * `timeout`: Seconds to wait for response until raising `requests.exceptions.ReadTimeout`
                - default: `self.default_timeout`
                - type: integer, float, tuple (for connect and read timeouts)

        Returns: all items in the compendium with their metadata nested in categories.
            - type: dict
        """

        if not timeout:
            timeout = self.default_timeout

        return api_req(self.url, timeout=timeout)

    def download_entry_image(self, entry: Union[int, str], output_file: Union[str, None]=None, get_entry_timeout: Union[int, float, None]=None) -> Tuple[str, HTTPMessage]:
        """
        Download the image of a compendium entry.

        Parameters:
            * `entry`: The ID or name of the entry of the image to be downloaded.
                - type: str, int
            * `output_file`: The output file's path.
                - default: entry's name with a ".png" extension with spaces replaced by underscores
                - type: str
            * `get_entry_timeout`: Seconds to wait for response until raising `requests.exceptions.ReadTimeout`.
                - default: `self.default_timeout`
                - type: int, float, tuple (for connect and read timeouts)

        Returns: path to the newly created image and the resulting HTTPMessage object.
            - type: tuple
        """

        if not get_entry_timeout:
            get_entry_timeout = self.default_timeout

        entry_data: dict = self.get_entry(entry, timeout=get_entry_timeout)

        if not output_file:
            output_file = f"{entry_data['name'].replace(' ', '_')}.png"

        return urlretrieve(entry_data["image"], output_file)