#!/usr/bin/env python3

import numpy as np 
import json 
import sys

x = np.linspace(0, 8, 10000)
y = 10 ** x + 40 * x**3

maj_ticks = []
min_ticks = []
for order in range(1, 9):
    val = 10**(order-1)
    maj_ticks.append(val) 

    while val < 10**order:
        val += 10**(order-1) 
        print(val, file=sys.stderr) 
        min_ticks.append(val)

print(json.dumps({
    "data": [ {"x": list(x), "y": list(y) } ],
    "xl": "x",
    "yl": "y",
    "logy": 10,
    "ticky": { "minor": list(min_ticks), "major": list(maj_ticks) },
    "path": "log.pdf",
}, indent=4))
