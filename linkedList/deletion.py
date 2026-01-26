# DELETION
# left to check✔️✔️✔️⌛
from ll1 import Node,linkedList1,traversal_ll
# delete element at head of linked list
head=linkedList1()
# (traversal_ll(head))
def delete_head(head:Node):
    if head==None or head.next==None:
        return None
    newhead=head.next
    head.next=None
    return newhead


# delete element at end of linked list
c=Node(3)
b=Node(2,c)
a=Node(1,b)

def delete_end(head:Node):
    if head==None or head.next==None:
        return None
    temp=head
    while(temp.next.next!=None):
        temp=temp.next
    temp.next=None
    return head

# delete element at a position of linked list
def delete_the_pos(head:Node, pos:int):
    if head==None:
        return head
    if head.next==None:
        return None
    if pos==1:
        temp=head
        head=head.next
        temp.next=None
        return head
    c=2
    prev=head
    temp=head.next
    while(temp!=None):
        if c==pos:
            if temp.next==None:
                prev.next=None
                return head
            else:
                prev.next=temp.next
                temp.next=None
                return head
        prev=prev.next
        temp=temp.next
        c+=1
    return None
                       
# delete the value in linked list
def delete_the_val(head:Node, val:int):
    if head==None or head.next==None:
        return None
    if head.data==val:
        if head.next==None:
            return None
        temp=head
        head=head.next
        temp.next=None
        return head
    temp=head.next
    prev=head
    while(temp!=None):
        if temp.data==val:
            if temp.next==None:
                prev.next=None
                temp.next=None
            else:
                prev.next=temp.next
                temp.next=None
            return head
        temp=temp.next
        prev=prev.next
    return None
# delete element before the value in linked list
def delete_ele_b4_value(head:Node, val: int):
    if head==None :
        return None
    if head.data==val or head.next==None:
        return head
    if head.next.data==val:
        temp=head
        head=head.next
        temp.next=None
        return head

    prev=head
    temp=head.next
    while(temp!=None):
        if temp.next!=None:
            if temp.next.data==val:
                prev.next=temp.next
                temp.next=None
                return head
        prev=prev.next
        temp=temp.next
    return None
# delete element after the value in linked list
def delete_ele_af_val(head:Node,val:int):
    if head==None or head.next==None:
        return head
    temp=head
    while(temp!=None):
        if temp.data==val:
            if temp.next==None:
                return head
            if temp.next.next!=None:
                new=temp.next
                temp.next=temp.next.next
                new.next=None
                return head
            else:
                temp.next=None
                return head
        temp=temp.next
    return head
if __name__=="__main__":
    # traversal_ll(delete_head(head))
    # traversal_ll(delete_end(head))
    # traversal_ll(head)
    # traversal_ll(delete_ele_pos(c,2))
    # traversal_ll(delete_the_val(c,2))
    # traversal_ll(delete_the_pos(head,3))
    traversal_ll(delete_ele_af_val(head,5))