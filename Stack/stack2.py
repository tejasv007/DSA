'''
What Are They?
These are three ways to write mathematical or logical expressions, differing only in where the operator is placed relative to its operands.

The Three Notations
Infix Notation
The operator is placed between the operands. This is the notation humans naturally use.
A + B, (A + B) * C
Prefix Notation (Polish Notation)
The operator is placed before the operands. Invented by Polish mathematician Jan Łukasiewicz.
+ A B, * + A B C
Postfix Notation (Reverse Polish Notation - RPN)
The operator is placed after the operands.
A B +, A B + C *

Why Do They Exist? (Uses)
Infix is designed for human readability. It requires parentheses and operator precedence rules to avoid ambiguity.
Prefix and Postfix are designed for machines. They are completely unambiguous — no parentheses or precedence rules are needed. This is why compilers and interpreters use them internally.
Postfix is used in stack-based virtual machines (like the JVM), calculators (HP calculators famously used RPN), and expression parsers. Prefix is used in LISP and similar languages, and in logic/math theory.

How to Convert: Infix → Postfix (Shunting-Yard Algorithm)
Rules using a stack:

Read tokens left to right
If operand → output it directly
If operator → pop operators from stack with higher or equal precedence to output, then push current operator
If ( → push to stack
If ) → pop to output until ( is found
At end → pop all remaining operators to output

Example: A + B * C

Real-World Applications

Compilers convert infix source code to postfix (or a tree) for execution
Expression trees — prefix is essentially a pre-order traversal, postfix is post-order
HP Calculators use RPN (postfix) for direct entry
Stack machines like the JVM execute postfix bytecode
LISP/Scheme use prefix notation natively: (+ a (* b c))
Spreadsheet formula parsers internally convert infix formulas to postfix

'''
# 1️⃣Infix to Postfix
# a+b*(c^d-e)-->abcd^e-*+
# use a stack for storing operators....
# if current operator have greater precedence then push in otherwise pop out the operators in stack till current have greater precedence than the stack top one
# if encounter backet just push in stack, when closed backet occur pop all the operators before the backet in stack and also pop the open backet but dont include it in ans
# if stack is not empty after traversal, pop out all and add to ans
# TC-O(2N)
# SC-O(2N)

def infixToPostfix(s:str):
    stack=[]
    ans=''
    d={
        "^":3,"*":2,"/":2,"+":1,"-":1,"(":0,")":0
    }
    
    for i in s:
        if (ord(i)>=65 and ord(i) <91) or (ord(i)>96 and ord(i)<123) or (ord(i)>=ord("0") and ord(i)<=ord("9")):
            ans=ans+i
        elif i=="(":
            stack.append(i)
        elif i==")":
            while(len(stack)!=0 and stack[-1]!="("):
                ans=ans+stack[-1]
                stack.pop()
            stack.pop()
        else:
            while(len(stack)!=0 and d[i]<=d[stack[-1]]):
                ans=ans+stack.pop()
                
            stack.append(i)
    while(len(stack)!=0):
        ans=ans+stack.pop()
    return ans

# 2️⃣Infix to Prefix
# (A+B)*C-D+F-->+-*+ABCDF
# 1. reverse the s--- when reversing change open bracket to closed brackets and vice versa
# 2. infix to postfix-- here dont pop out the operator equal priority to current one just push the current one in stack 
# 3. reverse the s

# TC-O(3N) SC-O(N)
def infixToPrefix(s:str):
    d={
        "^":3,"*":2,"/":2,"+":1,"-":1,"(":0,")":0
    }
    news=""
    for i in range(len(s)-1,-1,-1):
        if s[i]==")":
            news=news+"("
        elif s[i]=="(":
            news=news+")"
        else:
            news=news+s[i]
    ans=""
    stack=[]
    for i in news:
        if (ord(i)>=ord("a") and ord(i)<=ord("z")) or (ord(i)>=ord("A") and ord(i)<=ord("Z")) or (ord(i)>=ord("0") and ord(i)<=ord("9")):
            ans=ans+i
        elif i=="(":
            stack.append(i)
        elif i==")":
            while(len(stack)!=0 and stack[-1]!="("):
                ans=ans+stack.pop()
            stack.pop()
        else:
            if i=="^":
                while(len(stack)!=0 and d[i]<=d[stack[-1]]):
                    ans=ans+stack.pop()
            else:
                while(len(stack)!=0 and d[i]<d[stack[-1]]):
                    ans=ans+stack.pop()
            stack.append(i)
    while(len(stack)!=0):
        ans=ans+stack.pop()
    return ans[::-1]
            

# 3️⃣Postfix to Infix
# AB-DE+F*/-->((A-B)/((D+E)*F))
# use a stack put operand in 
# when encounter operator put between first two element of stack and push the whole as one in stack
# Tc-O(2n)-->lang specific--check
# Sc-O(N)
def postfixToInfix(s:str):
    stack=[]
    a=""
    d=["^","*","/","+","-"]
    for i in s:
        if i in d:
            a=stack.pop()
            b=stack.pop()
            b="("+b+i+a+")"
            stack.append(b)


        else:
            stack.append(i)
    return "".join(stack)


# 4️⃣Prefix to infix
# *+PQ-MN-->((P+Q)*(M-N))
# similar to postfix to infix --> 2 difference
# reverse the string
# change the assignment of operand between the operator
# Tc-O(2n)->lang specific
# Sc-O(N)
def prefixToInfix(s:str):
    stack=[]
    a=""
    d=["^","*","/","+","-"]
    news=s[::-1]
    for i in news:
        if i in d:
            a=stack.pop()
            b=stack.pop()
            b="("+a+i+b+")"
            stack.append(b)

        else:
            stack.append(i)
    return "".join(stack)


# 5️⃣Postfix to Prefix
# AB-DE+F*/-->/-AB*+DEF
# here when we encounter operator pop the two out 
#append the operator before the two as a single one
# then append it to stack
# Tc-O(2n)-->lang specific--check
# Sc-O(N)
def postfixToPrefix(s:str):
    stack=[]
    d=["^","*","/","+","-"]
    for i in s:
        if i in d:
            a=stack.pop()
            b=stack.pop()
            stack.append(i+b+a)
        else:
            stack.append(i)
    return stack[0]


# 6️⃣Prefix to Postfix
# /-AB*+DEF-->AB-DE+F*/
# similar to postfix to prefix -->
# just append the operator after the first two elements and except it all will be exact as it is
# Tc-O(2n)-->lang specific--check
# Sc-O(N)
def prefixToPostfix(s:str):
    stack=[]
    news=s[::-1]
    d=["^","*","/","+","-"]
    for i in news:
        if i in d:
            a=stack.pop()
            b=stack.pop()
            stack.append(a+b+i)
        else:
            stack.append(i)
    return stack[0]


if __name__=="__main__":
    # print(infixToPostfix("a+b*(c^d-e)"))
    # print(infixToPrefix("(A+B)*C-D+F"))
    # print(postfixToInfix("AB-DE+F*/"))
    # print(prefixToInfix("*+PQ-MN"))
    # print(postfixToPrefix("AB-DE+F*/"))
    # print(prefixToPostfix("/-AB*+DEF"))
    print(1<<3)