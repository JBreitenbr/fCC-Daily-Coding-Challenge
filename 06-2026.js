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

