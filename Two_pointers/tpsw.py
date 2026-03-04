# left to check----💀💀💀💀💀✅


'''
TWO POINTERS
The Two-Pointers Technique is a simple yet powerful strategy where you use two indices (pointers) that traverse a data structure - such as an array, list, or string - either toward each other or in the same direction to solve problems more efficiently

Two pointers is really an easy and effective technique that is typically used for Two Sum in Sorted Arrays, Closest Two Sum, Three Sum, Four Sum, Trapping Rain Water and many other popular interview questions.

When to Use Two Pointers:
-> Sorted Input : If the array or list is already sorted (or can be sorted), two pointers can efficiently find pairs or ranges. Example: Find two numbers in a sorted array that add up to a target.
-> Pairs or Subarrays : When the problem asks about two elements, subarrays, or ranges instead of working with single elements. Example: Longest substring without repeating characters, maximum consecutive ones, checking if a string is palindrome.
-> Sliding Window Problems : When you need to maintain a window of elements that grows/shrinks based on conditions. Example: Find smallest subarray with sum ≥ K, move all zeros to end while maintaining order.
-> Linked Lists (Slow–Fast pointers) : Detecting cycles, finding the middle node, or checking palindrome property. Example: Floyd’s Cycle Detection Algorithm (Tortoise and Hare).

Two-Pointer Technique - O(n) time and O(1) space
The idea of this technique is to begin with two corners of the given array. We use two index variables left and right to traverse from both corners.

Initialize: left = 0, right = n - 1
Run a loop while left < right, do the following inside the loop

Compute current sum, sum = arr[left] + arr[right]
If the sum equals the target, we’ve found the pair.
If the sum is less than the target, move the left pointer to the right to increase the sum.
If the sum is greater than the target, move the right pointer to the left to decrease the sum.


Sliding Window Technique

Sliding Window Technique is a method used to solve problems that involve subarray or substring or window.

Instead of repeatedly iterating over the same elements, the sliding window maintains a range (or “window”) that moves step-by-step through the data, updating results incrementally.
The main idea is to use the results of previous window to do computations for the next window.
Commonly used for problems like finding subarrays with a specific sum, finding the longest substring with unique characters, or solving problems that require a fixed-size window to process elements efficiently.


Using the Sliding Window Technique - O(n) Time and O(1) Space
We compute the sum of the first k elements out of n terms using a linear loop and store the sum in variable window_sum.
Then we will traverse linearly over the array till it reaches the end and simultaneously keep track of the maximum sum.
To get the current sum of a block of k elements just subtract the first element from the previous block and add the last element of the current block.

How to use Sliding Window Technique?
There are basically two types of sliding window:

1. Fixed Size Sliding Window:

The general steps to solve these questions by following below steps:

Find the size of the window required, say K.
Compute the result for 1st window, i.e. include the first K elements of the data structure.
Then use a loop to slide the window by 1 and keep computing the result window by window.
2. Variable Size Sliding Window:

The general steps to solve these questions by following below steps:

In this type of sliding window problem, we increase our right pointer one by one till our condition is true.
At any step if our condition does not match, we shrink the size of our window by increasing left pointer.
Again, when our condition satisfies, we start increasing the right pointer and follow step 1.
We follow these steps until we reach to the end of the array.
How to Identify Sliding Window Problems?
These problems generally require Finding Maximum/Minimum Subarray, Substrings which satisfy some specific condition.
The size of the subarray or substring ‘k’ will be given in some of the problems.
These problems can easily be solved in O(n2) time complexity using nested loops, using sliding window we can solve these in O(n) Time Complexity.
Required Time Complexity: O(n) or O(n log n)
Constraints: n <= 106 
'''

# 4 types of patterns
# 1️⃣ constant window 
# l and r --- var store the indexes
# increase r and l till r==len-1

# 2️⃣ longest subarray or substring where (a condition is provided)
# example
# longest subarray with sum<=k

# 1.brute force
# generate all arrays
# O(n²) O(N)
def longestSubarraySumK1(arr:list, k:int):
    m=-1
    l=len(arr)
    for i in range(l):
        for j in range(i,l):
            s=sum(arr[i:j+1])
            if s<=k:
                m=max(m,(j+1-i))
    return m


# 2. better solution
# using two ptrs and sliding window
# have two operations--> expand--for r and shrink for l
# assign both to r
# expand till end come and when the condition get false shrink
# tc O(2n) sc O(1)
def longestSubarraySumK2(arr:list,k:int):
    m=-1
    l=0
    r=0
    s=0
    ll=len(arr)
    while(r<ll ):
        s+=arr[r]
        while(s>k):
            s-=arr[l]
            l+=1
        if s<=k:
            m=max(m,r-l+1)
            
        r+=1
    return m


# 3. optimal one
# increase the r till get the max 
# when the s>k then dont update the r now
# move this constant sliding window further then if get s<k update the max and also increase r now
# tc O(n) sc O(1)
def longestSubarraySumK3(arr:list, k:int):
    n=len(arr)
    r=l=0
    s=0
    m=-1
    while(r<n):
        s+=arr[r]
        if s>k:
            s-=arr[l]
            l+=1  
        else:
            m=max(m,r-l+1)
        r+=1
           
    return m


# 3️⃣ No of subarrays where (a condition is provided)-- this type of problem can be solve by pattern 2
# example
# no of subarrays with sum==k-- for this its hard to know when to expand and when to shrink so calculate two things and subtract them---> (no of subarrays with sum<=k)-(no of subarrays with sum<=(k-1))


# 4️⃣ shorted / minimum window where (a condition is provided)
# here we use l and r 
# expand r till get the condition true if get then not expands the r shrink the l till condition satisfy and not further it satisfy return the res
if __name__=="__main__":
    arr=[2,5,1,7,10]
    k=14
    print(longestSubarraySumK3(arr,k))