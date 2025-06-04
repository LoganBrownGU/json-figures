#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys
import random 
import json

def f(x):
    return np.exp(- (x))

t = np.linspace(0, 5, 50)
xs = [[f(x) + random.uniform(-n, n) for x in t] for n in [.02, .05, .1]]
      
for x in xs:
    plt.plot(t, x)
plt.show()

jdata = []
jdata.append({
    "x": list(t),
    "y": list(xs[0]),
    "dashed": True,
    "colour": "tab:orange",
})

jdata.append({
    "x": list(t),
    "y": list(xs[1]),
    "colour": "tab:blue",
})

jdata.append({
    "x": list(t),
    "y": list(xs[2]),
    "dashed": False,
    "colour": "tab:green",
    "label": "line 3"
})

jstring = json.dumps({ 
    "data": jdata, 
    "xl": "time", 
    "yl": "amplitude", 
    "title": "Exp decay", 
    "logy": 2,
    "path": "exp-decay.pdf",
}, indent=4)

print(jstring)
