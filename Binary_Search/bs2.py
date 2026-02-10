# 1️⃣FIRST AND LAST OCCURRENCE OF AN ELEMENT
#  if the ele exist in the arr then return the first and last index of the element
# if not exist then give -1 -1 instead of the indexies
# TC-O(logN)
def floor(arr:list, n:int, ele:int):
    l=0
    h=n-1
    res=h
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]>=ele:
            res=mid
            h=mid-1
        else:
            l=mid+1
    return res

def ceil(arr:list,n:int,ele:int):
    l=0
    h=n-1
    res=-1
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]<=ele:
            res=mid
            l=mid+1
        else:
            h=mid-1
    return res

def firstLastOccurrence(arr:list,ele:int):
    l=len(arr)
    a=floor(arr,l,ele)
    b=ceil(arr,l,ele)
    if arr[a]!=arr[b]:
        return [-1,-1]
    return [a,b]


# 2️⃣COUNT OCCURRENCE OF AN ELEMENT
# use floor and ceil just subtract and add 1
def countOccurence(arr:list, l:int, ele:int):
    a=floor(arr,l,ele)
    b=ceil(arr,l,ele)
    if arr[a]!=ele:
        return -1
    return b-a+1


# 3️⃣SEARCH ELEMENT IN ROTATE SORTED ARRAY (have unique element)
# doubt----💀💀💀
# Brute force --> TC-O(N)
# traverse whole array if ele match the target return index
def searchElement(arr:list, n:int,ele:int): 
    for i in range(n):
        if arr[i]==ele:
            return i



# TC-O(logN)
# 
def searchEle(arr:list, n:int, ele: int):
    l=0
    h=n-1
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]==ele:
            return mid
        if arr[l]<=arr[mid]:
            if arr[l]<=ele and ele<=arr[mid]:
                h=mid-1
            else:
                l=mid+1
        else:
            if arr[mid]<=ele and ele<=arr[h]:
                l=mid+1
            else:
                h=mid-1
            
    return mid



# 4️⃣SEARCH ELEMENT IN ROTATE SORTED ARRAY (have duplicate element)
# here dont return index return whether it exist or not
# doubt----💀💀💀
def searchEle(arr:list, n:int, ele: int):
    l=0
    h=n-1
    while(l<=h):
        mid=(l+h)//2
        if arr[mid]==ele:
            return mid
        if arr[l]==arr[mid] and arr[mid]==arr[h]:
            l=l+1
            h=h-1
            continue
        if arr[l]<=arr[mid]:
            if arr[l]<=ele and ele<=arr[mid]:
                h=mid-1
            else:
                l=mid+1
        else:
            if arr[mid]<=ele and ele<=arr[h]:
                l=mid+1
            else:
                h=mid-1
            
    return mid



# 5️⃣FIND MINIMUM IN ROTATED SORTED ARRAY
# here we find where the array had been rotated
# ie eliminate the sorted array but keep the smallest one in var min and work on the unsorted one
# TC-O(logN)
def minRotateSortedArray(arr:list,n:int):
    l=0
    h=n-1
    minVar=1234567890
    while(l<=h):
        mid=(l+h)//2
        if arr[l]<=arr[mid]:
            minVar=min(arr[l],minVar)
            l=mid+1
        else:
            minVar=min(arr[mid],minVar)
            h=mid-1
    return minVar


# 6️⃣
if __name__=="__main__":
    aa=[1,2,3,4,4,5,5,5,5,6,7,8,9]
    l=len(aa)
    a1=[7,8,9,1,3,4,6]
    # print(firstLastOccurrence(aa,5))
    # print(ceil(aa,l,5))
    # print(countOccurence(aa,l,4))
    # print(searchElement(a1,len(a1),3))
    # a2=[4,4,5,6,7,8,1,2,3,3,3]
    a2=[3,3,2,1,3,3,3]
    # a3=[8,9,1,2,4,6]
    a3=[3,4,5,1,2]
    print(minRotateSortedArray(a3,len(a3)))

    # print(searchEle(a2,len(a2),4))