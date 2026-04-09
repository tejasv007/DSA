from bt1 import Node
from collections import deque
# 1️⃣maximum path sum-----💀💀💀💀💀💀💀💀💀💀
# find max sum of node values of a path
# here we use 
def maxPathSum(root:Node,m=[]):
    if root==None:return 0
    lefth=maxPathSum(root.left,m)
    righth=maxPathSum(root.right,m)
    m.append((lefth+righth+root.data))
    return max(lefth,righth)+root.data

def fn(root):
    m=[]
    maxPathSum(root,m)
    return max(m)

# 2️⃣check identical tree✅
# tc O(n) sc O(n)(call stack)
# here we put many base cases or i would say cases to handle end case
# if anywhere we get false we return not go further 
# here we only want to find the false one as when we get false we have to return ie dont have to go further 
def checkIdenticalTree(root1:Node, root2:Node):
    if root1==root2:
        return True
    if root1==None and root2!=None:
        return False
    if root2==None and root1!=None:
        return False
    if root1.data!=root2.data:
        return False
    l=checkIdenticalTree(root1.left,root2.left)
    r=checkIdenticalTree(root1.right,root2.right)
    if l==False or r==False:
        return False
    return True


# 3️⃣zig zag traversal
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7
# ans=[[1],[3,2],[4,5,6,7]]
# sc O(n)
# 1  use level order traversal then reverse alternate list in the traversal
# tc - o(n)
# 2  do reverse by using flag-->flag=0 then l to r else flag=1 then r to l
# but we use the 1 one only t here would be tc difference
# tc O(1+2(2)+3+2(4)+5+2(6).....) tc O(n^2)
def zigZagTraversal(root:Node):
    if root==None:
        return []
    tra=[]
    d=deque()
    d.append(root)
    flag=0
    while(len(d)!=0):
        l=len(d)
        level=[]
        for i in range(l):
            a=d.popleft()
            level.append(a.data)
            if a.left!=None:
                d.append(a.left)
            if a.right!=None:
                d.append(a.right)
        if flag==1:
            tra.append(level[::-1])
        else:
            tra.append(level)
        if flag==0:flag=1
        else:flag=0
    return tra

# 4️⃣boundary traversal----left
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7
# ans=[1,2,4,5,6,7,3]
# here we traverse the 

# 5️⃣vertical order traversal
#       1
#      / \ 
#     2    3
#    / \  / \
#   4  10 9 10
#    \
#     5
#      \ 
#       6
# vot=[[4],[2,5],[1,9,10,6],[3],[10]]
# tc O(n+n+logn)
# sc O(4n)
def verticalOrderTraversal(root:Node):
    tra=[]
    if root==None:
        return tra
    d=deque()
    d.append([root,0])
    while(len(d)!=0):
        a=d.popleft()
        a1=a[0]
        a2=a[1]
        tra.append([a1.data,a2])
        if a1.left!=None:
            newa=a2-1
            d.append([a1.left,newa])
        if a1.right!=None:
            newa=a2+1
            d.append([a1.right,newa])
    tra.sort(key=lambda i:i[1])
    ans=[]
    new=[tra[0][0]]
    ind=tra[0][1]
    for i in range(1,len(tra)):
        if ind != tra[i][1]:
            ans.append(new)
            ind=tra[i][1]
            new=[tra[i][0]]
        else:
            new.append(tra[i][0])
    ans.append(new)

    return ans
        
        
        
if __name__=="__main__":
    e=Node(7)
    d=Node(15)
    c=Node(20,d,e)
    b=Node(9)
    a=Node(-10,b,c)
    e1=Node(7)
    d1=Node(15)
    c1=Node(20,d1,e1)
    f=Node(55)
    b1=Node(9,f)
    a1=Node(-10,b1,c1)
    # print(fn(a))
    # print(checkIdenticalTree(None,None))
    # print(zigZagTraversal(a1))
    j2=Node(10)
    i2=Node(9)
    c2=Node(3,i2,j2)
    h2=Node(6)
    g2=Node(5,None,h2)
    d2=Node(4,None,g2)
    e2=Node(10)
    b2=Node(2,d2,e2)
    a2=Node(1,b2,c2)
    print(verticalOrderTraversal(a2))
