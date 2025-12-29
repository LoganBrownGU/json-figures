# JSON plotter

A python script (`plot.py`) that parses JSON files containing numerical and formatting data, outputting a consistent figure format. 

Any number of "lines" may be included, of differing lengths and x-axis data. 

## Mandatory fields (top level) 

| field | description | type | notes | 
| ----- | ----------- | ---- | ----- |
| `data` | data to be plotted | `object` | see below | 
| `xl` | x-axis label | `string` | | 
| `yl` | y-axis label | `string` | |

### 3D-specific

| field | description | type | notes | 
| ----- | ----------- | ---- | ----- |
| `zl` | z-axis label | `string` | | 

## Optional fields (top level) 

| field | description | type | notes | 
| ----- | ----------- | ---- | ----- |
| `logx` | base for x-axis log scale | `float` | will only use x log scale if set |
| `slogx` | base for _symmetrical_ x-axis log scale | `float` | only works for 2D plots |
| `logy` | base for y-axis log scale | `float` | will only use y log scale if set | 
| `slogy` | base for _symmetrical_ y-axis log scale | `float` | only works for 2D plots | 
| `tickx` | x axis ticks | `object` | see below | 
| `ticky` | y axis ticks | `object` | see below | 
| `path` | path to save figure | `string` | will display plot in window if not set | 
| `title` | title of the plot | `string` | | 
| `xlim` | range over which x-axis should be displayed | `[float; 2]` | |
| `ylim` | range over which y-axis should be displayed | `[float; 2]` | | 
| `legend` | position of legend | `string` | any recognised by matplotlib, a legend will always be included if any line has its `label` field set |
| `compression` | define compression settings | `object` | see below | 
| `size` | width and height in inches | `[float; 2]` | | 
| `aspect` | aspect ratio | `float` | the width as a fraction of the default height (e.g. `"aspect": 1` would give a 4.5x4.5 plot, `"aspect": 1.5` would give a 6.75x4.5 plot) |

### 3D-specific

| field | description | type | notes | 
| ----- | ----------- | ---- | ----- |
| `zl` | z-axis label | `string` | | 
| `3d` | is this a 3D plot? | `bool` | |
| `logz` | base for z-axis log scale | `float` | | 
| `tickz` | z axis ticks | `object` | see below | 
| `angle` | view angle for 3D plot | `float` | |

## Mandatory fields (data) 

| field | description | type | notes | 
| ----- | ----------- | ---- | ----- |
| `x` | x-axis data | `[float]` | |
| `y` | y-axis data | `[float]` | must be the same length as `x` |

### 3D-specific

| field | description | type | notes | 
| ----- | ----------- | ---- | ----- |
| `x` | x-axis data | `[float]` | |
| `y` | y-axis data | `[float]` | must be same length as `x` |
| `z` | z-axis data | `[float]` | must be same length as `x` |

## Optional fields (data) 

| field | description | type | notes | 
| ----- | ----------- | ---- | ----- |
| `colour` | colour of line | `string` | any recognised by matplotlib | 
| `label` | label for legend | `string` | | 
| `linestyle` | style of line | `string` | any recognised by matplotlib |   
| `inline` | whether labels should be attached to lines | `bool` | |
| `compression` | define compression settings | `object` | see below | 

## Axis ticks
Defines the major and minor axis ticks. Defined per axis.  

| field | description | type | notes | 
| ----- | ----------- | ---- | ----- |
| `major` | major ticks | `[float]` | |
| `minor` | minor ticks | `[float]` | |

## Compression

Defines settings for simple compression. Useful if there are so many datapoints that the output file takes a long time to load or create. Can be set at both top level and per-dataset. If set in top level, then the settings will be applied to every dataset *except* those that have their own compression settings. If defining compression settings, all fields must be defined. Dataset-specific `compression` can be set to `null` to disable compression. 

| field | description | type | notes | 
| ----- | ----------- | ---- | ----- |
| `level` | chunk groups of n datapoints together | `int` | |
| `type` | how to carry out compression | `string` | "discard" \| "mean" | 



## Example JSON file 
```
{
    "data": [
        {
            "x": [
                0.0,
                0.5555555555555556,
                1.1111111111111112,
                1.6666666666666667,
                2.2222222222222223,
                2.7777777777777777,
                3.3333333333333335,
                3.8888888888888893,
                4.444444444444445,
                5.0
            ],
            "y": [
                1.0,
                0.5737534207374327,
                0.32919298780790557,
                0.18887560283756183,
                0.10836802322189586,
                0.06217652402211632,
                0.035673993347252395,
                0.020468075714350477,
                0.01174362845702136,
                0.006737946999085467
            ],
            "linestyle": "--",
            "colour": "tab:red",
            "label": "exp"
        },
        {
            "x": [
                0.0,
                0.5555555555555556,
                1.1111111111111112,
                1.6666666666666667,
                2.2222222222222223,
                2.7777777777777777,
                3.3333333333333335,
                3.8888888888888893,
                4.444444444444445,
                5.0
            ],
            "y": [
                0.0,
                0.42624657926256726,
                0.6708070121920944,
                0.8111243971624382,
                0.8916319767781041,
                0.9378234759778836,
                0.9643260066527476,
                0.9795319242856495,
                0.9882563715429786,
                0.9932620530009145
            ],
            "colour": "tab:blue",
            "label": "exp"
        },
        {
            "x": [
                0.0,
                0.5555555555555556,
                1.1111111111111112,
                1.6666666666666667,
                2.2222222222222223,
                2.7777777777777777,
                3.3333333333333335,
                3.8888888888888893,
                4.444444444444445,
                5.0
            ],
            "y": [
                0.0,
                0.5274153857718655,
                0.8961922010299563,
                0.9954079577517649,
                0.7952200570230491,
                0.3558419914010657,
                -0.19056796287548539,
                -0.6796579563927465,
                -0.9643171169287782,
                -0.9589242746631385
            ],
            "linestyle": "-",
            "colour": "tab:green",
            "label": "sin"
        }
    ],
    "xl": "time",
    "yl": "amplitude",
    "path": "exp-decay.pdf",
    "inline": true
}
```
