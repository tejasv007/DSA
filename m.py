# def fn(n:int):
#     b=n.bit_length()
#     newn=(1<<b)-1
#     return n^newn

# print(fn(10))
# def fn1(arr:list):
#     stack=[]
#     n=0
#     l=len(arr)
#     while(n<l):
#         if len(stack)==0:
#             stack.append(arr[n])
#         else:
#             # while(len(stack)!=0 and stack[-1]>arr[])
#             if arr[n]>stack[-1]:
#                 stack.append(arr[n])
#         n+=1
#     return len(stack)


# print(fn1([3,4,5,8,9]))

def fn2(k:int):
    t=10
    n=k
    ans=1
    while(n>10):
        ans*=(n%t)
        
        n=n//10
    ans*=(n)
    return ans

# print(fn2(5244))
# print(345%100)
def fn3(arr:list,k:int):
    m=0
    l=0
    r=k-1
    ll=len(arr)
    for i in range(k-1):
        if arr[i]=='a':
            m+=1
    ans=m
    while(r<ll):
        if arr[r]=='a':
            m+=1
        ans=max(ans,m)
        if arr[l]=='a':
            m-=1
        l+=1
        r+=1
    
    return ans

# print(fn3('abbbaabbb',5))
# ---left use recursion
def fnhelper4(num:int):
    newnum=str(newnum)
    ans2=0
    for i in newnum:
        a=int(i)
        ans2+=a
    

def fn4(num:int,k:int):
    ans1=0
    num=str(num)
    for i in num:
        a=int(i)
        ans1+=a
    newnum=ans1*k
    newnum=str(newnum)
    ans2=0
    for i in newnum:
        a=int(i)
        ans2+=a
    return ans2

# print(fn4(99,3))
def fn5(arr:list,d:int, x:int):
    count=0
    flag=0
    if d%2==0:
        flag=1
    if flag==0:
        for i in arr:
            if i%2==0:
                count+=1
    else:
        for i in arr:
            if i%2!=0:
                count+=1       
    return count*x

# print(fn5([2,5,1,6,8],3,300))
# part 2 advance---
def advanceFn1(n:int,arr:list):
    a=arr[0]
    new=arr.count(a)
    return n-new

# print(advanceFn1(5,[1,2,3,2,2]))
# ---check it once
def advanceFn2(n:int,price:int,arr:list):
    ans=[]
    m=-1
    l=0;r=0
    while(r<n):
        ans.append(arr[r])
        if sum(ans)>=price:
            ans=[]
            l+=1
        else:
            m=max(m,len(ans))
            print(ans)
        r+=1
    return m

a=[30 ,40 ,50 ,20 ,80 ,10 ,90 ,10 ,10 ,10 ]
a2=[10 ,90 ,80 ,20 ,90 ,60 ,40 ,60 ,70 ,75 ]
# print(advanceFn2(10,100,a2))

# def advanceFn4(n:int,coor=list):
    
# print(5&6)

# part 3---------
# check tc O(n)
def advanceCodeFn1(n:int,k:int):
    m=0
    a=[]
    for i in range(1,(n//2)+1):
        if i not in a:
            if n%i==0:
                if i not in a:
                    a.append(i)
                if n//i not in a:
                    a.append(n//i)
                m+=2
    a.sort()
    print(a)
    if k>len(a):
        return -1
    return a[k-1]

    #     if n%i==0:
    #         m+=2
            
    #         a.append(i)
    #     if m==k:
    #         return i,a
    # return 1,a


# print(advanceCodeFn1(12,3))

def advanceCodeFn2(n:int,a:list):
    ans=0
    prev=a[0]
    for i in range(1,n):
        # prev+=a[i]
        # ans+=(prev+a[i+1])
        prev+=a[i]
        ans+=prev
    return ans

# print(advanceCodeFn2(5,[1,2,3,4,5]))
from math import *
def advanceCodeFn3(n:list):
    ans=0
    sqrs=[]
    for i in range(1,n+1):
        if n%i==0:
            new=int(sqrt(i))
            if new**2 ==i:
                sqrs.append(i)
                if i==1:
                    sqrs.pop()
            else:  
                flag=1
                for j in sqrs:
                    if i%j==0:
                        flag=0
                        break
                if flag==1:
                    ans+=1

    return ans

# print(advanceCodeFn3(72))
# ----not understand question
def advanceCodeFn4(n:int,l:list):
    ans=0
    for i in l:
        new=(2**i)
        if new>99:
            ans+=(new%100)
        else:
            ans+=new
    return ans%100
# print(23456//100)

# fn5--- dp
# print(advanceCodeFn4(4,[8,6,7,4]))

# NOTEPAD📒📒📒 
# 1
def notepadFn1(w:list,v:list):
    ans=w//2
    fourw=ans-v
    twow=ans-fourw
    return fourw,twow

# print(notepadFn1(540,200))

# 2
from collections import Counter
def fn1(s):
    new=Counter(s)
    newlist=list(new.values())
    newlist.sort(reverse=True)
    print(new)
    print(newlist)
    c=0
    flag=0
    for i in newlist:
        if i%2==0:
            c+=(i)
        else:
            if i>1:
                if flag==1:
                    c+=(i-1)
                else:
                    c+=i
                    flag=1
            else:
                if flag==0:
                    flag=1
                    c+=1
    return c

s="civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
# print(fn1(s))
# print(fn1("abccccdd"))


# -----------------
def fnnnnnnlc(people,limit):
    people.sort()
    l=0
    r=len(people)-1
    c=0
    while(l<=r):
        if l==r:c+=1;break
        if (people[l]+people[r])>limit and l<r:
            c+=1
            r-=1
        else:
            l+=1
            r-=1
            c+=1
    return c
# print(fnnnnnnlc([3,2,2,1],3))

def fnnnnnlc1(s):
    d=[]
    j=0
    new=[]
    for i in s:
        d.append([j,int(i)])
        new.append(int(i))
        j+=1
    d=sorted(d,key=lambda i:i)
    new.sort(reverse=True)
    print(d,new)

# print(fnnnnnlc1("1432219"))
# d={2:23,3:53}
# a=list(d.values())
# (a.sort())
# print(a)

def selection_sorting(n:int, arr: list):
    if n==0 or n==1:
        return arr
    
    for i in range(n):
        m=arr[i]
        c=i
        for j in range(i,n):
            if m>arr[j]:
                m=arr[j]
                c=j
        new=arr[i]
        arr[i]=arr[c]
        arr[c]=new
     
            
    return arr

# ---
# a=[2,2,4,5,3,4,5]
# a.remove(2)
# print(a)
# s="winter"
# m=-234
# a=0
# b=0
# l=len(s)
# flag=0
# while(b<l):
#     if flag==0:
#         if s[b]=="u" or s[b]=="o":
#             b+=1
#             flag=1
#             print(b)

#         else:
#             b+=1
#             a=b
        
#     else:
#         if s[b]=="w":
#             b+=1
#             flag=0
#         else:
#             if s[b]=="u" or s[b]=="o":
#                 a=b
#                 flag=0
#             else:
#                 b+=1
#                 a=b
#                 flag=0
#         # print(b)
#     if (b-a)%2!=0:
#         m=max(m,b-a)
#     print(b,a)
# print(m) \

# n,kk=map(int,input().split())
# a=list(map(int,input().split()))
# s=sum(a)
# c=0
# for j in range(n-1):
#     for k in range(j+1,n):
#         new=s-a[j]-a[k]
#         new=new//2
#         pp=((new+a[j]+a[k]))
#         # print(pp)
#         if pp>kk:
#             c+=1
# print(c)

# print(3|4)   
# ---✅✅ cmplt leetcode
# def longestcommonprefix(s):
#     if len(s)==1:
#         return s[0]
#     ans=''
#     i1=len(s[0])
#     j1=len(s[1])
#     i=0;j=0
#     while(i <i1 and j<j1):
#         if s[0][i]==s[1][j]:
#             ans=ans+s[0][i]
#         else:break
#         i+=1
#         j+=1
    
#     if ans=="":return ans
#     l=len(ans)
#     for new in range(2,len(s)):
#         if s[new][:l]==ans:
#             pass
#         else:
            
#             while(l>0):
#                 if s[new][:l]==ans[:l]:
#                     break
#                 else:
#                     l-=1
            
#     return ans[:l]

# a="unmm"
# # print(a[:0])
# s=['flower','flow','flot']
# s=['dd','ff','ddddd']
# print(longestcommonprefix(s))
def validSudoku(board):
    dd=dict()
    for i in range(1,10):
        dd[str(i)]=0
    print('mmmmm')
    
    for i in range(9):
        for j in range(9):
            if board[i][j]==".":
                pass
            elif dd[board[i][j]]==1:
                print(i,j)
                print( board[i][j])
                return False
            else:
                dd[board[i][j]]+=1
        for i in range(1,10):
            dd[str(i)]=0
    # print('mmmmm')
    
    dd=dict()
    for i in range(1,10):
        dd[str(i)]=0
    for i in range(9):
        for j in range(9):
            if board[j][i]==".":
                pass
            elif dd[board[j][i]]==1:
                return False
            else:
                dd[board[j][i]]+=1
        for i in range(1,10):
            dd[str(i)]=0
    dd=dict()
    for i in range(1,10):
        dd[str(i)]=0
    
    # while(ii<3):
    #     for j,k in zip(range(3*ii,3*(ii+1)),range())
    
    # i=0
    # new=0
    # # print('mmmmm')
    # while(i<3):
    #     ii=0
    #     for j in range(3*new,3*(new+1)):
    #         while(ii<3):
    #             for k in range(3*ii,3*(ii+1)):
    #                 if board[j][k]==".":
    #                     pass
    #                 elif dd[board[j][k]]>0:
    #                     return False
    #                 else:
    #                     dd[board[j][k]]+=1
    #             ii+=1
    #             dd=dict()
    #             for i in range(1,10):
    #                 dd[str(i)]=0
    #     new+=1
    #     i+=1
    # ii=0
    # while(ii<3):
    #     for j in range(3*ii):
    #         for k in range(3):
    #             if board[j][k]==".":
    #                 pass
    #             elif dd[board[j][k]]==1:
    #                 return False
    #             else:
    #                 dd[board[j][k]]+=1
    #     dd=dict()
    #     for i in range(1,10):
    #         dd[str(i)]=0
    #     for j in range(3*ii):
    #         for k in range(3,6):
    #             if board[j][k]==".":
    #                 pass
    #             elif dd[board[j][k]]==1:
    #                 return False
    #             else:
    #                 dd[board[j][k]]+=1
    #     dd=dict()
    #     for i in range(1,10):
    #         dd[str(i)]=0
    #     for j in range(3*ii):
    #         for k in range(6,9):
    #             if board[j][k]==".":
    #                 pass
    #             elif dd[board[j][k]]==1:
    #                 return False
    #             else:
    #                 dd[board[j][k]]+=1
    #     dd=dict()
    #     for i in range(1,10):
    #         dd[str(i)]=0
    #     ii+=1
        
    # return True


board1 = [["8","3",".",".","7",".",".",".","."] ,["6",".",".","1","9","5",".",".","."] ,[".","9","8",".",".",".",".","6","."] ,["8",".",".",".","6",".",".",".","3"] ,["4",".",".","8",".","3",".",".","1"] ,["7",".",".",".","2",".",".",".","6"] ,[".","6",".",".",".",".","2","8","."] ,[".",".",".","4","1","9",".",".","5"] ,[".",".",".",".","8",".",".","7","9"]]
board = [["5","3",".",".","7",".",".",".","."] ,
         ["6",".",".","1","9","5",".",".","."] ,
         [".","9","8",".",".",".",".","6","."] ,
         ["8",".",".",".","6",".",".",".","3"] ,
         ["4",".",".","8",".","3",".",".","1"] ,
         ["7",".",".",".","2",".",".",".","6"] ,
         [".","6",".",".",".",".","2","8","."] ,
         [".",".",".","4","1","9",".",".","5"] ,
         
         [".",".",".",".","8",".",".","7","9"]]

bb=[[".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]]
# print(validSudoku(bb))
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList( head):
    if head==None:return Node(None)
    newhead=Node(head.val,head.next)
    temp=head.next
    temp1=newhead
    d=dict()
    d1=dict()
    i=1
    d[temp]=0
    d[temp1]=0
    while(temp!=None):
        d[temp]=i
        newOne=Node(temp.val)
        d1[i]=newOne
        temp1.next=newOne
        temp1=newOne
        temp=temp.next
        i+=1
    temp=head
    temp1=newhead
    newd=dict()
    newd1=dict()
    i=0
    while(temp!=None):
        a=temp.random
        if a==None:
            newd[i]=None
        else:
            aa=d[a]
            newd[i]=aa
        temp=temp.next
        i+=1
    i=0
    while(temp1!=None):
        if newd[i]==None:
            temp1.random=None
        else:
            temp1.random=d1[newd[i]]
        temp1=temp1.next
        i+=1
    return newhead


    
        
# a=[3,5,3,2,5]
# a.sort()
# print(a)
new='iroir'
# while(len(new)>1):
#     ans=0
#     for i in new:
#         ans+=int(i)**2
#     new=str(ans)
# height = [1,8,6,2,5,4,8,3,7]
height=[1,1]
new=-123456789
i=0
j=len(height)-1
while(i<=j):
    a=0
    new=max(new,((j-i)*min(height[i],height[j])))
    if height[i]>=height[j]:
        a=height[j]
        j-=1
    else:
        a=height[i]
        i+=1
    
# print(new)
# cook your dish here
# --------function of making an array of equal value
def fn1(mini,maxi):
    count=0
    n=0
    while(mini!=maxi):
        maxi=maxi//2
        count+=1
        if mini>maxi:
            mini=mini//2
            count+=1
            n+=1
    return mini, count,n
def fn(mini,maxi):
    count=0
    n=0
    while(mini!=maxi):
        mini=maxi|mini
        count+=1
        if mini>maxi:
            maxi=maxi|mini
            count+=1
            n+=1
    return mini, count,n

# print(3,5)
# print(fn(2,7))
# print(7|2)
a=[23,4,5,6,7,]
# a.sort(reverse=True)
# print(a)
# cook your dish here
# t=int(input())
# for i in range(t):
#     n=int(input())
#     a=list(map(int,input().split()))
#     ans=min(a[0],a[1])
#     for j in range(1,n):
#         m=min(a[j-1],a[j])
#         if m>ans:
#             ans=m
#     print(ans)

def fn(i,n,arr):
    if len(arr)==n:
        print(arr)
        return
    arr.append(i)
    fn(i+1,n,arr)
    arr.pop()
    fn(i+1,n,arr)

# fn(1,4,[])
# n,k=map(int,input().split())
# w=list(map(int,input().split()))
# w.sort(reverse=True)
# a=sum(w[:k])
# b=sum(w[k:])
# ans1=a-b
# a1=sum(w[:(n-k)])
# b1=sum(w[(n-k):])
# ans2=a1-b1
# print(ans1,ans2)
n,p=1,1
s="LN"
dir=s[p-1]
m1=0
for j in range(p):
    if s[j]!=dir:
        m1+=1
m2=0
for j in range(p,n):
    if s[j]!=dir:
        m2+=1
print(min(m2,m1))