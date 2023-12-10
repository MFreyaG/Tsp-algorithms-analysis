from graph import *
from math import ceil

class TspBB:
    def __init__(self, graph):
        self.final_path = [None]*(graph.dimension+1)
        self.final_result = float('inf')
        
    def set_final_path(self, graph: Graph, current_path):
        self.final_path[:graph.dimension + 1] = current_path[:]
        self.final_path[graph.dimension] = current_path[0]
    
    def first_min(self, graph: Graph, vertex_number):
        min = float('inf')
        for x in range(0, graph.dimension):
            if graph.adjacency_matrix[vertex_number][x] < min and vertex_number != x:
                min = graph.adjacency_matrix[vertex_number][x]
        
        return min
    
    def second_min(self, graph: Graph, vertex_number):
        first, second = float('inf'), float('inf')
        
        for x in range(0, graph.dimension):
            if vertex_number == x:
                continue
            if graph.adjacency_matrix[vertex_number][x] <= first:
                second = first
                first = graph.adjacency_matrix[vertex_number][x]
            elif(graph.adjacency_matrix[vertex_number][x] <= second and
                 graph.adjacency_matrix[vertex_number][x] != first):
                second = graph.adjacency_matrix[vertex_number][x]
        
        return second
                
    def tsp_recursion(self, graph: Graph, current_bound, current_weight, level, current_path, visited):
        
        if level == graph.dimension:
            if graph.adjacency_matrix[current_path[level-1]][current_path[0]]!=0:
                current_result = current_weight + graph.adjacency_matrix[current_path[level-1]][current_path[0]]
                if current_result < self.final_result:
                    self.set_final_path(graph, current_path)
                    self.final_result = current_result
            return
        
        for x in range(0, graph.dimension):
            if graph.adjacency_matrix[current_path[level-1]][x] != 0 and visited[x] == False:
                temp = current_bound
                current_weight += graph.adjacency_matrix[current_path[level-1]][x]
                
                if level == 1:
                    current_bound -= (self.first_min(graph, current_path[level-1])+self.first_min(graph,x))/2
                else:
                    current_bound -= (self.second_min(graph, current_path[level-1])+self.first_min(graph,x))/2
                    
                if current_bound + current_weight < self.final_result:
                    current_path[level] = x
                    visited[x] = True
                    
                    self.tsp_recursion(graph, current_bound, current_weight, level+1, current_path, visited)
                
                current_weight -= graph.adjacency_matrix[current_path[level-1]][x]
                current_bound = temp
                
                visited = [False]*len(visited)
                for y in range(0, level):
                    if current_path[y] != -1:
                        visited[current_path[y]] = True               
    
    def tsp(self, graph: Graph):
        current_bound = 0
        current_path = [-1]*(graph.dimension+1)
        visited = [False]*graph.dimension

        for x in range(0, graph.dimension):
            current_bound += (self.first_min(graph,x)+self.second_min(graph,x))
        
        current_bound = ceil(current_bound/2)
        current_path[0] = 0
        visited[0] = True
        
        self.tsp_recursion(graph, current_bound, 0, 1, current_path, visited)
        
    def print_data(self):
        print(f'Optimal path = {self.final_path}')
        print(f'Optimal weight = {self.final_result}')
