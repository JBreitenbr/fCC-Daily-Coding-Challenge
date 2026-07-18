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
""" 05-07-2026: Bucket Fill
Given a 2D grid, a starting position ([row, col]), and a new value, replace the value at the starting position and all connected cells of the same value with the new value.
• Cells are connected if they are adjacent horizontally or vertically (not diagonally).
Return the updated grid. """
""" 06-07-2026: lowercase words
Given a string, return only the words that are entirely lowercase, in their original order and with a space between each word. """

""" 07-07-2026: Nearest Multiple
Given two integers, round the first to the nearest multiple of the second. """
""" 08-07-2026: Issue Triage
Given a number of milliseconds since the last post on an issue, and the last message posted on the issue, determine what you should do with the issue according to these rules:
• If the last message is less than 7 days ago, return "leave it"
• If the last message is 7 or more days ago and its content contains "bump" (case-insensitive), return "close it"
• Otherwise, return "bump it" """
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

""" 10-07-2026: Exact Change
Given an integer amount in cents, return the number of distinct ways to make exact change using pennies (1 cent), nickels (5 cents), dimes (10 cents), and quarters (25 cents). """
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
""" 13-07-2026: Tally Counter
Given a string of tally marks, return the total count represented.
• Each pipe "|" represents one count.
• Every fifth mark is represented as a forward slash "/", completing a group of five ("||||/").
• Groups are separated by a space. """

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
