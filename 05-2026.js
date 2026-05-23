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

