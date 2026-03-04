'''
RECURSION
The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called a recursive function.

A recursive algorithm takes one step toward solution and then recursively call itself to further move. The algorithm stops once we reach the solution.
Since called function may further call itself, this process might continue forever. So it is essential to provide a base case to terminate this recursion process.

Need of Recursion?

Recursion helps in logic building. Recursive thinking helps in solving complex problems by breaking them into smaller subproblems.
Recursive solutions work as a a basis for Dynamic Programming and Divide and Conquer algorithms.
Certain problems can be solved quite easily using recursion like Towers of Hanoi (TOH), Inorder/Preorder/Postorder Tree Traversals, DFS of Graph, etc.
What is the base condition in recursion? 
A recursive program stops at a base condition. There can be more than one base conditions in a recursion. In the above program, the base condition is when n = 1.

How a particular problem is solved using recursion?

The idea is to represent a problem in terms of one or more smaller problems, and add one or more base conditions that stop the recursion.  

When does Stack Overflow error occur in recursion?
also called segmentation fault 
This continuous recursion consumes memory on the function call stack. If the system's memory is exhausted due to these unending function calls, a stack overflow error occurs.

What is the difference between direct and indirect recursion? 

A function is called direct recursive if it calls itself directly during its execution. In other words, the function makes a recursive call to itself within its own body.

An indirect recursive function is one that calls another function, and that other function, in turn, calls the original function either directly or through other functions. This creates a chain of recursive calls involving multiple functions, as opposed to direct recursion, where a function calls itself.

What is the difference between tail and non-tail recursion?

A recursive function is tail recursive when a recursive call is the last thing executed by the function.

How memory is allocated to different function calls in recursion? 

Recursion uses more memory to store data of every recursive call in an internal function call stack.

Whenever we call a function, its record is added to the stack and remains there until the call is finished.
The internal systems use a stack because function calling follows LIFO structure, the last called function finishes first.
When any function is called from main(), the memory is allocated to it on the stack. A recursive function calls itself, the memory for a called function is allocated on top of memory allocated to the calling function and a different copy of local variables is created for each function call. When the base case is reached, the function returns its value to the function by whom it is called and memory is de-allocated and the process continues.
What are the advantages of recursive programming over iterative programming? 

Recursion provides a clean and simple way to write code.
Some problems are inherently recursive like tree traversals, Tower of Hanoi, etc. For such problems, it is preferred to write recursive code. We can write such codes also iteratively with the help of a stack data structure. For example refer Inorder Tree Traversal without Recursion, Iterative Tower of Hanoi.
What are the disadvantages of recursive programming over iterative programming?

Note every recursive program can be written iteratively and vice versa is also true.

Recursive programs typically have more space requirements and also more time to maintain the recursion call stack.
Recursion can make the code more difficult to understand and debug, since it requires thinking about multiple levels of function calls..

Common Applications of Recursion
Tree and Graph Traversal: Used for systematically exploring nodes/vertices in data structures like trees and graphs.
Sorting Algorithms: Algorithms like quicksort and merge sort divide data into subarrays, sort them recursively, and merge them.
Divide-and-Conquer Algorithms: Algorithms like binary search break problems into smaller subproblems using recursion.
Fractal Generation: Recursion helps generate fractal patterns, such as the Mandelbrot set, by repeatedly applying a recursive formula.
Backtracking Algorithms: Used for problems requiring a sequence of decisions, where recursion explores all possible paths and backtracks when needed.
Memoization: Involves caching results of recursive function calls to avoid recomputing expensive subproblems.

'''

# all have tc-O(n) sc-O(n)-->call stack took memory
#1️⃣ basic recursion fn-->
# print name 5 times
# tc-O(n)
def recFn(c:int):
    if c== 5:
        return
    c+=1
    print("Bittu")
    recFn(c)

# tc-O(n)
def num1ton(n:int,i=1):
    if i==n+1:
        return
    print(i)
    i+=1
    num1ton(n,i)

# tc-O(n)
def numNto1(n:int):
    if n==0:
        return
    print(n)
    n-=1
    numNto1(n)

# 1 to n using backtracking
def from1toN(n:int,i:int):
    if i==0:
        return
    from1toN(n,i-1)
    print(i)

# n to 1 using backtracking
def fromNto1(i:int,n:int):
    if i==n+1:
        return
    fromNto1(i+1,n)
    print(i)


# parameterised way
def sum1toN(n:int,s:int):
    if n==0:
        print(s)
        return
    s+=n
    sum1toN(n-1,s)

# functional way
def sum1toN2(n:int):
    if n==1:
        return n
    return sum1toN2(n-1)+n

# factorial of a number
def fact(n:int):
    if n==0:
        return 1
    return fact(n-1)*n

# 2️⃣medium recursion fn-->
# reverse an array
# tc-O(n/2)
# using 2 pointers
def reverseArray(arr:list,f:int,s=0):
    if s>=f :
        print(arr)
        return 
    arr[s]=arr[s]^arr[f]
    arr[f]=arr[s]^arr[f]
    arr[s]=arr[s]^arr[f]
    reverseArray(arr,f-1,s+1)


# using 1 pointer
def reverseArray2(arr:list,i:int,n:int):
    if i>=n/2:
        print(arr)
        return
    arr[i]=arr[i]^arr[(n-i-1)]
    arr[((n-i-1))]=arr[i]^arr[(n-i-1)]
    arr[i]=arr[i]^arr[((n-i-1))]
    reverseArray2(arr,i+1,n)


# check a string is palindrome or not
def checkPalindrome(s:str,i:int,f:int):
    if i>=f:
        return True
    if s[i]!=s[f]:
        return False
    return checkPalindrome(s,i+1,f-1)


if __name__=="__main__":
    a=[1,2,3,4,5]
    # recFn(0)
    # num1ton(10)
    # numNto1(10)
    # # from1toN(10,10)
    # # fromNto1(1,10)
    # sum1toN(5,0)
    # print(sum1toN2(5))
    # print(fact(5))
    # print(swap(4,8))
    # reverseArray(a,len(a)-1)
    # reverseArray2(a,0,5)
    print(checkPalindrome("madem",0,4))
    