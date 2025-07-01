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

# Utility functions 
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs) 


def do_if_present(dic, key, f):
    if key in dic: 
        return f(dic[key])

    return None




def compress(data, compression):
    comp_level = int(compression["level"])
    comp_type  = compression["type"]
    new_data = np.zeros(int(np.ceil(len(data) / comp_level)))
    
    for i, _ in enumerate(new_data):
        if comp_type == "discard": 
            new_data[i] = data[i * comp_level]
        elif comp_type == "mean":
            end = min(len(data), i*comp_level + comp_level)
            chunk = data[i*comp_level:end]
            new_data[i] = np.mean(chunk)
        else: 
            raise ValueError(f"Unrecognised compression type: {comp_type}")

    return new_data


def plot_line(d, ax, parent):
    do_legend = False 

    linestyle = d["linestyle"] if "linestyle" in d else "-"
    colour = d["colour"] if "colour" in d else None
    label  = d["label"]  if "label"  in d else None
   
    compression = None
    if "compression" in parent: compression = parent["compression"]
    if "compression" in d:      compression = d["compression"]      # Overloads parent compression settings

    if label: do_legend = True

    x_data = d["x"]; y_data = d["y"]
    
    if compression:  
        x_data = compress(x_data, compression); y_data = compress(y_data, compression)

    eprint(f"Plotting {label}...")
    ax.plot(x_data, y_data, linestyle, color=colour, label=label, markersize=2)

    return do_legend


def set_ticks(ax, ticks):
    ax.set_ticks(ticks["minor"], minor=True)
    ax.set_ticks(ticks["major"], minor=False)


def do_plot(jobject):

    dimensions = [8, 4.5]
    if "size" in jobject: dimensions = jobject["size"]
    if "aspect" in jobject: dimensions[0] = dimensions[1] * jobject["aspect"]

    fig, ax = plt.subplots(figsize=dimensions)

    do_legend = False
    for d in jobject["data"]: 
        if plot_line(d, ax, jobject): do_legend = True

    eprint("Setting options...")
    # Mandatory
    plt.xlabel(jobject["xl"])
    plt.ylabel(jobject["yl"])

    # Optional
    do_if_present(jobject, "title", lambda t: plt.title(t))
    do_if_present(jobject, "logx",  lambda l: ax.set_xscale("log", base=l))
    do_if_present(jobject, "logy",  lambda l: ax.set_yscale("log", base=l))
    do_if_present(jobject, "tickx", lambda t: set_ticks(ax.xaxis, t))
    do_if_present(jobject, "ticky", lambda t: set_ticks(ax.yaxis, t))
    do_if_present(jobject, "xlim",  lambda l: ax.set_xlim(l)) 
    do_if_present(jobject, "ylim",  lambda l: ax.set_ylim(l)) 
    do_if_present(jobject, "legend", lambda l: plt.legend(loc=l))
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
