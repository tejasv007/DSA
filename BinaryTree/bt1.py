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

'''
Binary Tree is a non-linear and hierarchical data structure where each node has at most two children referred to as the left child and the right child.  The topmost node in a binary tree is called the root, and the bottom-most nodes(having no children) are called leaves.

Representation of Binary Tree
Each node in a Binary Tree has three parts:

Data
Pointer to the left child
Pointer to the right child

Terminologies in Binary Tree

Parent Node: A node that is the direct ancestor of a node(its child node).
Child Node: A node that is the direct descendant of another node (its parent).
Ancestors of a node: All nodes on the path from the root to that node (including the node itself).
Descendants of a node: All nodes that lie in the subtree rooted at that node (including the node itself).
Subtree of a node: A tree consisting of that node as root and all its descendants.
Edge: The link/connection between a parent node and its child node.
Path in a binary tree: A sequence of nodes connected by edges from one node to another.
Leaf Node: A node that does not have any children or both children are null.
Internal Node: A node that has at least one child.
Depth/Level of a Node: The number of edges in the path from root to that node. The depth/level of the root node is zero.
Height of a Binary Tree: The number of edges on the longest path from root to a leaf.

Properties of Binary Tree

The maximum number of nodes at level L of a binary tree is 2L.
The maximum number of nodes in a binary tree of height H is 2H+1 – 1.
Total number of leaf nodes in a binary tree = total number of nodes with 2 children + 1.
In a Binary Tree with N nodes, the minimum possible height or the minimum number of levels is ⌊log2N⌋.
A Binary Tree with L leaves has at least ⌈log2L⌉+ 1 levels.
Please refer Properties of Binary Tree for more details.

Operations On Binary Tree

Following is a list of common operations that can be performed on a binary tree:

1. Traversal: Depth-First Search (DFS) Traversal and Breadth-First Search (BFS) Traversal
2. Search: Search a node in Binary Tree
3. Insertion and Deletion: Prerequisite: Level Order Traversal, Insert in a Binary Tree and Delete from a Binary Tree

Advantages of Binary Tree

Efficient Search: Binary Search Trees (a variation of Binary Tree) are efficient when searching for a specific element, as each node has at most two child nodes when compared to linked list and arrays
Memory Efficient: Binary trees require lesser memory as compared to other tree data structures, therefore memory-efficient.
Binary trees are relatively easy to implement and understand as each node has at most two children, left child and right child.
Disadvantages of Binary Tree
Limited structure: Binary trees are limited to two child nodes per node, which can limit their usefulness in certain applications. For example, if a tree requires more than two child nodes per node, a different tree structure may be more suitable.
Space inefficiency: Binary trees can be space inefficient when compared to other data structures like arrays and linked list. This is because each node requires two child references or pointers, which can be a significant amount of memory overhead for large trees.

Applications of Binary Tree

Binary Tree can be used to represent hierarchical data.
Huffman Coding trees are used in data compression algorithms.
Useful for indexing segmented at the database is useful in storing cache in the system,
Binary trees can be used to implement decision trees, a type of machine learning algorithm used for classification and regression analysis.

Properties of Binary Trees

1. Maximum Nodes at Level 'l'
A binary tree can have at most 2l nodes at level l.

Level Definition: The number of edges in the path from the root to a node. The root is at level 0.
Proof by Induction:
Base case: For root (l = 0), nodes = 20 = 1.

Inductive step: If level l has 2l nodes, then the next level has at most twice as many: 

2×2l = 2l+1
2. Maximum Nodes in a Binary Tree of Height 'h'
A binary tree of height h can have at most 2h+1 - 1 nodes.

Height Definition: The longest path from the root to a leaf node. Please note that a tree with only one root node is considered to have height 0 and an empty tree (or root is NULL) is considered to have height "-1"
Formula Derivation: A tree has the maximum nodes when all levels are completely filled. Summing nodes at each level:  

1 + 2 + 4 +...+ 2h = 2h+1 - 1

Alternate Height Convention: Some books consider a tree with only one root node is considered to have height 1 and an empty tree (or root is NULL) is considered to have height 0. making the formula 2h - 1.
3. Minimum Height for 'N' Nodes
The minimum possible height for N nodes is ⌊log⁡2N⌋.

Explanation: A binary tree with height h can have at most 2h+1 - 1 nodes.

Rearranging:

N ≤ 2h+1 − 1
2h+1 ≥ N+1
h ≥ log2​(N+1)  - 1   (Taking log2 both sides)
h ≥ ⌊log2​N⌋

This means a binary tree with N nodes must have at least ⌊log⁡2N⌋ levels.

4. Minimum Levels for 'L' Leaves
A binary tree with L leaves must have at least ⌊log⁡2L⌋ levels.

Why? A tree has the maximum number of leaves when all levels are fully filled.

From Property 1:
L  ≤ 2l ( l is the level where leaves appear)

Solving for l:
lmin = ⌊log⁡2L⌋

This gives the minimum levels needed to accommodate L leaves.

5. Nodes with Two Children vs. Leaf Nodes
In a full binary tree (where every node has either 0 or 2 children), the number of leaf nodes (L) is always one more than the internal nodes (T) with two children:

L=T+1

Proof:

A full binary tree has a total of 2h+1 - 1 nodes.

Leaves are at the last level: L = 2h.

Internal nodes: T =2h (2−1) − 1= 2h  - 1.

Simplifies to L=T+1

6. Total Edges in a Binary Tree
In any non-empty binary tree with n nodes, the total number of edges is n - 1.

Every node (except the root) has exactly one parent, and each parent-child connection represents an edge.

Since there are n nodes, there must be n - 1 edges.

Additional Key Properties

Node Relationships
Each node has at most two children.
0 children → Leaf Node
1 child → Unary Node
2 children → Binary Node

Types of Binary Trees

Full Binary Tree → Every non-leaf node has exactly two children.
Complete Binary Tree → All levels are fully filled except possibly the last, which is filled from left to right.
Perfect Binary Tree → Every level is completely filled, and all leaves are at the same depth.
Balanced Binary Tree → The left and right subtrees differ in height by at most 1.

Tree Traversal Methods

Tree traversal is categorized into Depth-First Search (DFS) and Breadth-First Search (BFS):

DFS Traversals: Explore one branch fully before backtracking.
In-Order (LNR): Left → Node → Right (retrieves BST elements in sorted order).
Pre-Order (NLR): Node → Left → Right (used for tree reconstruction).
Post-Order (LRN): Left → Right → Node (helps in deleting or evaluating expressions).
BFS Traversals: Visit nodes level by level.
Level-Order: Processes nodes from top to bottom (used in shortest path algorithms).
Zig-Zag Traversal: Alternates left-to-right and right-to-left at each level (used in hierarchical structures).

Types of Binary Tree

A binary tree is a tree data structure where each node has at most two children. These two children are usually referred to as the left child and right child. It is widely used in applications such as binary search trees and heaps.

Types of Binary Tree
1. On the basis of number of children:
Full Binary Tree
Degenerate Binary Tree
Skewed Binary Trees
Full Binary Tree
 A Binary Tree is a full binary tree if every node has 0 or 2 children. We can also say a full binary tree is a binary tree in which all nodes except leaf nodes have two children. 

A full Binary tree is a special type of binary tree in which every parent node/internal node has either two or no children. It is also known as a proper binary tree.

Degenerate (or pathological) tree
A Tree where every internal node has one child. Such trees are performance-wise same as linked list. A degenerate or pathological tree is a tree having a single child either left or right.

Skewed Binary Tree
A skewed binary tree is a pathological/degenerate tree in which the tree is either dominated by the left nodes or the right nodes. Thus, there are two types of skewed binary tree: left-skewed binary tree and right-skewed binary tree.

2. On the basis of level completion:
Complete Binary Tree
Perfect Binary Tree
Balanced Binary Tree
Complete Binary Tree
A Binary Tree is a Complete Binary Tree if all the levels are completely filled except possibly the last level and the last level is filled from left side.

A complete binary tree is just like a full binary tree, but with two major differences:

Every level except the last level must be completely filled.
All the leaf elements must lean towards the left.

Perfect Binary Tree
A Binary tree is a Perfect Binary Tree in which all the internal nodes have two children and all leaf nodes are at the same level. 
A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes and all the leaf nodes are at the same level.

In a Perfect Binary Tree, the number of leaf nodes is the number of internal nodes plus 1.

Balanced Binary Tree
A binary tree is balanced if the height of the tree is O(log n) where n is the number of nodes.

For example, the AVL tree maintains O(log n) height by making sure that the difference between the heights of the left and right subtrees of every node is at most 1.

Following is an example of balanced binary tree. Here, d = depth of node = |Height of Left child - Height of Right child|.

Some Special Types of Trees:
On the basis of node values, the Binary Tree can be classified into the following special types:

Binary Search Tree
AVL Tree
Red Black Tree
B Tree
B+ Tree

Applications:

General Applications

DOM in HTML: Binary trees help manage the hierarchical structure of web pages.
File Explorer: They organize file systems for efficient navigation.
Expression Evaluation: Used in calculators and compilers to evaluate arithmetic expressions.
Routing Algorithms: Support decision-making in network routing.
Additional Uses: Various other applications that benefit from hierarchical data organization.
Hierarchical Data Representation
File Systems & Folder Structures: Organize files and directories.
Organizational Charts: Represent corporate or institutional hierarchies.
XML/HTML Parsing: Process structured data in documents.
Applications of Binary Search Trees (BST)
Efficient Operations: Enable quick searching, insertion, and deletion (average time complexity: O(log n); AVL and Red-Black Trees maintain this efficiency). Apart from these operations, additional operations like sorted traversal, floor and ceil are also efficient. Please note search, insert and delete are faster than array and linked list and slower than hashing, but hashing does not allow sorted traversal, floor and ceil operations.
Data Structures: Implement associative arrays, maps, and sets while keeping data sorted.

Applications of Binary Heap Trees

Expression Trees: Represent arithmetic expressions where internal nodes are operators and leaf nodes are operands.
Use Cases: Common in compilers and calculators.
Huffman Coding Trees: Essential in data compression (e.g., Huffman coding for lossless compression).
Decision Trees:
Machine Learning: Serve as models for classification and regression problems.
Conditional Processes: Represent decision-making steps.
Traversal Operations: Preorder, inorder, and postorder traversals aid in tasks like expression evaluation and tree reconstruction.

Advantages of Binary Trees

Structured Organization: Offers a clear, hierarchical data structure.
Efficient Searching and Sorting: BSTs facilitate fast data operations.
Balanced Storage: Variants like AVL and Red-Black trees ensure balanced performance (O(log n)).
Flexibility: Adaptable to various specialized structures (e.g., heaps, BSTs).
Recursion Support: Naturally aligns with recursive algorithms.
Scalability: Suitable for managing large dynamic datasets.
Disadvantages of Binary Trees
Skewed Trees: Unbalanced trees can degrade performance to O(n), similar to linked lists.
Memory Overhead: Additional pointers in each node increase memory usage.
Complex Implementation:Balancing trees (e.g., AVL, Red-Black) requires sophisticated rotations.
Limited Degree: Restricts each node to two children, which might not be ideal for some applications
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
# n--> no of nodes
# tc O(n) - sc
def inorder1(root: Node):
    if root==None:
        return root
    inorder1(root.left)
    print(root.data,end=" ")
    inorder1(root.right)
# -> iterative
# review it
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
# tc O(n) - sc

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
# tc O(n) - sc

def preorder1(root: Node):
    if root==None:
        return root
    print(root.data,end=" ")
    preorder1(root.left)
    preorder1(root.right)

# -> iterative
# tc O(n) sc O(n)
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