# parents: A dictionary in which the keys are nodes, and the values are lists of their parent nodes
# Returns the total number of paths from start to finish
def dag_paths(parents):
    n = len(parents)
    numPaths = [0]*n
    numPaths[0] = 1
    for i in range(1, n):
        for parent in parents[i]:
            numPaths[i] += numPaths[parent]
            
    return numPaths[n - 1]
    
def dag_paths_tests():
    print("Testing dag_paths, should print 2, 4, 5")
    graph1 = {0: [], 1: [0], 2: [0, 1]}
    print(dag_paths(graph1))
    
    graph2 = {0: [], 1: [0], 2: [0, 1], 3: [0, 1, 2]}
    print(dag_paths(graph2))
    
    graph3 = {0: [], 1: [0], 2: [1], 3: [0, 2], 4: [0, 1, 2, 3]}
    print(dag_paths(graph3))

if __name__ == '__main__':
    dag_paths_tests()