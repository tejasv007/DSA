# left to check✔️✔️✔️⌛---already in notes
'''
Docstring for linkedList.dll1
Double linked list
-->linked list consist of nodes, where each node contains data field anf two pointers: one pointing to next and one to previous
--> can traverse in both forward and backward direction
APPLICATION
--> browse history--> navigating back and forward between pages
--> undo/ redo functionality
--> music player playlist 
'''

from ll1 import traversal_ll
# Representation of dll
class doublyNode:
    def __init__(self,data:int, prev=None, next=None):
        self.data=data
        self.prev=prev
        self.next=next


# convert a array into doubly linked list 
# simply apply a loop over the elements of the array
# 1. firstly made a head node 
# 2. assign prev to new node
# 3. prev next is new and new prev to prev 
# 4. repeat 2 and 3
def convertArrToDll(arr:list):
    prev=None
    next=None
    head=None
    for i in range(len(arr)):
        new=doublyNode(arr[i],prev,next)
        if prev!=None:
            prev.next=new
        prev=new
        if i==0:
            head=new
    return head

        
# DELETION
# deletion of node from head
def deletionHead(head:doublyNode):
    if head==None or head.next==None:
        return None
    temp=head
    head=head.next
    temp.next=None
    head.prev=None
    return head


# deletion of node of tail
def deletionTail(head:doublyNode):
    if head==None or head.next==None:
        return None
    temp=head
    
    while(temp.next!=None):
        temp=temp.next
    back=temp.prev
    back.next=None
    temp.prev=None
    return head


# deletion of kth node
def deletionKth(head:doublyNode,k:int):
    if head==None or head.next==None:
        return None
    temp=head
    if k==1:
        return deletionHead(head)
    c=1
    while(temp!=None):
        if k==c:
            break
        temp=temp.next
        c+=1
    back=temp.prev
    if temp.next==None:
        back.next=None
        temp.prev=None
    else:
        back.next=temp.next
        temp.next.prev=back
        temp.prev=None
        temp.next=None
    return head

# deletion of node of given value---(node!=head)
# (here we take node as int, if it is node then its not possible)
def deletionNode(head:doublyNode, val:int):
    if head==None or head.next==None:
        return None
    temp=head
    if head.data==val:
        return deletionHead(head)
    while(temp!=None):
        if val==temp.data:
            break
        temp=temp.next
    back=temp.prev
    if temp.next==None:
        back.next=None
        temp.prev=None
    else:
        back.next=temp.next
        temp.next.prev=back
        temp.prev=None
        temp.next=None
    return head


# INSERTION
# ------------AFTER-------------------------
# insertion of after head in dll
def insertionAfHead(head:doublyNode,val:int):
    new=doublyNode(val,head)
    if head==None :
        return new
    if head.next==None:
        head.next=new
        return head
    temp=head.next
    new.next=temp
    temp.prev=new
    head.next=new
    return head
    
# insertion of after tail in dll
def insertionAfEnd(head:doublyNode, val:int):
    if head==None or head.next==None:
        return None
    temp=head
    while(temp.next!=None):
        temp=temp.next
    new=doublyNode(val,temp)
    temp.next=new
    return head


# insertion of ele after kth node
def insertionAfKth(head:doublyNode,k:int,val:int):
    if k==1:
        return insertionAfHead(head,val)
    temp=head
    c=1
    while(temp!=None):
        if c==k:
            break
        c+=1
        temp=temp.next
    if temp==None:
        return head
    if temp.next==None:
        new=doublyNode(val,temp)
        temp.next=new
        return head
    front=temp.next
    new=doublyNode(val,temp,front)
    temp.next=new
    front.prev=new
    return head

# insertion of node after node
def insertionAfNode(head:doublyNode,node:int,val:int):
    if head==None:
        new=doublyNode(val)
        return new
    if head.data==node:
        return insertionAfHead(head,val)
    temp=head
    while(temp!=None):
        if temp.data==node:
            break
        temp=temp.next
    if temp==None:
        return head
    if temp.next==None:
        new=doublyNode(val,temp)
        temp.next=new
        return head
    front=temp.next
    new=doublyNode(val,temp,front)
    temp.next=new
    front.prev=new
    return head   


# ------------------BEFORE-------------
# insertion of node before head in dll
def insertionB4Head(head:doublyNode, val:int):
    if head==None:
        new=doublyNode(val)
        return new
    new=doublyNode(val,None,head)
    head.prev=new
    return new
    

# insertion of node before end in dll
def insertionB4End(head:doublyNode, val:int):
    if head==None:
        new=doublyNode(val)
        return new
    if head.next==None:
        new=doublyNode(val,None,head)
        head.prev=new
        return new
    temp=head
    while(temp.next!=None):
        temp=temp.next
    back=temp.prev
    new=doublyNode(val,back,temp)
    back.next=new
    temp.prev=new
    return head


# insertion of ele after kth node
def insertionB4Kth(head:doublyNode, val:int,k:int):
    if head==None:
        new=doublyNode(val)
        return new
    if k==1:
        return insertionB4Head(head,val)
    c=1
    temp=head
    while(temp.next!=None):
        if c==k:
            break
        temp=temp.next
        c+=1
    if c!=k:
        return head
    back=temp.prev
    new=doublyNode(val,back,temp)
    back.next=new
    temp.prev=new
    return head
    

# insertion of ele after the node
def insertionB4Node(head:doublyNode, val:int, node:int):
    if head==None:
        new=doublyNode(val)
        return new
    if head.data==node:
        return insertionB4Head(head,val)
    temp=head
    while(temp.next!=None):
        if temp.data==node:
            break
        temp=temp.next
    if temp.data!=node:
        return head
    back=temp.prev
    new=doublyNode(val,back,temp)
    back.next=new
    temp.prev=new
    return head



# REVERSE A DOUBLY LINKED LIST
# Approach 1--> store the data in stack then make change the linkedlist according the pop element from the stack
# TC-O(2N) and SC-O(N)
def reverseDll(head:doublyNode):
    arr=[]
    temp=head
    while(temp!=None):
        arr.append(temp.data)
        temp=temp.next
    temp1=head
    print(arr)
    i=-1
    while(temp1!=None):
        temp1.data=arr[i]
        temp1=temp1.next
        i-=1
    return head

# Approach 2 --> change the nodes pointers
# use 3 variable curr back and front
# TC-O(N) and SC-O(1)
def reverseDll2(head:doublyNode):
    if head==None or head.next==None:
        return head
    curr=head
    back=None
    front=head.next
    
    while(front!=None):
        curr.next=back
        curr.prev=front
        back=curr
        curr=front
        front=front.next
    curr.next=back
    curr.prev=front
    return curr

if __name__=="__main__":
    a=[1]
    head=convertArrToDll(a)
    # traversal_ll(deletionHead(None))
    # traversal_ll(deletionTail(head))
    # traversal_ll(deletionKth(head,2))
    traversal_ll(deletionNode(head,1))
    # traversal_ll(insertionHead(head,0))
    # traversal_ll(insertionAfHead(head,6))
    # traversal_ll(insertionAfKth(head,1,44))
    # traversal_ll(insertionAfNode(head,1,66))
    # traversal_ll(insertionB4End(head,9))
    # traversal_ll(insertionB4Head(head,55))
    # traversal_ll(insertionB4Kth(head,77,8))
    # traversal_ll(insertionB4Node(head,66,8))
