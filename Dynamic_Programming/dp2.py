# ⭐⭐⭐⭐⭐⭐⭐
# ⭐⭐⭐📝📝📝📖📖📖 2D problems

# 1️⃣ Ninja's training------✅checked

# Geek is going for a training program for n days. He can perform any of these activities: Running, Fighting, and Learning Practice. Each activity has some point on each day. As Geek wants to improve all his skills, he can't do the same activity on two consecutive days. Given a 2D matrix mat[][], where mat[i][0], mat[i][1], and mat[i][2] represent the merit points for Running, Fighting, and Learning on the i-th day, determine the maximum total merit points Geek can achieve .
# mat= [[1, 2, 5],
#                [3, 1, 1], 
#                [3, 3, 3]]
# Output: 11
# tc O(3*2^n)
# sc O(3n(call stack))
# here we did the same as we did make rec tree and acc to it make the rec fn
def ninjaTrainingHelper(arr:list[list],i:int,j:int,n:int):
    if i==n:
        return 0
    f=-1;s=-1
    if j==0:
        f=ninjaTrainingHelper(arr,i+1,j+1,n)
        s=ninjaTrainingHelper(arr,i+1,j+2,n)
        
    elif j==1:
        f=ninjaTrainingHelper(arr,i+1,j-1,n)
        s=ninjaTrainingHelper(arr,i+1,j+1,n)
    
    else:
        f=ninjaTrainingHelper(arr,i+1,j-1,n)
        s=ninjaTrainingHelper(arr,i+1,j-2,n)
    return max(f,s) +arr[i][j]



def ninjaTraining(arr:list[list]):
    if len(arr)==1:
        return max(arr[0])
    l=len(arr)
    a=ninjaTrainingHelper(arr,0,0,l)
    b=ninjaTrainingHelper(arr,0,1,l)
    c=ninjaTrainingHelper(arr,0,2,l)
    return max(a,b,c)

# tc O(3*2^n)
# sc O(3n(call stack))
# STRIVER--- did the same but put loop
def njHelper(arr,day,last):
    if day==0:
        maxi=0
        for i in range(3):
            if i!=last:
                maxi=max(maxi,arr[0][i])
        return maxi
    maxi=0
    for i in range(3):
        if i!=last:
            points=arr[day][i]+njHelper(arr,day-1,i)
            maxi=max(maxi,points)
    return maxi

def ninjaTrainingStriver(arr):
    ans=njHelper(arr,len(arr)-1,3)
    return ans



# memoization
# tc O(3*n)
# sc O(3n(call stack))
def ninjaTrainingHelperM(arr:list[list],i:int,j:int,n:int,newArr:list[list]):
    if i==n:
        return 0
    f=-1;s=-1
    if newArr[i][j]!=-1:
        return newArr[i][j]
    if j==0:
        f=ninjaTrainingHelperM(arr,i+1,j+1,n,newArr)
        s=ninjaTrainingHelperM(arr,i+1,j+2,n,newArr)
        
    elif j==1:
        f=ninjaTrainingHelperM(arr,i+1,j-1,n,newArr)
        s=ninjaTrainingHelperM(arr,i+1,j+1,n,newArr)
    
    else:
        f=ninjaTrainingHelperM(arr,i+1,j-1,n,newArr)
        s=ninjaTrainingHelperM(arr,i+1,j-2,n,newArr)
    newArr[i][j]=max(f,s) +arr[i][j]
    return newArr[i][j]


def ninjaTrainingM(arr:list[list]):
    if len(arr)==1:
        return max(arr[0])
    l=len(arr)
    newarr=[[-1 for i in range(3)] for j in range(l)]
    a=ninjaTrainingHelperM(arr,0,0,l,newarr)
    b=ninjaTrainingHelperM(arr,0,1,l,newarr)
    c=ninjaTrainingHelperM(arr,0,2,l,newarr)
    return max(a,b,c)


# tabulation
# tc O(n+3+3)
# sc O(3n)
def ninjaTrainingT(arr:list[list]):
    new=[[-1 for i in range(3)] for j in range(len(arr))]
    new[0][0]=arr[0][0]
    new[0][1]=arr[0][1]
    new[0][2]=arr[0][2]
    for i in range(1,len(arr)):
        for j in range(3):
            for k in range(3):
                if k!=j:
                    new[i][j]=max(new[i][j],new[i-1][k]+arr[i][j])
    return max(new[-1])

# tabulation optimise 
# tc O(n+3+3)
# sc O(some int(i m not confirm))


# 2️⃣ Total unique paths---checked✅in leetcode as well as in gfg
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.
# tc O(2^(m*n))
# sc o((m-1)+(n-1)(path length) )
# here we did the same as we did make rec tree and acc to it make the rec fn
# m = 3, n = 7
# ans 28

# m = 3, n = 2
# Output: 3
def uniquePathHelper(i,j,n,m):
    if i>m-1 or j>n-1:
        return 0
    if i==m-1 and j==n-1:
        return 1
    l=uniquePathHelper(i,j+1,n,m)
    r=uniquePathHelper(i+1,j,n,m)
    return l+r 


def numberOfPaths( m, n):
        a=uniquePathHelper(0,0,n,m)
        return a



# memoization 
# sc o((m-1)+(n-1)(path length) )+O(n*m)(dp arr)
# tc O(n*m)
def uniquePathHelperM(i,j,n,m,arr):
    if i>m-1 or j>n-1:
        return 0
    if i==m-1 and j==n-1:
        return 1
    if arr[i][j]!=-1:return arr[i][j]
    l=uniquePathHelperM(i,j+1,n,m,arr)
    r=uniquePathHelperM(i+1,j,n,m,arr)
    arr[i][j]=l+r
    return arr[i][j]

def uniquePathM(m,n):
    if m==1 or n==1:return 1
    arr=[[-1 for i in range(n)] for j in range(m)]
    uniquePathHelperM(0,0,n,m,arr)
    return arr[0][0]


# if make mistake in eng dont say sorry say rather
# tabulation
# memo to tabu-->
# 1. declare base case
# 2. express all states in for loop 
# 3. copy the recurrence and write
# tc==sc O(n*m)
def uniquePathHelperT(n,m,arr):
    arr[0][0]=1
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:arr[i][j]=1
            else:
                l=0;r=0
                if i>0:
                    l=arr[i-1][j]
                if j>0:
                    r=arr[i][j-1]
                arr[i][j]=l+r
                # print(i,j,l+r)
    return arr[m-1][n-1]

def uniquePathT(n,m):
    arr=[[-1 for i in range(n)] for i in range(m)]
    return uniquePathHelperT(n,m,arr)

# tabulation
# space optimization
# in 2d---> if there is prev row and prev col we can space optimize it
# ----left---------if interest can watch it further


# 3️⃣Unique path 2----✅checked in leetcode and gfg
# similar to unique path but have some edge cases
# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The testcases are generated so that the answer will be less than or equal to 2 * 109.

 
# tc sc both are same
# here we did the same as we did make rec tree and acc to it make the rec fn

# obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# ans 2
# recursion

def uniquePath2Helper(i,j,n,m,arr):
    if i>m-1 or j>n-1:
        return 0
    if i==m-1 and j==n-1:
        return 1
    if arr[i][j]==1:
        return 0
    
    l=uniquePath2Helper(i,j+1,n,m,arr)
    r=uniquePath2Helper(i+1,j,n,m,arr)
    return l+r 


def uniquePath2(arr):
    return uniquePath2Helper(0,0,len(arr[0]),len(arr),arr)


# memoization
def uniquePath2HelperM(i,j,n,m,arr,newArr):
    if i>m-1 or j>n-1:
        return 0
    if i==m-1 and j==n-1:
        return 1
    if arr[i][j]==1:
        return 0
    if newArr[i][j]!=-1:return newArr[i][j]
    l=uniquePath2HelperM(i,j+1,n,m,arr,newArr)
    r=uniquePath2HelperM(i+1,j,n,m,arr,newArr)
    newArr[i][j]=l+r
    return l+r 

def uniquePath2M(arr):
    n=len(arr[0])
    m=len(arr)
    if arr[0][0]==1:return 0
    if arr[m-1][n-1]==1:return 0
    if n==1 and m==1:return 1
    newArr=[[-1 for i in range(n)] for j in range(m)]
    uniquePath2HelperM(0,0,len(arr[0]),len(arr),arr,newArr)
    return newArr


# tabulation
def fn(nums:list,n:int):
    # a=0
    # d=dict()
    # k=len(nums)
    # for i in range(k):
    #     print(nums[:i+1],nums[i:])
    #     a=max(nums[:i+1])-min(nums[i:])
    #     if a<=n:
    #         d[i]=a
        
    # if len(d.keys())==0:
    #     return -1
    # print(d)
    # return min(d.keys())
    a=nums.index(3)
    nums.remove(4)
    print(nums)
    print(a)

# 4️⃣ Minimum path sum in grid ---- ✅leetcode
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.
# tc O(2**(m*n))
# sc O(m*n(call stack))
# here we did the same as we did make rec tree and acc to it make the rec fn
# grid = [[1,3,1],[1,5,1],[4,2,1]]
# ans=7
#  grid = [[1,2,3],[4,5,6]]
# Output: 12
# recursion
def miniPathSumHelper(i,j,m,n,arr):
    if i>m-1 or j>n-1:
        return 10**8
    if i==m-1 and j==n-1:
        return arr[i][j]
    l=miniPathSumHelper(i+1,j,m,n,arr)
    r=miniPathSumHelper(i,j+1,m,n,arr)
    return arr[i][j]+min(l,r)

def miniPathSum(grid):
    m=len(grid)
    n=len(grid[0])
    return miniPathSumHelper(0,0,m,n,grid)


# memoization
# tc O((m*n))
# sc O(m*n(call stack)+m*n(new array space))
def miniPathSumHelperM(i,j,m,n,arr,newArr):
    if i>m-1 or j>n-1:
        return 10**8
    if i==m-1 and j==n-1:
        return arr[i][j]
    if newArr[i][j]!=-1:return newArr[i][j]
    l=miniPathSumHelperM(i+1,j,m,n,arr,newArr)
    r=miniPathSumHelperM(i,j+1,m,n,arr,newArr)
    newArr[i][j]=arr[i][j]+min(l,r)
    return arr[i][j]+min(l,r)

def miniPathSumM(grid):
    m=len(grid)
    n=len(grid[0])
    new=[[-1 for i in range(n)] for j in range(m)]
    miniPathSumHelperM(0,0,m,n,grid,new)
    if new[0][0]==-1:return grid[0][0]
    return new


# tabulation
def fn(grid):
    m=len(grid)
    n=len(grid[0])
    new=[[-1 for i in range(n)] for j in range(m)]
    new[0][0]=grid[0][0]
    # ----------------left

# 5️⃣ mini/max falling path sum---- in leetcode but time limit exceed --- do it by tabulation(left ----💀💀💀💀⭐⭐)
# --leetcode have minimum one
# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
# here we can choose any index as starting in first row and any index as ending in last row
def miniFallingPath(i,j,n,arr):
    if i>n-1 or j<0 or j>n-1:
        return 10**8
    if i==n-1 :return arr[i][j]
    f=miniFallingPath(i+1,j-1,n,arr)
    s=miniFallingPath(i+1,j,n,arr)
    t=miniFallingPath(i+1,j+1,n,arr)
    return arr[i][j] +min(t,s,f) 

def fnnn(grid):
    n=len(grid)
    m=10**8
    for i in range(n):
        a=miniFallingPath(0,i,n,grid)
        m=min(a,m)
    return m


# memoization
def miniFallingPathM(i,j,n,arr,newArr):
    if i>n-1 or j<0 or j>n-1:
        return 10**8
    if i==n-1 :return arr[i][j]
    if newArr[i][j]!=-1:return newArr[i][j]
    f=miniFallingPathM(i+1,j-1,n,arr,newArr)
    s=miniFallingPathM(i+1,j,n,arr,newArr)
    t=miniFallingPathM(i+1,j+1,n,arr,newArr)
    newArr[i][j]=arr[i][j] +min(t,s,f)
    return arr[i][j] +min(t,s,f)


def fnnn(grid):
    n=len(grid)
    m=10**8
    new=[[-1 for i in range(n)] for j in range(n)]
    for i in range(n):
        a=miniFallingPathM(0,i,n,grid,new)
        m=min(a,m)
    return m


# tabulation
def miniFallingPathT(j,arr):
    n=len(arr)
    new=[[-1 for i in range(n)] for j in range(n)]
    new[0][j]=arr[0][j]
    # for i in range(n):
    #     for k in range(n):


if __name__=="__main__":
    # a=[[10,50,1],[5,100,11]]
    # print(fn( [5,0,3,3,3,1,4],3))
    # print(ninjaTrainingStriver(a))
    # print(ninjaTrainingM(a))
    # print(ninjaTrainingT(a))
    # print(f([10,15,20]))
    # print(f([1,100,1,1,1,100,1,1,100,1]))
    
    # print(numberOfPaths(3,3))
    # print(uniquePathM(1,1))
    # grid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    # # grid=[[1,1, 0]]
    # print(uniquePath2M(grid))
    # grid = [[1,3,1],[1,5,1],[4,2,1]]
    # grid = [[1,2,3],[4,5,6]]
    # print(miniPathSum( grid))
    grid=  [[2,1,3],[6,5,4],[7,8,9]]
    print(fnnn(grid))
