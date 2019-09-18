#!/usr/bin/env python3
################################################################################
# Name:    test_mysum.py and mysum.py
# Purpose: These Python scripts demonstrate how to communicate with another
#          Python script bi-directionally.
# Usage:   ./test_mysum.py mysum.py
# Author:  Huidae Cho
# Since:   September 18, 2019
#
# Copyright (C) 2019, Huidae Cho <https://idea.isnew.info>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
################################################################################

import sys
import subprocess
import os
from random import randint

def mysum(n):
    x = 0
    for i in range(1, n+1):
        x += i
    return x

done = False

p = subprocess.Popen([sys.executable, sys.argv[1]],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE)
while not done:
    for line in os.read(p.stdout.fileno(), 256).decode().split(os.linesep):
        if line == '':
            done = True
            break
        elif line == 'n? ':
            n = randint(1, 100)
            inp = '{n}'.format(n=n) + os.linesep
            p.stdin.write(inp.encode())
            p.stdin.flush()
        else:
            ans = int(line)
            if ans == mysum(n):
                print('Passed')
            else:
                print('Failed')
