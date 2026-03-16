""" 01-03-2026: Flattened 

Given an array, determine if it is flat.
• An array is flat if none of its elements are arrays. """

def is_flat(arr):
    for i in range(len(arr)):
        if isinstance(arr[i],list):
            return False
    return True

""" 02-03-2026: Sum the Letters

Given a string, return the sum of its letters.
• Letters are A-Z in uppercase or lowercase
• Letter values are: "A" = 1, "B" = 2, ..., "Z" = 26
• Uppercase and lowercase letters have the same value.
• Ignore all non-letter characters. """

import re
def sum_letters(s):
    r=re.findall("[A-Za-z]",s)
    a1="abcdefghijklmnopqrstuvwxyz"   
    a2=a1.upper()
    sn=0
    for el in r:
        if el.islower():
            sn+=a1.index(el)+1
        if el.isupper():
            sn+=a2.index(el)+1
    return sn

""" 03-03-2027: Perfect Cube Count

Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.
• The lower number is not garanteed to be the first argument.
• A number is a perfect cube if there exists an integer (n) where n * n * n = number. For example, 27 is a perfect cube because 3 * 3 * 3 = 27.  """

def count_perfect_cubes(a, b):
    c=[0]
    if b>a: 
        s1=a
        s2=b
    if b<a:
        s1=b
        s2=a
    for i in range(1,23):
        c.append(i*i*i)
        c.append(-i*i*i)
    sn=0
    for el in range(s1,s2+1):
        if el in c:
            sn+=1
    return sn

""" 04-03-2026: Playing Card Values

Given an array of playing cards, return a new array with the numeric value of each card.
Card Values:
• An Ace ("A") has a value of 1.
• Numbered cards ("2" - "10") have their face value: 2 - 10, respectively.
• Face cards: Jack ("J"), Queen ("Q"), and King ("K") are each worth 10.
Suits:
• Each card has a suit: Spades ("S"), Clubs ("C"), Diamonds ("D"), or Hearts ("H").
Card Format:
• Each card is represented as a string: "valueSuit". For Example: "AS" is the Ace of Spades, "10H" is the Ten of Hearts, and "QC" is the Queen of Clubs. """

def card_values(cards):
    res=[]
    p={"A":1,"J":10,"Q":10,"K":10};
    d=list("0123456789")
    d.append("10")
    for c in cards:
        if c[:-1] in d:
            res.append(int(c[:-1]))
        else:
            res.append(p[c[0]])
    return res

""" 05-03-2026: Smallest Gap

Given a string, return the substring between the two identical characters that have the smallest number of characters between them (smallest gap).
• There will always be at least one pair of matching characters.
• The returned substring should exclude the matching characters.
• If two or more gaps are the same length, return the characters from the first one.
For example, given "ABCDAC", return "DA".
• Only "A" and "C" repeat in the string.
• The number of characters between the two "A" characters is 3, and between the "C" characters is 2.
• So return the string between the two "C" characters. """

def flatten(arr):
    fl=[]
    for el in arr:
        if isinstance(el,list):
            fl.extend(flatten(el))
        else:
            fl.append(el)
    return fl

def gaps(arr,stri):
    res=[]
    for i in range(1,len(arr)):
        res.append(stri[arr[i-1]+1:arr[i]])
    return res

def smallest_gap(s):
    l=[]
    for el in list(set(s)):
        if len(s.split(el))>2:
           l.append(el)
    pre=[]
    for j in range(len(l)):
        ind = [i for i, x in enumerate(list(s)) if x == l[j]]
        pre.append(gaps(ind,s))
    w=flatten(pre)
    sz=[]
    for el in w:
        sz.append(len(el))
    mini=sorted(sz)[0]
    ms=[]
    for el in w:
        if len(el)==mini:
            ms.append(s.index(el))
    return s[sorted(ms)[0]:sorted(ms)[0]+mini]

"""  06-03-2026: Trail Traversal

Given an array of strings representing your trail map, return a string of the moves needed to get to your goal.
The given strings will contain the values:
• "C": Your current location
• "G": Your goal
• "T": Traversable parts of the trail
• "-": Untraversable parts of the map
Return a string with the moves needed to follow the trail from your location to your goal where:
• "R" is a move right
• "D" is a move down
• "L" is a move left
• "U" is a move up
• There will always be a single continuous trail, without any branching, from your current location to your goal.
• Each trail location will have a maximum of two traversable locations touching it.
For example, given:
[ "-CT--", "--T--", "--TT-", "---T-", "---G-" ] 
Return "RDDRDD". """

def solve_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    seq=[start]
    stack = [start]  
    visited = set() 
    while stack:
        current = stack.pop()
        x, y = current
        if current == end:
            return seq
        if current not in visited:
            visited.add(current)
            neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for nx, ny in neighbors:
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                    stack.append((nx, ny))
            seq.append(stack[0])
    return False 

def find_dir(arr):
    res=""
    for i in range(1,len(arr)):
        if arr[i][0]==arr[i-1][0] and arr[i][1]-arr[i-1][1]==1:
            res+="R"
        if arr[i][0]==arr[i-1][0] and arr[i][1]-arr[i-1][1]==-1:
            res+="L"
        if arr[i][0]-arr[i-1][0]==1 and arr[i][1]==arr[i-1][1]:
            res+="D"
        if arr[i][0]-arr[i-1][0]==-1 and arr[i][1]==arr[i-1][1]:
            res+="U"
    return res
    
def navigate_trail(m):
    for i in range(len(m)):
        c=m[i].find("C")
        g=m[i].find("G")
        if c!=-1:
            start=(i,c)
        if g!=-1:
            end=(i,g)
    hlp=[]
    for i in range(len(m)):
        hlp.append(list(m[i]))
    mat=[[1 for i in range(len(m[0]))] for _ in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            if hlp[i][j]!="-":
                mat[i][j]=0
    s=solve_maze(mat,start,end)
    return find_dir(s)
                                                           
""" 07-03-2026: Element Size

Given a window size, the width of an element in viewport width "vw" units, and the height of an element in viewport height "vh" units, determine the size of the element in pixels.
• The given window size and returned element size are strings in the format "width x height", "1200 x 800" for example.
• "vw" units are the percent of window width. "50vw" for example, is 50% of the width of the window.
• "vh" units are the percent of window height. "50vh" for example, is 50% of the height of the window. """

def get_element_size(window_size, element_vw, element_vh):
    vw=float(element_vw[:-2])/100
    vh=float(element_vh[:-2])/100
    sp=window_size.split(" x ")
    ws=str(round(int(sp[0])*vw))+" x "+str(round(int(sp[1])*vh))
    return ws

""" 08-03-2026: HSL Validator

Given a string, determine whether it is a valid CSS hsl() color value.
• A valid HSL value must be in the format "hsl(h, s%, l%)", where:
• h (hue) must be a number between 0 and 360 (inclusive).
• s (saturation) must be a percentage between 0% and 100%.
• l (lightness) must be a percentage between 0% and 100%.
• Spaces are only allowed:
• After the opening parenthesis
• Before and/or after the commas
• Before and/or after closing parenthesis
• Optionally, the value can end with a semi-colon (";").
For example, "hsl(240, 50%, 50%)" is a valid HSL value. """

def is_valid_hsl(hsl):
    if not "hsl(" in hsl:
        return False
    s=hsl[4:].replace(";","").replace(")","").split(",")
    c1=float(s[0])>=0 and float(s[0])<=255
    p2=float(s[1].strip()[::-1][1:][::-1])
    c2=p2>=0 and p2<=100 and "%" in s[1]
    p3=float(s[2].strip()[::-1][1:][::-1])
    c3=p3>=0 and p3<=100 and "%" in s[2]
    return c1 and c2 and c3
    
""" 09-03-2026: Array Sum

Given an array of numbers, return the sum of all the numbers. """

def sum_array(numbers):
    sn=0
    for num in numbers:
        sn+=num
    return sn

""" 10-03-2026: Array Insertion

Given an array, a value to insert into the array, and an index to insert the value at, return a new array with the value inserted at the specified index. """

def insert_into_array(arr, value, index):
    arr1=arr[:index]
    arr2=arr[index:]
    return arr1 + [value] +arr2

""" 11-03-2026: Word Length Converter

Given a string of words, return a new string where each word is replaced by its length.
• Words in the given string will be separated by a single space
• Keep the spaces in the returned string.
For example, given "hello world", return "5 5".  """

def convert_words(s):
    lst=s.split(" ")
    res=""
    for el in lst:
        res+=str(len(el))+" "
    return res[:-1]

""" 12-03-2026: Domino Chain Validator 

Given a 2D array representing a sequence of dominoes, determine whether it forms a valid chain.
• Each element in the array represents a domino and will be an array of two numbers from 1 to 6, (inclusive).
• For the chain to be valid, the second number of each domino must match the first number of the next domino.
• The first number of the first domino and the last number of the last domino don't need to match anything. """

def is_valid_domino_chain(dominoes):
    for i in range(1,len(dominoes)):
        if not dominoes[i][0]==dominoes[i-1][1]:
            return False
    return True

""" 13-03-2026: Parking Fee Calculator
Given two strings representing the time you parked your car and the time you picked it up, calculate the parking fee.
• The given strings will be in the format "HH:MM" using a 24-hour clock. So "14:00" is 2pm for example.
• The first string will be the time you parked your car, and the second will be the time you picked it up.
• If the pickup time is earlier than the entry time, it means the parking spanned past midnight into the next day.
Fee rules:
• Each hour parked costs $3.
• Partial hours are rounded up to the next full hour.
• If the parking spans overnight (past midnight), an additional $10 overnight fee is applied.
• There is a minimum fee of $5 (only used if the total would be less than $5).
Return the total cost in the format "$cost", "$5" for example. """

import math
def calculate_parking_fee(park_time, pickup_time):
    parkt=int(park_time[0:2])*60+int(park_time[3:5])
    pickt=int(pickup_time[0:2])*60+int(pickup_time[3:5])
    total=0;
    if parkt>pickt:
        diff=math.ceil((24*60-(parkt-pickt))/60);
        total+=10;
    else:
         diff=math.ceil((pickt-parkt)/60);
    if diff>1:
       total+=3*diff
    else:
        total=5
    return "$"+str(total)

""" 14-03-2026: Pi Day

Happy pi (π) day!
Given an integer (n), where n is between 1 and 1000 (inclusive), return the nth decimal of π.
• Make sure to return a number not a string.
π with its first five decimals is 3.14159. So given 5 for example, return 9, the fifth decimal.
You may have to find the first 1000 decimals of π somewhere. """

p="31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989"
                           
def get_pi_decimal(n):
    return int(p[n])

""" 15-03-2026: Captured Chess Pieces

Given an array of strings representing chess pieces you still have on the board, calculate the value of the pieces your opponent has captured.
In chess, you start with 16 pieces:
Piece    Abbreviation   Quantity   Value
Pawn             "P"                 8             1
Rook              "R"                 2             5
Knight           "N"                 2             3
Bishop          "B"                  2             3
Queen           "Q"                 1             9
King               "K"                 1             0
• The given array will only contain the abbreviations above.
• Any of the 16 pieces not included in the given array have been captured.
• Return the total value of all captured pieces, unless...
• If the King has been captured, return "Checkmate". """

def get_captured_value(pieces):
    v={"P":1,"R":5,"N":3,"B":3,"Q":9,"K":0}
    sn=39
    if "K" not in pieces:
        return "Checkmate"
    else:
        for el in pieces:
            sn-=v[el]
    return sn

""" 16-03-2026: Evenly Divisible

Given two integers, determine if you can evenly divide the first one by the second one. """

def is_evenly_divisible(a, b):
    return a%b==0
