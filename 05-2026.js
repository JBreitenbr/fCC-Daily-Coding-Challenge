/* 01-05-2026: Anagram Groups

Given an array of words, return a 2d array of the words grouped into anagrams.
• Words are anagrams if they contain the same letters in any order.
• Each word belongs to exactly one group.
• Return order doesn't matter.
For example, given ["listen", "silent", "hello", "enlist", "world"], return [["listen", "silent", "enlist"], ["hello"], ["world"]]. */

function groupAnagrams(words) {
  let hlp=words.map((item,index)=>[item.split("").sort().join(""),index]).sort();
  let pre=words.map((item)=>[item]);
  for(let j=0;j<words.length;j++){
  for(let i=0;i<hlp.length;i++){
    if(hlp[i][0]==words[j].split("").sort().join("")&&hlp[i][1]!=j){
      pre[j].push(words[hlp[i][1]]);
    } 
  }
  }
  return Array.from(new Set(pre.map((item)=>item.sort().join("/")))).map((item)=>item.split("/"));
}

/* 02-05-2026: Deepest Brackets
Given a string containing balanced brackets, return the content of the deepest nested brackets.
• Brackets can be any of the three types: (), [], and {}.
• The input will always have a single deepest group.
For example, given "(hello (world))", return "world". */

function getDeepestBrackets(s) {
  let p=[];
  let z=[];
  let s1=0;
  let s2=0;  
  for(let i=0;i<s.length;i++){
    if(["{","[","("].includes(s[i])){
      p.push(i);
      z.push(s1-s2);
      s1+=1;
    }
    if(["}","]",")"].includes(s[i])){
      p.push(i);
      z.push(s1-s2);
      s2+=1;
    }
  }
  let maxi=Math.max(...z);
  let ind=z.indexOf(maxi);
  return s.slice(p[ind-1]+1,p[ind]);
}

/* 03-05-2026: Good Day
Given a time string in "HH:MM" format (24-hour clock), return:
• "Good morning" for times 05:00 to 11:59
• "Good afternoon" for times 12:00 to 17:59
• "Good evening" for times 18:00 to 21:59
• "Good night" for times 22:00 to 04:59 */

function getGreeting(time) {
  let h=parseInt(time.slice(0,2));
  return h>=5 && h<12?"Good morning":h>=12 && h<18?"Good afternoon":h>=18 && h<22?"Good evening":"Good night";
}

/* 04-05-2026: Parsec Converter
In a distant galaxy, parsecs are used to measure both time and distance. Given an integer number of parsecs, return its equivalent in time or distance.
• If the given integer is odd, it represents time. If it's even, it represents distance.
Use these conversion rates:
ParsecsTime/Distance12 hours26 light years
Return the converted value as an integer. */

function convertParsecs(parsecs) {
  return parsecs%2==1?(parsecs*2):(parsecs*3);
}

/* 05-05-2026: Narcissistic Number
Given a positive integer, determine whether it is a narcissistic number.
• A number is narcissistic if the sum of each of its digits raised to the power of the total number of digits equals the number itself.
For example, 153 has 3 digits, and 13 + 53 + 33 = 153, so it is narcissistic. */

function isNarcissistic(n) {
  return n==n.toString().split("").map((item)=>Math.pow(parseInt(item),n.toString().length)).reduce((a,b)=>a+b,0);
}

/* 06-05-2026: Allergen Friendly Meals
Given an array of meals and an array of allergens to avoid, return the names of all the meals that contain none of the given allergens.
• Each meal is in the format [meal, allergens], where meal is the name of the meal, and allergens is an array of the allergens the meal contains. For example, ["pasta", ["wheat", "milk"]].
• Allergens to avoid will be an array of strings.
Return safe meal names in the same order given. If no meal is safe, return an empty array. */

function getAllergenFriendlyMeals(meals, allergens) {
  let aller=new Set(allergens);
  let res=[];
  for(let j=0;j<meals.length;j++){
    let r=new Set(meals[j][1]);
    if(Array.from(aller.intersection(r)).length==0){
      res.push(meals[j][0]);
    };
  }
  return res;

/* 07-05-2026: Longest Common Substring
Given a string, return the longest substring that appears more than once.
• The substrings can overlap. */

function indices(source, find) {
if (!source) {return [];} let result = [];
for (let i = 0; i < source.length; i++) {
if (source.substring(i, i + find.length) == find) {
       result.push(i);
      }
    }
    return result;
}

function getLongestSubstring(str) {
let res=[];
for(let i=0;i<str.length;i++){
for(let j=0;j<str.length;j++){
let sl=str.slice(i,j);
if(sl.length>=1){
res.push(sl);
    }
  }
}
return res.filter((item)=>indices(str,item).length>=2).sort((a,b)=>b.length-a.length)[0];
}

/* 08-05-2026: Medication Reminder
Given an array of medications and a string representing the current time, return the next medication you need to take and how long until you need to take it.
• Each medication is in the format [name, lastTaken], where name is the name of the medication and lastTaken is the time it was last taken.
• All given times will be in "HH:MM" (24-hour) format.
Use the following medication schedule:

Name
Schedule

Deployxitrin
08:00, 16:00

Debuggamanizole
07:00, 13:00, 21:00

Mergeflictamine
every 4 hours


Return a string in the format "{name} in Hh Mm". For example, "Debuggamanizole in 2h 0m" or "Deployxitrin in 1h 5m". */
  
function toMin(tStri){
  return parseInt(tStri.slice(0,2))*60+parseInt(tStri.slice(3,5));
}

function toStri(mins){
  let _h=(Math.floor(mins/60)).toString();
  let _m=(mins-parseInt(_h*60)).toString();
  return _h+"h "+_m+"m";
}

function medicationReminder(medis, currT) {
  let meds=["Deployxitrin","Debuggamanizole","Mergeflictamine"];
  let first=medis[0][1]=="08:00"?toMin("16:00"):toMin("08:00");
  let second=medis[1][1]=="07:00"?toMin("13:00"):medis[1][1]=="13:00"?toMin("21:00"):toMin("07:00");
  let third=toMin(medis[2][1])+240;
  let curr=toMin(currT);
  let arr=[Math.abs(first-curr),Math.abs(second-curr),Math.abs(third-curr)];
  let mini=Math.min(...arr);
  let ind=arr.indexOf(mini);
  return ${meds[ind]} in ${toStri(arr[ind])};
}

/* 09-05-2026: Transposed Matrix
Given a matrix (an array of arrays), return the transposed version of it. */
  
function transpose(matrix) {
  return matrix.reduce((prev, next) => next.map((item, i) => (prev[i] || []).concat(next[i])), []);
}

/* 10-05-2026: ISBN-13 Validator
Given a string, determine if it is a valid ISBN-13 number.
A valid ISBN-13:
• Contains only digits and hyphens
• Has exactly 13 digits after removing hyphens
• Passes the following check:
A. Multiply each digit by 1 or 3, alternating (multiply the first digit by 1, the second by 3, the third by 1, and so on).
B. The sum of the results must be divisible by 10. */

function isValidIsbn13(str) {
  let reg=/[0-9]+/gi;
  let m=str.replaceAll("-","").match(reg);
  if(m.length!=1||m[0].length!=13) return false;
  return m[0].split("").map((item,index)=>index%2==0?parseInt(item):parseInt(item)*3).reduce((a,b)=>a+b,0)%10==0;
}
  
/* 11-05-2026: Oldest Person
Given an array of objects, each with a "name" and "age" property, return an array containing the name of the oldest person.
If multiple people share the oldest age, return all of their names in the order they appear in the input. */

function getOldest(people) {
  let maxi=Math.max(...people.map((item)=>item.age));
  return people.filter((item)=>item.age==maxi).map((item)=>item.name);
}

/* 12-05-2026:
Character Frequency
Given a string, return an object (JavaScript) or dictionary (Python) mapping each character to the number of times it appears. */

function getFrequency(str) {
  let obj={};
  for(let i=0;i<str.length;i++){
   obj[str[i]]=0;
  }
  for(let i=0;i<str.length;i++){
   obj[str[i]]+=1;
  }
  return obj;
}

/* 13-05-2026: Offending Element
Given an array of integers that is sorted in ascending order except for one out-of-place element, return the index of that element.
• If more than one element could be considered out of place, return the index of the first one. */
  
function checkSorted(arr) {
  return arr.every((value, index, array) => index === 0 || value >= array[index - 1]);
}

function minusOne(arr,ind){
  let res=[];
  for(let i=0;i<arr.length;i++){
  if(i!=ind){
  res.push(arr[i]);
   }
 }
  return res;
}

function findOffender(arr) {
  for(let i=0;i<arr.length;i++){
   if(checkSorted(minusOne(arr,i))){
    return i;
    }
  }
}

/* 14-05-2026: Mirror Image
Given two strings, determine if the second string is a mirror image of the first.
A mirror image is formed by reversing the string and replacing each character with its mirror equivalent.
• Symmetric characters look like themselves in a mirror:
W, T, Y, U, I, O, H, A, X, V, M, w, o, x, v, 0, 8, =, +, :, |, -, _, *, ^, !, ., and the space ().
• Mirrored pairs swap with each other in a mirror:

Character
Swaps with

[
]

{
}

<
>

b
d

p
q

(
)


If either string includes a character not in the lists above, it doesn't have mirror image that can be created from the characters.
For example, the mirrored image of "[HOW]" is "[WOH]". */

function isMirrorImage(str1, str2) {
   let swap={"[":"]","{":"}","<":">","b":"d","p":"q","(":")"};
   for(let k of Object.keys(swap)) swap[swap[k]]=k;
   return str1.split("").reverse().map((item)=>Object.keys(swap).includes(item)?swap[item]:item).join("")==str2;
}

/*  15-05-2026: Coffee Order Parser
Given a string for a coffee order, identify any menu items and return a formatted order.
Use the following menu items and prices:

Item
Price

"cold brew"
$4.50

"oat latte"
$5.00

"cappuccino"
$4.75

"espresso"
$3.00

"vanilla syrup"
$0.75

"caramel drizzle"
$0.60

"extra shot"
$0.50

"oat milk"
$0.75

"cream"
$0.75


Return a string with the matched items joined by " + ", followed by a colon and space (": "), and the total price.
For example, given "I'd like an oat latte with vanilla syrup and an extra shot please.", return "oat latte + vanilla syrup + extra shot: $6.25"
Items should appear in the order they appear in the menu and the total price should always have two decimal places. */

function formatCoffeeOrder(order) {
  let drinks=["cold brew","oat latte","cappuccino","espresso","vanilla syrup",
"caramel drizzle" ,"extra shot","oat milk","cream"];
  let prices=[4.50,5.00,4.75,3.00,0.75,0.60,0.50,0.75,0.75];
  let ind=drinks.map((item,index)=>[order.indexOf(item),order.indexOf(item)+item.length,index]).filter((item)=>item[0]>=0);
  let sn=0;
  let pre="";
  for(let i=0;i<ind.length;i++){
    pre+=order.slice(ind[i][0],ind[i][1])+" + ";
    sn+=prices[ind[i][2]];
  }
  let pr=parseInt(sn)==sn?sn.toString()+".00":
   parseInt(10*sn)==10*sn?sn.toString()+"0":sn.toString();
  let res=pre.slice(0,pre.length-3)+": $"+pr;
  return res;
}

/* 16-05-2026: Longest Domino Chain
Given a 2D array representing a set of dominoes, return the longest valid chain.
• Each domino is a pair of numbers from 0–6, e.g. [3, 2].
• A chain is valid when the second number of each domino matches the first number of the next.
• The first number of the first domino and the second number of the last one don't need to match anything.
• Any domino can be flipped, so [3, 2] can be played as [2, 3].
• There is always exactly one longest valid chain.
For example, given [[1, 2], [4, 5], [2, 3]], return [[1, 2], [2, 3]]. */

/* 17-05-2026: Mongo ID Date
Given a MongoDB ID string, return its creation time as an ISO 8601 string.
• A MongoDB ID is a 24-character hex string. The first 8 characters represent a Unix timestamp (in seconds) encoded as a base-16 integer.
For example, "6a094b50bcf86cd799439011" has a timestamp of "6a094b50" in hex, which is 1778994000 in decimal, representing a creation time of "2026-05-17T05:00:00.000Z". */

  function mongoIdToDate(id) {
   return new Date(parseInt(id.slice(0,8),16)*1000).toISOString();
}

/* 18-05-2026: Bingo Range
Given a bingo letter, return the number range associated with that letter.

Letter
Number Range

"B"
1-15

"I"
16-30

"N"
31-45

"G"
46-60

"O"
61-75


Return an array with all numbers in the range from smallest to largest. */

function getBingoRange(letter) {
  let letters=["B","I","N","G","O"];
  return Array.from(Array(15).keys()).map((item)=>item+1+letters.indexOf(letter)*15);
}

/* 19-05-2026: Sleep Debt
Given an array of hours slept each night leading up to today, and a target number of hours per night, return how many hours of sleep you need tonight to eliminate your sleep debt.
• Include tonight's hours in the total time needed to catch up.
• If you've slept enough to cover tonight's target or more, return 0. */
function sleepDebt(hoursSlept, targetHours) {
  return Math.max(targetHours+hoursSlept.map((item)=>targetHours-item).reduce((a,b)=>a+b,0),0);
}

/* 20-05-2026: String Zipper
Given two strings, return a new string that interleaves their characters one at a time. If one string is longer, append the remaining characters at the end.
Begin with the first character of the first string. */


function zipStrings(a, b) {
  let res="";
  let mini=Math.min(a.length,b.length);
  for(let i=0;i<mini;i++){
   res+=a[i];
   res+=b[i];
  }
   return a.length>b.length?res+a.slice(mini):res+b.slice(mini);
}

/* 21-05-2026: I Before E
Given a word or sentence, return a corrected version where every word follows the "I before E except after C" rule.
• If a word contains "ei" not preceded by "c", replace it with "ie".
• If a word contains "ie" preceded by "c", replace it with "ei".
• All other words are left unchanged. */

function iBeforeE(sent) {
  let sp=sent.split(" ");
  let s=sp.map((item)=>[item.indexOf("c"),item.indexOf("ei"),item.indexOf("ie")]);
  for(let i=0;i<s.length;i++){
     if(s[i][0]==-1 && s[i][1]>0 || s[i][1]<s[i][0]){
      sp[i]=sp[i].replace("ei","ie");
    }
     if(s[i][0]>0 && s[i][2]>0 && s[i][0]<s[i][2]){
      sp[i]=sp[i].replace("ie","ei");
    }
   }
  return sp.join(" ");
}

/* 22-05-2026: Meeting Time
Given a 3D array representing availability windows for multiple people, return the earliest time where everyone has one hour free. If no such time exists, return "None".
• Each person's availability is an array of [start, end] integer pairs in 24-hour time. For example, [10, 12] would mean the person is available from 10 to 12. Start times range from 0-23, and end times range from 1-24.
For example, given:
json
[
  [[10, 12], [15, 16]], // person 1
  [[11, 14], [15, 16]]  // person 2
]

Return 11, the start of their first shared free hour. */

function isIn(el,arr){
  if(el>=arr[0] && el<arr[1]){
   return true;
  }
  return false;
}

function gimmeSomeTruth(arr){
  for(let i=0;i<arr.length;i++){
  if(arr[i].filter((item)=>item).length==0){
   return false;
   }
  }
  return true;
}

function getMeetingTime(av) {
  let l=av.length;
  let cands=[];
  let fl=av.flat();
  let mini=fl.flat().sort((a,b)=>a-b)[0];
  let maxi=fl.flat().sort((a,b)=>b-a)[0];
  let hlp=[];
  for(let i=mini;i<maxi;i++){
   for(let j=0;j<fl.length;j++){
    hlp.push(isIn(i,fl[j]));
   }
  }
  for(let k=0;k<hlp.length/fl.length;k++){
   let sl=hlp.slice(fl.lengthk,fl.length(k+1));
    if(sl.filter((item)=>item).length==l){
      cands.push(k+mini);
      };
  }
  for(let j=0;j<cands.length;j++){
    let hlp=[];
    for(let i=0;i<l;i++){
      let s=av[i];
      let flt=s.map((item)=>isIn(cands[j],item));
      hlp.push(flt);
      if(gimmeSomeTruth(hlp)) return cands[j];
     }
   }
 return "None";
}

/* 23-05-2026: Open Issues
Given an array of issue numbers and another array of pull request (PR) numbers, return an array of issues that remain open after all PRs have been merged.
• A PR closes an issue if their digits are a rotation of each other. For example, issue 123 would be closed by PR 231 or 312.
• A PR does not close an issue with the exact same number. For example, PR 123 does not close issue 123. So an issue with all the same number can't get closed.
• Either number may have leading zeros stripped. For example, PR 201 would close issue 12 (012, a rotation of 201). Similarily, issue 201 would be closed by PR 12.
Return the remaining open issues in the order they were given. */

function getOpenIssues(issues, prs) {
  let m1=issues.map((item)=>item.toString().split("")).map((item)=>item.map((item)=>item=="0"?"":item));
  let m2=prs.map((item)=>item.toString().split("")).map((item)=>item.map((item)=>item=="0"?"":item));
  let pre=[];
  for(let i=0;i<m2.length;i++){
    pre.push(m2[i].sort());
  }
  pre=pre.map((item)=>item.join(""));
  let hlp=Array.from((new Set(issues)).intersection(new Set(prs)));
  for(let i=0;i<m1.length;i++){
    let s=m1[i].sort();
    if(!pre.includes(s.join(""))){hlp.push(issues[i]);}
   }
  let ind=[];
  for(let i=0;i<hlp.length;i++){
     ind.push(issues.indexOf(hlp[i]));
    }
    return ind.sort((a,b)=>a-b).map((item)=>issues[item]);
}

