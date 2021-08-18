# pyrule compendium
The official python API wrapper for the Hyrule Compendium API.

## Installation

    pip3 install pyrule-compendium

## Documentation
Detailed documentation can be found [here](https://gadhagod.github.io/pyrule-compendium).

## Basic Usage
    from pyrule_compendium import compendium

    print(compendium().get_all()) # get all entries
    print(compendium().get_entry("silver_lynel")) # get a specific entry with it's name
    print(compendium().get_entry(1)) # get a specific entry with it's ID
    print(compendium().get_category("monsters")) # get all entries in a category
    compendium().get_image("silver_lynel").download() # download entry image
