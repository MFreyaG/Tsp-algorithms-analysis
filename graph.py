from math import sqrt
from stack import Stack

class Node:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y
    
    def print_data(self):
        print(f'number: {self.number}, coordinates: ({self.x}, {self.y})')

class Graph:
    def __init__(self):
        self.node_list = []
        self.adjacency_matrix = []
        self.dimension = 0
        
    def print_nodes(self):
        for node in self.node_list:
            node.print_data()
    
    def euclidean_distance(self, node1: Node, node2: Node):
        xd = node1.x - node2.x
        yd = node1.y - node2.y
        return sqrt(xd*xd + yd*yd)
        
    def init_adjacency_matrix(self, file):
        for line in file:
            words = line.strip().split()

            if words[0] == "DIMENSION":
                self.dimension = int(words[2])

            elif words[0] == "NODE_COORD_SECTION":
                break
        
        for x in range(0, self.dimension):
            words = file.readline().strip().split()
            self.adjacency_matrix.append([])
            self.node_list.append(
                Node(
                    number=int(words[0])-1,
                    x=float(words[1]),
                    y=float(words[2])
                )
            )
        
        for x in range(0, self.dimension):
            for y in range(0, self.dimension):
                self.adjacency_matrix[x].append(self.euclidean_distance(self.node_list[x], self.node_list[y])) 
        
    def dfs_recursive(self, index, visited, order_list):
        order_list.append(self.node_list[index])
        
        visited[index] = True
        
        aux = 0
        for node in self.adjacency_matrix[index]:
            if visited[aux] == False and self.adjacency_matrix[index][aux] != 0:
                self.dfs_recursive(aux, visited, order_list)
            aux += 1

    def dfs(self):
        order_list = []
        visited = [False] * self.dimension
        self.dfs_recursive(0, visited, order_list)

        return order_list