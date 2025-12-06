""" 01-10-2025: Binary to Decimal
Given a string representing a binary number, return its decimal equivalent as a number.

A binary number uses only the digits 0 and 1 to represent any number. To convert binary to decimal, multiply each digit by a power of 2 and add them together. Start by multiplying the rightmost digit by 2^0, the next digit to the left by 2^1, and so on. Once all digits have been multiplied by a power of 2, add the result together.

For example, the binary number 101 equals 5 in decimal because:

1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 4 + 0 + 1 = 5
"""
import math
def to_decimal(binary):
    dec=0
    s=list(reversed(binary))
    for i in range(len(s)):
        dec+=int(s[i])*math.pow(2,i)
    return dec

""" 02-10-2025: Decimal to Binary
Given a non-negative integer, return its binary representation as a string.
"""
def to_binary(decimal):
    return str(bin(decimal))[2:]

""" 03-10-2025: P@ssw0rd Str3ngth!
Given a password string, return "weak", "medium", or "strong" based on the strength of the password.

A password is evaluated according to the following rules:

It is at least 8 characters long.
It contains both uppercase and lowercase letters.
It contains at least one number.
It contains at least one special character from this set: !, @, #, $, %, ^, &, or *.
Return "weak" if the password meets fewer than two of the rules. Return "medium" if the password meets 2 or 3 of the rules. Return "strong" if the password meets all 4 rules.
"""

def check_strength(password):
    pw=list(password)
    sp=["!","@","#","$","%","^","&","*"]
    u=len([val for val in pw if val.isupper()])
    l=len([val for val in pw if val.islower()])
    n=len([val for val in pw if val.isnumeric()])
    s=len([val for val in pw if val in sp])
    c1=len(pw)>=8
    c2=u>=1 and l>=1
    c3=n>=1
    c4=s>=1
    arr=[c1,c2,c3,c4]
    f=len([val for val in arr if val==True])
    if f<2:
        return "weak"
    elif f<4:
        return "medium"
    else:
        return "strong"

""" 04-10-2025: Space Week Day 1: Stellar Classification
October 4th marks the beginning of World Space Week. The next seven days will bring you astronomy-themed coding challenges.

For today's challenge, you are given the surface temperature of a star in Kelvin (K) and need to determine its stellar classification based on the following ranges:

"O": 30,000 K or higher

"B": 10,000 K - 29,999 K

"A": 7,500 K - 9,999 K

"F": 6,000 K - 7,499 K

"G": 5,200 K - 5,999 K

"K": 3,700 K - 5,199 K

"M": 0 K - 3,699 K

Return the classification of the given star.
"""

def classification(temp):
    if temp>=30000:
        return "O"
    elif temp>=10000:
        return "B"
    elif temp>=7500:
        return "A"
    elif temp>=6000:
        return "F"
    elif temp>=5200:
        return "G"
    elif temp>=3700:
        return "K"
    else:
        return "M"

""" 05-10-2025: Space Week Day 2: Exoplanet Search
For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star. Determine if the readings have detected an exoplanet using the transit method. The transit method is when a planet passes in front of a star, reducing its observed luminosity.

Luminosity readings only comprise of characters 0-9 and A-Z where each reading corresponds to the following numerical values:
Characters 0-9 correspond to luminosity levels 0-9.
Characters A-Z correspond to luminosity levels 10-35.
A star is considered to have an exoplanet if any single reading is less than or equal to 80% of the average of all readings. For example, if the average luminosity of a star is 10, it would be considered to have a exoplanet if any single reading is 8 or less.
"""

def has_exoplanet(readings):
    lst=list(readings)
    avg=0
    for i in range(len(lst)):
        avg+=int(lst[i],36)
    avg=avg/len(lst)
    for i in range(len(lst)):
        if int(lst[i],36)<=0.8*avg:
            return True
    return False

""" 06-10-2025: Space Week Day 3: Phone Home
For day three of Space Week, you are given an array of numbers representing distances (in kilometers) between yourself, satellites, and your home planet in a communication route. Determine how long it will take a message sent through the route to reach its destination planet using the following constraints:

The first value in the array is the distance from your location to the first satellite.
Each subsequent value, except for the last, is the distance to the next satellite.
The last value in the array is the distance from the previous satellite to your home planet.
The message travels at 300,000 km/s.
Each satellite the message passes through adds a 0.5 second transmission delay.
Return a number rounded to 4 decimal places, with trailing zeros removed.
"""

from functools import reduce
def send_message(route):
    res=(len(route)-1)*0.5
    s = reduce(lambda x, y: (x + y), route)/300000
    return round(res+s,4)

""" 07-10-2025: Space Week Day 4: Landing Spot
In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover. Find the safest landing spot based on the following rules:

Each spot in the matrix will contain a number from 0-9, inclusive.
Any 0 represents a potential landing spot.
Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.
The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
Return the indices of the safest landing spot. There will always only be one safest spot.
For instance, given:

[
  [1, 0],
  [2, 0]
]
Return [0, 1], the indices for the 0 in the first array.
"""

def find_landing_spot(matrix):
    m=matrix
    l=len(m)
    p=[]
    for i in range(l):
        for j in range(l):
            if m[i][j]==0:
                p.append([i,j])
    for k in range(len(p)):
        sm=0
        if p[k][0]>0:
            sm+=m[p[k][0]-1][p[k][1]]
        if p[k][0]<l-1:
            sm+=m[p[k][0]+1][p[k][1]]
        if p[k][1]>0:
            sm+=m[p[k][0]][p[k][1]-1]
        if p[k][1]<l-1:
            sm+=m[p[k][0]][p[k][1]+1]
        p[k].append(sm)
    q = sorted(p, key=lambda x: x[2])
    return [q[0][0],q[0][1]]

""" 08-10-2025: Space Week Day 5: Goldilocks Zone
For the fifth day of Space Week, you will calculate the "Goldilocks zone" of a star - the region around a star where conditions are "just right" for liquid water to exist.

Given the mass of a star, return an array with the start and end distances of its Goldilocks Zone in Astronomical Units.

To calculate the Goldilocks Zone:

Find the luminosity of the star by raising its mass to the power of 3.5.
The start of the zone is 0.95 times the square root of its luminosity.
The end of the zone is 1.37 times the square root of its luminosity.
Return the distances rounded to two decimal places.
For example, given 1 as a mass, return [0.95, 1.37].
"""

import math
def goldilocks_zone(mass):
    lum=math.pow(mass,3.5)
    low=math.sqrt(lum)*0.95
    high=math.sqrt(lum)*1.37
    return [round(low,2),round(high,2)]

""" 09-10-2025: Space Week Day 6: Moon Phase
For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and need to determine the phase of the moon for that day using the following rules:

Use a simplified lunar cycle of 28 days, divided into four equal phases:

"New": days 1 - 7
"Waxing": days 8 - 14
"Full": days 15 - 21
"Waning": days 22 - 28
After day 28, the cycle repeats with day 1, a new moon.

Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
You will not be given any dates before the reference date.
Return the correct phase as a string.
"""

from datetime import datetime
def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def moon_phase(date_string):
    diff=days_between("2000-01-06",date_string);
    s=(diff+1)%28
    if s<8:
        return "New"
    elif s<15:
        return "Waxing"
    elif s<22:
        return "Full"
    else:
        return "Waning"

""" 10-10-2025: Space Week Day 7: Launch Fuel
For the final day of Space Week, you will be given the mass in kilograms (kg) of a payload you want to send to orbit. Determine the amount of fuel needed to send your payload to orbit using the following rules:

Rockets require 1 kg of fuel per 5 kg of mass they must lift.
Fuel itself has mass. So when you add fuel, the mass to lift goes up, which requires more fuel, which increases the mass, and so on.
To calculate the total fuel needed: start with the payload mass, calculate the fuel needed for that, add that fuel to the total mass, and calculate again. Repeat this process until the additional fuel required is less than 1 kg, then stop.
Ignore the mass of the rocket itself. Only compute fuel needed to lift the payload and its own fuel.
For example, given a payload mass of 50 kg, you would need 10 kg of fuel to lift it (payload / 5), which increases the total mass to 60 kg, which needs 12 kg to lift (2 additional kg), which increases the total mass to 62 kg, which needs 12.4 kg to lift - 0.4 additional kg - which is less 1 additional kg, so we stop here. The total mass to lift is 62.4 kg, 50 of which is the initial payload and 12.4 of fuel.

Return the amount of fuel needed rounded to one decimal place.
"""

def launch_fuel(payload):
    pl=[payload]
    fuel=[pl[0]/5]
    pl.append(fuel[0]+pl[0])
    fuel.append(pl[1]/5)
    for i in range(1,5):
        pl.append(fuel[i]+pl[0])
        fuel.append(pl[i+1]/5)
    for i in range(len(fuel)):
          if fuel[i+1]-fuel[i]<1: 
             return round(fuel[i+1],1)
    return payload

""" 11-10-2025: Hex to Decimal
Given a string representing a hexadecimal number (base 16), return its decimal (base 10) value as an integer.

Hexadecimal is a number system that uses 16 digits:

0-9 represent values 0 through 9.
A-F represent values 10 through 15.
Here's a partial conversion table:

Hexadecimal	Decimal
0	0
1	1
...	...
9	9
A	10
...	...
F	15
10	16
...	...
9F	159
A0	160
...	...
FF	255
100	256
The string will only contain characters 0–9 and A–F.
"""

def hex_to_decimal(hex):
    return int(hex,16)

""" 12-10-2025: Battle of Words
Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:

The given sentences will always contain the same number of words.
Words are separated by a single space and will only contain letters.
The value of each word is the sum of its letters.
Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is 26.
A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
A word wins if its value is greater than the opposing word's value.
The team with more winning words is the winner.
Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if both teams have the same number of wins.
"""

def valued(word):
    a1=list("abcdefghijklmnopqrstuvwxyz")
    n1=list(range(1,27))
    d1=dict(zip(a1,n1))
    a2=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    n2=list(range(2,54,2))
    d2=dict(zip(a2,n2))
    sn=0
    for i in range(len(word)):
        if word[i].islower():
            sn+=d1[word[i]]
        if word[i].isupper():
            sn+=d2[word[i]]
    return sn

def battle(our_team,opponent):
    sp1=our_team.split(" ")
    sp2=opponent.split(" ")
    s1=0
    s2=0
    for i in range(len(sp1)):
        if valued(sp1[i])>valued(sp2[i]):
            s1+=1
        if valued(sp2[i])>valued(sp1[i]):
            s2+=1
    if s1>s2:
        return "We win"
    elif s2>s1:
        return "We lose"  
    else:
        return "Draw"

""" 13-10-2025: 24 to 12
Given a string representing a time of the day in the 24-hour format of "HHMM", return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".

The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".
"""

def to_12(time):
    p1=time[0:2]
    p2=time[2:4]
    if int(p1)>12:
        t1=str(int(p1)%12)
    if p1=="00":
        t1="12"
    if int(p1)<10 and p1!="00":
        t1=p1[1:2]
    if 10<=int(p1)<=12:
        t1=p1
    if int(p1)<=12 or p1=="00":
        d="AM"
    else:
        d="PM"
    return t1+":"+p2+" "+d

""" 14-10-2025: String Count
Given two strings, determine how many times the second string appears in the first.

The pattern string can overlap in the first string. For example, "aaa" contains "aa" twice. The first two a's and the second two.
"""

def count(text, parameter):
    l=len(parameter)
    sn=0
    for i in range(len(text)-l+1):
      if text[i:i+l]==parameter:
         sn+=1
    return sn

""" 15-10-2025: HTML Tag Stripper
Given a string of HTML code, remove the tags and return the plain text content.

The input string will contain only valid HTML.
HTML tags may be nested.
Remove the tags and any attributes.
For example, '<a href="#">Click here</a>' should return "Click here".
"""

import re
def strip_tags(html):
    return re.sub('<[^<]+?>', '', html)

""" 16-10-2025: Email Validator
Given a string, determine if it is a valid email address using the following constraints:

It must contain exactly one @ symbol.
The local part (before the @):
Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
Cannot start or end with a dot.
The domain part (after the @):
Must contain at least one dot.
Must end with a dot followed by at least two letters.
Neither the local or domain part can have two dots in a row.
"""

import re
def validate(email):
    sp=email.split("@")
    if len(sp)!=2:
        return False
    if len(sp)==2:
        en=sp[1]
        if ".." in en:
            return False
        sp2=en.split(".")
        if not sp2[-1].isalpha():
            return False
    p=sp[0]
    if p[0]=="." or p[-1]=="." or ".." in p:
        return False
    return True

""" 17-10-2025: Credit Card Masker
Given a string of credit card numbers, return a masked version of it using the following constraints:

The string will contain four sets of four digits (0-9), with all sets being separated by a single space, or a single hyphen (-).
Replace all numbers, except the last four, with an asterisk (*).
Leave the remaining characters unchanged.
For example, given "4012-8888-8888-1881" return "****-****-****-1881".
"""

def mask(card):
    ind=card.find("-")
    if ind==-1:
      mk="**** **** **** "
    else:
      mk="****-****-****-"
    return mk+card[-4:]
      
""" 18-10-2025: Missing Socks
Given an integer representing the number of pairs of socks you started with, and another integer representing how many wash cycles you have gone through, return the number of complete pairs of socks you currently have using the following constraints:

Every 2 wash cycles, you lose a single sock.
Every 3 wash cycles, you find a single missing sock.
Every 5 wash cycles, a single sock is worn out and must be thrown away.
Every 10 wash cycles, you buy a pair of socks.
You can never have less than zero total socks.
Rules can overlap. For example, on wash cycle 10, you will lose a single sock, throw away a single sock, and buy a new pair of socks.
Return the number of complete pairs of socks.
"""

import math
def sock_pairs(pairs, cycles):
    s=pairs*2;
    s=s-math.floor(cycles/2)
    s=s+math.floor(cycles/3)
    s=s-math.floor(cycles/5)
    s=s+math.floor(cycles/10)*2
    if s<0:
      return 0;
    elif s%2==0:
      return s/2
    else:
      return math.floor(s/2)

""" 19-10-2025: HTML Attribute Extractor
Given a string of a valid HTML element, return the attributes of the element using the following criteria:

You will only be given one element.
Attributes will be in the format: attribute="value".
Return an array of strings with each attribute property and value, separated by a comma, in this format: ["attribute1, value1", "attribute2, value2"].
Return attributes in the order they are given.
If no attributes are found, return an empty array.
"""

import re
def extract_attributes(el):
    s=re.findall('[\w-]+=".+?"',el)
    if not s:
        return []
    res=[]
    for i in range(len(s)):
        w=s[i].split("=")
        stri=w[0]+", "+w[1]
        stri=stri.replace('"','')
        res.append(stri)
    return res

""" 20-10-2025: Tip Calculator
Given the price of your meal and a custom tip percent, return an array with three tip values; 15%, 20%, and the custom amount.

Prices will be given in the format: "$N.NN".
Custom tip percents will be given in this format: "25%".
Return amounts in the same "$N.NN" format, rounded to two decimal places.
For example, given a "$10.00" meal price, and a "25%" custom tip value, return ["$1.50", "$2.00", "$2.50"].
"""

def m_formatter(stri):
    s=stri.split(".")
    if len(s)==1:
        return "$"+stri+".00"
    elif len(s[1])==1:
        return "$"+stri+"0"
    else:
        return "$"+stri
        
def calculate_tips(meal_price, custom_tip):
    mp=float(meal_price[1:])
    cp=float(custom_tip[::-1][1:][::-1])/100
    m1=m_formatter(str(round(0.15*mp,2)))
    m2=m_formatter(str(round(0.2*mp,2)))
    m3=m_formatter(str(round(cp*mp,2)))
    return [m1,m2,m3]

""" 21-10-2025: Thermostat Adjuster 2
Given the current temperature of a room in Fahrenheit and a target temperature in Celsius, return a string indicating how to adjust the room temperature based on these constraints:

Return "Heat: X degrees Fahrenheit" if the current temperature is below the target. With X being the number of degrees in Fahrenheit to heat the room to reach the target, rounded to 1 decimal place.
Return "Cool: X degrees Fahrenheit" if the current temperature is above the target. With X being the number of degrees in Fahrenheit to cool the room to reach the target, rounded to 1 decimal place.
Return "Hold" if the current temperature is equal to the target.
To convert Celsius to Fahrenheit, multiply the Celsius temperature by 1.8 and add 32 to the result (F = (C * 1.8) + 32)."""

def adjust_thermostat(curr_f, targ_c):
    targ_f=targ_c*1.8+32
    diff=str(round(targ_f-curr_f,1))
    if float(diff)>0:
        return f"Heat: {diff} degrees Fahrenheit"
    elif float(diff)<0:
        return f"Cool: {diff[1:]} degrees Fahrenheit"
    else:
        return "Hold"

""" 22-10-2025: Speak Wisely, You Must
Given a sentence, return a version of it that sounds like advice from a wise teacher using the following rules:

Words are separated by a single space.
Find the first occurrence of one of the following words in the sentence: "have", "must", "are", "will", "can".
Move all words before and including that word to the end of the sentence and:
Preserve the order of the words when you move them.
Make them all lowercase.
And add a comma and space before them.
Capitalize the first letter of the new first word of the sentence.
All given sentences will end with a single punctuation mark. Keep the original punctuation of the sentence and move it to the end of the new sentence.
Return the new sentence, make sure there's a single space between each word and no spaces at the beginning or end of the sentence.
For example, given "You must speak wisely." return "Speak wisely, you must."
"""

def wise_speak(sentence):
    v=["have", "must", "are", "will", "can"]
    s=sentence.lower().split(" ")
    for i in range(len(s)):
        if s[i] in v:
            ind=i
    fst=""
    lst=""
    for i in range(ind+1):
        lst+=s[i]+" "
    for i in range(ind+1,len(s)):
        fst+=s[i]+" "
    fst=fst[0].upper()+fst[1:].replace(".",",").replace("!",",").replace("?",",")
    rev=fst+lst[0:-1]+sentence[-1]
    return rev

""" 23-10-2025: Favorite Songs
Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.

Given an array of song objects representing your iPod playlist, return an array with the titles of the two most played songs, with the most played song first.

Each object will have a "title" property (string), and a "plays" property (integer)."""

def favorite_songs(playlist):
    s=sorted(playlist, key=lambda songs: songs["plays"],reverse=True)
    lst=[val["title"] for val in s]
    return lst[0:2]

""" 24-10-2025: Hidden Treasure
Given a 2D array representing a map of the ocean floor that includes a hidden treasure, and an array with the coordinates ([row, column]) for the next dive of your treasure search, return "Empty", "Found", or "Recovered" using the following rules:

The given 2D array will contain exactly one unrecovered treasure, which will occupy multiple cells.

Each cell in the 2D array will contain one of the following values:

"-": No treasure.
"O": A part of the treasure that has not been found.
"X": A part of the treasure that has already been found.
If the dive location has no treasure, return "Empty".

If the dive location finds treasure, but at least one other part of the treasure remains unfound, return "Found".

If the dive location finds the last unfound part of the treasure, return "Recovered".

For example, given:

[
  [ "-", "X"],
  [ "-", "X"],
  [ "-", "O"]
]
And [2, 1] for the coordinates of the dive location, return "Recovered" because the dive found the last unfound part of the treasure."""

def srArr(arr):
    narr =[]
    for i in range(len(arr)):
        if type(arr[i]) is list:
            narr += srArr(arr[i])
        else:
            narr.append(arr[i])
    return narr

def dive(map, coords):
    m="".join(srArr(map)).split("O") 
    p=map[coords[0]][coords[1]]
    if p=="-":
        return "Empty"
    elif p=="X" or len(m)>2:
        return "Found"
    else:
        return "Recovered"

""" 25-10-2025 Complementary DNA
Given a string representing a DNA sequence, return its complementary strand using the following rules:

DNA consists of the letters "A", "C", "G", and "T".
The letters "A" and "T" complement each other.
The letters "C" and "G" complement each other.
For example, given "ACGT", return "TGCA".
"""

def complementary_dna(strand):
    d={"A":"T","C":"G","G":"C","T":"A"}
    res=""
    for i in list(strand):
        res+=d[i]
    return res

""" 26-10-2025: Duration Formatter
Given an integer number of seconds, return a string representing the same duration in the format "H:MM:SS", where "H" is the number of hours, "MM" is the number of minutes, and "SS" is the number of seconds. Return the time using the following rules:

Seconds: Should always be two digits.
Minutes: Should omit leading zeros when they aren't needed. Use "0" if the duration is less than one minute.
Hours: Should be included only if they're greater than zero. """

import math
def format(secs):
    mini=math.floor(secs/60)%60
    hrs=math.floor(secs/3600)
    sec=secs-60*mini-3600*hrs;
    if sec<10:
        _sec="0"+str(sec)
    else:
        _sec=str(sec)
    dt=""
    if hrs==0 and mini==0:
        dt+="0:"+_sec
    elif hrs==0:
        dt+=str(mini)+":"+_sec
    else:
        if mini<10:
            dt+=str(hrs)+":0"+str(mini)+":"+_sec
        else:
            dt+=str(hrs)+":"+str(mini)+":"+_sec
    return dt

""" 27-10-2025: Integer Sequence
Given a positive integer, return a string with all of the integers from 1 up to, and including, the given number, in numerical order.

For example, given 5, return "12345".
"""

def sequence(n):
    r=list(range(1,n+1))
    res=""
    for val in r:
        res+=str(val)
    return res
function sequence(n) {
  let stri=Array.from(Array(n).keys()).map((item)=>item+1).join("");
  return stri;
}

""" 28-10-2025: Navigator
On October 28, 1994, Netscape Navigator was released, helping millions explore the early web.

Given an array of browser commands you executed on Netscape Navigator, return the current page you are on after executing all the commands using the following rules:

You always start on the "Home" page, which will not be included in the commands array.
Valid commands are:
"Visit Page": Where "Page" is the name of the page you are visiting. For example, "Visit About" takes you to the "About" page. When you visit a new page, make sure to discard any forward history you have.
"Back": Takes you to the previous page in your history or stays on the current page if there isn't one.
"Forward": Takes you forward in the history to the page you came from or stays on the current page if there isn't one.
For example, given ["Visit About Us", "Back", "Forward"], return "About Us".
"""

class BrowserHistory:
    def __init__(self, homepage: str): 
        self.backStack = [homepage]
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
        
def navigate(c):
    h=BrowserHistory("Visit Home")
    bf=["Back","Forward"]
    for i in range(len(c)):
        if not c[i] in bf:
            h.visit(c[i])
        if c[i]=="Back":
            h.back(1)
        if c[i]=="Forward":
            h.forward(1)
    res=h.backStack[len(h.backStack)-1][6:]
    return res

""" 29-10-2025: Email Sorter
On October 29, 1971, the first email ever was sent, introducing the username@domain format we still use. Now, there are billions of email addresses.

In this challenge, you are given a list of email addresses and need to sort them alphabetically by domain name first (the part after the @), and username second (the part before the @).

Sorting should be case-insensitive.
If more than one email has the same domain, sort them by their username.
Return an array of the sorted addresses.
Returned addresses should retain their original case.
For example, given ["jill@mail.com", "john@example.com", "jane@example.com"], return ["jane@example.com", "john@example.com", "jill@mail.com"].
"""

def sort(emails):
    hlp=[[] for c in range(len(emails))]
    for i in range(len(emails)):
        sp=emails[i].split("@")
        hlp[i].append(sp[1].lower())
        hlp[i].append(sp[0].lower())
        hlp[i].append(i)
    st=sorted(hlp)
    ords=[]
    for i in range(len(st)):
        ords.append(st[i][-1])
    print(ords)
    res=[]
    for i in range(len(ords)):
        res.append(emails[ords[i]])
    return res

""" 30-10-2025 Nth Prime
A prime number is a positive integer greater than 1 that is divisible only by 1 and itself. The first five prime numbers are 2, 3, 5, 7, and 11.

Given a positive integer n, return the nth prime number. For example, given 5 return the 5th prime number: 11.
"""

import math
def is_prime(num):
    for i in range(2,math.ceil(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

def nth_prime(n):
    p=[2]
    for i in range(2,8000):
        if is_prime(i):
            p.append(i)
    return p[n-1]

""" 31-10-2025: SpOoKy~CaSe
Given a string representing a variable name, convert it to "spooky case" using the following constraints:

Replace all underscores (_), and hyphens (-) with a tilde (~).
Capitalize the first letter of the string, and every other letter after that, ignore the tilde character when counting.
For example, given hello_world, return HeLlO~wOrLd."""

def alter(wrd,p):
    res=""
    if p==0:
        for i in range(len(wrd)):
            if i%2==0:
                res+=wrd[i].upper()
            else:
                res+=wrd[i].lower()
    if p==1:
        for i in range(len(wrd)):
            if i%2==0:
                res+=wrd[i].lower()
            else:
                res+=wrd[i].upper()
    return res
    
import re
def spookify(boo):
    b=boo.replace("-","~").replace("_","~")
    b=b.replace("~~","~X~")
    s=b.split("~")
    res=[alter(s[0],0)]
    for i in range(1,len(s)):
        if res[i-1][-1].islower() and res[i-1].upper()!="X":
            res.append(alter(s[i],0))
        if res[i-1][-1].isupper() and res[i-1].upper()!="X":
            res.append(alter(s[i],1))
        if res[i-1].upper()=="X":
            res.append(alter(s[i],1))
    res="~".join(res).replace("x","").replace("X","")
    return res
