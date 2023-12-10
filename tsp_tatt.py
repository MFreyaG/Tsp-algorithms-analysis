from graph import *

class TspTATT:
    def __init__(self, graph):
        self.mst_set = [False]*graph.dimension
        self.parent = [None]*graph.dimension
    
    def find_min_vertex(self, key, graph: Graph):
        min = float('inf')
        for x in range(0, graph.dimension):
            if key[x] < min and self.mst_set[x] == False:
                min = key[x]
                min_index = x
        
        return min_index
    
    def prim_mst(self, graph: Graph):
        key = [float('inf')] * graph.dimension
        key[0] = 0
        
        for x in range(0, graph.dimension):
            u = self.find_min_vertex(key, graph)
            self.mst_set[u] = True
            
            for y in range(0, graph.dimension):
                if graph.adjacency_matrix[u][y] > 0 and self.mst_set[y] == False and key[y] > graph.adjacency_matrix[u][y]:
                    key[y] = graph.adjacency_matrix[u][y]
                    self.parent[y] = u
    
    def get_mst_list(self, graph):
        mst_return = []
        for x in range(1, graph.dimension):
            mst_return.append((self.parent[x], x, graph.adjacency_matrix[self.parent[x]][x]))
            
        return mst_return
    
    def calculate_path_weight(self, order_list, graph: Graph):
        total_weight = 0
        for x in range(0, len(order_list)-1):
            total_weight += graph.adjacency_matrix[order_list[x].number][order_list[x+1].number]
            
    
    def tatt(self, graph):
        mst_graph = Graph()
        mst_graph.dimension = graph.dimension
        mst_graph.node_list = graph.node_list
        
        self.prim_mst(graph)
        
        mst_edges = self.get_mst_list(graph)
        for x in range(0, graph.dimension):
            mst_graph.adjacency_matrix.append([])
            for y in range(0, graph.dimension):
                mst_graph.adjacency_matrix[x].append(0)
                
        for edge in mst_edges:
            mst_graph.adjacency_matrix[edge[0]][edge[1]] = edge[2]
            mst_graph.adjacency_matrix[edge[1]][edge[0]] = edge[2]
        
        order_list = mst_graph.dfs()
        order_list.append(graph.node_list[0])
        
        optimal_path = []
        for node in order_list:
            optimal_path.append(node.number)
            
        total_weight = 0
        for x in range(0, len(order_list)-1):
            total_weight += graph.adjacency_matrix[order_list[x].number][order_list[x+1].number]
        
        print(f'Optimal path = {optimal_path}')
        print(f'Optimal weight = {total_weight}')
    