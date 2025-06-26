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

t = np.linspace(0, 5, 100023)
xs = [f(t), g(t), h(t)]
      
for x in xs:
    plt.plot(t, x)
plt.show()

compression = 10000

jdata = []
jdata.append({
    "x": list(t),
    "y": list(xs[0]),
    "linestyle": "--",
    "colour": "tab:red",
    "compression": compression,
    "label": "exp"
})

jdata.append({
    "x": list(t),
    "y": list(xs[1]),
    "colour": "tab:blue",
    "compression": compression,
    "label": "exp",
})

jdata.append({
    "x": list(t),
    "y": list(xs[2]),
    "linestyle": "x",
    "colour": "tab:green",
    "label": "sin",
    "compression": compression,
})

jstring = json.dumps({ 
    "data": jdata, 
    "xl": "time", 
    "yl": "amplitude", 
    "path": "exp-decay.pdf",
    "inline": True,
    "legend": "upper left",
    "ylim": [0, 1.5],
}, indent=4)

print(jstring)
