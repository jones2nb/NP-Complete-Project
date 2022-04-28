"""
Exact solution for the max clique problem 

Author: Jacob McClaskey
Date: April 25, 2022
"""
from zeroconf import itertools


def is_clique(graph, test_clique):

    for vertex in test_clique:
        print(f"Test Clique is: {test_clique}")
        print(f"edges for {vertex} are: {graph[vertex]}")
        if test_clique.issubset(graph[vertex]):
            continue
        else:
            return False
    return True


# def clique(graph, vertex):
#     neighbors = graph[vertex]
#     clique = graph[vertex]
#     clique.add(vertex)
#     for neighbor in neighbors:
#         # print(f"temp: {temp}")
#         # print(f"cliqur: {clique}")
#         temp = clique.intersection(graph[neighbor])
#         if len(temp) > len(clique):
#             clique = temp
#         # print(clique)

#     return len(clique), clique

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
                if len(clique) > max_clique and is_clique(graph, clique):
                    if len(clique) > max_clique:
                        max_clique = len(clique)
                        found_clique = clique
                    
    # for vertex in graph.keys():
    #     clique_size, found_clique = clique(graph, vertex)
    #     if clique_size > max_clique:
    #         max_clique = clique_size
    #         cliques = found_clique
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
    size, clique = max_clique(graph)
    print(f"largest clique: {size}")
    print(f"vertex in the clique are: {clique}")


if __name__ == "__main__":
    main()
