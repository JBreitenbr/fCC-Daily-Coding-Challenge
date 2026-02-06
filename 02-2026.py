""" 01-02-2026: Digital Detox
Given an array of your login logs, determine whether you have met your digital detox goal.
Each log is a string in the format "YYYY-MM-DD HH:mm:ss".
You have met your digital detox goal if both of the following statements are true:
• You logged in no more than once within any four-hour period.
• You logged in no more than 2 times on any single day.
"""

from datetime import datetime
def digital_detox(logs):
    s=sorted(logs)
    days=[]
    for i in range(len(s)):
        days.append(s[i][:10])
    for i in range(len(days)):
        c=days.count(days[i])
        if c>2:
            return False
    for i in range(1,len(s)):
        l=datetime(2026,int(s[i-1][5:7]),int(s[i-1][8:10]),int(s[i-1][11:13]),int(s[i-1][14:16]),int(s[i-1][17:19]))
        m=datetime(2026,int(s[i][5:7]),int(s[i][8:10]),int(s[i][11:13]),int(s[i][14:16]),int(s[i][17:19]))
        if int((m-l).total_seconds()) < 4*3600:
            return False
    return True

""" 02-02-2026: Groundhog Day
Today is Groundhog Day, in which a groundhog predicts the weather based on whether or not it sees its shadow.
Given a value representing the groundhog's appearance, return the correct prediction:
• If the given value is the boolean true (the groundhog saw its shadow), return "Looks like we'll have six more weeks of winter.".
• If the value is the boolean false (the groundhog did not see its shadow), return "It's going to be an early spring.".
• If the value is anything else (the groundhog did not show up), return "No prediction this year.". """

def groundhog_day_prediction(app):
    if app==True:
        return "Looks like we'll have six more weeks of winter."
    elif app==False:
        return "It's going to be an early spring."
    else:
        return "No prediction this year."

""" 03-02-2026: String Mirror
Given a string, return a new string that consists of the given string with a reversed copy of itself appended to the end of it. """

def mirror(s):
    return s+s[::-1]

""" 04-02-2026: Truncate the Text
Given a string, return it as-is if it's 20 characters or shorter. If it's longer than 20 characters, truncate it to the first 17 characters and append "..." to the end of it (so it's 20 characters total) and return the result. """

def truncate_text(text):
    if len(text)>20:
        return text[0:17]+"..."
    return text

""" 05-02-2026: Pocket Change
Given an array of integers representing the coins in your pocket, with each integer being the value of a coin in cents, return the total amount in the format "$D.CC".
• 100 cents equals 1 dollar.
• In the return value, include a leading zero for amounts less than one dollar and always exactly two digits for the cents. """

def count_change(change):
    sn=0
    for el in change:
        sn+=el
    sd=str(sn)
    if sn<10:
        return "$0.0"+sd
    elif sn<100:
        return "$0."+sd
    else:
        return "$"+sd[:-2]+"."+sd[-2:]

""" 06-02-2026:2026 Winter Games Day 1: Opening Day
Today marks the start of the 2026 Winter Games. The next 17 days will bring you coding challenges inspired by them.
For the first one, you are given a two-letter country code and need to return the flag emoji for that country. """

def get_flag(code):
       cDict={
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
"UY":"🇺🇾","UZ":"🇺🇿","VE":"🇻🇪"}
        return cDict[code]



