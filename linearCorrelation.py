'''
scatterPlotAxes.py create a data set and plots it in a scatter plt array
Version 6/2/14. 
(c) 2014 Project LEad The Way, Inc
'''
import random
import numpy as np
import cse
reload(cse)
        
variables = cse.montecarlo.retail_data(20)
fig, ax = cse.viz.scatter_plot_array(variables) 
fig.show()