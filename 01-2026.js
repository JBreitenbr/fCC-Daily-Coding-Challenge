/* 01-01-2026 Resolution Streak
Given an array of arrays, where each sub-array represents a day of your resolution activities and contains three integers: the number of steps walked that day, the minutes of screen time that day, and the number of pages read that day; determine if you are keeping your resolutions.

The first sub-array is day 1, and second day 2, and so on.
A day is considered successful if all three of the following goals are met:

You walked at least 10,000 steps.
You had no more than 120 minutes of screen time.
You read at least five pages.
If all of the given days are successful, return "Resolution on track: N day streak." Where N is the number of successful days.

If one or more days is not a success, return "Resolution failed on day X: N day streak.". Where X is the day number of the first unsuccessful day, and N is the number of successful days before the first unsuccessful day.*/

function rCheck(arr){
  return arr[0]>=10000 && arr[1]<=120 && arr[2]>=5;
}

function resolutionStreak(days) {
  let m=days.map((item)=>rCheck(item));
  let sn=0;
  for(let i=0;i<m.length;i++){
    if(!m[i]){
      sn=i;
      break;
    }
  }
  if(sn>0){
    return `Resolution failed on day ${sn+1}: ${sn} day streak.`;
  } else return `Resolution on track: ${m.length} day streak.`;
}

/* 02-01-2026: Nth Fibonacci Number
Given an integer n, return the nth number in the fibonacci sequence.

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. The first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34. */

function nthFibonacci(n) {
  if (n <= 1) return n;
  let dp=new Array(n+1);
  dp[0]=0;
  dp[1]=0;
  dp[2]=1;
  dp[3]=1;
  for(let i=4;i<=n;i++){
    dp[i]=dp[i-1]+dp[i-2];
  }
  return dp[n];
}

/* 03-01-2026: Left-Handed Seat at the Table
Given a 4x2 matrix (array of arrays) representing the seating arrangement for a meal, determine how many seats a left-handed person can sit at.

A left-handed person cannot sit where a right-handed person would be in the seat to the immediate left of them.
In the given matrix:

An "R" is a seat occupied by a right-handed person.
An "L" is a seat occupied by a left-handed person.
An "U" is an unoccupied seat.
Only unoccupied seats are available to sit at.
The seats in the top row are facing "down", and the seats in the bottom row are facing "up" (like a table), so left and right are relative to the seat's orientation.
Corner seats only have one seat next to them.
For example, in the given matrix:

[
  ["U", "R", "U", "L"],
  ["U", "R", "R", "R"]
]
The top-left seat is cannot be sat in because there's a right-handed person to the left. The other two open seats can be sat in because there isn't a right-handed person to the left.
*/

function findLeftHandedSeats(table) {
  let sn=0;
  let row1=table[0];
  let row2=table[1].reverse();
  for(let i=0;i<row1.length;i++){
    if(row1[i]=="U"&&row1[i+1]!="R"){
      sn+=1;
    }
    if(row2[i]=="U"&&row2[i+1]!="R"){
      sn+=1;
    }
  }
  return sn;
}

/* 04-01-2026: Leap Year Calculator
Given an integer year, determine whether it is a leap year.

A year is a leap year if it satisfies the following rules:

The year is evenly divisible by 4, and
The year is not evenly divisible by 100, unless
The year is evenly divisible by 400. */

function isLeapYear(year) {
  return year%400==0||year%4==0&&year%100!=0;
}

/* 05-01-2026: Tire Pressure
Given an array with four numbers representing the tire pressures in psi of the four tires in your vehicle, and another array of two numbers representing the minimum and maximum pressure for your tires in bar, return an array of four strings describing each tire's status.

1 bar equal 14.5038 psi.
Return an array with the following values for each tire:

"Low" if the tire pressure is below the minimum allowed.
"Good" if it's between the minimum and maximum allowed.
"High" if it's above the maximum allowed. */

function tireStatus(pressuresPSI, rangeBar) {
  let c=14.5038;
  return pressuresPSI.map((item)=>item/c<rangeBar[0]?"Low":item/c<rangeBar[1]?"Good":"High");
}

/* 06-01-2026: vOwElcAsE
Given a string, return a new string where all vowels are converted to uppercase and all other alphabetical characters are converted to lowercase.

Vowels are "a", "e", "i", "o", and "u" in any case.
Non-alphabetical characters should remain unchanged. */

function vowelCase(str) {
  let v="aeiou".split("");
  let c="BCDFGHJKLMNPQRSTVWXYZ".split("");
  let res="";
  for(let i=0;i<str.length;i++){
    if(v.includes(str[i])){
      res+=str[i].toUpperCase();
    } else if(c.includes(str[i])){
      res+=str[i].toLowerCase();
    }
    else res+=str[i];
  }
  return res;
}

/* 07-01-2026: Markdown Unordered List Parser
Given the string of a valid unordered list in Markdown, return the equivalent HTML string.

An unordered list consists of one or more list items. A valid list item appears on its own line and:

Starts with a dash ("-"), followed by
At least one space, and then
The list item text.
The list is given as a single string with new lines separated by the newline character ("\n"). Do not include the newline characters in the item text.

Wrap each list item in HTML li tags, and the whole list of items in ul tags.

For example, given "- Item A\n- Item B", return "<ul><li>Item A</li><li>Item B</li></ul>". */

function parseUnorderedList(md) {
  let res="<ul>";
  let sp=md.replaceAll("\n","").split("- ");
  for(let i=0;i<sp.length;i++){
    if(sp[i]!=""){
      res+="<li>"+sp[i].trimStart()+"</li>"
    }
  }
  return res+"</ul>";
}

/* 08-01-2026: Sorted Array?
Given an array of numbers, determine if the numbers are sorted in ascending order, descending order, or neither.

If the given array is:

In ascending order (lowest to highest), return "Ascending".
In descending order (highest to lowest), return "Descending".
Not sorted in ascending or descending order, return "Not sorted". */

function isSorted(arr) {
  let c=[];
  for(let i=1;i<arr.length;i++){
    c.push(arr[i]-arr[i-1]);
  }
  let flt1=c.filter((item)=>item>0);
  let flt2=c.filter((item)=>item<0);
  return flt1.length+1==arr.length?"Ascending":flt2.length+1==arr.length?"Descending":"Not sorted";
} 

/* 09-01-2026: Circular Prime
Given an integer, determine if it is a circular prime.

A circular prime is an integer where all rotations of its digits are themselves prime.

For example, 197 is a circular prime because all rotations of its digits: 197, 971, and 719, are prime numbers. */

function isPrime(n) {
  let arr=Array.from(Array(n).keys()).map((item)=>item+1);
  let flt=arr.filter((item)=>n%item==0&&item>1);
  return flt.length==1?true:false;
}

function isCircularPrime(n) {
  let s=n.toString();
  let c=[s];
  for(let i=1;i<s.length;i++){
    let t=c[i-1].slice(1,c[i-1])+c[i-1][0];
    c.push(t);
  }
  return c.map((item)=>Number(item)).every(isPrime);
}

/* 10-01-2026: Tic-Tac-Toe
Given a 3×3 matrix (an array of arrays) representing a completed Tic-Tac-Toe game, determine the winner.

Each element in the given matrix is either an "X" or "O".
A player wins if they have three of their characters in a row - horizontally, vertically, or diagonally.

Return:

"X wins" if player X has three in a row.
"O wins" if player O has three in a row.
"Draw" if no player has three in a row.  */

function ticTacToe(board) {
let trans = board[0].map((_, colIndex) => board.map(row => row[colIndex]));
  let diag1=board[0][0]+board[1][1]+board[2][2];
  let diag2=board[0][2]+board[1][1]+board[2][0];
  for(let i=0;i<3;i++){
    if(board[i].join("")=="OOO"||trans[i].join("")=="OOO"||diag1=="OOO"||diag2=="OOO") return "O wins";
    else if(board[i].join("")=="XXX"||trans[i].join("")=="XXX"||diag1=="XXX"||diag2=="XXX") return "X wins";
  }
  return "Draw";
}

/* 11-01-2026: Par for the Hole
Given two integers, the par for a golf hole and the number of strokes a golfer took on that hole, return the golfer's score using golf terms.

Return:

"Hole in one!" if it took one stroke.
"Eagle" if it took two strokes less than par.
"Birdie" if it took one stroke less than par.
"Par" if it took the same number of strokes as par.
"Bogey" if it took one stroke more than par.
"Double bogey" if took two strokes more than par. */

function golfScore(par, strokes) {
  if(strokes==1) return "Hole in one!";
  else if(par-strokes==2) return "Eagle";
  else if(par-strokes==1) return "Birdie";
  else if(par==strokes) return "Par";
  else if(strokes-par==1) return "Bogey";
  else if(strokes-par==2)
  return "Double bogey";
}

/* 12-01-2026: Plant the Crop
Given an integer representing the size of your farm field, and "acres" or "hectares" representing the unit for the size of your farm field, and a type of crop, determine how many plants of that type you can fit in your field.

1 acre equals 4046.86 square meters.
1 hectare equals 10,000 square meters.
Here's a list of crops that will be given as input and how much space a single plant takes:

Crop	Space per plant
"corn"	1 square meter
"wheat"	0.1 square meters
"soybeans"	0.5 square meters
"tomatoes"	0.25 square meters
"lettuce"	0.2 square meters
Return the number of plants that fit in the field, rounded down to the nearest whole plant. */

function getNumberOfPlants(fieldSize, unit, crop) {
let cObj={"corn":1,
"wheat":0.1,"soybeans":0.5,
"tomatoes":	0.25,
"lettuce":0.2 };
  let fac=unit=="acres"?4046.86:10000;
  return Math.floor(1/cObj[crop]*fac*fieldSize);
}

/* 13-01-2026: Odd or Even?
Given a positive integer, return "Odd" if it's an odd number, and "Even" if it's even.*/

function oddOrEven(n) {
  return n%2==1?"Odd":"Even";
}

/* 14-01-2026: Markdown Link Parser
Given the string of a link in Markdown, return the equivalent HTML string.

A Markdown image has the following format: "[link_text](link_url)". Return the string of the HTML a tag with the href set to the link_url and the link_text as the tag content.

For example, given "[freeCodeCamp](https://freecodecamp.org/)" return '<a href="https://freecodecamp.org/">freeCodeCamp</a>';

Note: The console may not display HTML tags in strings when logging messages — check the browser console to see logs with tags included. */

function parseLink(md) {
  let sp1=md.split("]");
  let sp2=md.split("(");
  let lt=sp1[0].slice(1);
  let lu=sp2[1].slice(0,sp2[1].length-1)
  let res='<a href="'+lu+'">'+lt+'</a>';
  return res;
}

/* 15-01-2026: Array Swap
Given an array with two values, return an array with the values swapped.

For example, given ["A", "B"] return ["B", "A"]. */

function arraySwap(arr) {
  return arr.reverse();
}

/* 16-01-2026: Integer Hypotenuse
Given two positive integers representing the lengths for the two legs (the two short sides) of a right triangle, determine whether the hypotenuse is an integer.
*/

function isIntegerHypotenuse(a, b) {
  let c=Math.sqrt(a*a+b*b);
  return c==parseInt(c);
}

/* 17-01-2026: Knight Moves
Given the position of a knight on a chessboard, return the number of valid squares the knight can move to.
A standard chessboard is 8x8, with columns labeled A through H (left to right) and rows labeled 1 through 8 (bottom to top). It looks like this:
A8B8C8D8E8F8G8H8
A7B7C7D7E7F7G7H7
A6B6C6D6E6F6G6H6
A5B5C5D5E5F5G5H5
A4B4C4D4E4F4G4H4
A3B3C3D3E3F3G3H3
A2B2C2D2E2F2G2H2
A1B1C1D1E1F1G1H1
A knight moves in an "L" shape: two squares in one direction (horizontal or vertical), and one square in the perpendicular direction.
This means a knight can move to up to eight possible positions, but fewer when near the edges of the board. For example, if a knight was at A1, it could only move to B3 or C2.*/

let moves = ([i, j]) => [[i - 2, j - 1],[i - 1, j - 2],[i - 2, j + 1],[i - 1, j + 2],[i + 2, j - 1],[i + 1, j - 2],[i + 2, j + 1],[i + 1, j + 2]];

 function knightMoves(pos) {
  let row=8-Number(pos[1]);                     
  let col=pos.charCodeAt(0)-65;
  return moves([row,col]).filter((item)=>item[0]>=0&&item[0]<=7&&item[1]>=0&&item[1]<=7).length;
}

/* 18-01-2026: Free Shipping
Given an array of strings representing items in your shopping cart, and a number for the minimum order amount to qualify for free shipping, determine if the items in your shopping cart qualify for free shipping.
The given array will contain items from the list below:
Item       Price
"shirt"     34.25
"jeans"    48.50
"shoes"   75.00
"hat"        19.95
"socks"    15.00
"jacket"  109.95 */

function getsFreeShipping(cart, minimum) {
  let p={"shirt":34.25,"jeans":48.50,"shoes":75.00,"hat":19.95,"socks":15.00,"jacket":109.95};
  return cart.map((item)=>p[item]).reduce((a,b)=>a+b,0)>minimum;
}

/* 19-01-2026 Energy Consumption
Given the number of Calories burned during a workout, and the number of watt-hours used by your electronic devices during that workout, determine which one used more energy.
To compare them, convert both values to joules using the following conversions:
• 1 Calorie equals 4184 joules.
• 1 watt-hour equals 3600 joules.
Return:
• "Workout" if the workout used more energy.
• "Devices" if the device used more energy.
• "Equal" if both used the same amount of energy. */

function compareEnergy(caloriesBurned, wattHoursUsed) {

  return caloriesBurned*4184>wattHoursUsed*3600?"Workout":caloriesBurned*4184<wattHoursUsed*3600?"Devices":"Equal";
}

/* 20-01-2026 Consonant Case
Given a string representing a variable name, convert it to consonant case using the following rules:
• All consonants should be converted to uppercase.
• All vowels (a, e, i, o, u in any case) should be converted to lowercase.
• All hyphens (-) should be converted to underscores (_). */

function toConsonantCase(str) {
  let v="AEIOU".split("");
  let c="bcdfghjklmnpqrstvwxyz".split("");
  let stri=str.replaceAll("-","_");
  let res="";
  for(let i=0;i<stri.length;i++){
    if(v.includes(stri[i])){
      res+=stri[i].toLowerCase();
    } else if(c.includes(stri[i])){
      res+=stri[i].toUpperCase();
    }
    else res+=stri[i];
  }
  return res;
}

/*  21-01-2026: Markdown Inline Code Parser
Given a string of Markdown that includes one or more inline code blocks, return the equivalent HTML string.
Inline code blocks in Markdown use a single backtick (`) at the start and end of the code block text.
Return the given string with all code blocks converted to HTML code tags.
For example, given the string "Use `let` to declare the variable.", return "Use <code>let</code> to declare the variable.".
Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included. */

function parseInlineCode(md) {
  let sp=md.split("`").map((item)=>item==item.trimStart()&&item==item.trimEnd()&&![".","!","?",","].includes(item)?"<code>"+item+"</code>":item);
  console.log(sp);
  let res="";
  for(let i=0;i<sp.length;i++){
    res+=sp[i];
  }
  return res;
}

/* 22-01-2026: Class Average
Given an array of exam scores (numbers), return the average score in form of a letter grade according to the following chart:
Average Score  Letter Grade
97-100               "A+"
93-96                 "A"
90-92                 "A−"
87-89                 "B+"
83-86                 "B"
80-82.                "B-"
77-79                 "C+"
73–76                "C"
70-72                 "C-"
67-69                 "D+"
63-66                  "D"
60–62                "D-"
below 60            "F"
Calculate the average by adding all scores in the array and dividing by the total number of scores. */

function getAverageGrade(scores) {
  let sc=Math.floor(scores.reduce((a,b)=>a+b,0)/scores.length);
  let gr=[...Array(11).fill("A"),...Array(10).fill("B"),...Array(10).fill("C"),...Array(10).fill("D")].map((item,index)=>[1,2,3].includes(index%10)?(item+"+"):[8,9,0].includes(index%10)?(item+"-"):item);
  gr[0]="A+";
  let rg=Array.from(Array(41).keys()).map((item)=>100-item);
  let res = {};
    rg.forEach((key, index) => {res[key] = gr[index];});
  return sc<60?"F":res[sc.toString()];
}

