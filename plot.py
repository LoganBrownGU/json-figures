#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys
import json

from labellines import labelLine, labelLines

def do_plot(jobject):
    
    fig, ax = plt.subplots(figsize=(5,3))

    do_legend = False
    for d in jobject["data"]: 
        linestyle = d["linestyle"] if "linestyle" in d else "-"
        colour = d["colour"] if "colour" in d else None
        label  = d["label"]  if "label"  in d else None
        
        if label: do_legend = True

        ax.plot(d["x"], d["y"], linestyle, color=colour, label=label, markersize=2)

    # Mandatory
    plt.xlabel(jobject["xl"])
    plt.ylabel(jobject["yl"])

    # Optional
    if "title" in jobject: plt.title(jobject["title"])
    if "logx" in jobject: ax.set_xscale('log', base=jobject["logx"]) 
    if "logy" in jobject: ax.set_yscale('log', base=jobject["logy"]) 
    if "xlim" in jobject: ax.set_xlim(jobject["xlim"])
    if "ylim" in jobject: ax.set_ylim(jobject["ylim"])
    if "inline" in jobject and jobject["inline"]: labelLines(ax.get_lines(), False)
    elif do_legend                              : plt.legend()

    plt.grid(which="both")

    if "path" in jobject: plt.savefig(jobject["path"], bbox_inches="tight", pad_inches=0)
    else                : plt.show()

for path in sys.argv[1:]: 
    contents = ""
    
    try:
        with open(path) as f:
            for line in f.readlines(): contents += line
    except: print(f"Could not open `{path}', skipping.", file=sys.stderr); continue

    jobject = None
    try: jobject = json.loads(contents)
    except: print(f"Error parsing `{path}', skipping.", file=sys.stderr); continue
 
    do_plot(jobject) 
