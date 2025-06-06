#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys
import random 
import json

def f(x):
    return np.exp(-x)

def g(x):
    return 1 - np.exp(-x)

def h(x):
    return np.sin(x)

t = np.linspace(0, 5, 10)
xs = [f(t), g(t), h(t)]
      
for x in xs:
    plt.plot(t, x)
plt.show()

jdata = []
jdata.append({
    "x": list(t),
    "y": list(xs[0]),
    "dashed": True,
    "colour": "tab:red",
    "label": "exp"
})

jdata.append({
    "x": list(t),
    "y": list(xs[1]),
    "colour": "tab:blue",
    "label": "exp",
})

jdata.append({
    "x": list(t),
    "y": list(xs[2]),
    "dashed": False,
    "colour": "tab:green",
    "label": "sin"
})

jstring = json.dumps({ 
    "data": jdata, 
    "xl": "time", 
    "yl": "amplitude", 
    "path": "exp-decay.pdf",
    "inline": True,
    "ylim": [0, 1.5],
}, indent=4)

print(jstring)
