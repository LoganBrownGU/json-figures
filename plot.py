#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import json
import matplotlib

from pathlib import Path 
from matplotlib import font_manager as fm
from labellines import labelLine, labelLines

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs) 

def do_plot(jobject):

    #plt.rcParams["font"] = Path("times.ttf")
    fig, ax = plt.subplots(figsize=(5,3))

    do_legend = False
    for d in jobject["data"]: 
        linestyle = d["linestyle"] if "linestyle" in d else "-"
        colour = d["colour"] if "colour" in d else None
        label  = d["label"]  if "label"  in d else None
        
        if label: do_legend = True

        eprint(f"Plotting {label}...")
        ax.plot(d["x"], d["y"], linestyle, color=colour, label=label, markersize=2)

    eprint("Setting options...")
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

    eprint("Saving...")
    if "path" in jobject: plt.savefig(jobject["path"], bbox_inches="tight", pad_inches=0)
    else                : plt.show()




font_path = "/usr/share/fonts/truetype/times.ttf"
fm.fontManager.addfont(font_path)
prop = fm.FontProperties(fname=font_path)
matplotlib.rc('font', family='sans-serif') 
matplotlib.rcParams.update({
    'font.size': 16,
    'font.sans-serif': prop.get_name(),
})


for path in sys.argv[1:]: 
    contents = ""
    
    eprint(f"Opening {path}...")
    try:
        with open(path) as f:
            contents = "".join(f.readlines())
    except: eprint(f"Could not open `{path}', skipping."); continue

    jobject = None
    try: jobject = json.loads(contents)
    except: eprint(f"Error parsing `{path}', skipping."); continue
 
    do_plot(jobject) 
