from requests import get, Response
from shutil import copyfileobj
from .utils import *

class entry_image(object):
    def __init__(self, entry_data: types.entry, _api: api):
        self._api = api
        self.entry_data = entry_data
        self.url = _api.endpoint(f"/entry/{entry_data['name']}/image")
        self.res: Response = get(self.url, stream=True)
        self.binary = self.res.text

    def download(self, output_file=None) -> None: 
        if not output_file:
            entry_name = self.entry_data["name"].replace(' ', '_')
            output_file = f"{entry_name}.png"

        copyfileobj(self.res.raw, open(output_file, "wb"))