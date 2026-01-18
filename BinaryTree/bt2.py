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

# count no of nodes
def countNodes(root:Node):
    if root==None:
        return 0
    lc=countNodes(root.left)
    lr=countNodes(root.right)
    return lr+lc+1
 
# Sum of nodes
def sumOfNodes(root:Node):
    if root==None:
        return 0
    sl=sumOfNodes(root.left)
    sr=sumOfNodes(root.right)
    return sl+sr+root.data


# Height or depth of tree
def heightOfTree(root:Node):
    if root==None:
        return 0
    ll=heightOfTree(root.left)
    lr=heightOfTree(root.right)
    return max(lr,ll)+1


# diameter of tree
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
    maxi.append(max(maxi[0], ld+rd+1))
    maxi.pop(0)
    return 1+max(ld,rd)
    
# check for Balanced Tree

if __name__=="__main__":
    # print(levelOrderTraversal1(a))
    # print(countNodes(a))
    # print(sumOfNodes(a))
    # print(heightOfTree(a))
    print(diameterOfTree2(a))