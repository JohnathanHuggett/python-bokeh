import random

'''
#
## Edge Class
#
'''


class Edge:
    def __init__(self, destination):
        self.destination = destination


'''
#
## Vertex Class
# 
'''


class Vertex:
    def __init__(self, value='default', **pos):  # TODO test default args value = "default"
        self.value = value
        self.color = 'white'
        self.pos = pos
        self.edges = []


'''
#
## Graph Class
#
'''


class Graph:
    def __init__(self):
        self.vertexes = []

    '''
        # Breath first search
    '''

    def bfs(self, start):
        random_color = "#" + \
            ''.join([random.choice('0123456789ABCDEF') for j in range(6)])

        queue = []
        found = []

        queue.append(start)
        found.append(start)

        start.color = random_color

        while len(queue) > 0:
            v = queue[0]
            for edge in v.edges:
                if edge.destination not in found:
                    found.append(edge.destination)
                    queue.append(edge.destination)
                    edge.destination.color = random_color

            queue.pop(0)  # TODO: look at collection.dequeue

        return found

    '''
        # Connects Components
    '''

    def connectedComponents(self):
        searched = []

        for vertex in self.vertexes:
            if vertex not in searched:
                searched = self.bfs(vertex)

    '''
        # Creates a random graph
    '''

    def randomize(self, width, height, px_box, probability=0.6):
        def connectVerts(v0, v1):
            v0.edges.append(Edge(v1))
            v1.edges.append(Edge(v0))

        count = 0

        # build a grid of verts
        grid = []

        for y in range(height):
            row = []
            for x in range(width):
                v = Vertex()
                v.value = 'v' + str(x) + ',' + str(y)
                count += 1
                v.value = 'v' + str(count)
                row.append(v)

            grid.append(row)

        # Go through the grid randomly hooking up edges
        for y in range(height):
            for x in range(width):
                # connect down
                if y < height - 1:
                    if random.uniform(0, 1) < probability:
                        connectVerts(grid[y][x], grid[y + 1][x])

                # connect right
                if x < width - 1:
                    if random.uniform(0, 1) < probability:
                        connectVerts(grid[y][x], grid[y][x + 1])

        # Last pass, set the x and y coordinates for drawing
        box_buffer = 0.8
        box_inner = px_box * box_buffer
        box_inner_offset = (px_box - box_inner) / 2

        for y in range(height):
            for x in range(width):
                grid[y][x].pos = dict(
                    x=x * px_box + box_inner_offset +
                    random.uniform(0, 1) * box_inner,
                    y=y * px_box + box_inner_offset + random.uniform(0, 1) * box_inner)

        # add everything in our grid to the vertexes in this Graph
        for y in range(height):
            for x in range(width):
                self.vertexes.append(grid[y][x])

    '''
        # Debug Data 
    '''
    '''

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex('t1', x=100, y=300)
        debug_vertex_2 = Vertex('t2', x=100, y=100)
        debug_vertex_3 = Vertex('t3', x=300, y=100)
        debug_vertex_4 = Vertex('t4', x=300, y=300)
        debug_vertex_5 = Vertex('t5', x=200, y=400)
        debug_vertex_6 = Vertex('t6', x=200, y=200)
        debug_vertex_7 = Vertex('t7', x=400, y=400)
        debug_vertex_8 = Vertex('t8', x=400, y=200)
        debug_vertex_9 = Vertex('t9', x=500, y=400)
        debug_vertex_10 = Vertex('t10', x=500, y=300)
        debug_vertex_11 = Vertex('t11', x=500, y=200)

        # CUBE SHAPE
        # VERT 1
        debug_edge_1 = Edge(debug_vertex_2)
        debug_vertex_1.edges.append(debug_edge_1)

        debug_edge_2 = Edge(debug_vertex_5)
        debug_vertex_1.edges.append(debug_edge_2)

        debug_edge_3 = Edge(debug_vertex_4)
        debug_vertex_1.edges.append(debug_edge_3)

        # VERT 2
        debug_edge_4 = Edge(debug_vertex_3)
        debug_vertex_2.edges.append(debug_edge_4)

        debug_edge_5 = Edge(debug_vertex_6)
        debug_vertex_2.edges.append(debug_edge_5)

        # VERT 3
        debug_edge_6 = Edge(debug_vertex_4)
        debug_vertex_3.edges.append(debug_edge_6)

        debug_edge_7 = Edge(debug_vertex_8)
        debug_vertex_3.edges.append(debug_edge_7)

        # VERT 4
        debug_edge_8 = Edge(debug_vertex_7)
        debug_vertex_4.edges.append(debug_edge_8)

        # VERT 5
        debug_edge_9 = Edge(debug_vertex_6)
        debug_vertex_5.edges.append(debug_edge_9)

        debug_edge_10 = Edge(debug_vertex_7)
        debug_vertex_5.edges.append(debug_edge_10)

        # VERT 6
        debug_edge_11 = Edge(debug_vertex_8)
        debug_vertex_6.edges.append(debug_edge_11)

        # VERT 7
        debug_edge_12 = Edge(debug_vertex_8)
        debug_vertex_7.edges.append(debug_edge_12)

        # vert @ index 0 -> edge 1
        # vert @ index 2 -> edge 1

        self.vertexes.extend(
            [debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4, debug_vertex_5, debug_vertex_6, debug_vertex_7, debug_vertex_8, debug_vertex_9, debug_vertex_10, debug_vertex_11])
        '''
