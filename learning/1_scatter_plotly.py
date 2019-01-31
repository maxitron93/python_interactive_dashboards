import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

# Generate some random data
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

# go is a graph object. go.Scatter is a scatter graph object. feed the data into go.Scatter
data = [go.Scatter(x=random_x, y=random_y,mode='markers')]
# define the layout of the graph, like title, hover options ,etc
layout = go.Layout(title='Test Scatter',
                  xaxis = {'title': 'Test X AXIS'}, # passing in a dictionary
                  yaxis = dict(title='Test Y AXIS'),
                  hovermode = 'closest') # alternative dictionary syntax


# create a figure from the data and the layout
fig = go.Figure(data=data, layout=layout)

# plot the graph. this generates a html file
#pyo.plot(data, filename='1_scatter.html')

# plot 'figure' instead of 'data'
pyo.plot(fig, filename='1_scatter.html')