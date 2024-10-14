graph = {
'A' : ['B','C'],
'B' : ['D','E'],
'C' : ['F'],
'D' : [],
'E' : ['F'],
'F' : [],
}
visited = set() # set to keep track of visited nodes of graph.
def dfs(visted, graph, node):
#print(visited) #function for dfs
    if node not in visited:
            print (node)
            visited.add(node)
            for neighbour in graph[node]:
                dfs(visited,graph,neighbour)
print("following is the Depth-First Search")
dfs(visited, graph, 'A')
