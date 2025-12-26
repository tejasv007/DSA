'''
Docstring for DSA.BinaryTree.bt1
# THIS DOCUMENT CONTAIN ALL THE TRAVERSALS
-> Binary tree is hierarchicak data structure
-> comprises nodes arranged in tree like structure
-> each node have at most two children nodes

-> each node have data, left node, right node

TYPE OF TREE
1. Full binary(Strict binary tree)-- either 0 or 2 children 
2. Complete BT -- all level are cmplty filled except last level. last level has all nodes as left as possible.
3. Perfect BT -- all leaf nodes are at same level
4. Balanced BT -- where heights of 2 subtree of any node differ by at most one
5. Degenerate BT -- where nodes are arranged in a single path leaning to right or left
'''
from collections import deque
class Node:
    def __init__(self,data:int,left=None, right=None):
        self.left=left
        self.right=right
        self.data=data

# TREE 1
f=Node(6)
d=Node(4)
e=Node(5)
c=Node(3,f)
b=Node(2,d,e)
a=Node(1,b,c)

'''TRAVERSAL
->DFS-->depth first search-->preorder, postorder, inorder
-> BFS-->breadth first search-->level order traversal
-> DFS--> use recursion or stack
-> BFS--> use queue data structure
'''
# DFS
# INORDER 
# -> Recursive
def inorder1(root: Node):
    if root==None:
        return root
    inorder1(root.left)
    print(root.data,end=" ")
    inorder1(root.right)
# -> iterative

def inorder2(root:Node):
    stack=[]
    tra=[]
    temp=root
    while(True):
        if temp!=None:
            stack.append(temp)
            temp=temp.left
        else:
            if len(stack)==0:
                break
            temp=stack[-1]
            stack.pop()
            tra.append(temp.data)
            temp=temp.right
    return tra

# POSTORDER
# -> Recursive
def postorder1(root: Node):
    if root==None:
        return root
    postorder1(root.left)
    postorder1(root.right)
    print(root.data,end=" ")


# -> iterative
# using 2 stack
def postorder2(root:Node):
    st1=[]
    st2=[]
    temp=root
    if root==None:
        return st1
    st1.append(root)
    while(len(st1)!=0):
        if temp.left!=None:
            st1.append(temp.left)
        if temp.right!=None:
            st1.append(temp.right)
        a=st1.pop()
        temp=a
        st2.append(a)
    curr=[]
    l=len(st2)-1
    while(l!=-1):
        l-=1
        curr.append(st2[l].data)
    return curr
#  using 1 stack
# TC-O(2N), SC-O(N)
def postorder3(root:Node):
    curr=root
    st=[]
    tra=[]
    while(curr!=None or len(st)!=0):
        if curr!=None:
            st.append(curr)
            curr=curr.left
        else:
            temp=st[-1].right
            if temp==None:
                temp=st.pop()
                tra.append(temp.data)
                while(len(st)!=0 and temp==st[-1].right):
                    temp=st.pop()
                    tra.append(temp.data)
            else:
                curr=temp
    return tra

# PREORDER
# -> Recursive
def preorder1(root: Node):
    if root==None:
        return root
    print(root.data,end=" ")
    preorder1(root.left)
    preorder1(root.right)

# -> iterative
def preorder2(root:Node):
    stack=[]
    tra=[]
    if root==None:
        return tra
    stack.append(root)
    while(len(stack)!=0):
        b=stack.pop()
        tra.append(b.data)
        if b.right!=None:
            stack.append(b.right)
        if b.left!=None:
            stack.append(b.left)
    return tra

# BFS
# level order traversal
def levelOrderTraversal(root:Node):
    arr=[]
    d=deque()
    if root==None:
        return arr
    d.append(root)
    while(len(d)!=0):
        size=len(d)
        level=[]
        for i in range(size):
            new=d.popleft()
            if new.left!=None:
                d.append(new.left)
            if new.right!=None:
                d.append(new.right)
            level.append(new.data)
        arr.append(level)
    return arr

def levelOrderTraversal1(root:Node):
    d=deque()
    arr=[]
    d.append(root)
    while(len(d)!=0):
        a=d.popleft()
        arr.append(a.data)
        if a.left!=None:
            d.append(a.left)
        if a.right!=None:
            d.append(a.right)
    return arr

# all in one traversal
def allTraversal(root:Node):
    pre=[]
    ino=[]
    post=[]
    st=[]
    st.append([root,1])
    while(len(st)!=0):
        a=st[-1]
        if a[1]==1:
            pre.append(a[0].data)
            a[1]+=1
            if a[0].left!=None:
                st.append([a[0].left,1])
        elif a[1]==2:
            ino.append(a[0].data)
            a[1]+=1
            if a[0].right!=None:
                st.append([a[0].right,1])
        else:
            post.append(a[0].data)
            st.pop()
    return pre,ino,post

if __name__=="__main__":
    # print(inorder2(a))
    # inorder1(a)
    # print()
    # preorder1(a)
    # print()
    # print(preorder2(a))
    # print(postorder3(a))
    # # postorder1(a)
    # # print(levelOrderTraversal1(a))
    # print(allTraversal(a))
    print()