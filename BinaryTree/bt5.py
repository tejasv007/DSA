from bt1 import Node,levelOrderTraversal
from collections import deque, Counter
from bt4 import rootNodePath
# 1️⃣ Lowest Common Ancestor in Binary Tree
#       1
#      / \ 
#     2    3
#    / \  / \
#   4  10 9 13
#    \
#     5
#      \ 
#       6
# lca(4,10)=2
# lca(5,9)=1
# we find the path of both the targets then check which is same and when we get the node is not same, we break the loop 
# h=height of tree
# tc O(n+n+h) sc O(h)
def lowestCommonAncestor(root:Node,t1:int,t2:int):
    p1=rootNodePath(root,t1)
    p2=rootNodePath(root,t2)
    ans=root.data
    for i,j in zip(p1,p2):
        if i==j:
            ans=i
        else:
            break
    return ans
        
    
# tc O(n) sc O(n)--> auxillary stack space
def lowestCommonAncestor2(root:Node,t1:int,t2:int):
    if root==None :return None
    if root.data==t1 or root.data==t2:
        return root.data
    l=lowestCommonAncestor2(root.left,t1,t2)
    r=lowestCommonAncestor2(root.right,t1,t2)
    # if l==None and r==None:return None
    if l==None and r!=None:return r
    if l!=None and r==None:return l
    if l!=None and r!=None:return root.data
    
# 2️⃣Maximum Width of Binary Tree checked✅
# width the no of node in a level
# #     1
#      / \ 
#     2    3
#    / \  / \
#   4  10 9 10
#  /          \
# 12           22
# ans=8
# here we put index at every node
# ie      i
#        / \
#  2(i)+1  2(i)+2
# but if we do this for all if then there would be 10^5 node then it would be complicated
# so at every next level we substract 1 from the all so make start indexing from next level from 0
# for width build a var which store the max of(last-first+1) of indexes at every level
# here we do the level order traversal 
# tc O(n) sc(n)
def maxWidthBinaryTree(root:Node):
    if root==None:return 0
    d=deque()
    wid=1
    d.append([root,0])
    tra=[]
    while(len(d)!=0):
        l=len(d)
        first=0
        last=0
        flag=0
        for i in range(l):
            a=d.popleft()
            a1=a[0]
            a2=a[1]
            tra.append([a1.data,a2])   
            if a1.left!=None:
                if flag==0:
                    first=(2*a2)
                    flag=1
                d.append([a1.left,(((2*a2)))])
                last=(2*a2)
            if a1.right!=None:
                if flag==0:
                    first=(2*a2)+1
                    flag=1
                d.append([a1.right,(2*a2)+1])
                last=(2*a2)+1

        print(first,last)
        wid=max(wid,(last-first+1))
    return wid


# 3️⃣children sum property
# Convert an arbitrary Binary Tree to a tree that holds Children Sum Property
#  Given an arbitrary binary tree, your task is to convert it to a binary tree that holds Children Sum Property, by incrementing the data values of any node.
# tc sc O(n)
# here we use recursion, firstly save root value
# use recursion dfs and assign every root value of max(left.data+right.data, root.data,root value(that we save))
# and return the curr root.data
def childrenSumProperty(root:Node):
    if root==None:
        return root
    childrenSumPropertyHelper(root,root.data)
    return root

def childrenSumPropertyHelper(root:Node,d:int):
    if root==None:return 0
    l=childrenSumPropertyHelper(root.left,d)
    r=childrenSumPropertyHelper(root.right,d)
    root.data=max(l+r,d,root.data)
    return root.data
#------------------diff-------------------------------
# 3️⃣check for children sum property=-----left
# Given the root of a binary tree, return true if and only if every node’s value is equal to the sum of the values stored in its left and right children.
# here we use dfs and at every call we return bool value
# firstly if root==none return 0, check if l +r equals to root otherwise false
#
def checkCSP(root):
    ans=[]
    checkChildrenSumProperty(root,ans)
    if False in ans:return False
    else:return True
def checkChildrenSumProperty(root:Node,ans=[]):
    if root==None:
        ans.append(True)
        return 0
    l=checkChildrenSumProperty(root.left,ans)
    r=checkChildrenSumProperty(root.right,ans)
    # if ans==False:
    if l==r and r==0:
        ans.append(True)
    elif root.data==l+r:
        ans.append(True)
    else:ans.append(False)
    print(ans)
    return root.data


# 4️⃣
# ------------------different code 💀💀💀💀💀💀💀
# def maxPathSum(root:Node,ans,l,targetSum):
#     if root==None:return 
#     l.append(root.data)
#     # print(l)
#     if sum(l)==targetSum:
#         newl=l[::]
#         ans.append(newl) 
#         l.pop()      
#         return
#     maxPathSum(root.left,ans,l,targetSum)
#     maxPathSum(root.right,ans,l,targetSum)
#     l.pop()
#     return 




if __name__=="__main__":
    j2=Node(13)
    i2=Node(9)
    c2=Node(22,i2,j2)
    h2=Node(6)
    g2=Node(6,None,h2)
    d2=Node(6,None,g2)
    e2=Node(10)
    b2=Node(16,d2,e2)
    a2=Node(38,b2,c2)
    # print(lowestCommonAncestor2(a2,5,9))
    ans=[]
    l=[]
    # maxPathSum(a2,ans,l,13)
    # print(ans)
    # print(maxWidthBinaryTree(a2))
    # a=childrenSumProperty(a2)
    # print(levelOrderTraversal(a))
    c1=Node(1)
    b1=Node(2)
    a1=Node(3,b1,c1)
    print(checkCSP(a2))