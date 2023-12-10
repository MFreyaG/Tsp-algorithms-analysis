import sys
import time
from graph import Graph
from tsp_bb import TspBB
from tsp_tatt import TspTATT
from tsp_c import TspC

file = open(file = sys.argv[1], mode = 'r')

graph = Graph()
graph.init_adjacency_matrix(file)

print(f'Twice around the tree:')
tsp_tatt = TspTATT(graph)
tsp_tatt_start_time = time.time()
tsp_tatt.tatt(graph)
tsp_tatt_start_end = time.time()
print(f'Execution time: {tsp_tatt_start_end-tsp_tatt_start_time}')
print('\n')

print(f'Christofides:')
tsp_c_start_time = time.time()
tsp_c = TspC(graph)
tsp_c.christofides(graph)
tsp_c_end_time = time.time()
print(f'Execution time: {tsp_c_end_time-tsp_c_start_time}')
print('\n')

print(f'Branch and bound:')
tsp_bb_start_time = time.time()
tsp_bb = TspBB(graph)
tsp_bb.tsp(graph)
tsp_bb_end_time = time.time()
tsp_bb.print_data()
print(f'Execution time: {tsp_bb_end_time-tsp_bb_start_time}')
