""" 01-06-2026: Schema Validator Part 1
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
json
{
  username: string
}

• Extra keys are allowed """

def is_valid_schema(obj):
    k=list(obj.keys())
    if not "username" in k:
       return False
    ind=k.index("username")
    return isinstance(obj[k[ind]],str)

""" 02-06-2026: Schema Validator Part 2
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
json
{
  username: string,
  posts: number,
  verified: boolean
}

• Extra keys are allowed """

def is_valid_schema(obj):
    k=list(obj.keys())
    if not "username" in k or not "posts" in k or not "verified" in k:
        return False
    ind1=k.index("username")
    c1=isinstance(obj[k[ind1]],str)
    ind2=k.index("posts")
    c2=isinstance(obj[k[ind2]],int)
    ind3=k.index("verified")
    c3=isinstance (obj[k[ind3]], bool)
    return c1 and c2 and c3

""" 03-06-2026: Schema Validator Part 3
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
json
Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles
}

• The pipe (|) symbol means "or". role must be one of the listed Roles values.
• Extra keys are allowed """

def is_valid_schema(obj):
    roles=["user","creator","moderator","staff","admin"]
    k=list(obj.keys())
    if not "username" in k or not "posts" in k or not "verified" in k or not "role" in k:
        return False
    ind1=k.index("username")
    c1=isinstance(obj[k[ind1]],str)
    ind2=k.index("posts")
    c2=isinstance(obj[k[ind2]],int)
    ind3=k.index("verified")
    c3=isinstance (obj[k[ind3]], bool)
    return c1 and c2 and c3 an

""" 04-06-2026: Schema Validator Part 4
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
json
Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean
}

• The pipe (|) symbol means "or". role must be one of the listed Roles values.
• The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
• Extra keys are allowed """

def is_valid_schema(obj):
    roles=["user","creator","moderator","staff","admin"]
    k=list(obj.keys())
    if not "username" in k or not "posts" in k or not "verified" in k or not "role" in k:
        return False
    ind1=k.index("username")
    c1=isinstance(obj[k[ind1]],str)
    ind2=k.index("posts")
    c2=isinstance(obj[k[ind2]],int) and not isinstance(obj[k[ind2]],bool)
    ind3=k.index("verified")
    c3=isinstance (obj[k[ind3]], bool)
    if not "supporter" in k:
       return c1 and c2 and c3 and obj["role"] in roles
    else: 
       return c1 and c2 and c3 and obj["role"] in roles and isinstance(obj[k[k.index("supporter")]],bool)


""" 05-06-2026: Schema Validator Part 5
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
json
Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean,
  badges: string[]
}

• The pipe (|) symbol means "or". role must be one of the listed Roles values.
• The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
• The brackets [] after string means that badges should be an array of strings (or empty).
• Extra keys are allowed  """

def is_valid_schema(obj):
    roles=["user","creator","moderator","staff","admin"]
    k=list(obj.keys())
    if not "username" in k or not "posts" in k or not "verified" in k or not "role" in k or not "badges" in k:
        return False
    ind1=k.index("username")
    c1=isinstance(obj[k[ind1]],str)
    ind2=k.index("posts")
    c2=isinstance(obj[k[ind2]],int) and not isinstance(obj[k[ind2]],bool)
    ind3=k.index("verified")
    c3=isinstance(obj[k[ind3]], bool)
    if "supporter" in k:
        ind4=k.index("supporter")
        c4=isinstance(obj[k[ind4]],bool)
    for i in range(len(obj["badges"])):
        if not isinstance(obj["badges"][i],str):
            return False
    if "supporter" in k:
        return c1 and c2 and c3 and c4 and obj["role"] in roles
    else:
        return c1 and c2 and c3 and obj["role"] in roles          

""" 06-06-2026: Schema Validator Part 6
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
json
Roles = "user" | "creator" | "moderator" | "staff" | "admin"

UserProfile = {
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean,
  badges: string[]
}

{
  users: UserProfile[]
}

• The pipe (|) symbol means "or". role must be one of the listed Roles values.
• The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
• UserProfile[] denotes an array of UserProfile objects. An empty array is valid.
• Extra keys are allowed """

def check_obj(obj):
    roles=["user","creator","moderator","staff","admin"]
    k=list(obj.keys())
    if not "username" in k or not "posts" in k or not "verified" in k or not "role" in k or not "badges" in k:
         return False
    ind1=k.index("username")
    c1=isinstance(obj[k[ind1]],str)
    ind2=k.index("posts")
    c2=isinstance(obj[k[ind2]],int) and not isinstance(obj[k[ind2]],bool)
    ind3=k.index("verified")
    c3=isinstance(obj[k[ind3]], bool)
    if "supporter" in k:
        ind4=k.index("supporter")
        c4=isinstance(obj[k[ind4]],bool)
    for i in range(len(obj["badges"])):
        if not isinstance(obj["badges"][i],str):
            return False
    if "supporter" in k:
        return c1 and c2 and c3 and c4 and obj["role"] in roles
    else:
        return c1 and c2 and c3 and obj["role"] in roles

def is_valid_schema(obj):
    if not isinstance(obj["users"],list):
       return False
    elif obj["users"]==[]:
       return True
    else:
       for i in range(len(obj["users"])):
        if not check_obj(obj["users"][i]):
            return False
    return True

""" 07-06-2026: Last Load
Given the number of scoops of laundry detergent you have remaining and an array of how many scoops you used in each of the previous days, return the number of full days of detergent you have remaining.
Calculate your average daily usage from the usage history and assume that amount of usage each day going forward. """

import math
def last_load_date(scoops, usage):
    return math.floor(scoops/(sum(usage)/len(usage)))

""" 08-06-2026: Jet Lagged
Given a departure city, an arrival city, a flight duration in hours, and a direction of travel, return the number of jet lag hours the traveller is experiencing.
The given cities will be from the following list that includes their UTC offset:

City
Offset

"Los Angeles"
-8

"New York"
-5

"London"
0

"Istanbul"
+3

"Dubai"
+4

"Hong Kong"
+8

"Tokyo"
+9


To calculate jet lag hours:
1. Find the timezone difference in hours between the two cities.
2. Determine the direction multiplier. If travelling "east", it's 1.5, otherwise, it's 1.0.
3. Get the jet lag hours with the formula: timezone difference + (flight duration * 0.1) * direction multiplier
Return the jet lag hours rounded to one decimal place.  """

def get_jet_lag_hours(departure_city, arrival_city, flight_duration, direction):
   d={"Los Angeles":-8,
 "New York":-5,
 "London":0,"Istanbul":3,"Dubai":4,"Hong Kong":8,
 "Tokyo":9}
   tdiff=abs(d[departure_city]-d[arrival_city])
   if direction=="east":
      return tdiff+0.1*flight_duration*1.5
   else:
      return tdiff+0.1*flight_duration

""" 09-06-2026: Roommates
Given an array of people and their roommate group, return the room assignments for a hotel stay using the following rules:
• Each person has a name and a group property:
json
[
  { "name": "Alice", "group": "A" },
  { "name": "Bob", "group": "B" },
  { "name": "Carol", "group": "A" }
]

• People can only share a room with someone from the same group and are paired in the order they are given.
• Return an array of strings with names separated by " and " for a shared room, and just the name for a solo room. Names must appear in the order they were paired. For the example above, return ["Alice and Carol", "Bob"]. """

def flatten(arr):
    fl=[]
    for el in arr:
        if isinstance(el,list):
            fl.extend(flatten(el))
        else:
            fl.append(el)
    return fl

def rhlp(lst):
    res=[]
    for i in range(0,len(lst),2):
        sl=" and ".join(lst[i:i+2])
        res.append(sl)
    return res

def get_roommates(people):
    s=list(set([people[i]["group"] for i in range(len(people))]))
    d={}
    for i in range(len(s)):
        d[s[i]]=[]
    for i in range(len(people)):
        for j in range(len(s)):
            if people[i]["group"]==s[j]:
                d[s[j]].append(people[i]["name"])
    res=[]
    k=list(d.keys())
    for i in range(len(k)):
        res.append(rhlp(d[k[i]]))
    return flatten(res)

""" 10-06-2026: Itinerary Arrangements
Given an array of at least two optional stops for a day trip, return the number of valid itinerary arrangements.
The itinerary always includes "breakfast", "lunch", and "dinner", these will not be passed in as arguments. The optional stops can be placed anywhere in the itinerary, subject to the following rules:
• "breakfast" is always first, with at least one stop before "lunch".
• "lunch" must appear before "dinner", with at least one stop in between.
• At most, one optional stop may appear after "dinner".
Return the number of valid arrangements. """

from itertools import permutations 
def combs(arr):
    res=[]
    for p in permutations(arr):
        res.append(list(p))
    return res

def constr(arr):
    c1=arr[0]!="lunch" and arr[1]!="dinner"
    c2=arr.index("dinner")-arr.index("lunch")>=2
    c3=arr.index("dinner")>=len(arr)-2
    return c1 and c2 and c3

def get_itinerary_count(stops):
    stops.append("lunch")
    stops.append("dinner")
    lst=[el for el in combs(stops) if constr(el)]
    return len(lst)

""" 11-06-2026: Idea Rankings
Given a 2D array where each inner array contains (in this order) an idea name, an optimistic estimate, a realistic estimate, and a pessimistic estimate (in days), return an array of the idea names sorted by expected time to completion, shortest first.
Calculate the expected time to completion for each idea using the following formula:
• expected = ((optimistic + 4 * realistic + pessimistic) / 6) * length of idea name  """

def analyze_ideas(ideas):
    lst=[len(el[0])*(el[1]+4*el[2]+el[3])/6 for el in ideas]
    return [ideas[lst.index(el)][0] for el in sorted(lst)]
    
""" 12-06-2026: HTML Content Extractor
Given a string of HTML, return the plain text content with all tags removed. """

import re
def extract_content(html):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', html)

""" 13-06-2026: Zoning Regulations
Given a 2D grid (array of arrays) representing a city's building layout, return the coordinates of all buildings that are violating zoning rules.
Each cell in the grid contains one of the labels from the table below. A building is in violation if any of its (up to) 4 neighbors, horizontal or vertical, are a type it cannot be adjacent to.

Label
Type
Cannot be adjacent to

"i"
industrial
"R", "I"

"A"
Agricultural
"C"

"R"
Residential
"i", "C"

"I"
Institutional
"i"

"C"
Commercial
"R", "A"

"" (empty string)
undeveloped
no restrictions


Return the coordinates of all violating cells as an array of [row, col] pairs, in any order. If no violations exist, return an empty array. """

""" 14-06-2026: Credit Card Validator
Given a string of digits for a credit card number, determine if it's a valid card number using the following method:
• Starting from the second-to-last digit, double every other digit moving left.
• If doubling a digit results in a number greater than 9, subtract 9.
• Sum all the digits (doubled and undoubled).
• If the total is divisible by 10, the number is valid. """

def is_valid_card(number):
    pre=[]
    lst=list(number[::-1])
    for i in range(len(lst)):
        if i%2==1:
            pre.append(2*int(lst[i]))
        else:
            pre.append(int(lst[i]))
    res=[]
    for i in range(len(pre)):
        if pre[i]<=9:
            res.append(pre[i])
        else:
            res.append(pre[i]-9)
    return sum(res)%10==0
""" 15-06-2026: Number Sort
Given a string of numbers separated by commas, return an array of the numbers sorted from smallest to largest. """

def sort_numbers(s):
    return sorted([int(s.split(",")[i]) for i in range(len(s.split(",")))])

""" 16-06-2026: British to American
Given a sentence, convert any British English spellings to their American English equivalents using the following lookup table and return the updated sentence:

British
American

"colour"
"color"

"flavour"
"flavor"

"honour"
"honor"

"neighbour"
"neighbor"

"labour"
"labor"

"humour"
"humor"

"centre"
"center"

"fibre"
"fiber"

"defence"
"defense"

"offence"
"offense"

"organise"
"organize"

"recognise"
"recognize"

"analyse"
"analyze"


• Replacements should be case-insensitive. For example, "Colour" should become "Color".
• The input may contain words that build on the exact spelling of a root in the table that also need to be changed. For example, "colouring" should become "coloring", and "disorganised" should become "disorganized". """

def british_to_american(sentence):
     brit=["colour","flavour","honour","neighbour","labour","humour","centre","fibre","defence","offence","organise","recognise","analyse"]
     ami=["color","flavor","honor","neighbor","labor","humor","center","fiber","defense","offense","organize","recognize","analyze"]
     for i in range(len(brit)):
        sentence=sentence.replace(brit[i],ami[i])
     return sentence

""" 17-06-2026: Spellcaster
Given a string of spell codes you are casting, calculate the total score.
Each character in the string represents a spell:

Code
Spell
Category
Base Score

"f"
Fire
Destruction
3

"l"
Lightning
Destruction
3

"i"
Ice
Control
2

"w"
Wind
Control
2

"h"
Heal
Restoration
1

"s"
Shield
Restoration
1


A combo multiplier is applied based on how many spells in a row have been cast from different categories:
• The first spell always scores at base value.
• Each consecutive spell from a different category than the previous increases the multiplier by 1.
• Casting a spell from the same category as the previous resets the multiplier back to 1.
• The score for each spell is its base score multiplied by the current multiplier.
Return the total score from the sequence of spells. """

def cast(spells):
    c="fliwhs"
    s=["Fire","Lightning","Ice","Wind","Heal","Shield"]
    cat=["Destruction","Destruction","Control","Control","Restoration","Restoration"]
    b=[3,3,2,2,1,1]
    base=[b[c.index(spells[i])] for i in range(len(spells))]
    cats=[cat[c.index(spells[i])] for i in range(len(spells))]
    sn=base[0]
    m=1
    for i in range(1,len(spells)):
        if cats[i]!=cats[i-1]:
            m+=1
        else:
            m=1
        sn+=m*base[i]
    return sn

""" 18-06-2026: Streaming Cost
Given an array representing movies in the cart of your streaming service, and a string for your subscription tier, return the total cost of the movies.
Each item in the cart is an object with a "format" ("HD" or "4K") and a "type" ("rent" or "buy"). Their costs are:


"rent"
"buy"

"HD"
$3.99
$12.99

"4K"
$5.99
$19.99


Apply the following subscription tier discounts:
• "none": full price
• "basic": 10% off
• "premium": 25% off
Return the total cost rounded to two decimal places in the format "$D.CC"."""

def get_streaming_bill(cart, subscription):
    d={"HDrent":3.99,"HDbuy":12.99,"4Krent":5.99,"4Kbuy":19.99}
    sn=0
    for i in range(len(cart)):
        sn+=d["".join(list(cart[i].values()))]
    if subscription=="basic":
        sn=0.900001*sn
    if subscription=="premium":
        sn=0.749999*sn
    return "$"+str(round(sn,2))
  
""" 19-06-2026: Rental Cost
Given a rental timestamp, a return timestamp, and a rental tier, return the total cost of the rental including any late fees.
• Given timestamps are UTC ISO strings, for example: "2026-06-18T18:30:00Z".
• The rental tier is the number of days before the rental is due back: 1, 3, or 7.
• Rentals are due back by 12:00 PM UTC or earlier on the last day of the rental period. For example, a 1-day rental checked out at any time on March 15 is due back by 12:00 PM UTC on March 16.
• Each day past the due date and time incurs a late fee.
Pricing is as follows:

Tier
Base cost
Late fee per day

1 day
$4.99
$3.99

3 days
$3.99
$2.99

7 days
$2.99
$0.99


Return the total cost rounded to two decimal places in the format "$D.CC". """

from datetime import datetime
def get_rental_cost(rented, returned, tier):
    d={1:{"base":4.99,"late":3.99},3:{"base":3.99,"late":2.99},7:{"base":2.99,"late":0.99}}
    d1=datetime.strptime(rented[0:10], "%Y-%m-%d")
    d2=datetime.strptime(returned[0:10], "%Y-%m-%d")
    diff=(d2-d1).days
    m=int(returned[14:16])+int(returned[11:13])*60
    if m<=720:
        z=max(diff-tier,0)
    else:
        z=max(diff-tier+1,0)
    ges=d[tier]["base"]+z*d[tier]["late"]
    p=str(ges).split(".")
    return "$"+p[0]+"."+p[1][:2]
    
""" 20-06-2026: Prime Factorization
Given an integer greater than 1, return its prime factorization as an array of numbers in ascending order.
A prime factorization is the set of prime numbers that multiply together to produce the given integer. Each number has exactly one set. For example, the prime factorization of 20 is [2, 2, 5] because 2 * 2 * 5 = 20.
If the given integer is itself prime, return it in a single-element array. """

def is_prime(n):
    return True if len([i for i in range(2,n) if n % i == 0]) == 0 else False

def prime_factorization(n):
    pre=[]
    for i in range(2,n+1):
        if n%i==0 and is_prime(i):
            pre.append(i)
    res=[]
    for i in range(3):
        for j in range(len(pre)):
            if n%pre[j]==0:
                res.append(pre[j])
                n=n/pre[j]
    return sorted(res)
    
""" 21-06-2026: Summer Solstice
Today is the summer solstice, the longest day of the year in the Northern Hemisphere and the shortest in the Southern. Given a latitude, return a string representing daytime and nighttime hours.
• The latitude will be between 90 (north pole) and -90 (south pole), inclusive
• The number of daytime hours = 12 + (latitude / 90) * 12
• Round the daytime hours to the nearest even number
Return a 24-character string using "☀️" for daytime hours and "🌑" for nighttime hours, where:
• Each character represents one hour, starting at midnight (hour 0)
• Sunrise and sunset fall symmetrically around noon
For example, a latitude of 0 (the equator) has 12 hours of daylight, so sunrise is at 6:00 AM and sunset is at 6:00 PM. Return: "🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑". """

import math
def get_daytime_hours(lat):
    res=""
    pre=12+(lat/90)*12
    if math.floor(pre)%2==0:
        dt_hours=math.floor(pre)
    elif round(pre)%2==0:
        dt_hours=round(pre)
    else:
        dt_hours=round(pre)+1
    st=int((24-dt_hours)/2)
    if lat==90:
        return "☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️"
    else:
        for i in range(st):
            res+="🌑"
        for i in range(dt_hours):
            res+="☀️"
        for i in range(st):
            res+="🌑"
    return res

""" 22-06-2026: 1337 Speak
Given a lowercase string, return it translated into leet speak by replacing the letters below with their leet substitutions:

Letter
Leet

a
4

e
3

g
9

i
1

l
1

o
0

s
5

t
7


• Characters with no substitution are left unchanged. """

def make_leet(s):
    letter="aegilost"
    leet="43911057"
    lst=list(s)
    ind=[letter.find(lst[i]) for i in range(len(lst))]
    res=""
    for i in range(len(ind)):
        if ind[i]==-1:
            res+=lst[i]
        else:
            res+=leet[ind[i]]
    return res

""" 23-06-2026: BMI Calculator
Given a weight in pounds and a height in inches, return the BMI (Body Mass Index) rounded to one decimal place.
To get BMI: divide the weight by the height squared, then multiply the result by 703. """

def calculate_bmi(weight, height):
    return round(weight/(height*height)*703,1)

""" 24-06-2026: DNA Mutations
Given two DNA strands of equal length, return an array of indexes where the strands differ (mutations).
• DNA strands are strings made up of the characters "A", "T", "C", and "G"
• Return the indexes in ascending order
• If there are no mutations, return an empty array """

def detect_mutations(strand1, strand2):
    return [i for i in range(len(strand1)) if strand1[i]!=strand2[i]]

""" 25-06-2026: Frontmatter Parser
Given a string representing a frontmatter block, parse it and return an object (JavaScript) or dictionary (Python) with the keys and values.
Frontmatter is wrapped in --- delimiters and contains key: value pairs within them, one per line. For example:
md
---
title: My Post
draft: false
views: 100
---

Should return:
js
{
  title: "My Post",
  draft: false,
  views: 100
}

• Numbers, Booleans, and Strings should all be returned as their respective type.
• The given string will have new lines separated with the newline character ("\n"). The above example would be given as: "---\ntitle: My Post\ndraft: false\nviews: 100\n---".  """

import re
def parse_frontmatter(s):
    pre=s.split("\n")[1:-1]
    k=[pre[i].split(": ")[0]for i in range(len(pre))]
    v0=[pre[i].split(": ")[1] for i in range(len(pre))]
    v=[]
    for i in range(len(v0)):
        if v0[i].isnumeric():
            v.append(int(v0[i]))
        elif v0[i].replace(".","").isnumeric() and "." in v0[i] and len(v0[i].split("."))<3:
            v.append(float(v0[i]))
        elif v0[i]=="false":
            v.append(False)
        elif v0[i]=="true":
            v.append(True)
        else:
            v.append(v0[i])
    res={}
    for i in range(len(k)):
        res[k[i]]=v[i]
    return res

""" 26-06-2026: Blood Bank
Given an array of the inventory at a blood bank and an array of patient blood type requests, return a string in the format "X of Y patients served". Where X is the maximum number of patients that can receive blood from the bank's inventory, and Y is the total number of patients.
Each entry in both arrays is one of the following blood types: "AB", "A", "B", or "O".
Compatibility rules:
• "AB" can receive from any blood type.
• "A" can receive from "A" and "O".
• "B" can receive from "B" and "O".
• "O" can only receive from "O".
Duplicate entries in the given arrays represent quantity. """

from collections import Counter
def triage_blood(bank, patients):
    p={"O":["O"],"A":["A","O"],"B":["B","O"],"AB":["AB","A","B","O"]}
    sn=0
    d=dict(Counter(bank))
    for i in range(len(patients)):
        for j in range(len(p[patients[i]])):
            s=p[patients[i]][j]
            if s in d.keys() and d[p[patients[i]][j]]>0:
               d[p[patients[i]][j]]-=1
               sn+=1
               continue
    return f"{sn} of {len(patients)} patients served"

""" 27-06-2026: Periodic Spelling
Given a word, determine if it can be spelled using element symbols from the periodic table.
• Ignore casing when spelling a word. "neon" can be spelled with the symbols "Ne", "O", and "N".
Here's a full list of the element symbols:
json
["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"];

Return an array of the elements used to spell the word, in their original casing and in the order to spell the word. Or, an empty array if it can't be spelled. """

from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    lst=list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    return [list(el) for el in lst if len(el)>=2]

def indices(src,find):   
    res=[]
    l=len(find)
    for i in range(len(src)):
        if find==src[i:i+l]:
            res.append(i)
    return res

def make_wrd(lst):
    res=""
    for i in range(len(lst)):
        res+=lst[i][0]
    return res

from operator import itemgetter
def get_periodic_spelling(word):
    lst=["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"]
    lst2=[el.lower() for el in lst]
    hlp=[]
    for i in range(len(lst2)):
        c=indices(word,lst2[i])
        if len(c)>=1:
            hlp.append([lst2[i],c,i])
    hlp1=[[el[0],min(el[1]),el[2]] for el in hlp]
    hlp1 = sorted(hlp1, key=itemgetter(1))
    hlp2=[[el[0],max(el[1]),el[2]] for el in hlp]
    hlp2 = sorted(hlp2,key=itemgetter(1))
    flt1=[el for el in powerset(hlp1) if make_wrd(el)==word]
    flt2=[el for el in powerset(hlp2) if make_wrd(el)==word]
    print(flt1)
    if len(flt1)==0 and len(flt2)==0:
        return []
    elif len(flt1)==0:
        return [lst[el[2]] for el in flt2[0]]
    else:
        return [lst[el[2]] for el in flt1[0]]

""" 28-06-2026: Connect 3
Given a matrix of strings representing pieces on a game grid, determine if any player has three in a row.
• Each cell contains "R", "Y", or "" (empty string).
• Three in a row means three consecutive non-empty cells of the same type horizontally, vertically, or diagonally.
Return:
• A flat array with the winner and the coordinates of their three winning cells in the format: ["R", [0,2], [1,3], [2,4]]. Coordinates are returned top-to-bottom, then left-to-right.
• An empty array if there is no winner. """

""" 29-06-2026: Song Mood Finder
Given a genre string and a BPM number for a song, determine the mood using the following table:

Mood
Genre
BPM Range

"focus"
"classical"
60–109

"focus"
"electronic"
60–89

"happy"
"pop"
60–180

"happy"
"classical"
110–180

"happy"
"rock"
60–129

"happy"
"electronic"
90–134

"hype"
"rock"
130–180

"hype"
"electronic"
135–180


"""

""" 30-06-2026: Duplicate Character Count
Given two strings, return a count of characters from the second string that can be found in the first.
• Duplicate characters in the second string are counted separately. """
