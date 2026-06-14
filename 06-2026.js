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

function moves(i, j){
  return [[i - 1, j],[i , j - 1],[i , j + 1],[i + 1, j ]];
}

function getZoneViolations(grid) {
  let restr={"i":["R", "I"],"A":"C","R":["i", "C"],"I":"i","C":["R", "A"]};
  let r=grid.length;
  let c=grid[0].length;
  let res=[];
  for(let i=0;i<r;i++){
    for(let j=0;j<c;j++){
      let pre=moves(i,j);
      let flt=grid[i][j]==""?"":pre.filter((item)=>item[0]>=0&&item[1]>=0&&item[0]<r&&item[1]<c).map((item)=>item==""?"":grid[item[0]][item[1]]).filter((item)=>restr[grid[i][j]].includes(item)&&item!="");if grid[i][j] == "": flt = "" else: flt = [] for item in pre: # 1. Prüfen, ob die Koordinaten im Grid liegen if 0 <= item[0] < r and 0 <= item[1] < c: val = grid[item[0]][item[1]] # 2. Prüfen, ob der Wert gültig und in den Restriktionen erlaubt ist if val != "" and val in restr[grid[i][j]]: flt.append(val)
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

