from bst1 import Node
# 1️⃣ K-th Smallest/Largest Element in BST--✅checked
# here firstly brute force use firstly use traversal then sort the traversal
# get tc O(n+nlogn) sc O(n)-auxillary call stack
# optimal
# 📒inorder traversal of bst gives sorted elements
# here we use traversal and have a ptr(we use list though) which store the elements no if the len of list==k then we get it 
# here💀 we dont use-->trick-->for smallest--> given above and for largest find len then substract the k then do same traversal till n-k
# tc O(n) sc O(n)   (sc-O(1)--morris traversal)
#     8
#    / \
#   5   12
#  / \  / \
# 4  7 11  14
#   /      /
#  6      13
# ans= 6
def kthSmallestHelper(root:Node,k:int,a:list):
    if root==None :return
    kthSmallestHelper(root.left,k,a)
    a.append(root.data)
    kthSmallestHelper(root.right,k,a)

def kthSmallest(root:Node,k:int):
    a=[]
    kthSmallestHelper(root,k,a)
    return a[k-1]

def kthLargest(root:Node,k:int):
    a=[]
    kthSmallestHelper(root,k,a)
    return a[-k]


# 2️⃣Check if a tree is a BST or BT | Validate a BST----✅checked
# here we need to check if the given is bst or not
# here we use the min and max val 
# check at every level the node live between the min and max val
# if go to left update max to root
# and go to right update min to root
# tc O(n) sc O(n)

def validateBST(root:Node):
    return isvalidateBST(root,-(2**31)-1,(2**31))

def isvalidateBST(root:Node,minVal:int,maxVal:int):
    if root==None:return True
    if minVal>=root.data or maxVal<=root.data:
        return False
    l=isvalidateBST(root.left,minVal,root.data)
    r=isvalidateBST(root.right,root.data, maxVal)
    if l ==True and r==True:return True
    return False


# 3️⃣LCA in Binary Search Tree--✅checked
# here we use if else condition that is if both are in different path of root then the root is lca or if root ==a or root==b then root is lca
# if a,b < root then root=root.left or a,b>root then root=root.right
# tc O(logn)
#     8
#    / \
#   5   12
#  / \  / \
# 4  7 11  14
#   /      /
#  6      13
# a=5,b=12
# ans=8

def lowestCommonAncestor(root:Node,p:Node,q:Node):
    if root.data==p.data or root.data==q.data:
        return root
    if root.data >p.data and root.data>q.data:
        return lowestCommonAncestor(root.left,p,q)
    if root.data <p.data and root.data<q.data:
        return lowestCommonAncestor(root.right,p,q)
    return root

# 4️⃣Construct a BST from a preorder traversal | 3 Methods
# given traversal of preorder(root left right) and return the root node
# tra=[8,5,1,7,10,12]
#     8
#    / \
#   5   10
#  / \    \
# 1  7    12
# not understand⚡⚡⚡⚡⚡💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀

# 5️⃣ Inorder Successor/Predecessor in BST 
# successor-> a val is given find the immediate greater val than it
# predecessor-> a val is given find the immediate smaller val than it
#     8
#    / \
#   5   12
#  / \  / \
# 4  7 11  14
#   /      /
#  6      13
# val=11 ans 8(predecessor) 12(successor)
# method 1
# firstly find the the inorder then find the successor or predecessor
# tc sc O(n)
# method 2
# firstly do the inorder if any value greater than val return it
# tc O(n) sc (1)--> here we dont storing anything and also here in ques or other also where recursion has done but sc o(1) dont minding the auxillary call stack
# method 3
# here we first we use if else condition that 
# for successor if root<key then right elif root>key then left and append and root==key then right
# for predecessor if root<key then append and right else left
def inorderSuccessorPredecessor(root:Node,key:int):
    a=[]
    b=[]
    inorderSuccessor(root,a,key)
    inorderPredessor(root,b,key)
    m=-1
    m1=-1
    if len(a)!=0:
        m=min(a)
    if len(b)!=0:
        m1=max(b)
    return [m,m1]

def inorderSuccessor(root:Node,a:list,key:int):
    if root==None:return
    if root.data<=key:
        inorderSuccessor(root.right,a,key)
    else:
        a.append(root.data)
        inorderSuccessor(root.left,a,key)
    

def inorderPredessor(root:Node,a:list,key:int):
    if root==None:return
    if root.data<key:
        a.append(root.data)
        inorderPredessor(root.right,a,key)
    else:
        inorderPredessor(root.left,a,key)
    



if __name__=="__main__":
    i=Node(13)
    g=Node(14,i)
    f=Node(11)
    h=Node(6)
    e=Node(7,h)
    d=Node(4)
    c=Node(12,f,g)
    b=Node(5,d,e)
    a=Node(8,b,c)
    # print(kthSmallest(a,3))
    print(inorderSuccessorPredecessor(a,11))
    