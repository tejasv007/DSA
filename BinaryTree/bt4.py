from bt1 import Node
from collections import deque
# 1️⃣top view traversal
#       1
#      / \ 
#     2    3
#    / \  / \
#   4  10 9 10
#    \
#     5
#      \ 
#       6
# tvt=[4,2,1,3,10]
# tc O(n) sc (3n)
# we use queue for traversal
# here we use level order traversal
# here we use dict and not replace outdated one with updated one
def topViewTraversal(root:Node):
    tra=dict()
    if root==None:return []
    d=deque()
    d.append([root,0])
    while(len(d)!=0):
        a=d.popleft()
        a1=a[0]
        a2=a[1]
        if a2 not in tra.keys():
            tra[a2]=a1.data
        if a1.left!=None:
            newa=a2-1
            d.append([a1.left,newa])
        if a1.right!=None:
            newa=a2+1
            d.append([a1.right,newa])
    ans=[]
    new=sorted(list(tra.keys()))
    for i in new:
        ans.append(tra[i])
    return ans

# 2️⃣bottom view traversal
#       1
#      / \ 
#     2    3
#    / \  / \
#   4  10 9 10
#    \
#     5
#      \ 
#       6
# bvt=[4,5,6,3,10]
# here we use dict and  replace outdated one with updated one
# tc O(n) sc (3n)
def bottomViewTraversal(root:Node):
    tra=dict()
    if root==None:return []
    d=deque()
    d.append([root,0])
    while(len(d)!=0):
        a=d.popleft()
        a1=a[0]
        a2=a[1]
        # if a2 in tra.keys():
        tra[a2]=a1.data
        
        if a1.left!=None:
            newa=a2-1
            d.append([a1.left,newa])
        if a1.right!=None:
            newa=a2+1
            d.append([a1.right,newa])
    ans=[]
    new=sorted(list(tra.keys()))
    for i in new:
        ans.append(tra[i])
    return ans

# 3️⃣Right/Left View of Binary Tree
#       1
#      / \ 
#     2    3
#    / \  / \
#   4  10 9 10
#    \
#     5
#      \ 
#       6
# lfvt=[1,3,10,5,6]
# rtvt=[1,2,4,5,6]
# here we index the node not vertically but horizontally
def rightViewTraversal(root:Node):
    tra=dict()
    if root==None:return []
    d=deque()
    d.append([root,0])
    while(len(d)!=0):
        a=d.popleft()
        a1=a[0]
        a2=a[1]
        # if a2 not in tra.keys():
        tra[a2]=a1.data
        a2=a[1]+1
        if a1.left!=None:
            d.append([a1.left,a2])
        if a1.right!=None:
            d.append([a1.right,a2])
    ans=[]
    new=sorted(list(tra.keys()))
    for i in new:
        ans.append(tra[i])
    return ans

def leftViewTraversal(root:Node):
    tra=dict()
    if root==None:return []
    d=deque()
    d.append([root,0])
    while(len(d)!=0):
        a=d.popleft()
        a1=a[0]
        a2=a[1]
        if a2 not in tra.keys():
            tra[a2]=a1.data
        a2=a[1]+1
        if a1.left!=None:
            d.append([a1.left,a2])
        if a1.right!=None:
            d.append([a1.right,a2])
    ans=[]
    new=sorted(list(tra.keys()))
    for i in new:
        ans.append(tra[i])
    return ans

# 4️⃣Check for Symmetrical Binary Trees
# 💀💀💀💀💀did by ai
def isSymmetrical(root:Node):
    if root==None:
        return True
    return isSymmetricalHelp(root.left,root.right)

def isSymmetricalHelp(root1:Node,root2:Node):
    if root1==None and root2==None:
        return True
    if root1==None or root2==None:
        return False
    if root1.data!=root2.data:
        return False
    l=isSymmetricalHelp(root1.left,root2.right)
    r=isSymmetricalHelp(root1.right,root2.left)
    return l and r


# 5️⃣Print Root to Node Path in Binary Tree
#       1
#      / \ 
#     2    3
#    / \  / \
#   4  10 9 10
#    \
#     5
#      \ 
#       6
# target=6
# ans=[1,2,4,5,6]
# left to check
# tc O(n) sc O(logn)
def rootNodePath(root,target):
    p=[]
    rootToNodePath(root,target,p)
    return p
def rootToNodePath(root:Node,target:int,path=[]):
    if root==None:
        return False
    if root.data==target:
        path.append(root.data)
        return True
    path.append(root.data)
    l=rootToNodePath(root.left,target,path)
    r= rootToNodePath(root.right,target,path)
    if r==False and l==False:
        path.pop()
        return False
    if l==True or r==True:
        return True
    return False






if __name__=="__main__":
    j2=Node(10)
    i2=Node(9)
    c2=Node(3,i2,j2)
    h2=Node(6)
    g2=Node(5,None,h2)
    d2=Node(4,None,g2)
    e2=Node(10)
    b2=Node(2,d2,e2)
    a2=Node(1,b2,c2)
    # print(topViewTraversal(a2))
    # print(bottomViewTraversal(a2))
    # print(rightViewTraversal(a2))
    # print(leftViewTraversal(a2))
    print(rootNodePath(a2,6))