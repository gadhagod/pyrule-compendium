from requests import get, Response
from .utils import *

class entry_image(object):
    """
    Entry image object.

    Parameters:
        * `entry_data`: The data on the target entry, usually retrieved with `compendium.get_entry`
            - type: dict
        * `_api`: Instance of `utils.api`
            - type: `utils.api`
    """
    def __init__(self, entry_data: dict, _api: api):
        self._api = api
        self.entry_data = entry_data
        self.url: str = _api.endpoint(f"/entry/{entry_data['name']}/image")
        self.res: Response = get(self.url)
        self.binary = self.res.text

        self.res.raw.decode_content = True

    def download(self, output_file: str=None) -> None: 
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

        open(output_file, "wb").write(self.res.content)

    def get_binary(self) -> str: return self.binary
    def get_url(self) -> str: return self.url