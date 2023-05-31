def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def recursive_dfs(graph, start_node):
    visited=set()
    dfs(visited, graph, start_node)

def bfs(visited, graph, node, queue):
    visited.add(node)
    queue.append(node)

    while queue:
        s=queue.pop(0)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
def main():
    visited1 = set()
    visited2 = set()
    queue=[]
    n=int(input("Enter no of nodes: "))
    graph={}

    for i in range(1, 1+n):
        edge = int(input("Enter the no of Edges for node {}: ".format(i)))
        graph[i]=[]
        for j in range(1, edge+1):
            node=int(input("Enter Edges {} of node {}: ".format(j,i)))
            graph[i].append(node)

    start_node = int(input("Enter the Starting node: "))
    print("DFS: ")
    recursive_dfs(graph, start_node)
    print()
    print("BFS: ")
    bfs(visited2, graph, start_node, queue)


if __name__ == "__main__":
    main()
