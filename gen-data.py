#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys
import random 
import json

def f(x):
    return np.exp(- (x))

t = np.linspace(0, 5, 1000)
xs = [[f(x) + random.uniform(-n, n) for x in t] for n in [.1, .05, .02]]
      
for x in xs:
    plt.plot(t, x)
plt.show()

jdata = []
jdata.append({
    "x": list(t),
    "y": list(xs[0]),
    "dashed": True,
    "colour": "tab:orange",
    "label": "0.1"
})

jdata.append({
    "x": list(t),
    "y": list(xs[1]),
    "colour": "tab:blue",
    "label": "0.05",
})

jdata.append({
    "x": list(t),
    "y": list(xs[2]),
    "dashed": False,
    "colour": "tab:green",
    "label": "0.01"
})

jstring = json.dumps({ 
    "data": jdata, 
    "xl": "time", 
    "yl": "amplitude", 
    "path": "exp-decay.pdf",
    "inline": True,
}, indent=4)

print(jstring)
