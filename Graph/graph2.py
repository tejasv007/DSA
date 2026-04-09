# here we build whole graph using matrix or adjacency list
# 1️⃣ Number of provinces-- checked✅
# here adj is matrix
# find the connected component in a graph
# here we can use any traversal bfs or dfs
# firstly we apply loop over each node if its not exist in vis then dfs the node
# dfs update the vis
# then go to next node and whenever dfs call we increase count 
# output the count var
# 1 based
# isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# ans 2
def noOfProvincedfs(node,adj,vis):
    vis.append(node)
    for i in range(len(adj[node-1])):
        if adj[node-1][i]==1:
            if (i+1) not in vis:
                noOfProvincedfs(i+1,adj,vis)

def noOfProvinces(isConnected):
    c=0
    vis=[]
    for i in range(1,len(isConnected)+1):
        if i not in vis:
            noOfProvincedfs(i,isConnected,vis)
            c+=1
    return c

# 2️⃣Number of Islands---- checked✅
# Tc O(m*n(main loop )+m*n(bfs traversal worst case))
# sc O(m*n(for bfs traversal that is taken by deque worst case--- every is 1 )+m*n(vis 2d list))
# here we find the island where 1 is land and 0 is water(look at leetcode ques 200)
# here we use bfs, firstly we build a vis array similar to grid and assign 1 acc to grid by bfs
# here we loop over every node and if it is not in vis we execute the bfs one
# now bfs have similar traversal as original bfs has but here we put pair like [row,col]
# when we pop out the one we have to traverse row,col-1,row,col,row,col+1 and row-1,col,row,col,row+1,col
# so for that we apply two loops 
# with bfs we update the vis also
# grid = [
    # ["1","1","1","1","0"],
    # ["1","1","0","1","0"],
    # ["1","1","0","0","0"],
    # ["0","0","0","0","0"]
    # ]
# ans =1
from collections import deque
def bfs(row,col,vis,grid):
    n=len(grid)
    m=len(grid[0])
    vis[row][col]="1"
    d=deque()
    d.append([row,col])
    j=-1
    k=-1
    while(len(d)!=0):
        a=d.popleft()
        a1=a[0]
        a2=a[1]
        for k in range(-1,2):
            if a2+k>=0 and a2+k<m:
                if grid[a1][a2+k]=="1" and vis[a1][a2+k]=="0":
                    vis[a1][a2+k]="1"
                    d.append([a1,a2+k])
        for j in range(-1,2):
             if a1+j>=0 and a1+j<n :
                if grid[a1+j][a2]=="1" and vis[a1+j][a2]=="0":
                    vis[a1+j][a2]="1"
                    d.append([a1+j,a2])

def numIslands(grid):
    n=len(grid)
    m=len(grid[0])
    count=0
    vis=[["0" for i in range(m)] for j in range(n)]
    print(vis)
    for r in range(n):
        for c in range(m):
            # print(vis)
            # print(grid)
            if grid[r][c]=="1" and vis[r][c]=="0":
                print(vis)
                bfs(r,c,vis,grid)
                count+=1
    return count


# 3️⃣Flood Fill Algorithm---- checked✅
# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill:

# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.
# here we use bfs
# and build a vis 2d list which consist of only 0 and when a node visited we update the grid and vis
# tc O(n*m(worst case if all are same in grid))
# sc O(n*m(vis array)+n*m(deque if worst case ))
# image = [[1,1,1],[1,1,0],[1,0,1]],sr=1,sc=1,color=2
# ans= [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
# by bfs
def floodFill(grid,sr,sc,color):
    f=grid[sr][sc]
    if color==f:
        return grid
    d=deque()
    n=len(grid)
    m=len(grid[0])
    vis=[[0 for i in range(m)] for j in range(n)]
    d.append([sr,sc])
    vis[sr][sc]=1
    grid[sr][sc]=color
    while(len(d)!=0):
        a=d.popleft()
        a1=a[0]
        a2=a[1]
        for j in range(-1,2):
            if a2+j>=0 and a2+j<m:
                if  grid[a1][a2+j]==f and vis[a1][a2+j]==0:#--- why dont grid[a1][a2+j]==color taken
                    vis[a1][a2+j]=color
                    grid[a1][a2+j]=color
                    d.append([a1,a2+j])
        for k in range(-1,2):
            if a1+k>=0 and a1+k<n:
                if grid[a1+k][a2]==f and vis[a1+k][a2]==0:#--- why dont grid[a1+k][a2]==color taken
                    vis[a1+k][a2]=color
                    grid[a1+k][a2]=color
                    d.append([a1+k,a2])
    return grid


# 4️⃣ Rotten Oranges---- checked✅
# here we use bfs as we want to traverse level wise
# then we use a map to store the time and the node row and col
# traverse whole grid and push the row col with time in queue which has val =2
# pop out one by one and also insert the next 4 d next node of the curr one and increase time by 1 and also update next nodes if it is 1 
# do above 2 till queue get empty
# then loop over the grid if there any 1 if exist return -1 otherwise max time 
# tc O(n*m(traverse to find first all 2s)+n*m(worst case bfs if every node is 2))
# sc O(n*m(queue worst case if every node is 2))
# grid1 = [[2,1,1],[0,1,1],[1,0,1]]
# ans=-1

def rottenOranges(grid):
    n=len(grid)
    m=len(grid[0])
    d=deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j]==2:
                d.append([i,j,1])
    time=0
    while(len(d)!=0):
        a=d.popleft()
        a1=a[0]
        a2=a[1]
        a3=a[2]
        if time<a3:time=a3
        bfs(a1,a2,a3,grid,d)
    print(grid)
    for i in grid:
        if 1 in i:
            return -1
    return time

def bfs(r,c,l,grid,d):
    for k in range(-1,2):
        if c+k>=0 and c+k<len(grid[0]):
            if grid[r][c+k]==1:
                grid[r][c+k]=2
                d.append([r,c+k,l+1])
    for j in range(-1,2):
        if r+j>=0 and r+j<len(grid):
            if grid[r+j][c]==1:
                grid[r+j][c]=2
                d.append([r+j,c,l+1])
    

#5️⃣ Detect cycle in a graph
# BFS
# undirected, having adj list
# here we use bfs, use queue to store the node and its parent node
# and as we check next node of each node here we put condition if the node present in vis,
# if yes return true else do bfs till last then at last return false
# 0 based
# tc o(n+2e)
# sc O(2n ( queue+vis))
def detectCycleBFS(node,adj):
    d=deque()
    vis=[node]
    d.append((node,-1))
    while(len(d)!=0):
        a=d.popleft()
        a1=a[0]
        a2=a[1]
        for i in adj[a1]:
            if i in vis:
                if a2!=i:
                    return True
            else:
                vis.append(i)
                d.append((i,a1))
    return False


# DFS
# here we use dfs
# here we put one condition in for loop as use to check for the neighbouring nodes, that par should be equal to i if i in vis then return true
# at last return false 
# tc O(n+2e)---know why⚡⚡⚡💀💀
# sc O(2n (vis+call stack))
def detectCycleDFS(node,par,adj,vis):
    vis.append(node)
    for i in adj[node]:
        if i in vis:
            if i!=par:
                return True
        else:
            detectCycleDFS(i,node,adj,vis)

    return False

if __name__=="__main__":
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    # print(noOfProvinces(isConnected))
    grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]

    # print(numIslands(grid))
    image = [[1,1,1],[1,1,0],[1,0,1]]
    # print(floodFill(image,1,1,2))
    # image[0][2]=5/
    grid1 = [[2,1,1],[0,1,1],[1,0,1]]
    # grid1 = [[0,2]]
    # print(rottenOranges(grid1))
    adj=[[1,4],[0,2],[1,3],[2,4],[3,1]]
    # print(detectCycleBFS(0,adj))
    print(detectCycleDFS(0,-1,adj,[]))
