from ll1 import Node, traversal_ll,convertArrToLl
from ll4 import reverseLl2
# 1️⃣CHECK IF LINKED LIST PALIMDROME OR NOT✔️checked
# BRUTE FORCE✔️checked
# use a data structure store the values 
# pop out values one by one from data structure
# TC-O(2N) SC-O(N)
def checkPalimdrome1(head: Node):
    a=[]
    temp=head
    while(temp!=None):
        a.append(temp.data)
        temp=temp.next
    i=-1
    temp=head
    while(temp!=None):
        if temp.data!=a[i]:
            return False
        temp=temp.next
        i-=1
    return True


# OPTIMAL
# go to the middle one and then reverse the next
# then check from start is the all element same or not
# have tc-O(2n) and sc-O(n)
# i am not doing it.... as tc isnt changing


# 2️⃣ADD 1 TO LINKED LIST
# 1->5->9->9->none
# ans=>1->6->0->0->none

# BRUTE FORCE
# reverse the linked list 
# then add one check if there any carry
# if there is a carry, add to next node
# after traversing all node if carry!=0 build a new node with the carry value
# TC-O(3N)
def addOneToLL(head:Node):
    h1=reverseLl2(head)
    carry=1
    temp=h1
    while(temp.next!=None):
        newval=temp.data+carry
        temp.data=(newval)%10
        # print(temp.data)
        carry=(newval)//10
        # print(carry)
        temp=temp.next
    newval=temp.data+carry
    temp.data=(newval)%10
    carry=(newval)//10
    if carry!=0:
        new=Node(carry)
        temp.next=new
    h2=reverseLl2(h1)
    return h2


# OPTIMAL
# using recursion
# TC-O(2N)
def helperAddOne(head:Node, carry:int):
    if head.next==None:
        newval=head.data+carry
        head.data=newval%10
        return newval//10
    c=helperAddOne(head.next,carry)
    newval=head.data+c
    head.data=newval%10
    return newval//10
    
def addOneToLL2(head:Node):
    if head==None:
        new=Node(1)
        return new
    c=helperAddOne(head,1)
    if c!=0:
        new=Node(c)
        new.next=head
        return new
    return head


# 3️⃣ INTERSECTION OF Y LINKED LIST
# BRUTE FORCE
#use a data structure store the nodes of first linked list 
# then traverse second one and check if there node in data structure or not
# if node exist return the node else return none
# TC-O(2N) sc-O(n )
def intersectionYLl1(head1:Node, head2:Node):
    a=[]
    temp1=head1
    while(temp1!=None):
        a.append(temp1)
        temp1=temp1.next
    temp2=head2
    while(temp2!=None):
        if temp2 in a:
            return temp2
        temp2=temp2.next
    return None

# OPTIMAL-->code doubt💀💀💀
# traverse the first and second simultaneously
# change the head of each other, if they get same, return 
# TC-O(2n)
def intersectionYLl2(head1:Node, head2:Node):
    temp1=head1
    temp2=head2
    if head1==None and head2==None:return None
    while(temp1!= temp2):
        if temp1==temp2:
            return temp1
        if temp1==None:
            temp1=head2
        if temp2==None:
            temp2=head1
        temp1=temp1.next
        temp2=temp2.next
    return temp1


#4️⃣ MIDDLE OF LINKED LIST
# BRUTE FORCE
# count the no of nodes 
# half the count +1
# and return the node at half no
# TC-O(n+n/2)
def middleOfLl(head:Node):
    c=0
    temp=head
    while(temp!=None):
        c+=1
        temp=temp.next
    new=(c//2)+1
    temp=head
    while(new>1):
        new-=1
        temp=temp.next
    return temp


# OPTIMAL
# tortoise and hare
# slow and fast pointer
# move slow by 1 and fast by 2
# when fast==none or fast.next==none return slow
# TC-O(N/2)
def middleOfLl2(head:Node):
    if head==None:return None
    slow=head
    fast=head
    while(fast!=None and fast.next!=None):
        slow=slow.next
        fast=fast.next.next
    return slow

# 5️⃣DETECT LOOP IN A LINKED LIST
# BRUTE FORCE
# use a data structure store nodes
# traverse whole linked list if the node in data structure return true
# while the traverse reach to end mean none return false
# TC-O(N)
def detectLoop1(head:Node):
    a=[]
    temp=head
    while(temp!=None):
        if temp in a:
            return True
        a.append(temp)
        temp=temp.next
    return False

# OPTIMAL
# tortoise and hare algo
# slow==fast then true that is loop exist
# fast==none or fast.next==none loop not exist

def detectLoop2(head:Node):
    if head==None:
        return head
    slow=head
    fast=head
    while(fast!=None and fast.next!=None):
        if slow==fast:
            return True
        slow=slow.next
        fast=fast.next.next
    return False



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
    a1=Node(5)
    b1=Node(6)
    a1.next=b1
    b1.next=c
    arr=[99]
    arr2=[5,6,7,8,2,9]
    h11=convertArrToLl(arr)
    h22=convertArrToLl(arr2)

    # print(checkPalimdrome1(h1))
    # traversal_ll(addOneToLL(h1))
    # traversal_ll(addOneToLL2(h1))
    # print(intersectionYLl1(a,a1).data)
    # print(intersectionYLl2(a,a1).data)
    # print(middleOfLl(h22).data)
    # print(middleOfLl2(h11).data)
    # print(detectLoop1(h11))
    print(detectLoop2(h11))