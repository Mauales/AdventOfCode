from itertools import chain
from collections import Counter , deque

file = open("input.txt")
# file = open("test1.txt")

connections = {}

input = []
for line in file:
    input.append(line.rstrip().split('-'))


def create_graph(input):
    g = {i: [] for i in (sorted(set(chain.from_iterable(input)), reverse=True))}
    #print(g)
    for i in input:
        g[i[0]].append(i[-1])
        g[i[-1]].append(i[0])
    #print(g)
    return g


def find_all_paths(graph, start, end, path=[], not_allowed=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node_allowed(graph, path, node):
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def node_allowed(graph, path, node):
            small_caves = [k for k, _ in graph.items() if k == k.lower()]
            d = Counter([e for e in path if e in small_caves]) #check that small cave is not visited twice
            #print(small_caves, path, node, d, d[node])
            if (d[node] < 1):
                return True
            else:
                return False

paths = find_all_paths(create_graph(input), 'start', 'end', [])
print(f'part1: {len(paths)}')