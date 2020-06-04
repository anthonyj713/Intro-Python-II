# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

class Inventory(Item):
    def __init__(self, name, description):
        super().__init__(name, description)
    def __str__(self):
        return f'{self.name} -- {self.description}'