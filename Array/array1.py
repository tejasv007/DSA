'''
# ⭐⭐⭐EASY1⭐⭐⭐
Docstring for Array.array1
    to solve a question firstly use brute force approach --> better--> optimal
'''
# Largest element in an array
# ----1---- TC=O(Nlog(N)) --- Brute Force
def largest1(a:list):
    a.sort()
    return a[-1]

# ----2----- TC=O(N)---OPTIMAL
def largest2(a:list):
    m=-1
    for i in a:
        if m<i:
            m=i
    return m


# Second largest element in an array
# ----1---- TC=O(Nlog(N)) --- Brute Force
def secondLargest1(a:list):
    newa=list(set(a))
    if len(newa)==1:
        return 'not exist'
    newa.sort()
    return(newa[-2])
# ----2----- TC=O(2N)---BETTER
def secondLargest2(a:list):
    if len(a)==1:
        return "not exist"
    n=largest1(a) #O(N)
    l=-1
    for i in a:#O(N)
        if l<i and i<n:
            l=i
    return l 
# ----3---- TC=O(N)---OPTIMAL
def secondLargest3(a:list):
    if len(a)==1:
        return 'not exist'
    l1=-1
    l2=l1
    for i in a:
        if l1<i:
            l2=l1
            l1=i
        elif l1 >i and l2<i:
            l2=i
    return l2

# Check if the array is sorted or not
# --------------🧑🏿‍💻🧑🏿‍💻leetcode question is left
# ----1---- TC=O(Nlog(N)) --- Brute Force
def arrayIsSort1(a:list):
    new=sorted(a)
    if new==a:
        return True
    return False
# ----2----- TC=O(N)---OPTIMAL
def arrayIsSort2(a:list):
    num=a[0]
    for i in a:
        if num>i:
            return False
        num=i
    return True


# Remove duplicates from array

def duplicates1(a:list):
    return list(set(a))
# -------- change the given array dont build new one----correct
# TC-O(NlogN + N)----Brute force
def duplicates2(a:list,n:int):
    new=sorted(list(set(a)))
    l=len(new)
    for i in range(n):
        if i<l:
            a[i]=new[i]
        else:
            a[i]="_"
    return a

# ---TC-O(2N)-----Not optimal
# left⌛⌛  TC-O(N)---Optimal.....two pointer approach when
def duplicates3(a:list):
    new=[]
    if len(a)==1:
        return a
    new.append(a[0])
    for i in range(1,len(a)):
        if a[i-1]!=a[i]:
            new.append(a[i])
    for i in range(len(a)):
        if i<len(new):
            a[i]=new[i]
        else:
            a[i]="_"
    return a


if __name__=="__main__":
    a1=[1,5,3,7,32,7,8,4,8,45,42]
    a=[3,3,3,3,3,3,3]
    a2=[7,7,8,8,8,9]
   
    print(duplicates3(a2))
    # print(largest1(a))
    # print(secondLargest1(aa))
    # print(secondLargest2(a))
    # print(arrayIsSort1(a))
    # print(arrayIsSort2(a))
    # print(duplicates1(a2))

