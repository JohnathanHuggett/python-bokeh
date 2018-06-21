class Edge:
    def __init__(self, destination):
        self.destination = destination


class Vertex:
    def __init__(self, value, **pos):  # TODO test default args value = "default"
        self.value = value
        self.color = 'white'
        self.pos = pos
        self.edges = []


class Graph:
    def __init__(self):
        self.vertexes = []

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex('t1', x=100, y=300)
        debug_vertex_2 = Vertex('t2', x=100, y=100)
        debug_vertex_3 = Vertex('t3', x=300, y=100)
        debug_vertex_4 = Vertex('t4', x=300, y=300)
        debug_vertex_5 = Vertex('t5', x=200, y=400)
        debug_vertex_6 = Vertex('t6', x=200, y=200)
        debug_vertex_7 = Vertex('t7', x=400, y=400)
        debug_vertex_8 = Vertex('t8', x=400, y=200)

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
            [debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4, debug_vertex_5, debug_vertex_6, debug_vertex_7, debug_vertex_8])
