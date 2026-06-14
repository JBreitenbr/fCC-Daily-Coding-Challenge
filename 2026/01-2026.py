""" 01-01-2026 Resolution Streak
Given an array of arrays, where each sub-array represents a day of your resolution activities and contains three integers: the number of steps walked that day, the minutes of screen time that day, and the number of pages read that day; determine if you are keeping your resolutions.

The first sub-array is day 1, and second day 2, and so on.
A day is considered successful if all three of the following goals are met:

You walked at least 10,000 steps.
You had no more than 120 minutes of screen time.
You read at least five pages.
If all of the given days are successful, return "Resolution on track: N day streak." Where N is the number of successful days.

If one or more days is not a success, return "Resolution failed on day X: N day streak.". Where X is the day number of the first unsuccessful day, and N is the number of successful days before the first unsuccessful day."""

def rcheck(lst):
    return lst[0]>=10000 and lst[1]<=120 and lst[2]>=5

def resolution_streak(days):
    sn=0
    for i in range(len(days)):
        if(not rcheck(days[i])):
            sn=i
            break
    if sn>0:
        return f"Resolution failed on day {sn+1}: {sn} day streak."
    else:
        return f"Resolution on track: {len(days)} day streak."

""" 02-01-2026: Nth Fibonacci Number
Given an integer n, return the nth number in the fibonacci sequence.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34. """

def nth_fibonacci(n):
    if n<=1:
        return n
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=0
    dp[2]=1
    dp[3]=1
    for i in range(4,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
    
""" 03-01-2026: Left-Handed Seat at the Table
Given a 4x2 matrix (array of arrays) representing the seating arrangement for a meal, determine how many seats a left-handed person can sit at.

A left-handed person cannot sit where a right-handed person would be in the seat to the immediate left of them.
In the given matrix:

An "R" is a seat occupied by a right-handed person.
An "L" is a seat occupied by a left-handed person.
An "U" is an unoccupied seat.
Only unoccupied seats are available to sit at.
The seats in the top row are facing "down", and the seats in the bottom row are facing "up" (like a table), so left and right are relative to the seat's orientation.
Corner seats only have one seat next to them.
For example, in the given matrix:

[
  ["U", "R", "U", "L"],
  ["U", "R", "R", "R"]
]
The top-left seat is cannot be sat in because there's a right-handed person to the left. The other two open seats can be sat in because there isn't a right-handed person to the left.
"""

def find_left_handed_seats(table):
    row1=table[0]
    row2=table[1]
    rev=list("".join(table[1])[::-1])
    sn=0
    for i in range(len(row1)-1):
        if row1[i]=="U" and row1[i+1]!="R":
            sn+=1
        if rev[i]=="U" and rev[i+1]!="R":
            sn+=1
    if row1[-1]=="U":
        sn+=1
    if rev[-1]=="U":
        sn+=1
    return sn

""" 04-01-2026: Leap Year Calculator
Given an integer year, determine whether it is a leap year.

A year is a leap year if it satisfies the following rules:

The year is evenly divisible by 4, and
The year is not evenly divisible by 100, unless
The year is evenly divisible by 400. 
"""

def is_leap_year(year):
    return year%400==0 or year%4==0 and year%100!=0

""" 05-01-2026: Tire Pressure
Given an array with four numbers representing the tire pressures in psi of the four tires in your vehicle, and another array of two numbers representing the minimum and maximum pressure for your tires in bar, return an array of four strings describing each tire's status.

1 bar equal 14.5038 psi.
Return an array with the following values for each tire:

"Low" if the tire pressure is below the minimum allowed.
"Good" if it's between the minimum and maximum allowed.
"High" if it's above the maximum allowed. """

def tire_status(pressures_psi, range_bar):
    c=14.5038
    res=[]
    for el in pressures_psi:
        if el/c<range_bar[0]:
            res.append("Low")
        elif el/c<range_bar[1]:
            res.append("Good")
        else:
            res.append("High")
    return res

""" 06-01-2026: vOwElcAsE
Given a string, return a new string where all vowels are converted to uppercase and all other alphabetical characters are converted to lowercase.

Vowels are "a", "e", "i", "o", and "u" in any case.
Non-alphabetical characters should remain unchanged. """

def vowel_case(s):
    v=list("aeiou")
    c=list("BCDFGHJKLMNPQRSTVWXYZ")
    res=""
    for l in s:
        if l in v:
            res+=l.upper()
        elif l in c:
            res+=l.lower()
        else:
            res+=l
    return res

""" 07-01-2026: Markdown Unordered List Parser
Given the string of a valid unordered list in Markdown, return the equivalent HTML string.

An unordered list consists of one or more list items. A valid list item appears on its own line and:

Starts with a dash ("-"), followed by
At least one space, and then
The list item text.
The list is given as a single string with new lines separated by the newline character ("\n"). Do not include the newline characters in the item text.

Wrap each list item in HTML li tags, and the whole list of items in ul tags.

For example, given "- Item A\n- Item B", return "<ul><li>Item A</li><li>Item B</li></ul>". """

def parse_unordered_list(md):
    sp=md.replace("\n","").split("- ")
    res="<ul>"
    for el in sp:
        if el!="":
            res+="<li>"+el.strip()+"</li>"
    return res+"</ul>"
    
""" 08-01-2026: Sorted Array?
Given an array of numbers, determine if the numbers are sorted in ascending order, descending order, or neither.

If the given array is:

In ascending order (lowest to highest), return "Ascending".
In descending order (highest to lowest), return "Descending".
Not sorted in ascending or descending order, return "Not sorted". """

def is_sorted(arr):
    c=[]
    for i in range(1,len(arr)):
        c.append(arr[i]-arr[i-1])
    flt1=[]
    flt2=[]
    for i in range(len(c)):
        if c[i]>0:
            flt1.append(c[i])
        if c[i]<0:
            flt2.append(c[i])
    if len(flt1)==len(c):
        return "Ascending"
    elif len(flt2)==len(c):
        return "Descending"
    else:
        return "Not sorted"

""" 09-01-2026: Circular Prime
Given an integer, determine if it is a circular prime.

A circular prime is an integer where all rotations of its digits are themselves prime.

For example, 197 is a circular prime because all rotations of its digits: 197, 971, and 719, are prime numbers. """

def is_prime(n):
    res=[]
    for i in range(2,n):
        if n%i==0:
            res.append(i)
    if len(res)==0:
        return True
    else:
        return False


def is_circular_prime(n):
    c=[str(n)]
    for i in range(1,len(str(n))):
        t=c[i-1][1:]+c[i-1][0]
        c.append(t)
    for i in range(len(c)):
        if not is_prime(int(c[i])):
            return False
            break
    return True
    
""" 10-01-2026: Tic-Tac-Toe
Given a 3×3 matrix (an array of arrays) representing a completed Tic-Tac-Toe game, determine the winner.

Each element in the given matrix is either an "X" or "O".
A player wins if they have three of their characters in a row - horizontally, vertically, or diagonally.

Return:

"X wins" if player X has three in a row.
"O wins" if player O has three in a row.
"Draw" if no player has three in a row. """

def tic_tac_toe(m):
    t=[[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    d1=m[0][0]+m[1][1]+m[2][2]
    d2=m[0][2]+m[1][1]+m[2][0]
    for i in range(3):
        if "".join(m[i])=="OOO" or "".join(t[i])=="OOO" or d1=="OOO" or d2=="OOO":
            return "O wins"
        elif "".join(m[i])=="XXX" or "".join(t[i])=="XXX" or d1=="XXX" or d2=="XXX":
            return "X wins"
    return "Draw"

""" 11-01-2026: Par for the Hole
Given two integers, the par for a golf hole and the number of strokes a golfer took on that hole, return the golfer's score using golf terms.

Return:

"Hole in one!" if it took one stroke.
"Eagle" if it took two strokes less than par.
"Birdie" if it took one stroke less than par.
"Par" if it took the same number of strokes as par.
"Bogey" if it took one stroke more than par.
"Double bogey" if took two strokes more than par. """

def golf_score(par, strokes):
    if strokes==1:
        return "Hole in one!"
    elif par-strokes==2:
        return "Eagle"
    elif par-strokes==1:
        return "Birdie"
    elif par==strokes:
        return "Par"
    elif strokes-par==1:
        return "Bogey"
    elif strokes-par==2:
        return "Double bogey"

""" 12-01-2026: Plant the Crop
Given an integer representing the size of your farm field, and "acres" or "hectares" representing the unit for the size of your farm field, and a type of crop, determine how many plants of that type you can fit in your field.

1 acre equals 4046.86 square meters.
1 hectare equals 10,000 square meters.
Here's a list of crops that will be given as input and how much space a single plant takes:

Crop	Space per plant
"corn"	1 square meter
"wheat"	0.1 square meters
"soybeans"	0.5 square meters
"tomatoes"	0.25 square meters
"lettuce"	0.2 square meters
Return the number of plants that fit in the field, rounded down to the nearest whole plant. """

import math
def get_number_of_plants(field_size, unit, crop):
    c={"corn":1,"wheat":0.1,"soybeans":0.5,"tomatoes":0.25,"lettuce":0.2}
    if unit=="acres":
        fac=4046.86
    else: 
        fac=10000
    return math.floor(1/c[crop]*fac*field_size)

""" 13-01-2026: Odd or Even?
Given a positive integer, return "Odd" if it's an odd number, and "Even" if it's even. """

def odd_or_even(n):
    if n%2==1:
        return "Odd"
    else:
        return "Even"

""" 14-01-2026: Markdown Link Parser
Given the string of a link in Markdown, return the equivalent HTML string.

A Markdown image has the following format: "[link_text](link_url)". Return the string of the HTML a tag with the href set to the link_url and the link_text as the tag content.

For example, given "[freeCodeCamp](https://freecodecamp.org/)" return '<a href="https://freecodecamp.org/">freeCodeCamp</a>';

Note: The console may not display HTML tags in strings when logging messages — check the browser console to see logs with tags included. """

def parse_link(md):
    sp1=md.split("]")
    lt=sp1[0][1:]
    sp2=md.split("(")
    lu=sp2[1][0:-1]
    res='<a href="'+lu+'">'+lt+'</a>'
    return res

""" 15-01-2026: Array Swap
Given an array with two values, return an array with the values swapped.

For example, given ["A", "B"] return ["B", "A"]. """

def array_swap(arr):
    s=[]
    for i in range(len(arr)):
        s.append(arr[len(arr)-i-1])
    return s

""" 16-01-2026: Integer Hypotenuse
Given two positive integers representing the lengths for the two legs (the two short sides) of a right triangle, determine whether the hypotenuse is an integer.
"""

import math
def is_integer_hypotenuse(a, b):
    c=math.sqrt(a*a+b*b)
    return c==int(c)

""" 17-01-2026: Knight Moves
Given the position of a knight on a chessboard, return the number of valid squares the knight can move to.
A standard chessboard is 8x8, with columns labeled A through H (left to right) and rows labeled 1 through 8 (bottom to top). It looks like this:
A8B8C8D8E8F8G8H8
A7B7C7D7E7F7G7H7
A6B6C6D6E6F6G6H6
A5B5C5D5E5F5G5H5
A4B4C4D4E4F4G4H4
A3B3C3D3E3F3G3H3
A2B2C2D2E2F2G2H2
A1B1C1D1E1F1G1H1
A knight moves in an "L" shape: two squares in one direction (horizontal or vertical), and one square in the perpendicular direction.
This means a knight can move to up to eight possible positions, but fewer when near the edges of the board. For example, if a knight was at A1, it could only move to B3 or C2. """

def moves(i, j):
    return [[i - 2, j - 1],[i - 1, j - 2],[i - 2, j + 1],[i - 1, j + 2],[i + 2, j - 1],[i + 1, j - 2],[i + 2, j + 1],[i + 1, j + 2]]

def knight_moves(pos):
  c={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}
    row=8-int(pos[1])
    col=c[pos[0]]
    m=moves(row,col)
    res=[] 
    for el in m:
        if el[0]>=0 and el[0]<=7 and el[1]>=0 and el[1]<=7:
            res.append(el)
    return len(res)

""" 18-01-2026: Free Shipping
Given an array of strings representing items in your shopping cart, and a number for the minimum order amount to qualify for free shipping, determine if the items in your shopping cart qualify for free shipping.
The given array will contain items from the list below:
Item       Price
"shirt"     34.25
"jeans"    48.50
"shoes"   75.00
"hat"        19.95
"socks"    15.00
"jacket"  109.95  """

def gets_free_shipping(cart, minimum):
    p={"shirt":34.25,"jeans":48.50,"shoes":75.00,"hat":19.95,"socks":15.00,"jacket":109.95}
    sn=0
    for el in cart:
        sn+=p[el]
    return sn>=minimum

""" 19-01-2026 Energy Consumption
Given the number of Calories burned during a workout, and the number of watt-hours used by your electronic devices during that workout, determine which one used more energy.
To compare them, convert both values to joules using the following conversions:
• 1 Calorie equals 4184 joules.
• 1 watt-hour equals 3600 joules.
Return:
• "Workout" if the workout used more energy.
• "Devices" if the device used more energy.
• "Equal" if both used the same amount of energy. """

def compare_energy(calories_burned, watt_hours_used):
    if calories_burned*4184>watt_hours_used*3600:
        return "Workout"
    elif calories_burned*4184<watt_hours_used*3600:
        return "Devices"
    else:
        return "Equal"

/* 20-01-2026 Consonant Case
Given a string representing a variable name, convert it to consonant case using the following rules:
• All consonants should be converted to uppercase.
• All vowels (a, e, i, o, u in any case) should be converted to lowercase.
• All hyphens (-) should be converted to underscores (_). */


def to_consonant_case(stri):
    s=stri.replace("-","_")
    res=""
    for i in range(len(s)):
        if s[i] in list("AEIOU"): res+=s[i].lower()
        elif s[i] in list("bcdfghjklmnpqrstvwxyz"):
            res+=s[i].upper()
        else: 
            res+=s[i]
    return res

"""  21-01-2026: Markdown Inline Code Parser
Given a string of Markdown that includes one or more inline code blocks, return the equivalent HTML string.
Inline code blocks in Markdown use a single backtick (`) at the start and end of the code block text.
Return the given string with all code blocks converted to HTML code tags.
For example, given the string "Use `let` to declare the variable.", return "Use <code>let</code> to declare the variable.".
Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included. """

def parse_inline_code(md):
    sp=md.split("`")
    res=""
    for el in sp:
        if el.strip()==el and not el in [".",",","?","!"]:
            res+="<code>"+el+"</code>"
        else:
            res+=el
    return res

""" 22-01-2026: Class Average
Given an array of exam scores (numbers), return the average score in form of a letter grade according to the following chart:
Average Score  Letter Grade
97-100               "A+"
93-96                 "A"
90-92                 "A−"
87-89                 "B+"
83-86                 "B"
80-82.                "B-"
77-79                 "C+"
73–76                "C"
70-72                 "C-"
67-69                 "D+"
63-66                  "D"
60–62                "D-"
below 60            "F"
Calculate the average by adding all scores in the array and dividing by the total number of scores. """

import math
def get_average_grade(scores):
    gr=["A"]*11+["B"]*10+["C"]*10+["D"]*10
    for i in range(len(gr)):
        if i%10 in [1,2,3]:
            gr[i]+="+"
        elif i%10 in [8,9,0]:
            gr[i]+="-"
    gr[0]="A+"
    rg=list(range(100,59,-1))
    res=dict(zip(rg,gr))
    sc=math.floor(sum(scores)/len(scores))
    if sc<60:
        return "F"
    return res[sc]

""" 23-01-2026: Hex Validator
Given a string, determine whether it is a valid CSS hex color. A valid CSS hex color must:
• Start with a #, and
• be followed by either 3 or 6 hexadecimal characters.
Hexadecimal characters are numbers 0 through 9 and letters a through f (case-insensitive). """

import re
def is_valid_hex(s):
    rx=re.findall("[#a-fA-F0-9]",s)
    if s[0]!="#" or (len(s)!=4 and len(s)!=7) or (len(rx)!=4 and len(rx)!=7):
        return False
    return True

""" 24-01-2026 Bingo! Letter
Given a number, return the bingo letter associated with it (capitalized). Bingo numbers are grouped as follows:
LetterNumber Range 
"B"                       1-15
"I"                       16-30
"N"                      31-45
"G"                      46-60
"O"                      61-75         """

def get_bingo_letter(n):
    if n in range(1,16):
        return "B"
    elif n in range(16,31):
        return "I"
    elif n in range(31,46):
        return "N"
    elif n in range(46,61):
        return "G"
    else:
        return "O"

 """ 25-01-2026: Scaled Image
Given a string representing the width and height of an image, and a number to scale the image, return the scaled width and height.
• The input string is in the format "WxH". For example, "800x600".
• The scale is a number to multiply the width and height by.
Return the scaled dimensions in the same "WxH" format. """

def scale_image(size, scale):
    sp=size.split("x")
    res=str(int(float(sp[0])*scale))+"x"+str(int(float(sp[1])*scale))
    return res

""" 26-01-2026 FizzBuzz Mini
Given an integer, return a string based on the following rules:
• If the number is divisible by 3, return "Fizz".
• If the number is divisible by 5, return "Buzz".
• If the number is divisible by both 3 and 5, return "FizzBuzz".
• Otherwise, return the given number as a string. """

def fizz_buzz_mini(n):
    if n%3==0 and n%5!=0:
        return "Fizz"
    elif n%3!=0 and n%5==0:
        return "Buzz"
    elif n%3==0 and n%5==0:
        return "FizzBuzz"
    return str(n)

""" 27-01-2026: Odd or Even Day
Given a timestamp (number of milliseconds since the Unix epoch), return:
• "odd" if the day of the month for that timestamp is odd.
• "even" if the day of the month for that timestamp is even.
For example, given 1769472000000, a timestamp for January 27th, 2026, return "odd" because the day number (27) is an odd number.
"""

from datetime import datetime
def odd_or_even_day(ts):
    dt=datetime.utcfromtimestamp(int(ts/1000)).strftime('%Y-%m-%d %H:%M:%S')
    day=int(str(dt)[8:10])
    if day%2==0:
        return "even"
    return "odd"

""" 28-01-2026: Flatten the Array
Given an array that contains nested arrays, return a new array with all values flattened into a single, one-dimensional array. Retain the original order of the items in the arrays.
"""

def flatten(arr):
    fl=[]
    for el in arr:
        if isinstance(el,list):
            fl.extend(flatten(el))
        else:
            fl.append(el)
    return fl

""" 29-01-2026: Letters-Numbers
Given a string containing only letters and numbers, return a new string where a hyphen (-) is inserted every time the string switches from a letter to a number, or a number to a letter.
"""

def separate_letters_and_numbers(s):
    res=s[0]
    for i in range(1,len(s)):
        if s[i-1].isalpha() and s[i].isnumeric() or s[i-1].isnumeric() and s[i].isalpha():
            res=res+"-"+s[i]
        else:
            res+=s[i]
    return res

""" 30-01-2026: Valid Pawn Moves
Given the position of one of your pawns on a chessboard, return an array of all the valid squares it can move to in ascending order.
A standard chessboard is 8x8, with columns labeled A through H (left to right) and rows labeled 1 through 8 (bottom to top). It looks like this:
A8B8C8D8E8F8G8H8
A7B7C7D7E7F7G7H7
A6B6C6D6E6F6G6H6
A5B5C5D5E5F5G5H5
A4B4C4D4E4F4G4H4
A3B3C3D3E3F3G3H3
A2B2C2D2E2F2G2H2
A1B1C1D1E1F1G1H1
For this challenge:
• You are the player on the bottom of the board.
• Pawns can only move one square "up".
• Unless the pawn is in the starting row (row 2), then it can move one or two squares up.
For example, given "D4", return ["D5"], the only square your pawn can move to. Given "B2", return ["B3", "B4"], because it's on the starting row and needs to be in ascending order.
"""


def find_pawn_moves(pos):
    l=pos[0];
    n=int(pos[1])
    if n!=2:
       return [l+str(n+1)]
    else:
       return [l+str(n+1),l+str(n+2)]

""" 31-01-2026: Zodiac Finder
Given a date string in the format "YYYY-MM-DD", return the zodiac sign for that date using the following chart:
Date Range                Zodiac Sign
March 21 - April 19.  "Aries"
April 20 - May 20.      "Taurus"
May 21 - June 20.      "Gemini"
June 21 - July 22.      "Cancer"
July 23 - August 22.  "Leo"
August 23 - Sept. 22  "Virgo"
Sept. 23 - Oct. 22.      "Libra"
Oct. 23 - Nov. 21.       "Scorpio"
Nov. 22 - Dec. 21.     "Sagittarius"
Dec. 22 - Jan. 19.      "Capricorn"
Jan. 20 - Feb. 18.      "Aquarius"
Febr. 19 - March 20.  "Pisces"
• Zodiac signs are based only on the month and day, you can ignore the year.
"""

def get_sign(date_str):
    m=int(date_str[5:7])-1
    d=int(date_str[8:])
    if (m == 0 and d <= 19) or (m == 11 and d >=22):
        return "Capricorn"
    elif (m == 0 and d >= 20) or (m == 1 and d <= 18):
        return "Aquarius"
    elif (m==1 and d>=19)  or (m==2 and d<=20):
        return "Pisces"
    elif (m==2 and d>=21) or (m==3 and d<=19) :
        return "Aries"  
    elif (m==3 and d>=20)  or (m==4 and d<=20):
        return "Taurus"
    elif (m==4 and d>=21) or (m==5 and d<=20):
        return "Gemini"
    elif (m==5 and d>=21) or (m==6 and d<=22) :
        return "Cancer"
    elif (m==6 and d>=23) or (m==7 and d<=22):
        return "Leo"
    elif (m==7 and d>=23) or (m==8 and d<=22):
        return "Virgo"
    elif (m==8 and d>=23) or (m==9 and d<=22):
        return "Libra"
    elif (m==9 and d>=23) or (m==10 and d<=21):
        return "Scorpio"
    elif (m==10 and d>=22) or (m==11 and d<=21):
        return "Sagittarius"
