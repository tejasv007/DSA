'''
Introduction to Greedy Algorithms
Last Updated : 26 Jan, 2026
Greedy is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. Greedy algorithms are used for optimization problems. 

An optimization problem can be solved using Greedy if the problem has the following property: 

At every step, we can make a choice that looks best at the moment, and we get the optimal solution to the complete problem. 
Some popular Greedy Algorithms are Fractional Knapsack, Dijkstra’s algorithm, Kruskal’s algorithm, Huffman coding and Prim’s Algorithm
Also used to get an approximation for Hard optimization problems. For example, the Traveling Salesman Problem is an NP-Hard problem. A Greedy choice for this problem is to pick the nearest unvisited city from the current city at every step. These solutions don't always produce the best optimal solution but can be used to get an approximately optimal solution.
However, it's important to note that not all problems are suitable for greedy algorithms. They work best when the problem exhibits the following properties:

Greedy Choice Property: The optimal solution can be constructed by making the best local choice at each step.
Optimal Substructure: The optimal solution to the problem contains the optimal solutions to its sub-problems.
How does a Greedy Algorithm work?
Greedy Algorithm solve optimization problems by making the best local choice at each step in the hope of finding the global optimum. It's like taking the best option available at each moment, hoping it will lead to the best overall outcome.

Here's how it works:

Start with the initial state of the problem.
Consider all the options available at that specific moment.
Choose the option that seems best at that moment, regardless of future consequences. This is the "greedy" part - you take the best option available now, even if it might not be the best in the long run.
Move to the new state based on your chosen option. This becomes your new starting point for the next iteration.
Repeat steps 2-4 until you reach the goal state or no further progress is possible.

The greedy algorithm is not always the optimal solution for every optimization problem, as shown in the example below.

When using the greedy approach to make change for the amount 20 with the coin denominations [18, 1, 10], the algorithm starts by selecting the largest coin value that is less than or equal to the target amount. In this case, the largest coin is 18, so the algorithm selects one 18 coin. After subtracting 18 from 20, the remaining amount is 2.
At this point, the greedy algorithm chooses the next largest coin less than or equal to 2, which is 1. It then selects two 1 coins to make up the remaining amount. So, the greedy approach results in using one 18 coin and two 1 coins.
However, the greedy approach fails to find the optimal solution in this case. Although it uses three coins, a better solution would have been to use two 10 coins, resulting in a total of only two coins (10 + 10 = 20).

Characteristics of Greedy Algorithm
Here are the characteristics of a greedy algorithm:

Greedy algorithms are simple and easy to implement.
They are efficient in terms of time complexity, often providing quick solutions. Greedy Algorithms are typically preferred over Dynamic Programming for the problems where both are applied. For example, Jump Game problem and Single Source Shortest Path Problem (Dijkstra is preferred over Bellman Ford where we do not have negative weights).
These algorithms do not reconsider previous choices, as they make decisions based on current information without looking ahead.
These characteristics help to define the nature and usage of greedy algorithms in problem-solving.

Greedy Algorithms General Structure

A greedy algorithm solves problems by making the best choice at each step. Instead of looking at all possible solutions, it focuses on the option that seems best right now.

Problem structure:

Most of the problems where greedy algorithms work follow these two properties:

1). Greedy Choice Property:- This property states that choosing the best possible option at each step will lead to the best overall solution. If this is not true, a greedy approach may not work.

2). Optimal Substructure:- This means that you can break the problem down into smaller parts, and solving these smaller parts by making greedy choices helps solve the overall problem.

How to Identify Greedy Problems:
There are two major ways to detect greedy problems -

1). Can we break the problem into smaller parts? If so, and solving those parts helps us solve the main problem, it probably would be solved using greedy approach. For example - In activity selection problem, once we have selected a activity then remaining subproblem is to choose those activities that start after the selected activity.

2). Will choosing the best option at each step lead to the best overall solution? If yes, then a greedy algorithm could be a good choice. For example - In Dijkstra’s shortest path algorithm, choosing the minimum-cost edge at each step guarantees the shortest path.

Difference between Greedy and Dynamic Programming:
1). Greedy algorithm works when the problem has Greedy Choice Property and Optimal Substructure, Dynamic programming also works when a problem has optimal substructure but it also requires Overlapping Subproblems.

2). In greedy algorithm each local decision leads to an optimal solution for the entire problem whereas in dynamic programming solution to the main problem depends on the overlapping subproblems.

Some common ways to solve Greedy Problems:
1). Sorting

Job Sequencing:- In order to maximize profits, we prioritize jobs with higher profits. So we sort them in descending order based on profit. For each job, we try to schedule it as late as possible within its deadline to leave earlier slots open for other jobs with closer deadlines.

Activity Selection:- To maximize the number of non-overlapping activities, we prioritize activities that end earlier, which helps us to select more activities. Therefore, we sort them based on their end times in ascending order. Then, we select the first activity and continue adding subsequent activities that start after the previous one has ended.

Disjoint Intervals:- The approach for this problem is exactly similar to previous one, we sort the intervals based on their start or end times in ascending order. Then, select the first interval and continue adding next intervals that start after the previous one ends.

Fractional Knapsack:- The basic idea is to calculate the ratio profit/weight for each item and sort the item on the basis of this ratio. Then take the item with the highest ratio and add them as much as we can (can be the whole element or a fraction of it).

Kruskal Algorithm:- To find the Minimum Spanning Tree (MST), we prioritize edges with the smallest weights to minimize the overall cost. We start by sorting all the edges in ascending order based on their weights. Then, we iteratively add edges to the MST while ensuring that adding an edge does not form a cycle.

2). Using Priority Queue or Heaps

Dijkstra Algorithm:- To find the shortest path from a source node to all other nodes in a graph, we prioritize nodes based on the smallest distance from the source node. We begin by initializing the distances and using a min-priority queue. In each iteration, we extract the node with the minimum distance from the priority queue and update the distances of its neighboring nodes. This process continues until all nodes have been processed, ensuring that we find the shortest paths efficiently.

Connect N ropes:- In this problem, the lengths of the ropes picked first are counted multiple times in the total cost. Therefore, the strategy is to connect the two smallest ropes at each step and repeat the process for the remaining ropes. To implement this, we use a min-heap to store all the ropes. In each operation, we extract the top two elements from the heap, add their lengths, and then insert the sum back into the heap. We continue this process until only one rope remains.

Huffman Encoding:- To compress data efficiently, we assign shorter codes to more frequent characters and longer codes to less frequent ones. We start by creating a min-heap that contains all characters and their frequencies. In each iteration, we extract the two nodes with the smallest frequencies, combine them into a new node, and insert this new node back into the heap. This process continues until there is only one node left in the heap.

3). Arbitrary

Minimum Number of Jumps To Reach End:- In this problem we maintain a variable to store maximum reachable position at within the current jump's range and increment the jump counter when the current jump range has been traversed. We stop this process when the maximum reachable position at any point is greater than or equal to the last index value.

Applications, Advantages and Disadvantages of Greedy Algorithms
Last Updated : 12 Dec, 2024
Greedy is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. Greedy algorithms are used for optimization problems. 

Table of Content

Applications of Greedy Algorithms, Advantages of Greedy Algorithms,Disadvantages of the Greedy Approach

Applications of Greedy Algorithms

We use Greedy Algorithms in our day to day life to find minimum number of coins or notes for a given amount. We fist begin with largest denomination and try to use maximum number of the largest and then second largest and so on.
Dijkstra's shortest path algorithm: Finds the shortest path between two nodes in a graph.
Kruskal's and Prim's minimum spanning tree algorithm: Finds the minimum spanning tree for a weighted graph. Minimum Spanning Trees are used in Computer Networks Designs and have many real world applications
Huffman coding: Creates an optimal prefix code for a set of symbols based on their frequencies.
Fractional knapsack problem: Determines the most valuable items to carry in a knapsack with a limited weight capacity.
Activity selection problem: Chooses the maximum number of non-overlapping activities from a set of activities.
Job Sequencing and Job Scheduling Problems.
Finding close to the optimal solution for NP-Hard problems like TSP. ide range of network design problems, such as routing, resource allocation, and capacity planning.
Machine learning: Greedy algorithms can be used in machine learning applications, such as feature selection, clustering, and classification. In feature selection, greedy algorithms are used to select a subset of features that are most relevant to a given problem. In clustering and classification, greedy algorithms can be used to optimize the selection of clusters or classes
Image processing: Greedy algorithms can be used to solve a wide range of image processing problems, such as image compression, denoising, and segmentation. For example, Huffman coding is a greedy algorithm that can be used to compress digital images by efficiently encoding the most frequent pixels.
Combinatorics optimization: Greedy algorithms can be used to solve combinatorial optimization problems, such as the traveling salesman problem, graph coloring, and scheduling. Although these problems are typically NP-hard, greedy algorithms can often provide close-to-optimal solutions that are practical and efficient.
Game theory: Greedy algorithms can be used in game theory applications, such as finding the optimal strategy for games like chess or poker. In these applications, greedy algorithms can be used to identify the most promising moves or actions at each turn, based on the current state of the game.

Advantages of Greedy Algorithms

Simple and easy to understand: Greedy algorithms are often straightforward to implement and reason about.
Efficient for certain problems: They can provide optimal solutions for specific problems, like finding the shortest path in a graph with non-negative edge weights.
Fast execution time: Greedy algorithms generally have lower time complexity compared to other algorithms for certain problems.
Intuitive and easy to explain : The decision-making process in a greedy algorithm is often easy to understand and justify.
Can be used as building blocks for more complex algorithms: Greedy algorithms can be combined with other techniques to design more sophisticated algorithms for challenging problems.

Disadvantages of the Greedy Approach

Not always optimal: Greedy algorithms prioritize local optima over global optima, leading to suboptimal solutions in some cases.
Difficult to prove optimality: Proving the optimality of a greedy algorithm can be challenging, requiring careful analysis.
Sensitive to input order: The order of input data can affect the solution generated by a greedy algorithm.
Limited applicability: Greedy algorithms are not suitable for all problems and may not be applicable to problems with complex constraints.

'''
# 1️⃣ ASSIGN COOKIES
# parent have n child and m cookies with size 
# find the max no of child which parent can satisfy by cookies
# cookie cant be reuse, cookie size>= child greed
# greed=[1,5,3,3,4] s=[4,2,1,2,1,3]
# here we sort out both the array
# then use two ptrs l in greed and another r for s
# when greed[l]=<s[r] move l+=1 otherwise move r whole the time 
# when the r reach out of index then the ans be l
# tc O(n+2nlogn) sc O(1)
def assignCookies(greed:list,s:list):
    greed.sort()
    s.sort()
    i=0;j=0
    while(j<len(s) and i<len(greed)):
        if s[j]>=greed[i]:
            i+=1
        j+=1
    return i


# 2️⃣ LEMONADE CHANGE
# bills=[5,5,5,10,20]
# every lemonade costs 5 , there are 3 type of currency ie 5, 10,20. bills are the amt given by customer to use we should give them change if it exceed 5. if its not possible to change return false
# take two var 5 and 10, extend both according to the bills
# the bills is in sorted manner
# tc O(n)
def lemonadeChange(bills:list):
    c5=0
    c10=0
    for i in range(bills):
        if i==5:
            c5+=1
        elif i==10:
            if c5>0:
                c5-=1
                c10+=1
            else:return False
        else:
            if c10>0 and c5>0:
                c10-=1
                c5-=1
            elif c5>2:
                c5-=3
            else:
                return False
    return True

# 3️⃣SHORTEST JOB FIRST
# scheduling policy that selects the waiting process with the smallest execution time to execute next
# bs=[4,3,7,1,2] ans= 4
# calculate avg waiting time till all process get complete using sjf theorem
# given execution time of process, index 0 is process 1
# for eg--> we first run the p4 as it execution time is 1 so the waiting time for p4 is 0 then run p5 as it execution time is 2 but it waited for 1 sec for waiting time for p5 is 1

# here we sort the array 
# here we use two var prev and ans
# prev store the waiting time while ans add on the waiting time
# tc O(n+ nlogn)
def shortestJobFirst(arr:list):
    arr.sort()
    prev=0
    ans=0
    for i in arr:
        ans+=prev
        prev+=i
        
    return ans//len(arr)


# 4️⃣JUMP GAME I
# arr=[2,3,1,0,4] ans true
# arr=[3,2,1,0,4] ans false
# given an arr in which  the element tell a person can jump up how many further elements, can at most the no only 
# for eg if person on index 0 can go to 1 or 2 indexes not further
# return true if person can reach to last element else false
#  here we use a var maxInd which calculate till which index we can go with the curr index
# that is when we are i 0 we can go to 2 index then we are i 1 we go to index 4 which is greater than 2 so maxInd =4 .....
# tc O(n)
def jumoGameI(arr:list):
    maxInd=0
    i=0
    while( i<len(arr)):
        if i>maxInd:return False#iiiiiiimmmpppp
        maxInd=max(maxInd,arr[i]+i)
        i+=1
    return True

# 5️⃣JUMP GAME II
# similar to 4 one but here we reach to end anyhow
# find the min step to take to reach the last index
# a=[2,3,1,4,1,1,1,2] ans 3
# tc O(n)^n sc O(n)
def jumpGameII(i:int,s:int,arr:list,m=123456):
    if i>=(len(arr)-1):
        return s
    for j in range(1,arr[i]+1):
        m=min(m,jumpGameII(j+i,s+1,arr,m))
    return m 
    
# use of dynamic programming------💀💀💀💀💀do when you complete dp
# tc O(n)² sc O(n)²

# optimal
# not understand💀💀💀💀💀💀  -- have error---⚡⚡⚡
# tc O(n) sc O(1)
def jumpGameII1(arr:list):
    jumps=0
    l=0
    r=0
    n=len(arr)
    while(r<n-1):
        far=0
        for i in range(l,r):
            far=max(i+arr[i],far)
        l=r+1
        r=far 
        jumps+=1
    return jumps

if __name__=="__main__":
    greed=[1,5,3,3,4] 
    s=[4,2,1,2,1,3]
    # print(assignCookies(greed,s))
    b=[4,3,7,1,2] 
    # print(shortestJobFirst(b))
    arr=[2,3,1,0,4]
    arr2=[3,2,1,0,4]
    a=[2,3,1,4,1,1,1,2]
    # print(jumoGameI(arr))
    # print(jumoGameI(arr2))

    print(jumpGameII(0,0,a))
    # print(jumpGameII1(a))