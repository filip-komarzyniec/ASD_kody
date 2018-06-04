import _collections
import math
import random

class Cities :
    def __init__(self):
        self.city_coor = d
        self.city_prweights = _collections.defaultdict(float)
        self.city_weights = {}


    def create_weights(self):                               # graf pełny 4950 krawędzi
        for key1 in self.city_coor:
            for key2 in self.city_coor:
                if key2 != key1:
                    self.distance = math.sqrt((self.city_coor[key2][0] - self.city_coor[key1][0]) ** 2 + (self.city_coor[key2][1] - self.city_coor[key2][1]) ** 2)
                    if (key1,key2) not in self.city_weights:
                        self.city_weights[(key1, key2)] = round(self.distance, 4)
                        if (key2,key1) not in self.city_weights:
                            self.city_prweights[(key1, key2)] = round(self.distance, 4)

    def __str__(self):
        string = ''
        string += "coordinates:" + '\t' + str(self.city_coor) + '\n'
        string += "weights:" + '\t' + str(dict(self.city_prweights))
        return string

    def Trasale(self, start):
        coordinates = self.city_coor.copy()
        cycle = [start]
        a = random.choice(range(1, 101))
        while a == start:                               # zapobiega wylosowaniu startowego miasta
            a = random.choice(range(1, 101))
        sum = self.city_weights[start, a]
        del coordinates[start]
        del coordinates[a]
        rodzic = a
        cycle.append(a)
        c = set(range(1, 101))
        S = set()
        S.add(start)
        S.add(a)
        while coordinates:
            b = random.choice(tuple(c - S))                 # losowannie bez odwiedzonych
            if b in d:
                S.add(b)
                sum += self.city_weights[rodzic, b]
                # print('usuwam', b)                        # testowanie
                del coordinates[b]
                rodzic = b
                cycle.append(rodzic)
        #print(rodzic)
        sum += self.city_weights[rodzic, start]  # powrót do startowego miasta
        cycle.append(start)
        return 'pokonana droga to :' + '\t' + str(cycle) + '\n' + 'całkowita odległość :' + '\t' + str('%.4f' % sum)

    def MST_Prim(self, root):                        # działa xDD
        limit = dict.fromkeys(self.city_coor, math.inf)
        #print('1', limit)
        parents = _collections.defaultdict()
        self.parents_ =_collections.defaultdict(list)
        limit[root] = 0
        spanTree = {}                               # wagi MST
        pre_order = []                               # lista z kolejnością wierzchołków pre order w MST
        spanTree_vertices = list(limit.keys())                  # wierzchołki MST
        S = set()                                       # zawiera wierzchołki już odwiedzone
        # print(V)                                                       # test
        while limit:
            u = min(limit.keys() - S, key=limit.get)
            for v in limit.keys():
                if (u, v) in self.city_weights:                         # sprawdzenie czy dana krawędź istnieje w grafie
                    if limit[v] > self.city_weights[(u, v)]:
                        limit[v] = self.city_weights[(u, v)]
                        parents[v] = u
            del limit[u]
        for key, value in parents.items():                              # utworzenie słownika rodzic : wierzchołki
            self.parents_[value].append(key)
        print('wierzchołki w MST -> rodzic : wierzchołki', dict(self.parents_))
        #print('2', dict(parents))
        for key in parents.keys():                                      # krawędzie w MST
            #if parents[key] != 0:
            spanTree[(key, parents[key])] = self.city_weights[(key, parents[key])]
        #print(spanTree)
        return 'krawędzie w MST :' + '\t' + str(spanTree)

    def dfs(self, root, visited=None):
        if visited == None:
            self.visited = []
        self.visited.append(root)
        for i in self.parents_[root]:
            #print(self.parents_[i])
            self.dfs(i, self.visited)
        return 'optymalna kolejność : ' + '\t' + str(self.visited)

    def optimal_path(self, root):
        sum = 0
        for city in self.visited:
            i = self.visited.index(city)
            if i != len(self.visited)-1:
                #print(city, self.visited[i+1])
                sum += self.city_weights[(city,self.visited[i+1])]
            if i == len(self.visited)-1:
                sum += self.city_weights[(city, root)]
        return 'optymalna długość to -> :' + '\t' + str("%.4f"%sum)


with open("TSP.txt", "r") as f :
    d = {}
    for line in f:
        (key, val1, val2) = line.split()
        d[int(key)] = [float(val1), float(val2)]

tokio = Cities()
tokio.create_weights()
print(tokio, '\n')
#print(len(tokio.city_weights))
#print(len(tokio.city_prweights), '\n')
print(tokio.Trasale(10), '\n')
print(tokio.MST_Prim(10), '\n')
print(tokio.dfs(10))
print(tokio.optimal_path(10))