""" 11-08-2025: Vowel Balance
Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.

The string can contain any characters.
The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
If there's an odd number of characters in the string, ignore the center character. 
"""

def is_balanced(s):
    vowels=list("aeiouAEIOU")
    l=len(s)
    c1=0
    c2=0
    if l%2==1:
        h1=s[:int(l/2-0.5)]
        h2=s[int(l/2+0.5):]
    else:
        h1=s[:int(l/2)]
        h2=s[int(l/2):]
    for i in range(len(h1)):
        if h1[i] in vowels:
            c1+=1
    for i in range(len(h2)):
        if h2[i] in vowels:
            c2+=1
    return c1==c2

""" 12-08-2025: Base Check
Given a string representing a number, and an integer base from 2 to 36, determine whether the number is valid in that base.

The string may contain integers, and uppercase or lowercase characters.
The check should be case-insensitive.
The base can be any number 2-36.
A number is valid if every character is a valid digit in the given base.
Example of valid digits for bases:
Base 2: 0-1
Base 8: 0-7
Base 10: 0-9
Base 16: 0-9 and A-F
Base 36: 0-9 and A-Z """

def is_valid_number(n, base):
    last=sorted(list(n))[-1]
    digits=list("0123456789")
    chars=list("abcdefABCDEF")
    if base<16:
        if last in digits:
             if int(last)<base:
                return True
             else:
                return False
        if last not in digits:
            return False
    elif base==16:
        if last in digits or last in chars:
            return True
        else:
            return False
    else:
        return True

""" 13-08-2025: Fibonacci Sequence
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. When starting with 0 and 1, the first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

Given an array containing the first two numbers of a Fibonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.

Your function should handle sequences of any length greater than or equal to zero.
If the length is zero, return an empty array.
Note that the starting numbers are part of the sequence."""

def fibo(n,first,second): 
    if n==0:
        return first
    if n==1:
        return second
    if n>1:
        return fibo(n-1,first,second)+fibo(n-2,first,second)

def fibArr(n,first,second):
    targ=[]
    for i in range(n):
        targ.append(fibo(i,first,second))
    return targ    
    
def fibonacci_sequence(start_sequence, length):
    if length==0:
        return []
    elif length==1:
        return [start_sequence[0]]
    elif length==2:
        return start_sequence
    else:
        return fibArr(length,start_sequence[0],start_sequence[1])

""" 14-08-2025: S P A C E J A M
Given a string, remove all spaces from the string, insert two spaces between every character, convert all alphabetical letters to uppercase, and return the result.

Non-alphabetical characters should remain unchanged (except for spaces). """

def space_jam(s):
    lst=list(s.strip().upper().replace(" ",""))
    j="  ".join(lst)
    return j

""" 15-08-2025: Jbelmud Text
Given a string, return a jumbled version of that string where each word is transformed using the following constraints:

The first and last letters of the words remain in place
All letters between the first and last letter are sorted alphabetically.
The input strings will contain no punctuation, and will be entirely lowercase. """

def jbelmu(text):
    s=text.split(" ")
    res=[]
    for w in s:
        if len(w)>3:
            v=w[0]+"".join(sorted(list(w[1:-1])))+w[-1]        
            res.append(v)
        else:
            v=w
            res.append(v) 
    return " ".join(res)

""" 16-08-2025: Anagram Checker
Given two strings, determine if they are anagrams of each other (contain the same characters in any order).
Ignore casing and white space. """

def are_anagrams(str1, str2):
    lst1=list(str1.lower().replace(" ",""))
    lst2=list(str2.lower().replace(" ",""))
    if len(lst1)!=len(lst2):
        return False
    else:
        for c in lst1:
            if c not in lst2:
                return False
    return True

""" 17-08-2025: Targeted Sum
Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value. 
Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.
The returned array should have the indices in ascending order. """

def find_target(arr, target):
    res=[]
    for i in range(len(arr)-1):
        if arr[i]+arr[i+1]==target:
            res.append(i)
            res.append(i+1)
            return res
    return "Target not found"

""" 18-08-2025: Factorializer
Given an integer from zero to 20, return the factorial of that number. The factorial of a number is the product of all the numbers between 1 and the given number.

The factorial of zero is 1. """

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
""" 19-08-2025: Sum of Squares
Given a positive integer up to 1,000, return the sum of all the integers squared from 1 up to the number. """

from functools import reduce
def sum_of_squares(n):
    rng=list(range(1,n+1))
    sqr=[]
    for r in rng:
        sqr.append(r*r)
    res = reduce(lambda x, y: x + y, sqr)
    return res

""" 20-08-2025: 3 Strikes
Given an integer between 1 and 10,000, return a count of how many numbers from 1 up to that integer whose square contains at least one digit 3.
"""

def squares_with_three(n):
    sq=[str(x*x) for x in range(1,n+1)]
    res=[]
    for i in range(len(sq)):
        if sq[i].find("3")>-1:
            res.append(sq[i])
    return len(res)

""" 21-08-2025: Mile Pace
Given a number of miles ran, and a time in "MM:SS" (minutes:seconds) it took to run those miles, return a string for the average time it took to run each mile in the format "MM:SS".

Add leading zeros when needed. """

import math
def mile_pace(miles, dur):
    if len(dur)<=5:
        _min=dur[0:2]
        _sec=dur[3:5]
    else:
        _min=dur[0:3]
        _sec=dur[4:6]
    dur_m=(60*int(_min)+int(_sec))/miles
    min_m=math.floor(dur_m/60)
    sec_m=dur_m-60*min_m
    if min_m<10:
        min_m="0"+str(min_m)
    else:
        min_m=str(min_m)
    if sec_m<10:
        sec_m=("0"+str(sec_m))[0:2]
    else:
        sec_m=str(sec_m)[0:2]
    return min_m+":"+sec_m

""" 22-08-2025: Message Decoder
Given a secret message string, and an integer representing the number of letters that were used to shift the message to encode it, return the decoded string.

A positive number means the message was shifted forward in the alphabet.
A negative number means the message was shifted backward in the alphabet.
Case matters, decoded characters should retain the case of their encoded counterparts.
Non-alphabetical characters should not get decoded.
"""

def decode(message, shift):
    msg=message.lower()
    a="abcdefghijklmnopqrstuvwxyz"
    if shift>0:
       sh=a[26-shift:26]+a[0:26-shift]
    if shift<0:
       sh=a[-shift:26]+a[0:-shift]
    d=dict(zip(a,sh))
    pre=""
    for i in range(len(msg)):
       if msg[i] in d.keys():
          pre+=d[msg[i]]
       else:
          pre+=msg[i]
    res=""
    for i in range(len(msg)):
       if message[i].isupper():
          res+=pre[i].upper()
       else:
          res+=pre[i]
    return res

""" 23-08-2025: Unnatural Prime
Given an integer, determine if that number is a prime number or a negative prime number.

A prime number is a positive integer greater than 1 that is only divisible by 1 and itself.
A negative prime number is the negative version of a positive prime number.
1 and 0 are not considered prime numbers.
"""

import math
def is_unnatural_prime(n):
    if n==0 or n==-1 or n==1:
        return False
    if n<0:
        s=-n
    else:
        s=n
    for i in range(2,math.ceil(math.sqrt(s))+1):
        if s%i==0:
           return False  
    return True

""" 24-08-2025: Character Battle
Given two strings representing your army and an opposing army, each character from your army battles the character at the same position from the opposing army using the following rules:

Characters a-z have a strength of 1-26, respectively.
Characters A-Z have a strength of 27-52, respectively.
Digits 0-9 have a strength of their face value.
All other characters have a value of zero.
Each character can only fight one battle.
For each battle, the stronger character wins. The army with more victories, wins the war. Return the following values:

"Opponent retreated" if your army has more characters than the opposing army.
"We retreated" if the opposing army has more characters than yours.
"We won" if your army won more battles.
"We lost" if the opposing army won more battles.
"It was a tie" if both armies won the same number of battles.
"""

def battle(m_arm, o_arm):
    k="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    v=list(range(1,53))
    d=dict(zip(k,v))
    for i in range(10):
        d[str(i)]=i
    x=[]
    y=[]
    s1=0
    s2=0
    if len(m_arm)>len(o_arm):
        return "Opponent retreated"
    elif len(m_arm)<len(o_arm):
        return "We retreated"
    else:
        for i in range(len(m_arm)):
            if m_arm[i] in d.keys():
                x.append(d[m_arm[i]])
            else:
                x.append(0)
            if o_arm[i] in d.keys():
                y.append(d[o_arm[i]])
            else:
                y.append(0)
        for i in range(len(x)):
            if x[i]>y[i]:
                s1+=1
            if x[i]<y[i]:
                s2+=1
        if s1>s2:
            return "We won"
        elif s1<s2:
            return "We lost"
        else:
            return "It was a tie"

""" 25.08.2025: camelCase
Given a string, return its camel case version using the following rules:

Words in the string argument are separated by one or more characters from the following set: space ( ), dash (-), or underscore (_). Treat any sequence of these as a word break.
The first word should be all lowercase.
Each subsequent word should start with an uppercase letter, with the rest of it lowercase.
All spaces and separators should be removed.
"""

def prop_case(s):
    return s[0].upper()+s[1:].lower()

def to_camel_case(s):
    stri=s.lower().replace("-"," ").replace("_"," ")
    sp=[]
    sp0=stri.split(" ")
    for i in range(len(sp0)):
        if sp0[i]!="":
            sp.append(sp0[i])
    res=sp[0]
    for i in range(1,len(sp)):
        res+=prop_case(sp[i])
    return res
function propCase(stri){
  let prop = stri.slice(0,1).toUpperCase()+stri.slice(1).toLowerCase();
  return prop;
}

""" 26-08-2025: Reverse Parenthesis
Given a string that contains properly nested parentheses, return the decoded version of the string using the following rules:

All characters inside each pair of parentheses should be reversed.
Parentheses should be removed from the final result.
If parentheses are nested, the innermost pair should be reversed first, and then its result should be included in the reversal of the outer pair.
Assume all parentheses are evenly balanced and correctly nested.
"""

def indices(source,find):
    res=[]
    for i in range(len(source)):
        if source[i:i+len(find)]==find:
            res.append(i)
    return res

def hlp(s):
    ind1=indices(s,"(")
    ind2=indices(s,")")
    ind=sorted(ind1+ind2)
    d=[]
    for i in range(len(ind)):
        if ind[i] in ind1 and ind[i+1] in ind2:
            d.append([ind[i],ind[i+1]])
    ob={}
    for i in range(len(d)):
        ob[i]=s[d[i][0]+1:d[i][1]][::-1]
    m=s[0:d[0][0]]+ob[0]
    for i in range(len(d)-1):
        m+=s[(d[i][1]+1):d[i+1][0]]+ob[i+1]
    m+=s[(d[-1][1]+1):]
    return m

def decode(s):
    if "(" in s:
        return decode(hlp(s))
    else:
        return s

""" 27-08-2025: Unorder of Operations
Given an array of integers and an array of string operators, apply the operations to the numbers sequentially from left-to-right. Repeat the operations as needed until all numbers are used. Return the final result.

For example, given [1, 2, 3, 4, 5] and ['+', '*'], return the result of evaluating 1 + 2 * 3 + 4 * 5 from left-to-right ignoring standard order of operations.

Valid operators are +, -, *, /, and %.
"""

def evaluate(nums, ops):
    op=[]
    for i in range(len(nums)):
        for j in range(len(ops)):
            op.append(ops[j])
    op=op[0:(len(nums)-1)] 
    stri=str(nums[0])+op[0]+str(nums[1])
    val=eval(stri) 
    for i in range(1,len(op)):
        ex=str(val)+op[i]+str(nums[i+1])
        val=eval(ex);       
    return val

""" 28-08-2025: Second Best
Given an array of integers representing the price of different laptops, and an integer representing your budget, return:

The second most expensive laptop if it is within your budget, or
The most expensive laptop that is within your budget, or
0 if no laptops are within your budget.
Duplicate prices should be ignored.
"""

def get_laptop_cost(laptops, budget):
    s=sorted(list(set(laptops)))
    sl=s[-2]
    flt=[x for x in s if x<=budget]
    if budget>=sl:
        return sl
    else:
        if len(flt)>0:
            return flt[-1]
        else:
            return 0

""" 29-08-2025: Candlelight
Given an integer representing the number of candles you start with, and an integer representing how many burned candles it takes to create a new one, return the number of candles you will have used after creating and burning as many as you can.

For example, if given 7 candles and it takes 2 burned candles to make a new one:

Burn 7 candles to get 7 leftovers,
Recycle 6 leftovers into 3 new candles (1 leftover remains),
Burn 3 candles to get 3 more leftovers (4 total),
Recycle 4 leftovers into 2 new candles,
Burn 2 candles to get 2 leftovers,
Recycle 2 leftovers into 1 new candle,
Burn 1 candle.
You will have burned 13 total candles in the example.
"""

import math
def burn_candles(candles, leftovers_needed):
    burned=0
    while candles >=leftovers_needed:
        v=math.floor(candles/leftovers_needed)
        burned+=v*leftovers_needed;
        candles=v+(candles%leftovers_needed)
    burned+=candles
    return burned

""" 30-08-2025: Array Duplicates
Given an array of integers, return an array of integers that appear more than once in the initial array, sorted in ascending order. If no values appear more than once, return an empty array.

Only include one instance of each value in the returned array.
"""
def find_duplicates(arr):
    ulist=[]
    duplist=[]
    for el in arr:
        if el not in ulist:
            ulist.append(el)
        else:
            duplist.append(el)
    s=sorted(list(set(duplist)))
    return s

""" 31-08-2025: Hex Generator
Given a named CSS color string, generate a random hexadecimal (hex) color code that is dominant in the given color.

The function should handle "red", "green", or "blue" as an input argument.
If the input is not one of those, the function should return "Invalid color".
The function should return a random six-character hex color code where the input color value is greater than any of the others.
Example of valid outputs for a given input:
Input	Output
"red"	"FF0000"
"green"	"00FF00"
"blue"	"0000FF"
"""

import random
import math
def hlp(stri):
    if len(stri)==2:
        return stri
    else:
        return "0"+stri

def genRand():
    c1=math.floor(random.random()*255)
    c2=math.floor(random.random()*255)
    maxi=max(c1,c2)
    c3=math.floor(random.random()*(255-maxi))+maxi+1
    arr=[c1,c2,c3]
    print(arr)
    return arr
genRand()

def generate_hex(color):
    if color!="red" and color!="green" and color!="blue":
        return "Invalid color"
    if color=="red":
        rCol=genRand()
        hCol=hlp(hex(rCol[2])[2:])+hlp(hex(rCol[0])[2:])+hlp(hex(rCol[1])[2:])
    if color=="green":
        rCol=genRand()
        hCol=hlp(hex(rCol[0])[2:])+hlp(hex(rCol[2])[2:])+hlp(hex(rCol[1])[2:])
    if color=="blue":
        rCol=genRand()
        hCol=hlp(hex(rCol[0])[2:])+hlp(hex(rCol[1])[2:])+hlp(hex(rCol[2])[2:])
    return hCol
