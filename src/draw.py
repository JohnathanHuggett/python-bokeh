import math

from bokeh.io import show, output_file
from bokeh.plotting import figure, show, output_file
from bokeh.models import GraphRenderer, StaticLayoutProvider, Circle, ColumnDataSource, LabelSet, Label
from bokeh.palettes import Spectral8

from graph import *

color_list = []

# used for start and end point of edges
start = []
end = []

CIRCLE_SIZE = 25
PLOT_WIDTH = 640
PLOT_HEIGHT = 480
X_RANGE = 800
Y_RANGE = 800

# plots x,y coordinates for vertexes and labels
x = []
y = []

# values of each vertex
vertex_name = []

# class instance made
graph_data = Graph()

# graph_data.debug_create_test_data()
graph_data.randomize(5, 4, 150, 0.6)
graph_data.connectedComponents()

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
    x.append(vertex.pos['x'])
    y.append(vertex.pos['y'])
    vertex_name.append(vertex.value)
    for edge in vertex.edges:
        start.append(graph_data.vertexes.index(vertex))
        end.append(graph_data.vertexes.index(edge.destination))

### CHART SIZE ###
plot = figure(
    x_range=(-5, X_RANGE),
    y_range=(-10, Y_RANGE),
    toolbar_location=None,
    plot_width=PLOT_WIDTH,
    plot_height=PLOT_HEIGHT
)

'''
#
## LABEL MAKER
#
'''

# Label connects to vertexes
label_source = ColumnDataSource(
    data=dict(height=y,
              weight=x,
              names=vertex_name)
)

# Label position relative to the vertex it is associated with
labels = LabelSet(
    x='weight',
    y='height',
    text='names',
    level='overlay',
    source=label_source,
    render_mode='canvas',
    text_align="center",
    text_baseline="middle",
    text_color="white",
    text_font_size="10pt"
)

plot.scatter(
    x='weight',
    y='height',
    size=10,
    source=label_source
)

plot.add_layout(labels)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Circle(
    size=CIRCLE_SIZE,
    fill_color='color'
)

# this is drawing edges from start to end
graph.edge_renderer.data_source.data = dict(
    start=start,
    end=end)

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)
