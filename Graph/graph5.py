# MINIMUM SPANNING TREE
'''What is Minimum Spanning Tree (MST)
Last Updated : 23 Jul, 2025
A spanning tree is defined as a tree-like subgraph of a connected, undirected graph that includes all the vertices of the graph. Or, to say in Layman's words, it is a subset of the edges of the graph that forms a tree (acyclic) where every node of the graph is a part of the tree.

The minimum spanning tree has all the properties of a spanning tree with an added constraint of having the minimum possible weights among all possible spanning trees. Like a spanning tree, there can also be many possible MSTs for a graph.
Properties of a Spanning Tree
The spanning tree holds the below-mentioned principles:

The number of vertices (V) in the graph and the spanning tree is the same.
There is a fixed number of edges in the spanning tree which is equal to one less than the total number of vertices ( E = V-1 ).
The spanning tree should not be disconnected, as in there should only be a single source of component, not more than that.
The spanning tree should be acyclic, which means there would not be any cycle in the tree.
The total cost (or weight) of the spanning tree is defined as the sum of the edge weights of all the edges of the spanning tree.
There can be many possible spanning trees for a graph.


Minimum Spanning Tree
A minimum spanning tree (MST) is defined as a spanning tree that has the minimum weight among all the possible spanning trees.

The minimum spanning tree has all the properties of a spanning tree with an added constraint of having the minimum possible weights among all possible spanning trees. Like a spanning tree, there can also be many possible MSTs for a graph.

Algorithms to find Minimum Spanning Tree
There are several algorithms to find the minimum spanning tree from a given graph, some of them are listed below:

Kruskal's Minimum Spanning Tree Algorithm:

This is one of the popular algorithms for finding the minimum spanning tree from a connected, undirected graph. This is a greedy algorithm. The algorithm workflow is as below:

First, it sorts all the edges of the graph by their weights, 
Then starts the iterations of finding the spanning tree. 
At each iteration, the algorithm adds the next lowest-weight edge one by one, such that the edges picked until now does not form a cycle.
This algorithm can be implemented efficiently using a DSU (Disjoint-Set) data structure to keep track of the connected components of the graph. This is used in a variety of practical applications such as network design, clustering, and data analysis.

Prim's Minimum Spanning Tree Algorithm:

This is also a greedy algorithm. This algorithm has the following workflow:

It starts by selecting an arbitrary vertex and then adding it to the MST. 
Then, it repeatedly checks for the minimum edge weight that connects one vertex of MST to another vertex that is not yet in the MST. 
This process is continued until all the vertices are included in the MST. 
To efficiently select the minimum weight edge for each iteration, this algorithm uses priority_queue to store the vertices sorted by their minimum edge weight currently. It also simultaneously keeps track of the MST using an array or other data structure suitable considering the data type it is storing.

This algorithm can be used in various scenarios such as image segmentation based on color, texture, or other features. For Routing, as in finding the shortest path between two points for a delivery truck to follow.

Boruvka's Minimum Spanning Tree Algorithm:
This is also a graph traversal algorithm used to find the minimum spanning tree of a connected, undirected graph. This is one of the oldest algorithms. The algorithm works by iteratively building the minimum spanning tree, starting with each vertex in the graph as its own tree. In each iteration, the algorithm finds the cheapest edge that connects a tree to another tree, and adds that edge to the minimum spanning tree. This is almost similar to the Prim's algorithm for finding the minimum spanning tree. The algorithm has the following workflow:

Initialize a forest of trees, with each vertex in the graph as its own tree.
For each tree in the forest: 
Find the cheapest edge that connects it to another tree. Add these edges to the minimum spanning tree.
Update the forest by merging the trees connected by the added edges.
Repeat the above steps until the forest contains only one tree, which is the minimum spanning tree.
The algorithm can be implemented using a data structure such as a priority queue to efficiently find the cheapest edge between trees. Boruvka's algorithm is a simple and easy-to-implement algorithm for finding minimum spanning trees, but it may not be as efficient as other algorithms for large graphs with many edges.

Applications of Minimum Spanning Trees:
Network design: Spanning trees can be used in network design to find the minimum number of connections required to connect all nodes. Minimum spanning trees, in particular, can help minimize the cost of the connections by selecting the cheapest edges.
Image processing: Spanning trees can be used in image processing to identify regions of similar intensity or color, which can be useful for segmentation and classification tasks.
Biology: Spanning trees and minimum spanning trees can be used in biology to construct phylogenetic trees to represent evolutionary relationships among species or genes.
Social network analysis: Spanning trees and minimum spanning trees can be used in social network analysis to identify important connections and relationships among individuals or groups.

'''
# Prim's Algorithm and krushkal algorithm is used for finding mst
# use for undirected 
# 1️⃣Prim's algorithms--->---checked✅ 
# reread📖📖
# in this we use priority queue to store (wt,node, parent)

# 1 and pop out the one and store the neighbours of it in it if the neighbor is not in vis
# 2 check the pop out node exist in vis if not then append it. then mark the edge as that edges would be in the mst and if it exist then ignore it 
# follow above two till get the get whole queue empty
# in 2 why we ignore and then append its neighbour bcoz we already got the shortest path to reach till the node so why do add
# tc O((2e+v)*log v(pq tc))
# sc O(2e(pq)+v(vis)+mst(v-1))
# undirected
# adj=[[(2,1),(1,5)],[(0,5),(2,1)],[(1,1),(0,1),(3,7),(4,5)],[(2,7),(4,4)],[(2,5),(3,4)]]
# ans=([[0, 2], [2, 1], [2, 4], [4, 3]], 11)
from queue import PriorityQueue
def primAlgorithm(adjList):
    vis={0}
    p=PriorityQueue()
    mst=[]
    p.put((0,0,-1))
    s=0
    while(not p.empty()):#v
        wt,node,par=p.get()
        if node not in vis:
            mst.append([par,node])
            s+=wt
            vis.add(node)
        for i in adjList[node]:#2e
            if i[0] not in vis:
                p.put((i[1],i[0],node))

    return mst,s

# 2️⃣Disjoint Set-----📖📖📖📖📖📖rewatch and re learn
# we have connected component and when we ask if two node eg 1 and 5 belong to same connected component ---> it would take O(v)
# but it can be solve by disjoint set in const time tc
# it is usually use in dynamic graph
# 
# have two fn findPar and union( can be done thru rank or size)
# union by rank-->
# build two array ie parent(assign own node at first) and rank(assign 0 to all at first)
# union (u,v)-->
# 1. find ultimate parent(guy at topc) of u and v ie pu and pv
# 2. find rank of pu and pv
# 3. connect smaller rank to larger rank always

class DisJointSet:
    def __init__(self,V):
        self.rank=[0 for i in range(V+1)]
        self.par=[i for i in range(V+1)]
    

    def findUPar( self,node):
        if node==self.par[node]:
            return node
        self.par[node]=self.findUPar(self.par[node])
        return self.par[node]

    def unionByRank(self,u,v):
        pu=self.findUPar(u)
        pv=self.findUPar(v)
        if pu==pv:return
        if self.rank[pu]<self.rank[pv]:
            self.par[pu]=pv
        elif self.rank[pv]<self.rank[pu]:
            self.par[pv]=pu
        else:
            self.par[pv]=pu
            self.rank[pu]+=1
        
# 3️⃣Krushkal Algorithm---checked✅ 
# here we use edges not the list or matrix
# firstly sorted the edges into sorted wt
# pick one by one and check if the findUpar(first node) and findUPar(second node)
# if both same ignore it else: append it in mst
# tc O(e*logv)
# sc O(v-1)
# Optimizing tool selection...The time complexity of Kruskal's algorithm is O(E log E), dominated by sorting the edges. The disjoint set operations (find and union) are nearly O(E α(V)) amortized, where α(V) is the inverse Ackermann function (effectively constant for practical purposes). Overall: O(E log E + E α(V)).
def krushkalAlgo(edges,v):
    d=DisJointSet(v)
    mst=[]
    s=0
    edges.sort(key=lambda i:i[2])
    for i,j,k in edges:#take e
        if d.findUPar(i)!=d.findUPar(j):#take 2log v
            d.unionByRank(i,j)# O(1)
            mst.append((i,j))
            s+=k
        
    return mst,s




if __name__=="__main__":
    adj=[[(2,1),(1,5)],[(0,5),(2,1)],[(1,1),(0,1),(3,7),(4,5)],[(2,7),(4,4)],[(2,5),(3,4)]]
    edges=[]
    for i in range(len(adj)):
        for j,k in adj[i]:
            if [j,i,k] not in edges:
                edges.append([i,j,k])
    # print(edges)
    print(krushkalAlgo(edges,5))
    print(primAlgorithm(adj))
    times = [[2,1,1],[2,3,1],[3,4,1]];n = 4; k = 2
    d=DisJointSet(7)
    d.unionByRank(1,2)
    d.unionByRank(2,3)
    d.unionByRank(4,5)
    d.unionByRank(6,7)
    d.unionByRank(5,6)
    d.unionByRank(1,2)
    # if d.findUPar(3)==d.findUPar(7):
    #     print("ss")
    # else:print("ns")
    # d.unionByRank(3,7)
    # if d.findUPar(3)==d.findUPar(7):
    #     print("ss")
    # else:print("ns")
    