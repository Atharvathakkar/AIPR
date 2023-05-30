import json

def input1():
    with open('F:\\Degree\\6sem\\AI\\TE_Comp_LabPractice2-main\\As1_DFS_BFS\\graph(1).txt', 'r') as fp:
        graph = json.load(fp)
    return graph

def DFS(node, graph, visited=None):
    if visited is None:
        visited = []

    visited.append(node)
    if node in graph:
        for child in graph[node]:
            if child not in visited:
                DFS(child, graph, visited)
    return visited


def BFS(node, graph):
    visited = []
    queue = [node]
    
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            visited.append(current_node)
            if current_node in graph:
                queue.extend(graph[current_node])
    
    return visited

def menu():
    graph = input1()
    
    while True:
        visited = []
        print("1] DFS\n2] BFS\n3] Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            node = input("Enter the starting node: ")
            print("Graph sequence DFS:", DFS(node, graph))
        elif choice == '2':
            node = input("Enter the starting node: ")
            print("Graph sequence BFS:", BFS(node, graph))
        elif choice == '3':
            break

menu()
