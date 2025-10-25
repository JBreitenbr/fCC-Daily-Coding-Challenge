/* 11-08-2025: Vowel Balance
Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.

The string can contain any characters.
The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
If there's an odd number of characters in the string, ignore the center character. */

function isBalanced(s) {
  let v="aeiou";
  let str=s.toLowerCase();
  let l=str.length;
  let s1=str.slice(0,Math.floor(l/2)).split("");
  let s2=str.slice(Math.ceil(l/2)).split("");
  let sum1=0;
  let sum2=0;
  for(let i=0;i<s1.length;i++){
    if(v.includes(s1[i])){
      sum1+=1;
    }
  }
  for(let i=0;i<s2.length;i++)
  {
    if(v.includes(s2[i])){
      sum2+=1;
    }
  }
  return sum1==sum2;
      }

/* 12-08-2025: Base Check
Given a string representing a number, and an integer base from 2 to 36, determine whether the number is valid in that base.

The string may contain integers, and uppercase or lowercase characters.
The check should be case-insensitive.
The base can be any number 2-36.
A number is valid if every character is a valid digit in the given base.
Example of valid digits for bases:
Base 2: 0-1
Base 8: 0-7
Base 10: 0-9
Base 16: 0-9 and A-F
Base 36: 0-9 and A-Z */

function isValidNumber(n, base) {
  let m=n.toUpperCase().split("").sort();
  let last=m[m.length-1];
  if(base<16){
    if(last<base)
    return true;
    else return false;
  }
  else if(base==16){
    if(last<"G") return true;
    else return false;
  }
  else return true;
}

/* 13-08-2025: Fibonacci Sequence
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. When starting with 0 and 1, the first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

Given an array containing the first two numbers of a Fibonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.

Your function should handle sequences of any length greater than or equal to zero.
If the length is zero, return an empty array.
Note that the starting numbers are part of the sequence.*/

function fibo(n,first,second) {
     if(n==0){
       return first;
      }
     if(n==1){
       return second;
      }
     if(n>1){
        return fibo(n-1,first,second)+fibo(n-2,first,second);
     }
}

function fibArr(n,first,second){
  let targ=[];
  for(let i=0;i<n;i++){
    targ.push(fibo(i,first,second));
  }
  return targ;
}

function fibonacciSequence(startSequence, length) {
  if(length==0)
  { return [];}
  else if(length==1){
    return startSequence.slice(0,1);
  }
  else if(length==2){
    return startSequence;
  }
  else return fibArr(length,startSequence[0],startSequence[1]);
    }

/* 14-08-2025: S P A C E J A M
Given a string, remove all spaces from the string, insert two spaces between every character, convert all alphabetical letters to uppercase, and return the result.

Non-alphabetical characters should remain unchanged (except for spaces). */

function spaceJam(s) {
  let cap=s.toUpperCase().split("").filter((item)=>item!=" ").join("");
  let targ="";
  for(let i=0;i<cap.length;i++){
    targ+=cap[i];
    targ+="  ";
  }
  let res=targ.split("").slice(0,targ.length-2).join("");
  return res;
}

/* 15-08-2025: Jbelmud Text
Given a string, return a jumbled version of that string where each word is transformed using the following constraints:

The first and last letters of the words remain in place
All letters between the first and last letter are sorted alphabetically.
The input strings will contain no punctuation, and will be entirely lowercase. */

function jbelmu(text) {
  let spli=text.split(" ");
  let targ=[];
  for(let i=0;i<spli.length;i++){ 
      let f=spli[i][0];
      let l=spli[i][spli[i].length-1];
      let m=spli[i].slice(1,spli[i].length-1).split("").sort().join("");
      let c;
      if(spli[i].length==1){
        c=f;
      }  else {c=f+m+l} ;
      targ.push(c);
  }
  return targ.join(" ");
        }

/* 16-08-2025: Anagram Checker
Given two strings, determine if they are anagrams of each other (contain the same characters in any order).
Ignore casing and white space. */

function areAnagrams(str1, str2) {
  let stri1=str1.toLowerCase().split("").sort().join("");
  let stri2=str2.toLowerCase().split("").sort().join("");
  return stri1===stri2;
}

/* 17-08-2025: Targeted Sum
Given an array of numbers and an integer target, find two unique numbers in the array that add up to the target value. 
Return an array with the indices of those two numbers, or "Target not found" if no two numbers sum up to the target.
The returned array should have the indices in ascending order. */

function findTarget(arr, target) {
  let res=[];
  for(let i=0;i<arr.length-1;i++){
    if(arr[i]+arr[i+1]==target){
      res.push(i);
      res.push(i+1);
      return res;
    }
  }
  return "Target not found";
}

/* 18-08-2025: Factorializer
Given an integer from zero to 20, return the factorial of that number. The factorial of a number is the product of all the numbers between 1 and the given number.

The factorial of zero is 1. */

function factorial(n) {
  if(n==0) return 1;
  else return n*factorial(n-1);
}

/* 19-08-2025: Sum of Squares
Given a positive integer up to 1,000, return the sum of all the integers squared from 1 up to the number. */

function sumOfSquares(n) {
  let arr=Array.from(new Array(n+1).keys()).slice(1);
  return arr.map((item)=>item*item).reduce((a,b)=>a+b,0);
}

/* 20-08-2025: 3 Strikes
Given an integer between 1 and 10,000, return a count of how many numbers from 1 up to that integer whose square contains at least one digit 3.
*/

function squaresWithThree(n) {
  let r=Array.from(new Array(n).keys()).slice(1);
  let m=r.map((item)=>(item*item).toString()).filter((item)=>item.includes('3'));
  return m.length;
}

/* 21-08-2025: Mile Pace
Given a number of miles ran, and a time in "MM:SS" (minutes:seconds) it took to run those miles, return a string for the average time it took to run each mile in the format "MM:SS".

Add leading zeros when needed. */

function milePace(miles, duration) {
  let min=duration.length<=5?duration.substring(0,2):duration.substring(0,3);
  let sec=duration.length<=5?duration.substring(3,5):duration.substring(4,6);
  let dur_m=(60*Number(min)+Number(sec))/miles;
  let min_m=Math.floor(dur_m/60);
  let sec_m=dur_m-60*min_m;
  min_m=min_m<10?"0"+min_m.toString():min_m.toString();
  sec_m=sec_m<10?"0"+sec_m.toString():sec_m.toString().substring(0,2);
  let pace_per_mile=min_m+":"+sec_m;
  return pace_per_mile;
}

/* 22-08-2025: Message Decoder
Given a secret message string, and an integer representing the number of letters that were used to shift the message to encode it, return the decoded string.

A positive number means the message was shifted forward in the alphabet.
A negative number means the message was shifted backward in the alphabet.
Case matters, decoded characters should retain the case of their encoded counterparts.
Non-alphabetical characters should not get decoded.
*/

function isAlpha(ch) {
let cd=ch.charCodeAt(0);  
let arr1=Array.from(new Array(26).keys()).map((item)=>item+65);
let arr2=Array.from(new Array(26).keys()).map((item)=>item+97);
let arr=[...arr1,...arr2];
return arr.includes(cd);
}

function isUpper(ch){
  return ch.toUpperCase()===ch;
}

function isLower(ch){
  return ch.toLowerCase()===ch;
}

function decode(message, shift) {
  let shi=shift<0?shift+26:shift;
  let m=message;
  let stri="";
  for(let i=0;i<m.length;i++){
    let ch=m.charCodeAt(i);
    if(isAlpha(m[i])){
      if(isUpper(m[i])){
        if(ch+26-shi<91){
stri+=String.fromCharCode(ch+26-shi); }
        else stri+=String.fromCharCode(ch-shi);
      }
      if(isLower(m[i])){
        if(ch+26-shi<123){
          stri+=String.fromCharCode(ch+26-shi);}
          else stri+=String.fromCharCode(ch-shi);
        }
      }
     else stri+=m[i];
    }
    return stri;
}

/* 23-08-2025: Unnatural Prime
Given an integer, determine if that number is a prime number or a negative prime number.

A prime number is a positive integer greater than 1 that is only divisible by 1 and itself.
A negative prime number is the negative version of a positive prime number.
1 and 0 are not considered prime numbers.
*/

function isUnnaturalPrime(n) {
   if(n==0||n==1||n==-1){
     return false;
   }
   let s;
   if(n<0){
     s=-n;
   }
   else s=n;
   for(let i=2;i<Math.floor(Math.sqrt(s))+2;i++){
     if(s%i==0){
       return false;
     }
   }
   return true;
}

/* 24-08-2025: Character Battle
Given two strings representing your army and an opposing army, each character from your army battles the character at the same position from the opposing army using the following rules:

Characters a-z have a strength of 1-26, respectively.
Characters A-Z have a strength of 27-52, respectively.
Digits 0-9 have a strength of their face value.
All other characters have a value of zero.
Each character can only fight one battle.
For each battle, the stronger character wins. The army with more victories, wins the war. Return the following values:

"Opponent retreated" if your army has more characters than the opposing army.
"We retreated" if the opposing army has more characters than yours.
"We won" if your army won more battles.
"We lost" if the opposing army won more battles.
"It was a tie" if both armies won the same number of battles.
*/

function mkDict() {
  let s1="abcdefghijklmnopqrstuvwxyz";let s2=s1.toUpperCase();
  let d={};
  for(let i=0;i<s1.length;i++){
   d[s1.slice(i,i+1)]=s1.charCodeAt(i)-96;
   d[s2.slice(i,i+1)]=s2.charCodeAt(i)-38;
  }
  let n="0123456789";
  for(let i=0;i<10;i++){
    d[n.slice(i,i+1)]=Number(n[i]);
  }
  return d;
}


function battle(myArmy, opposingArmy) {
  let d=mkDict();
  if(myArmy.length>opposingArmy.length){
    return "Opponent retreated";
  }
  else if(myArmy.length<opposingArmy.length){
    return "We retreated";
  } else {
    let a1=myArmy;
    let a2=opposingArmy;
    let s1=0; let s2=0;
    for(let i=0;i<a1.length;i++){
if(d[a1[i]]==undefined){d[a1[i]]=0;}
if(d[a2[i]]==undefined){
  d[a2[i]]=0;
}
       if(d[a1[i]]>d[a2[i]]){s1+=1;}
      
       if(d[a2[i]]>d[a1[i]]){s2+=1;};
    } if(s1>s2){
return "We won";} else if(s1<s2) {
return "We lost";}
    return "It was a tie";
  }
}
// battle("C@T5", "D0G$");

/* 25.08.2025: camelCase
Given a string, return its camel case version using the following rules:

Words in the string argument are separated by one or more characters from the following set: space ( ), dash (-), or underscore (_). Treat any sequence of these as a word break.
The first word should be all lowercase.
Each subsequent word should start with an uppercase letter, with the rest of it lowercase.
All spaces and separators should be removed.
*/

function propCase(stri){
  let prop = stri.slice(0,1).toUpperCase()+stri.slice(1).toLowerCase();
  return prop;
}

function toCamelCase(s) {
  let spli=s.toLowerCase().split(/[ -_]/);
  console.log(spli);
  let mp=spli.slice(1).map((item)=>propCase(item)).join("");
  return spli[0]+mp;
}

/* 26-08-2025: Reverse Parenthesis
Given a string that contains properly nested parentheses, return the decoded version of the string using the following rules:

All characters inside each pair of parentheses should be reversed.
Parentheses should be removed from the final result.
If parentheses are nested, the innermost pair should be reversed first, and then its result should be included in the reversal of the outer pair.
Assume all parentheses are evenly balanced and correctly nested.
*/

function indices(source, find) {
if (!source) {return [];}    let result = [];
for (let i = 0; i < source.length; i++) {
if (source.substring(i, i + find.length) == find) {
result.push(i);
  }
 }
return result;
}

function hlp(s){
  let ind1=indices(s,"(");
  let ind2=indices(s,")");
  let ind=[...ind1,...ind2].sort((a,b)=>a-b);
  let d=[];
  for(let i=0;i<ind.length;i++){ 
   if(ind1.includes(ind[i])&&ind2.includes(ind[i+1])){
   d.push([ind[i],ind[i+1]]);
   }
  }
  let ob={};
for(let i=0;i<d.length;i++){
  ob[i]=s.substring(d[i][0]+1,d[i][1]).split("").reverse().join("");
}
 
 let m=s.substring(0,d[0][0])+ob[0];
 for(let i=0;i<d.length-1;i++){
   m+=s.substring(d[i][1]+1,d[i+1][0])+ob[i+1];
 }
 m+=s.substring(d[d.length-1][1]+1);
  return m;
}

function decode(s) {
if (s.includes('(')){
  console.log(hlp(s));
  return decode(hlp(s));
  } else {return s;}
} 

/* 27-08-2025: Unorder of Operations
Given an array of integers and an array of string operators, apply the operations to the numbers sequentially from left-to-right. Repeat the operations as needed until all numbers are used. Return the final result.

For example, given [1, 2, 3, 4, 5] and ['+', '*'], return the result of evaluating 1 + 2 * 3 + 4 * 5 from left-to-right ignoring standard order of operations.

Valid operators are +, -, *, /, and %.
*/

function evaluate(numbers, operators) {
  let op=Array(numbers.length).fill(operators).flat().slice(0,numbers.length-1);
  let n=numbers;
  let stri=n[0]+op[0]+n[1];
  let val=eval(stri);
  for(let i=1;i<op.length;i++){
    let ex=val.toString()+op[i]+n[i+1];
    val=eval(ex);
  }
  return val;
}

/* 28-08-2025: Second Best
Given an array of integers representing the price of different laptops, and an integer representing your budget, return:

The second most expensive laptop if it is within your budget, or
The most expensive laptop that is within your budget, or
0 if no laptops are within your budget.
Duplicate prices should be ignored.
*/

function getLaptopCost(laptops, budget) {
  let s=new Set(laptops);
  let arr=Array.from(s).sort(); 
  let sl=arr.slice(arr.length-2,arr.length-1);
  let flt=arr.filter((item)=>item<=budget);
  if(budget>=sl){
    return sl;
  } else {
    if(flt){
      return flt.slice(flt.length-1);
    } else return 0;
  }
}
// getLaptopCost([1200, 1500, 1600, 1800, 1400, 2000], 1450)

/* 29-08-2025: Candlelight
Given an integer representing the number of candles you start with, and an integer representing how many burned candles it takes to create a new one, return the number of candles you will have used after creating and burning as many as you can.

For example, if given 7 candles and it takes 2 burned candles to make a new one:

Burn 7 candles to get 7 leftovers,
Recycle 6 leftovers into 3 new candles (1 leftover remains),
Burn 3 candles to get 3 more leftovers (4 total),
Recycle 4 leftovers into 2 new candles,
Burn 2 candles to get 2 leftovers,
Recycle 2 leftovers into 1 new candle,
Burn 1 candle.
You will have burned 13 total candles in the example.
*/

function burnCandles(candles, leftoversNeeded) {
  let burned=0;
  while(candles >=leftoversNeeded){
    let v=Math.floor(candles/leftoversNeeded);
    burned+=v*leftoversNeeded;
    candles=v+(candles%leftoversNeeded);
  }
  burned+=candles;
  return burned;
}

/* 30-08-2025: Array Duplicates
Given an array of integers, return an array of integers that appear more than once in the initial array, sorted in ascending order. If no values appear more than once, return an empty array.

Only include one instance of each value in the returned array.
*/

function findDuplicates(arr) {
  let s=Array.from(new Set(arr.sort((a,b)=>a-b).filter((item,index)=>arr.indexOf(item)<index)));
  return s;
} 

/* 31-08-2025: Hex Generator
Given a named CSS color string, generate a random hexadecimal (hex) color code that is dominant in the given color.

The function should handle "red", "green", or "blue" as an input argument.
If the input is not one of those, the function should return "Invalid color".
The function should return a random six-character hex color code where the input color value is greater than any of the others.
Example of valid outputs for a given input:
Input	Output
"red"	"FF0000"
"green"	"00FF00"
"blue"	"0000FF"
*/

function genRand(){
  let c1=Math.floor(Math.random()*255);
  let c2=Math.floor(Math.random()*255);
  let maxi=Math.max(c1,c2);
  let c3=Math.floor(Math.random()*(255-maxi))+maxi+1;
  let arr=[c1,c2,c3];
  return arr;
}

function generateHex(color) {
  let rCol;
  let hCol;
  if(color!=="red"&&color!=="green"&&color!=="blue"){
  return "Invalid color";
  }
  if(color=="red"){
    rCol=genRand();
  hCol=rCol[2].toString(16)+rCol[0].toString(16)+rCol[1].toString(16);}
  if(color=="green"){
    rCol=genRand();
    hCol=rCol[0].toString(16)+rCol[2].toString(16)+rCol[1].toString(16);
  }
  if(color=="blue"){
    rCol=genRand();
    hCol=rCol[1].toString(16)+
 rCol[0].toString(16)+rCol[2].toString(16);}
  return hCol;
}
