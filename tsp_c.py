from graph import Graph
import networkx as nx

class TspC:
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
    
    def find_odd_nodes(self, mst_graph: Graph):
        odd_nodes = []
        
        index = 0
        for node in mst_graph.adjacency_matrix:
            edge_number = 0
            for edge in node:
                if edge > 0:
                    edge_number += 1
            if edge_number % 2 == 1:
                odd_nodes.append(index)
            index += 1
        
        return odd_nodes
    
    def find_minimum_cost_perfect_matching(self, odd_nodes, graph: Graph):
        networkx_graph = nx.Graph()
        for x in odd_nodes:
            networkx_graph.add_node(x)
            for y in odd_nodes:
                if x != y:
                    networkx_graph.add_edge(x,y,weight=graph.adjacency_matrix[x][y])
    
    def find_eulerian_cycle(self, mst_edges, mcpm_edges, graph: Graph):
        final_graph = nx.MultiGraph()
        final_graph.add_nodes_from(range(0, graph.dimension))
        final_graph.add_edges_from(mcpm_edges)
        
        for edge in mst_edges:
            final_graph.add_edge(edge[0],edge[1])
        
        return nx.eulerian_circuit(final_graph, source=0)
        
    def christofides(self, graph):
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
        
        odd_nodes = self.find_odd_nodes(mst_graph)
        
        networkx_graph = nx.Graph()
        for x in odd_nodes:
            networkx_graph.add_node(x)
            for y in odd_nodes:
                if x != y:
                    networkx_graph.add_edge(x,y,length=graph.adjacency_matrix[x][y])
                    
        for i,j in networkx_graph.edges:
            networkx_graph.edges[i,j]['negative_length'] = -networkx_graph.edges[i,j]['length']
            
        matching = nx.max_weight_matching(networkx_graph, maxcardinality=True, weight='negative_length')

        initial_tour = self.find_eulerian_cycle(mst_edges, matching, graph)
        
        optimal_path = [0]
        for i,j in initial_tour:
            if j not in optimal_path:
                optimal_path.append(j)
        optimal_path.append(0)
        
        total_weight = 0
        for x in range(0, len(optimal_path)-1):
            total_weight += graph.adjacency_matrix[optimal_path[x]][optimal_path[x+1]]
        
        print(f'Optimal path = {optimal_path}')
        print(f'Optimal weight = {total_weight}')
        
                
        