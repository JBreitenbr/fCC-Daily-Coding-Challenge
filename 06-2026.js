/* 01-06-2026: Schema Validator Part 1
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
json
{
  username: string
}

• Extra keys are allowed */

function isValidSchema(obj) {
  let k=Object.keys(obj);
  let ind=k.indexOf("username");
  return typeof obj[k[ind]]=="string";
}

/* 02-06-2026: Schema Validator Part 2
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
json
{
  username: string,
  posts: number,
  verified: boolean
}

• Extra keys are allowed */
function isValidSchema(obj) {
  let c1=Object.keys(obj).includes("username")?typeof obj["username"]=="string":false;
  let c2=Object.keys(obj).includes("posts")?typeof obj["posts"]=="number":false;
  let c3=Object.keys(obj).includes("verified")? typeof obj["verified"]=="boolean":false;
  return c1&&c2&&c3;
}

/* 03-06-2026: Schema Validator Part 3
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
json
Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles
}

• The pipe (|) symbol means "or". role must be one of the listed Roles values.
• Extra keys are allowed */

function isValidSchema(obj) {
  let roles = ["user","creator","moderator","staff","admin"];
  let k=Object.keys(obj);
  let v=Object.values(obj);
  let c1=typeof v[k.indexOf("username")]=="string";
  let c2=typeof v[k.indexOf("posts")]=="number";
  let c3=typeof v[k.indexOf("verified")]=="boolean";
  let c4=roles.includes(v[k.indexOf("role")]);
  return c1&&c2&&c3&&c4;
}

/* 04-06-2026: Schema Validator Part 4
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
json
Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean
}

• The pipe (|) symbol means "or". role must be one of the listed Roles values.
• The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
• Extra keys are allowed */

function isValidSchema(obj) {
  let roles = ["user","creator","moderator","staff","admin"];
  let k=Object.keys(obj);
  let v=Object.values(obj);
  let c1=typeof v[k.indexOf("username")]=="string";
  let c2=typeof v[k.indexOf("posts")]=="number";
  let c3=typeof v[k.indexOf("verified")]=="boolean";
  let c4=roles.includes(v[k.indexOf("role")]);
  let ind=k.indexOf("supporter");
  let c5=ind>=0?typeof v[ind]=="boolean":true;
  return c1&&c2&&c3&&c4&&c5;
}

/* 05-06-2026: Schema Validator Part 5
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
json
Roles = "user" | "creator" | "moderator" | "staff" | "admin"

{
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean,
  badges: string[]
}

• The pipe (|) symbol means "or". role must be one of the listed Roles values.
• The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
• The brackets [] after string means that badges should be an array of strings (or empty).
• Extra keys are allowed  */

function isValidSchema(obj) {
  let roles = ["user","creator","moderator","staff","admin"];
  let k=Object.keys(obj);
  let v=Object.values(obj);
  let c1=typeof v[k.indexOf("username")]=="string";
  let c2=typeof v[k.indexOf("posts")]=="number";
  let c3=typeof v[k.indexOf("verified")]=="boolean";
  let c4=roles.includes(v[k.indexOf("role")]);
  let ind1=k.indexOf("supporter");
  let c5=ind1>=0?typeof v[ind1]=="boolean":true;
  let ind2=k.indexOf("badges");
  let c6=ind2>=0?v[ind2].every((item)=> typeof item=="string"):typeof v[ind2]=="object";
  return c1&&c2&&c3&&c4&&c5&&c6;
}

/* 06-06-2026: Schema Validator Part 6
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
json
Roles = "user" | "creator" | "moderator" | "staff" | "admin"

UserProfile = {
  username: string,
  posts: number,
  verified: boolean,
  role: Roles,
  supporter?: boolean,
  badges: string[]
}

{
  users: UserProfile[]
}

• The pipe (|) symbol means "or". role must be one of the listed Roles values.
• The question mark (?) after supporter means that the field is optional, but is the specified type if it exists.
• UserProfile[] denotes an array of UserProfile objects. An empty array is valid.
• Extra keys are allowed */

function checkObj(obj){
  let roles = ["user","creator","moderator","staff","admin"];
  let k=Object.keys(obj);
  let v=Object.values(obj);
  let c1=typeof v[k.indexOf("username")]=="string";
  let c2=typeof v[k.indexOf("posts")]=="number";
  let c3=typeof v[k.indexOf("verified")]=="boolean";
  let c4=roles.includes(v[k.indexOf("role")]);
  let ind1=k.indexOf("supporter");
  let c5=ind1>=0?typeof v[ind1]=="boolean":true;
  let ind2=k.indexOf("badges");
  let c6=ind2>=0?v[ind2].every((item)=> typeof item=="string"):typeof v[ind2]=="object";
  return c1&&c2&&c3&&c4&&c5&&c6;
}

function isValidSchema(obj) {
  if(obj["users"].length==0){return true;}
  else if(obj["users"][0]==undefined ){return false;}
  else{
   return obj["users"].every((item)=>checkObj(item));}
}

/* 07-06-2026: Last Load
Given the number of scoops of laundry detergent you have remaining and an array of how many scoops you used in each of the previous days, return the number of full days of detergent you have remaining.
Calculate your average daily usage from the usage history and assume that amount of usage each day going forward. */

function lastLoadDate(scoops, usage) {
  return Math.floor(scoops/(usage.reduce((a,b)=>a+b,0)/usage.length));
}

/* 08-06-2026: Jet Lagged
Given a departure city, an arrival city, a flight duration in hours, and a direction of travel, return the number of jet lag hours the traveller is experiencing.
The given cities will be from the following list that includes their UTC offset:

City
Offset

"Los Angeles"
-8

"New York"
-5

"London"
0

"Istanbul"
+3

"Dubai"
+4

"Hong Kong"
+8

"Tokyo"
+9


To calculate jet lag hours:
1. Find the timezone difference in hours between the two cities.
2. Determine the direction multiplier. If travelling "east", it's 1.5, otherwise, it's 1.0.
3. Get the jet lag hours with the formula: timezone difference + (flight duration * 0.1) * direction multiplier
Return the jet lag hours rounded to one decimal place.  */

function getJetLagHours(departureCity, arrivalCity, flightDuration, direction) {
  let obj={"Los Angeles":-8,"New York":-5,"London":0,
           "Istanbul":3,"Dubai":4,"Hong Kong":8,"Tokyo":9};
  let tDiff=Math.abs(obj[departureCity]-obj[arrivalCity]);
  let dm=direction=="east"?1.5:1;
  return tDiff+0.1*flightDuration*dm;
}

/* 09-06-2026: Roommates
Given an array of people and their roommate group, return the room assignments for a hotel stay using the following rules:
• Each person has a name and a group property:
json
[
  { "name": "Alice", "group": "A" },
  { "name": "Bob", "group": "B" },
  { "name": "Carol", "group": "A" }
]

• People can only share a room with someone from the same group and are paired in the order they are given.
• Return an array of strings with names separated by " and " for a shared room, and just the name for a solo room. Names must appear in the order they were paired. For the example above, return ["Alice and Carol", "Bob"]. */

function rHlp(arr){
  let res=[];
  for(let i=0;i<arr.length;i=i+2){
    let sl=arr.slice(i,i+2).join(" and ");
    res.push(sl);
  }
  return res;
}

function getRoommates(people) {
  let m=people.map((item)=>item.group).sort().join("");
  let s=Array.from(new Set(people.map((item)=>item.group)));
  let obj={};
  for(let i=0;i<s.length;i++){
    obj[s[i]]=[];
  }
  for(let i=0;i<people.length;i++){
   for(let j=0;j<s.length;j++){
    if(people[i].group==s[j]){
       obj[s[j]].push(people[i].name);
    }
   }
  }
  let res=[];
  let k=Object.keys(obj);
  for(let i=0;i<k.length;i++){
    res.push(rHlp(obj[k[i]]));
  }
  return res.flat();
}

/* 10-06-2026: Itinerary Arrangements
Given an array of at least two optional stops for a day trip, return the number of valid itinerary arrangements.
The itinerary always includes "breakfast", "lunch", and "dinner", these will not be passed in as arguments. The optional stops can be placed anywhere in the itinerary, subject to the following rules:
• "breakfast" is always first, with at least one stop before "lunch".
• "lunch" must appear before "dinner", with at least one stop in between.
• At most, one optional stop may appear after "dinner".
Return the number of valid arrangements. */

function comb(arr){
  let res = [[]];
  for(let num of arr) {
   const temp = [];
   for (let arr of res) {
    for (let i = 0; i <= arr.length; i++) {
      const newArr = [...arr];
      newArr.splice(i, 0, num);
      temp.push(newArr);
    }
   }
    res = temp;
  }
  return res;
}

function getItineraryCount(stops) {
  stops.push("lunch");
  stops.push("dinner");
  let combis=comb(stops).filter((item)=>!["lunch","dinner"].includes(item[0])&&item.indexOf("dinner")-item.indexOf("lunch")>=2&&item.indexOf("lunch")>=1&&item.indexOf("dinner")>=item.length-2);
  return combis.length;
}

/* 11-06-2026: Idea Rankings
Given a 2D array where each inner array contains (in this order) an idea name, an optimistic estimate, a realistic estimate, and a pessimistic estimate (in days), return an array of the idea names sorted by expected time to completion, shortest first.
Calculate the expected time to completion for each idea using the following formula:
• expected = ((optimistic + 4 * realistic + pessimistic) / 6) * length of idea name  */
function analyzeIdeas(ideas) {
  let m=ideas.map((item)=>(item[1]+4item[2]+item[3])/6item[0].length);
  let s=m.slice(0).sort((a,b)=>a-b);
  let res=[];
  for(let i=0;i<
    s.length;i++){
    res.push(ideas[m.indexOf(s[i])][0]);
  }
  return res;
}

/* 12-06-2026: HTML Content Extractor
Given a string of HTML, return the plain text content with all tags removed. */

function extractContent(html) {
  return html.replace(/<[^>]*>/g, '');
}

/* 13-06-2026: Zoning Regulations
Given a 2D grid (array of arrays) representing a city's building layout, return the coordinates of all buildings that are violating zoning rules.
Each cell in the grid contains one of the labels from the table below. A building is in violation if any of its (up to) 4 neighbors, horizontal or vertical, are a type it cannot be adjacent to.

Label
Type
Cannot be adjacent to

"i"
industrial
"R", "I"

"A"
Agricultural
"C"

"R"
Residential
"i", "C"

"I"
Institutional
"i"

"C"
Commercial
"R", "A"

"" (empty string)
undeveloped
no restrictions


Return the coordinates of all violating cells as an array of [row, col] pairs, in any order. If no violations exist, return an empty array. */

function  moves(i, j){
return [[i - 1, j],[i , j - 1],[i , j + 1],[i + 1, j ]];
}

 function getZoneViolations(grid) {
  let restr={
"i":["R", "I"],"A":"C",
"R":["i", "C"],"I":"i",
"C":["R", "A"]};
  let r=grid.length;
  let c=grid[0].length;
  let res=[];
  for(let i=0;i<r;i++){
    for(let j=0;j<c;j++){
  let pre=moves(i,j);
  let flt=grid[i][j]==""?"":pre.filter((item)=>item[0]>=0&&item[1]>=0&&item[0]<r&&item[1]<c).map((item)=>item==""?"":grid[item[0]][item[1]]).filter((item)=>restr[grid[i][j]].includes(item)&&item!="");
  if(flt.length>0){res.push([i,j]);}
    }
  }
  return res;
}

/* 14-06-2026: Credit Card Validator
Given a string of digits for a credit card number, determine if it's a valid card number using the following method:
• Starting from the second-to-last digit, double every other digit moving left.
• If doubling a digit results in a number greater than 9, subtract 9.
• Sum all the digits (doubled and undoubled).
• If the total is divisible by 10, the number is valid. */

function isValidCard(number) {
  return (number.split("").reverse().slice(1).map((item,index)=>index%2==0?2*parseInt(item):parseInt(item)).map((item)=>item>9?item-9:item).reduce((a,b)=>a+b,0)+parseInt(number[number.length-1]))%10==0;
}

/* 15-06-2026: Number Sort
Given a string of numbers separated by commas, return an array of the numbers sorted from smallest to largest. */

function sortNumbers(str) {
  return str.split(",").map((item)=>Number(item)).sort((a,b)=>a-b);
}

/* 16-06-2026: British to American
Given a sentence, convert any British English spellings to their American English equivalents using the following lookup table and return the updated sentence:

British
American

"colour"
"color"

"flavour"
"flavor"

"honour"
"honor"

"neighbour"
"neighbor"

"labour"
"labor"

"humour"
"humor"

"centre"
"center"

"fibre"
"fiber"

"defence"
"defense"

"offence"
"offense"

"organise"
"organize"

"recognise"
"recognize"

"analyse"
"analyze"


• Replacements should be case-insensitive. For example, "Colour" should become "Color".
• The input may contain words that build on the exact spelling of a root in the table that also need to be changed. For example, "colouring" should become "coloring", and "disorganised" should become "disorganized". */

function britishToAmerican(sentence) {
  let brit=["colour","flavour","honour","neighbour","labour","humour","centre","fibre","defence","offence","organise","recognise","analyse"];
  let ami=["color","flavor","honor","neighbor","labor","humor","center","fiber","defense","offense","organize","recognize","analyze"];
  for(let i=0;i<brit.length;i++){
    sentence=sentence.replaceAll(brit[i],ami[i]);
  }
  return sentence;
}

/* 17-06-2026: Spellcaster
Given a string of spell codes you are casting, calculate the total score.
Each character in the string represents a spell:

Code
Spell
Category
Base Score

"f"
Fire
Destruction
3

"l"
Lightning
Destruction
3

"i"
Ice
Control
2

"w"
Wind
Control
2

"h"
Heal
Restoration
1

"s"
Shield
Restoration
1


A combo multiplier is applied based on how many spells in a row have been cast from different categories:
• The first spell always scores at base value.
• Each consecutive spell from a different category than the previous increases the multiplier by 1.
• Casting a spell from the same category as the previous resets the multiplier back to 1.
• The score for each spell is its base score multiplied by the current multiplier.
Return the total score from the sequence of spells. */

function cast(spells) {
  let c="fliwhs";
  let s=["Fire","Lightning","Ice","Wind","Heal","Shield"];
  let cat=["Destruction","Destruction","Control","Control","Restoration","Restoration"];
  let b=[3,3,2,2,1,1];
  let base=spells.split("").map((item)=>b[c.indexOf(item)]);
  let cats=spells.split("").map((item)=>cat[c.indexOf(item)]);
  let sn=base[0];
  let m=1;
  for(let i=1;i<spells.length;i++){
    if(cats[i]!=cats[i-1])
    { m+=1; }
    if(cats[i]==cats[i-1])
    { m=1; }
    sn+=base[i]*m;
   }
  return sn;
}

/* 18-06-2026: Streaming Cost
Given an array representing movies in the cart of your streaming service, and a string for your subscription tier, return the total cost of the movies.
Each item in the cart is an object with a "format" ("HD" or "4K") and a "type" ("rent" or "buy"). Their costs are:


"rent"
"buy"

"HD"
$3.99
$12.99

"4K"
$5.99
$19.99


Apply the following subscription tier discounts:
• "none": full price
• "basic": 10% off
• "premium": 25% off
Return the total cost rounded to two decimal places in the format "$D.CC".*/

function getStreamingBill(cart, subscription) {
  let m=cart.map((item)=>item.format=="HD" && item.type=="rent"?3.99:item.format=="HD" && item.type=="buy"?12.99:item.format=="4K"&& item.type=="rent"?5.99:19.99).reduce((a,b)=>a+b,0);
  let c=subscription=="none"?m:subscription=="basic"?0.9m:0.749999m;
  let res="$"+(Math.round(100*c)/100).toFixed(2);
  return res;
}

/* 19-06-2026: Rental Cost
Given a rental timestamp, a return timestamp, and a rental tier, return the total cost of the rental including any late fees.
• Given timestamps are UTC ISO strings, for example: "2026-06-18T18:30:00Z".
• The rental tier is the number of days before the rental is due back: 1, 3, or 7.
• Rentals are due back by 12:00 PM UTC or earlier on the last day of the rental period. For example, a 1-day rental checked out at any time on March 15 is due back by 12:00 PM UTC on March 16.
• Each day past the due date and time incurs a late fee.
Pricing is as follows:

Tier
Base cost
Late fee per day

1 day
$4.99
$3.99

3 days
$3.99
$2.99

7 days
$2.99
$0.99


Return the total cost rounded to two decimal places in the format "$D.CC". */

function getRentalCost(rented, returned, tier) {
  let d={1:{"base":4.99,"late":3.99},3:{"base":3.99,"late":2.99},7:{"base":2.99,"late":0.99}}
  let m=parseInt(returned.slice(14,16))+parseInt(returned.slice(11,13))60;
  let date1 = new Date(rented.slice(0,10));
  let date2 = new Date(returned.slice(0,10));
  // Differenz in Millisekunden berechnen
  let diffInMs = Math.abs(date2 - date1);
  // Millisekunden in Tage umrechnen (1000ms * 60s * 60m * 24h)
  let diffInDays = diffInMs / (1000 * 60 * 60 * 24);
  let z=m<=720?Math.max(diffInDays-tier,0):Math.max(diffInDays-tier+1,0);
  let ges=d[tier]["base"]+zd[tier]["late"];
  return "$"+ges.toFixed(2);
}

/* 20-06-2026: Prime Factorization
Given an integer greater than 1, return its prime factorization as an array of numbers in ascending order.
A prime factorization is the set of prime numbers that multiply together to produce the given integer. Each number has exactly one set. For example, the prime factorization of 20 is [2, 2, 5] because 2 * 2 * 5 = 20.
If the given integer is itself prime, return it in a single-element array. */

function isPrime(n){
  let arr=Array.from(Array(n).keys()).map((item)=>item+1).filter((item)=>n%item==0).slice(1);
  return arr[0]==n;
}

function primeFactorization(n) {
  let arr=Array.from(Array(n).keys()).map((item)=>item+1).filter((item)=>n%item==0).filter((item)=>isPrime(item));
  let res=[];
  for(let i=0;i<3;i++){
   for(let j=0;j<arr.length;j++){
    if(n%arr[j]==0) {res.push(arr[j]);
      n=n/arr[j];
    }
   }
  }
   return res.sort((a,b)=>a-b);
}

/* 21-06-2026: Summer Solstice
Today is the summer solstice, the longest day of the year in the Northern Hemisphere and the shortest in the Southern. Given a latitude, return a string representing daytime and nighttime hours.
• The latitude will be between 90 (north pole) and -90 (south pole), inclusive
• The number of daytime hours = 12 + (latitude / 90) * 12
• Round the daytime hours to the nearest even number
Return a 24-character string using "☀️" for daytime hours and "🌑" for nighttime hours, where:
• Each character represents one hour, starting at midnight (hour 0)
• Sunrise and sunset fall symmetrically around noon
For example, a latitude of 0 (the equator) has 12 hours of daylight, so sunrise is at 6:00 AM and sunset is at 6:00 PM. Return: "🌑🌑🌑🌑🌑🌑☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️🌑🌑🌑🌑🌑🌑". */

function getDaytimeHours(latitude) {
  let res="";
  let pre=12 + (latitude / 90) * 12;
  let dtHours=Math.round(pre)%2==0?Math.round(pre):Math.floor(pre)%2==0?Math.floor(pre):Math.round(pre)+1;
  let st=(24-dtHours)/2;if (latitude==90) {return "☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️☀️";}
  else {
    for(let i=0;i<st;i++){
      res+="🌑";
    }
    for(let i=0;i<dtHours;i++){
      res+="☀️";
    }
   for(let i=0;i<st;i++){
     res+="🌑";
   }
 }
 return res;
}

/* 22-06-2026: 1337 Speak
Given a lowercase string, return it translated into leet speak by replacing the letters below with their leet substitutions:

Letter
Leet

a
4

e
3

g
9

i
1

l
1

o
0

s
5

t
7


• Characters with no substitution are left unchanged. */
function makeLeet(str) {
  let letter="aegilost";
  let leet="43911057";
  return str.split("").map((item)=>letter.indexOf(item)==-1?item:leet[letter.indexOf(item)]).join("");
}

/* 23-06-2026: BMI Calculator
Given a weight in pounds and a height in inches, return the BMI (Body Mass Index) rounded to one decimal place.
To get BMI: divide the weight by the height squared, then multiply the result by 703. */

function calculateBmi(weight, height) {
  return Math.round(10*weight/(height*height)*703)/10;
}

/* 24-06-2026: DNA Mutations
Given two DNA strands of equal length, return an array of indexes where the strands differ (mutations).
• DNA strands are strings made up of the characters "A", "T", "C", and "G"
• Return the indexes in ascending order
• If there are no mutations, return an empty array */
function detectMutations(strand1, strand2) {
return strand1.split("").map((item,index)=>item!=strand2[index]).flatMap((val, idx) => val?idx:[]);
}

/* 25-06-2026: Frontmatter Parser
Given a string representing a frontmatter block, parse it and return an object (JavaScript) or dictionary (Python) with the keys and values.
Frontmatter is wrapped in --- delimiters and contains key: value pairs within them, one per line. For example:
md
---
title: My Post
draft: false
views: 100
---

Should return:
js
{
  title: "My Post",
  draft: false,
  views: 100
}

• Numbers, Booleans, and Strings should all be returned as their respective type.
• The given string will have new lines separated with the newline character ("\n"). The above example would be given as: "---\ntitle: My Post\ndraft: false\nviews: 100\n---".  */

function parseFrontmatter(str) {
  let r1=/[0-9]+/gi;
  let r2=/[A-Za-z]+/gi;
  let k=str.split("\n").filter((item)=>item!="---").map((item)=>item.split(": ")[0]);
  let v=str.split("\n").filter((item)=>item!="---").map((item)=>item.split(": ")[1]).map((item)=>item=="false"?false:item=="true"?true:item).map((item)=>r1.test(item) && !r2.test(item) && item.split(".").length<=2?Number(item):item);
  let res={};
  for(let i=0;i<k.length;i++){
   res[k[i]]=v[i];
   }
   return res;
}

/* 26-06-2026: Blood Bank
Given an array of the inventory at a blood bank and an array of patient blood type requests, return a string in the format "X of Y patients served". Where X is the maximum number of patients that can receive blood from the bank's inventory, and Y is the total number of patients.
Each entry in both arrays is one of the following blood types: "AB", "A", "B", or "O".
Compatibility rules:
• "AB" can receive from any blood type.
• "A" can receive from "A" and "O".
• "B" can receive from "B" and "O".
• "O" can only receive from "O".
Duplicate entries in the given arrays represent quantity. */

function triageBlood(bank, patients) {
  let p={"O":["O"],"A":["A","O"],"B":["B","O"],"AB":["AB","A","B","O"]};
  let d={"O":0,"A":0,"B":0,"AB":0};
  for(let i=0;i<bank.length;i++){
    d[bank[i]]+=1;
  }
  let sn=0;
  for(let i=0;i<patients.length;i++){
   for(let j=0;j<p[patients[i]].length;j++)
   {
     if(d[p[patients[i]][j]]){
      d[p[patients[i]][j]]-=1;
      sn+=1;
      continue;
     }
   }
  }
  return ${sn} of ${patients.length} patients served;
}

/* 27-06-2026: Periodic Spelling
Given a word, determine if it can be spelled using element symbols from the periodic table.
• Ignore casing when spelling a word. "neon" can be spelled with the symbols "Ne", "O", and "N".
Here's a full list of the element symbols:
json
["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"];

Return an array of the elements used to spell the word, in their original casing and in the order to spell the word. Or, an empty array if it can't be spelled. */

const subsets = ([x, ...xs]) =>
   x == undefined? [[]] : subsets (xs) .flatMap (ss => [ss, [x, ...ss]]);

function indices(source, find) {
  let res=[];
  let l=find.length;
  for (let i = 0; i < source.length; i++) {
   if (find==source.substring(i, i+l)) {
       res.push(i);
     }
   }
   return res;
}

function getPeriodicSpelling(word) {
let arr=["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"];
let arr2=arr.map((item)=>item.toLowerCase());
let hlp=[];
for(let i=0;i<arr2.length;i++){
let c=indices(word,arr2[i]);
if(c.length>=1){
hlp.push([arr2[i],c,i]);
};
}
let hlp1=hlp.map((item)=>[item[0],Math.min(...item[1]),item[2]]).sort((a,b)=>a[1]-b[1]);
let hlp2=hlp.map((item)=>[item[0],Math.max(...item[1]),item[2]]).sort((a,b)=>a[1]-b[1]);
let flt1=subsets(hlp1).filter((item)=>item.map((item)=>item[0]).join("")==word);
let flt2=subsets(hlp2).filter((item)=>item.map((item)=>item[0]).join("")==word);
if(flt1.length==0 && flt2.length==0){
return [];
} else if(flt1.length==0){
return flt2[0].map((item)=>arr[item[2]]);
}
else return flt1[0].map((item)=>arr[item[2]]);
}

/* 28-06-2026: Connect 3
Given a matrix of strings representing pieces on a game grid, determine if any player has three in a row.
• Each cell contains "R", "Y", or "" (empty string).
• Three in a row means three consecutive non-empty cells of the same type horizontally, vertically, or diagonally.
Return:
• A flat array with the winner and the coordinates of their three winning cells in the format: ["R", [0,2], [1,3], [2,4]]. Coordinates are returned top-to-bottom, then left-to-right.
• An empty array if there is no winner. */

function connectThree(matrix) {
  let h0=[[[0,0],[0,1],[0,2]],[[0,1],[0,2],[0,3]],[[1,0],[1,1],[1,2]],[[1,1],[1,2],[1,3]],[[2,0],[2,1],[2,2]],[[2,1],[2,2],[2,3]],[[3,0],[3,1],[3,2]],[[3,1],[3,2],[3,3]]];
  let h=h0.map((item)=>item.map((item)=>item.join("")));
  let v=h.map((item)=>item.map((item)=>item.split("").reverse().join("")));
  let d=[["00","11","22"],["01","12","23"],["10","21","32"],["11","22","33"],["02","11","20"],["03","12","21"],["12","21","30"],["13","22","31"]];
  let arr=[...v,...h,...d];
  let y=[];
  let r=[];
  let res=[];
  for(let i=0;i<4;i++){
   for(let j=0;j<4;j++){
    if(matrix[i][j]=="Y"){
      y.push([i,j].join(""));
    }
    if(matrix[i][j]=="R"){
     r.push([i,j].join(""));
    }
  }
}
for(let i=0;i<arr.length;i++){
   let s1=(new Set(arr[i])).intersection(new Set(r));
   let s2=(new Set(arr[i])).intersection(new Set(y));
   if(Array.from(s1).length==3){
     res=Array.from(s1).map((item)=>item.split("")).map((item)=>item.map((item)=>parseInt(item)));
     res.unshift("R");
   }
   if(Array.from(s2).length==3){
     res=Array.from(s2).map((item)=>item.split("")).map((item)=>item.map((item)=>parseInt(item)));
     res.unshift("Y");
   }
 }
   return res;
}

/* 29-06-2026: Song Mood Finder
Given a genre string and a BPM number for a song, determine the mood using the following table:

Mood
Genre
BPM Range

"focus"
"classical"
60–109

"focus"
"electronic"
60–89

"happy"
"pop"
60–180

"happy"
"classical"
110–180

"happy"
"rock"
60–129

"happy"
"electronic"
90–134

"hype"
"rock"
130–180

"hype"
"electronic"
135–180


*/

function getMood(genre, bpm) {
  return genre=="pop"||genre=="classical" && bpm>=110 ||genre=="rock"&& bpm<130 || genre=="electronic"&&bpm>=90 && bpm<135?"happy":genre=="classical" && bpm<110 || genre=="electronic"&&bpm<90?"focus":"hype";
}

/* 30-06-2026: Duplicate Character Count
Given two strings, return a count of characters from the second string that can be found in the first.
• Duplicate characters in the second string are counted separately. */

function duplicateCharacterCount(str1, str2) {
  return str2.split("").filter((item)=>str1.includes(item)).length;
}
