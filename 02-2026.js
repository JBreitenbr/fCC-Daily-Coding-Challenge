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


