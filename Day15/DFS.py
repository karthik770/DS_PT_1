def dfs(graph, start, visited=None):# 0 # dfs(graph , 1, visited)
    if visited is None:
        visited = set()
    visited.add(start) # visited={0,1,2,3,4}
    print(start)

    for next in graph[start] - visited: # 1
        dfs(graph, next, visited) # dfs(graph , 1, visited)
    return visited

graph = {'0': set(['1', '2','3']),
         '1': set(['0', '2', '3']),
         '2': set(['0','4']),
         '3': set(['0']),
         '4': set(['2'])}

dfs(graph, '0')