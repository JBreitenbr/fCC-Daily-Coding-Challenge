
""" 01-08-2026:  Magic Square Solver
Given a 3x3 grid with one missing number (represented as 0), return the missing number that completes the magic square, or "impossible" if no valid number exists.
A magic square is a grid where every row, column, and diagonal adds up to the same number. """

def transp(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def solve_magic_square(grid):
    m1=list(set([sum(grid[i]) for i in range(len(grid))]))
    m2=list(set([sum(transp(grid)[i]) for i in range(len(grid))]))
    if len(m1)>2 or len(m2)>2:
        return "impossible"
    s=max(m1)
    r=sum([el for el in grid if 0 in el][0])
    return s-r
  
""" 02-08-2026: Food Chain
Given an array of [predator, prey] pairs, return the food chain from the apex predator down to the bottom.
• The apex predator is the animal that is never prey to another animal.
• Return the chain as an array of strings. """
""" 03-08-2026: Emoji Translator
Given a string of emojis, return the phrase using the following table:

Emoji
Word

👶
"baby"

🐱
"cat"

🐕
"dog"

🐟
"fish"

🥵
"hot"

🧊
"ice"

🪨
"rock"

🦈
"shark"

🍲
"soup"

⭐
"star"


Return the words separated by spaces. """

""" 04-08-2026: Golf Handicap Calculator
Given an array of golf scores and a corresponding array of course par values, return the golfer's handicap index using the following method:
• Calculate the differential for each round by subtracting the par from the score, then return the average of all differentials rounded to one decimal place. """
""" 05-08-2016: Spoken Duration
Given a number of seconds, return the duration in spoken English.
• Break the duration into hours, minutes, and seconds.
• Skip any zero values.
• Use singular or plural as appropriate ("1 hour", "2 hours").
• If present, join the last two units with "and", and the second and third to last units with a comma ("1 hour, 2 minutes and 3 seconds")."""

""" 06-08-2026: Spoken Time
Given the angles for the hour and minute hands of an analog clock in degrees (clockwise from 12), return the time in spoken English.
Convert the minute hand angle to minutes (360° = 60 minutes), then use the following rules:

Minutes
Spoken

0
"Y o'clock"

15
"quarter past Y"

1–29 (excluding 15)
"X minutes past Y"

30
"half past Y"

45
"quarter to Z"

31–59 (excluding 45)
"X minutes to Z" (where X is 60 - minutes)


Where Y is the current hour and Z is the next hour, both derived from the hour hand angle (360° = 12 hours).
Note: Hand angles may not land exactly on a number, consider rounding them somehow. """


""" 07-08-2026: Nonogram Validator
Given an array of clue numbers and an array of cells, determine whether the cells satisfy the nonogram clue.
• The clue is an array of numbers representing the lengths of consecutive filled cells, in order. For example, a clue of [3, 2] means there should be 3 consecutive filled cells followed by 2 consecutive filled cells, separated by at least one empty cell.
• The row is an array of 1s (filled) and 0s (empty). 
""" 08-08-2026: Bucket Fill 2
Given a 2D grid of single-letter color strings and a target color, return the minimum number of flood fill "clicks" needed to make the entire grid the target color.
• Each click changes the clicked cell's color and the entire region of connected cells of the same color with the target color.
• Cells are connected horizontally and vertically (not diagonally). """

""" 09-08-2026: Between Two Buckets
Given two buckets of paint, each with an RGB color and a fullness level, return the mixed RGB color as an array of three integers.
• Each bucket is an object (JavaScript) or dictionary (Python) with a color property (an array of three integers [r, g, b]) and a fullness property (0–100).
• The mixed color is a weighted average of each channel in the two colors based on fullness level, with each channel rounded to the nearest integer. """
""" 10-08-2026: The Last Challenge: Bucket Fill 3
Today marks a year of daily coding challenges. This is the last new one for now. Good luck!
Given a 2D grid of single-letter color strings and a target color, return the minimum number of flood fill "clicks" needed to make the entire grid that color.
• Each click changes the clicked cell's color and the entire region of connected cells of the same color (4-directional).
• Clicks can use any color as an intermediate step, not just the target color. """
""" 11-08-2026: Vowel Balance
Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.
• The string can contain any characters.
• The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
• If there's an odd number of characters in the string, ignore the center character. """
""" 12-08-2026: Base Check
Given a string representing a number, and an integer base from 2 to 36, determine whether the number is valid in that base.
• The string may contain integers, and uppercase or lowercase characters.
• The check should be case-insensitive.
• The base can be any number 2-36.
• A number is valid if every character is a valid digit in the given base.
• Example of valid digits for bases:
◦ Base 2: 0-1
◦ Base 8: 0-7
◦ Base 10: 0-9
◦ Base 16: 0-9 and A-F
◦ Base 36: 0-9 and A-Z """
