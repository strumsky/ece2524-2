movementCheck.py checks to see if a desired movement will be allowed
on a given map from the player's current position. The map is defined
in a file called 'map' and is in the same directory as the program.

Usage: ./movementCheck [xpos] [ypos] [direction]

xpos is the player's current x-coordinate

ypos is the player's current y-coordinate

direction can be 'left' 'right' 'up' 'down' and is the direction the
    player wants to go.

The stand alone function simply prints the map to the screen and also
displays if the player can move in the desired direction. All movement
is considered to be one board unit at a time.

map file
--------

The map file right now only consists of 3 elements

E - earth space
W - water space
B - bridge space

The player can pass over earth and bridge spaces, but a water space
cannot be occupied by the player.

Map format:
Line1: #x#      this is the dimensions of the map
TTTTTTT
TTTTTTT
TTTTTTT         these are the T(tiles) on the map
