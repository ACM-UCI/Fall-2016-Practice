# graph: A graph with positive edge weights, represented as a dictionary, The keys are nodes,
# and the values are lists of tuples containing (node, distance) pairs
# Returns the length of the shortest path that visits every node once
def tsp(graph):
    distances = {}
    for node in graph:
        distances[(node, frozenset([node]))] = 0
        
    for i in range(len(graph) - 1):
        newDistances = {}
        for key in distances:
            currNode = key[0]
            currSet = set(key[1])
            
            for edge in graph[currNode]:
                nextNode = edge[0]
                edgeLength = edge[1]
                
                if nextNode not in currSet:
                    newSet = currSet.copy()
                    newSet.add(nextNode)
                    newDistance = distances[key] + edgeLength
                    newKey = (nextNode, frozenset(newSet))
                    
                    if newKey not in newDistances or newDistance < newDistances[newKey]:
                        newDistances[newKey] = newDistance
                        
        distances = newDistances
        
    minDist = -1
    for i in distances:
        if minDist == -1 or distances[i] < minDist:
            minDist = distances[i]
            
    return minDist
            
def tsp_tests():
    print("Traveling salesman tests, should print 2, 6")
    graph1 = {0: [(1,1)], 1: [(2,1)], 2: []} # There is only one path
    print(tsp(graph1))
    graph2 = {0: [(1,5), (2,1), (3,2)], 1: [(0,5), (3,3)], 2: [(0,1), (3,4)], 3: [(1,3), (2,4)]}
    print(tsp(graph2)) # One shortest path is 2 -> 0 -> 3 -> 1
    
if __name__ == '__main__':
    tsp_tests()