'''Introduction to Graph Data Structure
A graph is a non-linear data structure made up of vertices (nodes) and edges (connections) that represent relationships between objects. Unlike arrays or linked lists, graphs do not follow a sequential order.
Example: On a map, each city is a vertex, and each road connecting two cities is an edge. This way, a graph represents how cities are linked.

Components of Graph Data Structure
Vertices: Vertices are the fundamental units of the graph. Sometimes, vertices are also known as vertex or nodes. Every node/vertex can be labeled or unlabelled.
Edges: Edges are drawn or used to connect two nodes of the graph. It can be ordered pair of nodes in a directed graph. Edges can connect any two nodes in any possible way. There are no rules. Sometimes, edges are also known as arcs. Every edge can be labelled/unlabelled.

Types of Graphs with Examples

A graph is a mathematical structure used to represent relationships between objects. It consists of:

Vertices (or nodes): The points in the graph representing entities.
Edges: The lines connecting pair of vertices, representing relationships or interactions.
Graphs can be classified in multiple ways based on their properties. Here’s a structured categorization:

Based On Size:
Finite Graphs
A finite graph is a graph with a finite number of vertices and edges. In other words, both the number of vertices and the number of edges in a finite graph are limited and can be counted. Finite graphs are used to represent real-world situations where there is a limited number of objects and their connections. They help in organizing, analyzing, and optimizing relationships in different applications.
Infinite Graph: 
A graph is called an infinite graph if it has an infinite number of vertices and an infinite number of edges. Unlike finite graphs, which have a fixed number of nodes and connections, infinite graphs extend indefinitely.Based on Structure:
Trivial Graph
A graph is said to be trivial if a finite graph contains only one vertex and no edge. It is also known as a singleton graph or a single vertex graph. A trivial graph is the simplest type of graph and is often used as a starting point for building more complex graphs. In graph theory, trivial graphs are considered to be a degenerate case and are not typically studied in detail
Simple Graph
A simple graph is a graph that does not contain more than one edge between the pair of vertices. A simple railway track connecting different cities is an example of a simple graph. 

Multi Graph
Any graph which contains some parallel edges but doesn’t contain any self-loop is called a multigraph. For example a Road Map. 

Parallel Edges: If two vertices are connected with more than one edge then such edges are called parallel edges that are many routes but one destination.
Loop: An edge of a graph that starts from a vertex and ends at the same vertex is called a loop or a self-loop.
Null Graph
A graph of order n and size zero is a graph where there are only isolated vertices with no edges connecting any pair of vertices.A null graph is a graph with no edges. In other words, it is a graph with only vertices and no connections between them. A null graph can also be referred to as an edgeless graph, an isolated graph, or a discrete graph
Complete Graph
A simple graph with n vertices is called a complete graph if the degree of each vertex is n-1, that is, one vertex is attached with n-1 edges or the rest of the vertices in the graph. A complete graph is also called Full Graph. 
Based On Direction:
Directed Graphs:
A graph in which edges have a direction, i.e., the edges have arrows indicating the direction of traversal
Undirected Graphs
An undirected graph is a graph where edges do not have a specific direction, meaning connections go both ways. If two places are connected, you can travel in either direction. Examples include friendships on social media and two-way roads.

Based on Edge Weights:
Weighted Graphs
A weighted graph is a graph where each edge has a number (weight) that represents distance, cost, or time. These graphs help find the shortest or cheapest paths. Examples include Google Maps, airline routes, and delivery networks.

Unweighted Graphs
An unweighted graph is a graph where all edges are treated equally, with no extra values like distance or cost. It simply shows connections between points. Examples include basic social networks and metro maps without travel times.

Special Graph:
Pseudo Graph
A pseudograph is a type of graph that allows for the existence of self-loops (edges that connect a vertex to itself) and multiple edges (more than one edge connecting two vertices). In contrast, a simple graph is a graph that does not allow for loops or multiple edges. 
Regular Graph
A regular graph is a type of undirected graph in which every vertex has the same number of edges (or neighbors). In other words, all vertices in a regular graph have the same degree.

Based On Density:
Sparse Graphs
A graph with relatively few edges compared to the number of vertices. Example: A chemical reaction graph where each vertex represents a chemical compound and each edge represents a reaction between two compounds.
Dense Graphs
A graph with many edges compared to the number of vertices. Example: A social network graph where each vertex represents a person and each edge represents a friendship.

Based on Connectivity:
Connected or Disconnected Graph
Graph is said to be connected if there exists at least one path between each and every pair of vertices in graph G, otherwise, it is disconnected. A null graph with n vertices is a disconnected graph consisting of n components. Each component consists of one vertex and no edge.

Based On Cycles:
Cyclic Graph
A graph G consisting of n vertices and n> = 3 that is V1, V2, V3- - - - Vn and edges (V1, V2), (V2, V3), (V3, V4)- - - - (Vn, V1) are called cyclic graph. 

Trees
A tree is a connected graph that contains no cycles. In other words, there is exactly one path between any two vertices.

epresentation of Graph
Last Updated : 29 Oct, 2025
A Graph is a non-linear data structure consisting of vertices and edges. The vertices are sometimes also referred to as nodes and the edges are lines or arcs that connect any two nodes in the graph. More formally a Graph is composed of a set of vertices(V) and a set of edges(E). The graph is denoted by G(V, E).

Representations of Graph
Here are the two most common ways to represent a graph : For simplicity, we are going to consider only unweighted graphs in this post.

Adjacency Matrix
Adjacency List
Adjacency Matrix Representation
An adjacency matrix is a way of representing a graph as a boolean matrix of (0's and 1's).

Let's assume there are n vertices in the graph So, create a 2D matrix adjMat[n][n] having dimension n x n.

If there is an edge from vertex i to j, mark adjMat[i][j] as 1. 
If there is no edge from vertex i to j, mark adjMat[i][j] as 0.
Representation of Undirected Graph as Adjacency Matrix:
    # 1--2        
    #   3
    graph 
matrix==> 
  0  1  2
0 0  1  1
1 1  0  1
2 1  1  0    
We use an adjacency matrix to represent connections between vertices.
Initially, the entire matrix is filled with 0s, meaning no edges exist.
There is an edge between vertex 0 and vertex 1,so we set mat[0][1] = 1 and mat[1][0] = 1.
There is an edge between vertex 0 and vertex 2,so we set mat[0][2] = 1 and mat[2][0] = 1.
There is an edge between vertex 1 and vertex 2,so we set mat[1][2] = 1 and mat[2][1] = 1.

Representation of Directed Graph as Adjacency Matrix:
Initially, the entire matrix is filled with 0s, meaning no edges exist.
Unlike an undirected graph, we do not set mat[destination][source] because the edge goes in only one direction.
There is an edge between vertex 1 and vertex 0,so we set mat[1][0] = 1.
There is an edge between vertex 2 and vertex 0,so we set mat[2][0] = 1.
There is an edge between vertex 1 and vertex 2,so we set mat[1][2] = 1.

Adjacency List Representation
An array of Lists is used to store edges between two vertices. The size of array is equal to the number of vertices (i.e, n). Each index in this array represents a specific vertex in the graph. The entry at the index i of the array contains a linked list containing the vertices that are adjacent to vertex i. Let's assume there are n vertices in the graph So, create an array of list of size n as adjList[n].

adjList[0] will have all the nodes which are connected (neighbour) to vertex 0.
adjList[1] will have all the nodes which are connected (neighbour) to vertex 1 and so on.
Representation of Undirected Graph as Adjacency list:
    # 1--2        

    #   3
    graph 
list==> 
vertex neighbour
0       1,2
1       0,2
2       0,1
We use an array of lists (or vector of lists) to represent the graph.
The size of the array is equal to the number of vertices (here, 3).
Each index in the array represents a vertex.
Vertex 0 has two neighbours (1 and 2).
Vertex 1 has two neighbours (0 and 2).
Vertex 2 has two neighbours (0 and 1).

Representation of Directed Graph as Adjacency list:
We use an array of lists (or vector of lists) to represent the graph.
The size of the array is equal to the number of vertices (here, 3).
Each index in the array represents a vertex.
Vertex 0 has no neighbours
Vertex 1 has two neighbours (0 and 2).
Vertex 2 has 1 neighbours (0).

Difference Between Graph and Tree
Last Updated : 11 Jul, 2025
Graphs and trees are two fundamental data structures used in computer science to represent relationships between objects. While they share some similarities, they also have distinct differences that make them suitable for different applications.
Key Differences Between Graph and Tree
Cycles: Graphs can contain cycles, while trees cannot.
Connectivity: Graphs can be disconnected (i.e., have multiple components), while trees are always connected.
Hierarchy: Trees have a hierarchical structure, with one vertex designated as the root. Graphs do not have this hierarchical structure.
Applications: Graphs are used in a wide variety of applications, such as social networks, transportation networks, and computer science. Trees are often used in hierarchical data structures, such as file systems and XML documents.

Traversal Technique of Graph:
Traversal techniques are used to visit all the vertices of a graph systematically. These methods help to explore the graph completely and are useful for solving many graph-related problems.

Depth First Search or DFS for a Graph
Last Updated : 28 Mar, 2026
Explores as far as possible along each branch before backtracking.
Uses a stack (or recursion).
In Depth First Search (or DFS) for a graph, we traverse all adjacent vertices one by one. When we traverse an adjacent vertex, we completely finish the traversal of all vertices reachable through that adjacent vertex. This is similar to Preorder Traversal of Binary Tree, where we first completely traverse the left subtree and then move to the right subtree. The key difference is that, unlike trees, graphs may contain cycles (a node may be visited more than once). To avoid processing a node multiple times, we use a boolean visited array.

Note: There can be multiple DFS traversals of a graph according to the order in which we pick adjacent vertices. Here we pick vertices as per the insertion order.
DFS from a Given Source of Graph:
Depth First Search (DFS) starts from a given source vertex and explores one path as deeply as possible. When it reaches a vertex with no unvisited neighbors, it backtracks to the previous vertex to explore other unvisited paths. This continues until all vertices reachable from the source are visited.
In a graph, there might be loops. So we use an extra visited array to make sure that we do not process a vertex again.

Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
Auxiliary Space: O(V + E), since an extra visited array of size V is required, And stack size for recursive calls to dfsRec function.

DFS of a Disconnected Graph:
In a disconnected graph, some vertices may not be reachable from a single source. To ensure all vertices are visited in DFS traversal, we iterate through each vertex, and if a vertex is unvisited, we perform a DFS starting from that vertex being the source. This way, DFS explores every connected component of the graph.

Time complexity: O(V + E). We visit every vertex at most once and every edge is traversed at most once (in directed) and twice in undirected.
Auxiliary Space: O(V + E), since an extra visited array of size V is required, and stack size for recursive calls of dfs function.

Breadth First Search (BFS)
Explores all neighbors of a vertex before moving to the next level.
Uses a queue.

Breadth First Search (BFS) is a graph traversal algorithm that starts from a source node and explores the graph level by level. First, it visits all nodes directly adjacent to the source. Then, it moves on to visit the adjacent nodes of those nodes, and this process continues until all reachable nodes are visited.

BFS is different from DFS in a way that closest vertices are visited before others. We mainly traverse vertices level by level.
Popular graph algorithms like Dijkstra's shortest path, Kahn's Algorithm, and Prim's algorithm are based on BFS.
BFS itself can be used to detect cycle in a directed and undirected graph, find shortest path in an unweighted graph and many more problems.

BFS from a Given Source in an Undirected Graph:
The algorithm starts from a given source vertex and explores all vertices reachable from that source, visiting nodes in increasing order of their distance from the source, level by level using a queue. Since graphs may contain cycles, a vertex could be visited multiple times. To prevent revisiting a vertex, a visited array is used.

Time Complexity: O(V + E), BFS explores all the vertices and edges in the graph. It visits every vertex and edge only once.
Auxiliary Space: O(V), Using a queue to keep track of the vertices that need to be visited.

BFS of a Disconnected Undirected Graph:
In a disconnected graph, some vertices may not be reachable from a single source. To ensure all vertices are visited in BFS traversal, we iterate through each vertex, and if any vertex is unvisited, we perform a BFS starting from that vertex being the source. This way, BFS explores every connected component of the graph.

Time Complexity: O(V + E), The for loop ensures BFS starts from every unvisited vertex to cover all components, but the visited array ensures each vertex and edge is processed only once, keeping the total time complexity to be linear.

Auxiliary Space: O(V), using a queue to keep track of the vertices that need to be visited

Applications, Advantages and Disadvantages of Breadth First Search (BFS)
Last Updated : 23 Jul, 2025
We have earlier discussed Breadth First Traversal Algorithm for Graphs. Here in this article, we will see the applications, advantages, and disadvantages of the Breadth First Search.

Applications of Breadth First Search:
1. Shortest Path and Minimum Spanning Tree for unweighted graph: In an unweighted graph, the shortest path is the path with the least number of edges. With Breadth First, we always reach a vertex from a given source using the minimum number of edges. Also, in the case of unweighted graphs, any spanning tree is Minimum Spanning Tree and we can use either Depth or Breadth first traversal for finding a spanning tree. 

2. Minimum Spanning Tree for weighted graphs: We can also find Minimum Spanning Tree for weighted graphs using BFT, but the condition is that the weight should be non-negative and the same for each pair of vertices.

3. Peer-to-Peer Networks: In Peer-to-Peer Networks like BitTorrent, Breadth First Search is used to find all neighbor nodes. 

4. Crawlers in Search Engines: Crawlers build an index using Breadth First. The idea is to start from the source page and follow all links from the source and keep doing the same. Depth First Traversal can also be used for crawlers, but the advantage of Breadth First Traversal is, the depth or levels of the built tree can be limited.

5. Social Networking Websites: In social networks, we can find people within a given distance 'k' from a person using Breadth First Search till 'k' levels.

6. GPS Navigation systems: Breadth First Search is used to find all neighboring locations.

7. Broadcasting in Network: In networks, a broadcasted packet follows Breadth First Search to reach all nodes.

8. In Garbage Collection: Breadth First Search is used in copying garbage collection using Cheney's algorithm. Breadth First Search is preferred over Depth First Search because of a better locality of reference.

9. Cycle detection in undirected graph: In undirected graphs, either Breadth First Search or Depth First Search can be used to detect a cycle. We can use BFS to detect cycle in a directed graph also.

10. Ford–Fulkerson algorithm In Ford - Fulkerson algorithm, we can either use Breadth First or Depth First Traversal to find the maximum flow. Breadth First Traversal is preferred as it reduces the worst-case time complexity to O(VE2).

11. To test if a graph is Bipartite: We can either use Breadth First or Depth First Traversal.

12. Path Finding: We can either use Breadth First or Depth First Traversal to find if there is a path between two vertices. 

13. Finding all nodes within one connected component: We can either use Breadth First or Depth First Traversal to find all nodes reachable from a given node. 

14. AI: In AI, BFS is used in traversing a game tree to find the best move.

15. Network Security: In the field of network security, BFS is used in traversing a network to find all the devices connected to it.

16. Connected Component: We can find all connected components in an undirected graph.

17. Topological sorting: BFS can be used to find a topological ordering of the nodes in a directed acyclic graph (DAG).

18. Image processing: BFS can be used to flood-fill an image with a particular color or to find connected components of pixels.

19. Recommender systems: BFS can be used to find similar items in a large dataset by traversing the items' connections in a similarity graph.

20. Other usages: Many algorithms like Prim's Minimum Spanning Tree and Dijkstra's Single Source Shortest Path use structures similar to Breadth First Search. 

Advantages of Breadth First Search:
BFS will never get trapped exploring the useful path forever.
If there is a solution, BFS will definitely find it.
If there is more than one solution then BFS can find the minimal one that requires less number of steps.
Low storage requirement - linear with depth.
Easily programmable.
Disadvantages of Breadth First Search:
The main drawback of BFS is its memory requirement. Since each level of the graph must be saved in order to generate the next level and the amount of memory is proportional to the number of nodes stored the space complexity of BFS is O(bd ), where b is the branching factor(the number of children at each node, the outdegree) and d is the depth. As a result, BFS is severely space-bound in practice so will exhaust the memory available on typical computers in a matter of minutes.

Real-Life Applications of Graph Data Structure:
Graph Data Structure has numerous real-life applications across various fields. Some of them are listed below:
Social Networks: Represent users and their connections; used to find mutual friends, suggest new connections, and detect communities.
Computer Networks: Model routers and data links; used for efficient routing, fault detection, and network optimization.
Transportation Networks: Represent cities and routes; used to find shortest or fastest paths and plan optimal travel routes.
Neural Networks: Represent neurons and synapses; used to simulate learning, brain behavior, and data processing.
Compilers: Represent data dependencies and control flows; used for optimization, register allocation, and code analysis.
Robot Path Planning: Represent states and transitions; used to compute the safest or shortest route for autonomous movement.
Project Dependencies: Represent tasks and dependencies; used in topological sorting to determine the correct execution order.
Network Optimization: Represent network nodes and links; used to minimize cost, reduce latency, and improve efficiency.
Advantages of Graph Data Structure:
Graphs are flexible: Unlike arrays, linked lists, or trees, graphs have no restrictions and can represent any type of relationship.
Model real-world problems: Useful for pathfinding, data clustering, network analysis, and machine learning.
Represent items and relationships: Any set of items and their connections can be modeled as a graph.
Simplifies complex data: Graphs make complex relationships easy to visualize and understand.
'''
# connected component --> many graph can be contribute to one graph simply each were called as connected components
# eg 
# 1-2   3-4  5-7
#       | |  \ /
#       8-9   0
# so above is a graph have 3 connected components
# acyclic--> no cycle
# cyclic--> cycle

# DAG-->directed acyclic graph
# path--> means contains a lot of nodes and each of them are reachable , a node doesnt appear twice in path
# for undirected graph
# degree -> degree of node is the no of edges connected to the node
# total degree of a graph== 2*no of edges (as every edge connected to two nodes)
# for directed graph
# indegree of node-> incoming edges
# outdegree of node -> outgoing edges
# if weight is not assign assume weight as 1
# undirected
# when build each node
# -------------------check the graph class by gfg💀✅
# undirected unweighted
class GraphUn:
    def __init__(self,nodes):
        self.l=sorted([set() for i in range(nodes)])

    def add_edge(self,v,u):
        self.l[v].add(u)
        self.l[u].add(v)
    
    def printG(self):
        for i in range(len(self.l)):
            print(i,self.l[i])
# directed unweighted
class GraphDi:
    def __init__(self,nodes):
        self.l=sorted([set() for i in range(nodes)])

    def add_edge(self,v,u):
        self.l[v].add(u)
        # self.l[u].add(v)
    
    def printG(self):
        for i in range(len(self.l)):
            print(i,self.l[i])

# undirected weighted
class GraphUnWei:
    def __init__(self,nodes):
        self.l=sorted([set() for i in range(nodes)])

    def add_edge(self,v,u,w):
        self.l[v].add((u,w))
        self.l[u].add((v,w))

    
    def printG(self):
        for i in range(len(self.l)):
            print(i,self.l[i])
# directed weighted

class GraphDiWei:
    def __init__(self,nodes):
        self.l=sorted([set() for i in range(nodes)])

    def add_edge(self,v,u,w):
        self.l[v].add((u,w))
      
    def printG(self):
        for i in range(len(self.l)):
            print(i,self.l[i])

# when build whole graph at once
# we use this most
# edges are given
# undirected and unweighted
class Graph:
    def __init__(self,edges):
        self.l=dict()
        for i in edges:
            if i[0] not in self.l:
                self.l[i[0]]={i[1]}# add (i[1],i[2]) for weighted 
            else:
                a=self.l[i[0]]
                a.add(i[1])# add (i[1],i[2]) for weighted

            # dont do for directed
            if i[1] not in self.l:
                self.l[i[1]]={i[0]}
            else:
                a=self.l[i[1]]
                a.add(i[0])
    def printG(self):
        for i in self.l.keys():
            print(i,self.l[i])

# build one for number⚡⚡⚡ 

# for traversal of graph we build fn like 
# here build a fn which take the node and a vis array which take care that every nodes that every node should be visited
# for i in range(no of edges):
#   traverseFn(i)

# graph can be of 0 based or  1 based

# BFS traversal
# if starting node change it change the traversal as the next level nodes would be diff for every node
# here we use a queue and a vis whenever a node insert into we mark it in vis that this is visited
# put a node in queue 
# loop till queue become empty
# pop the first element, mark vis for first element and insert the neighbour of it in queue
# sc O(3n)-- vis, tra, queue
# tc O(n)(while loop)+O(2E(no of edges))(for loop)
from collections import deque
# for adj list checked✅✅✅
# eg adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]
def bfs(node,g):
    d=deque()
    d.append(node)
    tra=[]
    vis=[]
    vis.append(node)
    while(len(d)!=0):
        a=d.popleft()
        tra.append(a)
        for i in g[a]:
            if i not in vis:
                vis.append(i)
                d.append(i)       
    return tra

# for dict 
def bfs(node:int,g:Graph):
    d=deque()
    d.append(node)
    tra=[]
    vis=[]
    vis.append(node)
    while(len(d)!=0):
        a=d.popleft()
        tra.append(a)
        # print(vis)
        for i in g.l[a]:
            if i not in vis:
                vis.append(i)
                d.append(i)
          
    return tra


# DFS traversal---checked✅✅✅
# here we use recursion
# sc O(n)(vis)+O(n)(tra)+O(n)(call stack)
# tc O(n)+ O(2E)
# eg adj=[[1, 3, 4],[0, 2],[1, 3], [0, 2, 4], [0, 3]]
# ans=[1, 0, 3, 2, 4]
def dfs(node:int,adj:list):
    tra=[]
    dfshelper(tra,[],node,adj)
    return tra
def dfshelper(tra:list,vis:list,node:int,adj:list):
    tra.append(node)
    vis.append(node)
    for i in adj[node]:
        if i not in vis:
            dfshelper(tra,vis,i,adj)
    return

if __name__=="__main__":
    # g1=GraphDiWei(5)
    # g1.add_edge(1,2,45)
    # g1.add_edge(3,2,7)
    # g1.add_edge(1,0,90)
    # g1.add_edge(0,4,46)
    # g1.add_edge(0,3,65)
    # g1.add_edge(4,3,72)
    # g1.printG()
    
    edges=[
        ["mumbai","delhi"],
        ["mumbai","indore"],
        ["pune","delhi"],
        ["indore","pune"],
        ["goa","pune"],
        ["indore","goa"],
        
    ]
    edges1=[
        (1,2),(3,2),(1,0),(0,3),(4,3),(0,4)
    ]
    a=Graph(edges1)
    # a.printG()
    # print(bfs(2,a))
    adj=[[1, 3, 4],[0, 2],[1, 3], [0, 2, 4], [0, 3]]
    print(dfs(1,adj))