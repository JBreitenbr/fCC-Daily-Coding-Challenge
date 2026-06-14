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

