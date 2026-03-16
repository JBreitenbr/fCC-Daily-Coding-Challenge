/* 01-03-2026: Flattened 

Given an array, determine if it is flat.
• An array is flat if none of its elements are arrays. */

function isFlat(arr) {
  for(let i=0;i<arr.length;i++){
    if(Array.isArray(arr[i])){
      return false;
    }
  }
  return true;
}

/* 02-03-2026: Sum the Letters

Given a string, return the sum of its letters.
• Letters are A-Z in uppercase or lowercase
• Letter values are: "A" = 1, "B" = 2, ..., "Z" = 26
• Uppercase and lowercase letters have the same value.
• Ignore all non-letter characters. */

function sumLetters(str) {
  let reg=/[A-Za-z]/gi;
  let m=str.match(reg);
  let a1="abcdefghijklmnopqrstuvwxyz";
  let a2=a1.toUpperCase();
  let sn=0;
  for(let i=0;i<str.length;i++){
    if(a1.includes(str[i])){
      sn+=a1.indexOf(str[i])+1;
    } 
    if(a2.includes(str[i])){
      sn+=a2.indexOf(str[i])+1;
    }
  }
  return sn;
}
/* 03-03-2027: Perfect Cube Count

Given two integers, determine how many perfect cubes exist in the range between and including the two numbers.
• The lower number is not garanteed to be the first argument.
• A number is a perfect cube if there exists an integer (n) where n * n * n = number. For example, 27 is a perfect cube because 3 * 3 * 3 = 27. */

function countPerfectCubes(a, b) {
  let c=[0];
  let s1=b>a?a:b;
  let s2=a>b?a:b;
  for(let i=1;i<22;i++){
    c.push(-i*i*i);
    c.push(i*i*i);
  }
  let arr=Array.from(Array(s2-s1+1).keys()).map((item)=>item+s1);
  let sn=0;
  for(let i=0;i<arr.length;i++){
    if(c.includes(arr[i])){
      sn+=1;
    }
  }
  return sn;
}

/* 04-03-2026: Playing Card Values

Given an array of playing cards, return a new array with the numeric value of each card.
Card Values:
• An Ace ("A") has a value of 1.
• Numbered cards ("2" - "10") have their face value: 2 - 10, respectively.
• Face cards: Jack ("J"), Queen ("Q"), and King ("K") are each worth 10.
Suits:
• Each card has a suit: Spades ("S"), Clubs ("C"), Diamonds ("D"), or Hearts ("H").
Card Format:
• Each card is represented as a string: "valueSuit". For Example: "AS" is the Ace of Spades, "10H" is the Ten of Hearts, and "QC" is the Queen of Clubs. */

function cardValues(cards) {
  let d="0123456789".split("");
  d.push("10");
  let p={"A":1,"K":10,"Q":10,"J":10};
  let res=[];
  for(let i=0;i<cards.length;i++){
    if(d.includes(cards[i].slice(0,cards[i].length-1))){
      res.push(Number(cards[i].slice(0,cards[i].length-1)));
    }
    else res.push(p[cards[i][0]]);
  }
  return res;
}

/* 05-03-2026: Smallest Gap

Given a string, return the substring between the two identical characters that have the smallest number of characters between them (smallest gap).
• There will always be at least one pair of matching characters.
• The returned substring should exclude the matching characters.
• If two or more gaps are the same length, return the characters from the first one.
For example, given "ABCDAC", return "DA".
• Only "A" and "C" repeat in the string.
• The number of characters between the two "A" characters is 3, and between the "C" characters is 2.
• So return the string between the two "C" characters. */

function gaps(arr,stri){
  let res=[];
  for(let i=1;i<arr.length;i++){
    res.push(stri.slice(arr[i-1]+1,arr[i]));
  }
  return res;
}

function smallestGap(str) {
  let s=Array.from(new Set(str));
  let l=[];
  for(let i=0;i<s.length;i++){
    if(str.split(s[i]).length>2){
      l.push(s[i]);
    }
  }
  let pre=[];
  for(let j=0;j<l.length;j++){
  let ind = [],
      i = -1;
      while ((i = str.indexOf(l[j], i + 1)) !== -1) {
          ind.push(i);
          }
    pre.push(gaps(ind,str));
  }
  let w=pre.flat();
  let mini=Math.min(...w.map((item)=>item.length));
  let ms=w.filter((item)=>item.length==mini).map((item)=>str.indexOf(item)).sort()[0];
  return str.slice(ms,ms+mini);
}
/* 06-03-2026: Trail Traversal

Given an array of strings representing your trail map, return a string of the moves needed to get to your goal.
The given strings will contain the values:
• "C": Your current location
• "G": Your goal
• "T": Traversable parts of the trail
• "-": Untraversable parts of the map
Return a string with the moves needed to follow the trail from your location to your goal where:
• "R" is a move right
• "D" is a move down
• "L" is a move left
• "U" is a move up
• There will always be a single continuous trail, without any branching, from your current location to your goal.
• Each trail location will have a maximum of two traversable locations touching it.
For example, given:
[ "-CT--", "--T--", "--TT-", "---T-", "---G-" ] 
Return "RDDRDD". */

function findWay(matrix,position, end) {
  let queue = [];
  matrix[position[0]][position[1]] = 1;
  queue.push([position]); 
  while (queue.length > 0) {
  let path = queue.shift(); 
  let pos = path[path.length-1]; 
  let dir = [[pos[0]+ 1,pos[1]],[pos[0],pos[1]+1],
[pos[0]-1,pos[1]],[pos[0], pos[1]-1]];
  for (let i = 0; i < dir.length; i++) {
if(dir[i][0] == end[0] && dir[i][1] == end[1]) {
return path.concat([end]); 
}
if(dir[i][0] < 0 || dir[i][0] >= matrix.length || dir[i][1] < 0 || dir[i][1] >= matrix[0].length || matrix[dir[i][0]][dir[i][1]] != 0) { 
    continue;
}
matrix[dir[i][0]][dir[i][1]] = 1;
queue.push(path.concat([dir[i]])); 
  }
   }
   return queue;
    }

function findDir(arr){
  let res=""; 
  for(let i=1;i<arr.length;i++){
    if(arr[i][0]==arr[i-1][0] && arr[i][1]-arr[i-1][1]==1)
    res+="R";
    if(arr[i][0]==arr[i-1][0] && arr[i][1]-arr[i-1][1]==-1)
    res+="L";
    if(arr[i][0]-arr[i-1][0]==1 && arr[i][1]==arr[i-1][1])
    res+="D";
    if(arr[i][0]-arr[i-1][0]==-1 && arr[i][1]==arr[i-1][1])   res+="U";
}
return res;
}

function navigateTrail(m) {
  let c;
  let g;
  let start;
  let end;
  for(let i=0;i<m.length;i++){
    c=m[i].indexOf("C");
    if(c>-1){
      start=[i,c];
    }
    g=m[i].indexOf("G");
    if(g>-1){
      end=[i,g];
    }
  }
  let hlp=[];
  for(let i=0;i<m.length;i++){
    hlp.push(m[i].split(""));
  }
  let mat=Array(m.length).fill(1).map(_ => Array(m[0].length).fill(1));
  for(let i=0;i<m.length;i++){
    for(let j=0;j<m[0].length;j++){
      if(m[i][j]!="-"){
        mat[i][j]=0;
      }
    }
  }
  let s=findWay(mat,start,end);
  return findDir(s);
}

/* 07-03-2026: Element Size

Given a window size, the width of an element in viewport width "vw" units, and the height of an element in viewport height "vh" units, determine the size of the element in pixels.
• The given window size and returned element size are strings in the format "width x height", "1200 x 800" for example.
• "vw" units are the percent of window width. "50vw" for example, is 50% of the width of the window.
• "vh" units are the percent of window height. "50vh" for example, is 50% of the height of the window. */

function getElementSize(windowSize, elementVw, elementVh) {
  let vw=elementVw.split("").reverse().slice(2).reverse().join("")/100;
  let vh=elementVh.split("").reverse().slice(2).reverse().join("")/100;
  let sp=windowSize.split(" x ");
  return vw*sp[0]+" x "+vh*sp[1];
}

/* 08-03-2026: HSL Validator

Given a string, determine whether it is a valid CSS hsl() color value.
• A valid HSL value must be in the format "hsl(h, s%, l%)", where:
• h (hue) must be a number between 0 and 360 (inclusive).
• s (saturation) must be a percentage between 0% and 100%.
• l (lightness) must be a percentage between 0% and 100%.
• Spaces are only allowed:
• After the opening parenthesis
• Before and/or after the commas
• Before and/or after closing parenthesis
• Optionally, the value can end with a semi-colon (";").
For example, "hsl(240, 50%, 50%)" is a valid HSL value. */

function isValidHSL(hsl) {
  let sp=hsl.slice(4,hsl.length-1).replace(";","").replace(")","").split(",");
  let c1=sp[0]>=0 && sp[0]<=255;
  let p2=Number(sp[1].trimStart().trimEnd().split("").reverse().slice(1).reverse().join(""));
  let c2=p2>=0 && p2<=100 && sp[1].includes("%");
  let p3=Number(sp[2].trimStart().trimEnd().split("").reverse().slice(1).reverse().join(""));
  let c3=p3>=0 && p3<=100 && sp[2].includes("%");
  return c1 && c2 && c3;
}

/* 09-03-2026: Array Sum

Given an array of numbers, return the sum of all the numbers. */

function sumArray(numbers) {
  return numbers.reduce((a,b)=>a+b);
}

/* 10-03-2026: Array Insertion

Given an array, a value to insert into the array, and an index to insert the value at, return a new array with the value inserted at the specified index. */

function insertIntoArray(arr, value, index) {
  arr.splice(index,0,value);
  return arr;
}

/* 11-03-2026: Word Length Converter

Given a string of words, return a new string where each word is replaced by its length.
• Words in the given string will be separated by a single space
• Keep the spaces in the returned string.
For example, given "hello world", return "5 5".  */

function convertWords(str) {
  return str.split(" ").map((item)=>item.length).join(" ");
}

/* 12-03-2026: Domino Chain Validator 

Given a 2D array representing a sequence of dominoes, determine whether it forms a valid chain.
• Each element in the array represents a domino and will be an array of two numbers from 1 to 6, (inclusive).
• For the chain to be valid, the second number of each domino must match the first number of the next domino.
• The first number of the first domino and the last number of the last domino don't need to match anything. */

function isValidDominoChain(dominoes) {
  for(let i=1;i<dominoes.length;i++){
    if(dominoes[i][0]!=dominoes[i-1][1]) return false;
  }
  return true;
}

/* 13-03-2026: Parking Fee Calculator
Given two strings representing the time you parked your car and the time you picked it up, calculate the parking fee.
• The given strings will be in the format "HH:MM" using a 24-hour clock. So "14:00" is 2pm for example.
• The first string will be the time you parked your car, and the second will be the time you picked it up.
• If the pickup time is earlier than the entry time, it means the parking spanned past midnight into the next day.
Fee rules:
• Each hour parked costs $3.
• Partial hours are rounded up to the next full hour.
• If the parking spans overnight (past midnight), an additional $10 overnight fee is applied.
• There is a minimum fee of $5 (only used if the total would be less than $5).
Return the total cost in the format "$cost", "$5" for example. */

function calculateParkingFee(parkTime, pickupTime) {
  let parkT=parseInt(parkTime.slice(0,2)*60)+parseInt(parkTime.slice(3,5));
  let pickT=parseInt(pickupTime.slice(0,2)*60)+parseInt(pickupTime.slice(3,5));
  let diff;
  let total=0;
  if(parkT>pickT){
    diff=Math.ceil((24*60-(parkT-pickT))/60);
    total+=10;
  } else diff=Math.ceil((pickT-parkT)/60);
  total+=diff*3;
  total=diff<2?5:total;
  return "$"+total.toString();
}

/* 14-03-2026: Pi Day

Happy pi (π) day!
Given an integer (n), where n is between 1 and 1000 (inclusive), return the nth decimal of π.
• Make sure to return a number not a string.
π with its first five decimals is 3.14159. So given 5 for example, return 9, the fifth decimal.
You may have to find the first 1000 decimals of π somewhere. */

let p="31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989";

function getPiDecimal(n) {
  return parseInt(p[n]);
}

/* 15-03-2026: Captured Chess Pieces

Given an array of strings representing chess pieces you still have on the board, calculate the value of the pieces your opponent has captured.
In chess, you start with 16 pieces:
Piece    Abbreviation   Quantity   Value
Pawn             "P"                 8             1
Rook              "R"                 2             5
Knight           "N"                 2             3
Bishop          "B"                  2             3
Queen           "Q"                 1             9
King               "K"                 1             0
• The given array will only contain the abbreviations above.
• Any of the 16 pieces not included in the given array have been captured.
• Return the total value of all captured pieces, unless...
• If the King has been captured, return "Checkmate". */

function getCapturedValue(pieces) {
  let v={"P":1,"R":5,"N":3,"B":3,"Q":9,"K":0};
  if(!pieces.includes("K")) return "Checkmate";
  return 39-pieces.map((item)=>Number(v[item])).reduce((a,b)=>a+b);
}

/* 16-03-2026: Evenly Divisible

Given two integers, determine if you can evenly divide the first one by the second one. */

function isEvenlyDivisible(a, b) {
  return a%b==0;
}
