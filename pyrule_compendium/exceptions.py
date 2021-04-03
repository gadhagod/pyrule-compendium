from typing import Union

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