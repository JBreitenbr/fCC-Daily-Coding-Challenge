/* 01-09-2025: Tribonacci Sequence
The Tribonacci sequence is a series of numbers where each number is the sum of the three preceding ones. When starting with 0, 0 and 1, the first 10 numbers in the sequence are 0, 0, 1, 1, 2, 4, 7, 13, 24, 44.

Given an array containing the first three numbers of a Tribonacci sequence, and an integer representing the length of the sequence, return an array containing the sequence of the given length.

Your function should handle sequences of any length greater than or equal to zero.
If the length is zero, return an empty array.
Note that the starting numbers are part of the sequence.
*/

function tribo(n,first,second,third) {
if(n==0){return first;}
if(n==1){return second;}
if(n==2){return third;}
if(n>2){
return tribo(n-1,first,second,third)+tribo(n-2,first,second,third)+tribo(n-3,first,second,third);}
}
function tribArr(n,first,second,third){
let targ=[];
for(let i=0;i<n;i++){
targ.push(tribo(i,first,second,third));}
return targ;
}

function tribonacciSequence(startSequence, length) {
    if(length==0){ return [];}
    else if(length==1){
      return startSequence.slice(0,1);
    }
    else if(length==2){
      return startSequence.slice(0,2);
    }
    else if(length==3){
      return startSequence;
    }
    else return tribArr(length,startSequence[0],startSequence[1],startSequence[2]);
}

/* 02-09-2025: RGB to Hex
Given a CSS rgb(r, g, b) color string, return its hexadecimal equivalent.

Here are some example outputs for a given input:

Input	Output
"rgb(255, 255, 255)"	"#ffffff"
"rgb(1, 2, 3)"	"#010203"
Make any letters lowercase.
Return a # followed by six characters. Don't use any shorthand values.
*/

function rgbToHex(rgb) {
  let spl=rgb.split(",");
  let r=Number(spl[0].substring(4)).toString(16);
  if(r.length<2){r="0"+r;};
  let g=Number(spl[1]).toString(16);
  if(g.length<2){g="0"+g;};
  let b=Number(spl[2].replace(")","")).toString(16);
  if(b.length<2){b="0"+b;};
  let stri="#"+r+g+b;
  return stri;
}

/* 03-09-2025: Pangram
Given a word or sentence and a string of lowercase letters, determine if the word or sentence uses all the letters from the given set at least once and no other letters.

Ignore non-alphabetical characters in the word or sentence.
Ignore letter casing in the word or sentence.
*/

function isPangram(sentence, letters) {
  let s=sentence.toLowerCase().replaceAll(" ","").replaceAll(".","").replaceAll("!","").split(""); 
let l=letters.toLowerCase().split("");
  for(let i=0;i<s.length;i++){ if(!l.includes(s[i])){
    return false;
  }}
  for(let i=0;i<l.length;i++){
    if(!s.includes(l[i])){
      return false;
    }
  }
  return true;
}

/* 04-09-2025: Vowel Repeater
Given a string, return a new version of the string where each vowel is duplicated one more time than the previous vowel you encountered. For instance, the first vowel in the sentence should remain unchanged. The second vowel should appear twice in a row. The third vowel should appear three times in a row, and so on.

The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
The original vowel should keeps its case.
Repeated vowels should be lowercase.
All non-vowel characters should keep their original case.
*/

function indices(source, find) {
  if (!source) {return [];}    let result = [];
  for (let i = 0; i < source.length; i++) {
  if (find.includes(source.substring(i, i+1))) {
  result.push(i);
    }
     }
     return result;
     }
function mult(ch,n){
  let stri="";
  for(let i=0;i<n;i++){
    stri+=ch;
  }
  return stri;
}
function repeatVowels(str) {
  let v=["a","e","i","o","u"];
  let ind=indices(str.toLowerCase(),v);
  console.log(ind);
  let stri=str.substring(0,ind[1]);
  for(let i=1;i<ind.length;i++){
    let a=mult(str.substring(ind[i],ind[i]+1),i);
    let b=str.substring(ind[i],ind[i+1]);
    stri+=a+b;
  }
  let pre=stri.split("");
  for(let i=0;i<pre.length;i++){
    if(["A","E","I","O","U"].includes(pre[i])){
      pre[i]=pre[i].toLowerCase();
    }
  }
  stri=pre.join("");
  let arr=stri.split("");
  for(let i=0;i<ind.length;i++){
    arr[ind[i]+i*(i+1)*0.5-i]=str[ind[i]];
  }
  let res=arr.join("")
  return res;
                                  }

/* 05-09-2025: IPv4 Validator
Given a string, determine if it is a valid IPv4 Address. A valid IPv4 address consists of four integer numbers separated by dots (.). Each number must satisfy the following conditions:

It is between 0 and 255 inclusive.
It does not have leading zeros (e.g. 0 is allowed, 01 is not).
Only numeric characters are allowed.
*/

function indices(source, find) {
  if (!source) {return [];}    let result = [];
  for (let i = 0; i < source.length; i++) {
  if (source.substring(i, i + find.length) == find) {
  result.push(i);
    }
     }
     return result;
     }

function isValidIPv4(ipv4) {
  let ind=indices(ipv4,".");
  let spl=ipv4.split(".").map((i)=>Number(i));
  let flt=ipv4.split(".").filter((i)=>i!="");
  let lz=ipv4.split(".").filter((i)=>i!="0" && i.substring(0,1)=="0");
  if(ind.length!=3 || flt.length!=4 || lz.length){
    return false;
  } else {
    let ch=spl.filter((i)=>i>=0 && i<256);
    if(ch.length!=4){
      return false;
    }
  }
  return true;
}

/* 06-09-2025: Matrix Rotate
Given a matrix (an array of arrays), rotate the matrix 90 degrees clockwise and return it. For instance, given [[1, 2], [3, 4]], which looks like this:

1	2
3	4
You should return [[3, 1], [4, 2]], which looks like this:

3	1
4	2
*/

function rotate(matrix) {
let mat=matrix[0].map((val, index) => matrix.map(row => row[index]).reverse())
  return mat;
}

/* 07-09-2025: Roman Numeral Parser
Given a string representing a Roman numeral, return its integer value.

Roman numerals consist of the following symbols and values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Numerals are read left to right. If a smaller numeral appears before a larger one, the value is subtracted.
Otherwise, values are added.
*/

function parseRomanNumeral(numeral) {
const values = new Map([
    ['I', 1],
    ['V', 5],
    ['X', 10],
    ['L', 50],
    ['C', 100],
    ['D', 500],
    ['M', 1000]
          ]);
    let result = 0,
        current, previous = 0;
          for (const char of numeral.split("").reverse()) {
current = values.get(char);
if (current >= previous) {result += current; } else {
result -= current;}
previous = current;}
return result;
}

/* 08-09-2025: Acronym Builder
Given a string containing one or more words, return an acronym of the words using the following constraints:

The acronym should consist of the first letter of each word capitalized, unless otherwise noted.
The acronym should ignore the first letter of these words unless they are the first word of the given string: a, for, an, and, by, and of.
The acronym letters should be returned in order they are given.
The acronym should not contain any spaces.
*/

function buildAcronym(str) {
  let s=str.replace("a ","").replace("for ","").replace("an ","").replace("and ","").replace("by ","").replace("of ","");
  let spl=s.split(" ");
  let ac=spl.map((item)=>item.substring(0,1).toUpperCase()).join("");
  return ac;
}

/* 09-09-2025: Unique Characters
Given a string, determine if all the characters in the string are unique.

Uppercase and lowercase letters should be considered different characters.
*/

function allUnique(str) {
let s=Array.from(new Set(str.split("")));

  return str.length==s.length;
}

/* 10-09-2025: Array Diff
Given two arrays with strings values, return a new array containing all the values that appear in only one of the arrays.

The returned array should be sorted in alphabetical order.
*/

function arrayDiff(arr1, arr2) {
  let arr=[];
  for(let i=0;i<arr1.length;i++){
    if(!arr2.includes(arr1[i])){
      arr.push(arr1[i]);
    }
  }
  for(let i=0;i<arr2.length;i++){
    if(!arr1.includes(arr2[i])){
      arr.push(arr2[i]);
    }
  }
  return arr.sort();
}

/* 11-09-2025: Reverse Sentence
Given a string of words, return a new string with the words in reverse order. For example, the first word should be at the end of the returned string, and the last word should be at the beginning of the returned string.

In the given string, words can be separated by one or more spaces.
The returned string should only have one space between words.
*/

function reverseSentence(sentence) {
  let spl=sentence.split(" ").filter((item)=>item!="");
  let res=spl.reverse().join(" ");
  return res;
}

/* 12-09-2025: Screen Time
Given an input array of seven integers, representing a week's time, where each integer is the amount of hours spent on your phone that day, determine if it is too much screen time based on these constraints:

If any single day has 10 hours or more, it's too much.
If the average of any three days in a row is greater than or equal to 8 hours, it’s too much.
If the average of the seven days is greater than or equal to 6 hours, it's too much.
*/

function tooMuchScreenTime(hours) {
  let av=[];
  let h=hours;
  for(let i=0;i<h.length-2;i++){
   av.push(1/3*(h[i]+h[i+1]+h[i+2]));
  }
  let r=h.reduce((a,b)=>a+b,0)/h.length;
  if(h.filter((i)=>i>=10).length>0||av.filter((i)=>i>=8).length>0||r>=6){return true;}
  return false;
}

/* 13-09-2025: Missing Numbers
Given an array of integers from 1 to n, inclusive, return an array of all the missing integers between 1 and n (where n is the largest number in the given array).

The given array may be unsorted and may contain duplicates.
The returned array should be in ascending order.
If no integers are missing, return an empty array.
*/

function findMissingNumbers(arr) {
  let s=Array.from(new Set(arr)).sort((a,b)=>a-b);
  let b1=s[0];
  let b2=s[s.length-1];
  let r=[...Array(b2-b1+1).keys().map((i)=>i+b1)];
  console.log(r);
  let res=[];
  for(let i=0;i<r.length;i++)
  {
    if(!s.includes(r[i])){
      res.push(r[i]);
    }
  } 
    return res;
}

/* 14-09-2025: Word Frequency
Given a paragraph, return an array of the three most frequently occurring words.

Words in the paragraph will be separated by spaces.
Ignore case in the given paragraph. For example, treat Hello and hello as the same word.
Ignore punctuation in the given paragraph. Punctuation consists of commas (,), periods (.), and exclamation points (!).
The returned array should have all lowercase words.
The returned array should be in descending order with the most frequently occurring word first.
*/

function getWords(paragraph) {
  let obj={};
  let p=paragraph.replace(".","").replace(",","").replace("!","");
  let spl=p.split(" ").map((item)=>item.toLowerCase().replace(",",""));
  for(let i=0;i<spl.length;i++){
    if(spl[i] in obj){
      obj[spl[i]]+=1;
    } else {obj[spl[i]]=1;}
  }
  let s = Object.entries(obj).sort((x,y)=>y[1]-x[1]).slice(0,3).map((item)=>item[0]);
  return s;
}

/* 15-09-2025: Thermostat Adjuster
Given the current temperature of a room and a target temperature, return a string indicating how to adjust the room temperature based on these constraints:

Return "heat" if the current temperature is below the target.
Return "cool" if the current temperature is above the target.
Return "hold" if the current temperature is equal to the target.
*/

function adjustThermostat(temp, target) {
  return temp>target?"cool":temp==target?"hold":"heat";
}

/* 16-09-2025: Sentence Capitalizer
Given a paragraph, return a new paragraph where the first letter of each sentence is capitalized.

All other characters should be preserved.
Sentences can end with a period (.), one or more question marks (?), or one or more exclamation points (!).
*/

function capitalize(paragraph) {
  let p=paragraph.split("");
  p[0]=p[0].toUpperCase();
  for(let i=1;i<p.length-1;i++){
    if([".","!","?"].includes(p[i])){
      p[i+1]=p[i+1].toUpperCase();
    }
    if([".","!","?"].includes(p[i]) && p[i+1]==" "){
     p[i+2]=p[i+2].toUpperCase();
    }
  }
  return p.join("");
}
capitalize("hello world. how are you?")

/* 17-09-2025: Slug Generator
Given a string, return a URL-friendly version of the string using the following constraints:

All letters should be lowercase.
All characters that are not letters, numbers, or spaces should be removed.
All spaces should be replaced with the URL-encoded space code %20.
Consecutive spaces should be replaced with a single %20.
The returned string should not have leading or trailing %20.
*/

function generateSlug(str) {
  let low="abcdefghijklmnopqrstuvwxyz".split("");
  let up="ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
  let nums="0123456789".split("");
  let s=str.trim().replace("  "," ").split("");
  for(let i=0;i<s.length;i++){
    if(s[i]==" "){
      s[i]="Y";
    }
    if(!low.includes(s[i])&&!up.includes(s[i])&&!nums.includes(s[i])){
      s[i]="X";
    }
  }
  let flt=s.filter((item)=>item!="X").join("").toLowerCase();
  return flt.replace("y","%20");
}

/* 18-09-2025: Fill The Tank
Given the size of a fuel tank, the current fuel level, and the price per gallon, return the cost to fill the tank all the way.

tankSize is the total capacity of the tank in gallons.
fuelLevel is the current amount of fuel in the tank in gallons.
pricePerGallon is the cost of one gallon of fuel.
The returned value should be rounded to two decimal places in the format: "$d.dd".
*/

function costToFill(tankSize, fuelLevel, pricePerGallon) {
  let d=tankSize-fuelLevel;
  let p="$"+d*pricePerGallon.toString();
  if(!p.split("").includes(".")){
    p+=".00";
  }
  let s=p.split(".");
  if(s[s.length-1].length==1){
    p+="0";
  };
  return p;
}

/* 19-09-2025: Photo Storage
Given a photo size in megabytes (MB), and hard drive capacity in gigabytes (GB), return the number of photos the hard drive can store using the following constraints:

1 gigabyte equals 1000 megabytes.
Return the number of whole photos the drive can store.
*/

function numberOfPhotos(photoSizeMb, hardDriveSizeGb) {

  return Math.floor(hardDriveSizeGb*1000/photoSizeMb);
}

/* 20-09-2025: File Storage
Given a file size, a unit for the file size, and hard drive capacity in gigabytes (GB), return the number of files the hard drive can store using the following constraints:

The unit for the file size can be bytes ("B"), kilobytes ("KB"), or megabytes ("MB").
Return the number of whole files the drive can fit.
Use the following conversions:
Unit	Equivalent
1 B	1 B
1 KB	1000 B
1 MB	1000 KB
1 GB	1000 MB
For example, given 500, "KB", and 1 as arguments, determine how many 500 KB files can fit on a 1 GB hard drive.
*/

function numberOfFiles(fileSize, fileUnit, driveSizeGb) {
  let uObj={"B":1,"KB":1000,"MB":1000000,"GB":1000000000};
  let fS=fileSize*uObj[fileUnit];
  let dS=driveSizeGb*uObj["GB"];
  return Math.floor(dS/fS);
}

/* 21-09-2025: Video Storage
Given a video size, a unit for the video size, a hard drive capacity, and a unit for the hard drive, return the number of videos the hard drive can store using the following constraints:

The unit for the video size can be bytes ("B"), kilobytes ("KB"), megabytes ("MB"), or gigabytes ("GB").
If not given one of the video units above, return "Invalid video unit".
The unit of the hard drive capacity can be gigabytes ("GB") or terabytes ("TB").
If not given one of the hard drive units above, return "Invalid drive unit".
Return the number of whole videos the drive can fit.
Use the following conversions:
Unit	Equivalent
1 B	1 B
1 KB	1000 B
1 MB	1000 KB
1 GB	1000 MB
1 TB	1000 GB
For example, given 500, "MB", 100, and "GB" as arguments, determine how many 500 MB videos can fit on a 100 GB hard drive.
*/

function numberOfVideos(videoSize, videoUnit, driveSize, driveUnit) {
 let uObj={"B":1,"KB":1000,"MB":1000000,"GB":1000000000,"TB":1000000000000};
 let vS=videoSize*uObj[videoUnit];
 let dS=driveSize*uObj[driveUnit];
 if(!["KB","MB","GB"].includes(videoUnit)){
   return "Invalid video unit";
 };
if(!["GB","TB"].includes(driveUnit)){
  return "Invalid drive unit";
}
  return Math.floor(dS/vS);
}

/* 22-09-2025: Digits vs Letters
Given a string, return "digits" if the string has more digits than letters, "letters" if it has more letters than digits, and "tie" if it has the same amount of digits and letters.

Digits consist of 0-9.
Letters consist of a-z in upper or lower case.
Ignore any other characters.
*/

function digitsOrLetters(str) {
  let low="abcdefghojklmnopqrstuvwxyz";
  let up=low.toUpperCase();
  let alph=(low+up).split("");
  let digs="0123456789".split("");
  let c1=0;
  let c2=0;
  let a=str.split("");
  for(let i=0;i<a.length;i++){
    if(alph.includes(a[i])){
      c1+=1;
    } if(digs.includes(a[i])){
      c2+=1;
    }
  }
  return c1>c2?"letters":c1<c2?"digits":"tie";
}

/* 23-09-2025: String Mirror
Given two strings, determine if the second string is a mirror of the first.

A string is considered a mirror if it contains the same letters in reverse order.
Treat uppercase and lowercase letters as distinct.
Ignore all non-alphabetical characters.
*/

function isMirror(str1, str2) {
  let spl1=str1.split(/[" ",-]/).map((item)=>item.replace("!",""));
  let spl2=str2.split(/[" ",-]/).map((item)=>item.replace("!",""));
  let p=[];
  for(let i=spl2.length-1;i>=0;i--){
    p.push(spl2[i].split("").reverse().join(""));
  }
  return p.join(" ")==str1;
}

/* 24-09-2025: Perfect Square
Given an integer, determine if it is a perfect square.

A number is a perfect square if you can multiply an integer by itself to achieve the number. For example, 9 is a perfect square because you can multiply 3 by itself to get it.
*/

function isPerfectSquare(n) {
  let r=Math.sqrt(n);
  let f=Math.floor(r);
  return r==f;
}

/* 25-09-2025: 2nd Largest
Given an array, return the second largest distinct number.
*/

function secondLargest(arr) {
  let s=Array.from(new Set(arr)).sort((a,b)=>a-b);
  console.log(s);
  return s[s.length-2];
}

/* 26-09-2025: Caught Speeding
Given an array of numbers representing the speed at which vehicles were observed traveling, and a number representing the speed limit, return an array with two items, the number of vehicles that were speeding, followed by the average amount beyond the speed limit of those vehicles.

If there were no vehicles speeding, return [0, 0].
*/

function speeding(speeds, limit) {
  let flt=speeds.filter((item)=>item > limit);
  let av=flt.reduce((a,b)=>(a+b)-limit,0)/flt.length;
  if(flt.length>0){
  return [flt.length,av];
  } else {
    return [0,0];
  }
}

/* 27-09-2025: Spam Detector
Given a phone number in the format "+A (BBB) CCC-DDDD", where each letter represents a digit as follows:

A represents the country code and can be any number of digits.
BBB represents the area code and will always be three digits.
CCC and DDDD represent the local number and will always be three and four digits long, respectively.
Determine if it's a spam number based on the following criteria:

The country code is greater than 2 digits long or doesn't begin with a zero (0).
The area code is greater than 900 or less than 200.
The sum of first three digits of the local number appears within last four digits of the local number.
The number has the same digit four or more times in a row (ignoring the formatting characters).
*/

function isSpam(number) {
  let p="123456789".split("");
  let nstr=number.split("").filter((item)=>p.includes(item)).join("");
  for(let i=0;i<p.length;i++)
  {
    let cnt=nstr.split(p[i]).length-1;
    if(cnt>3){
      return true;
    }
  }
  let spl=number.split(" ");
  if(spl[0].slice(0,2)!="+0" || spl[0].length>3){
    return true;
  }
  let ac=spl[1].slice(1,4);
  if(Number(ac)<200 || Number(ac)>900) {
    return true;
  }

  let ln1=spl[2].split("-")[0];
  let ln2=spl[2].split("-")[1];
  let sm=ln1.split("").map((item)=>Number(item)).reduce((a,b)=>a+b,0).toString();
  if(ln2.split("").includes(sm)){
    return true;
  }
  return false;
}
isSpam("+0 (200) 234-0182");

/* 28-09-2025: CSV Header Parser
Given the first line of a comma-separated values (CSV) file, return an array containing the headings.

The first line of a CSV file contains headings separated by commas.
Remove any leading or trailing whitespace from each heading.
*/

function getHeadings(csv) {
  return csv.split(",").map((item)=>item.trim());
}

/* 29-09-2025: Longest Word
Given a sentence, return the longest word in the sentence.

Ignore periods (.) when determining word length.
If multiple words are ties for the longest, return the first one that occurs.
*/

function getLongestWord(sentence) {
  let s=sentence.split(" ").map((item)=>item.replace(".","")).sort((a,b)=>b.length-a.length).slice(0,1);
  return s;
}
getLongestWord("coding is fun")

/* 30-09-2025: Phone Number Formatter
Given a string of ten digits, return the string as a phone number in this format: "+D (DDD) DDD-DDDD".
*/

function formatNumber(number) {
  let n=number;
  let stri="+"+n[0]+" ";
  stri+="("+n.slice(1,4).toString()+") ";
  stri+=n.slice(4,7)+"-";
  stri+=n.slice(7,11).toString();
  return stri;
}
