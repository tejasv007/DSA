# LINKED LIST
'''
Docstring for DSA.linkedList.ll1
-- A data structure use to store data 
-- head never change
-- temp change 
-- in ll, the head is given only, we have to find who list acc to head
--A linked list is a type of linear data structure individual items are not necessarily at contiguous locations. The individual items are called nodes and connected with each other using links.

A node contains two things first is data and second is a link that connects it with another node.
The first node is called the head node and we can traverse the whole list using this head and next links.


Applications of Linked Lists in Computer Science
Data Structures: Implement stacks, queues, and adjacency lists in graphs.
Memory Management: Dynamic memory allocation using free blocks.
File & Directory Management: Maintain directories, symbol tables, and sparse matrices.
Mathematical Operations: Long integer arithmetic, polynomial manipulation.
Image & Signal Processing: Represent images, pixels, or signals.
Operating Systems: Task scheduling, process management.
Compilers: Symbol table management.

Real-World Applications
Image viewer, web browser, music player: Navigate previous/next items.
GPS & Robotics: Manage routes and robot control systems.
Undo/Redo functionality: Represent actions in applications.
File systems & simulations: Store hierarchical directories or system states.
Speech recognition & polynomial representation: Each node represents an element.
'''
# how to build node
class Node:
    def __init__(self,data, next=None):
        self.data=data
        self.next=next
    

# LINKED LIST 1
def linkedList1():
    e=Node(5)
    d=Node(4,e)
    c=Node(3,d)
    b=Node(2,c)
    a=Node(1,b)
    return a

# convert arr to linked list
def convertArrToLl(arr:list):
    if len(arr)==0:
        return None
    head=Node(arr[0])
    temp=head
    for i in range(1,len(arr)):
        new=Node(arr[i])
        temp.next=new
        temp=new
    return head


# traversal of a linked list
def traversal_ll(head:Node):
    temp= head
    while(temp!=None):
        print(temp.data)
        temp=temp.next
# length of linked list
def length_ll(head:Node):
    temp=head
    count=0
    while(temp!=None):
        temp=temp.next
        count+=1
    return count

# search an element in linked list
def search_ele(head:Node,n:int):
    temp=head
    count=1
    while(temp!=None):
        if temp.data==n:
            return count
        temp=temp.next
        count+=1
    return "not found"


if __name__=="__main__":
    a=[1,2,3,4,5]
    head=convertArrToLl(a)
    # traversal_ll(head)
    aa=5
    print(aa//10)
#     traversal_ll(a)
#     print(length_ll(a))
#     print(search_ele(a,2))
