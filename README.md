# JSON plotter

## Mandatory fields (top level) 

- `data`: data to be plotted (object, see below)
- `xl`: x-axis label (`str`) 
- `yl`: y-axis label (`str`)
- `title`: title of the plot (`str`)

## Optional fields (top level) 

- `logx`: base for x-axis log scale (`float`, will only use log scale if set)
- `logy`: base for y-axis log scale (`float`, will only use log scale if set)

## Mandatory fields (data) 

- `x`: x-axis data (`[float]`)
- `y`: y-axis data (`[float]`)

## Optional fields (data) 

- `colour`: colour of line (`string`, any recognised by matplotlib) 
- `label`: label for legend (`string`) 
- `dashed`: whether line should be dashed (`bool`)
