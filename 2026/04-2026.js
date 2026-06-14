/* 01-04-2026: Prank Number

Given an array of numbers where all but one number follow a pattern, return a new array with the one number that doesn't follow the pattern fixed.
The pattern will be one of:
• The numbers increase from one to the next by a fixed amount (addition).
• The numbers decrease from one to the next by a fixed amount (subtraction).
For example, given [2, 4, 7, 8, 10] return [2, 4, 6, 8, 10]. */

function freq(arr){
  let d={};
  for(let i=0;i<arr.length;i++){
    d[arr[i]]=0;
  }
  for(let i=0;i<arr.length;i++){
    d[arr[i]]+=1;
  }
  return d;
}

function fixPrankNumber(arr) {
  let sl=arr.slice(0);
  let d=[];
  let desc=arr[0]>=arr[arr.length-1]?true:false;
  let s=desc==true?arr.sort((a,b)=>b-a):arr.sort((a,b)=>a-b);
  for(let i=1;i<s.length;i++){
    d.push(s[i]-s[i-1]);
  }
  let v=Object.values(freq(d));
  let maxi=Math.max(...v);
  let val=0;
  for(let i=0;i<d.length;i++){
    if(freq(d)[d[i]]==maxi) val=d[i];
  }

  let c=(sl[1]-sl[0])==val;
  for(let i=0;i<s.length;i++){
    s[i]=s[0]+i*val;
  }

  if(desc && !c && sl[1]!=sl[0]){
    for(let i=0;i<s.length;i++){
      s[i]-=val;
    }
  }
  if(!desc && !c){
    for(let i=0;i<s.length;i++){
      s[i]+=val;
    }
  }
  
  return s;
}

/* 02-04-2026: Capitalized Fibonacci

Given a string, return a new string where each letter is capitalized if its index is a Fibonacci number, and lowercased otherwise.
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
• The first character is at index 0.
• If the index of non-letter characters is a Fibonacci number, leave it unchanged.
*/

function fibo(n) {
if(n==1 || n==2) return 1;
else return fibo(n-1)+fibo(n-2);
}

function capitalizeFibonacci(str) {
  let fibi=[0];
  for(let i=1;i<15;i++){
    fibi.push(fibo(i));
  }
  console.log(fibi);
  let res="";
  for(let i=0;i<str.length;i++){
    if(fibi.includes(i)) res+=str[i].toUpperCase();
    else res+=str[i].toLowerCase();
  }
  return res;
}

/* 03-04-2026: Browser History

Given an array of browser commands, return an array with two values: the history as an array of URLs, and the index of the current page.
Valid commands are:
• "URL" - Where URL is a web address ("freecodecamp.org" for example). Navigates to the given URL, adds it to the history at the next position, and discards any forward history.
• "Back" - moves to the previous page in history, or stays on the current page if there isn't one.
• "Forward" - moves to the next page in history, or stays on the current page if there isn't one.
For example, given ["freecodecamp.org", "freecodecamp.org/learn", "Back"], return [["freecodecamp.org", "freecodecamp.org/learn"], 0]. */

class BrowserHistory {
  constructor() {
    this.backStack = [];
    this.forwardStack = [];
  }
  
  visit(url) {
    this.forwardStack = [];
    this.backStack.push(url);
  }

  back(steps) {
    while (this.backStack.length > 1 && steps-- > 0) {
      this.forwardStack.push(this.backStack[this.backStack.length - 1]);
      this.backStack.pop();
    }
  return this.backStack[this.backStack.length - 1];
  }

  forward(steps) {
    while (this.forwardStack.length > 0 && steps-- > 0) {
      this.backStack.push(this.forwardStack[this.forwardStack.length - 1]);
      this.forwardStack.pop();
    }
    return this.backStack[this.backStack.length - 1];
   }
 }

function getBrowserHistory(c) {
  let sn=0;
  let bf=["Back","Forward"];
  if(!bf.includes(c[c.length-2]) && c[c.length-1]=="Forward") c=c.slice(0,c.length-1);
  for(let i=1;i<c.length;i++){
    if(!bf.includes(c[i])) sn+=1;
    else if(c[i]=="Back")sn-=1;
    else sn+=1;
  }
  let h=new BrowserHistory();
    for(let i=0;i<c.length;i++){
    if(!bf.includes(c[i])){
        h.visit(c[i]);  
    } if(c[i]=="Back"){
        h.back(1);
    } if(c[i]=="Forward"){
        h.forward(1);
    }         
  }
  let res=[];
  res.push([...h.backStack,...h.forwardStack]);
  res.push(Math.max(sn,0));
  return res;
}

/* 04-04-2026: Equation Validation

Given a string representing a math equation, determine whether it is correct.
• The left side may contain up to three positive integers and the operators +, -, *, and /.
• The equation will be given in the format: "number operator number = number" (with two or three numbers on the left). For example: "2 + 2 = 4" or "2 + 3 - 1 = 4".
• The right side will always be a single integer.
Follow standard order of operations: multiplication and division are evaluated before addition and subtraction, from left-to-right. */

function isValidEquation(equation) {
  let sp=equation.split("=");
  return eval(sp[0])==Number(sp[1]);
}

/* 05-04-2026: Digit Rotation Escape 

Given a positive integer, determine if it, or any of its rotations, is evenly divisible by its digit count.
A rotation means to move the first digit to the end. For example, after 1 rotation, 123 becomes 231.
• Check rotation 0 (the given number) first.
• Given numbers won't contain any zeros.
• Return the first rotation number if one is found, or "none" if not. */

function rotations(stri){
  let rots=[stri];
  for(let i=1;i<stri.length;i++){
    let rot=rots[i-1].slice(1)+rots[i-1][0];
    rots.push(rot);
  }
  return rots;
}

function getRotation(n) {
  let rots=rotations(n.toString());
  for(let i=0;i<rots.length;i++){
    if(parseInt(rots[i])%rots[i].length==0) return i;
  } return "none";
}

/* 06-04-2026: What Day Is It?

Given a Unix timestamp in milliseconds, return the day of the week.
Valid return days are:
• "Sunday"
• "Monday"
• "Tuesday"
• "Wednesday"
• "Thursday"
• "Friday"
• "Saturday"
Be sure to ignore time zones. */

function getDayOfWeek(timestamp) {
  let days={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",0:"Sunday"};
  let d=new Date(timestamp).getDay();
  return days[d];
}

/* 07-04-2026 Palindrome Characters

Given a string, determine if it's a palindrome and return the middle character (if it's odd length) or middle two characters (if it's even).
• A palindrome is a string that is the same forward and backward.
• If it's not a palindrome, return "none". */

function palindromeLocator(str) {
  let c=str.split("").reverse().join("")==str;
  if(!c) return "none";
  let d=str.length%2;
  if(d==1) return str[Math.floor(str.length/2)];
  else return str.slice(str.length/2-1,str.length/2+1);
}

/* 08-04-2026: FizzBuzz Validator

Given an array of sequential integers, with multiples of 3 and 5 replaced, determine if it's a valid FizzBuzz sequence.
In a valid FizzBuzz sequence:
• Multiples of 3 are replaced with "Fizz".
• Multiples of 5 are replaced with "Buzz".
• Multiples of both 3 and 5 are replaced with "FizzBuzz".
• All other numbers remain as integers. */

function isFizzBuzz(arr) {
  let c=[arr[0]];
  for(let i=1;i<arr.length;i++){
    if(arr[i]==parseInt(arr[i])){
      c.push(arr[i]);
    }
    else if(arr[i-1]==parseInt(arr[i-1])&&arr[i]!=parseInt(arr[i])){
      c.push(arr[i-1]+1);
    } else if(arr[i+1]==parseInt(arr[i+1])&&arr[i]!=parseInt(arr[i])){c.push(arr[i+1]-1);}
  }
  let m=c.map((item)=>item%3==0&&item%5!=0?"Fizz":item).map((item)=>item%3!=0&&item%5==0?"Buzz":item).map((item)=>item%3==0&&item%5==0?"FizzBuzz":item);
  for(let i=0;i<arr.length;i++){
    if(arr[i]!=m[i]) return false;
  }
  return true;
}

/* 09-04-2026: Next Bingo Number

Given a bingo number, return the next bingo number sequentially.
A bingo number is a single letter followed by a number in its range according to this chart:
LetterNumber Range
         "B"             1-15
         "I"             16-30
        "N"             31-45
        "G"             46-60
        "O"             61-75
For example, given "B10", return "B11", the next bingo number. If given the last bingo number, return "B1". */

function getNextBingoNumber(n) {
  let b=["B","I","N","G","O"];
  if(n.slice(1)=="75") return "B1";
  let p=(parseInt(n.slice(1))+1).toString();
   return parseInt(n.slice(1))%15==0?b[b.indexOf(n[0])+1]+p:n[0]+p;
}

/* 10-04-2026: Rook Attack

Given two strings for the location of two rooks on a chess board, determine if they can attack each other.
A standard chessboard is 8x8, with columns labeled A through H (left to right) and rows labeled 1 through 8 (bottom to top). */

function rookAttack(rook1, rook2) {
  return rook1[0]==rook2[0]||rook1[1]==rook2[1];
}

/* 11-04-2026: Rook and Bishop Attack

Given a string for the location of a rook on a chess board, and another for the location of a bishop, determine if one piece can attack another.
A standard chessboard is 8x8, with columns labeled A through H (left to right) and rows labeled 1 through 8 (bottom to top).  */

function rookBishopAttack(rook, bishop) {
  if(rook[0]==bishop[0]||rook[1]==bishop[1]) return "rook";
  let l="ABCDEFGH";
  let c="12345678";
  let d1=l.indexOf(rook[0])-l.indexOf(bishop[0]);
  let d2=c.indexOf(rook[1])-c.indexOf(bishop[1]);
  if(Math.abs(d1)==Math.abs(d2)) return "bishop";
  return "neither";
}

/* 12-04-2026: Spiral Matrix

Given a 2D matrix, return a flat array with all of its values in clockwise order.
The returned array should have the top-left value first, move right along the top row, then down the right column, then left along the bottom row, then up the left column. Repeat inward for any remaining layers.
For example, given:
[ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] 
Return [1, 2, 3, 6, 9, 8, 7, 4, 5]. */

function transpose(array) {
    return array.reduce((prev, next) => next.map((item, i) => (prev[i] || []).concat(next[i])), []);
}

function sliced(matrix,row,st,len,dir){
  return dir==0?matrix[row].slice(st,st+len):matrix[row].slice(st,st+len).reverse();
}

function spiralMatrix(matrix) {
  let c=matrix[0].length;
  let r=matrix.length;
  let trans=transpose(matrix);
  let rows=[];
  let cols=[];
  let sn=0;
  for(let i=0;i<Math.ceil(r/2);i++){
  if(r==c){
    rows.push(sliced(matrix,i,i,r-sn,0));
    rows.push(sliced(matrix,r-i-1,i,r-sn-1,1));
  }
  if(r==c+1){
    rows.push(sliced(matrix,i,i,r-sn-i,0));
    rows.push(sliced(matrix,r-i-1,i,r-sn-2,1));
  }
  sn+=2;
}
sn=0;
for(let i=0;i<Math.ceil(c/2);i++){
 if(r==c){
    cols.push(sliced(trans,c-1-i,i+1,c-sn-1,0));
    cols.push(sliced(trans,i,i+1,c-sn-2,1));
  }
  if(r==c+1){
    cols.push(sliced(trans,c-1-i,i+1,c-sn,0));
    cols.push(sliced(trans,i,i+1,c-sn-1,1));
  }
  sn+=2;
 }
  let pre=[];
  for(let i=0;i<rows.length;i++){
    pre.push(rows[i]);
    pre.push(cols[i]);
  }
  let res=pre.filter((item)=>item.length>=1).flat();
  return res;
}

/* 13-04-2026: Name Initials

Given a full name as a string, return their initials.
• Names to initialize are separated by a space.
• Initials should be made uppercase.
• Initials should be separated by dots.
For example, "Tommy Millwood" returns "T.M.". */

function getInitials(name) {
  return name.split(" ").map((item)=>item[0]+".").join("");
}

/* 14-04-2026: Last Letter

Given a string, return the letter from the string that appears last in the alphabet.
• If two or more letters tie for the last in the alphabet, return the first one.
• Ignore all non-letter characters. */

function getLastLetter(str) {
  let ch1=str.toLowerCase().split("").sort().reverse()[0];
  let ch2=ch1.toUpperCase();
  let i1=str.indexOf(ch1);
  let i2=str.indexOf(ch2);
  return i1==-1?ch2:i2==-1?ch1:str[Math.min(i1,i2)];
}

/* 15-04-06: Sorted Array Swap

Given an array of integers, return a new array using the following rules:
• Sort the integers in ascending order
• Then swap all values whose index is a multiple of 3 with the value before it. */

function sortAndSwap(arr) {
  let s=arr.sort((a,b)=>a-b);
  for(let i=1;i<s.length;i++){
    if(i%3==0){
      let temp=s[i-1];
      s[i-1]=s[i];
      s[i]=temp;
    }
  }
  return s;
}

/* 16-04-2026: String Math

Given a string with numbers and other characters, perform math on the numbers based on the count of non-digit characters between the numbers.
• If the count of characters separating two numbers is even, use addition.
• If it's odd, use subtraction.
• Consecutive digits form a single number.
• Operations are applied left to right.
• Ignore leading and trailing characters that aren't digits.
For example, given "3ab10c8", return 5. Add 3 and 10 to get 13 because there's an even number of characters between them. Then subtract 8 from 13 because there's an odd number of characters between the result and 8. */

function doMath(str) {
  let reg1=/[0-9]+/gi;
  let reg2=/\D+/gi;
  let m1=str.match(reg1).map((item)=>item[0]=="0"&&item.length>1?item.slice(1):item);
  let m2=str.match(reg2);
  let ops=m2.map((item)=>item.length%2==0?"+":"-");
  let d="0123456789";
  ops=d.includes(str[0])&&d.includes(str[str.length-1])?ops:ops.slice(1,ops.length-1);
 let res=eval(m1[0]+ops[0]+m1[1]);
  for(let i=1;i<ops.length;i++){
    res=eval(res+ops[i]+m1[i+1]);
  }
  return res;
}

/* 17-04-2026: Hidden Key

Welcome to the 250th daily challenge!
Given an encoded string, decode it using an encryption key and return it.
To find the key:
• Look at all daily challenges up to today whose challenge number is a multiple of 25 (including this one).
• Take the first letter from each of those challenge titles and combine them into a string. If the title starts with a non-letter, find its first letter.
To decode the message, go over each letter in the encoded message and:
• Look at the corresponding letter in the key (repeat the key if the message is longer than the key).
• Convert the key letter to its corresponding number: "A" = 1, "B" = 2, ..., "Z" = 26.
• Shift the encoded letter backward in the alphabet by that number.
• If the shift goes before "A", wrap around to "Z".
For example, if the encoded message starts with "Y" and the first key letter is "V" (22), shift "Y" back 22 places to get "C". Repeat this process for each letter to decode the full message.
• Only letters are shifted, spaces are returned as-is.
• All given and returned letters are uppercase. */

function decode(message) {
  let k0="VLHCGMDLNH";
  let l=Math.ceil(message.length/10);
  let k="";
  for(let i=0;i<l;i++){
    k+=k0;
  }
  let a="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  let sp=message.split(" ");
  let sn1=0;
  let sn2=sp[0].length;
  let sl=[[sn1,sn2]];
  for(let i=1;i<sp.length;i++){
     sn1=sl[i-1][1];
     sn2=sn1+sp[i].length;
     sl.push([sn1,sn2]);
  }
  let msg=message.replaceAll(" ","");
  let pre="";
  for(let i=0;i<msg.length;i++){
    let c1=a.indexOf(k[i])+1;
    let s=a.indexOf(msg[i])+1-c1;
    let c2=s<1?(s+26):s;
    let ch=a[c2-1];
    pre+=ch;
  }
  let res="";
  for(let i=0;i<sl.length;i++){
    res+=pre.slice(sl[i][0],sl[i][1])+" ";
  }
  return res.slice(0,res.length-1);
}

/* 18-04-2026: Array Sum Finder

Given an array of numbers and a target number, return the first subset of two or more numbers that adds up to the target.
• The "first" subset is the one whose elements have the lowest possible indices, prioritizing the earliest index first.
• Each number in the array may only be used once.
• If no valid subset exists, return "Sum not found".
Return the matching numbers as an array in the order they appear in the original array. */

let getAllSubsets = (nums) => {
  const subsets = [[]];
  for (let n of nums) {
    subsets.map((el) => {
    subsets.push([...el, n]);
                    });
  }
  return subsets.filter((item)=>item.length>=2);
};

function findSum(arr, target) {
  let pos=arr.every((item)=>item>0);
  if(pos) arr=arr.filter((item)=>item<=target-1);
  let subs=getAllSubsets(arr).map((item)=>Array.from(new Set(item))).filter((item)=>item.reduce((a,b)=>a+b,0)==target);
  if(subs.length==0) return "Sum not found";
  return subs.map((item)=>item.map((item)=>arr.indexOf(item))).sort()[0].map((item)=>arr[item]);
}

/* 19-04-2026: Unique Stair Climber

Given a number of stairs, return how many distinct ways someone can climb them taking either 1 or 2 steps at a time. */

function getUniqueClimbs(steps) {
  let arr=[1,2];
  for(let i=2;i<steps;i++){
    arr.push(arr[i-1]+arr[i-2]);
  }
  return arr[steps-1];
}

/* 20-04-2026: Acronym Finder

Given a string representing an acronym, return the full name of the organization it belongs to from the list below:
• "National Avocado Storage Authority"
• "Cats Infiltration Agency"
• "Fluffy Beanbag Inspectors"
• "Department Of Jelly"
• "Wild Honey Organization"
• "Eating Pancakes Administration"
Each letter in the given acronym should match the first letter of each word in the organization it belongs to, in the same order. */

function findOrg(acronym) {
let arr=["National Avocado Storage Authority",
"Cats Infiltration Agency",
"Fluffy Beanbag Inspectors",
"Department Of Jelly",
"Wild Honey Organization",
"Eating Pancakes Administration"];
let k=arr.map((item)=>item.split(" ").map((item)=>item[0]).join(""));
  return arr[k.indexOf(acronym)];
}

/* 21-04-2026: Odd Words

Given a string of words, return only the words with an odd number of letters.
• Words in the given string will be separated by a single space.
• Return the words separated by a single space. */

function getOddWords(str) {
  return str.split(" ").filter((item)=>item.length%2==1).join(" ");
}

/* 22-04-2026: Earth Day Cleanup Crew
Today is Earth Day. Given an array of items you cleaned up, return your total cleanup score based on the rules below.
Given items will be one of:
ItemBase Value"bottle"10"can"6"bag"8"tire"35"straw"4"cardboard"3"newspaper"3"shoe"12"electronics"25"battery"18"mattress"38
A Rare item is represented as ["rare", value]. For example, ["rare", 80]. Rare items do not get a streak bonus.
• Streak bonus: If the same item appears consecutively, it gets increasing bonus points.
• First consecutive occurrence: base value
• Second: base value + 1
• Third: base value + 2
• etc.
• Fifth Item Multiplier: Every fifth item collected gets a multiplier.
• Fifth item: *2
• Tenth item: *3
• etc.
• Apply the multiplier after calculating any bonuses. */

function getCleanupScore(items) {
let obj={"bottle":10,"can":6,
"bag":8,"tire":35,"straw":4,
"cardboard":3,"newspaper":3,
"shoe":12,"electronics":25,
"battery":18,"mattress":38};
  let s=[];
  let sn=0;
  for(let i=0;i<items.length;i++){
    if(Array.isArray(items[i])){
      sn=0;
      s.push(items[i][1]);
    } 
    else if(i>=1 && items[i]==items[i-1]){
      sn+=1;
      s.push(obj[items[i]]+sn);
    } else {
      sn=0;
      s.push(obj[items[i]]);
    }
  }
  for(let i=0;i<s.length;i++){
    if((i+1)%5==0){
      s[i]*=((i+1)/5+1);
    }
  }
  return s.reduce((a,b)=>a+b,0);
}

/* 23-04-2026: Closest Time Direction

Given two times, determine whether you can get from the first to the second faster by moving forward or backward.
• Times are given in 24-hour format ("HH:MM")
• The clock wraps around (23:59 goes to 00:00 when moving forward, and 00:00 goes to 23:59 when moving backwards)
Return:
• "forward" if moving forward is shorter
• "backward" if moving backward is shorter
• "equal" if both directions take the same amount of time */

function getDirection(time1, time2) {
  let t1=parseInt(time1.slice(0,2)*60)+parseInt(time1.slice(3,5));
  let t2=parseInt(time2.slice(0,2)*60)+parseInt(time2.slice(3,5));
  let d1=(t2-t1)/60;
  let d2=(24*60-(t2-t1))/60%24;
  return d1<0&&-d1>12?"forward":d1<0&&-d1<12?"backward":d1<d2?"forward":d1>d2?"backward":"equal";
}

/* 24-04-2026: Word Compressor

Given a string, return a compressed version of the string using the following rules:
• The first occurrence of a word remains unchanged.
• Subsequent occurrences are replaced with the position of the first occurrence, where the first word is at position 1.
• Words are separated by a single space.
For example, given "practice makes perfect and perfect practice makes perfect", return "practice makes perfect and 3 1 2 3".
*/

function compress(str) {
  let sp=str.split(" ");
  return sp.map((item,index)=>sp.slice(0,index).includes(item)?sp.indexOf(item)+1:item).join(" ");
}

/* 25-04-2026: Word Decompressor

Given a compressed string, return the decompressed version using the following rules:
• The given string is made up of words and numbers separated by spaces.
• Leave the words unchanged.
• Replace numbers with the word at that position, where the first word is at position 1.
For example, given "practice makes perfect and 3 1 2 3", return "practice makes perfect and perfect practice makes perfect". */

function decompress(str) {
  let reg=/[0-9]+/gi;
  let m=str.match(reg);
  let sp=str.split(" ");
  return sp.map((item)=>m.includes(item)?sp[Number(item)-1]:item).join(" ");
}

/* 26-04-2026: FizzBuzz Explosion

Given an integer, return the number of steps it takes to turn the word "fizzbuzz" into a string with at least the given number of "z"'s using the following rules:
• Start with the string "fizzbuzz".
• Each step, apply the standard FizzBuzz rules using the letter position in the string (the first "f" is position 1).
• If the letter position is divisible by 3, replace the letter with "fizz"
• If it's divisible by 5, replace the letter with "buzz"
• If it's divisible by 3 and 5, replace the letter with "fizzbuzz"
So after 1 step, "fizzbuzz" turns into "fifizzzbuzzfizzzz", which has 9 "z"'s. */

function explodeFizzbuzz(targetZCount) {
  let arr="afizzbuzz".split("");
for(let j=0;j<15;j++){
  for(let i=1;i<arr.length;i++){
    if(i%3==0 && i%5!=0){
      arr[i]="fizz";
    } 
    if(i%5==0&&i%3!=0){
      arr[i]="buzz";
    } 
    if(i%3==0&&i%5==0){
      arr[i]="fizzbuzz";
    }
  }
  arr=arr.join("");
  let sp=arr.split("z").length-1;
  if(sp>=targetZCount){
    return j+1;
  }
  arr=arr.split("");
  }
}

/* 27-04-2026: Word Score

Given a word, return its score using a standard letter-value table:
LetterValueA1B2......Z26
• Upper and lowercase letters have the same value. */

function getWordScore(word) {
  let a="abcdefghijklmnopqrstuvwxyz";
  let sn=0;
  for(let i=0;i<word.length;i++){
    sn+=a.indexOf(word[i].toLowerCase())+1;
  }
  return sn;
}

/* 28-04-2026: Number Words

Given an integer from 0 to 99, return its English word representation.
• 0 returns "zero".
• Numbers 1-19 have unique names ("one", "two", ..., "ten", "eleven", ..., "eighteen", "nineteen").
• Multiples of 10 from 20-90 have their own names ("twenty", "thirty", ..., "eighty", "ninety").
• Numbers 21-99 that are not multiples of 10 are written as two words joined by a hyphen. For example "forty-two" and "fifty-three". */

function getNumberWords(n) {
  let w1=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"];
  let w2=["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"];
  if(n<=19) return w1[n];
  else if(n%10==0) return w2[n/10-2];
  else return w2[Math.floor(n/10)-2]+"-"+w1[n%10];
}

/* 29-04-2026: URL Query Parser

Given a URL that contains a query string, parse the query string into an object (or dictionary) of key-value pairs.
• The query string begins after the "?",
• each parameter is separated by "&",
• each key/value pair is separated by "="
For example, given "https://example.com/search?name=Alice&age=30", return:
{ "name": "Alice", "age": "30" } 
All values should be returned as strings. */

function parseUrlQuery(url) {
  let sp=url.split("?")[1].split("&");
  let res={};
  let k=sp.map((item)=>item.split("=")[0]);
  let v=sp.map((item)=>item.split("=")[1]);
  for(let i=0;i<k.length;i++){
    res[k[i]]=v[i];
  }
  return res;
}

/* 30-04-2026: Binary Crossword

Given a character, determine if its 8-bit binary representation can be found in the following grid, horizontally or vertically in either direction:
0 1 0 0 0 0 0 1 
0 1 1 0 1 1 1 1 
0 1 0 0 0 1 0 0 
0 1 1 0 0 1 0 1
0 1 0 1 0 0 1 0 
0 1 0 1 0 1 0 0 
0 1 1 0 1 0 0 0 
1 0 1 0 1 1 1 0 
For example, "A" has the binary representation 01000001, which appears in the first row from left to right. */

function toNum(stri){
  let n=0;
  for(let i=0;i<8;i++){
    n+=Math.pow(2,7-i)*stri[i];
  }
  return n;
}

function transpose(array) {
    return array.reduce((prev, next) => next.map((item, i) => (prev[i] || []).concat(next[i])), []);
}

function isInCrossword(char) {
let grid=["01000001".split(""),"01101111".split(""),"01000100".split(""),"01100101".split(""),"01010010".split(""),"01010100".split(""),"01101000".split(""),"10101110".split("")];
let trans=transpose(grid);
let diag1=Array(8).fill(0).map((item,index)=>grid[index][index]).join("");
let diag2=diag1.split("").reverse().join("");
let diag3=Array(8).fill(0).map((item,index)=>trans[index][index]).join("");
let diag4=diag3.split("").reverse().join("");
let arr=[];
for(let i=0;i<grid.length;i++){
  arr.push(grid[i].join(""));
  arr.push(grid[i].reverse().join(""));
  arr.push(trans[i].join(""));
  arr.push(trans[i].reverse().join(""));
}
  arr.push(diag1);
  arr.push(diag2);
  arr.push(diag3);
  arr.push(diag4);
  let c=arr.map((item)=>String.fromCharCode(toNum(item)));
  return c.includes(char);
}
