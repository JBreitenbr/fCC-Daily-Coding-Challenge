/* 01-08-2026:  Magic Square Solver
Given a 3x3 grid with one missing number (represented as 0), return the missing number that completes the magic square, or "impossible" if no valid number exists.
A magic square is a grid where every row, column, and diagonal adds up to the same number. */

function trans(mat){
  return mat[0].map((item,index)=>mat.map((item)=>item[index]));
}

function solveMagicSquare(grid) {
  let m1=Array.from(new Set(grid.map((item)=>item.reduce((a,b)=>a+b,0))));
  let m2=Array.from(new Set(trans(grid).map((item)=>item.reduce((a,b)=>a+b,0))));
  if(m1.length>2||m2.length>2) {return "impossible";}
  else {
   let s=Math.max(...m1);
   let t=grid.map((item,index)=>item.includes(0)?index:"x").filter((item)=>item!="x")[0];
   return s-grid[t].reduce((a,b)=>a+b,0);
  }
}

/* 02-08-2026: Food Chain
Given an array of [predator, prey] pairs, return the food chain from the apex predator down to the bottom.
• The apex predator is the animal that is never prey to another animal.
• Return the chain as an array of strings. */

function getFoodChain(pairs) {
  if(pairs.length==1) return pairs[0];
  let res=[];
  let fl=pairs.flat();
  for(let i=0;i<pairs.length;i++){
   if(fl.filter((item)=>item==pairs[i][0]).length==1){
    res.push(pairs[i]);
   };
}
  
function conn(j){
  for(let i=0;i<pairs.length;i++){
  if(res[res.length-1][1]==pairs[i][0]){
   res.push(pairs[i]);
  }
 }
}
  
for(let j=0;j<pairs.length;j++){
  conn(j);
}
 return Array.from(new Set(res.flat()));
}

/* 03-08-2026: Emoji Translator
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


Return the words separated by spaces. */

function getEmojiPhrase(str) {
  let emojis={"👶":"baby","🐱":"cat","🐕":"dog","🐟":"fish","🥵":"hot","🧊":"ice","🪨":"rock","🦈":"shark","🍲":"soup","⭐":"star"};
  return Array.from(str).map((item)=>emojis[item]).join(" ");
}

/* 04-08-2026: Golf Handicap Calculator
Given an array of golf scores and a corresponding array of course par values, return the golfer's handicap index using the following method:
• Calculate the differential for each round by subtracting the par from the score, then return the average of all differentials rounded to one decimal place. */

function calculateHandicap(scores, pars) {
  return Math.round(10*[...scores,...pars].map((item,index)=>index<scores.length?(scores[index]-pars[index]):0).reduce((a,b)=>a+b,0)/scores.length)/10;
}

/* 05-08-2016: Spoken Duration
Given a number of seconds, return the duration in spoken English.
• Break the duration into hours, minutes, and seconds.
• Skip any zero values.
• Use singular or plural as appropriate ("1 hour", "2 hours").
• If present, join the last two units with "and", and the second and third to last units with a comma ("1 hour, 2 minutes and 3 seconds").*/

function getSpokenDuration(seconds) {
  let hrs=Math.floor(seconds/3600);
  let mins=Math.floor((seconds-hrs*3600)/60);
  let secs=seconds-hrs*3600-mins*60;
  let arr=[hrs,mins,secs].map((item)=>item).map((item,index)=>[item,index]).filter((item)=>item).map((item,index)=>[item[0],index==0?" hour":index==1?" minute":" second",item[0]>1?"s":""]).filter((item)=>item[0]!=0).map((item)=>item.join(""));
  return arr.length==1?arr[0]:arr.length==2?arr[0]+" and "+arr[1]:arr[0]+", "+arr[1]+" and "+arr[2];
}

/* 06-08-2026: Spoken Time
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
Note: Hand angles may not land exactly on a number, consider rounding them somehow. */

function getSpokenTime(hourAngle, minuteAngle) {
  let arr=[hourAngle/360*12,Math.floor(minuteAngle/360*60)];
  return arr[1]==0?arr[0]+" o'clock":arr[1]==15?"quarter past "+Math.floor(arr[0]):arr[1]==30?"half past "+Math.floor(arr[0]):arr[1]==45?"quarter to "+Math.ceil(arr[0]):arr[1]>=1 && arr[1]<=29 && arr[1]!=15?arr[1]+" minutes past "+Math.floor(arr[0]):(60-arr[1])+" minutes to "+Math.ceil(arr[0]);
}


/* 07-08-2026: Nonogram Validator
Given an array of clue numbers and an array of cells, determine whether the cells satisfy the nonogram clue.
• The clue is an array of numbers representing the lengths of consecutive filled cells, in order. For example, a clue of [3, 2] means there should be 3 consecutive filled cells followed by 2 consecutive filled cells, separated by at least one empty cell.
• The row is an array of 1s (filled) and 0s (empty). */

function isEqual(arr1,arr2){
  if(arr1.length!=arr2.length)return false;
  for(let i=0;i<arr1.length;i++){
    if(arr1[i]!=arr2[i]){
     return false;
   }
 }
  return true;
}

function isValidNonogram(clue, cells) {
  let sn=0;
  let res=[];
  for(let i=0;i<cells.length;i++){
  if(cells[i]==1){sn+=1;
  if(cells[i+1]==0||i==cells.length-1){
  res.push(sn);}
 } if(cells[i]==0){sn=0;}
}
  return isEqual(res,clue);
}

/* 08-08-2026: Bucket Fill 2
Given a 2D grid of single-letter color strings and a target color, return the minimum number of flood fill "clicks" needed to make the entire grid the target color.
• Each click changes the clicked cell's color and the entire region of connected cells of the same color with the target color.
• Cells are connected horizontally and vertically (not diagonally). */

function bucketFill(grid, targetColor) {
  let gridClone = structuredClone(grid);
  
  function changeRegion(x,y,color){
    if (x < 0 || x >= gridClone.length || y < 0 || y >= gridClone[x].length) return;
     if (gridClone[x][y] === color) {
      gridClone[x][y] = targetColor;
      changeRegion(x - 1, y, color); 
      changeRegion(x + 1, y, color); 
      changeRegion(x, y - 1, color); 
      changeRegion(x, y + 1, color); 
     }
    }
   let clicks = 0;
   for (let i = 0; i < gridClone.length; i++) {
     for (let j = 0; j < gridClone[i].length; j++) {
     const cellColor = gridClone[i][j];
    if (cellColor === targetColor) continue;
    clicks++;
    changeRegion(i, j, cellColor);
   }
  }
  return clicks;
}


/* 09-08-2026: Between Two Buckets
Given two buckets of paint, each with an RGB color and a fullness level, return the mixed RGB color as an array of three integers.
• Each bucket is an object (JavaScript) or dictionary (Python) with a color property (an array of three integers [r, g, b]) and a fullness property (0–100).
• The mixed color is a weighted average of each channel in the two colors based on fullness level, with each channel rounded to the nearest integer. */

function mixPaint(bucket1, bucket2) {
  let m=[bucket1,bucket2].map((item)=>[item.color,item.fullness]).map((item)=>item[0].map((sub)=>sub*item[1]/100)).flat();
  let rel=100/(bucket1.fullness+bucket2.fullness);
  return [Math.round((m[0]+m[3])*rel),Math.round((m[1]+m[4])*rel),Math.round((m[2]+m[5])*rel)];
}

/* 10-08-2026: The Last Challenge: Bucket Fill 3
Today marks a year of daily coding challenges. This is the last new one for now. Good luck!
Given a 2D grid of single-letter color strings and a target color, return the minimum number of flood fill "clicks" needed to make the entire grid that color.
• Each click changes the clicked cell's color and the entire region of connected cells of the same color (4-directional).
• Clicks can use any color as an intermediate step, not just the target color. */

/* 11-08-2026: Vowel Balance
Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.
• The string can contain any characters.
• The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
• If there's an odd number of characters in the string, ignore the center character. */

function isBalanced(s) {
  let reg=/[aeiou]/gi;
  let l=s.length;
  let b=Math.floor(l/2);
  let p1=s.slice(0,b);
  let p2=l%2==1?s.slice(b+1):s.slice(b);
  let m1=p1.match(reg);
  let m2=p2.match(reg);
  return m1==null && m2!=null || m1!=null && m2==null?false:m1==null&&m2==null?true:m1.length==m2.length;
}

/* 12-08-2026: Base Check
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
◦ Base 36: 0-9 and A-Z */

function isValidNumber(n, base) {
  let l=n.length;
  let r1=/[0-9A-Z]/gi;
  let r2=/[0-9A-F]/gi;
  let r3=/[0-9]/gi;
  let r4=/[0-7]/gi;
  let r5=/[0-1]/gi;
  let m1=n.match(r1);
  let m2=n.match(r2);
  let m3=n.match(r3);
  let m4=n.match(r4);
  let m5=n.match(r5);
  return base>16?r1.test(n)&&m1.length==l:base>10?r2.test(n)&&m2.length==l:base>8?r3.test(n)&&m3.length==l:base>2?r4.test(n)&&m4.length==l:r5.test(n)&&m5.length==l;
}

/* 13-08-2026: Fibonacci Sequence
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. When starting with 0 and 1, the first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
Given an array containing the first two numbers of a Fibonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.
• Your function should handle sequences of any length greater than or equal to zero.
• If the length is zero, return an empty array.
• Note that the starting numbers are part of the sequence. */

function fibonacciSequence(startSeq, length) {
  if(length==0) return [];
  if(length==1) return [startSeq[0]];
  let res=[startSeq[0],startSeq[1]];
  for(let i=2;i<length;i++){
   res.push(res[i-2]+res[i-1]);
  }
  return res;
}

/* 14-08-2026: S P A C E J A M
Given a string, remove all spaces from the string, insert two spaces between every character, convert all alphabetical letters to uppercase, and return the result.
• Non-alphabetical characters should remain unchanged (except for spaces). */

function spaceJam(s) {
  return s.replaceAll(" ","").split("").map((item)=>item.toUpperCase()).join(" ");
}

/* 15-08-2026: Jbelmud Text
Given a string, return a jumbled version of that string where each word is transformed using the following constraints:
• The first and last letters of the words remain in place
• All letters between the first and last letter are sorted alphabetically.
• The input strings will contain no punctuation, and will be entirely lowercase. */

function jbelmu(text) {
  return text.split(" ").map((item)=>item.length==1?item:item[0]+item.slice(1,item.length-1).split("").sort().join("")+item[item.length-1]).join(" ");
}

/* 16-08-2026: Anagram Checker
Given two strings, determine if they are anagrams of each other (contain the same characters in any order).
• Ignore casing and white space. */

function areAnagrams(str1, str2) {
  let s1=str1.replaceAll(" ","").toLowerCase().split("").sort().join("");
  let s2=str2.replaceAll(" ","").toLowerCase().split("").sort().join("");
  for(let i=0;i<s1.length;i++){
    if(s1[i]!=s2[i]) return false;
  }
  return true;
}

/* 17-08-2026: Targeted Sum
Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value. Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.
• The returned array should have the indices in ascending order. */
function findTarget(arr, target) {
  let pairs=[];
  for(let i=0;i<arr.length;i++){
   for(let j=i+1;j<arr.length;j++){
    pairs.push([arr[i],arr[j]]);
    }
   }
  let flt=pairs.filter((item)=>item[0]+item[1]==target);
  return flt.length==0?"Target not found":[arr.indexOf(flt[0][0]),arr.indexOf(flt[0][1])];
}

/* 18-08-2026: Factorializer
Given an integer from zero to 20, return the factorial of that number. The factorial of a number is the product of all the numbers between 1 and the given number.
• The factorial of zero is 1. */

function factorial(n) {
  return n==0||n==1?1:n*factorial(n-1);
}

/* 19-08-2026: Sum of Squares
Given a positive integer up to 1,000, return the sum of all the integers squared from 1 up to the number. */

function sumOfSquares(n) {
  return Array.from(Array(n).keys()).map((item)=>(item+1)*(item+1)).reduce((a,b)=>a+b,0);
}

/* 20-08-2026: 3 Strikes
Given an integer between 1 and 10,000, return a count of how many numbers from 1 up to that integer whose square contains at least one digit 3. */

function squaresWithThree(n) {
  return Array.from(Array(n).keys()).map((item)=>((item+1)*(item+1)).toString()).filter((item)=>item.includes("3")).length ;
}

