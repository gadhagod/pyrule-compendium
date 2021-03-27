# pyrule compendium
The official python API wrapper for the Hyrule Compendium API.

## Installation

    pip3 install pyrule-compendium

## Usage
Read code comments for detailed documentation.

    from pyrule_compendium import compendium

    print(compendium().get_all()) # get all entries
    print(compendium().get_entry("silver_lynel")) # get a specific entry with it's name
    print(compendium().get_entry(1)) # get a specific entry with it's ID
    print(compendium().get_category("monsters")) # get all entries in a category
    compendium().download_entry_image("silver_lynel", "silver_lynel.png") # download entry image

## Notes
* If a key's value is `None`, it means that the key is marked as "unknown" in the compendium.
* The response schema of `creatures` is different from the others, as it has two sub categories: food and non_food
