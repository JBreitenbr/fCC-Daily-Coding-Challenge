""" 01-04-2026: Prank Number

Given an array of numbers where all but one number follow a pattern, return a new array with the one number that doesn't follow the pattern fixed.
The pattern will be one of:
• The numbers increase from one to the next by a fixed amount (addition).
• The numbers decrease from one to the next by a fixed amount (subtraction).
For example, given [2, 4, 7, 8, 10] return [2, 4, 6, 8, 10]. """

def freq(arr):
    d={}
    for i in range(len(arr)):
        if arr[i] in d.keys():
            d[arr[i]]+=1
        else:
            d[arr[i]]=1
    return d

def fix_prank_number(arr):
    d=[]
    desc=False
    if arr[0]>=arr[-1]:
       desc=True
    s=sorted(arr,reverse=desc)
    for i in range(1,len(s)):
        d.append(s[i]-s[i-1])
    res = max(freq(d), key=freq(d).get)
    c=(arr[1]-arr[0])==res
    for i in range(len(s)):
        s[i]=s[0]+i*res
    if desc and not c and arr[1]!=arr[0]:
        for i in range(len(s)):
            s[i]-=res
    if not desc and not c:
        for i in range(len(s)):
            s[i]+=res
    return s

""" 02-04-2026: Capitalized Fibonacci

Given a string, return a new string where each letter is capitalized if its index is a Fibonacci number, and lowercased otherwise.
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
• The first character is at index 0.
• If the index of non-letter characters is a Fibonacci number, leave it unchanged.
"""

def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def capitalize_fibonacci(s):
    fibi=[0]
    for i in range(1,16):
        fibi.append(fibo(i))
    res=""
    for i in range(len(s)):
        if i in fibi:
            res+=s[i].upper()
        else:
            res+=s[i].lower()
    return res

""" 03-04-2026: Browser History

Given an array of browser commands, return an array with two values: the history as an array of URLs, and the index of the current page.
Valid commands are:
• "URL" - Where URL is a web address ("freecodecamp.org" for example). Navigates to the given URL, adds it to the history at the next position, and discards any forward history.
• "Back" - moves to the previous page in history, or stays on the current page if there isn't one.
• "Forward" - moves to the next page in history, or stays on the current page if there isn't one.
For example, given ["freecodecamp.org", "freecodecamp.org/learn", "Back"], return [["freecodecamp.org", "freecodecamp.org/learn"], 0]. """

class BrowserHistory:
    def __init__(self): 
        self.backStack = []
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

def get_browser_history(c):
    sn=0
    bf=["Back","Forward"]
    if c[-1]=="Forward" and c[-2] not in bf:
        c=c[0:-1]
    for i in range(1,len(c)):
        if not c[i] in bf:
           sn+=1
        if c[i]=="Back":
               sn-=1
        if c[i]=="Forward":
               sn+=1
    h=BrowserHistory()
    for i in range(len(c)):
        if not c[i] in bf:
                h.visit(c[i])
        if c[i]=="Back":
                h.back(1)
        if c[i]=="Forward":
                h.forward(1)
    res=[]
    res.append(h.backStack+h.forwardStack)
    res.append(max(sn,0))
    return res

""" 04-04-2026: Equation Validation

Given a string representing a math equation, determine whether it is correct.
• The left side may contain up to three positive integers and the operators +, -, *, and /.
• The equation will be given in the format: "number operator number = number" (with two or three numbers on the left). For example: "2 + 2 = 4" or "2 + 3 - 1 = 4".
• The right side will always be a single integer.
Follow standard order of operations: multiplication and division are evaluated before addition and subtraction, from left-to-right. """

def is_valid_equation(equation):
    sp=equation.split("=")
    return eval(sp[0])==int(sp[1])

""" 05-04-2026: Digit Rotation Escape 

Given a positive integer, determine if it, or any of its rotations, is evenly divisible by its digit count.
A rotation means to move the first digit to the end. For example, after 1 rotation, 123 becomes 231.
• Check rotation 0 (the given number) first.
• Given numbers won't contain any zeros.
• Return the first rotation number if one is found, or "none" if not. """

def rotations(stri):
    rots=[stri]
    for i in range(1,len(stri)):
        rot=rots[i-1][1:]+rots[i-1][0]
        rots.append(rot)
    return rots

def get_rotation(n):
    rots=rotations(str(n))
    for i in range(len(rots)):
        if int(rots[i])%len(str(n))==0:
            return i
    return "none"

""" 06-04-2026: What Day Is It?

Given a Unix timestamp in milliseconds, return the day of the week.
Valid return days are:
• "Sunday"
• "Monday"
• "Tuesday"
• "Wednesday"
• "Thursday"
• "Friday"
• "Saturday"
Be sure to ignore time zones. """

import datetime
import time
def get_day_of_week(timestamp):
    days={0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
    t = time.time()
    d = datetime.date.fromtimestamp(timestamp/1000);
    return days[d.weekday()]

""" 07-04-2026 Palindrome Characters

Given a string, determine if it's a palindrome and return the middle character (if it's odd length) or middle two characters (if it's even).
• A palindrome is a string that is the same forward and backward.
• If it's not a palindrome, return "none". """

def palindrome_locator(s):
    c=s[::-1]==s
    if not c:
        return "none"
    if len(s)%2==1:
        v=s[int((len(s)-1)/2)]
    else:
        v=s[int(len(s)/2-1):int(len(s)/2+1)]
    return v

""" 08-04-2026: FizzBuzz Validator

Given an array of sequential integers, with multiples of 3 and 5 replaced, determine if it's a valid FizzBuzz sequence.
In a valid FizzBuzz sequence:
• Multiples of 3 are replaced with "Fizz".
• Multiples of 5 are replaced with "Buzz".
• Multiples of both 3 and 5 are replaced with "FizzBuzz".
• All other numbers remain as integers. """

def is_fizz_buzz(arr):
    c=[arr[0]]
    for i in range(1,len(arr)):
        if not isinstance(arr[i],int):
            if isinstance(arr[i-1],int):
                c.append(arr[i-1]+1)
            elif isinstance(arr[i+1],int):
                c.append(arr[i+1]-1)      
            else: c.append(arr[i])
        else: c.append(arr[i])
    m=[]
    for i in range(len(c)):
        if not isinstance(c[i],int):
            m.append(c[i])
        elif isinstance(c[i],int):
            if c[i]%3==0 and c[i]%5!=0:
                m.append("Fizz")
            elif c[i]%3!=0 and c[i]%5==0:
                m.append("Buzz")
            elif c[i]%3==0 and c[i]%5==0:
                m.append("FizzBuzz")
            else:
                m.append(c[i])
    return m==arr
