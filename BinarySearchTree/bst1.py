'''A Binary Search Tree (BST) is a type of binary tree data structure in which each node contains a unique key and satisfies a specific ordering property:

All nodes in the left subtree of a node contain values strictly less than the node’s value.
All nodes in the right subtree of a node contain values strictly greater than the node’s value.
This structure enables efficient operations for searching, insertion, and deletion of elements, especially when the tree remains balanced.
BSTs are widely used in database indexing, symbol tables, range queries, and are foundational for advanced structures like AVL tree and Red-Black tree. In problem solving, BSTs are used in problems where we need to maintain sorted stream of data.
Operations like search, insertion, and deletion work in O(Log n) time for a balanced binary search tree. In the worst-case (unbalanced), these degrade to O(n). With self-balancing BSTs like AVL and Red Black Trees, we can ensure the worst case as O(Log n)


Key Properties
Unique ordering of elements means duplicates are usually not allowed.
Inorder traversal of a BST gives sorted order of elements.
Average height: O(log n) (for balanced BST).
Worst case height: O(n) (when tree becomes skewed).
Operations in BST
Search : Finds whether a given key exists in the BST. Time Complexity on average is O(log n) and worst case is O(n)
Insertion : Insert a new node while maintaining BST property. Compare key with current node and move left/right recursively or iteratively. Time Complexity on average is O(log n) and worst case is O(n)
Deletion : Remove a node while keeping BST valid. Node has no children means remove directly. Node has one child means replace node with its child. Node has two children means replace node with inorder successor/predecessor and delete that successor/predecessor. Time Complexity: average O(logn) and O(n) worst case
Traversals : The four common tree traversals are Inorder (Left, Root, Right) which gives nodes in sorted order for a BST, Preorder (Root, Left, Right), Postorder (Left, Right, Root), and Level-order, which traverses the tree level by level using a queue.
# ---if duplicate provide and want us to made bst then l<=node<r 

Application of Binary Search Tree
Searching and indexing (e.g., maps, sets).
Dynamic sorting and range queries.
Implementing symbol tables in compilers.
Used in advanced structures (AVL Tree, Red-Black Tree, Splay Tree).

A BST supports operations like search, insert, delete, maximum, minimum, floor, ceil, greater, smaller, etc in O(h) time where h is height of the BST. To keep height less, self balancing BSTs (like AVL and Red Black Trees) are used in practice. These Self-Balancing BSTs maintain the height as O(Log n). Therefore all of the above mentioned operations become O(Log n). Together with these, BST also allows sorted order traversal of data in O(n) time.

A Self-Balancing Binary Search Tree is used to maintain sorted stream of data. For example, suppose we are getting online orders placed and we want to maintain the live data (in RAM) in sorted order of prices. For example, we wish to know number of items purchased at cost below a given cost at any moment. Or we wish to know number of items purchased at higher cost than given cost.
A Self-Balancing Binary Search Tree is used to implement doubly ended priority queue. With a Binary Heap, we can either implement a priority queue with support of extractMin() or with extractMax(). If we wish to support both the operations, we use a Self-Balancing Binary Search Tree to do both in O(Log n)
There are many more algorithm problems where a Self-Balancing BST is the best suited data structure, like count smaller elements on right, Smallest Greater Element on Right Side, etc.
 A BST can be used to sort a large dataset. By inserting the elements of the dataset into a BST and then performing an in-order traversal, the elements will be returned in sorted order. When compared to normal sorting algorithms, the advantage here is, we can later insert / delete items in O(Log n) time.
Variations of BST like B Tree and B+ Tree are used in Database indexing.
TreeMap and TreeSet in Java, and set and map in C++ are internally implemented using self-balancing BSTs, more formally a Red-Black Tree.

Advantages of Binary Search Tree (BST):
Efficient searching: O(log n) time complexity for searching with a self balancing BST
Ordered structure: Elements are stored in sorted order, making it easy to find the next or previous element
Dynamic insertion and deletion: Elements can be added or removed efficiently
Balanced structure: Balanced BSTs maintain a logarithmic height, ensuring efficient operations
Doubly Ended Priority Queue: In BSTs, we can maintain both maximum and minimum efficiently


Disadvantages of Binary Search Tree (BST):
Not self-balancing: Unbalanced BSTs can lead to poor performance
Worst-case time complexity: In the worst case, BSTs can have a linear time complexity for searching and insertion
Memory overhead: BSTs require additional memory to store pointers to child nodes
Not suitable for large datasets: BSTs can become inefficient for very large datasets
Limited functionality: BSTs only support searching, insertion, and deletion operations
The main competitor Data Structure of BST is Hash Table in terms of applications. We have discussed BST vs Hash Table in details for your reference.
'''
# ⚡⚡⚡⚡in recursion sc is the auxillary call stack


class Node:
    def __init__(self,data:int,left=None, right=None):
        self.left=left
        self.right=right
        self.data=data
# 1️⃣Search in a Binary Search Tree ✅checked
#       1
#      / \ 
#     2    3
#    / \  / \
#   4  10 9 10
#    \
#     5
#      \ 
#       6
# given the int value, if exist return the node else return none
# tc sc o(logn) as we only traverse the heights
# here we apply if else only
def searchInBst(root:Node,val:int):
    if root==None:return None
    if val==root.data:return root
    elif val<root.data:
        return searchInBst(root.left,val)
    else:
        return searchInBst(root.right,val)


# 2️⃣Ceil in a Binary Search Tree
# given a key find the node which have min value such the node value>=key
# tc sc O(logn) (auxillary call stack as it is in recursion)
def ceilBST(root,t):
    a=[]
    ceilInBst(root,t,a)
    return min(a)
def ceilInBst(root:Node,t:int,a:list):
    if root==None:return 
    if t<=root.data:
        a.append(root.data)
        ceilInBst(root.left,t,a)
    else:
        ceilInBst(root.right,t,a)
    
# 3️⃣floor in a Binary Search Tree
# given a key find the node which have max value such the node value<=key
# tc sc O(logn) (auxillary call stack as it is in recursion)
def floorBST(root,t):
    a=[]
    floorInBst(root,t,a)
    return max(a)
def floorInBst(root:Node,t:int,a:list):
    if root==None:return 
    if t<=root.data:
        # a.append(root.data)
        floorInBst(root.left,t,a)
    else:
        a.append(root.data)
        floorInBst(root.right,t,a)


# 4️⃣Insert a given Node in Binary Search Tree ✅checked
# here we use simple concept that if t <root val go to left and if left is none we get our point
# and if t>root val fo to right and if right is none we ge our point
# we use here recursion but striver use loop

# tc sc O(logn)
def insertBSTHelper(root,t):
    if t<root.data:
        if root.left==None:
            new=Node(t)
            root.left=new
            return
        insertBSTHelper(root.left,t)
    else:
        if root.right==None:
            new=Node(t)
            root.right=new
            return
        insertBSTHelper(root.right,t)
def insertBST(root,val):
    if root==None:
        return Node(val)
    insertBSTHelper(root,val)
    return root

# 5️⃣ Delete a Node in Binary Search Tree----💀💀💀💀💀💀💀💀💀💀💀💀 --checked✅✅✅
# but made by ai

def maxNode(root: Node):
    # returns the node with maximum value in a subtree
    current = root
    while current and current.right:
        current = current.right
    return current


def minNode(root: Node):
    # returns the node with minimum value in a subtree
    current = root
    while current and current.left:
        current = current.left
    return current


def deleteNodeInBST(root: Node, t: int):
    if root is None:
        return None

    if t < root.data:
        root.left = deleteNodeInBST(root.left, t)
    elif t > root.data:
        root.right = deleteNodeInBST(root.right, t)
    else:
        # found node to delete
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # node with two children: replace with inorder successor (min in right subtree)
        successor = minNode(root.right)
        root.data = successor.data
        root.right = deleteNodeInBST(root.right, successor.data)

    return root


# -------by me
def maxInLeft(root:Node):
    curr=root
    while (curr.right is not None):
        curr=curr.right
    return curr


def findDelete(root:Node,t:int):
    if root==None:
        return None
    if root.data==t:
        return root
    if t<root.val:
        return findDelete(root.left,t)
    else:return findDelete(root.right,t)

def deleteBST(root,t):
    n=findDelete(root,t)
    if n==None:
        return root
    # if root==n:
    #     if n.left==None and n.right==None:
    #         return None
    if n.left==None and n.right==None:
        if n.data==root.data:return None
        return root
    if n.left!=None and n.right==None:
        n=n.left
        return root
    if n.left==None and n.right!=None:
        n=n.right
        return root
    if n.left!=None and n.right!=None:
        lasta=maxInLeft(n.left)
        n.data=lasta.data
        lasta.val=None
        return root
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
    # print(ceilBST(a,10))
    # print(floorBST(a,10))
    print(deleteBST(h,6))