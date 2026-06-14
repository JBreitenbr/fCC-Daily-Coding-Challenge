""" 01-11-2025: Signature Validation
Given a message string, a secret key string, and a signature number, determine if the signature is valid using this encoding method:

Letters in the message and secret key have these values:
a to z have values 1 to 26 respectively.
A to Z have values 27 to 52 respectively.
All other characters have no value.
Compute the signature by taking the sum of the message plus the sum of the secret key.
For example, given the message "foo" and the secret key "bar", the signature would be 57:

f (6) + o (15) + o (15) = 36
b (2) + a (1) + r (18) = 21
36 + 21 = 57
Check if the computed signature matches the provided signature.
"""

def verify(message, key, signature):
    a0="abcdefghijklmnopqrstuvwxyz"
    a=list(a0+a0.upper())
    n=list(range(1,53))
    d=dict(zip(a,n))
    sn=0
    for ch in message:
        if ch.isupper() or ch.islower():
           sn+=d[ch]
    for ch in key:
        if ch.isupper() or ch.islower():
           sn+=d[ch]
    return sn==signature

""" 02-11-2025: Infected
On November 2nd, 1988, the first major internet worm was released, infecting about 10% of computers connected to the internet after only a day.

In this challenge, you are given a number of days that have passed since an internet worm was released, and you need to determine how many computers are infected using the following rules:

On day 0, the first computer is infected.
Each subsequent day, the number of infected computers doubles.
Every 3rd day, a patch is applied after the virus spreads and reduces the number of infected computers by 20%. Round the number of patched computers up to the nearest whole number.
For example, on:

Day 0: 1 total computer is infected.
Day 1: 2 total computers are infected.
Day 2: 4 total computers are infected.
Day 3: 8 total computers are infected. Then, apply the patch: 8 infected * 20% = 1.6 patched. Round 1.6 up to 2. 8 computers infected - 2 patched = 6 total computers infected after day 3.
Return the number of total infected computers after the given amount of days have passed.
"""

import math
def infected(days):
    p=[1]
    for i in range(1,26):
        p.append(2*p[i-1])
        if i%3==0:
           p[i]-=math.ceil(0.2*p[i])
    return p[days]

""" 03-11-2025: Word Counter
Given a sentence string, return the number of words that are in the sentence.

Words are any sequence of non-space characters and are separated by a single space.
"""

def count_words(s):
    return len(s.split(" "))

""" 04-11-2025: Image Search
On November 4th, 2001, Google launched its image search, allowing people to find images using search terms. In this challenge, you will imitate the image search.

Given an array of image names and a search term, return an array of image names containing the search term.

Ignore the case when matching the search terms.
Return the images in the same order they appear in the input array.
"""

def image_search(images, term):
    res=[]
    for im in images:
        if term.lower() in im.lower():
            res.append(im)
    return res

""" 05-11-2025: Matrix Builder
Given two integers (a number of rows and a number of columns), return a matrix (an array of arrays) filled with zeros (0) of the given size.

For example, given 2 and 3, return:

[
  [0, 0, 0],
  [0, 0, 0]
]
"""

def build_matrix(rows, cols):
    mat=[]
    for i in range(rows):
        mat.append([])
        for j in range(cols):
            mat[i].append(0)
    return mat

""" 06-11-2025: Weekday Finder
Given a string date in the format YYYY-MM-DD, return the day of the week.

Valid return days are:

"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
Be sure to ignore time zones.
"""

from datetime import datetime
def get_weekday(d):
    dt=datetime.strptime(d, "%Y-%m-%d")  
    wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return wd[dt.weekday()]

""" 07-11-2025: Counting Cards
A standard deck of playing cards has 13 unique cards in each suit. Given an integer representing the number of cards to pick from the deck, return the number of unique combinations of cards you can pick.

Order does not matter. Picking card A then card B is the same as picking card B then card A.
For example, given 52, return 1. There's only one combination of 52 cards to pick from a 52 card deck. And given 2, return 1326, There's 1326 card combinations you can end up with when picking 2 cards from the deck.
"""

def combinations(cards):
    if cards>52 or cards<0:
        return 0
    elif cards==52 or cards==0:
        return 1
    elif cards==51 or cards==1:
        return 52
    else:
        if cards>26:
            cards=52-cards
        res=52
        for i in range(2,cards+1):
            res*=(52-i+1)/i
    return round(res)
    
""" 08-11-2025: Character Limit
In this challenge, you are given a string and need to determine if it fits in a social media post. Return the following strings based on the rules given:

"short post" if it fits within a 40-character limit.
"long post" if it's greater than 40 characters and fits within an 80-character limit.
"invalid post" if it's too long to fit within either limit.
"""
    
def can_post(msg):
    if len(msg)<=40:
        return "short post"
    elif len(msg)<=80:
        return "long post"
    else:
        return "invalid post"
        
""" 09-11-2025: Word Search
Given a matrix (an array of arrays) of single letters and a word to find, return the start and end indices of the word in the matrix.

The given matrix will be filled with all lowercase letters (a-z).
The word to find will always be in the matrix exactly once.
The word to find will always be in a straight line in one of these directions:
left to right
right to left
top to bottom
bottom to top
For example, given the matrix:

[
  ["a", "c", "t"],
  ["t", "a", "t"],
  ["c", "t", "c"]
]
And the word "cat", return:

[[0, 1], [2, 1]]
Where [0, 1] are the indices for the "c" (start of the word), and [2, 1] are the indices for the "t" (end of the word)."""

def find_word(m, w):
    pre=[]
    t=[[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    for i in range(len(m)):
        if "".join(m[i])[0:len(w)]==w:
            if len(m)==len(w):
                pre.append([i,0])
                pre.append([i,len(m)-1])
            else:
                pre.append([i,1])
                pre.append([i,len(m)-1])
        if "".join(m[i])[::-1][0:len(w)]==w:
            if len(m)==len(w):
                pre.append([i,len(m)-1])
                pre.append([i,0])
            else:
                pre.append([i,len(m)-1])
                pre.append([i,1])
        if "".join(t[i])[0:len(w)]==w:
            if len(m)==len(w):
                pre.append([0,i])
                pre.append([len(m)-1,i])
            else:
                pre.append([1,i])
                pre.append([len(m)-1,i])
        if "".join(t[i])[::-1][0:len(w)]==w:
            if len(m)==len(w):
                pre.append([len(m)-1,i])
                pre.append([0,i])
            else:
                pre.append([len(m)-1,i])
                pre.append([1,i])
    return pre

""" 10-11-2025: Extension Extractor
Given a string representing a filename, return the extension of the file.

The extension is the part of the filename that comes after the last period (.).
If the filename does not contain a period or ends with a period, return "none".
The extension should be returned as-is, preserving case.
"""
  
def get_extension(fn):
    sp=fn.split(".")
    if len(sp)<2 or sp[-1]=="":
        return "none"
    return sp[-1]

""" 11-11-2025: Vowels and Consonants
Given a string, return an array with the number of vowels and number of consonants in the string.

Vowels consist of a, e, i, o, u in any case.
Consonants consist of all other letters in any case.
Ignore any non-letter characters.
For example, given "Hello World", return [3, 7].
"""

import re
def count(s):
    v="aeiouAEIOU"
    sv=0
    sc=0
    for i in range(len(s)):
        if s[i].isalpha():
           sc+=1
        if s[i] in v:
           sv+=1
    return [sv,sc-sv]

""" 12-11-2025: Email Signature Generator
Given strings for a person's name, title, and company, return an email signature as a single string using the following rules:

The name should appear first, preceded by a prefix that depends on the first letter of the name. For names starting with (case-insensitive):
A-I: Use >> as the prefix.
J-R: Use -- as the prefix.
S-Z: Use :: as the prefix.
A comma and space (, ) should follow the name.
The title and company should follow the comma and space, separated by " at " (with spaces around it).
For example, given "Quinn Waverly", "Founder and CEO", and "TechCo" return "--Quinn Waverly, Founder and CEO at TechCo".
"""

def generate_signature(name, title, company):
    x1="abcdefghiABCDEFGHI"
    x2="jklmnopqrJKLMNOPQR"
    x3="stuvwxyzSTUVWXYZ"
    if name[0] in x1:
        res=">>"
    elif name[0] in x2:
        res="--"
    else:
        res="::"
    sig=res+name+", "+title+" at "+company
    return sig
 
""" 13-11-2025: Array Shift
Given an array and an integer representing how many positions to shift the array, return the shifted array.

A positive integer shifts the array to the left.
A negative integer shifts the array to the right.
The shift wraps around the array.
For example, given [1, 2, 3] and 1, shift the array 1 to the left, returning [2, 3, 1].
"""

def shift_array(arr, n):
    new=arr*5
    s=new[n:n+len(arr)]
    if n<0:
        s=new[n+len(arr):n+2*len(arr)]
    return s

""" 14-11-2025: Is It the Weekend?
Given a date in the format "YYYY-MM-DD", return the number of days left until the weekend.

The weekend starts on Saturday.
If the given date is Saturday or Sunday, return "It's the weekend!".
Otherwise, return "X days until the weekend.", where X is the number of days until Saturday.
If X is 1, use "day" (singular) instead of "days" (plural).
Make sure the calculation ignores your local timezone.
"""

from datetime import date
def days_until_weekend(date_string):
    y=int(date_string[0:4])
    m=int(date_string[5:7])
    d=int(date_string[8:10])
    dt=date(y,m,d)
    wd=dt.weekday()
    if wd==5 or wd==6:
        return "It's the weekend!"
    elif wd==4:
        return "1 day until the weekend."
    else:
        return f"{5-wd} days until the weekend."

""" 15-11-2025: GCD
Given two positive integers, return their greatest common divisor (GCD).

The GCD of two integers is the largest number that divides evenly into both numbers without leaving a remainder.
For example, the divisors of 4 are 1, 2, and 4. The divisors of 6 are 1, 2, 3, and 6. So given 4 and 6, return 2, the largest number that appears in both sets of divisors.
"""

def gcd(x, y):
    if x>y:
        r=list(range(1,x+1))
    else:
        r=list(range(1,y+1))
    res=[]
    for i in range(len(r)):
        if x%r[i]==0 and y%r[i]==0:
            res.append(r[i])
    return res[-1]

""" 16-11-2025: Rectangle Count
Given two positive integers representing the width and height of a rectangle, determine how many rectangles can fit in the given one.

Only count rectangles with integer width and height.
For example, given 1 and 3, return 6. Three 1x1 rectangles, two 1x2 rectangles, and one 1x3 rectangle.
"""

def count_rectangles(width, height):
    cnt=0
    for i in range(1,width+1):
        for j in range(1,height+1):
            cnt+=(width-i+1)*(height-j+1)
    return cnt

""" 17-11-2025: Fingerprint Test
Given two strings representing fingerprints, determine if they are a match using the following rules:

Each fingerprint will consist only of lowercase letters (a-z).
Two fingerprints are considered a match if:
They are the same length.
The number of differing characters does not exceed 10% of the fingerprint length."""

def is_match(f_a, f_b):
    sn=0
    if len(f_a) !=len(f_b):
        return False
    else:
        if f_a==f_b:
           return True
        else: 
            for i in range(len(f_a)):
                if f_a[i]!=f_b[i]:
                    sn+=1
                    if sn/len(f_a)>0.1:
                        return False
    return True

""" 18-11-2025: 100 Characters
Welcome to the 100th Daily Coding Challenge!

Given a string, repeat its characters until the result is exactly 100 characters long. If your repetitions go over 100 characters, trim the extra so it's exactly 100.
"""

def one_hundred(chars):
    return (chars*100)[0:100]

""" 19-11-2025 Markdown Heading Converter
Given a string representing a Markdown heading, return the equivalent HTML heading.

A valid Markdown heading must:

Start with zero or more spaces, followed by
1 to 6 hash characters (#) in a row, then
At least one space. And finally,
The heading text.
The number of hash symbols determines the heading level. For example, one hash symbol corresponds to an h1 tag, and six hash symbols correspond to an h6 tag.

If the given string doesn't have the exact format above, return "Invalid format".

For example, given "# My level 1 heading", return "<h1>My level 1 heading</h1>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included. """

import re
def convert(heading):
    h=heading.strip().replace("  "," ")
    sp=h.split(" ")
    sn=0
    res=""
    for i in range(1,7):
        t="#"*i+" "
        s=sp[0]+" "
        j=" ".join(sp[1:])
        if s==t:
            res+=f"<h{i}>"
            res+=j
            res+=f"</h{i}>"
    for i in range(1,7):
        if sp[0]!="#"*i:
            sn+=1
        if sn==6:
            return "Invalid format"
    return res

""" 20-11-2025: Longest Word
Given a sentence string, return the longest word in the sentence.

Words are separated by a single space.
Only letters (a-z, case-insensitive) count toward the word's length.
If there are multiple words with the same length, return the first one that appears.
Return the word as it appears in the given string, with punctuation removed."""

def longest_word(s):
    stri=""
    for i in range(len(s)):
        if s[i].islower() or s[i].isupper() or s[i]==" ":
            stri+=s[i]
    sp=stri.split(" ")
    st=sorted(sp,key=len)
    maxi=len(st[-1])
    p=[]
    for i in range(len(sp)):
        if len(sp[i])==maxi:
            p.append(sp[i])
    return p[0]

""" 21-11-2025 LCM
Given two integers, return the least common multiple (LCM) of the two numbers.

The LCM of two numbers is the smallest positive integer that is a multiple of both numbers. For example, given 4 and 6, return 12 because:

Multiples of 4 are 4, 8, 12 and so on.
Multiples of 6 are 6, 12, 18 and so on.
12 is the smallest number that is a multiple of both. """
  
def gcd(x,y):
    if x>y:
        r=list(range(1,x+1))
    else:
        r=list(range(1,y+1))
    res=[]
    for i in range(len(r)):
        if x%r[i]==0 and y%r[i]==0:
            res.append(r[i])
    return res[-1]

def lcm(a, b):
    return a*b/gcd(a,b)

""" 22-11-2025: Recipe Scaler
Given an array of recipe ingredients and a number to scale the recipe, return an array with the quantities scaled accordingly.

Each item in the given array will be a string in the format: "quantity unit ingredient". For example "2 C Flour".
Scale the quantity by the given number. Do not include any trailing zeros and do not convert any units.
Return the scaled items in the same order they are given."""

def scale_recipe(ingredients, scale):
    ing=ingredients
    lst=[]
    for i in range(len(ing)):
        lst.append([])
        s=ing[i].split(" ")
        lst[i].append(str(float(s[0])*scale).replace(".0",""))
        lst[i].append(" ".join(s[1:]))
    res=[]
    for i in range(len(ing)):
        res.append(" ".join(lst[i]))
    return res
    
""" 23-11-2025: Character Count
Given a sentence string, return an array with a count of each character in alphabetical order.

Treat upper and lowercase letters as the same letter when counting.
Ignore numbers, spaces, punctuation, etc.
Return the count and letter in the format "letter count". For instance, "a 3".
All returned letters should be lowercase.
Do not return a count of letters that are not in the given string. """

def count_characters(s):
    stri=""
    v=[]
    for i in range(len(s)):
        if s[i].islower() or s[i].isupper():
           stri+=s[i].lower()
    k=sorted(list(set(list(stri))))
    for i in range(len(k)):
        v.append(len(stri.split(k[i]))-1)
    res=[]
    for i in range(len(k)):
        res.append(k[i]+" "+str(v[i]))
    return res

""" 24-11-2025: Message Validator
Given a message string and a validation string, determine if the message is valid.

A message is valid if each word in the message starts with the corresponding letter in the validation string, in order.
Letters are case-insensitive.
Words in the message are separated by single spaces."""

def is_valid_message(msg, val):
    res=""
    sp=msg.split(" ")
    if len(sp)!=len(val):
        return False
    else:
        for i in range(len(sp)):
            res+=sp[i][0].lower() 
        return val.lower()==res

""" 25-11-2025: FizzBuzz
Given an integer (n), return an array of integers from 1 to n (inclusive), replacing numbers that are multiple of:

3 with "Fizz".
5 with "Buzz".
3 and 5 with "FizzBuzz"."""

def fizz_buzz(n):
    lst=[]
    for i in range(n):
        if (i+1)%3!=0 and (i+1)%5!=0:
            lst.append(i+1)
        elif (i+1)%3==0 and (i+1)%5!=0:
            lst.append("Fizz")
        elif (i+1)%3!=0 and (i+1)%5==0:
            lst.append("Buzz")
        else:
            lst.append("FizzBuzz")
    return lst

""" 26-11-2025: BuzzFizz
Given an array, determine if it is a correct FizzBuzz sequence from 1 to the last item in the array. A sequence is correct if:

Numbers that are multiples of 3 are replaced with "Fizz"
Numbers that are multiples of 5 are replaced with "Buzz"
Numbers that are multiples of both 3 and 5 are replaced with "FizzBuzz"
All other numbers remain as integers in ascending order, starting from 1.
The array must start at 1 and have no missing or extra elements. """

def is_fizz_buzz(seq):
    lst=[]
    for i in range(len(seq)):
        if (i+1)%3!=0 and (i+1)%5!=0:
            lst.append(i+1)
        elif (i+1)%3==0 and (i+1)%5!=0:
            lst.append("Fizz")
        elif (i+1)%3!=0 and (i+1)%5==0:
            lst.append("Buzz")
        else:
            lst.append("FizzBuzz")
    for i in range(len(seq)):
        if seq[i]!=lst[i]:
            return False
    return True

""" 27-11-2025: What's My Age Again?
Given the date of someone's birthday in the format YYYY-MM-DD, return the person's age as of November 27th, 2025.

Assume all birthdays are valid dates before November 27th, 2025.
Return the age as an integer.
Be sure to account for whether the person has already had their birthday in 2025."""

from datetime import datetime
import math
def calculate_age(bday):
    y=int(bday[0:4])
    m=int(bday[5:7])
    d=int(bday[8:10])
    diff=int(str(datetime(2025,11,27)-datetime(y,m,d)).split(" ")[0])
    return math.floor(diff/365.25)

""" 28-11-2025: 
Word Guesser
Given two strings of the same length, a secret word and a guess, compare the guess to the secret word using the following rules:

The secret word and guess will only consist of uppercase letters ("A" to "Z");
For each letter in the guess, replace it with a number according to how it matches the secret word:
"2" if the letter is in the secret word and in the correct position.
"1" if the letter is in the secret word but in the wrong position.
"0" if the letter is not in the secret word.
Each letter in the secret word can be used at most once.
Exact matches ("2") are assigned first, then partial matches ("1") are assigned from left to right for remaining letters.
If a letter occurs multiple times in the guess, it can only match as many times as it appears in the secret word.
For example, given a secret word of "APPLE" and a guess of "POPPA", return "10201"
The first "P" is not in the correct location ("1"), the "O" isn't in the secret word ("0"), the second "P" is in the correct location ("2"), the third "P" is a zero ("0") because the two "P"'s in the secret word have been used, and the "A" is not in the correct location ("1")."""


def compare(word, guess):
    l=len(word)
    res=list(l*"0")
    word_used=list(l*"0")
    guess_used=list(l*"0")
    for i in range(l):
        if word[i]==guess[i]:
            res[i]="2"
            word_used[i]="1"
            guess_used[i]="1"
    for i in range(l):
        if guess_used[i]=="1":
            continue
        ch=guess[i]
        for j in range(l):
            if word_used[j]=="0" and word[j]==ch:
                res[i]="1"
                word_used[j]="1"
                break
    return "".join(res) 
  
""" 29-11-2025: Ball Trajectory
Today's challenge is inspired by the video game Pong, which was released November 29, 1972.

Given a matrix (array of arrays) that includes the location of the ball (2), and the previous location of the ball (1), return the matrix indices for the next location of the ball.

The ball always moves in a straight line.
The movement direction is determined by how the ball moved from 1 to 2.
The edges of the matrix are considered walls. If the ball hits a:
top or bottom wall, it bounces by reversing its vertical direction.
left or right wall, it bounces by reversing its horizontal direction.
corner, it bounces by reversing both directions."""

def get_next_location(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j]==1:
                r1=i
                c1=j
            if matrix[i][j]==2:
                r2=i
                c2=j
    dx=r2-r1
    dy=c2-c1
    nr=r2+dx
    nc=c2+dy
    if nr<0 or nr>3:
        ndx=-dx
        nr=r2+ndx
    if nc<0 or nc>3:
        ndy=-dy
        nc=c2+ndy
    return [nr,nc]

""" 30-11-2025: AI Detector
Today's challenge is inspired by the release of ChatGPT on November 30, 2022.

Given a string of one or more sentences, determine if it was likely generated by AI using the following rules:

It contains two or more dashes (-).

It contains two or more sets of parenthesis (()). Text can be within the parenthesis.

It contains three or more words with 7 or more letters.

Words are separated by a single space and only consist of letters (A-Z). Don't include punctuation or other non-letters as part of a word.

If the given sentence meets any of the rules above, return "AI", otherwise, return "Human"."""

def detect_ai(text):
    sp=text.split(" ")
    sn=0
    for i in range(len(sp)):
        if len(sp[i])>=7:
            sn+=1
    d=text.split("-")
    p1=text.split("(")
    p2=text.split(")")
    if sn>2 or len(d)>2 or len(p1)>2 and len(p2)>2:
        return "AI"
    return "Human"
