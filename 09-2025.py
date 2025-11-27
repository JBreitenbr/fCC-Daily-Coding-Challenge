""" 01-09-2025: Tribonacci Sequence
The Tribonacci sequence is a series of numbers where each number is the sum of the three preceding ones. When starting with 0, 0 and 1, the first 10 numbers in the sequence are 0, 0, 1, 1, 2, 4, 7, 13, 24, 44.

Given an array containing the first three numbers of a Tribonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.

Your function should handle sequences of any length greater than or equal to zero.
If the length is zero, return an empty array.
Note that the starting numbers are part of the sequence.
"""

def tribo(n,first,second,third):
    if n==0:
        return first;
    if n==1:
        return second;
    if n==2:
        return third;
    if n>2:
        return tribo(n-1,first,second,third)+tribo(n-2,first,second,third)+tribo(n-3,first,second,third)  

def trib_arr(n,first,second,third):
    targ=[]
    for i in range(n):
        targ.append(tribo(i,first,second,third))
    return targ

def tribonacci_sequence(start_sequence, length):
    if length==0:
        return []
    elif length==1:
        return start_sequence[0:1]
    elif length==2:
        return start_sequence[0:2]
    elif length==3:
        return start_sequence
    else:
        return trib_arr(length,start_sequence[0],start_sequence[1],start_sequence[2])

""" 02-09-2025: RGB to Hex
Given a CSS rgb(r, g, b) color string, return its hexadecimal equivalent.

Here are some example outputs for a given input:

Input	Output
"rgb(255, 255, 255)"	"#ffffff"
"rgb(1, 2, 3)"	"#010203"
Make any letters lowercase.
Return a # followed by six characters. Don't use any shorthand values.
"""

def rgb_to_hex(rgb):
    sp0=rgb.split("rgb")[1][1:-1]
    sp=sp0.split(",")
    return '#%02x%02x%02x'%(int(sp[0]),int(sp[1]),int(sp[2]))
    
""" 03-09-2025: Pangram
Given a word or sentence and a string of lowercase letters, determine if the word or sentence uses all the letters from the given set at least once and no other letters.

Ignore non-alphabetical characters in the word or sentence.
Ignore letter casing in the word or sentence.
"""

def is_pangram(sentence, letters):
    s1=sorted(list(set(sentence.lower())))
    s2=sorted(list(set(letters.lower())))
    stri1=""
    stri2=""
    for i in range(len(s1)):
        if s1[i].isalpha():
            stri1+=s1[i]
    for i in range(len(s2)):
        if s2[i].isalpha():
            stri2+=s2[i]
    return stri1==stri2

""" 04-09-2025: Vowel Repeater
Given a string, return a new version of the string where each vowel is duplicated one more time than the previous vowel you encountered. For instance, the first vowel in the sentence should remain unchanged. The second vowel should appear twice in a row. The third vowel should appear three times in a row, and so on.

The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
The original vowel should keeps its case.
Repeated vowels should be lowercase.
All non-vowel characters should keep their original case.
"""

def propcase(stri):
    return stri[0].upper()+stri[1:].lower()

def repeat_vowels(s):
    v="aeiouAEIOU"
    lst=list(s)
    sn=0
    for i in range(len(lst)):
        if lst[i] in v:
            sn+=1
            if lst[i].isupper():
               lst[i]=propcase(sn*lst[i])
            else:
                lst[i]=sn*lst[i]
    j="".join(lst)
    return j

""" 05-09-2025: IPv4 Validator
Given a string, determine if it is a valid IPv4 Address. A valid IPv4 address consists of four integer numbers separated by dots (.). Each number must satisfy the following conditions:

It is between 0 and 255 inclusive.
It does not have leading zeros (e.g. 0 is allowed, 01 is not).
Only numeric characters are allowed.
"""

def is_valid_ipv4(ipv4):
    sp=ipv4.split(".")
    for i in range(len(sp)):
        if sp[i]=="":
            return False
        if int(sp[i])<0 or int(sp[i])>255:
            return False
        if sp[i][0]=="0" and len(sp[i])>1:
            return False
    return True

""" 06-09-2025: Matrix Rotate
Given a matrix (an array of arrays), rotate the matrix 90 degrees clockwise and return it. For instance, given [[1, 2], [3, 4]], which looks like this:

1	2
3	4
You should return [[3, 1], [4, 2]], which looks like this:

3	1
4	2
"""

def rotate(matrix):
    m=matrix[::-1]
    res=[]
    for i in range(len(m[0])):
        res.append([])
        for j in range(len(m)):           
            
            res[i].append(m[j][i])
    return res

""" 07-09-2025: Roman Numeral Parser
Given a string representing a Roman numeral, return its integer value.

Roman numerals consist of the following symbols and values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Numerals are read left to right. If a smaller numeral appears before a larger one, the value is subtracted.
Otherwise, values are added.
"""

def parse_roman_numeral(numeral):
    vals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M': 1000}
    res=0
    prev=0
    curr=0
    sp=list(numeral[::-1])
    for el in sp:
        curr=vals[el]
        if curr>=prev:
            res+=curr
        else:
            res-=curr
        prev=curr
    return res

""" 08-09-2025: Acronym Builder
Given a string containing one or more words, return an acronym of the words using the following constraints:

The acronym should consist of the first letter of each word capitalized, unless otherwise noted.
The acronym should ignore the first letter of these words unless they are the first word of the given string: a, for, an, and, by, and of.
The acronym letters should be returned in order they are given.
The acronym should not contain any spaces.
"""
def build_acronym(s):
    st_w=["a", "for", "an", "and", "by", "of"]
    res=[]
    sp=s.split(" ")
    for el in sp:
        if not el in st_w:
            res.append(el.upper()[0])
    return "".join(res)

""" 09-09-2025: Unique Characters
Given a string, determine if all the characters in the string are unique.

Uppercase and lowercase letters should be considered different characters.
"""

def all_unique(s):
    st=list(set(s))
    return len(list(s))==len(st)

""" 10-09-2025: Array Diff
Given two arrays with strings values, return a new array containing all the values that appear in only one of the arrays.

The returned array should be sorted in alphabetical order.
"""

def array_diff(arr1, arr2):
    res=[]
    for el in arr1:
        if not el in arr2:
            res.append(el)
    for el in arr2:
        if not el in arr1:
            res.append(el)
    return sorted(res)

""" 11-09-2025: Reverse Sentence
Given a string of words, return a new string with the words in reverse order. For example, the first word should be at the end of the returned string, and the last word should be at the beginning of the returned string.

In the given string, words can be separated by one or more spaces.
The returned string should only have one space between words.
"""

def reverse_sentence(sentence):
    sp=sentence.split(" ")
    res=[]
    for i in range(len(sp)):
        if sp[len(sp)-i-1]!="":
           res.append(sp[len(sp)-i-1])
    return " ".join(res)

""" 12-09-2025: Screen Time
Given an input array of seven integers, representing a week's time, where each integer is the amount of hours spent on your phone that day, determine if it is too much screen time based on these constraints:

If any single day has 10 hours or more, it's too much.
If the average of any three days in a row is greater than or equal to 8 hours, it’s too much.
If the average of the seven days is greater than or equal to 6 hours, it's too much.
"""
from functools import reduce
def too_much_screen_time(h):
    av=[]
    for i in range(len(h)-2):
        av.append(1/3*(h[i]+h[i+1]+h[i+2]))
    r=reduce(lambda x,y:x+y,h)/len(h)
    if r>=6:
        return True
    for i in range(len(h)):
        if h[i]>=10:
            return True
    for i in range(len(av)):
        if av[i]>=8:
            return True
    return False

""" 13-09-2025: Missing Numbers
Given an array of integers from 1 to n, inclusive, return an array of all the missing integers between 1 and n (where n is the largest number in the given array).

The given array may be unsorted and may contain duplicates.
The returned array should be in ascending order.
If no integers are missing, return an empty array.
"""

def find_missing_numbers(arr):
    st=sorted(arr)
    rg=list(range(st[0],st[-1]+1))
    m=[]
    for el in rg:
        if not el in arr:
            m.append(el)
    return m

""" 14-09-2025: Word Frequency
Given a paragraph, return an array of the three most frequently occurring words.

Words in the paragraph will be separated by spaces.
Ignore case in the given paragraph. For example, treat Hello and hello as the same word.
Ignore punctuation in the given paragraph. Punctuation consists of commas (,), periods (.), and exclamation points (!).
The returned array should have all lowercase words.
The returned array should be in descending order with the most frequently occurring word first.
"""

def get_words(paragraph):
    al="abcdefghijklmnopqrstuvxyz "
    p0=paragraph.lower()
    p=""
    for i in range(len(p0)):
        if p0[i] in al:
            p+=p0[i]
    d={}
    sp=p.split(" ")
    for el in sp:
        if el not in d.keys():
            d[el]=1
        else:
            d[el]+=1
    st= sorted(d.items(), key=lambda kv: kv[1],reverse=True)
    res=[]
    for i in range(3):
        res.append(st[i][0])
    return res

""" 15-09-2025: Thermostat Adjuster
Given the current temperature of a room and a target temperature, return a string indicating how to adjust the room temperature based on these constraints:

Return "heat" if the current temperature is below the target.
Return "cool" if the current temperature is above the target.
Return "hold" if the current temperature is equal to the target.
"""

def adjust_thermostat(temp, target):
    if temp<target:
        return "heat"
    elif temp>target:
        return "cool"
    else:
        return "hold"

""" 16-09-2025: Sentence Capitalizer
Given a paragraph, return a new paragraph where the first letter of each sentence is capitalized.

All other characters should be preserved.
Sentences can end with a period (.), one or more question marks (?), or one or more exclamation points (!).
"""

def capitalize(p):
    s0=p[0].upper()+p[1:]
    s=list(s0)
    for i in range(2,len(s0)-2):
        if s[i-2]=="." and s[i-1]==" " or s[i-1]=="?" or s[i-1]=="!" or s[i-1]==".":
            s[i]=s[i].upper()
    return "".join(s)

""" 17-09-2025: Slug Generator
Given a string, return a URL-friendly version of the string using the following constraints:

All letters should be lowercase.
All characters that are not letters, numbers, or spaces should be removed.
All spaces should be replaced with the URL-encoded space code %20.
Consecutive spaces should be replaced with a single %20.
The returned string should not have leading or trailing %20.
"""

def generate_slug(str):
    lst=list(str.lower().strip().replace("  "," "))
    res=[]
    for i in range(len(lst)):
        if lst[i].isalpha() or lst[i].isnumeric() or lst[i]==" ":
            res.append(lst[i])
    stri="".join(res).replace(" ","%20")
    return stri

""" 18-09-2025: Fill The Tank
Given the size of a fuel tank, the current fuel level, and the price per gallon, return the cost to fill the tank all the way.

tankSize is the total capacity of the tank in gallons.
fuelLevel is the current amount of fuel in the tank in gallons.
pricePerGallon is the cost of one gallon of fuel.
The returned value should be rounded to two decimal places in the format: "$d.dd".
"""

def cost_to_fill(tank_size, fuel_level, price_per_gallon):
    d=tank_size-fuel_level
    p="$"+str(d*price_per_gallon)
    if p[-2]==".":
        p+="0"
    return p

""" 19-09-2025: Photo Storage
Given a photo size in megabytes (MB), and hard drive capacity in gigabytes (GB), return the number of photos the hard drive can store using the following constraints:

1 gigabyte equals 1000 megabytes.
Return the number of whole photos the drive can store.
"""

import math
def number_of_photos(photo_size_mb, drive_size_gb):
    return math.floor(drive_size_gb*1000/photo_size_mb);

""" 20-09-2025: File Storage
Given a file size, a unit for the file size, and hard drive capacity in gigabytes (GB), return the number of files the hard drive can store using the following constraints:

The unit for the file size can be bytes ("B"), kilobytes ("KB"), or megabytes ("MB").
Return the number of whole files the drive can fit.
Use the following conversions:
Unit	Equivalent
1 B	1 B
1 KB	1000 B
1 MB	1000 KB
1 GB	1000 MB
For example, given 500, "KB", and 1 as arguments, determine how many 500 KB files can fit on a 1 GB hard drive.
"""

import math
def number_of_files(file_size, file_unit, drive_size_gb):
    uObj={"B":1,"KB":1000,"MB":1000000,"GB":1000000000}  
    fS=file_size*uObj[file_unit]
    dS=drive_size_gb*uObj["GB"]
    return math.floor(dS/fS)
    
""" 21-09-2025: Video Storage
Given a video size, a unit for the video size, a hard drive capacity, and a unit for the hard drive, return the number of videos the hard drive can store using the following constraints:

The unit for the video size can be bytes ("B"), kilobytes ("KB"), megabytes ("MB"), or gigabytes ("GB").
If not given one of the video units above, return "Invalid video unit".
The unit of the hard drive capacity can be gigabytes ("GB") or terabytes ("TB").
If not given one of the hard drive units above, return "Invalid drive unit".
Return the number of whole videos the drive can fit.
Use the following conversions:
Unit	Equivalent
1 B	1 B
1 KB	1000 B
1 MB	1000 KB
1 GB	1000 MB
1 TB	1000 GB
For example, given 500, "MB", 100, and "GB" as arguments, determine how many 500 MB videos can fit on a 100 GB hard drive.
"""

import math
def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    uObj={"B":1,"KB":1000,"MB":1000000,"GB":1000000000,"TB":1000000000000}
    vS=video_size*uObj[video_unit]
    dS=drive_size*uObj[drive_unit]
    if not video_unit in ["KB","MB","GB"]:
        return "Invalid video unit"
    if not drive_unit in ["GB","TB"]:
        return "Invalid drive unit"
    return math.floor(dS/vS)

""" 22-09-2025: Digits vs Letters
Given a string, return "digits" if the string has more digits than letters, "letters" if it has more letters than digits, and "tie" if it has the same amount of digits and letters.

Digits consist of 0-9.
Letters consist of a-z in upper or lower case.
Ignore any other characters.
""" 

def digits_or_letters(s):
    d=0
    a=0
    for c in s:
        if c.isdigit():
           d+=1
        if c.isalpha():
           a+=1
    if a>d:
        return "letters"
    elif a<d:
        return "digits"
    else:
        return "tie"

""" 23-09-2025: String Mirror
Given two strings, determine if the second string is a mirror of the first.

A string is considered a mirror if it contains the same letters in reverse order.
Treat uppercase and lowercase letters as distinct.
Ignore all non-alphabetical characters.
"""

def is_mirror(str1, str2):
    a0="abcdefghijklmnopqrstuvwxyz"   
    a=a0+a0.upper()
    stri1=""
    stri2=""
    for i in range(len(str1)):
        if str1[i] in a:
            stri1+=str1[i]
    for i in range(len(str2)):
        if str2[i] in a:
            stri2+=str2[i]
    return stri1==stri2[::-1]

""" 24-09-2025: Perfect Square
Given an integer, determine if it is a perfect square.

A number is a perfect square if you can multiply an integer by itself to achieve the number. For example, 9 is a perfect square because you can multiply 3 by itself to get it.
"""

import math
def is_perfect_square(n):
    if n<0:
        return False
    r=math.sqrt(n)
    f=math.floor(r)
    return f==r

""" 25-09-2025: 2nd Largest
Given an array, return the second largest distinct number.
"""

def second_largest(arr):
    return sorted(list(set(arr)))[-2]

""" 26-09-2025: Caught Speeding
Given an array of numbers representing the speed at which vehicles were observed traveling, and a number representing the speed limit, return an array with two items, the number of vehicles that were speeding, followed by the average amount beyond the speed limit of those vehicles.

If there were no vehicles speeding, return [0, 0].
"""

from functools import reduce
def speeding(speeds, limit):
    flt=[val-limit for val in speeds if val > limit]
    if len(flt)>0:
       av = reduce(lambda x, y: x + y , flt)/len(flt)
       res=[len(flt),float(av)]
    else:
        res=[0,0]
    return res

""" 27-09-2025: Spam Detector
Given a phone number in the format "+A (BBB) CCC-DDDD", where each letter represents a digit as follows:

A represents the country code and can be any number of digits.
BBB represents the area code and will always be three digits.
CCC and DDDD represent the local number and will always be three and four digits long, respectively.
Determine if it's a spam number based on the following criteria:

The country code is greater than 2 digits long or doesn't begin with a zero (0).
The area code is greater than 900 or less than 200.
The sum of first three digits of the local number appears within last four digits of the local number.
The number has the same digit four or more times in a row (ignoring the formatting characters).
"""
from functools import reduce
def is_spam(number):
    sp=number.split(" ")
    a=int(sp[1][1:-1])
    l1=list((sp[2].split("-")[0]))
    l2=sp[2].split("-")[1]
    r=str(reduce(lambda x,y:int(x)+int(y),l1))
    for c in list("123456789"):
        spli=number.split(c)
        if len(spli)>4:
            return True
    if r in l2:
        return True
    if a<200 or a>900:
        return True
    if len(sp[0][1:])>2 or sp[0][1]!="0":
        return True
    return False

""" 28-09-2025: CSV Header Parser
Given the first line of a comma-separated values (CSV) file, return an array containing the headings.

The first line of a CSV file contains headings separated by commas.
Remove any leading or trailing whitespace from each heading.
"""

def get_headings(csv):
    sp=csv.split(",")
    res=[]
    for w in sp:
        res.append(w.strip())
    return res

""" 29-09-2025: Longest Word
Given a sentence, return the longest word in the sentence.

Ignore periods (.) when determining word length.
If multiple words are ties for the longest, return the first one that occurs.
"""

def get_longest_word(sentence):
    s=sentence.replace(".","")
    sp=s.split(" ")
    maxi=sp[0]
    for i in range(len(sp)):
        if len(sp[i])>len(maxi):
            maxi=sp[i]
    return maxi

""" 30-09-2025: Phone Number Formatter
Given a string of ten digits, return the string as a phone number in this format: "+D (DDD) DDD-DDDD".
"""

def format_number(n):
    return "+"+n[0]+" ("+n[1:4]+") "+n[4:7]+"-"+n[7:]
