""" 01-07-2026: Lucky Number
Given a string of a person's first and last name, calculate their lucky number using the following rules:
• First and last names are separated by a space
• Find the vowel and consonant count for each name
• Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name
• Do the same for the two larger counts and the larger name
• Subtract the smaller value from the larger one to get their lucky number
If the final value is zero (0), return 13. """

def get_lucky_number(name):
    sp=name.split(" ")
    stri1="".join(["v" if sp[0][i].lower() in "aeiou" else "c" for i in range(len(sp[0]))])
    stri2="".join(["v" if sp[1][i].lower() in "aeiou" else "c" for i in range(len(sp[1]))])
    lst=[len(stri1.split("v"))-1,len(stri1.split("c"))-1,len(stri2.split("v"))-1,len(stri2.split("c"))-1]
    m1=min(lst[0],lst[2])*min(lst[1],lst[3])*min(len(sp[0]),len(sp[1]))
    m2=max(lst[0],lst[2])*max(lst[1],lst[3])*max(len(sp[0]),len(sp[1]))
    if m1==m2:
        return 13
    elif m2>m1:
        return m2-m1
    else:
        return m1-m2
      
""" 02-07-2026: Max Profit
Given an array of daily stock prices and a budget (in dollars), calculate the maximum profit you could make by buying and selling the stock over the given period.
• You may only sell after you buy.
• You may perform at most one buy and one sell transaction. Once you sell, you cannot buy again.
• You can only buy whole shares.
• Return the maximum possible profit as a string, rounded down to the nearest cent and formatted to two decimal places. """

import math
def get_max_profit(prices, budget):
    max_profit=0
    for i in range(len(prices)):
      for j in range(i,len(prices)):
            if prices[j]>prices[i]:
                  shares=math.floor(budget/prices[i])
                  profit=shares*(prices[j]-prices[i])
                  if profit>max_profit:
                        max_profit=profit
    res=str(round(max_profit,2))
    if "." in res:
      if res[::-1].find(".")==1:
            res+="0"
    else:
      res+=".00"
    return res

""" 03-07-2026: Database Migration
Given two database objects, return the second object with any missing properties from the first filled in.
• Fields that already exist in the record should not be overwritten. """

def migrate_record(schema, record):
    res=schema
    k=list(record.keys())
    for i in range(len(k)):
        res[k[i]]=record[k[i]]
    return res
    
""" 04-07-2026: Kaprekar's Routine
Given a 4-digit number, return the number of times you need to apply Kaprekar's routine until reaching 6174.
Kaprekar's routine works as follows:
• Arrange the digits in descending order to form the largest number
• Arrange the digits in ascending order to form the smallest number (pad with leading zeros if necessary)
• Subtract the smaller from the larger
• Repeat with the new number  """

def kaprekar(n):
    s=n
    for i in range(7):
        mini="".join(sorted(list(str(s))))
        maxi="".join(sorted(list(str(s)),reverse=True))
        s=int(maxi)-int(mini)
        if s==6174:
            return i+1
            
""" 05-07-2026: Bucket Fill
Given a 2D grid, a starting position ([row, col]), and a new value, replace the value at the starting position and all connected cells of the same value with the new value.
• Cells are connected if they are adjacent horizontally or vertically (not diagonally).
Return the updated grid. """

from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    lst=list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    return [list(el) for el in lst if len(el)>=2]

def is_subset_connected(subset_coords):
    subset_set = set(subset_coords)
    start_cell = next(iter(subset_set))
    queue = [start_cell]
    visited = {start_cell}
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for curr_row, curr_col in queue:
        for dr, dc in dirs:
            neighbor = (curr_row + dr, curr_col + dc)
            if neighbor in subset_set and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return len(subset_set)==len(visited)              
                 
def bucket_fill(grid, pos, new_value):
    ch=grid[pos[0]][pos[1]]
    hlp=[]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==ch:
                hlp.append([i,j])
    s=powerset(hlp)
    r=[[] for i in range(len(s))]
    for i in range(len(s)):
        for j in range(len(s[i])):
            el=(s[i][j][0],s[i][j][1])
            r[i].append(el)
    t=[]
    for i in range(len(r)):
        t.append(set(r[i]))
    m=[]
    for i in range(len(t)):
        if is_subset_connected(t[i]):
            m.append([i,len(t[i])])
    c=s[m[-1][0]]
    for i in range(len(c)):
        grid[c[i][0]][c[i][1]]=new_value
    return grid

""" 06-07-2026: lowercase words
Given a string, return only the words that are entirely lowercase, in their original order and with a space between each word. """

def get_lowercase_words(s):
    return " ".join([w for w in s.split(" ") if w.islower()])
    
""" 07-07-2026: Nearest Multiple
Given two integers, round the first to the nearest multiple of the second. """

import math
def round_to_nearest_multiple(num, multiple):
    lst=[i*multiple for i in range(1,math.ceil(num/multiple)+1) if i*multiple>=num-multiple]
    if abs(lst[0]-num)>abs(lst[1]-num):
        return lst[1]
    return lst[0]
    
""" 08-07-2026: Issue Triage
Given a number of milliseconds since the last post on an issue, and the last message posted on the issue, determine what you should do with the issue according to these rules:
• If the last message is less than 7 days ago, return "leave it"
• If the last message is 7 or more days ago and its content contains "bump" (case-insensitive), return "close it"
• Otherwise, return "bump it" """

def triage_issue(ms, message):
    t=ms/1000/3600/24
    if t<7:
        return "leave it"
    elif "bump" in message.lower():
        return "close it"
    return "bump it"
    
""" 09-07-2026: Issue Triage 2
Given an issue title and an array of current labels, return an updated array of labels based on the following rules:
If the issue doesn't have any labels, add:
• "bug"
• and "needs triage" if the title contains "error" or "bug"
• "enhancement" and "discussing" if the title contains "feature" or "add"
Otherwise, if the given labels contain:
• "needs triage" and the title contains "simple" or "easy", remove "needs triage" and add "good first issue"
• "discussing" and the title contains "planned" or "next", remove "discussing" and add "on the roadmap"
• Otherwise, if "needs triage" or "discussing" is present, remove it and add "help wanted"
If the title contains:
• "security", add a "critical" label """

def triage_issue(title, labels):
    if len(labels)==0:
        if "error" in title or "bug" in title:
            pre=["bug","needs triage"]
        elif "feature" in title or "add" in title:
            pre=["enhancement", "discussing"]
        else:
            pre=[]
    else:
        if "needs triage" in labels and "simple" in title or "easy" in title:
            pre=[labels[i].replace("needs triage","good first issue") for i in range(len(labels))]
        elif "discussing" in labels and "planned" in title or "next" in title:
            pre=[labels[i].replace("discussing","on the roadmap") for i in range(len(labels))]
        else:
            if "discussing" in labels or "needs triage" in labels:
               pre=[labels[i].replace("discussing", "help wanted").replace("needs triage","help wanted") for i in range(len(labels))]
    print(pre)
    if "security" in title:
        return pre+["critical"]
    else:
        return pre
        
""" 10-07-2026: Exact Change
Given an integer amount in cents, return the number of distinct ways to make exact change using pennies (1 cent), nickels (5 cents), dimes (10 cents), and quarters (25 cents). """

import math
def exact_change(amount):
    sn=0
    for m in range(math.ceil(amount/25)):
        for i in range(math.ceil(amount/10)):
            for j in range(math.ceil(amount/5)):
                for k in range(amount+1):
                    if 25*m+10*i+5*j+k==amount:
                        sn+=1
    return sn
    
""" 11-07-2026: Five Dice
Given an array of five dice with values 1-6, return the best possible hand.
Here are the hands ranked lowest to highest:

Hand
Description

"no pair"
No pair or better

"pair"
Two dice with the same value

"two pair"
Two different pairs

"three of a kind"
Three dice with the same value

"small straight"
Four consecutive values

"large straight"
Five consecutive values

"full house"
Three of a kind and a pair

"four of a kind"
Four dice with the same value

"five of a kind"
All five dice with the same value

"""

from collections import Counter
def five_dice(dice):
    d=dict(Counter(dice))
    k=d.keys()
    v=d.values()
    if 5 in v:
        return "five of a kind"
    elif 4 in v:
        return "four of a kind"
    elif 2 in v and 3 in v:
        return "full house"
    elif 3 in v and not 2 in v:
        return "three of a kind"
    elif list(v).count(2)==2:
        return "two pair"
    elif 2 in v and list(v).count(1)==3:
        return "pair"
    elif list(v).count(1)==5 and (not 1 in dice or not 6 in dice):
        return "large straight"
    elif list(v).count(1)==5 and (not 2 in dice or not 5 in dice):
        return "small straight"
    else:
        return "no pair"

""" 12-07-2026: Horoscope Match
Given two star sign strings, return their compatibility percentage.
The signs are arranged in a wheel of 12 positions in this order: "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces", wrapping back to "Aries" after "Pisces". Find the shortest distance between the two signs and return the compatibility:

Distance
Compatibility

0
"100%"

1
"40%"

2
"80%"

3
"30%"

4
"90%"

5
"20%"

6
"50%"

"""

def horoscope_match(sign1, sign2):
    signs=["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    dist=[100,40,80,30,90,20,50]
    d1=abs(signs.index(sign1)-signs.index(sign2));
    if d1<=6:
        d2=d1
    else:
        d2=12-d1
    return str(dist[d2])+"%"
    
""" 13-07-2026: Tally Counter
Given a string of tally marks, return the total count represented.
• Each pipe "|" represents one count.
• Every fifth mark is represented as a forward slash "/", completing a group of five ("||||/").
• Groups are separated by a space. """

def get_tally_count(s):
    sp1=s.split("/")
    sp2=sp1[-1].split("|")
    return 5*(len(sp1)-1)+(len(sp2)-1)

""" 14-07-2026: Pet Age Calculator
Given a pet type and age in human years, return the equivalent age in pet years using the following conversion table:

Pet
Multiplier

"dog"
7

"cat"
6

"rabbit"
8

"hamster"
30

"guinea pig"
12

"goldfish"
6

"bird"
5

"""

def pet_years(pet, age):
    pets=["dog","cat","rabbit","hamster","guinea pig","goldfish","bird"]
    m=[7,6,8,30,12,6,5]
    return m[pets.index(pet)]*age
    
""" 15-07-2026: Array Chunks
Given an array and a chunk size, return the array split into sub-arrays of that size.
The last chunk may be smaller if the array doesn't divide evenly. """

def chunk_array(arr, size):
    res=[]
    for i in range(0,len(arr),size):
        res.append(arr[i:i+size])
    return res

""" 16-07-2026: Pig Latin Converter
Given a string, convert it to Pig Latin using the following rules:
• If a word begins with a vowel ("a", "e", "i", "o", or "u"), add "way" to the end. For example, "universe" converts to "universeway".
• If a word begins with one or more consonants, move them to the end and add "ay". For example, "hello" converts to "ellohay".
• Preserve the case of the first letter. For example, "Hello" converts to "Ellohay". """

import re
def little_pig(s):
    ind=s.find(re.findall("[aeiou]",s)[0])
    if ind==0:
        pre=s+"way"
    else:
        pre=s[ind:]+s[0:ind]+"ay"
    if s[0].islower():
        return pre.lower()
    else:
        return pre[0].upper()+pre[1:].lower()

def pig_latin(s):
    return " ".join([little_pig(el) for el in s.split(" ")])

""" 17-07-2026: Birthday Countdown
Given today's date and a birthday, return the number of days until the person's next birthday.
• Today's date is given as a string in "YYYY-MM-DD" format, with leading zeros, for example: "2026-07-16".
• The birthday is given as a string in "M/D" format, without leading zeros, for example: "9/7".
• If today is their birthday, return the number of days until their next birthday (not 0).
• Leap years should be accounted for. """

from datetime import datetime

def is_leap_year(year):
    return year%400==0 or year%100!=0 and year%4==0

def days_until_birthday(today, birthday):
    _year=int(today[0:4])
    m1=int(today[5:7])
    d1=int(today[8:10])
    m2=int(birthday.split("/")[0])
    d2=int(birthday.split("/")[1])
    nxt=[el for el in list(range(_year,_year+9)) if is_leap_year(el)]
    if birthday=="2/29":
        if m1<=2:
            if is_leap_year(_year):
                year=_year
            else:
                year=nxt[0]
        else:
            if is_leap_year(_year+1):
                year=_year+1
            else:
                year=nxt[1]
    else:
        if m1<m2 or m1==m2 and d1<d2:
            year=_year
        else:
            year=_year+1
    if m2<10:
        month="0"+str(m2)
    else:
        month=str(m2)
    if d2<10:
        day="0"+str(d2)
    else:
        day=str(d2)
    bd=str(year)+"-"+month+"-"+day
    ts1=int(datetime.strptime(today, "%Y-%m-%d").timestamp())
    ts2=int(datetime.strptime(bd,"%Y-%m-%d").timestamp())
    diff=(ts2-ts1)/3600/24
    return int(diff)

""" 18-07-2026: Dice Odds
Given a number of six-sided dice to roll and a target sum, return the odds of rolling that sum as a string in the format "1 in X".
• The number of dice will be between 1 and 6.
• The target sum is always achievable with the given number of dice.
• Round "X" to the nearest whole number. """

def enh(lst):
    res=[]
    for i in range(1,7):
        res.append(lst+[i])
    return res
    
def add_dim(lst):
    pre=[]
    for i in range(len(lst)):
        pre.append(enh(lst[i]))
    res=[]
    for i in range(len(pre)):
        for j in range(6):
            res.append(pre[i][j])
    return res

import math
def get_odds(dice, target):
    s=[[1],[2],[3],[4],[5],[6]]
    if dice==1:
        return "1 in 6"
    n=dice-1
    while n>0:
        s=add_dim(s)
        n-=1
    m=len([el for el in s if sum(el)==target])
    p=math.pow(6,dice)
    fr=m/p
    res=[]
    hlp=[]
    for i in range(min(int(p)+2,7778)):
        res.append(i)
        hlp.append(abs(fr*i-1))
        if i*fr==1:
            break
    mini=min(hlp)
    if 0.0 in hlp:
        return f"1 in {res[-1]}"
    else:
        return f"1 in {hlp.index(mini)}"

""" 19-07-2026: Elevator Stops
Given a number for the current floor of an elevator and an array of requested floors, return an array of the order the elevator should visit them to minimize number of floors traveled.
• If tied, go up first
• Floors with a request must be visited when the elevator first passes them  """

def min_dist(curr,lst):
    mini=min([abs(curr-lst[i]) for i in range(len(lst))])
    return sorted([lst[i] for i in range(len(lst)) if abs(curr-lst[i])==mini])[0]

def elevator_stops(current_floor, stops):
    res=[]
    l=len(stops)
    while l>0:
       s=min_dist(current_floor,stops)
       res.append(s)
       stops.remove(s)
       current_floor=s
       l-=1
    return res

""" 20-07-2026: Golden Ratio
Given two numbers, determine if their ratio approximates the golden ratio.
• Use a golden ratio of 1.618
• Allow a tolerance of 0.01 """

def is_golden_ratio(a, b):
    return abs(max(a,b)/min(a,b)-1.618)<0.01

""" 21-07-2026: Blender
Given two words, return a new word by combining the first half of the first word with the second half of the second word.
• For odd-length words, the first half is the shorter half. """

import math
def blend_words(word1, word2):
    p1=word1[0:math.floor(len(word1)/2)]
    p2=word2[math.floor(len(word2)/2):]
    return p1+p2
    
""" 22-07-2026: Piggy Bank
Given an object representing a piggy bank, return the total value as a string formatted as "$D.CC".
The object may contain any of the following:

Coin
Value

pennies
$0.01

nickels
$0.05

dimes
$0.10

quarters
$0.25


"""

""" 23-07-2026: Game Theory
Given two equal length strings representing two players' strategies for a game, return the scores as an array [player1, player2].
• The given strings will only contain one of two letters: "C" (cooperate) or "D" (defect).
• Each character represents one round, scored as follows:
◦ If both players cooperate, each scores 3.
◦ If both players defect, each scores 1.
◦ If one player defects and the other cooperates, the defector scores 5 and the cooperator scores 0. """

