""" 01-12-2025: Miles to Kilometers
Given a distance in miles as a number, return the equivalent distance in kilometers.

The input will always be a non-negative number.
1 mile equals 1.60934 kilometers.
Round the result to two decimal places. """

def convert_to_km(miles):
    return round(1.60934*miles,2)

""" 02-12-2025: Camel to Snake
Given a string in camel case, return the snake case version of the string using the following rules:

The input string will contain only letters (A-Z and a-z) and will always start with a lowercase letter.
Every uppercase letter in the camel case string starts a new word.
Convert all letters to lowercase.
Separate words with an underscore (_). """

def to_snake(c):
    ind=[0]
    res=[]
    for i in range(len(c)):
        if c[i].isupper():
            ind.append(i)
    ind.append(len(c))
    for i in range(1,len(ind)):
        res.append(c[ind[i-1]:ind[i]].lower())
    return "_".join(res)

""" 03-12-2025: Markdown Ordered List Item Converter
Given a string representing an ordered list item in Markdown, return the equivalent HTML string.

A valid ordered list item in Markdown must:

Start with zero or more spaces, followed by
A number (1 or greater) and a period (.), followed by
At least one space, and then
The list item text.
If the string doesn't have the exact format above, return "Invalid format". Otherwise, wrap the list item text in li tags and return the string.

For example, given "1. My item", return "<li>My item</li>". """

import re
def convert_list_item(md):
    x=re.split("[1-9]\.",md);
    res=""
    for el in x:
        el=el.strip()
        if el=="":
            el="<li>"
        res+=el
    res+="</li>"
    if len(x)>1:
        return res
    else:
        return "Invalid format"
    

""" 04-12-2025: Permutation Count
Given a string, return the number of distinct permutations that can be formed from its characters.

A permutation is any reordering of the characters in the string.
Do not count duplicate permutations.
If the string contains repeated characters, repeated arrangements should only be counted once.
The string will contain only letters (A-Z, a-z).
For example, given "abb", return 3 because there's three unique ways to arrange the letters: "abb", "bab", and "bba". """

def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

def count_permutations(s):
    sn=factorial(len(s))
    l=list(set(list(s)))
    for i in range(len(l)):
        sp=s.split(str(l[i]))
        sn/=factorial(len(sp)-1)
    return sn

""" 05-12-2025 Symmetric Difference
Given two arrays, return a new array containing the symmetric difference of them.

The symmetric difference between two sets is the set of values that appear in either set, but not both.
Return the values in the order they first appear in the input arrays. """

def difference(arr1, arr2):
    res=[]
    for c in arr1:
        if not c in arr2:
            res.append(c)
    for c in arr2:
        if not c in arr1:
            res.append(c)
    return res

""" 06-12-2025: Date Formatter
Given a date in the format "Month day, year", return the date in the format "YYYY-MM-DD".

The given month will be the full English month name. For example: "January", "February", etc.
In the return value, pad the month and day with leading zeros if necessary to ensure two digits.
For example, given "December 6, 2025", return "2025-12-06". """

def format_date(date_string):
    sp=date_string.split(" ")
    conv={"January":"01","February":"02","March":"03","April":"04","May":"05","June":"06","July":"07","August":"08","September":"09","October":"10","November":"11","December":"12"}
    p1=sp[0];
    p2=sp[1].replace(",","")
    if int(p2)<10:
      d="0"+p2
    else:
      d=p2
    return sp[2]+"-"+conv[p1]+"-"+d
    
""" 07-12-2025: String Compression
Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by the word followed with the number of times it repeats in parentheses.

Only consecutive duplicates are compressed.
Words are separated by single spaces.
For example, given "yes yes yes please", return "yes(3) please". """

def compress_string(s):
    d={}
    sp=s.split(" ")
    for i in range(len(sp)):
        if sp[i] in d.keys():
            d[sp[i]]+=1
        else:
            d[sp[i]]=1
    r=list(d.keys())
    res=[]
    for i in range(len(r)):
        stri=(r[i]+"("+str(d[r[i]])+")").replace("(1)","")
        res.append(stri)
    return " ".join(res)
    
""" 08-12-2025: Pounds to Kilograms
Given a weight in pounds as a number, return the string "(lbs) pounds equals (kgs) kilograms.".

Replace "(lbs)" with the input number.
Replace "(kgs)" with the input converted to kilograms, rounded to two decimals and always include two decimal places in the value.
1 pound equals 0.453592 kilograms.
If the input is 1, use "pound" instead of "pounds".
If the converted value is 1, use "kilogram" instead of "kilograms". """

def convert_to_kgs(lbs):
    kg=round(lbs*0.453592,2)
    if str(kg)[-2:]==".0":
        fkg=str(kg)+"0"
    else:
        fkg=str(kg)
    if lbs==1:
        s1=""
    else:
        s1="s"
    if kg==1:
        s2=""
    else:
        s2="s"
    stri=f"{lbs} pound{s1} equals {fkg} kilogram{s2}."
    return stri
    
""" 09-12-2025: Most Frequent
Given an array of elements, return the element that appears most frequently.

There will always be a single most frequent element."""

def most_frequent(arr):
    d={}
    for i in range(len(arr)):
        if arr[i] in d.keys():
            d[arr[i]]+=1
        else:
            d[arr[i]]=1
    maxi=arr[0]
    for k in d.keys():
        if d[k]>=d[maxi]:
            maxi=k
    return maxi


""" 10-12-2025: Markdown Bold Parser
Given a string that may include some bold text in Markdown, return the equivalent HTML string.

Bold text in Markdown is any text that starts and ends with two asterisks (**) or two underscores (__).
There cannot be any spaces between the text and the asterisks or underscores, but there can be spaces in the text itself.
Convert all bold occurrences to HTML b tags and return the string.
For example, given "**This is bold**", return "<b>This is bold</b>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included."""

def parse_bold(md):
    lst=[]
    sp=md.split(" ")
    for i in range(len(sp)):
        if sp[i]=="**" or sp[i]=="__":
            return md
    for i in range(len(sp)):
        if sp[i][0:2]=="**" or sp[i][0:2]=="__":
            sp[i]="<b>"+sp[i][2:]
    for i in range(len(sp)):
        if sp[i][-2:]=="**" or sp[i][-2:]=="__":
            sp[i]=sp[i][0:-2]+"</b>"
    return " ".join(sp)
    
""" 11-12-2025: Roman Numeral Builder
Given an integer, return its equivalent value in Roman numerals.

Roman numerals use these symbols:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Roman numerals are written from largest to smallest, left to right using the following rules:

Addition is used when a symbol is followed by one of equal or smaller value. For example, 18 is written as XVIII (10 + 5 + 1 + 1 + 1 = 18).
Subtraction is used when a smaller symbol appears before a larger one, to represent 4 or 9 in any place value. For example, 19 is written as XIX (10 + (10 - 1)).
No symbol may be repeated more than three times in a row. Subtraction is used when you would otherwise need to write a symbol more than three times in a row. So the largest number you can write is 3999.
Here's one more example: given 1464, return "MCDLXIV" (1000 + (500 - 100) + 50 + 10 + (5 - 1))."""

def to_roman(num):
    nums=[1000,900,500,400,100,90,50,40,10,9,5,4,1];
    romans=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I'];
    res=""
    while num>0:
        for i in range(len(romans)):
            if num>=nums[i]:
                num-=nums[i]
                res+=romans[i]
                break
    return res
    
""" 12-12-2025: Inventory Update
Given a 2D array representing the inventory of your store, and another 2D array representing a shipment you have received, return your updated inventory.

Each element in the arrays will have the format: [quantity, "item"], where quantity is an integer and "item" is a string.
Update items in the inventory by adding the quantity of any matching items from the shipment.
If a received item does not exist in the current inventory, add it as a new entry to the end of the inventory.
Return inventory in the order it was given with new items at the end in the order they appear in the shipment.
For example, given an inventory of [[2, "apples"], [5, "bananas"]] and a shipment of [[1, "apples"], [3, "bananas"]], return [[3, "apples"], [8, "bananas"]]. """

def update_inventory(inv, ship):
    arr1=[]
    arr2=[]
    am1=[]
    am2=[]
    for i in range(len(inv)):
        arr1.append(inv[i][1])
        am1.append(inv[i][0])
    for j in range(len(ship)):
        arr2.append(ship[j][1])
        am2.append(ship[j][0])
    d=dict(zip(arr1,am1))
    for j in range(len(ship)):
        if arr2[j] in d.keys():
            d[arr2[j]]+=am2[j]
        else:
             d[arr2[j]]=am2[j]
    res=[]
    for k in d.keys():
        res.append([d[k],k])
    return res

""" 13-12-2025: Game of Life
Given a matrix (array of arrays) representing the current state in Conway's Game of Life, return the next state of the matrix using these rules:

Each cell is either 1 (alive) or 0 (dead).
A cell's neighbors are the up to eight surrounding cells (vertically, horizontally, and diagonally).
Cells on the edges have fewer than eight neighbors.
Rules for updating each cell:

Any live cell with fewer than two live neighbors dies (underpopulation).
Any live cell with two or three live neighbors lives on.
Any live cell with more than three live neighbors dies (overpopulation).
Any dead cell with exactly three live neighbors becomes alive (reproduction).
For example, given:

[
  [0, 1, 0],
  [0, 1, 1],
  [1, 1, 0]
]
return:

[
  [0, 1, 1],
  [0, 0, 1],
  [1, 1, 1]
]
Each cell updates according to the number of live neighbors. 
For instance, [0][0] stays dead (2 live neighbors), [0][1] stays alive (2 live neighbors), [0][2] dies (3 live neighbors), and so on. """

def game_of_life(grid):
    m,n = len(grid),len(grid[0])
    new = [[0 for _ in range(n)] for _ in range(m)]
    dirs = [(0, 1),(1, 0),(0, -1),(-1, 0),(1, 1),(-1, -1),(1, -1),(-1, 1)]
    for i in range(m):
        for j in range(n):
            live=0
            for dx,dy in dirs:
                x,y=i+dx,j+dy
                if 0 <= x < m and 0 <= y < n and (grid[x][y] == 1):
                    live+=1
            if grid[i][j] == 1 and (live<2 or live>3):
                new[i][j]=0
            elif grid[i][j]==0 and live==3:
                new[i][j]=1
            else:
                new[i][j]=grid[i][j]
    return new
    
""" 14-12-2025: Capitalize It
Given a string title, return a new string formatted in title case using the following rules:

Capitalize the first letter of each word.
Make all other letters in each word lowercase.
Words are always separated by a single space."""

def title_case(title):
    sp=title.split(" ")
    res=""
    for i in range(len(sp)):
        res+=sp[i][0].upper()+sp[i][1:].lower()+" "
    return res[0:-1]
    
""" 15-12-2025: Speed Check
Given the speed you are traveling in miles per hour (MPH), and a speed limit in kilometers per hour (KPH), determine whether you are speeding and if you will get a warning or a ticket.

1 mile equals 1.60934 kilometers.
If you are travelling less than or equal to the speed limit, return "Not Speeding".
If you are travelling 5 KPH or less over the speed limit, return "Warning".
If you are travelling more than 5 KPH over the speed limit, return "Ticket"."""

def speed_check(speed_mph, speed_limit_kph):
    speed_kph=speed_mph*1.60934
    if speed_kph<=speed_limit_kph:
        return "Not Speeding"
    elif speed_kph-5<=speed_limit_kph:
        return "Warning"
    else:
        return "Ticket"
        
""" 16-11-2025: Consonant Count
Given a string and a target number, determine whether the string contains exactly the target number of consonants.

Consonants are all alphabetic characters except "a", "e", "i", "o", and "u" in any case.
Ignore digits, punctuation, spaces, and other non-letter characters when counting."""

def has_consonant_count(text, target):
    sn=0
    c="bcdfghjklmnpqrstvwxyz";
    for ch in text:
        if ch.lower() in c:
            sn+=1
    return sn==target
    
""" 17-12-2025: Markdown Blockquote Parser
Given a string that includes a blockquote in Markdown, return the equivalent HTML string.

A blockquote in Markdown is any line that:

Starts with zero or more spaces
Followed by a greater-than sign (>)
Then, one or more spaces
And finally, the blockquote text.
Return the blockquote text surrounded by opening and closing HTML blockquote tags.

For example, given "> This is a quote", return <blockquote>This is a quote</blockquote>.

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included."""

def parse_blockquote(markdown):
    md=markdown.strip()
    sp=" ".join(md.split(" ")[1:]).strip()
    stri="<blockquote>"+sp+"</blockquote>"
    return stri
    
""" 18-12-2025: Checkerboard
Given an array with two numbers, the first being the number of rows and the second being the number of columns, return a matrix (an array of arrays) filled with "X" and "O" characters of the given size.

The characters should alternate like a checkerboard.
The top-left cell must always be "X".
For example, given [3, 3], return:

[
  ["X", "O", "X"],
  ["O", "X", "O"],
  ["X", "O", "X"]
]
"""

def create_board(dims):
    rows=dims[0]
    cols=dims[1]
    a=[]
    for i in range(rows):
        a.append([])
    for i in range(rows):
        for j in range(cols):
            if (i+j)%2==0:
                a[i].append("X")
            else:
                a[i].append("O")
    return a

""" 19-12-2025: Pairwise
Given an array of integers and a target number, find all pairs of elements in the array whose values add up to the target and return the sum of their indices.

For example, given [2, 3, 4, 6, 8] and 10, you will find two valid pairs:

2 and 8 (2 + 8 = 10), whose indices are 0 and 4
4 and 6 (4 + 6 = 10), whose indices are 2 and 3
Add all the indices together to get a return value of 9. """

def pairwise(arr, target):
    sn=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]+arr[j]==target and j>i:
                sn+=i+j
    return sn

""" 20-12-2025: Purge Most Frequent
Given an array of values, remove all occurrences of the most frequently occurring element and return the resulting array.

If multiple values are tied for most frequent, remove all of them.
Do not change any of the other elements or their order. """

import collections
def purge_most_frequent(arr):
    cnt=collections.Counter(arr)
    mf=cnt.most_common(1)[0][0]
    res=[]
    for i in range(len(arr)):
        if arr[i]!=mf:
            res.append(arr[i])
    return res
    
""" 21-12-2025: Daylight Hours
December 21st is the winter solstice for the northern hemisphere and the summer solstice for the southern hemisphere. That means it's the day with the least daylight in the north and the most daylight in the south.

Given a latitude number from -90 to 90, return a rough approximation of daylight hours on the solstice using the following table:

Latitude	Daylight Hours
-90	24
-75	23
-60	21
-45	15
-30	13
-15	12
0	12
15	11
30	10
45	9
60	6
75	2
90	0
If the given latitude does not exactly match a table entry, use the value of the closest latitude. """

def daylight_hours(lat):
    lats=[-90,-75,-60,-45,-30,-15,0,15,30,45,60,75,90]
    vals=[24,23,21,15,13,12,12,11,10,9,6,2,0]
    diff=[]
    for i in range(len(lats)):
        diff.append(abs(lats[i]-lat))
    ind=diff.index(min(diff))
    return vals[ind]

""" 22-12-2025: Traveling Shopper
Given an amount of money you have, and an array of items you want to buy, determine how many of them you can afford.

The given amount will be in the format ["Amount", "Currency Code"]. For example: ["150.00", "USD"] or ["6000", "JPY"].
Each array item you want to purchase will be in the same format.
Use the following exchange rates to convert values:

Currency	1 Unit Equals
USD	1.00 USD
EUR	1.10 USD
GBP	1.25 USD
JPY	0.0070 USD
CAD	0.75 USD
If you can afford all the items in the list, return "Buy them all!".
Otherwise, return "Buy the first X items.", where X is the number of items you can afford when purchased in the order given. """

def buy_items(funds, items):
    conv={"USD":1.00,"EUR":1.10,"GBP":1.25,"JPY":0.0070,"CAD":0.75}	
    av=float(funds[0])*conv[funds[1]]
    am=0
    sn=0
    for i in range(len(items)):
        c=float(items[i][0])*conv[items[i][1]]
        am+=c
        if am<=av:
            sn+=1
    if sn==len(items):
        return "Buy them all!"
    else:
        return f"Buy the first {sn} items."

""" 23-12-2025: Re: Fwd: Fw: Count
Given a string representing the subject line of an email, determine how many times the email has been forwarded or replied to.

For simplicity, consider an email forwarded or replied to if the string contains any of the following markers (case-insensitive):

"fw:"
"fwd:"
"re:"
Return the total number of occurrences of these markers. """

def email_chain_count(subject):
    sn=0
    sp=subject.split(":")
    for i in range(len(sp)):
        if sp[i].lower().strip() in ["fw","fwd","re"]:
            sn+=1
    return sn
    
""" 24-12-2025: Markdown Image Parser
Given a string of an image in Markdown, return the equivalent HTML string.

A Markdown image has the following format: "![alt text](image_url)". Where:

alt text is the description of the image (the alt attribute value).
image_url is the source URL of the image (the src attribute value).
Return a string of the HTML img tag with the src set to the image URL and the alt set to the alt text.

For example, given "![Cute cat](cat.png)" return '<img src="cat.png" alt="Cute cat">';

Make sure the tag, order of attributes, spacing, and quote usage is the same as above.
Note: The console may not display HTML tags in strings when logging messages — check the browser console to see logs with tags included. """

def parse_image(md):
    sp=md.split("(")
    im=sp[1][:-1]
    alt=sp[0][2:-1]
    stri=f'<img src="{im}" alt="{alt}">'
    return stri

""" 25-12-2025: Snowflake Generator
Given a multi-line string that uses newline characters (\n) to represent a line break, return a new string where each line is mirrored horizontally and attached to the end of the original line.

Mirror a line by reversing all of its characters, including spaces.
For example, given "* \n *\n* ", which logs to the console as:

* 
 *
* 
Return "*  *\n ** \n*  *", which logs to the console as:

*  *
 ** 
*  *
Take careful note of the whitespaces in the given and returned strings. Be sure not to trim any of them. """

def generate_snowflake(crystals):
    stri=""
    res=[]
    sp=crystals.split("\n")
    for i in range(len(sp)):
        res.append(sp[i]+sp[i][::-1])
    return "\n".join(res)

""" 26-12-2025: Sum of Divisors
Given a positive integer, return the sum of all its divisors.

A divisor is any integer that divides the number evenly (the remainder is 0).
Only count each divisor once.
For example, given 6, return 12 because the divisors of 6 are 1, 2, 3, and 6, and the sum of those is 12. """

def sum_divisors(n):
    sn=0
    for i in range(1,n+1):
        if n%i==0:
            sn+=i
    return sn

""" 27-12-2025: Rock, Paper, Scissors
Given two strings, the first representing Player 1 and the second representing Player 2, determine the winner of a match of Rock, Paper, Scissors.

The input strings will always be "Rock", "Paper", or "Scissors".
"Rock" beats "Scissors".
"Paper" beats "Rock".
"Scissors" beats "Paper".
Return:

"Player 1 wins" if Player 1 wins.
"Player 2 wins" if Player 2 wins.
"Tie" if both players choose the same option. """

def rock_paper_scissors(player1, player2):
    c=[["Rock","Scissors"],["Paper","Rock"],["Scissors","Paper"]]
    if player1==player2:
        return "Tie"
    elif [player1,player2] in c:
        return "Player 1 wins"
    else:
        return "Player 2 wins"
        
""" 28-12-2025: SCREAMING_SNAKE_CASE
Given a string representing a variable name, return the variable name converted to SCREAMING_SNAKE_CASE.

The given variable names will be written in one of the following formats:

camelCase
PascalCase
snake_case
kebab-case
In the above formats, words are separated by an underscore (_), a hyphen (-), or a new word starts with a capital letter.

To convert to SCREAMING_SNAKE_CASE:

Make all letters uppercase
Separate words with an underscore (_) """

def to_screaming_snake_case(vari):
    res=vari[0].upper()
    for i in range(1,len(vari)):
        if(vari[i].isupper()):
            res+="_"+vari[i]
        else:
            res+=vari[i].upper()
    res=res.replace("-","_")
    return res

""" 29-12-2025: Takeoff Fuel
Given the numbers of gallons of fuel currently in your airplane, and the required number of liters of fuel to reach your destination, determine how many additional gallons of fuel you should add.

1 gallon equals 3.78541 liters.
If the airplane already has enough fuel, return 0.
You can only add whole gallons.
Do not include decimals in the return number. """

import math
def fuel_to_add(curr_gall, req_lit):
    curr_lit=curr_gall*3.78541
    need=math.ceil((req_lit-curr_lit)/3.78541)
    if need<0:
        return 0
    else:
        return need

""" 30-12-2025: Sum the String
Given a string containing digits and other characters, return the sum of all numbers in the string.

Treat consecutive digits as a single number. For example, "13" counts as 13, not 1 + 3.
Ignore any non-digit characters. """

import re
def string_sum(s):
    sn=0
    m = re.findall("[0-9]+",s)
    for i in range(len(m)):
        sn+=int(m[i])
    return sn
    
""" 31-12-2025: Markdown Italic Parser
Given a string that may include some italic text in Markdown, return the equivalent HTML string.

Italic text in Markdown is any text that starts and ends with a single asterisk (*) or a single underscore (_).
There cannot be any spaces between the text and the asterisk or underscore, but there can be spaces in the text itself.
Convert all italic occurrences to HTML i tags and return the string.
For example, given "*This is italic*", return "<i>This is italic</i>". """

import re
def parse_italics(md):
    sp=re.split(r'[*_]+',md)
    if md[:2] in ["* ","_ "] or md[-2:] in [" *"," _"]:
        return md
    res=""
    for i in range(len(sp)):
        if sp[i]==sp[i].strip() and len(sp[i])>0:
            res+="<i>"+sp[i]+"</i>"
        else:
            res+=sp[i]
    return res
