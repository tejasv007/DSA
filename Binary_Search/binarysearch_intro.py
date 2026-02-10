'''
Docstring for Binary_Search.binarysearch_intro
--> binary search applicable to only sorted data
--> Binary Search is a searching algorithm that operates on a sorted or monotonic search space, repeatedly dividing it into halves to find a target value or optimal answer in logarithmic time O(log N)
APPLICATIONS
Searching in sorted arrays
Finding first/last occurrence or closest match in a sorted array
Database indexing — Used in B-trees and similar structures for fast data lookup.
Debugging in version control — Tools like git bisect use binary search to isolate faulty commits.
Network routing & IP lookup — Efficiently find routing entries in tables sorted by address ranges.
File systems & libraries — Fast search through sorted directories or symbol tables.
Gaming/graphics — Collision detection or ray tracing using sorted spatial data.
Machine learning tuning — Efficient hyperparameter search (e.g., learning rate, thresholds).
Optimization problems & competitive programming — Solve boundary-value challenges by narrowing search space.
Advanced data structures — Binary search trees, self-balancing BSTs, and fractional cascading rely on search logic.

REAL LIFE
Dictionary Lookup: Open a dictionary to the middle, check if the word is in the first or second half, and repeat on the relevant half.
Number Guessing Game: When guessing a number from 1-100, always pick the midpoint (50) to eliminate half the possibilities.
Phonebook Search: Look for a name by opening the book in the middle and deciding whether to look earlier or later.
Physical Index/File Search: Find a specific page in a sorted, indexed file cabinet by jumping to the middle divider.
Version Control (Git Bisect): Identify a buggy code commit by testing the midpoint commit and halving the search range of commits.
Price Filtering: Online stores use this to quickly locate items within a specific price range in a sorted list.
Checking Test Scores: A teacher finds a specific grade by opening a sorted list of student scores in the middle.
Finding a Page Number: Open a thick book in the middle to locate a specific page number.
Autocorrect/Spell Check: Dictionary words are searched using this method to quickly find matches.
'''

# ---one things to be mind when writing binary search algorithm that is when element is not in the data then the high< low 

# BINARY SEARCH
# TC-O(logN)
# ----iterative approach 
# --> build 3 var low,mid and high 
# --> high at last index and low at first index
# --> check mid index has val equal to given value if not then
#   --> mid one> ele  then high=mid-1
#   --> mid one< ele then low =mid+1

def binarySearch(arr:list, n:int,ele:int):
    l=0
    h=n-1
    while(l<=h):
        mid=(h+l)//2
        if arr[mid]==ele:
            return mid
        elif ele>arr[mid]:
            l=mid+1
        else:
            h=mid-1
    return "not in list"

# ----recursive approach  
def binaryRec(arr:list,ele:int,low:int,high:int):
    if high>low:
        return "not found"
    mid=(low+high)//2
    if arr[mid]==ele:
        return mid
    if arr[mid]<ele:
        return binaryRec(arr,ele,mid+1,high)
    if arr[mid]>ele:
        return binaryRec(arr,ele,low, mid-1)
  

# LOWER BOUND----✔️✔️✔️✔️recheck one more time
# --smaller index such that arr[index]>=n
# a=[1,2,3,4,5,7,8,9,10]--> search for 6 not found then ans be 5 index
# here if we find ele then okay 
# make a var res which store the last index as hypothetically it would be the max ele which can be greater then the ele
# store the mid greater than ele in res
# TC_O(logN)

def lowerBound(arr:list,n:int,ele:int):
    l=0
    h=n-1
    res=n-1
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]>=ele:
            res=mid
            h=mid-1
        else:
            l=mid+1
      
    return res

# UPPER BOUND
# --smaller index such that arr[index]>n
def upperBound(arr:list, n:int, ele:int):
    l=0
    h=n-1
    res=n
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]>ele:
            res=mid
            h=mid-1
        else:
            l=mid+1
    return res


# SEARCH INSERT POSITION
# similar to lower bound if ele is missing where should be if it is inserted in array


# FLOOR AND CEIL IN A SORTED ARRAY
# FLOOR--> largest ele >=x
# CEIL--> smallest ele<=x
# if no find then floor ==ceil== ele
# ---floor as ceil is similar to lower bound
def floor(arr:list,n:int,ele:int):
    l=0
    h=n-1
    ans=-1
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]<=ele:
            ans=arr[mid]
            l=mid+1
        else:
            h=mid-1
    return ans

if __name__=="__main__":
    a=[1,2,3,4,6,6,6,8,9,10]
    a1=[1,1,1,1,1,1]
    # print(binarySearch(a1,6,1))
    # print(binaryRec(a,99,0,9))
    print(lowerBound(a1,len(a1),1))
    # print(upperBound(a1,len(a1),8))
    # print(floor(a,len(a),0))