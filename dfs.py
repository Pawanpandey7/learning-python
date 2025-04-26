# first of all defing the functiom 
def dfs_recursion(graph,node,visited=None):
    if visited is None:
        visited =set()

    print(node)
    visited.add(node)

    for neighbor in graph.get(node,[]):
        if neighbor not in visited:
            dfs_recursion(graph,neighbor,visited)



    return visited
    


graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

dfs_recursion(graph,'A')
