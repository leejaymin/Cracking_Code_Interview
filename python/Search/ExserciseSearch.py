
# my own works from memory

class graph:
    def __init__(self, vertexList, edgeList):
        self.vertexList = vertexList
        self.edgeList = edgeList
        self.adjacentList = [[] for id in range(len(vertexList))]
        for edge in edgeList:
            self.adjacentList[edge[0]].append(edge[1])

#DFS Traverse:
#[0, 1, 3, 2, 4, 6, 5]
def recursiveDFS(graph,node, visited=[]):
    current = node
    visited.append(current)
    for vertex in graph.adjacentList[current]:
        if vertex not in visited:
            recursiveDFS(graph, vertex, visited)
    return visited

#BFS Traverse:
#[0, 1, 2, 3, 4, 5, 6]
def BFS(graph,node, visited=[]):
    queue = [node]
    #visited.append(node)

    while queue:
        current = queue.pop()
        for vertex in graph.adjacentList[current]:
            if vertex not in visited:
                queue.insert(0, vertex)
        visited.append(current)
    return visited




if __name__ == "__main__":

    # Depth First Search (DFS)
    vertexList = ['0', '1', '2', '3', '4', '5', '6']
    edgeList = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (2, 4), (2, 5), (3, 1), (4, 2), (4, 6), (5, 2), (6, 4)]

    graphObj = graph(vertexList, edgeList)
    print("vertex list")
    print(graphObj.vertexList)
    print("edge list")
    print(graphObj.edgeList)
    print("adjacent list")
    print(graphObj.adjacentList)

    print("DFS Traverse:")
    print(recursiveDFS(graphObj,0))
    print("BFS Traverse:")
    print(BFS(graphObj,0))
