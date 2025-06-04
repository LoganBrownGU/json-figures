#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys
import json

contents = ""
with open(sys.argv[1]) as f:
    for line in f.readlines(): contents += line
jobject = json.loads(contents)

fig, ax = plt.subplots()

for d in jobject["data"]: 
    dashed = "dashed" in d and d["dashed"]
    colour = d["colour"] if "colour" in d else None
    label  = d["label"]  if "label"  in d else None

    ax.plot(d["x"], d["y"], "--" if dashed else "-", color=colour, label=label)

# Mandatory
plt.title(jobject["title"])
plt.xlabel(jobject["xl"])
plt.ylabel(jobject["yl"])

# Optional
if "logx" in jobject: ax.set_xscale('log', base=jobject["logx"]) 
if "logy" in jobject: ax.set_yscale('log', base=jobject["logy"]) 

plt.legend(loc="upper right") 
plt.grid(which="both")

if "path" in jobject: plt.savefig(jobject["path"])
else                : plt.show()
