from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

def move(player, direction):
    attribute = direction + '_to'
    
    if hasattr(player.current_room, attribute):
        player.current_room = getattr(player.current_room, attribute)
    else:
        print('There is nothing that direction')

# def action(player, action):
#     attribute = action

#     if hasattr(player.)

# Make a new player object that is currently in the 'outside' room.

# player = Player(room['outside'])

# Write a loop that:

name = input('What is your name, adventurer?\n')
player = Player(name, room['outside'])
print(f'Welcome {player.name}.\n')


while True: 
    # * Prints the current room name
    print(player.current_room)

# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
    command = input("\nCommand: ").strip().lower().split()
    command = command[0]
    print(command)
# If the user enters "q", quit the game.
    if command == 'q':
        break
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#

    if command == 'n':
        move(player, command)
    elif command == 's':
        move(player, command)
    elif command == 'e':
        move(player, command)
    elif command == 'w':
        move(player, command)


    # if command == 'a':
    #     action(player, command)

