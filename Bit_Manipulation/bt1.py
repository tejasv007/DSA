'''
Docstring for Bit_Manipulation.bt1
Fundamental Concepts

Bit: The smallest unit of data in computing, representing 0 or 1
Byte: Collection of 8 bits
Binary representation: Numbers stored as sequences of bits (e.g., 5 = 101₂)
Positions are 0-indexed: Rightmost bit is position 0, increasing leftward
Signed vs unsigned: Signed integers use leftmost bit for sign (0=positive, 1=negative)


Basic Bitwise Operators

AND (&): Returns 1 only if both bits are 1 (e.g., 5 & 3 = 1)
OR (|): Returns 1 if at least one bit is 1 (e.g., 5 | 3 = 7)
XOR (^): Returns 1 if bits are different (e.g., 5 ^ 3 = 6)
NOT (~): Flips all bits (e.g., ~5 = -6 in two's complement)
Left shift (<<): Shifts bits left, fills with 0s (e.g., 5 << 1 = 10)
Right shift (>>): Shifts bits right, behavior depends on sign

Common Bit Manipulation Tricks

Check if number is even/odd: n & 1 (0=even, 1=odd)
Multiply by 2ⁿ: n << k (left shift by k)
Divide by 2ⁿ: n >> k (right shift by k)
Check if power of 2: n & (n-1) == 0 and n != 0
Toggle kth bit: n ^ (1 << k)
Set kth bit: n | (1 << k)
Clear kth bit: n & ~(1 << k)
Check if kth bit is set: (n & (1 << k)) != 0
Get rightmost set bit: n & (-n)
Remove rightmost set bit: n & (n-1)
Swap two numbers: Use a ^= b; b ^= a; a ^= b (no temp variable)

XOR Properties (Very Important)

Commutative: a ^ b = b ^ a
Associative: (a ^ b) ^ c = a ^ (b ^ c)
Identity: a ^ 0 = a
Self-inverse: a ^ a = 0
Finding single element: XOR all numbers; duplicates cancel out
Swap values: a = a ^ b; b = a ^ b; a = a ^ b

Counting Bits

Count set bits (Brian Kernighan's algorithm): while(n) { count++; n &= (n-1); }
Count with built-ins: __builtin_popcount(n) in C++, Integer.bitCount(n) in Java
Check total bits needed: log₂(n) + 1 or iterate until n becomes 0

Bit Masking Techniques

Create mask with k bits set: (1 << k) - 1
Extract lower k bits: n & ((1 << k) - 1)
Clear lower k bits: n & (~((1 << k) - 1))
Check if subset: (mask & subset) == subset
Iterate all subsets of mask: Use for(int s = mask; s > 0; s = (s-1) & mask)

Common Problem Patterns

Finding missing number: XOR all array elements with 1 to n
Finding single non-duplicate: XOR all elements
Finding two non-duplicates: XOR all, then split by any set bit
Subset generation: Use numbers 0 to 2ⁿ-1 as bitmasks
Gray code: Use i ^ (i >> 1) formula
Reverse bits: Swap and shift systematically

Advanced Techniques

Fast exponentiation: Use binary representation of exponent
DP with bitmasks: Store states as integers (e.g., Traveling Salesman)
Fenwick Tree (BIT): Uses bit manipulation for range queries
Finding position of rightmost set bit: log₂(n & -n) or count trailing zeros
Check if two numbers have opposite signs: (x ^ y) < 0

Performance Benefits

Speed: Bit operations are faster than arithmetic operations
Space: Can store multiple boolean flags in single integer
Optimization: Compilers often optimize to bit operations automatically
Memory efficiency: Bitsets use 1 bit per element vs 8+ bits for boolean

Common Pitfalls

Operator precedence: Use parentheses; & has lower precedence than ==
Signed right shift: May fill with sign bit instead of 0
Overflow: Left shifting can cause overflow if not careful
Negative numbers: Two's complement representation can be tricky
Language differences: Behavior varies between languages for signed operations

Practical Applications

Permissions systems: Each bit represents a permission flag
State compression: Represent board states in games
Network protocols: Efficient flag and option encoding
Graphics: Color manipulation (RGB channels)
Cryptography: XOR ciphers and bit-level operations
Data compression: Huffman coding and bit-level packing

'''


# ------ have a doubt--> do reversing a string not affect the tc💀💀💀
# ----Binary to Decimal
# 1101
# 2^3*1+2^2*1+2^1*0+2^0*1
# TC-O(len(s))
def binary2decimal(s:str):
    new=s[::-1]
    c=0
    ans=0
    for i in new:
        if i=="1":
            ans+=(2**c)
        c+=1
    return ans



#----Decimal to Binary
# 13-->divide by 2, note the remainders, put all from reverse manner
# TC-O(log(x)) sc-O(log(x))
def decimal2binary(x:int):
    ans=""
    while(x>1):
        a=x%2
        ans=ans+str(a)
        x=x//2
    ans=ans+str(x)
    return ans[::-1]

if __name__=="__main__":
    # print(decimal2binary(13))
    print(~(-6))
    # print(binary2decimal("1101"))