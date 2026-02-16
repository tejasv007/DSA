from ll1 import Node,convertArrToLl,traversal_ll

# 1️⃣ADD TWO NUMBER USING LINKED LISTS
# 2->4->6->none
# 3->8->7->none
# ans=5->2->4->1->
# BRUTE FORCE
# build find the two numbers than add both then create new linked list consist of the res number
# TC-O(4N) SC-O(2N) (here, assuming that each linked list have n length)
def addTwoNo1(head1:Node,head2:Node):
    i1=""
    i2=""
    temp1=head1
    while(temp1!=None):
        a=str(temp1.data)
        i1=i1+a
        temp1=temp1.next
    i1=i1[::-1]
    i1=int(i1)
    temp2=head2
    while(temp2!=None):
        a=str(temp2.data)
        i2=i2+a
        temp2=temp2.next
    i2=i2[::-1]
    i2=int(i2)
    res=i1+i2
    temp=Node(res%10)
    head=temp
    res=res//10
    while(res>10):
        new=Node(res%10)
        res=res//10
        temp.next=new
        temp=new
    if res!=0:
        new=Node(res)
        temp.next=new
    return head

# OPTIMAL
# create a linked list by adding the number in both linked list
# TC-O(N) SC-O(N)
def addTwoNo2(head1:Node, head2:Node):
    temp1=head1
    temp2=head2
    dummy=Node(-1)
    carry=0
    curr=dummy
    while(temp1!=None or temp2!=None):
        if temp1!=None and temp2!=None:
            new=Node(((temp1.data+temp2.data)+carry)%10)
            carry=((temp1.data+temp2.data)+carry)//10
            # print(carry)
            curr.next=new
            curr=new
            # print(curr.data)
        elif temp1!=None and temp2==None:
            if (temp1.data+carry)//10!=0:
                carry=(temp1.data+carry)//10
            temp1.data=(temp1.data+carry)%10
            curr.next=temp1
            curr=temp1
            # print(curr.data)

        elif temp1==None and temp2!=None:
            if (temp2.data+carry)//10!=0:
                carry=(temp2.data+carry)//10
            temp2.data=(temp2.data+carry)%10
            curr.next=temp2
            curr=temp2
            # print(curr.data)

        
        
        if temp1!=None:
            temp1=temp1.next
        if temp2!=None:
            temp2=temp2.next
    if carry!=0:
        new=Node(carry)
        curr.next=new
    return dummy.next


# 2️⃣ODD AND EVEN LINKED LIST
# 1->6->4->5->3->9->8
# res=>1->4->3->8->6->5->9

# BRUTE FORCE
# use a data structure store the odd no values then even no values
# change the data of linked list according to it
# TC-O(2N) SC-O(N)
def oddAndEven1(head:Node):
    if head==None or head.next==None:
        return None
    arr=[]
    temp=head
    while(temp!=None and temp.next!=None):
        arr.append(temp.data)
        temp=temp.next.next
    if temp:
        arr.append(temp.data)
    temp=head.next
    while(temp!=None and temp.next!=None ):
        arr.append(temp.data)
        temp=temp.next.next
    if temp:
        arr.append(temp.data)
    temp=head
    i=0
    while(temp!=None):
        temp.data=arr[i]
        temp=temp.next
        i+=1
    return head

# OPTIMAL
# TC-O(N) SC-O(1)
def oddAndEven2(head:Node):
    temp=head
    odd=Node(-1)
    curr1=odd
    even=Node(-1)
    curr2=even
    i=1
    while(temp!=None):
        if i%2!=0:
            curr1.next=temp
            curr1=temp
        else:
            curr2.next=temp
            curr2=temp
        temp=temp.next
        i+=1
    curr1.next=even.next
    return odd.next

# 3️⃣SORT LINKED LIST 0 1 AND 2
# BRUTE FORCE
# TC-O(2n) 
# 3 var one two and zero to count all three then loop over the ll and assign the values
def sortLinkedList(head:Node):
    zeroes=0
    one=0
    two=0
    temp=head
    while(temp!=None):
        if temp.data==0:
            zeroes+=1
        elif temp.data==1:
            one+=1
        else:
            two+=1
        temp=temp.next
    temp=head
    while(temp!=None):
        if zeroes!=0:
            temp.data=0
            zeroes-=1
        elif one!=0:
            temp.data=1
            one-=1
        else:
            temp.data=2
            two-=1
        temp=temp.next
    return head


# OPTIMAL
# change linked list links
# make three linked list and then join them
# TC-O(N)
def sortLinkedList2(head:Node):
    zeroes=Node(-1)
    curr0=zeroes
    one=Node(-1)
    curr1=one
    two=Node(-1)
    curr2=two
    temp=head
    while(temp!=None):
        if temp.data==0:
            curr0.next=temp
            curr0=temp
        elif temp.data==1:
            curr1.next=temp
            curr1=temp
        else:
            curr2.next=temp
            curr2=temp
        temp=temp.next
    
    if one.next==None: 
        curr0.next=two.next
        return zeroes.next
    curr0.next=one.next
    curr1.next=two.next
    curr2.next=None#---- change maker...
    return zeroes.next



# 4️⃣REMOVE NTH NODE FROM THE END
# BRUTE FORCE
# firstly count the nodes 
# make new var that stor count - nth node
# traverse till new var then remove the next node
# TC-O(2N)
def removeNthNodeEnd(head:Node,n:int):
    temp=head
    c=0
    while(temp!=None):
        c+=1
        temp=temp.next
    if (c-n)<0:
        return head
    if (c-n)==0:
        temp=head
        head=head.next
        temp.next=None
        return head
    temp=head
    new=c-n
    while(temp!=None):
        if new==1:
            break
        new-=1
        temp=temp.next
    if temp.next.next==None:
        temp.next=None
        return head
    newone=temp.next
    temp.next=temp.next.next
    newone.next=None
    return head

# OPTIMAL
# use two pointer fast and slow fast will move first till n th node then slow start from root node
# TC-O(n)
def removeNthNodeEnd2(head:Node, n:int):
    fast=head
    slow=head
    while(fast!=None):
        if n==0:break
        n-=1
        fast=fast.next
    if fast==None and n==0:
        new=head
        head=head.next
        new.next=None
        return head
    if fast==None and n!=0:
        return head
    fast=fast.next
    while(fast!=None):
        slow=slow.next
        fast=fast.next
    slow.next=slow.next.next
    return head
    

# 5️⃣REVERSE A GIVEN LINKED LIST
# BRUTE FORCE
# use a data structure and stor the values
# traverse the linked list one more time and replace the values acc to reverse data structure
# TC-O(2N) SC-O(n)
def reverseLL1(head:Node):
    temp=head
    a=[]
    while(temp!=None):
        a.append(temp.data)
        temp=temp.next
    i=-1
    temp=head
    while(temp!=None):
        temp.data=a[i]
        i-=1
        temp=temp.next
    return head

# OPTIMAL---- iterative
# reverse the link of the nodes
def reverseLl2(head:Node):
    if head==None or head.next==None:
        return head
    curr=head
    front=curr.next
    prev=None
    while(front!=None):
        curr.next=prev
        prev=curr
        curr=front
        front=front.next
    curr.next=prev
    return curr


# OPTIMAL---- recursive-----pending💀💀💀💀

# def reverseLL3Helper(prev:Node, curr:Node, front:Node):
#     if curr.next==None:
#         curr.next=prev
#         return curr
#     curr.next=prev
#     curr=front
#     prev=curr
#     front=front.next
#     return reverseLL3Helper(prev,curr,front)

# def reverseLL3(head:Node):
#     if head==None:return head
#     return reverseLL3Helper(None,head,head.next)



if __name__=="__main__":
    a=[1,2,3,4,5]
    b=[0,2,0,2,1,1,0,2,0]
    h1=convertArrToLl(a)
    h2=convertArrToLl(b)
    # traversal_ll(addTwoNo1(h1,h2))

    # traversal_ll(addTwoNo2(h1,h2))
    # traversal_ll(oddAndEven1(h1))
    # print(oddAndEven1(h1))
    # traversal_ll(oddAndEven2(h1))
    # traversal_ll(sortLinkedList(h2))
    # traversal_ll(sortLinkedList2(h2))
    # traversal_ll(removeNthNodeEnd(h1,9))
    # traversal_ll(reverseLL1(h1))
    # traversal_ll(reverseLl2(h1))
    a=2
    print(a//10)