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
            if(25m+10i+5*j+k==amount ){
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

