#!/usr/bin/env python3 

import numpy as np
import json 

def f(x, y): 
    return np.exp(np.sin(x) + np.sin(y))
def g(x, y): 
    return np.exp(np.sinc(x) + np.sinc(y))



x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

data_f = [[], [], []]
data_g = [[], [], []]

for x_i in x:
    for d in data_f:
        d.append([])
    for d in data_g:
        d.append([])

    for y_i in y:
        data_f[0][-1].append(x_i)
        data_f[1][-1].append(y_i)
        data_f[2][-1].append(f(x_i, y_i))
        data_g[0][-1].append(x_i)
        data_g[1][-1].append(y_i)
        data_g[2][-1].append(g(x_i, y_i))

with open ("data.json", "w") as f:
    f.write(json.dumps({
        "3d": True,
        "data": [ 
            { "x": list(data_f[0]), "y": list(data_f[1]), "z": list(data_f[2]) },
            { "x": list(data_g[0]), "y": list(data_g[1]), "z": list(data_g[2]) },
        ],
        "xlim": [-7, 7],
        "ylim": [-7, 7],
        "zlim": [-3, 3],
        "xl": "x",
        "yl": "y",
        "zl": "$f(x, y)$",
        "logz": 2, 
        "angle": 225,
        "path": "3d.pdf" 
    }, indent=4))
