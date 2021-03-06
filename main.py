#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
#
# Fleury's Algorithm implementation
# Dawid Kulig
# dawid.kulig[at]uj.edu.pl
# 0.1

from Fleury import *
from tests import *


# Uruchomienie unit-testow
# runTests()

#G = {0: [2, 2, 3], 1: [2, 2, 3], 2: [0, 0, 1, 1, 3], 3: [0, 1, 2]}

#G = {0: [1, 4, 6, 8], 1: [0, 2, 3, 8], 2: [1, 3], 3: [1, 2, 4, 5], 4: [0, 3], 5: [3, 6], 6: [0, 5, 7, 8], 7: [6, 8], 8: [0, 1, 6, 7]}

#G = {1: [2, 3, 4, 4], 2: [1, 3, 3, 4], 3: [1, 2, 2, 4], 4: [1, 1, 2, 3]}

#G = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}

G = {0: [4, 5], 1: [2, 3, 4, 5], 2: [1, 3, 4, 5], 3: [1, 2], 4: [0, 1, 2, 5], 5: [0, 1, 2, 4]}

test = Fleury(G)
test.run()
