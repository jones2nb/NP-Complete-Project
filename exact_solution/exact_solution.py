"""
Exact solution for the max clique problem 

Author: Jacob McClaskey
Date: April 25, 2022
"""
def clique(graph, vertex):
    neighbors = graph[vertex]
    clique = [vertex]
    for neighbor in neighbors:
        temp = graph[neighbor]
        for vertex in temp:
            if vertex in neighbors and vertex not in clique:
                clique.append(vertex)

    return len(clique), clique

def max_clique(graph):
    max_clique = 0
    cliques = []
    for vertex in graph.keys():
        clique_size, found_clique = clique(graph, vertex)
        if clique_size > max_clique:
            max_clique = clique_size
            cliques = found_clique
    return max_clique, cliques


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
    size, clique = max_clique(graph)
    print(f"largest clique: {size}")
    print(f"vertex in the clique are: {clique}")


if __name__ == "__main__":
    main()
