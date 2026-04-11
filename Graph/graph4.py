# 1️⃣Shortest Path in Directed Acyclic Graph - Topological Sort ----- checked✅✅
# we use topological sort using dfs store the stack
# build a dist list initialize all with 1e9
# then pop out the one put the dist 0 for the one by which we need to find the dist to all
# then use while till st become empty
# apply loop over the list of the node if the node dist in dist list > dist of popone and i[1] then dist of node update to mini
# topo sort --tc O(v+e) sc O(3v)
# adj1 = [
#     [(1, 2)],
#     [(3, 1)],
#     [(3, 3)],
#     [],
#     [(0, 3), (2, 1)],
#     [(4, 1)],
#     [(4, 2), (5, 3)],
# ]
# source=6,vertex=7
# ans [5, 7, 3, 6, 2, 3, 0]
def topo_sort_dfs(node, adj, visited, stack):
    visited.add(node)
    for neighbor, _ in adj[node]:
        if neighbor not in visited:
            topo_sort_dfs(neighbor, adj, visited, stack)
    stack.append(node)


def topological_sort(v, adj):
    visited = set()
    stack = []
    for node in range(v):
        if node not in visited:
            topo_sort_dfs(node, adj, visited, stack)
    return stack
# not use for undirected-----implementation left
# shortest path tc O(v+e)+ O(v+e)(topo sort) sc O(2v)
def shortest_path_dag(source, adj, v):
    dist = [2<<30 for i in range(v)] 
    topo_order = topological_sort(v, adj)
    dist[source] = 0
    while(topo_order):
        a=topo_order.pop()
        for i,j in adj[a]:
            if dist[i]>dist[a]+j:
                dist[i]=dist[a]+j
    return dist

# 2️⃣Shortest Path in Undirected Graph with Unit Weights----- checked✅✅
# here we use the bfs
# built a dist list
# firstly we start with the element from which we need tp find the paths
# in queue we append the dist with the weight also
# if the curr weight is greater than the popout weight+1 then append that in queue with node
# tc O(v+2e)
# sc O(2v)
# can be use for directed -----implementation left
from collections import deque
def shortestPathUndirected(source,v,adj):
    d=deque()
    d.append((source,0))
    dist=[2<<30 for i in range(v)]
    dist[source]=0
    while(d):
        a,distt=d.popleft()
        for i in adj[a]:
            # here we apply greedy also
            if dist[i]>distt+1:
                dist[i]=distt+1
                d.append((i,dist[i]))
    return dist
# 📖📖📖📖📖 READ ABOUT LIBRARIES--> QUEUE HEAPDICT HEAPQ
from queue import PriorityQueue
# priorityqueue and heapdict, heapq work same
from heapdict import heapdict
from heapq import *
# 3️⃣Dijkstra algorithm  ====checked✅ 
# using priority queue
# use for undirected and directed graph
# cant be use when weight are negative
# similar to 2 one question
# tc((v+e)log v)
# sc O(v)
# priority queue
def dijkstraAlgoPQ(source, v, adj):
    p = PriorityQueue()
    dist = [float('inf')] * v
    dist[source] = 0
    p.put((0, source))

    while not p.empty():
        a, b = p.get()
        if a > dist[b]:  # ⭐⭐Skip outdated entries
            continue
        for i, j in adj[b]:
            if dist[i] > a + j:
                dist[i] = a + j
                p.put((dist[i], i))

    return dist
# heapdict
def dijkstraAlgoHeapdict(source,v,adj):
    p=heapdict()
    dist=[float('inf') for i in range(v)]
    p[source]=0
    dist[source]=0
    while p:
        b,a=p.popitem()
        if a > dist[b]:  # Skip outdated entries
            continue
        for i,j in adj[b]:
            if dist[i]>a+j:
                dist[i]=a+j
                p[i]=dist[i]
    return dist
# heapq
def dijkstraAlgoHeapq(source, v, adj):
    p = []
    heappush(p, (0, source))
    dist = [float('inf')] * v
    dist[source] = 0
    while p:
        a, b = heappop(p)
        if a > dist[b]:  # Skip outdated entries
            continue
        for i, j in adj[b]:
            if dist[i] > a + j:
                dist[i] = a + j
                heappush(p, (dist[i], i))
    return dist

# both can be use for undirected and directed 
# build for directed change the edges of undirected to directed(you know how)
# recheck both one more time💀💀📝📝📝📝

# 4️⃣Bell Ford Algorithms ----checked✅ 
# shortest path, graph can have negative weights
# if there is negative cycle---💀 doubt
# write more abt it📝📝📝 
# use for both undirected and directed graph
# run loop n-1 times on the all edges
# in each calculate dist[i]> dist[a]+b---- i neighbour of a, b is dist reaching to a
# here we dont need adj list here we need edges list
# tc O(v*e+e)
def bellFordAlgo(src,V,edges):
    dist=[float('inf') for i in range(V)]
    dist[src]=0
    for j in range(1,V):
        for u,v,w in edges:
            if dist[u]!=float('inf') and dist[v]>dist[u]+w: 
                dist[v]=dist[u]+w
    # negative cycle detection-- if there is then no shortest path can be find
    for u,v,w in edges:
        if dist[u]!=float('inf') and dist[v]>dist[u]+w:
            return [-1] 
    return dist


        
# 5️⃣Floyd warshall algorithm ----checked✅
# this multisource shortest path
# that is find shortest distance to from all to all
# build a matrix having distance
# update one by one 
# that is for eg if find path btw 0 to 1
# firstly we find 0 to 1 + 1 to 1 then 0 to 2 +2 to 1 to all nodes 
# 
# tc O(v^3) sc O(v^2)
def floydWarshallAlgo(dist):
    V = len(dist)
    # Floyd-Warshall algorithm: for each intermediate node k, update all pairs i,j
    for st in range(V):
        for bich in range(V):
            for i in range(V):
                if dist[bich][st]!=10**8 and dist[st][i]!=10**8 and dist[bich][i]>dist[bich][st]+dist[st][i]:
                    dist[bich][i]=dist[bich][st]+dist[st][i]
                

    # Check for negative cycles: if any diagonal element is negative
    for i in range(V):
        if dist[i][i] < 0:
            return None  # Negative cycle detected
    
    return dist

if __name__ == "__main__":
    adj1 = [
        [(1, 2)],
        [(3, 1)],
        [(3, 3)],
        [],
        [(0, 3), (2, 1)],
        [(4, 1)],
        [(4, 2), (5, 3)],
    ]

    V = 4; edges = [[0,1,2], [0,2,1]]
    # 📝📝📝edges to adj list
    adj=[[]for i in range(V)]
    for i in edges:
        adj[i[0]].append((i[1],i[2]))
    dist_from_start = shortest_path_dag(0, adj, 4)
    # print( dist_from_start)
    
    topo_order = topological_sort(4, adj)
    # print("Topological order:", topo_order)
    # print(shortest_path_dag(6,adj1,7))

    # undirected
    adj2=[[1,3],[0,2,3],[1,6],[0,4],[3,5],[4,6],[2,5,7,8],[6,8],[6,7]]
    # print(shortestPathUndirected(0,9,adj2))
    edges= [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
    V=3
    adj=[[]for i in range(V)]
    for i in edges:
        adj[i[0]].append((i[1],i[2]))
        adj[i[1]].append((i[0],i[2]))
    
    # print(dijkstraAlgoPQ(2,V,adj))
    # print(dijkstraAlgoHeapq(2,V,adj))
    # print(dijkstraAlgoHeapdict(2,V,adj))
    edges1=[[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
    edges2=[[0, 1, 4], [1, 2, -6], [2, 3, 5], [3, 1, -2]]
    edges3=[[1, 0, -4], [3, 5, -4], [4, 3, -5], [5, 3, -10]]
    # print(bellFordAlgo(1,8,edges3))
    edges4= [[0, 4, 10**8, 5, 10**8], [10**8, 0, 1, 10**8, 6], [2, 10**8, 0, 3, 10**8], [10**8, 10**8, 1, 0, 2], [1, 10**8, 10**8, 4, 0]]
    print(floydWarshallAlgo(edges4))