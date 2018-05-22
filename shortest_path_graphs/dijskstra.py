
import _collections
import  math

class Graph:

    def __init__(self):
        self.vertices = set()
        self.edges = _collections.defaultdict(list)
        self.predges = _collections.defaultdict(list)
        self.weights = {}
        self.prweights = {}

    def add_vertex(self, label):
        for i in range(1, label+1):
            self.vertices.add(i)

    def add_edge(self, source, dest, distance):                 # graph nie jeset skierowany (NIE DIGRAF)
        self.edges[source].append(dest)
        self.edges[dest].append(source)
        self.predges[source].append(dest)
        self.weights[source, dest] = distance
        self.prweights[source,dest] = distance
        self.weights[dest, source] = distance


    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Edges: " + str(dict(self.edges)) + "\n"
        string += "Weights: " + str(self.prweights)
        return string

    def dijkstra(self,v0):                                      # implementacja dla grafu prostego
        S = set()
        self.v0 = v0
        limit =  dict.fromkeys(self.vertices, math.inf)        # tabelka górnych ograniczeń
        #print(limit)
        self.parent = _collections.defaultdict(list)      # tabelka rodziców
        limit[v0] = 0
        path = []
        while S!=self.vertices:
            u = min(limit.keys() - S,key=limit.get)
            #print('u to:', u)
            S.add(u)
            #print('zbiór S :', S)
            for vertex in (self.vertices - S):
                #print(u)
                if (u, vertex) in self.weights :                # dla grafów skierowanych -> in self.prweights
                    if limit[vertex] > limit[u] + self.weights[u,vertex] :
                        #print(self.weights[u,vertex])
                        self.parent[vertex].append(u)
                        #print(vertex, self.parent[vertex])
                        limit[vertex] = limit[u] + self.weights[(u,vertex)]
        for i in self.vertices:
            self.short_paths(i)


    def BeFord(self,v0_):                               # tylko dla grafów skierowanych!!!
        self.v0_ = v0_
        limit = dict.fromkeys(self.vertices, math.inf)
        self.parent_ = _collections.defaultdict(list)
        limit[self.v0_] = 0
        for i in range(1,len(self.vertices)):
            for u,v in self.prweights.keys():
                #(u,v) = set((u,v))
                if limit[v] > limit[u] + self.weights[u,v]:
                    limit[v] = limit[u] + self.weights[u,v]
                    self.parent_[v].append(u)
        for u,v in self.prweights.keys():
            #(u, v) = set((u, v))
            if limit[v] > limit[u] + self.weights[u, v]:
                print('ERROR ->ujemny cykl')
                return
        for i in self.vertices:
            self.BeFord_shortpaths(i)

    def BeFord_shortpaths(self, end):
        print('shortest path from', end, 'to', self.v0_, 'is :', self.parent_[end][::-1], sep='\t' )
    def short_paths(self, start):
        print('shortest path from', start, 'to', self.v0, 'is :', self.parent[start][::-1], sep='\t')

My_graph = Graph()
My_graph.add_vertex(5)
My_graph.add_edge(1, 3, 4)
My_graph.add_edge(1, 2, 2)
My_graph.add_edge(4, 1, 1)
My_graph.add_edge(5, 1, 3)
My_graph.add_edge(2, 3, 1)
My_graph.add_edge(4, 3, 2)
My_graph.add_edge(4, 5, 3)
print(My_graph,'\n')
My_graph.dijkstra(1)
print('\n')
My_graph.BeFord(1)