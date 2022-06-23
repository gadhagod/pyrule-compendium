# pyrule compendium
The official python API wrapper for the Hyrule Compendium API.

## Installation

    pip3 install pyrule-compendium

## Documentation
Detailed documentation can be found [here](https://gadhagod.github.io/pyrule-compendium).

## Basic Usage
```python
from pyrule_compendium import compendium

comp = compendium()
print(comp.get_all()) # get all entries
print(comp.get_entry("silver_lynel")) # get a specific entry with it's name
print(comp.get_entry(1)) # get a specific entry with it's ID
print(comp).get_category("monsters")) # get all entries in a category
comp.get_image("silver_lynel").download() # download entry image
```

Made with :heart: by [Aarav Borthakur](https://github.com/gadhagod) and [Shaunik Musukula](https://github.com/shaunikm).
