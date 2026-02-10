# INSERTION
from ll1 import Node,linkedList1,traversal_ll
# insert element at head of linked list
def insert_head(head:Node,data:int):
    if head==None:
        new=Node(data)
        return new
    new=Node(data,head)
    return new

# insert element at end of linked list
def insert_end(head:Node, data:int):
    if head==None:
        new=Node(data)
        return new
    temp=head
    while(temp.next!=None):
        temp=temp.next
    new=Node(data)
    temp.next=new
    return head

# insert element at a position of linked list
def insert_K(head:Node,k:int, data: int, l:int):
    if head==None:
        new=Node(data)
        return new
    temp=head
    if k>l+1:
        return "cant insert"
    new=Node(data)
    if k==1:
        new.next=head
        return new
    prev=temp
    while(k>1 ):
        prev=temp
        temp=temp.next
        k-=1
    prev.next=new
    new.next=temp
    return head
    
# insert element before the value in linked list
def insert_b4_val(head:Node,val:int, new_one:int):
    if head==None:
        new=Node(data)
        return new
    temp=head
    prev=temp
    if head.data==val:
        new=Node(new_one,head)
        return new
    while(temp!=None):
        if temp.data==val:
            new=Node(new_one,temp)
            prev.next=new
            return head
        prev=temp
        temp=temp.next
    return head

# insertion after the value in ll
def insert_after_val(head:Node,val:int,new_one:int):
    if head==None:
        new=Node(new_one)
        return new
    temp=head
    prev=temp
    temp=temp.next
    while(prev.next!=None):
        if prev.data==val:
            break
        prev=prev.next
        temp=temp.next
    if prev.data!=val:
        return head
    new=Node(new_one,temp)
    prev.next=new
    return head



if __name__=="__main__":
    head=linkedList1()
    h1=insert_after_val(head,5,7)
    traversal_ll(h1)
