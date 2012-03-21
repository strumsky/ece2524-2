#!/usr/bin/env python
# Chris Moore
# movementCheck
#
# take in the player's position, and desired direction and return a boolean telling if the player can move in the desired direction
#
# Input: (int) xposition, (int) yposition, (string) direction [up, right, down, left]
# Output: (boolean) movementPossible
#

import re
import fileinput
from sys import stdin, stdout, stderr, exit, argv

def movementCheck(args):
    if len(args) != 4:
        stderr.write("\n\033[1;31mError\033[0m: bad arguments passed in.\n")
        exit(1)

    currentXPosition = int(args[2])
    currentYPosition = int(args[1])
    desiredDirection = args[3]
    desiredPosition = 2*[1] # desiredPosition[xpos, ypos]

    for line in fileinput.input('map'): # for each line in the input file...
        if fileinput.isfirstline(): #get the size of the map
            xwidth = line[:line.find('x')] # grab the first part up to the x
            ywidth = line[line.find('x') + 1:] # grab the part after the x
            xwidth = int(xwidth) # convert the xwidth to an integer
            ywidth = int(ywidth) # convert the ywidth to an integer
            stderr.write("%d x %d\n" % (xwidth, ywidth))
            stderr.write("\t0123456789abcdef\n")
            currentMap = (xwidth)*[ywidth]
        else:
            if fileinput.lineno() > 1:
                currentMap[fileinput.lineno()-2] = list(line)

    for x in range(int(xwidth)):
        stderr.write("%d\t" %(x))
        for y in range(ywidth):
            #stderr.write("%s" %(currentMap[x][y]))
            if x == currentXPosition and y == currentYPosition:
                stderr.write("\033[1;31m%s\033[0m"%(currentMap[x][y]))
            elif currentMap[x][y] =='W':
                stderr.write("\033[1;34m%s\033[0m"%(currentMap[x][y]))
            elif currentMap[x][y] =='B': # check for bridges
                stderr.write("\033[1;43m%s\033[0m"%(currentMap[x][y]))
            else:
                stderr.write("\033[1;32m%s\033[0m"%(currentMap[x][y]))
        stderr.write("\n")
    #ignore variable names, they are backwards
    if desiredDirection == "left" and currentXPosition > 0:
        desiredPosition[0] = currentXPosition
        desiredPosition[1] = currentYPosition - 1
    elif desiredDirection == "right" and currentXPosition < xwidth:
        desiredPosition[0] = currentXPosition
        desiredPosition[1] = currentYPosition + 1
    elif desiredDirection == "up" and currentYPosition > 0:
        desiredPosition[0] = currentXPosition - 1
        desiredPosition[1] = currentYPosition
    elif desiredDirection == "down" and currentYPosition < ywidth:
        desiredPosition[0] = currentXPosition + 1
        desiredPosition[1] = currentYPosition

    stderr.write("\nDesired positoin: %d,%d is: %s\n" %(desiredPosition[0], desiredPosition[1], currentMap[desiredPosition[0]][desiredPosition[1]]))

    if currentMap[desiredPosition[0]][desiredPosition[1]] == "E" or currentMap[desiredPosition[0]][desiredPosition[1]] == "B":
        acceptable = True
    else:
        acceptable = False
    return(acceptable)


if __name__ == '__main__':
    from sys import stdin, argv, stdout, stderr, exit
    
    (acceptable) = movementCheck(argv)
    print acceptable
