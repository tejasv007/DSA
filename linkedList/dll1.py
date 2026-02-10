'''
Docstring for linkedList.dll1
Double linked list
-->linked list consist of nodes, where each node contains data field anf two pointers: one pointing to next and one to previous
--> can traverse in both forward and backward direction
APPLICATION
--> browse history--> navigating back and forward between pages
--> undo/ redo functionality
--> music player playlist 
'''

from ll1 import traversal_ll
# Representation of dll
class doublyNode:
    def __init__(self,data:int, prev=None, next=None):
        self.data=data
        self.prev=prev
        self.next=next

# def convertDllToArr(arr:list):
#     prev=None
#     next=None
#     for i in range(len(arr)):
#         new=doublyNode(arr[i])
#         new.prev=prev
#         if prev !=None:prev.next=new
#         new.next=None
#         prev=new
#     return

        



traversal_ll(a)