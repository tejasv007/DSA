'''
Queue is a linear data structure that follows FIFO (First In First Out) Principle, so the first element inserted is the first to be popped out.

It is an ordered list in which insertions are done at one end which is known as the rear and deletions are done from the other end known as the front.
A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first. 
The difference between stack and queue is in removing an element. In a stack we remove the item that is most recently added while in a queue, we remove the item that is least recently added.
FIFO Principle in Queue:

FIFO Principle states that the first element added to the Queue will be the first one to be removed or processed. So, Queue is like a line of people waiting to purchase tickets, where the first person in line is the first person served. (i.e. First Come First Serve).
Basic Terminologies of Queue
Front: Position of the entry in a queue ready to be served, that is, the first entry that will be removed from the queue, is called the front of the queue. It is also referred as the head of the queue.
Rear: Position of the last entry in the queue, that is, the one most recently added, is called the rear of the queue. It is also referred as the tail of the queue.
Size: Size refers to the current number of elements in the queue.
Capacity: Capacity refers to the maximum number of elements the queue can hold.
Types of Queues
Queue data structure can be classified into 3 types:
1. Simple Queue
A simple queue follows the FIFO (First In, First Out) principle.

Insertion is allowed only at the rear (back).
Deletion is allowed only from the front.
Can be implemented using a linked list or a circular array.
When an array is used, we often prefer a circular queue, which is mainly an efficient array implementation of a simple queue. It efficiently utilizes memory by reusing the empty spaces left after deletion, avoiding wastage that occurs in a normal linear array implementation..

2. Double-Ended Queue (Deque)
In a deque, insertion and deletion can be performed from both ends.

3. Priority Queue
A queue where each element is assigned a priority, and deletion always happens based on priority (not just position).

Queue Operations
Enqueue: Adds an element to the end (rear) of the queue. If the queue is full, an overflow error occurs.
Dequeue: Removes the element from the front of the queue. If the queue is empty, an underflow error occurs.
Peek/Front: Returns the element at the front without removing it.
Size: Returns the number of elements in the queue.
isEmpty: Returns true if the queue is empty, otherwise false.
isFull: Returns true if the queue is full, otherwise false.

APPLICATION
A Queue is a linear data structure. This data structure follows a particular order in which the operations are performed. The order is First In First Out (FIFO).

Network: In a network, a queue is used in devices such as a router or a switch. another application of a queue is a mail queue which is a directory that stores data and controls files for mail messages.
Job Scheduling: The computer has a task to execute a particular number of jobs that are scheduled to be executed one after another. These jobs are assigned to the processor one by one which is organized using a queue.
Shared resources: Queues are used as waiting lists for a single shared resource.
Real-time application of Queue:

Working as a buffer between a slow and a fast device. For example keyboard and CPU, and two devices on network.
ATM Booth Line
Ticket Counter Line
CPU task scheduling
Waiting time of each customer at call centers.
Advantages of Queue:

Queues are useful when a particular service is used by multiple consumers.
Queues are fast in speed for data inter-process communication.
Queues can be used for the implementation of other data structures.
Disadvantages of Queue:

The operations such as insertion and deletion of elements from the middle are time consuming.
In a classical queue, a new element can only be inserted when the existing elements are deleted from the queue.
Searching an element takes O(N) time.
Maximum size of a queue must be defined prior in case of array implementation.

QUEUE IN PYTHON
Queue is a linear data structure that stores items in a First In First Out (FIFO) manner. The item that is added first will be removed first. Queues are widely used in real-life scenarios, like ticket booking, or CPU task scheduling, where first-come, first-served rule is followed.
There are various ways to implement a queue in Python by following ways:

1. Using list - Inefficient
Lists can be used as queues, but removing elements from front requires shifting all other elements, making it O(n).
2. Using collections.deque - Efficient
deque (double-ended queue) is preferred over a list for queues because both append() and popleft() run in O(1) time.
3. Using queue.Queue - Efficient and Thread Safe
Python’s queue module provides a thread-safe FIFO queue. You can specify a maxsize. Key Methods are:

put(item) / put_nowait(item) – Add an element.
get() / get_nowait() – Remove an element.
empty() – Check if the queue is empty.
full() – Check if the queue is full.
qsize() – Get current size of the queue.

'''

# building queue manual using arrays
class Queue:
    def __init__(self,n:int):
        self.a=[0 for i in range(n)]
        self.f=-1
        self.l=-1
        self.s=0
        self.n=n
    def push(self,x:int):
        if self.s==self.n:
            return "full"
        if self.s==0:
            self.f=0
            self.l=0
        else:
            self.f=(self.f+1)%self.n
        self.a[self.f]=x
        self.s+=1


    def pop(self):
        if self.s==0:
            return "empty"
        if self.l==self.f:
            e=a[self.l]
            self.l=-1
            self.f=-1
        else:
            e=a[self.l]
            self.l=(self.l+1)%self.s
        self.s-=1
        return e
    
    def top(self):
        if self.s==0:
            return "empty"
        return self.a[self.l]
    
    def size(self):
        return self.s
    

# building queue manual using linkedlist
from linkedList.ll1 import *
# for this use python -m Queue.queue1
class QueueLL:
    def __init__(self):
        self.head=Node()
        self.s=0
        self.temp=Node()

    def push(self,x:int):
        new=Node(x)
        if self.head==None:
            self.head=new
            self.temp=new
            return
        self.temp.next=new
        self.temp=new
        self.s+=1

    def pop(self):
        if self.s==0:
            return "empty"
        new=self.head
        self.head=self.head.next
        new.next=None
        self.s-=1

    def top(self):
        if self.head==None:
            return "empty"
        return self.head.data
    def size(self):
        return self.s


# implement queue using stack
# TC-O(2n)--- approach 1
class QueueS:
    def __init__(self):
        self.obj=list()
    
    def push(self,x:int):#use O(2n)
        s=len(self.obj)
        new=[]
        for i in range(s):
            new.append(self.obj.pop())
        self.obj.append(x)
        for i in range(s):
            self.obj.append(new.pop())

    def pop(self):
        return self.obj.pop()
    def top(self):
        return self.obj[len(self.obj)-1]
    
    def size(self):
        return len(self.obj)

# if have more push operation than pop and top
class QueueS2:
    def __init__(self):
        self.obj=[]
        self.obj2=[]
    def push(self,x:int):
        self.obj.append(x)
    
    def pop(self):#use O(n)
        if len(self.obj2) !=0:
            self.obj2.pop()
        else:
            for i in range(len(self.obj)):
                self.obj2.append(self.obj.pop())
    
    def top(self):#use O(n)
        if len(self.obj2) !=0:
            return self.obj2[len(self.obj2)-1]
        else:
            for i in range(len(self.obj)):
                self.obj2.append(self.obj.pop())
        return self.obj2[len(self.obj2)-1]

if __name__=="__main__":
    # a=Queue(10)
    # a.push(1)
    # a.push(2)
    # # a.pop()
    # print(a.size())
    # print(a.top())
    # a2=QueueLL()
    # a2.push(1)
    # # a2.push(2)
    # # a2.push(3)
    # # a2.push(4)
    # print(a2.size())

    # a2.pop()
    # # print(a2.size())
    # print(a2.top())
    a3=QueueS2()
    a3.push(1)
    a3.push(2)
    a3.push(3)
    a3.push(4)
    print(a3.top())
    a3.pop()
    print(a3.top())

