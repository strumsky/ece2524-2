#!/usr/bin/env python

# Chris Moore

import movementCheck
import re
import fileinput

from sys import stdin, stdout, stderr, argv, exit

(acceptable) = movementCheck.movementCheck(argv)

print acceptable
