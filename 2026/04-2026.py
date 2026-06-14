""" 01-04-2026: Prank Number

Given an array of numbers where all but one number follow a pattern, return a new array with the one number that doesn't follow the pattern fixed.
The pattern will be one of:
• The numbers increase from one to the next by a fixed amount (addition).
• The numbers decrease from one to the next by a fixed amount (subtraction).
For example, given [2, 4, 7, 8, 10] return [2, 4, 6, 8, 10]. """

def freq(arr):
    d={}
    for i in range(len(arr)):
        if arr[i] in d.keys():
            d[arr[i]]+=1
        else:
            d[arr[i]]=1
    return d

def fix_prank_number(arr):
    d=[]
    desc=False
    if arr[0]>=arr[-1]:
       desc=True
    s=sorted(arr,reverse=desc)
    for i in range(1,len(s)):
        d.append(s[i]-s[i-1])
    res = max(freq(d), key=freq(d).get)
    c=(arr[1]-arr[0])==res
    for i in range(len(s)):
        s[i]=s[0]+i*res
    if desc and not c and arr[1]!=arr[0]:
        for i in range(len(s)):
            s[i]-=res
    if not desc and not c:
        for i in range(len(s)):
            s[i]+=res
    return s

""" 02-04-2026: Capitalized Fibonacci

Given a string, return a new string where each letter is capitalized if its index is a Fibonacci number, and lowercased otherwise.
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
• The first character is at index 0.
• If the index of non-letter characters is a Fibonacci number, leave it unchanged.
"""

def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def capitalize_fibonacci(s):
    fibi=[0]
    for i in range(1,16):
        fibi.append(fibo(i))
    res=""
    for i in range(len(s)):
        if i in fibi:
            res+=s[i].upper()
        else:
            res+=s[i].lower()
    return res

""" 03-04-2026: Browser History

Given an array of browser commands, return an array with two values: the history as an array of URLs, and the index of the current page.
Valid commands are:
• "URL" - Where URL is a web address ("freecodecamp.org" for example). Navigates to the given URL, adds it to the history at the next position, and discards any forward history.
• "Back" - moves to the previous page in history, or stays on the current page if there isn't one.
• "Forward" - moves to the next page in history, or stays on the current page if there isn't one.
For example, given ["freecodecamp.org", "freecodecamp.org/learn", "Back"], return [["freecodecamp.org", "freecodecamp.org/learn"], 0]. """

class BrowserHistory:
    def __init__(self): 
        self.backStack = []
        self.forwardStack=[]  
    def visit(self, url: str): 
        self.forwardStack.clear()
        self.backStack.append(url)
    def back(self, steps: int): 
        while len(self.backStack) > 1 and steps > 0: 
                self.forwardStack.append(self.backStack.pop())
                steps -= 1
        return self.backStack[-1]
    def forward(self, steps: int): 
        while len(self.forwardStack) > 0 and steps > 0: 
                self.backStack.append(self.forwardStack.pop())
                steps -= 1
        return self.backStack[-1]

def get_browser_history(c):
    sn=0
    bf=["Back","Forward"]
    if c[-1]=="Forward" and c[-2] not in bf:
        c=c[0:-1]
    for i in range(1,len(c)):
        if not c[i] in bf:
           sn+=1
        if c[i]=="Back":
               sn-=1
        if c[i]=="Forward":
               sn+=1
    h=BrowserHistory()
    for i in range(len(c)):
        if not c[i] in bf:
                h.visit(c[i])
        if c[i]=="Back":
                h.back(1)
        if c[i]=="Forward":
                h.forward(1)
    res=[]
    res.append(h.backStack+h.forwardStack)
    res.append(max(sn,0))
    return res

""" 04-04-2026: Equation Validation

Given a string representing a math equation, determine whether it is correct.
• The left side may contain up to three positive integers and the operators +, -, *, and /.
• The equation will be given in the format: "number operator number = number" (with two or three numbers on the left). For example: "2 + 2 = 4" or "2 + 3 - 1 = 4".
• The right side will always be a single integer.
Follow standard order of operations: multiplication and division are evaluated before addition and subtraction, from left-to-right. """

def is_valid_equation(equation):
    sp=equation.split("=")
    return eval(sp[0])==int(sp[1])

""" 05-04-2026: Digit Rotation Escape 

Given a positive integer, determine if it, or any of its rotations, is evenly divisible by its digit count.
A rotation means to move the first digit to the end. For example, after 1 rotation, 123 becomes 231.
• Check rotation 0 (the given number) first.
• Given numbers won't contain any zeros.
• Return the first rotation number if one is found, or "none" if not. """

def rotations(stri):
    rots=[stri]
    for i in range(1,len(stri)):
        rot=rots[i-1][1:]+rots[i-1][0]
        rots.append(rot)
    return rots

def get_rotation(n):
    rots=rotations(str(n))
    for i in range(len(rots)):
        if int(rots[i])%len(str(n))==0:
            return i
    return "none"

""" 06-04-2026: What Day Is It?

Given a Unix timestamp in milliseconds, return the day of the week.
Valid return days are:
• "Sunday"
• "Monday"
• "Tuesday"
• "Wednesday"
• "Thursday"
• "Friday"
• "Saturday"
Be sure to ignore time zones. """

import datetime
import time
def get_day_of_week(timestamp):
    days={0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
    t = time.time()
    d = datetime.date.fromtimestamp(timestamp/1000);
    return days[d.weekday()]

""" 07-04-2026 Palindrome Characters

Given a string, determine if it's a palindrome and return the middle character (if it's odd length) or middle two characters (if it's even).
• A palindrome is a string that is the same forward and backward.
• If it's not a palindrome, return "none". """

def palindrome_locator(s):
    c=s[::-1]==s
    if not c:
        return "none"
    if len(s)%2==1:
        v=s[int((len(s)-1)/2)]
    else:
        v=s[int(len(s)/2-1):int(len(s)/2+1)]
    return v

""" 08-04-2026: FizzBuzz Validator

Given an array of sequential integers, with multiples of 3 and 5 replaced, determine if it's a valid FizzBuzz sequence.
In a valid FizzBuzz sequence:
• Multiples of 3 are replaced with "Fizz".
• Multiples of 5 are replaced with "Buzz".
• Multiples of both 3 and 5 are replaced with "FizzBuzz".
• All other numbers remain as integers. """

def is_fizz_buzz(arr):
    c=[arr[0]]
    for i in range(1,len(arr)):
        if not isinstance(arr[i],int):
            if isinstance(arr[i-1],int):
                c.append(arr[i-1]+1)
            elif isinstance(arr[i+1],int):
                c.append(arr[i+1]-1)      
            else: c.append(arr[i])
        else: c.append(arr[i])
    m=[]
    for i in range(len(c)):
        if not isinstance(c[i],int):
            m.append(c[i])
        elif isinstance(c[i],int):
            if c[i]%3==0 and c[i]%5!=0:
                m.append("Fizz")
            elif c[i]%3!=0 and c[i]%5==0:
                m.append("Buzz")
            elif c[i]%3==0 and c[i]%5==0:
                m.append("FizzBuzz")
            else:
                m.append(c[i])
    return m==arr
    
""" 09-04-2026: Next Bingo Number

Given a bingo number, return the next bingo number sequentially.
A bingo number is a single letter followed by a number in its range according to this chart:
LetterNumber Range
         "B"             1-15
         "I"             16-30
        "N"             31-45
        "G"             46-60
        "O"             61-75
For example, given "B10", return "B11", the next bingo number. If given the last bingo number, return "B1". """

def get_next_bingo_number(n):
    b=["B","I","N","G","O"];
    if n[1:]=="75":
        return "B1"
    p=str(int(n[1:])+1)
    print(p)
    if int(n[1:])%15==0:
        return b[b.index(n[0])+1]+p
    else:
        return n[0]+p
    
""" 10-04-2026: Rook Attack

Given two strings for the location of two rooks on a chess board, determine if they can attack each other.
A standard chessboard is 8x8, with columns labeled A through H (left to right) and rows labeled 1 through 8 (bottom to top). """

def rook_attack(rook1, rook2):
    return rook1[0]==rook2[0] or rook1[1]==rook2[1]


""" 11-04-2026: Rook and Bishop Attack

Given a string for the location of a rook on a chess board, and another for the location of a bishop, determine if one piece can attack another.
A standard chessboard is 8x8, with columns labeled A through H (left to right) and rows labeled 1 through 8 (bottom to top).  """

def rook_bishop_attack(rook, bishop):
    l="ABCDEFGH"
    if rook[0]==bishop[0] or rook[1]==bishop[1]:
        return "rook"
    elif abs(l.index(rook[0])-l.index(bishop[0]))==abs(int(rook[1])-int(bishop[1])):
        return "bishop"
    else:
        return "neither"

""" 12-04-2026: Spiral Matrix

Given a 2D matrix, return a flat array with all of its values in clockwise order.
The returned array should have the top-left value first, move right along the top row, then down the right column, then left along the bottom row, then up the left column. Repeat inward for any remaining layers.
For example, given:
[ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] 
Return [1, 2, 3, 6, 9, 8, 7, 4, 5]. """

import math 
from itertools import chain

def flatten(arr):
    fl=[]
    for el in arr:
        if isinstance(el,list):
            fl.extend(flatten(el))
        else:
            fl.append(el)
    return fl    

def transpose(M):
    n = len(M[0])
    L = list(chain(*M))
    return [L[i::n] for i in range(n)]

def sliced(matrix,row,st,l,d):
    s=matrix[row][st:st+l]
    if d==0:
      return s
    else:
        return [s[len(s)-1-i] for i in range(len(s))]

def spiral_matrix(matrix):
    c=len(matrix[0])
    r=len(matrix)
    trans=transpose(matrix)
    rows=[]
    cols=[]
    sn=0
    for i in range(math.ceil(r/2)):
        if r==c:
            rows.append(sliced(matrix,i,i,r-sn,0))
            rows.append(sliced(matrix,r-i-1,i,r-sn-1,1))
        if r==c+1:
            rows.append(sliced(matrix,i,i,r-sn-i,0))
            rows.append(sliced(matrix,r-i-1,i,r-sn-2,1))
        sn+=2
    sn=0
    for i in range(math.ceil(c/2)):
        if r==c:
            cols.append(sliced(trans,c-1-i,i+1,c-sn-1,0))
            cols.append(sliced(trans,i,i+1,c-sn-2,1))
        if r==c+1:
            cols.append(sliced(trans,c-1-i,i+1,c-sn,0))
            cols.append(sliced(trans,i,i+1,c-sn-1,1))
        sn+=2
    pre=[]
    for i in range(len(rows)):
        pre.append(rows[i])
        pre.append(cols[i])
    return flatten(pre)

""" 13-04-2026: Name Initials

Given a full name as a string, return their initials.
• Names to initialize are separated by a space.
• Initials should be made uppercase.
• Initials should be separated by dots.
For example, "Tommy Millwood" returns "T.M.". """

def get_initials(name):
    return "".join([name.split(" ")[i][0]+"." for i in range(len(name.split(" ")))])


""" 14-04-2026: Last Letter

Given a string, return the letter from the string that appears last in the alphabet.
• If two or more letters tie for the last in the alphabet, return the first one.
• Ignore all non-letter characters. """

def get_last_letter(s):
    l=sorted([el.lower() for el in s if el.isalpha()])[-1]
    u=l.upper()
    if not u in s:
        return l
    elif not l in s:
        return u
    else:
        return s[min(s.index(u),s.index(l))]


""" 15-04-06: Sorted Array Swap

Given an array of integers, return a new array using the following rules:
• Sort the integers in ascending order
• Then swap all values whose index is a multiple of 3 with the value before it. """

def sort_and_swap(arr):
    s=sorted(arr)
    for i in range(1,len(s)):
        if i%3==0:
            temp=s[i-1]
            s[i-1]=s[i]
            s[i]=temp
    return s

""" 16-04-2026: String Math

Given a string with numbers and other characters, perform math on the numbers based on the count of non-digit characters between the numbers.
• If the count of characters separating two numbers is even, use addition.
• If it's odd, use subtraction.
• Consecutive digits form a single number.
• Operations are applied left to right.
• Ignore leading and trailing characters that aren't digits.
For example, given "3ab10c8", return 5. Add 3 and 10 to get 13 because there's an even number of characters between them. Then subtract 8 from 13 because there's an odd number of characters between the result and 8. """

import re
def do_math(s):
    m1=re.findall("[0-9]+",s)
    m2=re.findall("\D+",s)
    ops=["+" if len(m2[i])%2==0 else "-" for i in range(len(m2))]
    if not s[0].isnumeric() and not s[-1].isnumeric():
        ops=ops[1:-1]
    res=int(m1[0])
    for i in range(len(ops)):
        if ops[i]=="+":
           res=res+int(m1[i+1])
        else:
           res=res-int(m1[i+1])
    return res

""" 17-04-2026: Hidden Key

Welcome to the 250th daily challenge!
Given an encoded string, decode it using an encryption key and return it.
To find the key:
• Look at all daily challenges up to today whose challenge number is a multiple of 25 (including this one).
• Take the first letter from each of those challenge titles and combine them into a string. If the title starts with a non-letter, find its first letter.
To decode the message, go over each letter in the encoded message and:
• Look at the corresponding letter in the key (repeat the key if the message is longer than the key).
• Convert the key letter to its corresponding number: "A" = 1, "B" = 2, ..., "Z" = 26.
• Shift the encoded letter backward in the alphabet by that number.
• If the shift goes before "A", wrap around to "Z".
For example, if the encoded message starts with "Y" and the first key letter is "V" (22), shift "Y" back 22 places to get "C". Repeat this process for each letter to decode the full message.
• Only letters are shifted, spaces are returned as-is.
• All given and returned letters are uppercase. """

import math
def decode(message):
    k="VLHCGMDLNH"*math.ceil(len(message)/10)
    a="ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    sp=message.split(" ")
    sn1=0
    sn2=len(sp[0])
    sl=[[sn1,sn2]]
    for i in range(1,len(sp)):
        sn1=sl[i-1][1]
        sn2=sn1+len(sp[i])
        sl.append([sn1,sn2])
    msg=message.replace(" ","")
    pre=""
    for i in range(len(msg)):
        c1=a.index(k[i])+1
        s=a.index(msg[i])+1-c1
        if s<1:
            c2=s+26
        else:
            c2=s
        ch=a[c2-1]
        pre+=ch
    res=""
    for i in range(len(sl)):
        res+=pre[sl[i][0]:sl[i][1]]+" "
    return res[0:-1]

""" 18-04-2026: Array Sum Finder

Given an array of numbers and a target number, return the first subset of two or more numbers that adds up to the target.
• The "first" subset is the one whose elements have the lowest possible indices, prioritizing the earliest index first.
• Each number in the array may only be used once.
• If no valid subset exists, return "Sum not found".
Return the matching numbers as an array in the order they appear in the original array. """

import itertools
def get_subsets(nums):
    res=[]
    for i in range(2,len(nums)+1):
        combs=[list(el) for el in list(itertools.combinations(nums, i))]
        for j in range(len(combs)):
            res.append(combs[j])
    return res
 
def find_sum(arr, target):
    pos=[el for el in arr if el>0]
    if len(pos)==len(arr):
        arr=[el for el in arr if el<=target-1]
    subs=get_subsets(arr)
    subs=[el for el in subs if sum(el)==target]
    if len(subs)==0:
        return "Sum not found"
    ind=[]
    for i in range(len(subs)):
        lst = [arr.index(subs[i][j]) for j in range(len(subs[i]))]
        ind.append(lst)
    ind=[el for el in ind if list(set(el))==el]
    s=sorted(ind)[0]
    return [arr[i] for i in s]

""" 19-04-2026: Unique Stair Climber

Given a number of stairs, return how many distinct ways someone can climb them taking either 1 or 2 steps at a time. """

def get_unique_climbs(steps):
    arr=[1,2]
    for i in range(2,steps):
        arr.append(arr[i-2]+arr[i-1])
    return arr[steps-1]

""" 20-04-2026: Acronym Finder

Given a string representing an acronym, return the full name of the organization it belongs to from the list below:
• "National Avocado Storage Authority"
• "Cats Infiltration Agency"
• "Fluffy Beanbag Inspectors"
• "Department Of Jelly"
• "Wild Honey Organization"
• "Eating Pancakes Administration"
Each letter in the given acronym should match the first letter of each word in the organization it belongs to, in the same order. """

def find_org(acronym):
    arr=["National Avocado Storage Authority",
"Cats Infiltration Agency",
"Fluffy Beanbag Inspectors",
"Department Of Jelly",
"Wild Honey Organization",
"Eating Pancakes Administration"]
    pre=[arr[i].split(" ") for i in range(len(arr))]
    acs=[]
    for i in range(len(pre)):
        lst=[pre[i][j][0] for j in range(len(pre[i]))]
        acs.append("".join(lst))
    return arr[acs.index(acronym)]


""" 21-04-2026: Odd Words

Given a string of words, return only the words with an odd number of letters.
• Words in the given string will be separated by a single space.
• Return the words separated by a single space. """

def get_odd_words(s):
    sp=s.split(" ")
    return " ".join([sp[i] for i in range(len(sp)) if len(sp[i])%2==1])

""" 22-04-2026: Earth Day Cleanup Crew
Today is Earth Day. Given an array of items you cleaned up, return your total cleanup score based on the rules below.
Given items will be one of:
ItemBase Value"bottle"10"can"6"bag"8"tire"35"straw"4"cardboard"3"newspaper"3"shoe"12"electronics"25"battery"18"mattress"38
A Rare item is represented as ["rare", value]. For example, ["rare", 80]. Rare items do not get a streak bonus.
• Streak bonus: If the same item appears consecutively, it gets increasing bonus points.
• First consecutive occurrence: base value
• Second: base value + 1
• Third: base value + 2
• etc.
• Fifth Item Multiplier: Every fifth item collected gets a multiplier.
• Fifth item: *2
• Tenth item: *3
• etc.
• Apply the multiplier after calculating any bonuses. """

def get_cleanup_score(items):
    obj={"bottle":10,"can":6,
"bag":8,"tire":35,"straw":4,
"cardboard":3,"newspaper":3,
"shoe":12,"electronics":25,
"battery":18,"mattress":38}
    s=[]
    sn=0
    for i in range(len(items)):
        if isinstance(items[i],list):
            sn=0
            s.append(items[i][1])
        elif items[i]==items[i-1] and i>=1:
            sn+=1
            s.append(obj[items[i]]+sn)
        else:
            sn=0
            s.append(obj[items[i]])
    for i in range(len(s)):
        if (i+1)%5==0:
            s[i]*=((i+1)/5+1)
    return int(sum(s))

""" 23-04-2026: Closest Time Direction

Given two times, determine whether you can get from the first to the second faster by moving forward or backward.
• Times are given in 24-hour format ("HH:MM")
• The clock wraps around (23:59 goes to 00:00 when moving forward, and 00:00 goes to 23:59 when moving backwards)
Return:
• "forward" if moving forward is shorter
• "backward" if moving backward is shorter
• "equal" if both directions take the same amount of time """

def get_direction(time1, time2):
    t1=int(time1[0:2])*60+int(time1[3:5])
    t2=int(time2[0:2])*60+int(time2[3:5])
    d1=(t2-t1)/60
    d2=(24*60-(t2-t1))/60%24
    print(d1)
    print(d2)
    if d1<0:
        if abs(d1)>12:
            return "forward"
        if abs(d1)<12:
            return "backward"
        else:
            return "equal"
    else:
        if d1<d2:
            return "forward"
        elif d2<d1:
            return "backward"
        else:
            return "equal"

""" 24-04-2026: Word Compressor

Given a string, return a compressed version of the string using the following rules:
• The first occurrence of a word remains unchanged.
• Subsequent occurrences are replaced with the position of the first occurrence, where the first word is at position 1.
• Words are separated by a single space.
For example, given "practice makes perfect and perfect practice makes perfect", return "practice makes perfect and 3 1 2 3".
"""

def compress(s):
    sp=s.split(" ")
    res=""
    for i in range(len(sp)):
        if sp[i] in sp[0:i]:
            res+=str(sp.index(sp[i])+1)+" "
        else:
            res+=sp[i]+" "
    return res[0:-1]

""" 25-04-2026: Word Decompressor

Given a compressed string, return the decompressed version using the following rules:
• The given string is made up of words and numbers separated by spaces.
• Leave the words unchanged.
• Replace numbers with the word at that position, where the first word is at position 1.
For example, given "practice makes perfect and 3 1 2 3", return "practice makes perfect and perfect practice makes perfect". """

import re
def decompress(s):
    sp=s.split(" ")
    d=re.findall("[0-9]+",s)
    res=""
    for i in range(len(sp)):
        if sp[i] in d:
            res+=sp[int(sp[i])-1]+" "
        else:
            res+=sp[i]+" "
    return res[0:-1]

""" 26-04-2026: FizzBuzz Explosion

Given an integer, return the number of steps it takes to turn the word "fizzbuzz" into a string with at least the given number of "z"'s using the following rules:
• Start with the string "fizzbuzz".
• Each step, apply the standard FizzBuzz rules using the letter position in the string (the first "f" is position 1).
• If the letter position is divisible by 3, replace the letter with "fizz"
• If it's divisible by 5, replace the letter with "buzz"
• If it's divisible by 3 and 5, replace the letter with "fizzbuzz"
So after 1 step, "fizzbuzz" turns into "fifizzzbuzzfizzzz", which has 9 "z"'s. """


def joined(lst):
    res=""
    for i in range(len(lst)):
        res+=lst[i]
    return res

def explode_fizzbuzz(target_z_count):
    arr=list("afizzbuzz")
    for j in range(15):
        for i in range(1,len(arr)):
            if i%3==0 and i%5!=0:
                arr[i]="fizz"
            if i%3!=0 and i%5==0:
                arr[i]="buzz"
            if i%3==0 and i%5==0:
                arr[i]="fizzbuzz"
        arr=joined(arr)
        sp=len(arr.split("z"))-1
        if sp>=target_z_count:
            return j+1
        arr=list(arr)

""" 27-04-2026: Word Score

Given a word, return its score using a standard letter-value table:
LetterValueA1B2......Z26
• Upper and lowercase letters have the same value. """

def get_word_score(word):
    a="#abcdefghijklmnopqrstuvwxyz"
    sn=0
    for el in word:
        sn+=a.index(el.lower())
    return sn

""" 28-04-2026: Number Words

Given an integer from 0 to 99, return its English word representation.
• 0 returns "zero".
• Numbers 1-19 have unique names ("one", "two", ..., "ten", "eleven", ..., "eighteen", "nineteen").
• Multiples of 10 from 20-90 have their own names ("twenty", "thirty", ..., "eighty", "ninety").
• Numbers 21-99 that are not multiples of 10 are written as two words joined by a hyphen. For example "forty-two" and "fifty-three". """

import math
def get_number_words(n):
    w1=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    w2=["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    if n<=19:
        return w1[n]
    elif n%10==0:
        return w2[int(n/10)-2]
    else:
        return w2[math.floor(n/10)-2]+"-"+w1[n%10]


""" 29-04-2026: URL Query Parser

Given a URL that contains a query string, parse the query string into an object (or dictionary) of key-value pairs.
• The query string begins after the "?",
• each parameter is separated by "&",
• each key/value pair is separated by "="
For example, given "https://example.com/search?name=Alice&age=30", return:
{ "name": "Alice", "age": "30" } 
All values should be returned as strings. """

def parse_url_query(url):
    sp=url.split("?")[1].split("&")
    res={}
    k=[el.split("=")[0] for el in sp]
    v=[el.split("=")[1] for el in sp]
    for i in range(len(k)):
        res[k[i]]=v[i]
    return res

""" 30-04-2026: Binary Crossword

Given a character, determine if its 8-bit binary representation can be found in the following grid, horizontally or vertically in either direction:
0 1 0 0 0 0 0 1 
0 1 1 0 1 1 1 1 
0 1 0 0 0 1 0 0 
0 1 1 0 0 1 0 1
0 1 0 1 0 0 1 0 
0 1 0 1 0 1 0 0 
0 1 1 0 1 0 0 0 
1 0 1 0 1 1 1 0 
For example, "A" has the binary representation 01000001, which appears in the first row from left to right. """

import math 
from itertools import chain
def toNum(stri):
    n=0
    for i in range(8):
        n+=math.pow(2,7-i)*int(stri[i])
    return int(n)

def transpose(M):
    n = len(M[0])
    L = list(chain(*M))
    return [L[i::n] for i in range(n)]

def is_in_crossword(char):
    grid=[list("01000001"),list("01101111"),list("01000100"),list("01100101"),list("01010010"),list("01010100"),list("01101000"),list("10101110")]
    trans=transpose(grid)
    arr=["".join([grid[i][i] for i in range(8)]),
    "".join([grid[7-i][7-i] for i in range(8)]),
    "".join([grid[i][7-i] for i in range(8)]),
    "".join([grid[7-i][i] for i in range(8)])]
    for i in range(len(grid)):
        stri="".join(grid[i])
        arr.append(stri)
        arr.append(stri[::-1])
        stri2="".join(trans[i])
        arr.append(stri2)
        arr.append(stri2[::-1])
    pre=[toNum(arr[i]) for i in range(len(arr))]
    res = list(''.join(map(chr, pre)))
    return char in res
