/* 01-07-2026: Lucky Number
Given a string of a person's first and last name, calculate their lucky number using the following rules:
• First and last names are separated by a space
• Find the vowel and consonant count for each name
• Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name
• Do the same for the two larger counts and the larger name
• Subtract the smaller value from the larger one to get their lucky number
If the final value is zero (0), return 13. */

function getLuckyNumber(name) {
  let sp=name.split(" ");
  let arr=[];
  for(let i=0;i<2;i++){
    arr.push(sp[i].split("").filter((item)=>"aeiou".includes(item.toLowerCase())?1:0).length);
    arr.push(sp[i].split("").filter((item)=>"aeiou".includes(item.toLowerCase())?0:1).length);
  }
  let c1=Math.min(arr[0],arr[2])*Math.min(arr[1],arr[3])*Math.min(sp[0].length,sp[1].length);
  let c2=Math.max(arr[0],arr[2])*Math.max(arr[1],arr[3])*Math.max(sp[0].length,sp[1].length);
  return c1==c2?13:c1<c2?c2-c1:c1-c2;
}

/* 02-07-2026: Max Profit
Given an array of daily stock prices and a budget (in dollars), calculate the maximum profit you could make by buying and selling the stock over the given period.
• You may only sell after you buy.
• You may perform at most one buy and one sell transaction. Once you sell, you cannot buy again.
• You can only buy whole shares.
• Return the maximum possible profit as a string, rounded down to the nearest cent and formatted to two decimal places. */
• 
function getMaxProfit(prices, budget) {
  let maxProfit = 0;
  for (let i = 0; i < prices.length; i++) {
    for (let j = i + 1; j < prices.length; j++) {
      if (prices[j] > prices[i]) {
         let shares = Math.floor(budget / prices[i]);
         let profit = shares * (prices[j] - prices[i]);
         if (profit > maxProfit) {
            maxProfit = profit;
         }
       }
     }
  }
  return (Math.floor(maxProfit * 100)/ 100).toFixed(2);
}

/* 03-07-2026: Database Migration
Given two database objects, return the second object with any missing properties from the first filled in.
• Fields that already exist in the record should not be overwritten. */
function migrateRecord(schema, record) {
  let k=Object.keys(record);
  let res=schema;
  for(let i=0;i<k.length;i++){
      res[k[i]]=record[k[i]];
  }
   return res;
}

/* 04-07-2026: Kaprekar's Routine
Given a 4-digit number, return the number of times you need to apply Kaprekar's routine until reaching 6174.
Kaprekar's routine works as follows:
• Arrange the digits in descending order to form the largest number
• Arrange the digits in ascending order to form the smallest number (pad with leading zeros if necessary)
• Subtract the smaller from the larger
• Repeat with the new number */

function kaprekar(n) {
  let s=n;
  for(let i=0;i<7;i++){
     let mini=Number(s.toString().split("").slice(0).sort((a,b)=>a-b).join(""));
     let maxi=Number(s.toString().split("").slice(0).sort((a,b)=>b-a).join(""));
     s=maxi-mini;
     if(s==6174){
        return i+1;
     }
  }
}

/* 05-07-2026: Bucket Fill
Given a 2D grid, a starting position ([row, col]), and a new value, replace the value at the starting position and all connected cells of the same value with the new value.
• Cells are connected if they are adjacent horizontally or vertically (not diagonally).
Return the updated grid. */

const subsets = ([x, ...xs]) =>
x == undefined? [[]] : subsets (xs) .flatMap (ss => [ss, [x, ...ss]]);

function isSubsetConnected(subset) {
  const subsetSet = new Set();
  for (const cell of subset) {
      subsetSet.add(${cell.x},${cell.y});
  }

  const visited = new Set();
  const queue = [];
  const startKey = ${subset[0].x},${subset[0].y};
  queue.push(subset[0]);
  visited.add(startKey);

  const directions = [
   { dx: 0, dy: -1 },
   { dx: 0, dy: 1 },
   { dx: -1, dy: 0 },
   { dx: 1, dy: 0 }
 ];

  while (queue.length > 0) {
    const current = queue.shift();

  for (const { dx, dy } of directions) {
     const nextX = current.x + dx;
     const nextY = current.y + dy;
     const neighborKey = ${nextX},${nextY};

     if (subsetSet.has(neighborKey) && !visited.has(neighborKey)) {
         visited.add(neighborKey);
         queue.push({ x: nextX, y: nextY });
    }
  }
}

   return visited.size === subsetSet.size;
}


function bucketFill(grid, [row, col], newValue) {
  let ch=grid[row][col];
  let hlp=[];
  for(let i=0;i<grid.length;i++){
    for(let j=0;j<grid[0].length;j++){
      if(grid[i][j]==ch){
        hlp.push([i,j]);
       }
     }
   }
  let s=subsets(hlp).filter((item)=>item.length>=2);
  let sets=[];
  for(let i=0;i<s.length;i++){
    sets.push([]);
    for(let j=0;j<s[i].length;j++){
      sets[i].push({x:s[i][j][0],y:s[i][j][1]});
    }
  }
  let m=sets.map((item,index)=>[index,isSubsetConnected(item),item.length]).filter((item)=>item[1]).sort((a,b)=>b[2]-a[2]);
  let ind=m[0][0];
  for(let k=0;k<s[ind].length;k++){
    grid[s[ind][k][0]][s[ind][k][1]]=newValue;
  }
  return grid;
}

/* 06-07-2026: lowercase words
Given a string, return only the words that are entirely lowercase, in their original order and with a space between each word. */

function getLowercaseWords(str) {
  return str.split(" ").filter((item)=>item==item.toLowerCase()).join(" ");
}

/* 07-07-2026: Nearest Multiple
Given two integers, round the first to the nearest multiple of the second. */

function roundToNearestMultiple(num, multiple) {
  let m=Array.from(Array(Math.ceil(num/multiple)+1).keys()).map((item)=>item*multiple).slice(1).filter((item)=>item>=num-multiple).slice(0,2);
  return Math.abs(m[1]-num)>Math.abs(m[0]-num)?m[0]:m[1];
}

/* 08-07-2026: Issue Triage
Given a number of milliseconds since the last post on an issue, and the last message posted on the issue, determine what you should do with the issue according to these rules:
• If the last message is less than 7 days ago, return "leave it"
• If the last message is 7 or more days ago and its content contains "bump" (case-insensitive), return "close it"
• Otherwise, return "bump it" */

function triageIssue(ms, message) {
   let t=ms/1000/3600/24;
   return t<7?"leave it":message.toLowerCase().includes("bump")?"close it":"bump it";
}

/* 09-07-2026: Issue Triage 2
Given an issue title and an array of current labels, return an updated array of labels based on the following rules:
If the issue doesn't have any labels, add:
• "bug"
• and "needs triage" if the title contains "error" or "bug"
• "enhancement" and "discussing" if the title contains "feature" or "add"
Otherwise, if the given labels contain:
• "needs triage" and the title contains "simple" or "easy", remove "needs triage" and add "good first issue"
• "discussing" and the title contains "planned" or "next", remove "discussing" and add "on the roadmap"
• Otherwise, if "needs triage" or "discussing" is present, remove it and add "help wanted"
If the title contains:
• "security", add a "critical" label */

function triageIssue(title, labels) {
  let pre;
  if(labels.length==0){
     pre=title.includes("error")||title.includes("bug")?["bug","needs triage"]:title.includes("feature")||title.includes("add")?["enhancement","discussing"]:[];
  } else {
     pre=labels.includes("needs triage")&&(title.includes("simple")||title.includes("easy"))?labels.map((item)=>item.replace("needs triage","good first issue")):labels.includes("discussing")&&(title.includes("planned")||title.includes("next"))?labels.map((item)=>item.replace("discussing","on the roadmap")):labels.includes("discussing")||labels.includes("needs triage")?
     labels.map((item)=>item.replace("discussing","help wanted").replace("needs triage","help wanted")):labels;
}
  return title.includes("security")?[...pre,"critical"]:pre;
}

/* 10-07-2026: Exact Change
Given an integer amount in cents, return the number of distinct ways to make exact change using pennies (1 cent), nickels (5 cents), dimes (10 cents), and quarters (25 cents). */

function exactChange(amount) {
  let sn=0;
  for(let m=0;m<Math.ceil(amount/25);m++){
   for(let i=0;i<Math.ceil(amount/10);i++){
      for(let j=0;j<Math.ceil(amount/5);j++){
         for(let k=0;k<amount+1;k++){
            if(25*m+10*i+5*j+k==amount ){
              sn+=1;
             }
          }
       }
    }
 }
    return sn;
}

/* 11-07-2026: Five Dice
Given an array of five dice with values 1-6, return the best possible hand.
Here are the hands ranked lowest to highest:

Hand
Description

"no pair"
No pair or better

"pair"
Two dice with the same value

"two pair"
Two different pairs

"three of a kind"
Three dice with the same value

"small straight"
Four consecutive values

"large straight"
Five consecutive values

"full house"
Three of a kind and a pair

"four of a kind"
Four dice with the same value

"five of a kind"
All five dice with the same value



*/

function fiveDice(dice) {
  let obj={};
  let s=Array.from(new Set(dice));
  for(let i=0;i<s.length;i++){
    obj[s[i]]=0;
  }
  for(let i=0;i<5;i++){
    obj[dice[i]]+=1;
  }
  let k=Object.keys(obj);
  let v=Object.values(obj);
  let c=v.sort().map((item)=>item.toString()).join("");
  if(v.includes(5)) return "five of a kind";
  else if(v.includes(4)) return "four of a kind";
  else if(v.includes(3) && v.includes(2)) return "full house";
  else if(v.includes(3) && !v.includes(2)) return "three of a kind";
  else if(c.split("2").length==3) return "two pair";
  else if(c.split("2").length==2 && c.split("1").length==4) return "pair";
  else if((!dice.includes(6)||!dice.includes(1)) && Math.max(...v)==1)
     return "large straight";
  else if(Math.max(...v)==1 && (!dice.includes(5)||!dice.includes(2))) return "small straight";
  else return "no pair";
}

/* 12-07-2026: Horoscope Match
Given two star sign strings, return their compatibility percentage.
The signs are arranged in a wheel of 12 positions in this order: "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces", wrapping back to "Aries" after "Pisces". Find the shortest distance between the two signs and return the compatibility:

Distance
Compatibility

0
"100%"

1
"40%"

2
"80%"

3
"30%"

4
"90%"

5
"20%"

6
"50%"



*/

function horoscopeMatch(sign1, sign2) {
  let signs=["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"];
  let dist=[100,40,80,30,90,20,50];
  let i1=signs.indexOf(sign1);
  let i2=signs.indexOf(sign2);
  let d1=Math.abs(i1-i2);
  let d2=d1>6?12-d1:d1;
  return dist[d2].toString()+"%";
}

/* 13-07-2026: Tally Counter
Given a string of tally marks, return the total count represented.
• Each pipe "|" represents one count.
• Every fifth mark is represented as a forward slash "/", completing a group of five ("||||/").
• Groups are separated by a space. */

function getTallyCount(str) {
  let sp1=str.split("/");
  let sp2=sp1.reverse()[0].split("|");
  return 5*(sp1.length-1)+(sp2.length-1);
}

/* 14-07-2026: Pet Age Calculator
Given a pet type and age in human years, return the equivalent age in pet years using the following conversion table:

Pet
Multiplier

"dog"
7

"cat"
6

"rabbit"
8

"hamster"
30

"guinea pig"
12

"goldfish"
6

"bird"
5



*/

function petYears(pet, age) {
  let pets=["dog","cat","rabbit","hamster","guinea pig","goldfish","bird"];
  let m=[7,6,8,30,12,6,5];
  return m[pets.indexOf(pet)]*age;
}

/* 15-07-2026: Array Chunks
Given an array and a chunk size, return the array split into sub-arrays of that size.
The last chunk may be smaller if the array doesn't divide evenly. */

function chunkArray(arr, size) {
  let t=Math.ceil(arr.length/size);
  let res=[];
  for(let i=0;i<2*t;i=i+size){
     res.push(arr.slice(i,i+size));
   }
  return res.filter((item)=>item.length>0);
}


/* 16-07-2026: Pig Latin Converter
Given a string, convert it to Pig Latin using the following rules:
• If a word begins with a vowel ("a", "e", "i", "o", or "u"), add "way" to the end. For example, "universe" converts to "universeway".
• If a word begins with one or more consonants, move them to the end and add "ay". For example, "hello" converts to "ellohay".
• Preserve the case of the first letter. For example, "Hello" converts to "Ellohay". */

function pigLatin(str) {
  let pre=[];
  let sp=str.split(" ");
  let c=sp.map((item)=>item[0].toUpperCase()==item[0]);
  for(let i=0;i<sp.length;i++){
     for(let j=0;j<sp[i].length;j++){
      if("aeiou".includes(sp[i][j].toLowerCase())){
        if(j==0){pre.push(sp[i]+"way");
        }
      else {
        if(c[i]){pre.push(sp[i][j].toUpperCase()+sp[i].slice(j+1).toLowerCase()+sp[i].slice(0,j).toLowerCase()+"ay");}
        else {
          pre.push(sp[i].slice(j)+sp[i].slice(0,j).toLowerCase()+"ay")
        }
       }
         break;
       }
     }
  }
    return pre.join(" ");
}

/* 17-07-2026: Birthday Countdown
Given today's date and a birthday, return the number of days until the person's next birthday.
• Today's date is given as a string in "YYYY-MM-DD" format, with leading zeros, for example: "2026-07-16".
• The birthday is given as a string in "M/D" format, without leading zeros, for example: "9/7".
• If today is their birthday, return the number of days until their next birthday (not 0).
• Leap years should be accounted for. */

function isLeapYear(year){
  return year%400==0 || year%4==0 && year%100!=0
}

function daysUntilBirthday(today, birthday) {
  let _year=parseInt(today.slice(0,4));
  let nxt=Array.from(Array(9).keys()).map((item)=>item+_year).filter((item)=>isLeapYear(item));
  let m1=parseInt(today.slice(5,7));
  let d1=parseInt(today.slice(8,10));
  let m2=parseInt(birthday.split("/")[0]);
  let d2=parseInt(birthday.split("/")[1]);
  let year;
  if(birthday=="2/29"){
     if(m1<=2){
      year=isLeapYear(_year)?_year:nxt[0];
     } else year=isLeapYear(_year+1)?_year+1:nxt[1];
  } else {
    year=m1<m2||m1==m2&&d1<d2?_year:_year+1;
    }
  let month=m2<10?"0"+m2.toString():m2.toString();
  let day=d2<10?"0"+d2.toString():d2.toString();
  let bd=year.toString()+"-"+month+"-"+day;
  let dt1=+Date.parse(today)/1000;
  let dt2=+Date.parse(bd)/1000;
  let diff=(dt2-dt1)/3600/24;
  return diff;
}

/* 18-07-2026: Dice Odds
Given a number of six-sided dice to roll and a target sum, return the odds of rolling that sum as a string in the format "1 in X".
• The number of dice will be between 1 and 6.
• The target sum is always achievable with the given number of dice.
• Round "X" to the nearest whole number. */

function enh(arr){
  return [[...arr,1],[...arr,2],[...arr,3],[...arr,4],[...arr,5],[...arr,6]];
}

function addDim(arr){
  let res=[];
  for(let i=0;i<arr.length;i++){
    res=[...res,...enh(arr[i])];
  }
  return res;
}

function getOdds(dice, target) {
  let s=[[1],[2],[3],[4],[5],[6]];
  if(dice==1) return "1 in 6";
  let n=dice-1;
  while(n>0){
    s=addDim(s);
    n-=1;
  }
  let m=s.filter((item)=>item.reduce((a,b)=>a+b,0)==target).length;
  let p=Math.pow(6,dice);
  let fr=m/p;
  let res=[];
  let hlp=[];
  for(let i=1;i<Math.min(p+2,7777);i++){
    res.push(i);
    hlp.push(Math.abs(i*fr-1))
    if(i*fr-1==0) break;
  }
  let mini=Math.min(...hlp);
  if(hlp.includes(0))
    return `1 in ${res[res.length-1]}`; 
  else return `1 in ${hlp.indexOf(mini)+1}`
}

/* 19-07-2026: Elevator Stops
Given a number for the current floor of an elevator and an array of requested floors, return an array of the order the elevator should visit them to minimize number of floors traveled.
• If tied, go up first
• Floors with a request must be visited when the elevator first passes them */

function minDist(curr,arr){
  let dist=[];
  let pre=[];
  for(let i=0;i<arr.length;i++){
   dist.push(Math.abs(arr[i]-curr));
  }
  let mini=Math.min(...dist);
  for(let i=0;i<dist.length;i++){
   if(dist[i]==mini) pre.push(arr[i]);
  }
  return pre.sort((a,b)=>a-b)[0];
}

function elevatorStops(currentFloor, stops) {
  let res=[];
  let l=stops.length;
  while(l>0){
   let s=minDist(currentFloor,stops);
   res.push(s);
   let ind = stops.indexOf(s);
   stops.splice(ind, 1);
   currentFloor=s;
   l-=1;
  }
  return res;
}

/* 20-07-2026: Golden Ratio
Given two numbers, determine if their ratio approximates the golden ratio.
• Use a golden ratio of 1.618
• Allow a tolerance of 0.01 */

function isGoldenRatio(a, b) {
  return Math.abs(1.618-Math.max(a,b)/Math.min(a,b))<0.01;
}

/* 21-07-2026: Blender
Given two words, return a new word by combining the first half of the first word with the second half of the second word.
• For odd-length words, the first half is the shorter half.
*/
function blendWords(word1, word2) {
  let p1=word1.slice(0,Math.floor(word1.length/2));
  let p2=word2.slice(Math.floor(word2.length/2),word2.length);
  return p1+p2;
}


/* 22-07-2026: Piggy Bank
Given an object representing a piggy bank, return the total value as a string formatted as "$D.CC".
The object may contain any of the following:

Coin
Value

pennies
$0.01

nickels
$0.05

dimes
$0.10

quarters
$0.25

*/

function piggyBank(coins) {
  let c=["pennies","nickels","dimes","quarters"];
  let v=[0.01,0.05,0.1,0.25];
  let k=Object.keys(coins);
  if(k.length==0) return "$0.00";
  let m=k.map((item)=>coins[item]*v[c.indexOf(item)]).reduce((a,b)=>a+b,0);
  return "$"+m.toFixed(2);
}

/* 23-07-2026: Game Theory
Given two equal length strings representing two players' strategies for a game, return the scores as an array [player1, player2].
• The given strings will only contain one of two letters: "C" (cooperate) or "D" (defect).
• Each character represents one round, scored as follows:
◦ If both players cooperate, each scores 3.
◦ If both players defect, each scores 1.
◦ If one player defects and the other cooperates, the defector scores 5 and the cooperator scores 0. */


function playGame(p1, p2) {
  let s1=0;
  let s2=0;
  for(let i=0;i<p1.length;i++){
    if(p1[i]=="C" && p2[i]=="C"){
       s1+=3;s2+=3;
   } else if(p1[i]=="C" && p2[i]=="D"){
       s2+=5;
   } else if (p1[i]=="D" && p2[i]=="C"){
       s1+=5;
   } else { s1+=1;s2+=1;}
  }
  return [s1,s2];
}

/* 24-07-2026: Loan Calculator
Given a loan amount, annual interest rate percentage, and fixed monthly payment, return an array of remaining balances after each monthly payment until the loan is paid off.
• Each month, interest is calculated on the remaining balance using the monthly interest rate: (annual rate / 100) / 12, then the monthly payment is subtracted.
• Return each remaining balance rounded to the nearest dollar.
• Include the loan amount in the returned array. The first element in the array will always be the loan amount, and the last element of the array will always be 0. */

function myRound(amount){
  if(!amount.toString().includes(".")) return amount;
  let sp=amount.toString().split(".");
  let s=parseInt(sp[1][0]);
  return s>=5?parseInt(sp[0])+1:parseInt(sp[0]);
}

function getLoanSchedule(loanAmount, annualRate, monthlyPayment) {
  let ir=loanAmount*(annualRate / 100) / 12;
  let res=[loanAmount];
  let pre=[];
  let s=loanAmount;
  while(s>0){
     s=Math.round(100*(s-monthlyPayment+ir))/100;
     ir=s*(annualRate/100)/12;
     pre.push(s<0?0:s);
  }
  for(let i=0;i<pre.length-1;i++){
     res.push(myRound(pre[i]));
  }
  res.push(0);
  return res;
}

/* 25-07-2026: Cell Signal
Given a grid containing three cell tower readings, determine the location of the phone.
• Each cell in the grid is either 0 (no tower) or a positive integer representing the number of cells to the phone, measured in a straight line: horizontal, vertical, or diagonal.
• Return the [row, col] of the cell that is the correct number of cells from all three towers.
• There is always exactly one solution. */

function getDist(cell,arr){
  let signs=arr.map((item)=>item.split("").map((item)=>Math.max(parseInt(item),0))).map((item)=>[item[0]-cell[0],item[1]-cell[1]]).map((item)=>Math.max(Math.abs(item[0]),Math.abs(item[1])));
  return signs;
}

function findSignal(grid) {
  let rows=grid.length;
  let cols=grid[0].length;
  let sigs={};
  for(let i=0;i<rows;i++){
    for(let j=0;j<cols;j++){
      if(grid[i][j]!=0){
      sigs[i.toString()+j.toString()]=grid[i][j];
      }
    }
   }
  for(let m=0;m<rows;m++){
    for(let n=0;n<cols;n++){
     let ch=[];
     let k=Object.keys(sigs);
     let t=getDist([m,n],k);
    for(let i=0;i<k.length;i++){
     let s=t[i]==sigs[k[i]];
     if(s) ch.push(s);
    }
    if(ch.length==k.length) return [m,n];
    }
   }
   return grid;
}

/* 26-07-2026: Letter Distance
Given two strings of equal length, return the sum of the shortest distances between each pair of characters.
• The input will only contain lowercase letters
• The alphabet is treated as a circle, so the distance between a and z is 1. */

function letterDistance(str1, str2) {
  let arr1=str1.split("").map((item)=>item.charCodeAt(item));
  let arr2=str2.split("").map((item)=>item.charCodeAt(item));
  let m=[];
  for(let i=0;i<arr1.length;i++){
   m.push(Math.min(Math.abs(arr1[i]-arr2[i]),26-Math.abs(arr1[i]-arr2[i])));
  }
   return m.reduce((a,b)=>a+b,0);
}


/* 27-07-2026: Pronic Number
Given a number, determine whether it is a pronic number.
A pronic number is the product of two consecutive integers. For example, 6 is pronic because 2 * 3 = 6. */

function isPronic(n) {
  if(n==0) return true;
  let arr=Array.from(Array(n).keys()).map((item)=>item+1).slice(1).filter((item)=>n%item==0&&item!=n);
  for(let i=1;i<arr.length;i++){
    if(arr[i]==arr[i-1]+1 && arr[i-1]*arr[i]==n) return true;
  }
  return false;
}

/* 28-07-2026: Contrast Rating 1
Given a contrast ratio and a boolean indicating whether the text is large, return the WCAG rating using the following table:

Rating
Normal Text
Large Text

"AAA"
7.0+
4.5+

"AA"
4.5+
3.0+

"Fail"
below 4.5
below 3.0



*/

function getContrastRating(ratio, isLargeText) {
  return ratio>=7.5 && !isLargeText || ratio>=4.5 && isLargeText?"AAA":ratio>=4.5 && !isLargeText || ratio>=3 && isLargeText?"AA":"Fail";
}

/* 29-07-2026: Contrast Rating 2
Given two relative luminance values and a boolean indicating whether the text is large, return the WCAG contrast rating using the following method:
Calculate the contrast ratio by adding 0.05 to each luminance value, then dividing the lighter one by the darker one. The lighter one will always be the first argument.
Return the rating based on the contrast ratio using the following table:

Rating
Normal Text
Large Text

"AAA"
7.0+
4.5+

"AA"
4.5+
3.0+

"Fail"
below 4.5
below 3.0



*/

function getContrastRating(l1, l2, isLargeText) {
  let ratio=(l1+0.05)/(l2+0.05);
  return ratio>=7.5 && !isLargeText || ratio>=4.5 && isLargeText?"AAA":ratio>=4.5 && !isLargeText || ratio>=3 && isLargeText?"AA":"Fail";
}

/* 30-07-2026: Contrast Rating 3
Given two arrays representing RGB values and a boolean indicating whether the text is large, return the WCAG contrast rating using the following method:
First, convert each RGB value to relative luminance:
• Divide each channel [R, G, B] by 255 to get a value between 0 and 1
• Apply the gamma correction formula to each channel:
◦ If the channel value is less than or equal to 0.04045: channel / 12.92
◦ Otherwise: ((channel + 0.055) / 1.055) ^ 2.4
• Calculate luminance: 0.2126 * R + 0.7152 * G + 0.0722 * B
Then, calculate the contrast ratio by adding 0.05 to each luminance value, then dividing the lighter one by the darker one. The lighter one will always be the first argument.
Return the rating based on the contrast ratio using the following table:

Rating
Normal Text
Large Text

"AAA"
7.0+
4.5+

"AA"
4.5+
3.0+

"Fail"
below 4.5
below 3.0


*/

function getContrastRating(rgb1, rgb2, isLargeText) {
  let m1=rgb1.map((item)=>item/255).map((item)=>item<=0.04045?item / 12.92:Math.pow((item + 0.055) / 1.055,2.4));
  let l1=0.2126 * m1[0] + 0.7152 * m1[1] + 0.0722 * m1[2];
  let m2=rgb2.map((item)=>item/255).map((item)=>item<=0.04045?item/12.92:Math.pow((item+0.055)/1.055,2.4));
  let l2=0.2126*m2[0]+0.7151*m2[1]+0.0722*m2[2];
  let ratio=(l1+0.05)/(l2+0.05);
  return isLargeText==false && ratio>=7.0?"AAA":isLargeText==false && ratio>=4.5?"AA":isLargeText==false && ratio<4.5?"Fail":isLargeText==true && ratio>=4.5?"AAA":isLargeText==true && ratio>=3.0?"AA":"Fail";
}

/* 31-07-2026: Morse Code
Given a Morse code string, return the decoded message using the following table:

Code
Letter
Code
Letter

.-
A
-.
N

-...
B
---
O

-.-.
C
.--.
P

-..
D
--.-
Q

.
E
.-.
R

..-.
F
...
S

--.
G
-
T

....
H
..-
U

..
I
...-
V

.---
J
.--
W

-.-
K
-..-
X

.-..
L
-.--
Y

--
M
--..
Z


• Letters are separated by a single space
• Words are separated by three spaces */

function decodeMorse(code) {
  let morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
  let alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
  return code.split(" ").map((item)=>item.split(" ").map((sub)=>morse.indexOf(sub)).filter((sub)=>sub>=0)).map((item)=>item.map((sub)=>alph[sub])).map((item)=>item.join("")).join(" ");
}
