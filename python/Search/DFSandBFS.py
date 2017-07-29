
class graph:
    def __init__(self, vertexList, edgeList):
        self.vertexList = vertexList
        self.edgeList = edgeList
        self.adjacentList = [[] for id in range(len(vertexList))]
        for edge in edgeList:
            self.adjacentList[edge[0]].append(edge[1])

def recursiveDFS(graph,node, visited=[]):
    visited.append(node)
    for neighbor in graph.adjacentList[node]:
        if neighbor not in visited:
            recursiveDFS(graph, neighbor, visited)
    return visited

def BFS(graph,node, visited=[]):
    queue = [node] # 맨 처음 버텍스를 삽입 한다.
    while queue: # 큐가 비었는지 확인 한다
        current = queue.pop() # 큐에서 데이터를 꺼내온다.
        for neighbor in graph.adjacentList[current]: # 인접 vertex에서 값을 하나 가져온다.
            if neighbor not in visited: # 현재 인접 노드의 값이 방문한 것이 아닌지 확인 한다.
                queue.insert(0,neighbor)
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
