# 1️⃣ buy stock and sell stock ---Checked ✅ leetcode
# buy stock and sell it and make highest profit
# only buy one time 
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 
# s=[7,1,5,3,6,4]
# output=5
# approach--- dynamic programming as we are taking past one also
# here we have to find the max diff of every no to the mini one... so we focus on mini one and also find the max diff
# tc o(n)
# sc o(1)
def buySellOneTime(s):
    mini=s[0]
    m=0
    cost=0
    for i in range(1,len(s)):
        cost=s[i]-mini
        m=max(m,cost)
        mini=min(mini,s[i])
    return m

# 2️⃣Best Time to Buy and Sell Stock II✅ checked--leetcode
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

# Find and return the maximum profit you can achieve.
# buy stock and sell it and make highest profit
# can buy any no of time 
# s=[7,1,5,3,6,4]
# output 4+3=7
# tc O(2^n)
# sc O(n)

def buySellStockIIHelper(i,s,buy,n):
    if i==n:
        return 0
    profit=0
    if buy==0:
        profit=max(-s[i]+buySellStockIIHelper(i+1,s,1,n),0+buySellStockIIHelper
                   (i+1,s,0,n))
    else:
        profit=max(s[i]+buySellStockIIHelper(i+1,s,0,n),0+buySellStockIIHelper(i+1,s,1,n))
    return profit

def buySellStockII(s):
    return (buySellStockIIHelper(0,s,0,len(s)))


# memoization 
# tc O(n*2)
# sc O(n*2)+O(n)

def buySellStockIIMHelper(i,s,buy,n,newarr):
    if i==n:
        return 0
    profit=0
    if newarr[i][buy]!=-1:
        return newarr[i][buy]
    if buy==0:
        profit=max(-s[i]+buySellStockIIMHelper(i+1,s,1,n,newarr),0+buySellStockIIMHelper
                   (i+1,s,0,n,newarr))
    else:
        profit=max(s[i]+buySellStockIIMHelper(i+1,s,0,n,newarr),0+buySellStockIIMHelper(i+1,s,1,n,newarr))
    newarr[i][buy]=profit
    return profit

def buySellStockIIM(s):
    new=[[-1 for i in range(2)] for j in range(len(s)+1)]
    return (buySellStockIIMHelper(0,s,0,len(s),new))

# 3️⃣Best Time to Buy and Sell Stock III✅ checked--leetcode
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete at most two transactions.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

#s= [2,1,4,5,2,9,7]
# output 11
# s = [3,3,5,0,0,3,1,4]
# Output: 6
# recursion
# tc O(2 ^n)
# sc O(n)(auxiallary stack)

def buySellStockIIIHelper(i,s,buy,n,day):
    if i==n:
        return 0
    if day==0:
        return 0
    profit=0
    
    if buy==0:
        profit=max(-s[i]+buySellStockIIIHelper(i+1,s,1,n,day),0+buySellStockIIIHelper
                   (i+1,s,0,n,day))
    else:
        profit=max(s[i]+buySellStockIIIHelper(i+1,s,0,n,day-1),0+buySellStockIIIHelper(i+1,s,1,n,day))
    
    return profit

def buySellStockIII(s):
    return (buySellStockIIIHelper(0,s,0,len(s),2))

# memoization
# tc O(n*2*3)
# sc O(n*2*3)+O(n)

def buySellStockIIIMHelper(i,s,buy,n,newarr,day):
    if i==n:
        return 0
    if day==0:
        return 0
    profit=0
    if newarr[i][buy][day]!=-1:
        return newarr[i][buy][day]
    if buy==0:
        profit=max(-s[i]+buySellStockIIIMHelper(i+1,s,1,n,newarr,day),0+buySellStockIIIMHelper
                   (i+1,s,0,n,newarr,day))
    else:
        profit=max(s[i]+buySellStockIIIMHelper(i+1,s,0,n,newarr,day-1),0+buySellStockIIIMHelper(i+1,s,1,n,newarr,day))
    newarr[i][buy][day]=profit
    return profit

def buySellStockIIIM(s):
    new=[[[-1 for i in range(3)] for i in range(2)] for j in range(len(s)+1)]
    return (buySellStockIIIMHelper(0,s,0,len(s),new,2))
    # return new


# tabulation---left


# 4️⃣Best Time to Buy and Sell Stock IV✅ checked--leetcode
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# k = 2, prices = [2,4,1]
# Output: 2

# Recursion
# # tc O(2 ^n)
# sc O(n)(auxiallary stack)

def buySellStockIVHelper(i,s,buy,n,day):
    if i==n:
        return 0
    if day==0:
        return 0
    profit=0
    
    if buy==0:
        profit=max(-s[i]+buySellStockIVHelper(i+1,s,1,n,day),0+buySellStockIVHelper
                   (i+1,s,0,n,day))
    else:
        profit=max(s[i]+buySellStockIVHelper(i+1,s,0,n,day-1),0+buySellStockIVHelper(i+1,s,1,n,day))
    
    return profit

def buySellStockIV(s):
    return (buySellStockIVHelper(0,s,0,len(s),2))

# memoization
# tc O(n*2*3)
# sc O(n*2*3)+O(n)
def buySellStockIVMHelper(i,s,buy,n,newarr,day):
    if i==n:
        return 0
    if day==0:
        return 0
    profit=0
    if newarr[i][buy][day]!=-1:
        return newarr[i][buy][day]
    if buy==0:
        profit=max(-s[i]+buySellStockIVMHelper(i+1,s,1,n,newarr,day),0+buySellStockIVMHelper
                   (i+1,s,0,n,newarr,day))
    else:
        profit=max(s[i]+buySellStockIVMHelper(i+1,s,0,n,newarr,day-1),0+buySellStockIVMHelper(i+1,s,1,n,newarr,day))
    newarr[i][buy][day]=profit
    return profit

def buySellStockIVM(s,k):
    new=[[[-1 for i in range(k+1)] for i in range(2)] for j in range(len(s)+1)]
    return (buySellStockIVMHelper(0,s,0,len(s),new,k))

# tabulation----

# 5️⃣ Best Time to Buy and Sell Stock V
# You are given an integer array prices where prices[i] is the price of a stock in dollars on the ith day, and an integer k.

# You are allowed to make at most k transactions, where each transaction can be either of the following:

# Normal transaction: Buy on day i, then sell on a later day j where i < j. You profit prices[j] - prices[i].

# Short selling transaction: Sell on day i, then buy back on a later day j where i < j. You profit prices[i] - prices[j].

# Note that you must complete each transaction before starting another. Additionally, you can't buy or sell on the same day you are selling or buying back as part of a previous transaction.

# Return the maximum total profit you can earn by making at most k transactions.

# -------🧧🧧🧧🧧🧧🧧🧧🧧⚡⚡⚡ left

def buySellStockIIHelper(i,s,tdone,n,ttype,k):
    if i==n:
        return 0
    if k==0:
        return 0
    profit=0
    if tdone==1:
        if ttype==0:        
            profit=max(-s[i]+buySellStockIIHelper(i+1,s,0,n,0,k),buySellStockIIHelper(i+1,s,1,n,0,k),s[i]+buySellStockIIHelper(i+1,s,1,n,0,k),buySellStockIIHelper(i+1,s,1,n,1,k))
        else:
            profit=max(s[i]+buySellStockIIHelper(i+1,s,0,n,0,k),buySellStockIIHelper(i+1,s,1,n,0,k),-s[i]+buySellStockIIHelper(i+1,s,1,n,0,k),buySellStockIIHelper(i+1,s,1,n,1,k))
    else:
        if ttype==0:        
            profit=max(s[i]+buySellStockIIHelper(i+1,s,0,n,0,k-1),buySellStockIIHelper(i+1,s,1,n,0,k),-s[i]+buySellStockIIHelper(i+1,s,1,n,0,k-1),buySellStockIIHelper(i+1,s,1,n,1,k))
        else:
            profit=max(-s[i]+buySellStockIIHelper(i+1,s,0,n,0,k-1),buySellStockIIHelper(i+1,s,1,n,0,k),s[i]+buySellStockIIHelper(i+1,s,1,n,0,k-1),buySellStockIIHelper(i+1,s,1,n,1,k))
    return profit

def buySellStockII(s,k):
    return (buySellStockIIHelper(0,s,1,len(s),0,k))



# 6️⃣  Best Time to Buy and Sell Stock with Cooldown ✅ checked--leetcode
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

# After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# s= [1,2,3,0,2]
# output 3

# recursion
# tc O(2^n)
# sc O(n)

def buySellStockCooldownHelper(i,s,buy,n):
    if i==n:
        return 0
    
    profit=0
    if buy==0:
        profit=max(-s[i]+buySellStockCooldownHelper(i+1,s,1,n),0+buySellStockCooldownHelper
                   (i+1,s,0,n))
    else:
        profit=max(s[i]+buySellStockCooldownHelper(i+1,s,0,n),0+buySellStockCooldownHelper(i+1,s,1,n))
    return profit

def buySellStockCooldown(s):
    return (buySellStockCooldownHelper(0,s,0,len(s)))


# memoization
# tc O(n*2)
# sc O(n*2)+O(n)
def buySellStockCooldownMHelper(i,s,buy,n,newarr):
    if i>=n:
        return 0
    profit=0
    if newarr[i][buy]!=-1:
        return newarr[i][buy]
    if buy==0:
        profit=max(-s[i]+buySellStockCooldownMHelper(i+1,s,1,n,newarr),0+buySellStockCooldownMHelper
                   (i+1,s,0,n,newarr))
    else:
        profit=max(s[i]+buySellStockCooldownMHelper(i+2,s,0,n,newarr),0+buySellStockCooldownMHelper(i+1,s,1,n,newarr))
    newarr[i][buy]=profit
    return profit

def buySellStockCoolDownM(s):
    new=[[-1 for i in range(2)] for j in range(len(s)+1)]
    return (buySellStockCooldownMHelper(0,s,0,len(s),new))

# tabulation----

# 7️⃣   Best Time to Buy and Sell Stock with Transaction Fee ✅ checked--leetcode
# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

# Note:

# You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# The transaction fee is only charged once for each stock purchase and sale.
# s = [1,3,2,8,4,9], fee = 2
# Output: 8
# recursion
# tc O(2^n)
# sc O(n*2)+O(n)
def buySellStockFeeHelper(i,s,buy,n):
    if i==n:
        return 0
    profit=0
    if buy==0:
        profit=max(-s[i]+buySellStockFeeHelper(i+1,s,1,n),0+buySellStockFeeHelper
                   (i+1,s,0,n))
    else:
        profit=max(s[i]+buySellStockFeeHelper(i+1,s,0,n),0+buySellStockFeeHelper(i+1,s,1,n))
    return profit

def buySellStockFee(s):
    return (buySellStockFeeHelper(0,s,0,len(s)))

# memoization
# tc O(n*2)
# sc O(n*2)+O(n)(as)(auxillary space)
def buySellStockFeeMHelper(i,s,buy,n,newarr,fee):
    if i==n:
        return 0
    profit=0
    if newarr[i][buy]!=-1:
        return newarr[i][buy]
    if buy==0:
        profit=max(-s[i]+buySellStockFeeMHelper(i+1,s,1,n,newarr,fee),0+buySellStockFeeMHelper
                   (i+1,s,0,n,newarr,fee))
    else:
        profit=max(s[i]+buySellStockFeeMHelper(i+1,s,0,n,newarr,fee)-fee,0+buySellStockFeeMHelper(i+1,s,1,n,newarr,fee))
    newarr[i][buy]=profit
    return profit

def buySellStockFeeM(s,fee):
    new=[[-1 for i in range(2)] for j in range(len(s)+1)]
    return (buySellStockFeeMHelper(0,s,0,len(s),new,fee))


# tabulation----
# ---------------------


if __name__=="__main__":
    # s=[7,1,5,3,6,4]
    s=[3,3,5,0,0,3,1,4]
    s=[2,1,4,5,2,9,7]
    # print(buySellOneTime(s))
    s=  [1]
    # print(buySellStockCoolDownM(s))
    s=[1,7,9,8,2]
    k = 2
    # print(buySellStockIVM(s,k))
    s = [1,7,9,8,2]; k = 2
    s = [12,16,19,19,8,1,19,13,9]; k = 3
    print(buySellStockII(s,k))