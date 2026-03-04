# 1️⃣Valid or Balanced parenthesis ---checked
# s="()[{}()]"--valid
# s="()[{}(])"-- invalid
# Tc-O(2n)
# logic--> build two stack on store all or you can skip first one stack to made, i made it for ease
# build a var l which store the updated closing backets
# loop till first stack get empty 
# if encounter open one check if it is correspond l if not return false
# if yes pop out then assign l to next element in stack two
# at last check if stack is not empty and l is not empty then return false
# at last return true
def validParenthesis(s:str):
    news=[]
    for i in s:
        news.append(i)
    news2=[]
    l=""
    d={"{":"}","[":"]","(":")"}
    while(len(news)!=0):
        a=news.pop()
        if a in d.keys():
            if l=="":
                return False
            else:
                ans=d[a]
                if ans==l:
                    if len(news2)!=0:
                        l=news2.pop()
                    else:
                        l=""
                    
                else:
                    return False
        else:
            if l=="":
                l=a
            else:
                news2.append(l)
                l=a
    if len(news2)!=0 or l!="":
        return False
    return True

if __name__=="__main__":
    print(validParenthesis("()[{}(])"))