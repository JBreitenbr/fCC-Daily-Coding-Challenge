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
