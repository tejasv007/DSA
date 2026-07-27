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
# a="Donetsk Kiev 560"
# newa=(a.strip().split())
# print(newa,)






# def bitMani(num:int,k:int):
#     ans=""
#     while(num>1):
#         a=num%2
#         num=num//2
#         ans=ans+str(a)
#     ans=ans+str(num)
#     new=""
#     if len(ans)<k:
        
#         for _ in range(k-len(ans)):
#             new+="0"
#     ans=ans+new
#     return ans[::-1]

# print(bitMani(0,2))
# print(bitMani(1,2))
# print(bitMani(2,2))
# print(bitMani(3,2))

# def decimal(s:str):
#     ans=0
#     l=0
#     while(l<len(s)):
#         if s[l]=="1":
#             ans+=(2**l)
#         l+=1 
#     return ans

# s="chef"
# d=dict()
# j=0
# k=2
# for i in s:
#     d[j]=i
#     j+=1
# newd=dict()
# for i in range(len(s)):
#     g=d.get(i)
#     newd[g]= decimal(bitMani(i,k))
# c=0
# k=1
# a=[1,2,2]
# d=Counter(a)
# s=sorted((d.values()))
# # print(s)
# m=s[0]
# # while(c<k):
# for i in range(1,len(a)):
#     if c>=k:
#         break
#     if d[a[i]]==m:
#         if a[i]!=a[i-1]: 
#             a[i]=a[i-1]
#             c+=1
#             s.remove(m)
#             m=s[0]
        

# print(a)

# def fn(num:int):
#     k=[chr(c) for c in range(65,90) ]
#     i=0
#     d=dict()
#     for j in range(num):
#         a=[]
#         n=int(input())
#         for i in range(n):
#             new=tuple(map(int,input().split()))
#             a.append(new)

#         d[k[i]]=a
#         i+=1
#     return d
# print(fn(3))

# def suspenseStr(s:str,n:int):
#     t=""
#     a=0
#     b=n-1
#     while(a<b):
#         if s[a]=="1":
#             t=t+s[a]
#         else:
#             t=s[a]+t
#         if s[b]=="1":
#             t=s[b]+t
#         else:
#             t=t+s[b]
#         a+=1
#         b-=1
#     return t
# cook your dish here\

# def suspenseStr(s:str,n:int):
#     flag=0
#     if n%2!=0:
#         flag=1
#     t=""
#     a=0
#     b=n-1
#     while(a<b):
#         if s[a]=="1":
#             t=t+s[a]
#         else:
#             t=s[a]+t
#         if s[b]=="1":
#             t=s[b]+t
#         else:
#             t=t+s[b]
#         a+=1
#         b-=1
#     if flag==1:
#         if s[a]=="1":
#             t=t+s[a]
#         else:
#             t=s[a]+t
#     return t
# print(suspenseStr("010111",6))

# print(suspenseStr("0101111",7))

# def fn(n):
    # res=[]
    # ans=0
    # res.append(ans)
    # for j in range(1,n):
    #     if (j & (j+1))>0:
    #         ans+=1
    #         # print(ans)
    #         res.append(ans)

    #     else:
    #         ans=0
        
    # # print(res)
    # m=max(res)
    # if m==0:
    #     print(1)
    # else:
    #     print(m+1)

# fn(7)



# if 3&2 ==0:
#     print("l")
# else:
    # print("kkk")
# import math as m
# print(1<<4)
# n=13
# print(n.bit_length())
# print(((1<<(n.bit_length()-1)),(n-8+1)))
new="d4"
newl=[]
# print(ord("a"))
# print(ord("h"))
new1=new[0]
new2=int(new[1])
# if ord(ord(new1)-1) >96 and ord(ord(new1)-1) <105:
#     if new2 >0 and
#     newl.append(chr(ord(new1)-1))

res="c2"
res1=res[0]
res2=int(res[1])
flag=0
if ord(res1)+1 ==ord(new1) or ord(res1)-1 ==ord(new1):
    if res2+2==new2 or res2-2==new2:
        flag=1
if ord(res1)+2 ==ord(new1) or ord(res1)-2 ==ord(new1):
    if res2+1==new2 or res2-1==new2:
        flag=1
    
if flag==1:
    if ord(res1) >96 and ord(res1)<105:
        if res2 >0 and res2<9:
            print("Yes")
        else:
            print("no")
    else:
        print("no")
else:
    print("No")

print(ord("1"))
print(ord("8"))