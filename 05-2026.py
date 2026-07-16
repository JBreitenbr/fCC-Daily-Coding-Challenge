""" 01-05-2026: Anagram Groups

Given an array of words, return a 2d array of the words grouped into anagrams.
• Words are anagrams if they contain the same letters in any order.
• Each word belongs to exactly one group.
• Return order doesn't matter.
For example, given ["listen", "silent", "hello", "enlist", "world"], return [["listen", "silent", "enlist"], ["hello"], ["world"]]. """

def group_anagrams(words):
    hlp=[]
    for i in range(len(words)):
        hlp.append(["".join(sorted(words[i])),i])
    pre=[[el] for el in words]
    for j in range(len(words)):
        for i in range(len(hlp)):
            if hlp[i][0]=="".join(sorted(words[j])) and hlp[i][1]!=j:
                pre[j].append(words[hlp[i][1]])
    res=[]
    for i in range(len(pre)):
        s=sorted(pre[i])
        if not s in res:
            res.append(s)
    return res

""" 02-05-2026: Deepest Brackets
Given a string containing balanced brackets, return the content of the deepest nested brackets.
• Brackets can be any of the three types: (), [], and {}.
• The input will always have a single deepest group.
For example, given "(hello (world))", return "world". """

def get_deepest_brackets(s):
   p=[]
   z=[]
   s1=0
   s2=0
   for i in range(len(s)):
      if s[i] in ["{","[","("]:
         p.append(i)
         z.append(s1-s2)
         s1+=1
      if s[i] in ["}","]",")"]:
         p.append(i)
         z.append(s1-s2)
         s2+=1
   maxi=z.index(max(z))
   return s[p[maxi-1]+1:p[maxi]]

""" 03-05-2026: Good Day
Given a time string in "HH:MM" format (24-hour clock), return:
• "Good morning" for times 05:00 to 11:59
• "Good afternoon" for times 12:00 to 17:59
• "Good evening" for times 18:00 to 21:59
• "Good night" for times 22:00 to 04:59 """

def get_greeting(s):
    h=int(s[0:2])
    if h>=5 and h<12:
        return "Good morning"
    elif h>=12 and h<18:
        return "Good afternoon"
    elif h>=18 and h<22:
        return "Good evening"
    else:
        return "Good night"

""" 04-05-2026: Parsec Converter
In a distant galaxy, parsecs are used to measure both time and distance. Given an integer number of parsecs, return its equivalent in time or distance.
• If the given integer is odd, it represents time. If it's even, it represents distance.
Use these conversion rates:
ParsecsTime/Distance12 hours26 light years
Return the converted value as an integer. """

def convert_parsecs(parsecs):
    if parsecs%2==1:
       return parsecs*2
    else:
       return parsecs*3

""" 05-05-2026: Narcissistic Number
Given a positive integer, determine whether it is a narcissistic number.
• A number is narcissistic if the sum of each of its digits raised to the power of the total number of digits equals the number itself.
For example, 153 has 3 digits, and 13 + 53 + 33 = 153, so it is narcissistic. """

import math
def is_narcissistic(n):
    return n==int(sum([math.pow(int(str(n)[i]),len(str(n))) for i in range(len(str(n)))]))

""" 06-05-2026: Allergen Friendly Meals
Given an array of meals and an array of allergens to avoid, return the names of all the meals that contain none of the given allergens.
• Each meal is in the format [meal, allergens], where meal is the name of the meal, and allergens is an array of the allergens the meal contains. For example, ["pasta", ["wheat", "milk"]].
• Allergens to avoid will be an array of strings.
Return safe meal names in the same order given. If no meal is safe, return an empty array. """

def get_allergen_friendly_meals(meals, allergens):
    res=[]
    for m in meals:
        if not set(m[1]).intersection(set(allergens)):
            res.append(m[0])
    return res

""" 07-05-2026: Longest Common Substring
Given a string, return the longest substring that appears more than once.
• The substrings can overlap. """

def indices(source,find):
    res=[]
    for i in range(len(source)):
        if source[i:i+len(find)]==find:
            res.append(i)
    return res

def get_longest_substring(s):
    lst=[]
    for i in range(len(s)):
        for j in range(len(s)):
            sub=s[j:i]
            if len(sub)>0:
               lst.append(sub)
    lst=list(set(lst))
    res=[]
    for i in range(len(lst)):
        ind=indices(s,lst[i])
        if len(ind)>=2:
            res.append(lst[i])
    res.sort(key=lambda s: len(s))
    return res[-1]

 
""" 08-05-2026: Medication Reminder
Given an array of medications and a string representing the current time, return the next medication you need to take and how long until you need to take it.
• Each medication is in the format [name, lastTaken], where name is the name of the medication and lastTaken is the time it was last taken.
• All given times will be in "HH:MM" (24-hour) format.
Use the following medication schedule:

Name
Schedule

Deployxitrin
08:00, 16:00

Debuggamanizole
07:00, 13:00, 21:00

Mergeflictamine
every 4 hours


Return a string in the format "{name} in Hh Mm". For example, "Debuggamanizole in 2h 0m" or "Deployxitrin in 1h 5m". """

import math

def to_min(tstri):
    return int(tstri[0:2])*60+int(tstri[3:5])

def to_stri(mins):
    _h=str(math.floor(mins/60))
    _m=str(mins-60*int(_h))
    return _h+"h "+_m+"m"

def medication_reminder(medis, curr_t):
    meds=["Deployxitrin","Debuggamanizole","Mergeflictamine"]
    if medis[0][1]=="08:00":
        first=to_min("16:00")
    else:
        first=to_min("08:00")
    if medis[1][1]=="07:00":
        second=to_min("13:00")
    elif medis[1][1]=="13:00":
        second=to_min("21:00")
    else:
        second=to_min("07:00")
    third=to_min(medis[2][1])+240
    curr=to_min(curr_t)
    arr=[abs(first-curr),abs(second-curr),abs(third-curr)]
    ind=arr.index(min(arr))
    return f"{meds[ind]} in {to_stri(arr[ind])}"    
    
""" 09-03-2026: Transposed Matrix
Given a matrix (an array of arrays), return the transposed version of it. """
from itertools import chain
def transpose(matrix):
n = len(matrix[0])
L = list(chain(*matrix))
return [L[i::n] for i in range(n)]

""" 10-05-2026: ISBN-13 Validator
Given a string, determine if it is a valid ISBN-13 number.
A valid ISBN-13:
• Contains only digits and hyphens
• Has exactly 13 digits after removing hyphens
• Passes the following check:
A. Multiply each digit by 1 or 3, alternating (multiply the first digit by 1, the second by 3, the third by 1, and so on).
B. The sum of the results must be divisible by 10. """

import re
def is_valid_isbn_13(s):
    s=s.replace("-","")
    r=re.findall("[0-9]+",s)
    if len(r)!=1 or len(r[0])!=13:
        return False
    lst=list(r[0])
    sn=0
    for i in range(len(lst)):
        if i%2==0:
            sn+=int(lst[i])
        else:
            sn+=int(lst[i])*3
    return sn%10==0
    
""" 11-05-2026: Oldest Person
Given an array of objects, each with a "name" and "age" property, return an array containing the name of the oldest person.
If multiple people share the oldest age, return all of their names in the order they appear in the input. """

def get_oldest(people):
    return [el["name"] for el in people if el["age"]==max([el["age"] for el in people])]

""" 12-05-2026:
Character Frequency
Given a string, return an object (JavaScript) or dictionary (Python) mapping each character to the number of times it appears. """

def get_frequency(s):
    d={}
    for l in s:
      if not l in d:
          d[l]=1
      else:
          d[l]+=1
   return d


""" 13-05-2026: Offending Element
Given an array of integers that is sorted in ascending order except for one out-of-place element, return the index of that element.
• If more than one element could be considered out of place, return the index of the first one. """

def minus_one(lst,ind):
    res=[]
    for i in range(len(lst)):
        if i!=ind:
            res.append(lst[i])
    return res

def find_offender(arr):
    for i in range(len(arr)):
        if minus_one(arr,i)==sorted(minus_one(arr,i)):
            return i

""" 14-05-2026: Mirror Image
Given two strings, determine if the second string is a mirror image of the first.
A mirror image is formed by reversing the string and replacing each character with its mirror equivalent.
• Symmetric characters look like themselves in a mirror:
W, T, Y, U, I, O, H, A, X, V, M, w, o, x, v, 0, 8, =, +, :, |, -, _, *, ^, !, ., and the space ().
• Mirrored pairs swap with each other in a mirror:

Character
Swaps with

[
]

{
}

<
>

b
d

p
q

(
)


If either string includes a character not in the lists above, it doesn't have mirror image that can be created from the characters.
For example, the mirrored image of "[HOW]" is "[WOH]". """

def is_mirror_image(s1, s2):
    swap={"[":"]","{":"}","<":">","b":"d","p":"q","(":")","]":"[","}":"{",">":"<","d":"b","q":"p",")":"("}
    m=list(s1[::-1])
    res=""
    for el in m:
        if el in swap.keys():
            res+=swap[el]
        else:
            res+=el
    return res==s2
    
""" 15-05-2026: Coffee Order Parser
Given a string for a coffee order, identify any menu items and return a formatted order.
Use the following menu items and prices:

Item
Price

"cold brew"
$4.50

"oat latte"
$5.00

"cappuccino"
$4.75

"espresso"
$3.00

"vanilla syrup"
$0.75

"caramel drizzle"
$0.60

"extra shot"
$0.50

"oat milk"
$0.75

"cream"
$0.75


Return a string with the matched items joined by " + ", followed by a colon and space (": "), and the total price.
For example, given "I'd like an oat latte with vanilla syrup and an extra shot please.", return "oat latte + vanilla syrup + extra shot: $6.25"
Items should appear in the order they appear in the menu and the total price should always have two decimal places. """

def format_coffee_order(order):
    drinks=["cold brew","oat latte","cappuccino","espresso","vanilla syrup",
    "caramel drizzle"	,"extra shot","oat milk","cream"]
    prices=[4.50,5.00,4.75,3.00,0.75,0.60,0.50,0.75,0.75]
    ind=[[order.find(drinks[i]),order.find(drinks[i])+len(drinks[i]),prices[i]] for i in range(len(drinks)) if order.find(drinks[i])>=0]
    print(ind)
    sn=0
    pre=""
    for i in range(len(ind)):
        sn+=ind[i][2]
        pre+=order[ind[i][0]:ind[i][1]]+" + "
    pr=str(sn)
    if int(sn)==sn or int(10*sn)==10*sn:
        pr=str(sn)+"0"
    return pre[0:-3]+": $"+pr

""" 16-05-2026: Longest Domino Chain
Given a 2D array representing a set of dominoes, return the longest valid chain.
• Each domino is a pair of numbers from 0–6, e.g. [3, 2].
• A chain is valid when the second number of each domino matches the first number of the next.
• The first number of the first domino and the second number of the last one don't need to match anything.
• Any domino can be flipped, so [3, 2] can be played as [2, 3].
• There is always exactly one longest valid chain.
For example, given [[1, 2], [4, 5], [2, 3]], return [[1, 2], [2, 3]]. """

""" 17-05-2026: Mongo ID Date
Given a MongoDB ID string, return its creation time as an ISO 8601 string.
• A MongoDB ID is a 24-character hex string. The first 8 characters represent a Unix timestamp (in seconds) encoded as a base-16 integer.
For example, "6a094b50bcf86cd799439011" has a timestamp of "6a094b50" in hex, which is 1778994000 in decimal, representing a creation time of "2026-05-17T05:00:00.000Z". """

from datetime import datetime
def mongo_id_to_date(s):
    return (datetime.utcfromtimestamp(int(s[0:8],16))).isoformat()+".000Z"

""" 18-05-2026: Bingo Range
Given a bingo letter, return the number range associated with that letter.

Letter
Number Range

"B"
1-15

"I"
16-30

"N"
31-45

"G"
46-60

"O"
61-75


Return an array with all numbers in the range from smallest to largest. """

def get_bingo_range(letter):
    letters=["B","I","N","G","O"]
    ind=letters.index(letter)
    return list(range(15*ind+1,15*(ind+1)+1))

""" 19-05-2026: Sleep Debt
Given an array of hours slept each night leading up to today, and a target number of hours per night, return how many hours of sleep you need tonight to eliminate your sleep debt.
• Include tonight's hours in the total time needed to catch up.
• If you've slept enough to cover tonight's target or more, return 0. """

def sleep_debt(hours_slept, target_hours):
    return max(0,target_hours+sum([target_hours - el for el in hours_slept ]))

""" 20-05-2026: String Zipper
Given two strings, return a new string that interleaves their characters one at a time. If one string is longer, append the remaining characters at the end.
Begin with the first character of the first string. """

def zip_strings(a, b):
    mini=min(len(a),len(b))
    s=list(zip(list(a),list(b)))
    res=""
    for i in range(len(s)):
        res+=s[i][0]+s[i][1]
    if len(a)>len(b):
        res+=a[mini:]
    if len(b)>len(a):
        res+=b[mini:]
    return res
    
""" 21-05-2026: I Before E
Given a word or sentence, return a corrected version where every word follows the "I before E except after C" rule.
• If a word contains "ei" not preceded by "c", replace it with "ie".
• If a word contains "ie" preceded by "c", replace it with "ei".
• All other words are left unchanged. """

def i_before_e(sentence):
    sp=sentence.split(" ")
    s=[[sp[i].find("c"),sp[i].find("ei"),sp[i].find("ie")] for i in range(len(sp))]
    for i in range(len(sp)):
        c1=s[i][0]==-1 or s[i][0]>s[i][1]
        if c1:
           sp[i]=sp[i].replace("ei","ie")
        c2=s[i][0]!=-1 and s[i][2]>0 and s[i][2]>s[i][0]
        if c2:
           sp[i]=sp[i].replace("ie","ei")
    return " ".join(sp) 

""" 22-05-2026: Meeting Time
Given a 3D array representing availability windows for multiple people, return the earliest time where everyone has one hour free. If no such time exists, return "None".
• Each person's availability is an array of [start, end] integer pairs in 24-hour time. For example, [10, 12] would mean the person is available from 10 to 12. Start times range from 0-23, and end times range from 1-24.
For example, given:
json
[
  [[10, 12], [15, 16]], // person 1
  [[11, 14], [15, 16]]  // person 2
]

Return 11, the start of their first shared free hour. """

def get_meeting_time(av):
    pre=[]
    for i in range(len(av)):
        hlp=[]
        for j in range(len(av[i])):
            rg=list(range(av[i][j][0],av[i][j][1]))
            hlp.append(rg)
        pre.append(hlp)
    c2=[]
    for i in range(len(pre)):
        c1=[]
        for j in range(len(pre[i])):
            c1+=pre[i][j]
        c2.append(c1)
    cands=[]
    for i in range(len(c2)):
        cands+=c2[i]
    cands=sorted(list(set(cands)))
    lst=[[] for i in range(len(cands))]
    for j in range(len(cands)):
        for i in range(len(c2)):
           lst[j].append(cands[j] in c2[i])
    for i in range(len(lst)):
        if sum(lst[i])==len(lst[i]):
            return cands[i]
    return "None"

""" 23-05-2026: Open Issues
Given an array of issue numbers and another array of pull request (PR) numbers, return an array of issues that remain open after all PRs have been merged.
• A PR closes an issue if their digits are a rotation of each other. For example, issue 123 would be closed by PR 231 or 312.
• A PR does not close an issue with the exact same number. For example, PR 123 does not close issue 123. So an issue with all the same number can't get closed.
• Either number may have leading zeros stripped. For example, PR 201 would close issue 12 (012, a rotation of 201). Similarily, issue 201 would be closed by PR 12.
Return the remaining open issues in the order they were given. """

def get_open_issues(issues, prs):
    hlp=[issues[i] for i in range(len(issues)) if issues[i] in prs]
    m1=[int("".join(sorted(list(str(issues[i]).replace("0",""))))) for i in range(len(issues)) ]
    m2=[int("".join(sorted(list(str(prs[i]).replace("0",""))))) for i in range(len(prs))]
    for i in range(len(m1)):
        if not m1[i] in m2:
            hlp.append(issues[i])
    ind=[]
    for i in range(len(hlp)):
        ind.append(issues.index(hlp[i]))
    ind=sorted(ind)
    return [issues[ind[i]] for i in range(len(ind))]

""" 24-05-2026: Roman Numeral Fixer
Given a string of malformed Roman numerals, return the value in standard Roman numeral notation.
The input will only use additive notation, so each symbol adds its value to the total. As a reminder, here are the symbols and values:

Symbol
Value

"I"
1

"V"
5

"X"
10

"L"
50

"C"
100

"D"
500

"M"
1000


When re-encoding, use the largest possible symbol at each step, using subtractive pairs ("IV", "IX", "XL", "XC", "CD", "CM") where needed. """

def convert_to_roman(num):
    nums=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    romans=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    res=""
    while num>0:
        for i in range(len(romans)):
            if num>=nums[i]:
                num-=nums[i]
                res+=romans[i]
                break
    return res

def fix_numerals(s):
    rObj={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    sn=0
    for i in range(len(s)):
        sn+=rObj[s[i]]
    return convert_to_roman(sn)

""" 25-05-2026: Secret Number
Given a secret number and a guess, determine if the guess is correct.
Return:
• "higher" if the secret number is higher than the guess.
• "lower" if the secret number is lower than the guess.
• "you got it!" if the guess is correct. """

def guess_number(secret, guess):
    if guess<secret:
        return "higher"
    elif guess>secret:
        return "lower"
    else:
        return "you got it!"
        
""" 26-05-2026: Sum of Differences
Given an array of numbers, return the sum of the differences between each number and the one that follows it.
For example, given [1, 3, 4], return 3 (2 + 1). """

def sum_of_differences(arr):
    sn=0
    for i in range(1,len(arr)):
        sn+=(arr[i]-arr[i-1])
    return sn

""" 27-05-2026: Pizza Party
Given an array of hours worked today per person, return the number of pizzas to order for a pizza party.
• Divide each person's hours worked by 3 to get their slice count.
• You can't eat a partial slice, so round each person's slice count up to the nearest whole number.
• Each person gets a minimum of two slices.
• Each pizza has 8 slices. Round the total number of pizzas up to the nearest whole pizza. """

import math
def get_pizzas_to_order(hours_worked):
    return math.ceil(sum([max(math.ceil(hours_worked[i]/3),2) for i in range(len(hours_worked))])/8)

""" 28-05-2026: FizzBuzz Count
Given a start and end number, count the number of fizz and buzz appearances in the range (inclusive).
• Numbers divisible by 3 count as a fizz.
• Numbers divisible by 5 count as a buzz.
• Numbers divisible by both 3 and 5 count as both a fizz and a buzz.
Return an object or dictionary with the counts in the format: { fizz, buzz }. """

from collections import Counter 
def fizz_buzz_count(start, end):
    lst=[]
    for i in range(start,end+1):
        if i%3==0:
            lst.append("fizz")
        if i%5==0:
            lst.append("buzz")
    return dict(Counter(lst))

""" 29-05-2026: Wider Aspect Ratio
Given two strings for different image dimensions, return the aspect ratio of the image with a greater width-to-height ratio.
• The given strings will be in the format "WxH", for example, "1920x1080".
• The aspect ratio is the ratio of width to height, reduced to the lowest whole numbers. For example, "1920x1080" reduces to "16:9".
• Return a string in format "W:H", for example, "16:9". """

import math
def get_wider_aspect_ratio(a, b):
    d11=int(a.split("x")[0])
    d12=int(a.split("x")[1])
    d21=int(b.split("x")[0])
    d22=int(b.split("x")[1])
    gcd1=math.gcd(d11,d12)
    gcd2=math.gcd(d21,d22)
    if d11/d12>d21/d22:
        return str(int(d11/gcd1))+":"+str(int(d12/gcd1))
    else:
        return str(int(d21/gcd2))+":"+str(int(d22/gcd2))

""" 30-05-2026: Best Hand
Given an array of five strings representing playing cards, return the name of the best hand.
• Each card is represented as a two-character string: the rank followed by the suit, "2h" for example.
◦ Ranks, from low to high, are: "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", and "A".
◦ Suits are: "h", "d", "c", and "s".
• Aces ("A") can be used as high or low in a straight.
The hands, in order from worst to best, are:

Name
Description

"High Card"
No pair or better

"Pair"
Two of one rank

"Two Pair"
Two of one rank and two of another

"Three of a Kind"
Three of one rank

"Straight"
Five ranks in a row

"Flush"
Five of the same suit

"Full House"
Three of one rank, and two of another

"Four of a Kind"
Four of one rank

"Straight Flush"
Five ranks in a row of the same suit

"Royal Flush"
"A", "K", "Q", "J", "T" of the same suit


Return the name of the best hand. """

from collections import Counter
def get_best_hand(cards):
    rDict={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13,"A":14}
    ranks=sorted([rDict[s[0]] for s in cards],reverse=True)
    suits=[s[1] for s in cards]
    rCount=dict(Counter(ranks))
    sCount=dict(Counter(suits))
    counts=sorted(rCount.values(),reverse=True)
    uniques=list(rCount.values())
    is_flush=5 in list(sCount.values())
    is_straight=False
    straight_high_card=ranks[0]
    if len(uniques)==5:
        if ranks[0]-ranks[4]==4:
            is_straight=True
        elif ranks[0] == 14 and ranks[1] == 5 and ranks[4] == 2:
            is_straight=True
            straight_high_card=5
    if is_flush and is_straight:
        if straight_high_card==14:
            return "Royal Flush"
        else:
            return "Straight Flush"
    if counts[0]==4:
        return "Four of a Kind"
    if counts[0]==3 and counts[1]==2:
        return "Full House"
    if is_flush:
        return "Flush"
    if is_straight:
        return "Straight"
    if counts[0]==3:
        return "Three of a Kind"
    if counts[0]==2 and counts[1]==2:
        return "Two Pair"
    if counts[0]==2:
        return "Pair"
    return "High Card"

""" 31-05-2026:Parentheses Combinations
Given an integer, n, return the number of valid combinations of n pairs of parentheses.
• A valid combination is a string where every opening parentheses has a corresponding closing parentheses, and no closing parentheses appears before its matching opening parentheses.
For example, given 2, there are 2 valid combinations:
json
(())
()()

def add_parentheses(n,openCount,curr,res):
    if len(curr)==2*n:
        res.append(curr)
        return
    if openCount < n:
        add_parentheses(n, openCount+1,curr+'(', res)
    if len(curr) - openCount < openCount:
        add_parentheses(n, openCount,curr+')', res)

def get_combinations(n):
    res=[]
    add_parentheses(n, 0, '', res)  
    return len(res)
