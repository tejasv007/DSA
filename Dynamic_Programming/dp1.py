'''Dynamic Programming (DP) Introduction
Last Updated : 7 Jan, 2026
Dynamic Programming (DP) is a method used to solve complex problems by breaking them into smaller overlapping subproblems and storing their results to avoid recomputation. It is an optimization technique that transforms recursive solutions with exponential time into efficient ones with polynomial time.

Why Do We Need Dynamic Programming?
When we try to solve complex problems, especially those involving choices or sequences, we often notice that the same smaller problems appear again and again. If we solve them every time from scratch, it leads to unnecessary repetition and wasted computation.

Dynamic Programming helps us avoid this. Instead of recomputing results, we remember (or store) the solutions of smaller problems and reuse them when needed.
This simple idea — of remembering the past to solve the future faster — forms the core of DP.

Dynamic Programming is a commonly used algorithmic technique used to optimize recursive solutions when same subproblems are called again.

The core idea behind DP is to store solutions to subproblems so that each is solved only once.
To solve DP problems, we first write a recursive solution in a way that there are overlapping subproblems in the recursion tree (the recursive function is called with the same parameters multiple times).
To make sure that a recursive value is computed only once (to improve time taken by algorithm), we store results of the recursive calls.
There are two ways to store the results, one is top down (or memoization) and other is bottom up (or tabulation).
When to Use Dynamic Programming (DP)?
Dynamic programming is used for solving problems that consists of the following characteristics:

1. Optimal Substructure:
The property Optimal substructure means that we use the optimal results of subproblems to achieve the optimal result of the bigger problem.

Example:

Consider the problem of finding the minimum cost path in a weighted graph from a source node to a destination node. We can break this problem down into smaller subproblems:

Find the minimum cost path from the source node to each intermediate node.
Find the minimum cost path from each intermediate node to the destination node.
The solution to the larger problem (finding the minimum cost path from the source node to the destination node) can be constructed from the solutions to these smaller subproblems.

2. Overlapping Subproblems:
The same subproblems are solved repeatedly in different parts of the problem refer to Overlapping Subproblems Property in Dynamic Programming.

Example:

Consider the problem of computing the Fibonacci series. To compute the Fibonacci number at index n, we need to compute the Fibonacci numbers at indices n-1 and n-2. This means that the subproblem of computing the Fibonacci number at index n-2 is used twice (note that the call for n - 1 will make two calls, one for n-2 and other for n-3) in the solution to the larger problem of computing the Fibonacci number at index n. 

You may notice overlapping subproblems highlighted in the second recursion tree for Nth Fibonacci diagram shown below.

Approaches of Dynamic Programming (DP)
Dynamic programming can be achieved using two approaches:

1. Top-Down Approach (Memoization):
In the top-down approach, also known as memoization, we keep the solution recursive and add a memoization table to avoid repeated calls of same subproblems.

Before making any recursive call, we first check if the memoization table already has solution for it.
After the recursive call is over, we store the solution in the memoization table.
2. Bottom-Up Approach (Tabulation):
In the bottom-up approach, also known as tabulation, we start with the smallest subproblems and gradually build up to the final solution.

We write an iterative solution (avoid recursion overhead) and build the solution in bottom-up manner.
We use a dp table where we first fill the solution for base cases and then fill the remaining entries of the table using recursive formula.
We only use recursive formula on table entries and do not make recursive calls.

How will Dynamic Programming (DP) Work?
Let us now see the above recursion tree with overlapping subproblems highlighted with same color. We can clearly see that that recursive solution is doing a lot work again and again which is causing the time complexity to be exponential. Imagine time taken for computing a large Fibonacci number.
Identify Subproblems: Divide the main problem into smaller, independent subproblems, i.e., F(n-1) and F(n-2)
Store Solutions: Solve each subproblem and store the solution in a table or array so that we do not have to recompute the same again.
Build Up Solutions: Use the stored solutions to build up the solution to the main problem. For F(n), look up F(n-1) and F(n-2) in the table and add them.
Avoid Recomputation: By storing solutions, DP ensures that each subproblem (for example, F(2)) is solved only once, reducing computation time.

Using Memoization Approach - O(n) Time and O(n) Space
To achieve this in our example we simply take an memo array initialized to -1. As we make a recursive call, we first check if the value stored in the memo array corresponding to that position is -1. The value - 1 indicates that we haven't calculated it yet and have to recursively compute it. The output must be stored in the memo array so that, next time, if the same value is encountered, it can be directly used from the memo array.  

Using Tabulation Approach - O(n) Time and O(n) Space
In this approach, we use an array of size (n + 1), often called dp[], to store Fibonacci numbers. The array is initialized with base values at the appropriate indices, such as dp[0] = 0 and dp[1] = 1. Then, we iteratively calculate Fibonacci values from dp[2] to dp[n] by using the relation dp[i] = dp[i-1] + dp[i-2]. This allows us to efficiently compute Fibonacci numbers in a loop. Finally, the value at dp[n] gives the Fibonacci number for the input n, as each index holds the answer for its corresponding Fibonacci number.

Using Space Optimised Approach - O(n) Time and O(1) Space
In the above code, we can see that the current state of any fibonacci number depends only on the previous two values. So we do not need to store the whole table of size n+1 but instead of that we can only store the previous two values. 

Common Algorithms that Use DP:
Longest Common Subsequence (LCS): This is used in day to day life to find difference between two files (diff utility)
Edit Distance : Checks how close to strings are. Can we be useful in implementing Google's did you mean type feature.
Longest Increasing Subsequence : There are plenty of variations of this problem that arise in real world.
Bellman–Ford Shortest Path: Finds the shortest path from a given source to all other vertices.
Floyd Warshall : Finds shortest path from every pair of vertices.
Knapsack Problem: Determines the maximum value of items that can be placed in a knapsack with a given capacity.
Matrix Chain Multiplication: Optimizes the order of matrix multiplication to minimize the number of operations.
Fibonacci Sequence: Calculates the nth Fibonacci number.
Advantages of Dynamic Programming (DP)
Dynamic programming has a wide range of advantages, including:

Avoids recomputing the same subproblems multiple times, leading to significant time savings.
Ensures that the optimal solution is found by considering all possible combinations.

Applications of Dynamic Programming (DP)
Dynamic programming has a wide range of applications, including:

Optimization: Knapsack problem, shortest path problem, maximum subarray problem
Computer Science: Longest common subsequence, edit distance, string matching
Operations Research: Inventory management, scheduling, resource allocation
'''


# memoization--> tend to store the value of subproblems in map or table

# recursion --> dynamic programming
# 3 steps->
# declare array of size n 
# store the answer
# if encounter then put it rather than solving it once again
# return
#1️⃣ Fibonacci series---checked✅ 
# 0 1 1 2 3 5 8 11
# use memoization
# store the solution of sub problem in an array
# if arr[num] not equal to -1 then return arr[num]
# tc O(n(as it only go till find all as after all search it dont repeat as it is already store))
# sc O(n)+O(n(call stack))
def fibonacciSeriesM(num:int,arr:list):
    if num<=1:return num
    if arr[num]!=-1:
        return arr[num]
    ans=fibonacciSeriesM(num-1,arr)+ fibonacciSeriesM(num-2,arr)
    arr[num]=ans
    return ans

# tabulation--> going from base case to required
# recursion --> tabulation(bottom up)
# firstly store the ans of base case then go to other
# tc O(n)
# sc  O(n)
def fibonacciSeriesT(num, arr):
    arr=[-1 for i in range(num+1)]
    arr[0]=0
    arr[1]=1
    for i in range(2,num+1):
        arr[i]=arr[i-1]+arr[i-2]
    return arr[num]        

# use var instead of arr
# tc O(n)
# sc  O(1)

def fibonacciSeriesTOptimise(num):
    prev1=0
    prev2=1
    for i in range(2,num+1):
        new=prev2
        prev2=prev1+prev2
        prev1=new
    return prev2        


# ⭐⭐⭐📝📝📝📖📖📖1D problems
# ⭐⭐⭐⭐⭐⭐⭐
# understand a dp problm
# how to find-->
# 1. count the no of ways
# 2. min or max
# when we have to try all possible ways



# (shortcut trick help in every prblm related to rec or dp)
# 1. try to represent the prblm in index, if it is not in arr than also try
# 2. do all possible stuffs on that index acc to prblm statement
# 3. if ques says count all stuff--> sum all stuffs
#   if ques says min of all stuff--> min of all stuffs
#   if ques says max of all stuff--> max of all stuffs


# 2️⃣Climbing Stairs | Learn How to Write 1D Recurrence Relations---checked✅ 
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# ~ similar to fibonacci
def climbingStairs(num):
    if num<=1:return 1
    left=climbingStairs(num-1)
    right=climbingStairs(num-2)
    return left+right


# memoization
def climbStairM(num,arr):
    if num<=1:return 1
    left=climbStairM(num-1,arr)
    if arr[num-2]!=-1:right=arr[num-2]
    else:right=climbStairM(num-2,arr)
    arr[num]=left+right
    return arr[num]

# tabulation
def climbStairT(num,arr):
    arr=[-1 for i in range(num+1)]
    arr[0]=1
    arr[1]=1
    for i in range(2,num+1):
        arr[i]=arr[i-1]+arr[i-2]
    return arr[num]


# 3️⃣ frog jump---checked✅ 
# , a frog starts from the first stair and wants to reach the last stair. From any stair i, the frog has two options: it can either jump to the (i+1)th stair or the (i+2)th stair. The cost of a jump is the absolute difference in height between the two stairs. Determine the minimum total cost required for the frog to reach the last stair.
#  arr= [20, 30, 40, 20]
# Output: 20
# why do greedy not work as there is substraction and in many case it doesn't work as we need to change the upcoming target if taken min or max acc to curr
# here we do the same as done in climbing stairs and fibonacci
# recursion
def frogJump(arr,num):
    if num==0:return 0
    left=frogJump(arr,num-1)+abs(arr[num]-arr[num-1])
    right=10**8
    if num>1:
        right=frogJump(arr,num-2)+abs(arr[num]-arr[num-2])
    return min(left,right)

# memoization
def frogJumpM(arr,num,newArr):
    if num==0:return 0
    if newArr[num]!=-1:return newArr[num]
    left=frogJumpM(arr,num-1,newArr)+abs(arr[num]-arr[num-1])
    right=10**8
    if num>1:
        right=frogJumpM(arr,num-2)+abs(arr[num]-arr[num-2])
    newArr[num]=min(left,right)
    return newArr[num]

# tabulation
def frogJumpT(arr,num,newArr):
    newArr[0]=0
    # newArr[1]=abs(arr[1]-arr[0])
    for i in range(1,num+1):
        fs=(newArr[i-1]+abs(arr[i]-arr[i-1]))
        ss=10**8
        if i>1:
            ss=newArr[i-2]+abs(arr[i]-arr[i-2])
        newArr[i]=min(fs,ss)
    return newArr[num]


# 4️⃣  frog K jump

# 5️⃣ Maximum Sum of Non-Adjacent Elements | House Robber---- checked✅ 
# here we have to make subsequences
# but not taking the adjacent one
# so we take care of if take the one then its next one should not be take here we have two case bcoz we dont need to take the adjacent one
# if there is that take after 2 then we have 3 cases
# here we do using recursion
# tc O(2**n)
# sc O(n)
def houseRobber(arr:list,i:int):
    if i<0:
        return 0
    if i==0:
        return arr[i]
    pick=arr[i]+houseRobber(arr,i-2)
    nonpick=0+houseRobber(arr,i-1)
    return max(pick,nonpick)

# memoization
# we store the values that we get, we use an array for that
# tc O(n)
# sc O(n)+O(n)
def houseRobberM(arr:list,i:int,newArr:list):
    if i==0:return arr[i]
    if i<0:return 0
    if newArr[i]!=-1:
        return newArr[i]
    pick=arr[i]+houseRobberM(arr,i-2,newArr)
    nonpick=0+houseRobberM(arr,i-1,newArr)
    newArr[i]=max(pick,nonpick)
    return newArr[i]

# tabulation
# base to required
def houseRobberT(arr:list):
    new=[-1 for i in range(len(arr))]
    new[0]=arr[0]
    for i in range(1,len(arr)):
        pick=arr[i]
        if i>1:
            pick=arr[i]+new[i-2]
        nonpick=0+new[i-1]
        new[i]=max(pick,nonpick)
    return new[i-1]

def houseRobberToptimise(arr:list):
    prev=arr[0]
    prev2=0
    for i in range(1,len(arr)):
        pick=arr[i]
        if i>1:
            pick=arr[i]+prev2
        nonpick=0+prev
        c=prev
        prev2=c
        prev=max(pick,nonpick)
    return prev


# 6️⃣ House Robber 2 -----✅checked
# here we can use the house robber but  we create two cases
# first one take first other take last
# if take first then dont take last and vice versa
# tc O(n+n)
# sc O(1)
# recursive
def houseRobberIIHelper(arr,i):
    if i<0:return 0
    if i==0:return arr[i]
    pick=arr[i]+houseRobberIIHelper(arr,i-2)
    nonpick=0+houseRobberIIHelper(i-1)
    return max(pick,nonpick)
def houseRobberII(arr):
    if len(arr)<3:return max(arr)
    a=houseRobberIIHelper(arr[:len(arr)-1:],len(arr)-1)
    b=houseRobberIIHelper(arr[1::],len(arr)-1)
    return max(a,b)

# memoization  are left
def houseRobberIIMHelper(arr,newArr,i):
    if i==0:return arr[i]
    if i<0:return 0
    if newArr[i]!=-1: return newArr[i]
    pick=arr[i]+houseRobberIIMHelper(arr,newArr,i-2)
    nonpick=0+houseRobberIIMHelper(arr,newArr,i-1)
    newArr[i]=max(pick,nonpick)
    return newArr[i]

def houseRobberIIM(arr):
    if len(arr)<3:return max(arr)
    a=houseRobberIIMHelper(arr[:len(arr)-1:],len(arr)-1)
    b=houseRobberIIMHelper(arr[1::],len(arr)-1)
    return max(a,b)


# ṭabulation
def houseRobberIITHelper(arr:list):
    new=[-1 for i in range(len(arr))]
    new[0]=arr[0]
    for i in range(1,len(arr)):
        pick=arr[i]
        if i>1:
            pick=arr[i]+new[i-2]
        nonpick=0+new[i-1]
        new[i]=max(pick,nonpick)
    return new[i-1]

def houseRobberIIT(arr):
    if len(arr)<3:return max(arr)
    a=houseRobberIITHelper(arr[:len(arr)-1:],len(arr)-1)
    b=houseRobberIITHelper(arr[1::],len(arr)-1)
    return max(a,b)

# tabulation Optimise
def houseRobberIIToptimiseHelper(arr):
    prev=arr[0]
    prev2=0
    for i in range(1,len(arr)):
        pick=arr[i]
        if i>1:
            pick=arr[i]+prev2
        nonpick=0+prev
        c=prev
        prev2=c
        prev=max(pick,nonpick)
    return prev

def rob(nums) -> int:
    if len(nums)<3:return max(nums)
    a=houseRobberIIToptimiseHelper(nums[:len(nums)-1:])
    b=houseRobberIIToptimiseHelper(nums[1::])
    return max(a,b)
# ------FINISH 1D PROBLEMS------
if __name__=="__main__":
    # print(fibonacciSeriesTOptimise(6))
    # arr=[-1 for i in range(7)]
    # print(fibonacciSeriesM(6,arr))
    # # print(arr)
    # arr=[-1 for i in range(4)]
    # print(climbStairT(3,arr))
    a= [20, 30, 40, 20]
    new=[-1 for i in range(len(a)+1)]
    # print(frogJumpM(a,len(a)-1,new))
    # a=[30, 20, 50, 10, 40]
    # print(frogJump(a,len(a)-1))
    # print(frogJumpT(a,len(a)-1,new))
    a= [1,2,3,1]
    new=[-1 for i in range(len(a)+1)]
    print(houseRobberM(a,3,new))
    print(houseRobberT(a))
    print(houseRobberToptimise(a))