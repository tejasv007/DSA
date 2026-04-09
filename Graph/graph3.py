
from collections import deque
# 1️⃣Distance of nearest cell having 1----PENDINg⌚⌚⌚⌚⌚⌚
# Distance of nearest cell having 0--leetcode
# adj=[[0,0,0],[0,1,0],[1,1,1]]
# ans= [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
# def distanceNearestCellHave0(adj):
#     d=deque()
#     n=len(adj)
#     m=len(adj[0])
#     vis=[[0 for i in range(m)] for j in range(n)]
#     grid=[[0 for i in range(m)] for j in range(n)]
    
#     for i in range(n):
#         for j in range(m):
#             if adj[i][j]==0:
#                 d.append((i,j,0))
#     while(len(d)!=0):
#         a=d.popleft()
#         a1=a[0]
#         a2=a[1]
#         a3=a[2]
#         vis[a1][a2]=1
#         grid[a1][a2]=a3
#         print(d)
#         steps=[[1,0],[-1,0],[0,-1],[0,1]]
#         for i in steps:
            # new=
            # if i[0]==0:
            #     if a2+i[1]>=0 and a2+i[1]<m:
            #         if vis[a1][a2+i[1]]!=1:
            #             if adj[a1][a2+i[1]]==0:
            #                 d.append((a1,a2+i[1],0))
            #             else:
            #                 d.append((a1,a2+i[1],a3+1))
            # if i[1]==0:
            #     if a1+i[0]>=0 and a1+i[0]<n:
            #         if vis[a1+i[0]][a2]!=1:
            #             if adj[a1+i[0]][a2]==0:
            #                 d.append((a1+i[0],a2,0))
            #             else:
            #                 d.append((a1+i[0],a2,a3+1))
    # return grid
# tc O(n*m +n*m*4 (worst case--everyone in 1))
# sc O(3n*m(vis+grid+queue(worst case-every one is 1)))
# here we use bfs
# in this question we have to go according to the 1 as we have to find steps in which the 0 became 1
# we can only change the 4 side of a node to 1 at a time
# adj=[[0,0,0],[0,1,0],[1,0,1]]
# ans=[[2, 1, 2], [1, 0, 1], [0, 1, 0]]
# here we use bfs as there we have to count the steps
# here we first append the row col 0 in queue when we find 1 by looping over whole matrix
# make a vis and grid similar to the matrix
# loop till queue get empty--> add 4 d of each if not vis
def distanceNearestCellHave1(adj):
    d=deque()
    n=len(adj)
    m=len(adj[0])
    vis=[[0 for i in range(m)] for j in range(n)]
    grid=[[0 for i in range(m)] for j in range(n)]
    
    for i in range(n):
        for j in range(m):
            if adj[i][j]==1:
                d.append((i,j,0))
    while(len(d)!=0):
        a=d.popleft()
        a1=a[0]
        a2=a[1]
        a3=a[2]
        vis[a1][a2]=1
        grid[a1][a2]=a3
        print(d)
        steps=[[1,0],[-1,0],[0,-1],[0,1]]
        for i in steps:
            if i[0]==0:
                if a2+i[1]>=0 and a2+i[1]<m:
                    if vis[a1][a2+i[1]]!=1:
                        if adj[a1][a2+i[1]]==1:
                            d.append((a1,a2+i[1],0))
                        else:
                            d.append((a1,a2+i[1],a3+1))
            if i[1]==0:
                if a1+i[0]>=0 and a1+i[0]<n:
                    if vis[a1+i[0]][a2]!=1:
                        if adj[a1+i[0]][a2]==1:
                            d.append((a1+i[0],a2,0))
                        else:
                            d.append((a1+i[0],a2,a3+1))
    return grid


# class Node:
#     def __init__(self, val = 0, neighbors = None):
#         self.val = val
#         self.neighbors = neighbors if neighbors is not None else []

# def dfs(vis,node,n):
#     for i in n.neighbors:
#         if i not in vis.keys():
#             new=Node(n.val)
#             vis[n]=new
#             node.neighbors.append(new)
#             dfs(vis,new,i)
#         else:
#             node.neighbors.append(vis[i])
#     return


# def clone(node):
#     if node==None:return node
#     new=Node(node.val)
#     vis=dict()
#     dfs(vis,new,node)
    
#     return new

# 2️⃣Number of Distinct Islands---correct✅checked in gfg
# use set instead of list📝📝📝⭐⭐⭐⭐⭐⭐
# firstly find the islands and store them in a list
# then in each island substract the first value from all if doing this if two island get same so both are same
# here we use bfs
# # build vis, a set which contain the all islands
def bfs(island,r,c,vis,adj):
    d=deque()
    d.append((r,c))
    vis[r][c]=1
    rr=r
    cc=c
    rows=len(adj)
    cols=len(adj[0])
    dirs=[(-1,0),(1,0),(0,1),(0,-1)]
    while d:
        a1,a2=d.popleft()
        island.append((a1-rr,a2-cc))
        for dr,dc in dirs:
            new1=a1+dr
            new2=a2+dc
            if 0 <= new1 < rows and 0 <= new2 < cols and vis[new1][new2]==0 and adj[new1][new2]==1:
                vis[new1][new2]=1
                d.append((new1,new2))
    
def dfs(island,r,c,vis,adj,r1,c1):
    vis[r][c]=1
    island.append((r-r1,c-c1))
    dir=[[-1,0],[1,0],[0,1],[0,-1]]
    for i in dir:
        new1=r+i[0]
        new2=c+i[1]
        if new1>=0 and new1<len(adj) and new2>=0 and new2<len(adj[0]):
            if vis[new1][new2]==0 and adj[new1][new2]==1:
                dfs(island,new1,new2,vis,adj,r1,c1)

def numberOfDistinctIslands(adj):
    shapes=set()
    vis=[[0 for i in range(len(adj[0]))] for i in range(len(adj))]
    for i in range(len(adj)):
        for j in range(len(adj[0])):
            if adj[i][j]==1 and vis[i][j]==0:
                island=[]
                dfs(island,i,j,vis,adj,i,j)
                shapes.add(tuple(island))
    return len(shapes)
   
# 3️⃣ Bipartite graph---✅checked
# A bipartite graph can be colored with two colors such that no two adjacent vertices share the same color. This means we can divide the graph's vertices into two distinct sets where:

# All edges connect vertices from one set to vertices in the other set.
# No edges exist between vertices within the same set.   
# adj3=[{1},{0,2},{1,3,6},{2,4},{3,5},{4,6,7},{2,5},{5}]
# ans false
# adj4=[{1},{0,2},{1,3,6},{2,4},{3,5},{4,8,7},{2,8},{5},{5,6}]
# ans True
def colorSwap(color):
    color ^=1
    return color
# BFS
# here we use vis and color dict which store the color of node 
# in bfs loop for if i not in vis then append that in queue otherwise color[i]==curr color then return false
# tc O(n+2e)
# sc O(3n)
def bipartiteGraphBFS(node:int,adj:list):
    color=dict()
    vis=[]
    d=deque()
    d.append((node,0))
    while(len(d)!=0):
        a,a1=d.popleft()
        vis.append(a)
        color[a]=a1
        for i in adj[a]:
            if i in vis:
                if color[i]!=colorSwap(a1):
                    return False
            else:
                d.append((i,colorSwap(a1)))
    return True

# DFS--- have doubt
# here we use vis and color dict which store the color of node 
# in dfs loop for if i not in vis then append that in queue otherwise color[i]==curr color then return false
# tc O(n+2e)
# sc O(3n)
def bipartiteGraphDFS(vis,color,n,c,adj,ans):
    vis.append(n)
    color[n]=c
    for i in adj[n]:
        if i not in vis:
            if not bipartiteGraphDFS(vis,color,i,colorSwap(c),adj,ans):
                return False
        else:
            if color[i] == c:
                return False
    return True


def bipartiteGraph(graph):
    vis=[]
    color=dict()# remove this for bfs
    for i in range(len(graph)):
        if i not in vis:
            if bipartiteGraphDFS(vis,color,i,0,graph) !=True:# write bipartiteGraphBFS
                return False
    return True


# 4️⃣ Detect cycle in directed graph----✅checked in gfg and course schedule(leetcode) both
# dfs
# here we build a dict list vis when we encounter a node we assign 1 in dict to that node and when we backtrack we make path[node]=0
# and in for loop when looping over neighbors if i is visited if path[i]==1 then cycle exist otherwise not
# tc O(2e+n)
# sc O(3n)
# [[], [0, 3], [3], [1]] not working for this
def detectCycleDirectedGraph(vis,path,n,adj):
    vis.append(n)
    path[n]=1
    for i in adj[n]:
        if i not in vis:
            if detectCycleDirectedGraph(vis,path,i,adj)==True:
                return True
        else:
            if path[i]==1:
                return True
    path[n]=0
    return False


# 5️⃣Topological Sort Algorithm | DFS---✅checked in gfg
# linearing order of vertices such that if there is an edge between u and v u appear before v in that ordering
# can be made for dag only (directed acyclic graph)
# here we use stack to store the node firstly do whole traversal till getting whole connection after add the node 
# mistake use set.... dont use list to store📝📝📝📝📝⭐⭐⭐⭐⭐⭐
def topologicalSort(adj):
    vis=set()
    st=[]
    for i in range(len(adj)):
        if i not in vis:
            dfsTopo(i,vis,st,adj)

    return st
def dfsTopo(n,vis,st,adj):
    vis.add(n)
    for i in adj[n]:
        if i not in vis:
            dfsTopo(i,vis,st,adj)
    st.append(n)

# for if edges are given like edges=[[3,0],[4,2],[1,2]]
# here have 5 nodes and 3 edges->3->0, 4->2, 1->2
def topoSort( V, edges):
    adj=[[] for i in range(V)]
    for i in edges:
        adj[i[0]].append(i[1])
    
    ans=topologicalSort(adj)
    return ans[::-1]


if __name__=="__main__":
    # adj=[[0,0,0],[0,1,0],[1,0,1]]
    # adj=[[0,0,0],[0,1,0],[1,1,1]]
    adj=[[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]
    # adj=[[0],[0],[0],[0],[0]]
    # print(distanceNearestCellHave0(adj))
    adj=[[1,1,0,0],[0,0,1,1]]
    grid = [[1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]]
    # print(numberOfDistinctIslands(grid))
    adj3=[{1},{0,2},{1,3,6},{2,4},{3,5},{4,6,7},{2,5},{5}]
    adj4=[{1},{0,2},{1,3,6},{2,4},{3,5},{4,8,7},{2,8},{5},{5,6}]
    
    # print(bipartiteGraphBFS(0,adj3))
    ans=[]
    coor=dict()
    # print(bipartiteGraphDFS([],coor,0,0,adj4,ans))
    adj5=[{1},{2},{3},{4},{1}]
    adj6=[[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
    # print(detectCycleDirectedGraph([],dict(),0,adj5))
    # edges = [[0, 1], [1, 2], [2, 0], [2, 3]]
    edges=[[3,0],[4,2],[1,2]]
    # print(detectCycleDirectedGraph([],dict(),0,adj))
    # edges= [[0, 1], [1, 2], [2, 0], [2, 3]]

    
    adjt=[[],[],[3],[1],[0,1],[0,2]]
    # print(topologicalSort(adjt))
    edges=[[0,1],[3,1],[1,3],[3,2]]
    adj=[[] for i in range(4)]
    for i in edges:
        adj[i[1]].append(i[0])
    print(adj)
    print(detectCycleDirectedGraph([],dict(),0,adj))