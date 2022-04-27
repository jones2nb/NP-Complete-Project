"""
Exact solution for the max clique problem 

Author: Jacob McClaskey
Date: April 25, 2022
"""
def clique(graph, vertex):
    neighbors = graph[vertex]
    for edge in neighbors:
        pass

    pass

def max_clique(graph):
    max_clique = 0
    clique = []
    for vertex in graph.keys():
        clique_size, found_clique = clique(graph, vertex)
        if clique_size > max_clique:
            max_clique = clique_size
            clique = found_clique
    return max_clique, clique


"""
Input to the function should be an int stating how many vertices there are in the graph.
Followed by each vertices and the edges they connect too.
"""
def main():
    num_vert = int(input())
    graph = dict()
    for _ in range(num_vert):
        vertex = input().split()
        graph[vertex[0]] = set(vertex[1:])
    # print(graph)

if __name__ == "__main__":
    main()
