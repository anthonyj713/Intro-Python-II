# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}. {self.description}"

class List(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
    def __str__(self):
        return f'{self.name} -- {self.description}'