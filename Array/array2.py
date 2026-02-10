'''
# ⭐⭐⭐EASY2⭐⭐⭐
Docstring for Array.array1
    to solve a question firstly use brute force approach --> better--> optimal
'''
# Left rotate the array by one place
# brute force---TC-O(N)--optimal also
def leftRotateOne(a:list,n:int):
    new=a[0]
    a.remove(a[0])
    a.append(new)
    return a

# Left rotate the array by k place
# brute force---TC=O()---left
def leftRotateK(a:list, n:int,k:int):
    if n==k:
        return a
    new1=a[:k]
    new2=a[k:]
    new2.extend(new1)
    return new2

if __name__=="__main__":
    a=[1,2,3,4,5]
    print(leftRotateK(a,5,4))