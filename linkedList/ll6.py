# ✔️checked
from ll1 import Node, traversal_ll, convertArrToLl
# 1️⃣LENGTH OF LOOP IN LINKED LIST
# BRUTE FORCE✔️checked
# use a data structure and store the nodes 
# if node in array subtract current count from the prev
# TC-O(N+(dict time taken)) SC-O(N)
def lengthLoop1(head:Node):
    if head==None:
        return 0
    a=dict()
    temp=head
    c=1
    while(temp!=None):
        if temp in a.keys():
            return c-a.get(temp)
        a[temp]=c
        temp=temp.next
        c+=1
    return 0


# OPTIMAL-----everything is correcct but then also error💀💀💀💀💀💀💀💀💀
# tortoise and hare algo
# use slow and fast pointer
# when both gets equal to each other start slow and create a new c var with 0
# increment c till fast ==slow
# def lengthHelper(slow:Node,fast:Node):
#     c=1
#     fast=fast.next
#     while(slow!=fast):
#         c+=1
#         fast=fast.next
#     return c

# def lengthOfLoop(head:Node):
#     slow=head
#     fast=head
#     c=1
#     while(fast!=None and fast.next!=None):
#         if slow==fast:return lengthHelper(slow,fast)
#         slow=slow.next
#         fast=fast.next.next
    
if __name__=="__main__":
    e=Node(5)
    d=Node(4)
    c=Node(3)
    b=Node(2)
    a=Node(1)
    a.next=b
    b.next=c
    c.next=d
    d.next=e
    e.next=b
    aa=[1,2,3,4,5]
    h1=convertArrToLl(aa)
    # print(lengthLoop1(h1))
    print(lengthOfLoop(a))