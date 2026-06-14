/* 01-11-2025: Signature Validation
Given a message string, a secret key string, and a signature number, determine if the signature is valid using this encoding method:

Letters in the message and secret key have these values:
a to z have values 1 to 26 respectively.
A to Z have values 27 to 52 respectively.
All other characters have no value.
Compute the signature by taking the sum of the message plus the sum of the secret key.
For example, given the message "foo" and the secret key "bar", the signature would be 57:

f (6) + o (15) + o (15) = 36
b (2) + a (1) + r (18) = 21
36 + 21 = 57
Check if the computed signature matches the provided signature.
*/

function verify(message, key, signature) {
  let a0="abcdefghijklmnopqrstuvwxyz";
  let a=[...a0.split(""),a0.toUpperCase().split("")].flat();
  let r=Array.from(Array(52).keys()).map((item)=>item+1);
  let obj = {};
  a.forEach((key, index) => {obj[key] = r[index];});
    let s1=message.split("").map((item)=>a.includes(item)?obj[item]:0).reduce((a,b)=>a+b,0);
    let s2=key.split("").map((item)=>a.includes(item)?obj[item]:0).reduce((a,b)=>a+b,0);
  return s1+s2==signature;
        }
verify("Check out the freeCodeCamp podcast,", "in the mobile app", 514)

/* 02-11-2025: Infected
On November 2nd, 1988, the first major internet worm was released, infecting about 10% of computers connected to the internet after only a day.

In this challenge, you are given a number of days that have passed since an internet worm was released, and you need to determine how many computers are infected using the following rules:

On day 0, the first computer is infected.
Each subsequent day, the number of infected computers doubles.
Every 3rd day, a patch is applied after the virus spreads and reduces the number of infected computers by 20%. Round the number of patched computers up to the nearest whole number.
For example, on:

Day 0: 1 total computer is infected.
Day 1: 2 total computers are infected.
Day 2: 4 total computers are infected.
Day 3: 8 total computers are infected. Then, apply the patch: 8 infected * 20% = 1.6 patched. Round 1.6 up to 2. 8 computers infected - 2 patched = 6 total computers infected after day 3.
Return the number of total infected computers after the given amount of days have passed.
*/

function infected(days) {
  let p=[1];
  for(let i=1;i<26;i++){
    p[i]=2*p[i-1];
    if(i%3==0){
      p[i]-=Math.ceil(0.2*p[i]);
    }
  }
  return p[days];
}

/* 03-11-2025: Word Counter
Given a sentence string, return the number of words that are in the sentence.

Words are any sequence of non-space characters and are separated by a single space.
*/

function countWords(sentence) {
  return sentence.split(" ").length;
}

/* 04-11-2025: Image Search
On November 4th, 2001, Google launched its image search, allowing people to find images using search terms. In this challenge, you will imitate the image search.

Given an array of image names and a search term, return an array of image names containing the search term.

Ignore the case when matching the search terms.
Return the images in the same order they appear in the input array.
*/

function imageSearch(images, term) {
  let res=[];
  let t=term.toLowerCase();
  for(let i=0;i<images.length;i++){
    if(images[i].toLowerCase().includes(t)){
      res.push(images[i]);
    }
  }
  return res;
}

/* 05-11-2025: Matrix Builder
Given two integers (a number of rows and a number of columns), return a matrix (an array of arrays) filled with zeros (0) of the given size.

For example, given 2 and 3, return:

[
  [0, 0, 0],
  [0, 0, 0]
]
*/

function buildMatrix(rows, cols) {
  return Array(rows).fill("").map((item)=>Array(cols).fill(0));
}

/* 06-11-2025: Weekday Finder
Given a string date in the format YYYY-MM-DD, return the day of the week.

Valid return days are:

"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
Be sure to ignore time zones.
*/

function getWeekday(dateString) {
  let wD={0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"};
  let d=new Date(dateString).getDay();
  return wD[d];
}

/* 07-11-2025: Counting Cards
A standard deck of playing cards has 13 unique cards in each suit. Given an integer representing the number of cards to pick from the deck, return the number of unique combinations of cards you can pick.

Order does not matter. Picking card A then card B is the same as picking card B then card A.
For example, given 52, return 1. There's only one combination of 52 cards to pick from a 52 card deck. And given 2, return 1326, There's 1326 card combinations you can end up with when picking 2 cards from the deck.
*/

function combinations(cards) {
  if(cards>52 || cards<0) {return 0;}
  else if(cards==52 || cards==0){
    return 1;
  }
  else if(cards==51 || cards==1){
    return 52;
  } else {
    if(cards>26){
      cards=52-cards;
    }
    let res=52;
    for(let i = 2; i <= cards; i++) res *= (52 - i + 1) / i;
  return Math.round(res);
  }
}

/* 08-11-2025: Character Limit
In this challenge, you are given a string and need to determine if it fits in a social media post. Return the following strings based on the rules given:

"short post" if it fits within a 40-character limit.
"long post" if it's greater than 40 characters and fits within an 80-character limit.
"invalid post" if it's too long to fit within either limit.
*/

function canPost(message) {
  return message.length<=40?"short post":message.length<=80?"long post":"invalid post";
}

/* 09-11-2025: Word Search
Given a matrix (an array of arrays) of single letters and a word to find, return the start and end indices of the word in the matrix.

The given matrix will be filled with all lowercase letters (a-z).
The word to find will always be in the matrix exactly once.
The word to find will always be in a straight line in one of these directions:
left to right
right to left
top to bottom
bottom to top
For example, given the matrix:

[
  ["a", "c", "t"],
  ["t", "a", "t"],
  ["c", "t", "c"]
]
And the word "cat", return:

[[0, 1], [2, 1]]
Where [0, 1] are the indices for the "c" (start of the word), and [2, 1] are the indices for the "t" (end of the word).
*/

function findWord(matrix, word) {
    let pre=[];
    let l=matrix.length;
    let m=matrix;
    let wL=word.length;
    let t=m[0].map((_, colIndex)=>m.map(row=>row[colIndex]));
    for(let i=0;i<l;i++){
        if(m[i].join("").slice(0,wL)==word){
            pre.push([i,wL==l?0:1],[i,l-1]);
           } 
        if(m[i].reverse().join("").slice(0,wL)==word){
            pre.push([i,l-1],[i,wL==l?0:1]);
           } 
        if(t[i].join("").slice(0,wL)==word){
            pre.push([wL==l?0:1,i],[l-1,i]);
           } 
        if(t[i].reverse().join("").slice(0,wL)==word){
            pre.push([l-1,i],[wL==l?0:1,i]);
           }
        return pre;
}
findWord([["f", "x", "o", "x"], ["o", "x", "o", "f"], ["f", "o", "f", "x"], ["f", "x", "x", "o"]], "fox") 

/* 10-11-2025: Extension Extractor
Given a string representing a filename, return the extension of the file.

The extension is the part of the filename that comes after the last period (.).
If the filename does not contain a period or ends with a period, return "none".
The extension should be returned as-is, preserving case.
 */
  
function getExtension(filename) {
  let s=filename.split(".");
  if(s.length>1 && s[s.length-1]!=''){
    return s[s.length-1];
  }
  else return 'none';
}

/* 11-11-2025: Vowels and Consonants
Given a string, return an array with the number of vowels and number of consonants in the string.

Vowels consist of a, e, i, o, u in any case.
Consonants consist of all other letters in any case.
Ignore any non-letter characters.
For example, given "Hello World", return [3, 7].
*/

function count(str) {
let vReg=/[aeiou]/gi;
let lReg=/[a-z]/gi;
  let s1=str.split("").map((item)=>item.match(vReg)?1:0).reduce((a,b)=>a+b,0);
  let s2=str.split("").map((item)=>item.match(lReg)?1:0).reduce((a,b)=>a+b,0);
  return [s1,s2-s1];
}

/* 12-11-2025: Email Signature Generator
Given strings for a person's name, title, and company, return an email signature as a single string using the following rules:

The name should appear first, preceded by a prefix that depends on the first letter of the name. For names starting with (case-insensitive):
A-I: Use >> as the prefix.
J-R: Use -- as the prefix.
S-Z: Use :: as the prefix.
A comma and space (, ) should follow the name.
The title and company should follow the comma and space, separated by " at " (with spaces around it).
For example, given "Quinn Waverly", "Founder and CEO", and "TechCo" return "--Quinn Waverly, Founder and CEO at TechCo".
*/
  
function generateSignature(name, title, company) {
  let r1=/[A-I]/;
  let r2=/[J-R]/;
  let r3=/[S-Z]/;
  let stri=r1.test(name[0])?">>":r2.test(name[0])?"--":"::";
  stri+=name+", "+title+" at "+ company;
  return stri;
 }

/* 13-11-2025: Array Shift
Given an array and an integer representing how many positions to shift the array, return the shifted array.

A positive integer shifts the array to the left.
A negative integer shifts the array to the right.
The shift wraps around the array.
For example, given [1, 2, 3] and 1, shift the array 1 to the left, returning [2, 3, 1].
*/

function shiftArray(arr, n) {
  let rep=[].concat(...new Array(5).fill(arr));
  let s=rep.slice(n,n+arr.length);
  if(n<0){
    s=rep.slice(n+arr.length,n+2*arr.length);
  }
  return s;
}
shiftArray([1,2,3],-1);
shiftArray(["alpha", "bravo", "charlie"], 5) 
shiftArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 15)

/* 14-11-2025: Is It the Weekend?
Given a date in the format "YYYY-MM-DD", return the number of days left until the weekend.

The weekend starts on Saturday.
If the given date is Saturday or Sunday, return "It's the weekend!".
Otherwise, return "X days until the weekend.", where X is the number of days until Saturday.
If X is 1, use "day" (singular) instead of "days" (plural).
Make sure the calculation ignores your local timezone.
*/

function daysUntilWeekend(dateString) {
  let wD=new Date(dateString).getDay();
  if(wD==0 || wD==6){
  return "It's the weekend!";
  } else {
    return wD<5?`${6-wD} days until the weekend.`:"1 day until the weekend."
  }
}

/* 15-11-2025: GCD
Given two positive integers, return their greatest common divisor (GCD).

The GCD of two integers is the largest number that divides evenly into both numbers without leaving a remainder.
For example, the divisors of 4 are 1, 2, and 4. The divisors of 6 are 1, 2, 3, and 6. So given 4 and 6, return 2, the largest number that appears in both sets of divisors.
*/

function gcd(x, y) {
  return Array.from(Array(x>y?x:y).keys()).map((item)=>item+1).filter((item)=>x%item==0&&y%item==0).reverse()[0];
}

/* 16-11-2025: Rectangle Count
Given two positive integers representing the width and height of a rectangle, determine how many rectangles can fit in the given one.

Only count rectangles with integer width and height.
For example, given 1 and 3, return 6. Three 1x1 rectangles, two 1x2 rectangles, and one 1x3 rectangle.
*/

function countRectangles(width, height) {
   let count = 0;
   for (let i = 1; i <= width; i++) { 
     for (let j = 1; j <= height; j++) { 
      count += (width - i + 1) * (height - j + 1); 
    }
      }
  return count;
}

/* 17-11-2025: Fingerprint Test
Given two strings representing fingerprints, determine if they are a match using the following rules:

Each fingerprint will consist only of lowercase letters (a-z).
Two fingerprints are considered a match if:
They are the same length.
The number of differing characters does not exceed 10% of the fingerprint length.
*/

function isMatch(fingerprintA, fingerprintB) {
  let l1=fingerprintA.length;
  let l2=fingerprintB.length;
  if(l1!==l2){
    return false;
  }
  else {
  if(fingerprintA===fingerprintB){
    return true;
  }
  else {
  let sn=0;
    for(let i=0;i<l1;i++){
      if(fingerprintA[i]!==fingerprintB[i]){
        sn+=1;
      }
    }
    return sn/l1<=0.1?true:false;
  }
  }
}

/* 18-11-2025: 100 Characters
Welcome to the 100th Daily Coding Challenge!

Given a string, repeat its characters until the result is exactly 100 characters long. If your repetitions go over 100 characters, trim the extra so it's exactly 100.
*/

function oneHundred(chars) {
let rep=[].concat(...new Array(100).fill(chars)).join("").slice(0,100);
  return rep;
}

/* 19-11-2025 Markdown Heading Converter
Given a string representing a Markdown heading, return the equivalent HTML heading.

A valid Markdown heading must:

Start with zero or more spaces, followed by
1 to 6 hash characters (#) in a row, then
At least one space. And finally,
The heading text.
The number of hash symbols determines the heading level. For example, one hash symbol corresponds to an h1 tag, and six hash symbols correspond to an h6 tag.

If the given string doesn't have the exact format above, return "Invalid format".

For example, given "# My level 1 heading", return "<h1>My level 1 heading</h1>".

Note: The console may not display HTML tags in strings when logging messages. Check the browser console to see logs with tags included. */

function convert(heading) {
  let h=heading.trimStart();
  let s=h.split(" ");
  let r=/^[#]{1,6}$/;
  console.log(s);
  if(!r.test(s[0])){
    return "Invalid format";
  }
  let res="";
  let s2=s.slice(1).filter((item)=>item!="").join(" ");
  if(s[0]=="#"){
    res="<h1>"+s2+"</h1>";
  } else if(s[0]=="##"){
    res="<h2>"+s2+"</h2>";
  } else if(s[0]=="###"){
    res="<h3>"+s2+"</h3>";
  } else if(s[0]=="####"){
    res="<h4>"+s2+"</h4>";
  } else if(s[0]=="#####"){
    res="<h5>"+s2+"</h5>";
  } else if(s[0]=="######"){
    res="<h6>"+s2+"</h6>";
  }
  return res;
}

/* 20-11-2025 Longest Word
Given a sentence string, return the longest word in the sentence.

Words are separated by a single space.
Only letters (a-z, case-insensitive) count toward the word's length.
If there are multiple words with the same length, return the first one that appears.
Return the word as it appears in the given string, with punctuation removed.*/

function longestWord(sentence) {
  let reg=/[A-Za-z ]/gi;
  let s=sentence.match(reg).join("").split(" ").sort((a,b)=>b.length-a.length);
  return s[0];
}

/* 21-11-2025 LCM
Given two integers, return the least common multiple (LCM) of the two numbers.

The LCM of two numbers is the smallest positive integer that is a multiple of both numbers. For example, given 4 and 6, return 12 because:

Multiples of 4 are 4, 8, 12 and so on.
Multiples of 6 are 6, 12, 18 and so on.
12 is the smallest number that is a multiple of both.*/
  
function lcm(a, b) {
  let gcd=Array.from(Array(a>b?a:b).keys()).map((item)=>item+1).filter((item)=>a%item==0 && b%item==0).reverse()[0];
  return a*b/gcd;
}

/* 22-11-2025: Recipe Scaler
Given an array of recipe ingredients and a number to scale the recipe, return an array with the quantities scaled accordingly.

Each item in the given array will be a string in the format: "quantity unit ingredient". For example "2 C Flour".
Scale the quantity by the given number. Do not include any trailing zeros and do not convert any units.
Return the scaled items in the same order they are given.*/

function scaleRecipe(ingredients, scale) {
  let ing=ingredients.map((item)=>item.split(" ")).map((item)=>[item[0]*scale,item.slice(1)]).map((item)=>item.flat()).map((item)=>item.join(" "));
  return ing;
}

/* 23-11-2025: Character Count
Given a sentence string, return an array with a count of each character in alphabetical order.

Treat upper and lowercase letters as the same letter when counting.
Ignore numbers, spaces, punctuation, etc.
Return the count and letter in the format "letter count". For instance, "a 3".
All returned letters should be lowercase.
Do not return a count of letters that are not in the given string.*/

function countCharacters(sentence) {
  let reg=/[A-Za-z]/gi;
  let x=sentence.match(reg).map((item)=>item.toLowerCase()).sort();
  let obj={};
  for(let i=0;i<x.length;i++){
    if(!Object.keys(obj).includes(x[i])){
      obj[x[i]]=1
    } else {
      obj[x[i]]+=1
    }
  }
  let res=[]
  for(let i=0;i<x.length;i++){
    res.push(x[i]+" "+obj[x[i]])
  }
  return Array.from(new Set(res));
}

/* 24-11-2025: Message Validator
Given a message string and a validation string, determine if the message is valid.

A message is valid if each word in the message starts with the corresponding letter in the validation string, in order.
Letters are case-insensitive.
Words in the message are separated by single spaces.*/

function isValidMessage(msg, val) {
  if(msg.split(" ").length!=val.length){
    return false;
  } else {
    let acr=msg.toLowerCase().split(" ").map((item)=>item[0]).join("");
    if(acr==val.toLowerCase()){
      return true;
    } else return false;
  }
}

/* 25-11-2025: FizzBuzz
Given an integer (n), return an array of integers from 1 to n (inclusive), replacing numbers that are multiple of:

3 with "Fizz".
5 with "Buzz".
3 and 5 with "FizzBuzz".*/

function fizzBuzz(n) {
  let arr=[];
  for(let i=0;i<n;i++){
    if((i+1)%3!=0&&(i+1)%5!=0){
      arr.push(i+1);
    }
    else if((i+1)%3==0&&(i+1)%5!=0){arr.push("Fizz");
    }
    else if((i+1)%3!=0&&(i+1)%5==0){
      arr.push("Buzz");
    }
    else arr.push("FizzBuzz");
  }
  return arr;
}
  
/* 26-11-2025: BuzzFizz
Given an array, determine if it is a correct FizzBuzz sequence from 1 to the last item in the array. A sequence is correct if:

Numbers that are multiples of 3 are replaced with "Fizz"
Numbers that are multiples of 5 are replaced with "Buzz"
Numbers that are multiples of both 3 and 5 are replaced with "FizzBuzz"
All other numbers remain as integers in ascending order, starting from 1.
The array must start at 1 and have no missing or extra elements. */

function isFizzBuzz(seq) {
  let fb=["Fizz","Buzz","FizzBuzz"];
  for(let i=0;i<seq.length;i++){
    if(seq[i]!="Fizz"&&(i+1)%3==0&&(i+1)%5!=0 || seq[i]!="Buzz"&&(i+1)%3!=0&&(i+1)%5==0||seq[i]!="FizzBuzz"&&(i+1)%3==0&&(i+1)%5==0||fb.includes(seq[i])&&(i+1)%3!=0&&(i+1)%5!=0){
      return false;
    };
  }
  return true;
}

/* 27-11-2025: What's My Age Again?
Given the date of someone's birthday in the format YYYY-MM-DD, return the person's age as of November 27th, 2025.

Assume all birthdays are valid dates before November 27th, 2025.
Return the age as an integer.
Be sure to account for whether the person has already had their birthday in 2025.*/

function calculateAge(birthday) {
  let b=(new Date(birthday)).valueOf();
  let now=Date.now();
  let diff=Math.floor((now-b)/31556952000);
  return diff;
}

/* 28-11-2025: 
Word Guesser
Given two strings of the same length, a secret word and a guess, compare the guess to the secret word using the following rules:

The secret word and guess will only consist of uppercase letters ("A" to "Z");
For each letter in the guess, replace it with a number according to how it matches the secret word:
"2" if the letter is in the secret word and in the correct position.
"1" if the letter is in the secret word but in the wrong position.
"0" if the letter is not in the secret word.
Each letter in the secret word can be used at most once.
Exact matches ("2") are assigned first, then partial matches ("1") are assigned from left to right for remaining letters.
If a letter occurs multiple times in the guess, it can only match as many times as it appears in the secret word.
For example, given a secret word of "APPLE" and a guess of "POPPA", return "10201":
The first "P" is not in the correct location ("1"), the "O" isn't in the secret word ("0"), the second "P" is in the correct location ("2"), the third "P" is a zero ("0") because the two "P"'s in the secret word have been used, and the "A" is not in the correct location ("1").*/

/* Hier hat das liebe ChatGPT geholfen, nachdem ich lange erfolglos nach einer Lösung gesucht hatte */
function compare(secret, guess) {
  const n = secret.length;
  const result = Array(n).fill('0');

  // Merkt sich, welche Positionen im Secret/Guess schon benutzt wurden
  const secretUsed = Array(n).fill(false);
  const guessUsed = Array(n).fill(false);

  // 1. Runde: exakte Treffer ("2")
  for (let i = 0; i < n; i++) {
    if (guess[i] === secret[i]) {
      result[i] = '2';
      secretUsed[i] = true;
      guessUsed[i] = true;
    }
  }

  // 2. Runde: teilweise Treffer ("1"), von links nach rechts
  for (let i = 0; i < n; i++) {
    // schon exakter Treffer? Dann überspringen
    if (guessUsed[i]) continue;

    const ch = guess[i];

    // Suche denselben Buchstaben irgendwo im Secret,
    // aber nur an noch nicht benutzten Positionen
    for (let j = 0; j < n; j++) {
      if (!secretUsed[j] && secret[j] === ch) {
        result[i] = '1';
        secretUsed[j] = true; // diese Secret-Position ist jetzt "verbraucht"
        break;                // nur einmal matchen!
      }
    }
  }

  return result.join('');
}
  
/* 29-11-2025: Ball Trajectory
Today's challenge is inspired by the video game Pong, which was released November 29, 1972.

Given a matrix (array of arrays) that includes the location of the ball (2), and the previous location of the ball (1), return the matrix indices for the next location of the ball.

The ball always moves in a straight line.
The movement direction is determined by how the ball moved from 1 to 2.
The edges of the matrix are considered walls. If the ball hits a:
top or bottom wall, it bounces by reversing its vertical direction.
left or right wall, it bounces by reversing its horizontal direction.
corner, it bounces by reversing both directions.*/

// Hier hat wieder das liebe ChatGPT geholfen, da ich zunächst keinen Plan hatte.
function getNextLocation(matrix) {
  const rows = matrix.length;
  const cols = matrix[0].length;

  let r1, c1, r2, c2;

  // 1. Finde Position von 1 (vorher) und 2 (jetzt)
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (matrix[i][j] === 1) {
        r1 = i;
        c1 = j;
      } else if (matrix[i][j] === 2) {
        r2 = i;
        c2 = j;
      }
    }
  }

  // 2. Bewegungsrichtung bestimmen
  const dx = r2 - r1; // vertikale Bewegung
  const dy = c2 - c1; // horizontale Bewegung

  // 3. Naive nächste Position
  let nr = r2 + dx;
  let nc = c2 + dy;

  // 4. Wände checken – vertikal
  if (nr < 0 || nr >= rows) {
    const ndx = -dx;      // vertikale Richtung umdrehen
    nr = r2 + ndx;
  }

  // 5. Wände checken – horizontal
  if (nc < 0 || nc >= cols) {
    const ndy = -dy;      // horizontale Richtung umdrehen
    nc = c2 + ndy;
  }

  return [nr, nc];
}

/* 30-11-2025: AI Detector
Today's challenge is inspired by the release of ChatGPT on November 30, 2022.

Given a string of one or more sentences, determine if it was likely generated by AI using the following rules:

It contains two or more dashes (-).

It contains two or more sets of parenthesis (()). Text can be within the parenthesis.

It contains three or more words with 7 or more letters.

Words are separated by a single space and only consist of letters (A-Z). Don't include punctuation or other non-letters as part of a word.

If the given sentence meets any of the rules above, return "AI", otherwise, return "Human".*/

function detectAI(text) {
  let spl=text.split(" ");
  let flt1=spl.filter((item)=>item[0]=="(" && item[item.length-1]==")");
  let flt2=spl.filter((item)=>item.length>=7);
  if(text.split("-").length>2 || flt1.length>=2 || flt2.length>=3)
  return "AI";
  else return "Human";
}
