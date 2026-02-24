'''
A Stack is a linear data structure that follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out). LIFO implies that the element that is inserted last, comes out first and FILO implies that the element that is inserted first, comes out last.

It behaves like a stack of plates, where the last plate added is the first one to be removed. Think of it this way:

Pushing an element onto the stack is like adding a new plate on top.

Popping an element removes the top plate from the stack.

LIFO(Last In First Out) Principle
The LIFO principle means that the last element added to a stack is the first one to be removed.

New elements are always pushed on top.
Removal (pop) also happens only from the top.
This ensures a strict order: last in → first out.
Real-world examples of LIFO:

Stack of plates – The last plate placed on top is the first one you pick up.
Stack of books – Books are added and removed from the top, so the last book placed is the first one taken.
Basic Terminologies of Stack
Top: The position of the most recently inserted element. Insertions (push) and deletions (pop) are always performed at the top.
Size: Refers to the current number of elements present in the stack.
Types of Stack:
Fixed Size Stack
A fixed size stack has a predefined capacity.
Once it becomes full, no more elements can be added (this causes overflow).
If the stack is empty and we try to remove an element, it causes underflow.
Typically implemented using a static array.
Example: Declaring a stack of size 10 using an array.

Dynamic Size Stack
A dynamic size stack can grow and shrink automatically as needed.
If the stack is full, its capacity expands to allow more elements.
As elements are removed, memory usage can shrink as well.
Can be implemented using:
-> Linked List → grows/shrinks naturally.
-> Dynamic Array (like vector in C++ or ArrayList in Java) → resizes automatically.
Example: Stack implementation using linked list or resizable array.

Note: We generally use dynamic stacks in practice, as they can grow or shrink as needed without overflow issues.

Common Operations on Stack:
In order to make manipulations in a stack, there are certain operations provided to us.

push() to insert an element into the stack.
pop() to remove an element from the stack.
top() Returns the top element of the stack.
isEmpty() returns true if stack is empty else false.
size() returns the size of the stack.


APPLICATION
A Stack is a linear data structure in which the insertion of a new element and removal of an existing element takes place at the same end represented as the top of the stack.

This property of stack is used to solve a lot of interesting problems:

Next Greater, Previous Greater.
Next Smaller, Previous Smaller.
Largest Area in a Histogram
Stock Span Problems
Stack applications are diverse, representing a dynamic data structure with various uses, some of which are mentioned below:

1. Function Calls

Stacks manage the "active" functions in a program. When a function is called, its execution state is pushed onto the stack; when it finishes, it is popped to return control to the caller.

Example: In a program where Main() calls CalculateBill(), which then calls ApplyDiscount(), the stack ensures that once the discount is calculated, the program knows exactly how to jump back into the middle of the billing function.
2. Recursion

Since recursion is essentially a function calling itself, the stack stores a "snapshot" of each call (including local variables) so the program doesn't lose its place.

Example: In calculating a Factorial (n!), the stack stores the value of n for every nested call. For 3!, it pushes 3, then 2, then 1. Once it hits the base case, it pops them off to multiply them in reverse order (1 x 2 x 3).
3. Expression Evaluation

Stacks are used by compilers and calculators to handle the order of operations without needing complex parentheses.

Example: To solve the postfix expression "3 4 + 5 *", a stack pushes 3 and 4, pops them to add them (resulting in 7), pushes the 7 back, then pushes 5, and finally pops both to multiply them for a total of 35.
4. Syntax Parsing

Stacks are perfect for "balancing" symbols. They ensure that every opening bracket has a corresponding closing bracket in the correct order.

Example: An IDE uses a stack to check code like " if (a > b) { print(c); } " . It pushes ' ( ' and ' { ' onto the stack as it sees them. When it encounters ' ) ' and ' } ' , it pops the top element to ensure the types match. If the stack is empty at the end, the syntax is valid.
5. Memory Management

The "Stack" is a specific region of RAM used for automatic variable allocation. It is incredibly fast because it only allocates and deallocates memory in a strict Last-In, First-Out (LIFO) order.

Example: When you declare " int x = 10; " inside a Java or C++ function, that memory is allocated on the Stack. As soon as the function's closing brace ' } ' is reached, that memory is automatically reclaimed by the system without needing manual cleanup.
Advantages:
Time & Memory Efficiency: Push and pop operations on a stack can be performed in constant time-O(1), enabling efficient data access, they are memory-efficient because they only store pushed elements, compared to other data structures.
Last-In, First-Out (LIFO): Stacks follow the LIFO principle, ensuring the last element added is the first one removed. This behavior is useful in scenarios like function calls and expression evaluation.
Disadvantages:
Limited access: Elements in a stack can only be accessed from the top, which makes it difficult to retrieve or modify elements in the middle.
Potential for overflow: Pushing more elements onto a stack than it can hold results in an overflow error, leading to data loss.

STACK IN PYTHON

Stack in Python
Last Updated : 11 Dec, 2025
A stack is a linear data structure that follows the Last-In/First-Out (LIFO) principle, also known as First-In/Last-Out (FILO). This means that the last element added is the first one to be removed. In a stack, both insertion and deletion happen at the same end, which is called the top of the stack.
Python does not have a built-in stack type, but stacks can be implemented in different ways using different data structures, let's look at some of the implementations:

1. Using a List
Python lists provide built-in methods that make them suitable for stack operations.
The append () method adds an element to the end of the list.
The pop () method removes and returns the last element from the list.
These operations allow a list to directly support stack-like behavior.

2. Using collections.deque
Python’s collections module provides a deque (double-ended queue) for efficient insertions and deletions.
The append () method adds an element to the right end of the deque.
The pop () method removes and returns the element from the right end.
Since deque is optimized for fast appends and pops, it is often preferred over lists for stack implementation.
'''

# building stack using arrays
# all method take O(1)
# Sc-O(n)--- if we use arrays otherwise not
class Stack:
    def __init__(self,n:int):
        self.a=[0 for i in range(n)]
        self.top=-1
        self.s=n
    def push(self,x:int):
        if self.top+1==self.s:
            return "full"
        self.a[self.top+1]=x
        self.top+=1

    def pop(self):
        if self.top==-1:
            return "not possible"
        self.top-=1
        return "popped"
    def Top(self):
        if self.top==-1:
            return "empty"
        return self.a[self.top]
    
    def size(self):
        if self.top==-1:
            return "empty"
        return self.top+1
    

# building stack using linkedlist
# import sys
# print(sys.path)
from linkedList.ll1 import *
# ----for this use --->python -m Stack.stack1

class StackLL:
    def __init__(self):
        self.head=Node()
        self.s=0

    def push(self,x:int):
        temp=Node(x,self.head)
        self.head=temp
        self.s+=1
    
    def pop(self):
        self.head=self.head.next
        self.s-=1

    def top(self):
        return self.head.data
    
    def size(self):
        return self.s



# implement stack using queue
from Queue.queue1 import *
from collections import deque
class StackQ:
    def __init__(self):
        self.obj=deque()
        
    def Push(self,x:int):#use O(n)
        s=len(self.obj)
        self.obj.append(x)
        for i in range(s):
            self.obj.append(self.obj.popleft())

    def Pop(self):
        self.obj.popleft()
        

    def Size(self):
        return len(self.obj)

    def Top(self):
        return self.obj[0]



if __name__=="__main__":
    # a=Stack(10)
    # a.push(1)
    # a.push(2)
    # a.push(3)
    # a.push(4)
    # a.pop()
    # print(a.Top())
    # # print(a.size())
    # a2=StackLL()
    # a2.push(1)
    # a2.push(2)
    # a2.push(3)
    # a2.push(4)
    # a2.pop()
    # print(a2.size())
    # print(a2.top())
    a3=StackQ()
    a3.Push(1)
    a3.Push(2)
    print(a3.Top())
    print(a3.Size())
    a3.Push(3)
    a3.Push(4)
    a3.Pop()
    print(a3.Top())


