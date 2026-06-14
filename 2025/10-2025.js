/* 01-10-2025: Binary to Decimal
Given a string representing a binary number, return its decimal equivalent as a number.

A binary number uses only the digits 0 and 1 to represent any number. To convert binary to decimal, multiply each digit by a power of 2 and add them together. Start by multiplying the rightmost digit by 2^0, the next digit to the left by 2^1, and so on. Once all digits have been multiplied by a power of 2, add the result together.

For example, the binary number 101 equals 5 in decimal because:

1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 4 + 0 + 1 = 5
*/

function toDecimal(binary) {
  let dec=binary.split("").reverse().map((item,index)=>Number(item)*Math.pow(2,index)).reduce((a,b)=>a+b,0);
  return dec;
}
toDecimal("1010")

/* 02-10-2025: Decimal to Binary
Given a non-negative integer, return its binary representation as a string.
*/

function toBinary(decimal) {
  return decimal.toString(2);
}

/* 03-10-2025: P@ssw0rd Str3ngth!
Given a password string, return "weak", "medium", or "strong" based on the strength of the password.

A password is evaluated according to the following rules:

It is at least 8 characters long.
It contains both uppercase and lowercase letters.
It contains at least one number.
It contains at least one special character from this set: !, @, #, $, %, ^, &, or *.
Return "weak" if the password meets fewer than two of the rules. Return "medium" if the password meets 2 or 3 of the rules. Return "strong" if the password meets all 4 rules.
*/

function checkStrength(password) {
  let pw=password;
  let sp=["!","@","#","$","%","^","&","*"];
  let n="0123456789".split("");
  let u=pw.split("").filter((item)=>item.toUpperCase()==item && !n.includes(item) && !sp.includes(item)).length;
  let l=pw.split("").filter((item)=>item.toLowerCase()==item && !n.includes(item) && !sp.includes(item)).length;
  let c1=pw.length>=8;
  let c2=u>=1 && l>=1;
  let c3=pw.split("").filter((item)=>n.includes(item)).length>0;
  let c4=pw.split("").filter((item)=>sp.includes(item)).length>0;
  let arr=[c1,c2,c3,c4];
  let c=[c1,c2,c3,c4].filter((item)=>item).length;
  return c<2?"weak":c<4?"medium":"strong";
}
checkStrength("pass!!!");

/* 04-10-2025: Space Week Day 1: Stellar Classification
October 4th marks the beginning of World Space Week. The next seven days will bring you astronomy-themed coding challenges.

For today's challenge, you are given the surface temperature of a star in Kelvin (K) and need to determine its stellar classification based on the following ranges:

"O": 30,000 K or higher

"B": 10,000 K - 29,999 K

"A": 7,500 K - 9,999 K

"F": 6,000 K - 7,499 K

"G": 5,200 K - 5,999 K

"K": 3,700 K - 5,199 K

"M": 0 K - 3,699 K

Return the classification of the given star.
*/

function classification(temp) {
  return temp>=30000?"O":temp>=10000?"B":temp>=7500?"A":temp>=6000?"F":temp>=5200?"G":temp>=3700?"K":"M";
}

/* 05-10-2025: Space Week Day 2: Exoplanet Search
For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star. Determine if the readings have detected an exoplanet using the transit method. The transit method is when a planet passes in front of a star, reducing its observed luminosity.

Luminosity readings only comprise of characters 0-9 and A-Z where each reading corresponds to the following numerical values:
Characters 0-9 correspond to luminosity levels 0-9.
Characters A-Z correspond to luminosity levels 10-35.
A star is considered to have an exoplanet if any single reading is less than or equal to 80% of the average of all readings. For example, if the average luminosity of a star is 10, it would be considered to have a exoplanet if any single reading is 8 or less.
*/

function hasExoplanet(readings) {
  let s="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
  let arr=s.map((item,index)=>index);
  const res = {};
  s.forEach((key, index) => {
      res[key] = arr[index];
      });
  let avg=readings.split("").map((item)=>res[item]).reduce((a,b)=>a+b,0)/readings.length;
  let flt=readings.split("").filter((item)=>res[item]<=0.8*avg);
  return flt.length>0;
}
hasExoplanet("665544554")

/* 06-10-2025: Space Week Day 3: Phone Home
For day three of Space Week, you are given an array of numbers representing distances (in kilometers) between yourself, satellites, and your home planet in a communication route. Determine how long it will take a message sent through the route to reach its destination planet using the following constraints:

The first value in the array is the distance from your location to the first satellite.
Each subsequent value, except for the last, is the distance to the next satellite.
The last value in the array is the distance from the previous satellite to your home planet.
The message travels at 300,000 km/s.
Each satellite the message passes through adds a 0.5 second transmission delay.
Return a number rounded to 4 decimal places, with trailing zeros removed.
*/

function sendMessage(route) {
  let res=(route.length-1)*0.5;
  let d=route.reduce((a,b)=>a+b,0)/300000;
  let dur=Math.round(10000*(res+d));
  return dur/10000;
}
sendMessage([1000000, 500000000, 1000000]);

/* 07-10-2025: Space Week Day 4: Landing Spot
In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover. Find the safest landing spot based on the following rules:

Each spot in the matrix will contain a number from 0-9, inclusive.
Any 0 represents a potential landing spot.
Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.
The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
Return the indices of the safest landing spot. There will always only be one safest spot.
For instance, given:

[
  [1, 0],
  [2, 0]
]
Return [0, 1], the indices for the 0 in the first array.
*/

function findLandingSpot(matrix) {
  let m=matrix;
  let l=m.length;
  let p=[];
  for(let i=0;i<l;i++){
    for(let j=0;j<l;j++){
      if(m[i][j]==0){
        p.push([i,j]);
      }
    }
  }
  for(let k=0;k<p.length;k++){ let sm=0;
    if(p[k][0]>0){
        sm+=m[p[k][0]-1][p[k][1]];
     } 
    if(p[k][0]<l-1){
        sm+=m[p[k][0]+1][p[k][1]];
      }
    if(p[k][1]>0){
      sm+=m[p[k][0]][p[k][1]-1];
    }
    if(p[k][1]<l-1){
      sm+=m[p[k][0]][p[k][1]+1];
    }
    p[k].push(sm);
  }
  let q=p.sort((a,b)=>a[2]-b[2]);
  let r= q[0];
  let res=[];
  res.push(r[0]);
  res.push(r[1]);
  return res;
}
findLandingSpot([[1,0],[2,0]]);
//findLandingSpot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]);

/* 08-10-2025: Space Week Day 5: Goldilocks Zone
For the fifth day of Space Week, you will calculate the "Goldilocks zone" of a star - the region around a star where conditions are "just right" for liquid water to exist.

Given the mass of a star, return an array with the start and end distances of its Goldilocks Zone in Astronomical Units.

To calculate the Goldilocks Zone:

Find the luminosity of the star by raising its mass to the power of 3.5.
The start of the zone is 0.95 times the square root of its luminosity.
The end of the zone is 1.37 times the square root of its luminosity.
Return the distances rounded to two decimal places.
For example, given 1 as a mass, return [0.95, 1.37].
*/

function goldilocksZone(mass) {
  let lum=Math.pow(mass,3.5);
  let low=0.95*Math.sqrt(lum);
  let high=1.37*Math.sqrt(lum); 
  let zone=[Math.round(100*low)/100,Math.round(100*high)/100];
  return zone;
}
goldilocksZone(0.5);

/* 09-10-2025: Space Week Day 6: Moon Phase
For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and need to determine the phase of the moon for that day using the following rules:

Use a simplified lunar cycle of 28 days, divided into four equal phases:

"New": days 1 - 7
"Waxing": days 8 - 14
"Full": days 15 - 21
"Waning": days 22 - 28
After day 28, the cycle repeats with day 1, a new moon.

Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
You will not be given any dates before the reference date.
Return the correct phase as a string.
*/

function calculateDays(startDate, endDate) {
   let start = new Date(startDate);
   let end = new Date(endDate);
   let timeDifference = end - start;
   let daysDifference = timeDifference / (1000 * 3600 * 24);
   return daysDifference;
  }

function moonPhase(dateString){
  let diff=calculateDays("2000-01-06",dateString);
  let s=(diff+1)%28;
  return s<8?"New":s<15?"Waxing":s<22?"Full":"Waning";
}
moonPhase("2000-01-13");

/* 10-10-2025: Space Week Day 7: Launch Fuel
For the final day of Space Week, you will be given the mass in kilograms (kg) of a payload you want to send to orbit. Determine the amount of fuel needed to send your payload to orbit using the following rules:

Rockets require 1 kg of fuel per 5 kg of mass they must lift.
Fuel itself has mass. So when you add fuel, the mass to lift goes up, which requires more fuel, which increases the mass, and so on.
To calculate the total fuel needed: start with the payload mass, calculate the fuel needed for that, add that fuel to the total mass, and calculate again. Repeat this process until the additional fuel required is less than 1 kg, then stop.
Ignore the mass of the rocket itself. Only compute fuel needed to lift the payload and its own fuel.
For example, given a payload mass of 50 kg, you would need 10 kg of fuel to lift it (payload / 5), which increases the total mass to 60 kg, which needs 12 kg to lift (2 additional kg), which increases the total mass to 62 kg, which needs 12.4 kg to lift - 0.4 additional kg - which is less 1 additional kg, so we stop here. The total mass to lift is 62.4 kg, 50 of which is the initial payload and 12.4 of fuel.

Return the amount of fuel needed rounded to one decimal place.
*/

function launchFuel(payload) {
  let pl=[payload];
  let fuel=[pl[0]/5];
  pl.push(fuel[0]+pl[0]);
  fuel.push(pl[1]/5);
  for(let i=1;i<5;i++){
    pl.push(fuel[i]+pl[0]);
    fuel.push(pl[i+1]/5);
  }
  for(let i=0;i<fuel.length;i++){
    if(fuel[i+1]-fuel[i]<1){
      return Math.round(10*fuel[i+1])/10;
    }
  }
  return payload;
}
launchFuel(243);

/* 11-10-2025: Hex to Decimal
Given a string representing a hexadecimal number (base 16), return its decimal (base 10) value as an integer.

Hexadecimal is a number system that uses 16 digits:

0-9 represent values 0 through 9.
A-F represent values 10 through 15.
Here's a partial conversion table:

Hexadecimal	Decimal
0	0
1	1
...	...
9	9
A	10
...	...
F	15
10	16
...	...
9F	159
A0	160
...	...
FF	255
100	256
The string will only contain characters 0–9 and A–F.
*/

function hexToDecimal(hex) {
   let d={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9};
   let h=hex.split("").reverse().map((item)=>d[item]);
   let c=h.map((item,index)=>Math.pow(16,index)*item).reduce((a,b)=>a+b,0);
   return c;
}
hexToDecimal("2E");

/* 12-10-2025: Battle of Words
Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:

The given sentences will always contain the same number of words.
Words are separated by a single space and will only contain letters.
The value of each word is the sum of its letters.
Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is 26.
A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
A word wins if its value is greater than the opposing word's value.
The team with more winning words is the winner.
Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if both teams have the same number of wins.
*/

function compArr(arr1,arr2){
  let s1=0;
  let s2=0;
  for(let i=0;i<arr1.length;i++){
    if(arr1[i]>arr2[i]){
      s1+=1;
    }
    if(arr2[i]>arr1[i]){
      s2+=1;
    }
  }
  return [s1,s2];
}

function battle(ourTeam, opponent) {
  let alph1="abcdefghijklmnopqrstuvwxyz".split("");
  let alph2=alph1.join("").toUpperCase().split("");
  let arr1=alph1.map((item,index)=>index+1);
  let arr2=alph2.map((item,index)=>2*index+2);  
  let res = {};
  alph1.forEach((key, index) => {res[key] = arr1[index];});
  alph2.forEach((key, index)=>{res[key]=arr2[index];});
  let stri1=ourTeam.split(" "); 
  let stri2=opponent.split(" ");
  let t1=stri1.map((item)=>item.split("").map((sub)=>res[sub]));
  let r1=t1.map((item)=>item.reduce((a,b)=>a+b,0));
  let t2=stri2.map((item)=>item.split("").map((sub)=>res[sub]));
  let r2=t2.map((item)=>item.reduce((a,b)=>a+b,0));
  let c=compArr(r1,r2);
  return c[0]>c[1]?"We win":c[0]<c[1]?"We lose":"Draw";
}
//battle("hello world", "hello word");
battle("We must never surrender", "Our team must win");

/* 13-10-2025: 24 to 12
Given a string representing a time of the day in the 24-hour format of "HHMM", return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".

The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".
*/

function to12(time) {
  let p1=time.slice(0,2);
  let p2=time.slice(2,4);
  let t1=Number(p1)>12?(Number(p1)%12).toString():p1=="00"?"12":p1<10?p1.slice(1,2):p1;
  let d=Number(p1)>12?"PM":"AM";
  return t1+":"+p2+" "+d;
}
to12("0030")
  
/* 14-10-2025: String Count
Given two strings, determine how many times the second string appears in the first.

The pattern string can overlap in the first string. For example, "aaa" contains "aa" twice. The first two a's and the second two.
*/

function count(text, pattern) {
  let l=pattern.length;
  let sn=0;
  for(let i=0;i<text.length-l+1;i++){
    if(text.slice(i,i+l)==pattern){
      sn+=1;
    }
  }
  return sn;
}

/* 15-10-2025: HTML Tag Stripper
Given a string of HTML code, remove the tags and return the plain text content.

The input string will contain only valid HTML.
HTML tags may be nested.
Remove the tags and any attributes.
For example, '<a href="#">Click here</a>' should return "Click here".
*/

function stripTags(html) {
  let txt=html.replace(/<[^>]*>/g,"");
  return txt;
}

/* 16-10-2025: Email Validator
Given a string, determine if it is a valid email address using the following constraints:

It must contain exactly one @ symbol.
The local part (before the @):
Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
Cannot start or end with a dot.
The domain part (after the @):
Must contain at least one dot.
Must end with a dot followed by at least two letters.
Neither the local or domain part can have two dots in a row.
*/

function validate(email) {
  let l="abcdefghijklmnopqrstuvwxyz"; let v0=l+l.toUpperCase()+"0123456789"+"-"+"_"+".";
  let v=v0.split("");
  let alph=v0.slice(0,52).split("");
  let p=email.split("@");
  if(p.length!=2){
    return false;
  }
  let d=email.split(".");
  let flt=d.filter((item)=>item.length!=0);
  if(flt.length<d.length){
    return false;
  }
  let p1=p[0];
  let p2=p[1];
  let ls=p2.split(".")[1];
  if(p1[0]=="." ||p1[p1.length-1]=="."){
    return false;
  }
  let flt2=ls.split("").filter((item)=>!alph.includes(item))
  ;
  if(flt2.length){
    return false;
  }
  return true;
}
validate("example@test.c0")
//validate("hello@world..com")
//validate("git@commit@push.io")

/* 17-10-2025: Credit Card Masker
Given a string of credit card numbers, return a masked version of it using the following constraints:

The string will contain four sets of four digits (0-9), with all sets being separated by a single space, or a single hyphen (-).
Replace all numbers, except the last four, with an asterisk (*).
Leave the remaining characters unchanged.
For example, given "4012-8888-8888-1881" return "****-****-****-1881".
*/

function mask(card) {
  let sp=card.includes("-")?card.split("-"):card.split(" ");
  let mk=sp.map((item,index)=>index<3?"****":item);
  return card.includes("-")?mk.join("-"):mk.join(" ");
}

/* 18-10-2025: Missing Socks
Given an integer representing the number of pairs of socks you started with, and another integer representing how many wash cycles you have gone through, return the number of complete pairs of socks you currently have using the following constraints:

Every 2 wash cycles, you lose a single sock.
Every 3 wash cycles, you find a single missing sock.
Every 5 wash cycles, a single sock is worn out and must be thrown away.
Every 10 wash cycles, you buy a pair of socks.
You can never have less than zero total socks.
Rules can overlap. For example, on wash cycle 10, you will lose a single sock, throw away a single sock, and buy a new pair of socks.
Return the number of complete pairs of socks.
*/

function sockPairs(pairs, cycles) {
  let s=pairs*2;
  s=s-Math.floor(cycles/2);
  s=s+Math.floor(cycles/3);
  s=s-Math.floor(cycles/5);
  s=s+Math.floor(cycles/10)*2;
  if(s<0){
    return 0;
  }
  let p=s%2==0?s/2:Math.floor(s/2);
  return p;
}
sockPairs(1,2);

/* 19-10-2025: HTML Attribute Extractor
Given a string of a valid HTML element, return the attributes of the element using the following criteria:

You will only be given one element.
Attributes will be in the format: attribute="value".
Return an array of strings with each attribute property and value, separated by a comma, in this format: ["attribute1, value1", "attribute2, value2"].
Return attributes in the order they are given.
If no attributes are found, return an empty array.
*/

/* I used the article on "https://www.codemzy.com/blog/get-html-attributes-regex" to find the regular expression used to match */ 
function extractAttributes(element) {
  let sp=element.match(/[\w-]+=".+?"/gm);
  if(!sp){
    return [];
  };
  let res=[];
  for(let i=0;i<sp.length;i++)
  {
    let w=sp[i].split("=");
  let stri=w[0]+", "+w[1].replaceAll('\"',"");
  res.push(stri);
  }
  return res;
}
extractAttributes('<input name="email" type="email" required="true" />');

/* 20-10-2025: Tip Calculator
Given the price of your meal and a custom tip percent, return an array with three tip values; 15%, 20%, and the custom amount.

Prices will be given in the format: "$N.NN".
Custom tip percents will be given in this format: "25%".
Return amounts in the same "$N.NN" format, rounded to two decimal places.
For example, given a "$10.00" meal price, and a "25%" custom tip value, return ["$1.50", "$2.00", "$2.50"].
*/

function mFormatter(stri){
  let s=stri.split(".");
  if(s.length==1){
    return "$"+stri+".00";
  } else if(s[1].length==1){
    return "$"+stri+"0";
  }
  return "$"+stri;
}

function calculateTips(mealPrice, customTip) {
  let mP=Number(mealPrice.slice(1));
  let cT=customTip.split("").reverse().slice(1).reverse().join("")/100;
  console.log(cT);
  let m1=(Math.round(0.15*mP*100)/100).toString();
  let m2=(Math.round(0.2*mP*100)/100).toString();
  let m3=(Math.round(cT*mP*100)/100).toString();
  return [mFormatter(m1),mFormatter(m2),mFormatter(m3)];
}
calculateTips("$10.00", "25%") ;
//calculateTips("$89.67", "26%")

/* 21-10-2025: Thermostat Adjuster 2
Given the current temperature of a room in Fahrenheit and a target temperature in Celsius, return a string indicating how to adjust the room temperature based on these constraints:

Return "Heat: X degrees Fahrenheit" if the current temperature is below the target. With X being the number of degrees in Fahrenheit to heat the room to reach the target, rounded to 1 decimal place.
Return "Cool: X degrees Fahrenheit" if the current temperature is above the target. With X being the number of degrees in Fahrenheit to cool the room to reach the target, rounded to 1 decimal place.
Return "Hold" if the current temperature is equal to the target.
To convert Celsius to Fahrenheit, multiply the Celsius temperature by 1.8 and add 32 to the result (F = (C * 1.8) + 32).
*/

function adjustThermostat(currentF, targetC) {
let targetF = (targetC * 1.8) + 32;
  let diff=(Math.round(10*(targetF-currentF))/10).toString();
  diff=diff.includes(".")?diff:diff+".0";
  return diff>0?`Heat: ${diff} degrees Fahrenheit`:diff<0?`Cool: ${-diff} degrees Fahrenheit`:"Hold";
}
adjustThermostat(72, 18)

/* 22-10-2025: Speak Wisely, You Must
Given a sentence, return a version of it that sounds like advice from a wise teacher using the following rules:

Words are separated by a single space.
Find the first occurrence of one of the following words in the sentence: "have", "must", "are", "will", "can".
Move all words before and including that word to the end of the sentence and:
Preserve the order of the words when you move them.
Make them all lowercase.
And add a comma and space before them.
Capitalize the first letter of the new first word of the sentence.
All given sentences will end with a single punctuation mark. Keep the original punctuation of the sentence and move it to the end of the new sentence.
Return the new sentence, make sure there's a single space between each word and no spaces at the beginning or end of the sentence.
For example, given "You must speak wisely." return "Speak wisely, you must."
*/

function wiseSpeak(sentence) {
let w=["have", "must", "are", "will", "can"];
let s=sentence.split(" ");
let t=s.map((x, i) => [x,i]).filter(([x,i]) => w.includes(x)).map(([x,i]) => i)[0];
console.log(t);
let s1=s.slice(t+1).concat(s.slice(0,t+1));
let s2=s1.map((item)=>item.toLowerCase()).map((item)=>item.replace(".",",")).map((item)=>item.replace("!",",")).map((item)=>item.replace("?",",")).map((item,index)=>index>0?item:item[0].toUpperCase()+item.slice(1));
let last=sentence.split("").reverse()[0];
let stri=s2.join(" ")+last;
  return stri;
}
wiseSpeak("You can do it!")

/* 23-10-2025: Favorite Songs
Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.

Given an array of song objects representing your iPod playlist, return an array with the titles of the two most played songs, with the most played song first.

Each object will have a "title" property (string), and a "plays" property (integer).
*/

function favoriteSongs(playlist) {
  let pl=playlist.sort((a,b)=>b.plays-a.plays);
  let titles=pl.slice(0,2).map((item)=>item.title);
  return titles;
}

/* 24-10-2025: Hidden Treasure
Given a 2D array representing a map of the ocean floor that includes a hidden treasure, and an array with the coordinates ([row, column]) for the next dive of your treasure search, return "Empty", "Found", or "Recovered" using the following rules:

The given 2D array will contain exactly one unrecovered treasure, which will occupy multiple cells.

Each cell in the 2D array will contain one of the following values:

"-": No treasure.
"O": A part of the treasure that has not been found.
"X": A part of the treasure that has already been found.
If the dive location has no treasure, return "Empty".

If the dive location finds treasure, but at least one other part of the treasure remains unfound, return "Found".

If the dive location finds the last unfound part of the treasure, return "Recovered".

For example, given:

[
  [ "-", "X"],
  [ "-", "X"],
  [ "-", "O"]
]
And [2, 1] for the coordinates of the dive location, return "Recovered" because the dive found the last unfound part of the treasure.
*/

function dive(map, coordinates) {
  let fl=map.flat().filter((item)=>item=="O");
  let p=map[coordinates[0]][coordinates[1]];
if(p=="-"){
  return "Empty";
} else if(p=="X" || fl.length>1){
  return "Found";
} else return "Recovered";
}
dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1])

/* 25-10-2025 Complementary DNA
Given a string representing a DNA sequence, return its complementary strand using the following rules:

DNA consists of the letters "A", "C", "G", and "T".
The letters "A" and "T" complement each other.
The letters "C" and "G" complement each other.
For example, given "ACGT", return "TGCA".
*/

function complementaryDNA(strand) {
 let t={"A":"T","T":"A","G":"C","C":"G"};
  return strand.split("").map((item)=>t[item]).join("");
}
complementaryDNA("ACGT")
/* 26-10-2025: Duration Formatter
Given an integer number of seconds, return a string representing the same duration in the format "H:MM:SS", where "H" is the number of hours, "MM" is the number of minutes, and "SS" is the number of seconds. Return the time using the following rules:

Seconds: Should always be two digits.
Minutes: Should omit leading zeros when they aren't needed. Use "0" if the duration is less than one minute.
Hours: Should be included only if they're greater than zero.
*/

function format(seconds) {
  let min=Math.floor(seconds/60)%60;
  let hrs=Math.floor(seconds/3600);
  let sec=seconds-60*min-3600*hrs;
  let _sec=sec<10?"0"+sec.toString():sec.toString();
  let dt="";
  if(hrs==0 && min==0){
    dt+="0:"+_sec.toString();
  } else if(hrs==0){
    dt+=min.toString()+":"+_sec.toString();
  } else {
    if(min<10){
    dt+=hrs.toString()+":0"+min.toString()+":"+_sec.toString();
    } else {
      dt+=hrs.toString()+":"+min.toString()+":"+_sec.toString();
    }
  }
  return dt;
}
format(1);

/* 27-10-2025: Integer Sequence
Given a positive integer, return a string with all of the integers from 1 up to, and including, the given number, in numerical order.

For example, given 5, return "12345".
*/

function sequence(n) {
  let stri=Array.from(Array(n).keys()).map((item)=>item+1).join("");
  return stri;
}

/* 28-10-2025: Navigator
On October 28, 1994, Netscape Navigator was released, helping millions explore the early web.

Given an array of browser commands you executed on Netscape Navigator, return the current page you are on after executing all the commands using the following rules:

You always start on the "Home" page, which will not be included in the commands array.
Valid commands are:
"Visit Page": Where "Page" is the name of the page you are visiting. For example, "Visit About" takes you to the "About" page. When you visit a new page, make sure to discard any forward history you have.
"Back": Takes you to the previous page in your history or stays on the current page if there isn't one.
"Forward": Takes you forward in the history to the page you came from or stays on the current page if there isn't one.
For example, given ["Visit About Us", "Back", "Forward"], return "About Us".
*/

// JavaScript implementation of browser history
// using 2 stacks,
// from "https://www.geeksforgeeks.org/system-design/design-custom-browser-history-based-on-given-operations/"
class BrowserHistory {
    constructor(homepage) {
        this.backStack = [];
        this.forwardStack = [];

        // Initialize object with homepage
        this.backStack.push(homepage);
    }

    // Visit current URL
    visit(url) {
        this.forwardStack = [];
        this.backStack.push(url);
    }

    // 'steps' move backward in history and 
    // return current page
    back(steps) {
        while (this.backStack.length > 1 && steps-- > 0) {
            this.forwardStack.push(this.backStack[
                              this.backStack.length - 1]);
                              
            this.backStack.pop();
        }
        return this.backStack[this.backStack.length - 1];
    }

    // 'steps' move forward and return current page
    forward(steps) {
        while (this.forwardStack.length > 0 && steps-- > 0) {
            this.backStack.push(this.forwardStack[
                             this.forwardStack.length - 1]);
                             
            this.forwardStack.pop();
        }
        return this.backStack[this.backStack.length - 1];
    }
}
                                                                                                                                                                                                                                                                                                                      }
function navigate(commands){                                                                                                                                                                                                                                                                                                      function navigate(commands) {
  let h=new BrowserHistory("Visit Home");
  let c=commands;
  let bf=["Back","Forward"];
  for(let i=0;i<c.length;i++)
  {
      if(!bf.includes(c[i])){
          h.visit(c[i]);  
      }  
      if(c[i]=="Back"){
          h.back(1);
      }
      if(c[i]=="Forward"){
          h.forward(1);
      }         
  }
  return h.backStack[h.backStack.length-1].slice(6);
}
//navigate(["Visit About Us", "Visit Gallery", "Back", "Back"]) ;

/* 29-10-2025: Email Sorter
On October 29, 1971, the first email ever was sent, introducing the username@domain format we still use. Now, there are billions of email addresses.

In this challenge, you are given a list of email addresses and need to sort them alphabetically by domain name first (the part after the @), and username second (the part before the @).

Sorting should be case-insensitive.
If more than one email has the same domain, sort them by their username.
Return an array of the sorted addresses.
Returned addresses should retain their original case.
For example, given ["jill@mail.com", "john@example.com", "jane@example.com"], return ["jane@example.com", "john@example.com", "jill@mail.com"].
*/
                            
function sort(emails) {
  let s=emails.map((item)=>item.split("@")).map((item)=>item[1]+"/"+item[0]);
  let t= s.sort(function (a, b) {
      return a.toLowerCase().localeCompare(b.toLowerCase());
      });
  let r=s.map((item)=>item.split("/")).map((item)=>item[1]+"@"+item[0]);
  return r;
}
sort(["jill@mail.com", "john@example.com", "jane@example.com"]);

/* 30-10-2025 Nth Prime
A prime number is a positive integer greater than 1 that is divisible only by 1 and itself. The first five prime numbers are 2, 3, 5, 7, and 11.

Given a positive integer n, return the nth prime number. For example, given 5 return the 5th prime number: 11.
*/

function isPrime(num){
  for(let i = 2, s = Math.sqrt(num); i <= s; i++) {
    if(num % i === 0) return false;
    }
  return num > 1;
}
function nthPrime(n) {
  let p=[];                  
  for(let i=2;i<8000;i++){
    if(isPrime(i)){
      p.push(i);
    }
  }
  return p[n-1];
}

/* 31-10-2025: SpOoKy~CaSe
Given a string representing a variable name, convert it to "spooky case" using the following constraints:

Replace all underscores (_), and hyphens (-) with a tilde (~).
Capitalize the first letter of the string, and every other letter after that, ignore the tilde character when counting.
For example, given hello_world, return HeLlO~wOrLd.
*/

function alterCase(stri,v){
  let s=stri.split("");
  let st;
  if(v==0){
     st=s.map((item,index)=>index%2==0?item.toUpperCase():item.toLowerCase());
  } else {
    st=s.map((item,index)=>index%2==1?item.toUpperCase():item.toLowerCase());
  }
  return st.join("");
}
alterCase("hello",1);

function spookify(boo) {
  let b=boo.replaceAll("-","~").replaceAll("_","~").split("~");
  let c=b.map((item)=>item.length);
  let sn=[];
  for(let i=1;i<c.length;i++){
    sn.push(c.slice(0,i).reduce((a,b)=>a+b,0));
  }
 let stri=alterCase(b[0],0)+"~";
  let d=b.slice(1);
  let arr=[];
  for(let i=0;i<d.length;i++){ arr.push(alterCase(d[i],sn[i]%2));}
  return stri+arr.join("~");
}
spookify("TRICK-or-TREAT")
