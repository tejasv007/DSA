'''
Docstring for DSA.BinaryTree.bt2
-> max depth== max height

'''
from bt1 import Node,levelOrderTraversal1
h=Node(6)
g=Node(5,None,h)
d=Node(4,None,g)
e=Node(7)
f=Node(3,e)
c=Node(8)
b=Node(2,f,d)
a=Node(1,b,c)

# 1️⃣count no of nodes
def countNodes(root:Node):
    if root==None:
        return 0
    lc=countNodes(root.left)
    lr=countNodes(root.right)
    return lr+lc+1
 
# 2️⃣Sum of nodes
def sumOfNodes(root:Node):
    if root==None:
        return 0
    sl=sumOfNodes(root.left)
    sr=sumOfNodes(root.right)
    return sl+sr+root.data


# 3️⃣Height or depth of tree
def heightOfTree(root:Node):
    if root==None:
        return 0
    ll=heightOfTree(root.left)
    lr=heightOfTree(root.right)
    return max(lr,ll)+1


# 4️⃣diameter of tree
# longest path between two nodes and that path can pass via root otherwise no need
# calculate height of left + right and find max of of all
# T(C)->O(N²)
def diameterOfTree1(root:Node):
    if root==None:
        return 0
    curr_dia=heightOfTree(root.left)+heightOfTree(root.right)+1
    dia_l=diameterOfTree1(root.left)
    dia_r=diameterOfTree1(root.right)
    return max(dia_r,dia_l,curr_dia)
    
# T(C)->O(N)
def diameterOfTree2(root:Node):
    maxi=[0]
    diameter2(root,maxi)
    return maxi[0]
def diameter2(root:Node,maxi:list):
    if root==None:
        return 0
    ld=diameter2(root.left,maxi)
    rd=diameter2(root.right,maxi)
    maxi[0]=(max(maxi[0], ld+rd+1))
    return 1+max(ld,rd)
    
# 5️⃣check for Balanced Tree✅
# balanced tree--> left height- right height<=1
# here we return two things one is height and second one is the boolean value
def balanceTree(root:Node):
    if root==None:
        return 0, True
    h1,s1=balanceTree(root.left)
    h2,s2=balanceTree(root.right)
    if abs(h1-h2)<=1 and s1==s2 and s1==True:
        return max(h1,h2)+1,True
    return max(h1,h2)+1,False



if __name__=="__main__":
    # print(levelOrderTraversal1(a))
    # print(countNodes(a))
    # print(sumOfNodes(a))
    # print(heightOfTree(a))
    # print(diameterOfTree2(a))
    h=Node(6)
    g=Node(5,None,h)
    d=Node(4,None,g)
    e=Node(7)
    f=Node(3,e)
    c=Node(8)
    b=Node(2,f,d)
    a=Node(1,b,c)
    d1=Node(4)
    c1=Node(3)
    b1=Node(2,d1)
    a1=Node(1,b1,c1)
    print(balanceTree(a))
