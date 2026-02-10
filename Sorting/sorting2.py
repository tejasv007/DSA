from collections import Counter
a=[1,2,3,3,3,3,4]
d=Counter(a)
# # print(max(d.values()))
# c=0
# k=4
# n=5
# a=[1,-2,-4,0,5]
# odda=[]
# m=max(a)
# for i in range(n):
#     odda.append(m-a[i])
# evena=[]
# m1=max(odda)
# for i in range(n):
#     evena.append(m1-odda[i])
# if k%2==0:
#     for i in evena:
#         print(i,end=" ")
# else:
#     for i in odda:
#         print(i,end=" ")
# a="Begin on Old Madras Road"
# # new=a.split(" ",2)
# # print(new)
# n=4
# for k in range(-1,(-(n)-1),-1):
#     print(k)
# print(ord("A"))
# a=[5,4,-1,7,8]
# def subArray(a:list):
    
#     for i in range(len(a)):
#         for j in range(i,len(a)):
#             print(a[i:j+1])
# subArray(a)

# a="AabBccCDDDDd"
# a1=a.lower()
# d=Counter(a1)
# print(d)
# new=list(d.values())
# (new.sort())
# l1=new[-1]
# l2=new[-2]

# cook your dish here
# t= int(input())
# for i in range(t):
#     b,g,x,y,n=map(int,input().split())
#     if n<(x+y) or x>b or y>g:
#         print(-1)
#     else:
#         total=b+g
#         r1=(total/n).__ceil__()
#         lb=(b-(r1*x))
#         lg=(g-(r1*y))
#         if lb<0 or lg<0:
#             print(-1)
#         else:
#             print(r1)

# cook your dish here
# t=int(input())
# for i in range(t):
#     s=input().strip()
#     m=[]
#     c=0
#     if len(s)==1:
#         print(-1)
#     else:
#         first=s[0]
#         last=s[-1]
#         flag=0
#         # print(first)
#         # print(last)
#         for j in range(1,len(s)-1):
#             # print(s[j])
#             if s[j]==first or s[j]==last:
              
#                 if flag==1:
#                     m.append(c)
#                     # print(c)
#                     c=0
#                     flag=0
#             else:
#                 if flag!=1:
#                     flag=1
#                 c+=1
                
#         m.append(c)
#     # print(m)

#     if max(m)==0:
#         print(-1)
#     else:
#         print(max(m))
a="Donetsk Kiev 560"
newa=(a.strip().split())
print(newa)
