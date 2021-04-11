from requests import get, Response
from shutil import copyfileobj
from .utils import *

class entry_image(object):
    """
    Entry image object.

    Parameters:
        * `entry_data`: The data on the target entry, usually retrieved with `compendium.get_entry`
            - type: dict
        * `_api`: Instance of `utils.api`
            - type: `utils.api`

    Attributes:
        * `_api`: `_api` parameter.
        * `entry_data`: `entry_data` parameter.
        * `url`: The URL of the image.
            - type: str
        * `res`: Response object of request.
            - type: `requests.models.Response`
        * `binary`: Raw binary image.
            - type: str
    """
    def __init__(self, entry_data: dict, _api: api):
        self._api = api
        self.entry_data = entry_data
        self.url: str = _api.endpoint(f"/entry/{entry_data['name']}/image")
        self.res: Response = get(self.url, stream=True)
        self.binary = self.res.text

    def download(self, output_file=None) -> None: 
        """
        Downloads the entry image object.

        Parameters:
            * `output_file`: The file to write the image to.
                type: str
                default: `None`, meaning the entry name with spaces replaced with underscores with a ".png" extension.
        """
        if not output_file:
            entry_name = self.entry_data["name"].replace(' ', '_')
            output_file = f"{entry_name}.png"

        copyfileobj(self.res.raw, open(output_file, "wb"))