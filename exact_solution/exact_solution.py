"""
Exact solution for the max clique problem 

Though process take in a graph loop over every vertex and then create a lists of every combination of potential cliques.
Then check to see if the potential clique is a subset of every node in the potential set. IE that every vertex in the test clique,
should contain the test clique as a subset for the vertexs edges, else the test clique is not a clique

Author: Jacob McClaskey
Date: April 25, 2022
"""
import itertools
import time

"""
Simple function to test if a given clique is in fact a clique.
Loop through the clique to see if the given clique is a subset of every edge list for each of the vertices in the given clique.
"""
def is_clique(graph, test_clique):
    for vertex in test_clique:
        # print(f"Test Clique is: {test_clique}")
        # print(f"edges for {vertex} are: {graph[vertex]}")
        if not test_clique.issubset(graph[vertex]):
            return False
    return True

"""
Simple function that takes a graph and loops over ever vertice and creates all potential combination of subsets of the edges,
and then check to see if given subset of edges is an actual clique.
"""
def max_clique(graph):
    max_clique = 0
    found_clique = []
    for vertex in graph.keys():
        for i in range(1, len(graph[vertex])):
            for path in itertools.combinations(graph[vertex], i):
                clique = set(path)
                # print(clique)
                # print(f"i: {i}")
                # print(f"vertex: {vertex}")
                clique.add(vertex)
                # if is_clique(graph, clique):
                if len(clique) > max_clique and is_clique(graph, clique):
                    if len(clique) > max_clique:
                        max_clique = len(clique)
                        found_clique = clique
    return max_clique, found_clique


"""
Input to the function should be an int stating how many vertices there are in the graph.
Followed by each vertices and the edges they connect too.
"""
def main():
    num_vert = int(input())
    graph = dict()
    for _ in range(num_vert):
        vertex = input().split()
        graph[vertex[0]] = set(vertex)
    # print(graph)
    t0 = time.time()
    size, clique = max_clique(graph)
    t1 = time.time() - t0
    print(f"largest clique: {size}")
    print(f"vertex in the clique are: {clique}")
    print(f"Time elpsed: {t1} seconds")


if __name__ == "__main__":
    main()
