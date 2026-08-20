
""" 01-08-2026:  Magic Square Solver
Given a 3x3 grid with one missing number (represented as 0), return the missing number that completes the magic square, or "impossible" if no valid number exists.
A magic square is a grid where every row, column, and diagonal adds up to the same number. """

def transp(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def solve_magic_square(grid):
    m1=list(set([sum(grid[i]) for i in range(len(grid))]))
    m2=list(set([sum(transp(grid)[i]) for i in range(len(grid))]))
    if len(m1)>2 or len(m2)>2:
        return "impossible"
    s=max(m1)
    r=sum([el for el in grid if 0 in el][0])
    return s-r
  
""" 02-08-2026: Food Chain
Given an array of [predator, prey] pairs, return the food chain from the apex predator down to the bottom.
• The apex predator is the animal that is never prey to another animal.
• Return the chain as an array of strings. """

""" 03-08-2026: Emoji Translator
Given a string of emojis, return the phrase using the following table:

Emoji
Word

👶
"baby"

🐱
"cat"

🐕
"dog"

🐟
"fish"

🥵
"hot"

🧊
"ice"

🪨
"rock"

🦈
"shark"

🍲
"soup"

⭐
"star"


Return the words separated by spaces. """

def get_emoji_phrase(s):
    emojis={"👶":"baby","🐱":"cat","🐕":"dog","🐟":"fish","🥵":"hot","🧊":"ice","🪨":"rock","🦈":"shark","🍲":"soup","⭐":"star"}
    return " ".join([emojis[el] for el in list(s)])

""" 04-08-2026: Golf Handicap Calculator
Given an array of golf scores and a corresponding array of course par values, return the golfer's handicap index using the following method:
• Calculate the differential for each round by subtracting the par from the score, then return the average of all differentials rounded to one decimal place. """

def calculate_handicap(scores, pars):
    return round(sum([scores[i]-pars[i] for i in range(len(scores))])/len(scores)+0.01,1)
    
""" 05-08-2016: Spoken Duration
Given a number of seconds, return the duration in spoken English.
• Break the duration into hours, minutes, and seconds.
• Skip any zero values.
• Use singular or plural as appropriate ("1 hour", "2 hours").
• If present, join the last two units with "and", and the second and third to last units with a comma ("1 hour, 2 minutes and 3 seconds")."""

import math
def get_spoken_duration(seconds):
    hrs=math.floor(seconds/3600)
    mins=math.floor((seconds-3600*hrs)/60)
    secs=seconds-3600*hrs-60*mins
    vals=[hrs,mins,secs]
    units=["hour","minute","second"]
    ends=["" if vals[i]==1 else "s" for i in range(len(vals))]
    pre=[]
    for i in range(3):
        if vals[i]!=0:
            pre.append(str(vals[i])+" "+units[i]+ends[i])
    if len(pre)==1:
        return pre[0]
    elif len(pre)==2:
        return pre[0]+" and "+pre[1]
    else:
        return pre[0]+", "+pre[1]+" and "+pre[2]

""" 06-08-2026: Spoken Time
Given the angles for the hour and minute hands of an analog clock in degrees (clockwise from 12), return the time in spoken English.
Convert the minute hand angle to minutes (360° = 60 minutes), then use the following rules:

Minutes
Spoken

0
"Y o'clock"

15
"quarter past Y"

1–29 (excluding 15)
"X minutes past Y"

30
"half past Y"

45
"quarter to Z"

31–59 (excluding 45)
"X minutes to Z" (where X is 60 - minutes)


Where Y is the current hour and Z is the next hour, both derived from the hour hand angle (360° = 12 hours).
Note: Hand angles may not land exactly on a number, consider rounding them somehow. """

import math 
def get_spoken_time(hour_angle, minute_angle):
    lst=[math.floor(12*hour_angle/360),math.floor(60*minute_angle/360)]
    if lst[1]==0:
        return str(lst[0])+" o'clock"
    elif lst[1]==15:
        return "quarter past "+str(lst[0])
    elif lst[1]==30:
        return "half past "+str(lst[0])
    elif lst[1]==45:
        return "quarter to "+str(lst[0]+1)
    elif lst[1]<30:
        return str(lst[1])+" minutes past "+str(lst[0])
    elif lst[1]>30:
        return str(60-lst[1])+" minutes to "+str(lst[0]+1)

""" 07-08-2026: Nonogram Validator
Given an array of clue numbers and an array of cells, determine whether the cells satisfy the nonogram clue.
• The clue is an array of numbers representing the lengths of consecutive filled cells, in order. For example, a clue of [3, 2] means there should be 3 consecutive filled cells followed by 2 consecutive filled cells, separated by at least one empty cell.
• The row is an array of 1s (filled) and 0s (empty). """

def is_valid_nonogram(clue, cells):
    lst=[]
    sn=0
    for i in range(len(cells)):
        if cells[i]==1:
            sn+=1
            if i<len(cells)-1 and cells[i+1]==0 or i==len(cells)-1:
                lst.append(sn)
        if cells[i]==0:
            sn=0
    return clue==lst

""" 08-08-2026: Bucket Fill 2
Given a 2D grid of single-letter color strings and a target color, return the minimum number of flood fill "clicks" needed to make the entire grid the target color.
• Each click changes the clicked cell's color and the entire region of connected cells of the same color with the target color.
• Cells are connected horizontally and vertically (not diagonally). """

def bucket_fill(grid, target_color):
    _grid=grid.copy()
    def change_region(x,y,color):
        if x<0 or x>=len(_grid) or y<0 or y>=len(_grid[x]):
            return
        if _grid[x][y]==color:
            _grid[x][y]=target_color
            change_region(x-1,y,color)
            change_region(x+1,y,color)
            change_region(x,y-1,color)
            change_region(x,y+1,color)
    clicks=0
    for i in range(len(_grid)):
        for j in range(len(_grid[i])):
            cell_color=_grid[i][j]
            if cell_color==target_color:
                continue
            clicks+=1
            change_region(i,j,cell_color)
    return clicks
    
""" 09-08-2026: Between Two Buckets
Given two buckets of paint, each with an RGB color and a fullness level, return the mixed RGB color as an array of three integers.
• Each bucket is an object (JavaScript) or dictionary (Python) with a color property (an array of three integers [r, g, b]) and a fullness property (0–100).
• The mixed color is a weighted average of each channel in the two colors based on fullness level, with each channel rounded to the nearest integer. """

def mix_paint(bucket1, bucket2):
    b1=bucket1["color"]
    b2=bucket2["color"]
    m1=[]
    m2=[]
    for i in range(3):
        m1.append(bucket1["fullness"]*b1[i]/100)
        m2.append(bucket2["fullness"]*b2[i]/100)
    rel=100/(bucket1["fullness"]+bucket2["fullness"])
    return [round(rel*(m1[0]+m2[0]),0),round(rel*(m1[1]+m2[1]),0),round(rel*(m1[2]+m2[2]),0)]

""" 10-08-2026: The Last Challenge: Bucket Fill 3
Today marks a year of daily coding challenges. This is the last new one for now. Good luck!
Given a 2D grid of single-letter color strings and a target color, return the minimum number of flood fill "clicks" needed to make the entire grid that color.
• Each click changes the clicked cell's color and the entire region of connected cells of the same color (4-directional).
• Clicks can use any color as an intermediate step, not just the target color. """
""" 11-08-2026: Vowel Balance
Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.
• The string can contain any characters.
• The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
• If there's an odd number of characters in the string, ignore the center character. """

import re
def is_balanced(s):
    if len(s)%2==1:
        p1=s[0:round(len(s)/2-1)]
    else:
        p1=s[0:round(len(s)/2)]
    p2=s[round(len(s)/2):]
    r1=re.findall("[aeiouAEIOU]",p1)
    r2=re.findall("[aeiouAEIOU]",p2)
    return len(r1)==len(r2)

""" 12-08-2026: Base Check
Given a string representing a number, and an integer base from 2 to 36, determine whether the number is valid in that base.
• The string may contain integers, and uppercase or lowercase characters.
• The check should be case-insensitive.
• The base can be any number 2-36.
• A number is valid if every character is a valid digit in the given base.
• Example of valid digits for bases:
◦ Base 2: 0-1
◦ Base 8: 0-7
◦ Base 10: 0-9
◦ Base 16: 0-9 and A-F
◦ Base 36: 0-9 and A-Z """

import re
def is_valid_number(n, base):
    r1=re.findall("[0-9A-Za-z]",n)
    r2=re.findall("[0-9A-Fa-f]",n)
    r3=re.findall("[0-9]",n)
    r4=re.findall("[0-7]",n)
    r5=re.findall("[0-1]",n)
    if base>16:
        return len(r1)==len(n)
    if base>10:
        return len(r2)==len(n)
    if base>8:
        return len(r3)==len(n)
    if base>2:
        return len(r4)==len(n)
    return len(r5)==len(n)

""" 13-08-2026: Fibonacci Sequence
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. When starting with 0 and 1, the first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

Given an array containing the first two numbers of a Fibonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.

Your function should handle sequences of any length greater than or equal to zero.
If the length is zero, return an empty array.
Note that the starting numbers are part of the sequence. """

def fibonacci_sequence(start_seq, length):
    if length==0:
        return []
    if length==1:
        return [start_seq[0]]
    res=[start_seq[0],start_seq[1]]
    for i in range(2,length):
        res.append(res[i-2]+res[i-1])
    return res
    
""" 14-08-2026: S P A C E J A M
Given a string, remove all spaces from the string, insert two spaces between every character, convert all alphabetical letters to uppercase, and return the result.
• Non-alphabetical characters should remain unchanged (except for spaces). """

def space_jam(s):
    return "  ".join(s.replace(" ","").upper())

""" 15-08-2026: Jbelmud Text
Given a string, return a jumbled version of that string where each word is transformed using the following constraints:
• The first and last letters of the words remain in place
• All letters between the first and last letter are sorted alphabetically.
• The input strings will contain no punctuation, and will be entirely lowercase. """

def jbelmu(text):
    return " ".join([el[0]+"".join(sorted(list(el[1:-1])))+el[-1] if len(el)>1 else el[0] for el in text.split(" ")])

""" 16-08-2026: Anagram Checker
Given two strings, determine if they are anagrams of each other (contain the same characters in any order).
• Ignore casing and white space. """

def are_anagrams(str1, str2):
    return sorted(list(str1.replace(" ","").lower()))==sorted(list(str2.replace(" ","").lower()))

""" 17-08-2026: Targeted Sum
Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value. Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.
• The returned array should have the indices in ascending order. """

def find_target(arr, target):
    c=[[arr.index(i),arr.index(j)] for i in arr for j in arr if i<j and i+j==target]
    if len(c)==0:
        return "Target not found"
    return c[0] 

""" 18-08-2026: Factorializer
Given an integer from zero to 20, return the factorial of that number. The factorial of a number is the product of all the numbers between 1 and the given number.
• The factorial of zero is 1. """

""" 19-08-2026: Sum of Squares
Given a positive integer up to 1,000, return the sum of all the integers squared from 1 up to the number. """

""" 20-08-2026: 3 Strikes
Given an integer between 1 and 10,000, return a count of how many numbers from 1 up to that integer whose square contains at least one digit 3. """

