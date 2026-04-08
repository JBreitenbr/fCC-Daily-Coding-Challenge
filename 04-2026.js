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

