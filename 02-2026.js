/* 01-02-2026: Digital Detox

Given an array of your login logs, determine whether you have met your digital detox goal.
Each log is a string in the format "YYYY-MM-DD HH:mm:ss".
You have met your digital detox goal if both of the following statements are true:
• You logged in no more than once within any four-hour period.
• You logged in no more than 2 times on any single day.
*/

function digitalDetox(logs) {
  let days=logs.map((item)=>item.slice(0,10)).sort();
  for(let i=0;i<days.length;i++){
    let sp=days.filter(x => x === days[i]).length;
    if(sp>2){
      return false;
    }
  }
  let ts=[];
  let s=logs.sort();
  for(let i=0;i<s.length;i++){
    ts.push(Date.parse(s[i]));
  }
  for(let i=1;i<ts.length;i++){   
    if(ts[i]/1000/3600-ts[i-1]/1000/3600<4) return false;
  }  
  return true;
}

/* 02-02-2026: Groundhog Day

Today is Groundhog Day, in which a groundhog predicts the weather based on whether or not it sees its shadow.
Given a value representing the groundhog's appearance, return the correct prediction:
• If the given value is the boolean true (the groundhog saw its shadow), return "Looks like we'll have six more weeks of winter.".
• If the value is the boolean false (the groundhog did not see its shadow), return "It's going to be an early spring.".
• If the value is anything else (the groundhog did not show up), return "No prediction this year.". */

function groundhogDayPrediction(app) {
  if(app===true)
   {return "Looks like we'll have six more weeks of winter.";}
  else if(app===false){
    return "It's going to be an early spring.";
  } else return "No prediction this year.";
}

/* 03-02-2026: String Mirror

Given a string, return a new string that consists of the given string with a reversed copy of itself appended to the end of it. */


function mirror(str) {
  let m=str.split("").reverse().join("");
  return str+m;
}

/* 04-02-2026: Truncate the Text

Given a string, return it as-is if it's 20 characters or shorter. If it's longer than 20 characters, truncate it to the first 17 characters and append "..." to the end of it (so it's 20 characters total) and return the result. */

function truncateText(text) {
  if(text.length>20){
    return text.slice(0,17)+"...";
  }
  return text;
}

/* 05-02-2026: Pocket Change

Given an array of integers representing the coins in your pocket, with each integer being the value of a coin in cents, return the total amount in the format "$D.CC".
• 100 cents equals 1 dollar.
• In the return value, include a leading zero for amounts less than one dollar and always exactly two digits for the cents. */

function countChange(change) {
  let sn=(change.reduce((a,b)=>a+b,0)/100).toString();
  let sp=sn.split(".");
  if(sp.length==1){
    sn=sn+".00";
  } else if(sp[1].length==1){
    sn=sn+"0";
  }
  return "$"+sn;
}

/* 06-02-2026:2026 Winter Games Day 1: Opening Day

Today marks the start of the 2026 Winter Games. The next 17 days will bring you coding challenges inspired by them.
For the first one, you are given a two-letter country code and need to return the flag emoji for that country. */

function getFlag(code) {
let cDict={
"AL":"🇦🇱","AD":"🇦🇩","AR":"🇦🇷","AM":"🇦🇲",
"AU":"🇦🇺","AT":"🇦🇹","AZ":"🇦🇿","BE":"🇧🇪",
"BJ":"🇧🇯","BO":"🇧🇴","BA":"🇧🇦","BR":"🇧🇷",
"BG":"🇧🇬","CA":"🇨🇦","CL":"🇨🇱","CN":"🇨🇳",
"CO":"🇨🇴","HR":"🇭🇷","CY":"🇨🇾","CZ":"🇨🇿",
"DK":"🇩🇰","EC":"🇪🇨","ER":"🇪🇷","EE":"🇪🇪",
"FI":"🇫🇮","FR":"🇫🇷","GE":"🇬🇪","DE":"🇩🇪",
"GB":"🇬🇧","GR":"🇬🇷","GW":"🇬🇼","HT":"🇭🇹",
"HK":"🇭🇰","HU":"🇭🇺","IS":"🇮🇸","IN":"🇮🇳",
"IR":"🇮🇷","IE":"🇮🇪","IL":"🇮🇱","IT":"🇮🇹",
"JM":"🇯🇲","JP":"🇯🇵","KZ":"🇰🇿","KE":"🇰🇪",
"XK":"🇽🇰","KG":"🇰🇬","LV":"🇱🇻","LB":"🇱🇧",
"LI":"🇱🇮","LT":"🇱🇹","LU":"🇱🇺","MG":"🇲🇬",
"MY":"🇲🇾","MT":"🇲🇹","MX":"🇲🇽","MD":"🇲🇩",
"MC":"🇲🇨","MN":"🇲🇳","ME":"🇲🇪","MA":"🇲🇦",
"NL":"🇳🇱","NZ":"🇳🇿","NG":"🇳🇬","MK":"🇲🇰",
"NO":"🇳🇴","PK":"🇵🇰","PH":"🇵🇭","PL":"🇵🇱",
"PT":"🇵🇹","PR":"🇵🇷","RO":"🇷🇴","SM":"🇸🇲",
"SA":"🇸🇦","RS":"🇷🇸","SG":"🇸🇬","SK":"🇸🇰",
"SI":"🇸🇮","ZA":"🇿🇦","KR":"🇰🇷","ES":"🇪🇸",
"SE":"🇸🇪","CH":"🇨🇭","TH":"🇹🇭","TT":"🇹🇹",
"TR":"🇹🇷","UA":"🇺🇦","AE":"🇦🇪","US":"🇺🇸",
"UY":"🇺🇾","UZ":"🇺🇿","VE":"🇻🇪"};
return cDict[code];
}

/* 07-02-2026: 2026 Winter Games Day 2: Snowboarding

Given a snowboarder's starting stance and a rotation in degrees, determine their landing stance.
• A snowboarder's stance is either "Regular" or "Goofy".
• Trick rotations are multiples of 90 degrees. Positive indicates clockwise rotation, and negative indicate counter-clockwise rotation.
• The landing stance flips every 180 degrees of rotation.
For example, given "Regular" and 90, return "Regular". Given "Regular" and 180 degrees, return "Goofy". */

function getLandingStance(startStance, rotation) {
  let t=rotation>0?Math.floor(rotation/180):Math.ceil(rotation/180);
  let opp={"Goofy":"Regular","Regular":"Goofy"};
  return t%2==0?startStance:opp[startStance];
}

/* 08-02-2026: 2026 Winter Games Day 3: Biathlon

Given an array of integers, where each value represents the number of targets hit in a single round of a biathlon, return the total penalty distance the athlete must ski.
• Each round consists of 5 targets.
• Each missed target results in a 150 meter penalty loop. */

function calculatePenaltyDistance(rounds) {
  return rounds.map((item)=>(5-item)*150).reduce((a,b)=>a+b,0);
}

/* 09-02-2026: 2026 Winter Games Day 4: Ski Jumping

Given distance points, style points, a wind compensation value, and K-point bonus value, calculate your score for the ski jump and determine if you won a medal or not.
• Your score is calculated by summing the above four values.
The current total scores of the other jumpers are:
165.5 172.0 158.0 180.0 169.5 175.0 162.0 170.0 
• If your score is the best, return "Gold"
• If it's second best, return "Silver"
• If it's third best, return "Bronze"
• Otherwise, return "No Medal" */

function skiJumpMedal(distancePoints, stylePoints, windComp, kPointBonus) {
  let arr=[165.5,172.0,158.0,180.0,169.5,175.0,162.0,170.0];
  let sn=distancePoints+stylePoints+windComp+kPointBonus;
  arr.push(sn);
  arr.sort((a,b)=>b-a);
  return arr[2]==sn?"Bronze":arr[1]==sn?"Silver":arr[0]==sn?"Gold":"No Medal";
}

/* 10-02-2026: 2026 Winter Games Day 5: Cross-Country Skiing

Given an array of finish times for a cross-country ski race, convert them into times behind the winner.
• Given times are strings in "H:MM:SS" format.
• Given times will be in order from fastest to slowest.
• The winners time (fastest time) should correspond to "0".
• Each other time should show the time behind the winner, in the format "+M:SS".
For example, given ["1:25:32", "1:26:10", "1:27:05"], return ["0", "+0:38", "+1:33"]. */

const secondsToHms = (seconds) => {
    const SECONDS_PER_DAY=86400;
    const HOURS_PER_DAY=24;
    const days = Math.floor(seconds / SECONDS_PER_DAY);
    const remainderSeconds = seconds % SECONDS_PER_DAY;
    const hms = new Date(remainderSeconds * 1000).toISOString().substring(11, 19);
  let res= hms.replace(/^(\d+)/, h => `${Number(h) + days * HOURS_PER_DAY}`.padStart(2, '0'));
  let sp=res.split(":").slice(1).join(":");
  let erg=sp[0]=="0"?sp.slice(1):sp;
  return "+"+erg;
};

function getRelativeResults(results) {
  let m=results.map((item)=>item.split(":")).map((item)=>Number(item[0]*3600)+Number(item[1])*60+Number(item[2]));
  let d=["0"];
  for(let i=1;i<m.length;i++){
    d.push(secondsToHms(m[i]-m[0]));
  }
  return d;
}

/* 11-02-2026: 2026 Winter Games Day 6: Figure Skating

Given an array of judge scores and optional penalties, calculate the final score for a figure skating routine.
The first argument is an array of 10 judge scores, each a number from 0 to 10. Remove the highest and lowest judge scores and sum the remaining 8 scores to get the base score.
Any additional arguments passed to the function are penalties. Subtract all penalties from the base score to get the final score. */

function computeScore(judgeScores, ...penalties) {
  let p=penalties;
  let sn=judgeScores.sort((a,b)=>a-b).slice(1,judgeScores.length-1).reduce((a,b)=>a+b,0);
  if(p.length>0){
    for(let i=0;i<p.length;i++){
      sn-=p[i];
    }
  }
  return sn;
}

/* 12-02-2026: 2026 Winter Games Day 7: Speed Skating

Given two arrays representing the lap times (in seconds) for two speed skaters, return the lap number where the difference in lap times is the largest.
The first element of each array corresponds to lap 1, the second to lap 2, and so on. */

function largestDifference(skater1, skater2) {
  let arr=[];
  for(let i=0;i<skater1.length;i++){
    arr.push(Math.abs(skater2[i]-skater1[i]));
  }
  let s=[...arr];
  let maxi=arr.sort((a,b)=>b-a)[0];
  for(let i=0;i<arr.length;i++){
    if(Math.abs(s[i]-maxi)==0){
      return i+1;
    }
  }
}

/* 13-02-2026:  2026 Winter Games Day 8: Luge

Given an array of five numbers, each representing the time (in seconds) it took a luger to complete a segment of a track, determine which segment had the fastest speed and what that speed was.
The track is divided into the following segments:
• Segment 1: 320 meters
• Segment 2: 280 meters
• Segment 3: 350 meters
• Segment 4: 300 meters
• Segment 5: 250 meters
The first value in the given array corresponds to the time for segment 1, the second value to segment 2, and so on.
To calculate the speed (in meters per second) for a segment, divide the distance by the time.
Return "The luger's fastest speed was X m/s on segment Y.". Where X is the fastest speed, rounded to two decimal places, and Y is the segment number where the fastest speed occurred. */

function getFastestSpeed(times) {
  let l=[320,280,350,300,250];
  let maxi=Math.round(100*l[0]/times[0])/100;
  let ind=1;
  for(let i=0;i<l.length;i++){
    let v=Math.round(100*l[i]/times[i])/100;
    if(v>maxi){
      maxi=v;
      ind=i+1;
    }
  }
  return `The luger's fastest speed was ${maxi} m/s on segment ${ind}.`;
}

/* 14-02-2026: 2026 Winter Games Day 9: Skeleton

Given a string representing the curves on a skeleton track, determine the difficulty of the track.
• The given string will only consist of the letters:
• "L" for a left turn
• "R" for a right turn
• "S" for a straight segment
• Each direction change adds 15 points (an "L" followed by an "R" or vice versa).
• All other curves add 5 points each (all other "L" or "R" characters).
• Straight segments add 0 points.
The difficulty of the track is based on the total score. Return:
• "Easy" if the total is 0 - 100
• "Medium" if the total is 101-200
• "Hard" if the total is over 200
*/

function getDifficulty(track) {
  let sn=track[0]=="S"?0:5;
  for(let i=1;i<track.length;i++){
    if(track[i-1]=="L" && track[i]=="R" || track[i-1]=="R" && track[i]=="L"){
      sn+=15;
    }
    else if(track[i]!="S"){
      sn+=5;
    }
  }
  return sn<=100?"Easy":sn<=200?"Medium":"Hard";
}

/* 15-02-2026: 2026 Winter Games Day 10: Alpine Skiing

Given a ski hill's vertical drop, horizontal distance, and type, determine the difficulty rating of the hill.
To determine the rating:
• Calculate the steepness of the hill by taking the drop divided by the distance.
• Then, calculate the adjusted steepness based on the hill type:
• "Downhill" multiply steepness by 1.2
• "Slalom": multiply steepness by 0.9
• "Giant Slalom": multiply steepness by 1.0
Return:
• "Green" if the adjusted steepness is less than or equal to 0.1
• "Blue" if the adjusted steepness is greater than 0.1 and less than or equal to 0.25
• "Black" if the adjusted steepness is greater than 0.25 */

function getHillRating(drop, distance, type) {
  let st=drop/distance;
  st=type=="Downhill"?st*1.2:type=="Slalom"?st*0.9:st;
  return st<=0.1?"Green":st<=0.25?"Blue":"Black";
}

/* 16-02-2026: 2026 Winter Games Day 11: Ice Hockey

Given an array of 6 ice hockey teams and their records after the round robin games, determine the match-ups for the semi-final round.
• Each array item will have a team and their record in the format "TEAM: W-OTW-OTL-L". Where:
• "W" is the number of wins in regulation, worth 3 points each
• "OTW" is the number of overtime wins, worth 2 points each
• "OTL" is the number of overtime losses, worth 1 point each
• "L" is the number of losses, worth 0 points each
For example, "FIN: 2-2-1-0" would have 11 points after adding up their record.
Find the total number of points for each team and return "The semi-final games will be (1st) vs (4th) and (2nd) vs (3rd).". For example, "The semi-final games will be FIN vs SWE and CAN vs USA." */

function getSemifinalMatchups(teams) {
  let m=teams.map((item)=>item.split(": ")[1]).map((item)=>3*Number(item.split("-")[0])+2*Number(item.split("-")[1])+Number(item.split("-")[2]));
  let s=[...m].sort((a,b)=>b-a);
  let r=[m.indexOf(s[0]),m.indexOf(s[3]),m.indexOf(s[1]),m.indexOf(s[2])];
  let c=[];
  for(let i=0;i<4;i++){
    c.push(teams[r[i]].split(":")[0]);
  }
  return `The semi-final games will be ${c[0]} vs ${c[1]} and ${c[2]} vs ${c[3]}.`;
}

/* 17-02-2026: 2026 Winter Games Day 12: Bobsled

Given an array representing the weights of the athletes on a bobsled team and a number representing the weight of the bobsled, determine whether the team is eligible to race.
• The length of the array determines the team size: 1, 2 or 4 person teams.
• All given weight values are in kilograms (kg).
The bobsled (sled by iteself) must have a minimum weight of:
• 162 kg for a 1-person team
• 170 kg for a 2-person team
• 210 kg for a 4-person team
The total weight of the bobsled (athletes plus sled) must not exceed:
• 247 kg for a 1-person team
• 390 kg for a 2-person team
• 630 kg for a 4-person team
Return "Eligible" if the team meets all the requirements, or "Not Eligible" if the team fails to meet one or more of the requirements. */

function checkEligibility(athleteWeights, sledWeight) {
  let l=athleteWeights.length;
  let c1=l==1?sledWeight>=162:l==2?sledWeight>=170:sledWeight>=210;
  let sn=athleteWeights.reduce((a,b)=>a+b,0)+sledWeight;
  let c2=l==1?sn<=247:l==2?sn<=390:sn<=630;
  if(!c1||!c2) { return "Not Eligible";}
  return "Eligible";
}

/* 18-02-2026: 2026 Winter Games Day 13: Nordic Combined

Given an array of jump scores for athletes, calculate their start delay times for the cross-country portion of the Nordic Combined.
The athlete with the highest jump score starts first (0 second delay). All other athletes start later based on how far behind their jump score is compared to the best jump.
To calculate the delay for each athlete, subtract the athlete's jump score from the best overall jump score and multiply the result by 1.5. Round the delay up to the nearest integer. */

function calculateStartDelays(jumpScores) {
  let maxi=[...jumpScores].sort((a,b)=>b-a)[0];
  return
jumpScores.map((item)=>Math.ceil((maxi-item)*1.5));
}

/* 19-02-2026: 2026 Winter Games Day 14: Ski Mountaineering

Given the snow depth and slope of a mountain, determine if there's an avalanche risk.
• The snow depth values are "Shallow", "Moderate", or "Deep".
• Slope values are "Gentle", "Steep", or "Very Steep".
Return "Safe" or "Risky" based on this table:
                  "Shallow"  "Moderate"  "Deep"
"Gentle"        "Safe"        "Safe"       "Safe"
"Steep"          "Safe"       "Risky"     "Risky"
"Very Steep" "Safe"       "Risky"     "Risky"
*/

function avalancheRisk(snowDepth, slope) {
  if(slope=="Gentle" ||snowDepth=="Shallow"){
    return "Safe";
  }
  else return "Risky";
}

/* 20-02-2026: 2026 Winter Games Day 15: Freestyle Skiing

Given a trick name consisting of two words, determine if it is a valid freestyle skiing trick name.
A trick is valid if the first word is in the list of valid first words, and the second word is in the list of valid second words.
• The two words will be separated by a single space.
Valid first words:
"Misty","Ghost","Thunder","Solar","Sky","Phantom","Frozen","Polar"
Valid second words:
"Twister","Icequake","Avalanche","Vortex","Snowstorm","Frostbite","Blizzard","Shadow" */

function isValidTrick(trickName) {
  let arr1=["Misty","Ghost","Thunder","Solar","Sky","Phantom","Frozen","Polar"];
  let arr2=["Twister","Icequake","Avalanche","Vortex","Snowstorm","Frostbite","Blizzard","Shadow"]
  let sp=trickName.split(" ");
  if(arr1.includes(sp[0]) && arr2.includes(sp[1])) return true;
  return false;
}

/* 21-02-2026: 2026 Winter Games Day 16: Curling

Given a 5x5 matrix representing the "house" at the end of a curling round, determine which team scores and how many points they score.
The layout:
• The center cell (index [2, 2]) is the "button".
• The 8 cells directly surrounding the button represent ring 1.
• And the 16 cells on the outer edge of the house represent ring 2.
In the given matrix:
• "." represents an empty space.
• "R" represents a space with a red stone.
• "Y" represents a space with a yellow stone.
Scoring rules:
• Only one team can score per round.
• The team with the stone closest to the button scores.
• The scoring team earns 1 point for each of their stones that is closer to the button than the opponent's closest stone.
• The lower the ring number, the closer to the center the stone is.
• If both teams' closest stone is the same distance from the center, no team scores.
Return:
• A string in the format "team: number_of_points". e.g: "R: 2".
• or "No points awarded" if neither team scored any points.
For example, given:
[ [".", ".", "R", ".", "."],
  [".", "R", ".", ".", "."], 
  ["Y", ".", ".", ".", "."], 
  [".", "R", ".", ".", "."], 
  [".", ".", ".", ".", "."] ] 
Return "R: 2". The two red stones in ring 1 are tied for the closest and are the only two stones closer than yellows closest. */

function scoreCurling(house){
  let r0=[];
  let y0=[];
  for(let i=0;i<5;i++){
    for(let j=0;j<5;j++){
      if(house[i][j]=="R"){
        r0.push([i-2,j-2]);
      }
      if(house[i][j]=="Y"){
        y0.push([i-2,j-2]);
      }
    }
  }
  let r=r0.map((item)=>[Math.abs(item[0]),Math.abs(item[1])]).map((item)=>Math.max(...item));
  let y=y0.map((item)=>[Math.abs(item[0]),Math.abs(item[1])]).map((item)=>Math.max(...item));
  let m_r=Math.min(...r);
  let m_y=Math.min(...y);
  return m_r<m_y?`R: ${r.filter((item)=>item<m_y).length}`:m_r>m_y?`Y: ${y.filter((item)=>item<m_r).length}`:"No points awarded";
}
