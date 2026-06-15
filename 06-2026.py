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
