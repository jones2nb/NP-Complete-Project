
"""
This is a greedy algorithm that takes processes vertex
with highest degree first to find cliques, then removes said
vertex. Flawed in that the vertex with the highest degree may not
be within the largest clique. This algorithm runs in polynomial time.

"""

def main():
    n = int(input())
    e = [input().split() for _ in range(n)]

    G = {}

    for edge in e:
        G[edge[0]] = set(edge[1::])


    keys = list(G.keys())
    maxClique = -1

    maxV = returnLargest(G)

    #continue for all nodes

    while maxV:

        result = find_clique(G, maxV)
        if len(result) > maxClique:
            maxClique = len(result)

        G.pop(maxV)
        maxV = returnLargest(G)

    print(maxClique)

#Returns the key that holds the vertex with the highest degree.

def returnLargest(G):
    max_len = 0
    max_key = ""
    for key in G:
        cur_len = len(G[key])
        if cur_len > max_len:
            max_key = key
            max_len = cur_len
    return max_key

#Searches for cliques given a starting vertex and a graph.

def find_clique(G, vert):
    clique = [vert]
    vertices = list(G.keys())

    for v in vertices:
        addToClique = True
        for u in clique:
            if u not in G[v]:
                addToClique = False
                break
        if addToClique:
            clique.append(v)

    return clique




    
    












if __name__ == "__main__":
    main()