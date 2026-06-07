""" 01-06-2026: Schema Validator Part 1
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
json
{
  username: string
}

• Extra keys are allowed """

def is_valid_schema(obj):
    k=list(obj.keys())
    if not "username" in k:
       return False
    ind=k.index("username")
    return isinstance(obj[k[ind]],str)

""" 02-06-2026: Schema Validator Part 2
Given an object (JavaScript) or dictionary (Python), determine if it matches the following schema:
json
{
  username: string,
  posts: number,
  verified: boolean
}

• Extra keys are allowed """

def is_valid_schema(obj):
    k=list(obj.keys())
    if not "username" in k or not "posts" in k or not "verified" in k:
        return False
    ind1=k.index("username")
    c1=isinstance(obj[k[ind1]],str)
    ind2=k.index("posts")
    c2=isinstance(obj[k[ind2]],int)
    ind3=k.index("verified")
    c3=isinstance (obj[k[ind3]], bool)
    return c1 and c2 and c3

""" 03-06-2026: Schema Validator Part 3
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
• Extra keys are allowed """

def is_valid_schema(obj):
    roles=["user","creator","moderator","staff","admin"]
    k=list(obj.keys())
    if not "username" in k or not "posts" in k or not "verified" in k or not "role" in k:
        return False
    ind1=k.index("username")
    c1=isinstance(obj[k[ind1]],str)
    ind2=k.index("posts")
    c2=isinstance(obj[k[ind2]],int)
    ind3=k.index("verified")
    c3=isinstance (obj[k[ind3]], bool)
    return c1 and c2 and c3 an

""" 04-06-2026: Schema Validator Part 4
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
• Extra keys are allowed """

def is_valid_schema(obj):
    roles=["user","creator","moderator","staff","admin"]
    k=list(obj.keys())
    if not "username" in k or not "posts" in k or not "verified" in k or not "role" in k:
        return False
    ind1=k.index("username")
    c1=isinstance(obj[k[ind1]],str)
    ind2=k.index("posts")
    c2=isinstance(obj[k[ind2]],int) and not isinstance(obj[k[ind2]],bool)
    ind3=k.index("verified")
    c3=isinstance (obj[k[ind3]], bool)
    if not "supporter" in k:
       return c1 and c2 and c3 and obj["role"] in roles
    else: 
       return c1 and c2 and c3 and obj["role"] in roles and isinstance(obj[k[k.index("supporter")]],bool)


""" 05-06-2026: Schema Validator Part 5
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
• Extra keys are allowed  """

def is_valid_schema(obj):
    roles=["user","creator","moderator","staff","admin"]
    k=list(obj.keys())
    if not "username" in k or not "posts" in k or not "verified" in k or not "role" in k or not "badges" in k:
        return False
    ind1=k.index("username")
    c1=isinstance(obj[k[ind1]],str)
    ind2=k.index("posts")
    c2=isinstance(obj[k[ind2]],int) and not isinstance(obj[k[ind2]],bool)
    ind3=k.index("verified")
    c3=isinstance(obj[k[ind3]], bool)
    if "supporter" in k:
        ind4=k.index("supporter")
        c4=isinstance(obj[k[ind4]],bool)
    for i in range(len(obj["badges"])):
        if not isinstance(obj["badges"][i],str):
            return False
    if "supporter" in k:
        return c1 and c2 and c3 and c4 and obj["role"] in roles
    else:
        return c1 and c2 and c3 and obj["role"] in roles          

""" 06-06-2026: Schema Validator Part 6
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
• Extra keys are allowed """

def check_obj(obj):
    roles=["user","creator","moderator","staff","admin"]
    k=list(obj.keys())
    if not "username" in k or not "posts" in k or not "verified" in k or not "role" in k or not "badges" in k:
         return False
    ind1=k.index("username")
    c1=isinstance(obj[k[ind1]],str)
    ind2=k.index("posts")
    c2=isinstance(obj[k[ind2]],int) and not isinstance(obj[k[ind2]],bool)
    ind3=k.index("verified")
    c3=isinstance(obj[k[ind3]], bool)
    if "supporter" in k:
        ind4=k.index("supporter")
        c4=isinstance(obj[k[ind4]],bool)
    for i in range(len(obj["badges"])):
        if not isinstance(obj["badges"][i],str):
            return False
    if "supporter" in k:
        return c1 and c2 and c3 and c4 and obj["role"] in roles
    else:
        return c1 and c2 and c3 and obj["role"] in roles

def is_valid_schema(obj):
    if not isinstance(obj["users"],list):
       return False
    elif obj["users"]==[]:
       return True
    else:
       for i in range(len(obj["users"])):
        if not check_obj(obj["users"][i]):
            return False
    return True

""" 07-06-2026: Last Load
Given the number of scoops of laundry detergent you have remaining and an array of how many scoops you used in each of the previous days, return the number of full days of detergent you have remaining.
Calculate your average daily usage from the usage history and assume that amount of usage each day going forward. """

import math
def last_load_date(scoops, usage):
    return math.floor(scoops/(sum(usage)/len(usage)))
