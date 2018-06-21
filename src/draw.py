import math

from bokeh.io import show, output_file
from bokeh.plotting import figure, show, output_file
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, Range1d, LabelSet, Label
from bokeh.palettes import Spectral8

from graph import *

color_list = []
start = []
end = []
# LABEL_FONT_SIZE = "10pt"

# class instance made
graph_data = Graph()
graph_data.debug_create_test_data()

N = len(graph_data.vertexes)
node_indices = list(range(N))

'''
for i, vertex in enumerate(graph_data.vertexes):  # keeps track of value and index
    color_list.append(vertex.color)
    if (len(vertex.edges)):
        for edge in vertex.edges:
            start.append(i)
            end.append(graph_data.vertexes.index(edge.destination))
'''

# Code refactoried from above ( a little more costly )
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)
    if (len(vertex.edges)):
        for edge in vertex.edges:
            start.append(graph_data.vertexes.index(vertex))
            end.append(graph_data.vertexes.index(edge.destination))

### CHART SIZE ###
plot = figure(title='Graph Layout Demonstration', x_range=(0, 500), y_range=(0, 500),
              tools='', toolbar_location=None)

'''
#
## LABEL MAKER
#
'''

# Label connects to vertexes
source = ColumnDataSource(data=dict(height=[v.pos['y'] for v in graph_data.vertexes],
                                    weight=[v.pos['x']
                                            for v in graph_data.vertexes],
                                    names=[v.value for v in graph_data.vertexes]))

# Label position relative to the vertex it is associated with
labels = LabelSet(x='weight', y='height', text='names', level='overlay',
                  x_offset=-6, y_offset=-10, source=source, render_mode='canvas')


plot.scatter(x='weight', y='height', size=10, source=source)
plot.add_layout(labels)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Circle(size=25, fill_color='color')

# this is drawing edges from start to end
graph.edge_renderer.data_source.data = dict(
    start=start,
    end=end)

# print(start)
# print(end)

# plots x,y coordinates for vertexes
x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)
