from http.client import HTTPMessage
from requests import get
from urllib.request import urlretrieve
from typing import Union, Tuple

class NoCategoryError(Exception):
    """
    Raised when a given category does not exist in the compendium

    Parameters:
        * `target_category`: Non-existant input category that causes error.
            - type: string
    """

    def __init__(self, target_category: str):
        self.target_category = target_category
        super().__init__(f"Category '{self.target_category}' not found. Must be 'creatures', 'equipment', 'materials', 'monsters', or 'treasure'")

class NoEntryError(Exception):
    """
    Raised when a given entry does not exist in the compendium

    Parameters:
        * `target_entry`: Non-existant input entry that causes error.
            - type: string, int
    """

    def __init__(self, target_entry: Union[str, int]):
        self.target_entry = target_entry

        self.message: str
        if isinstance(self.target_entry, int):
            self.message = f"Entry with ID {self.target_entry} not found."
        elif isinstance(self.target_entry, str):
            self.message = f"Entry with name '{self.target_entry}' not found"
        else:
            self.message = f"Type '{type(self.target_entry).__name__}' invalid for entry indexing"
        
        super().__init__(self.message)

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

        res: dict = get(f"{self.url}/entry/{entry}", timeout=timeout).json()["data"]
        if res == {}:
            raise NoEntryError(entry)

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
            raise NoCategoryError(category)

        return get(f"{self.url}/category/{category}", timeout=timeout).json()["data"]

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

        return(get(self.url, timeout=timeout).json()["data"])

    def download_entry_image(self, entry: Union[int, str], output_file: str, get_entry_timeout: Union[int, float, None]=None) -> Tuple[str, HTTPMessage]:
        """
        Download the image of a compendium entry.

        Parameters:
            * `entry`: The ID or name of the entry of the image to be downloaded.
                - type: str, int
            * `output_file`: The output file's path.
                - type: str
            * `get_entry_timeout`: Seconds to wait for response until raising `requests.exceptions.ReadTimeout`.
                - default: `self.default_timeout`
                - type: integer, float, tuple (for connect and read timeouts)

        Returns: path to the newly created image and the resulting HTTPMessage object.
            - type: tuple
        """

        if not get_entry_timeout:
            get_entry_timeout = self.default_timeout

        img_link: str = self.get_entry(entry, timeout=get_entry_timeout)["image"]
        return(urlretrieve(img_link, output_file))