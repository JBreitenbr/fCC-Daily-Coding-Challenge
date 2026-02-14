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

""" 07-02-2026: 2026 Winter Games Day 2: Snowboarding
Given a snowboarder's starting stance and a rotation in degrees, determine their landing stance.
• A snowboarder's stance is either "Regular" or "Goofy".
• Trick rotations are multiples of 90 degrees. Positive indicates clockwise rotation, and negative indicate counter-clockwise rotation.
• The landing stance flips every 180 degrees of rotation.
For example, given "Regular" and 90, return "Regular". Given "Regular" and 180 degrees, return "Goofy". """

import math
def get_landing_stance(start_stance, rotation):
    if rotation>0:
        t=math.floor(rotation/180)
    else:
        t=math.ceil(rotation/180)
    opp={"Goofy":"Regular","Regular":"Goofy"}
    if t%2==0:
        return start_stance
    else:
        return opp[start_stance]

""" 08-02-2026: 2026 Winter Games Day 3: Biathlon
Given an array of integers, where each value represents the number of targets hit in a single round of a biathlon, return the total penalty distance the athlete must ski.
• Each round consists of 5 targets.
• Each missed target results in a 150 meter penalty loop. """

def calculate_penalty_distance(rounds):
    sn=0
    for el in rounds:
        sn+=(5-el)*150
    return sn

""" 09-02-2026: 2026 Winter Games Day 4: Ski Jumping
Given distance points, style points, a wind compensation value, and K-point bonus value, calculate your score for the ski jump and determine if you won a medal or not.
• Your score is calculated by summing the above four values.
The current total scores of the other jumpers are:
165.5 172.0 158.0 180.0 169.5 175.0 162.0 170.0 
• If your score is the best, return "Gold"
• If it's second best, return "Silver"
• If it's third best, return "Bronze"
• Otherwise, return "No Medal" """

def ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus):
    lst=[165.5,172.0,158.0,180.0,169.5,174.0,162.0,170.0]
    sn=distance_points+style_points+wind_comp+k_point_bonus
    lst.append(sn)
    s=sorted(lst)
    if sn==s[-3]:
        return "Bronze"
    elif sn==s[-2]:
        return "Silver"
    elif sn==s[-1]:
        return "Gold"
    return "No Medal"

""" 10-02-2026: 2026 Winter Games Day 5: Cross-Country Skiing
Given an array of finish times for a cross-country ski race, convert them into times behind the winner.
• Given times are strings in "H:MM:SS" format.
• Given times will be in order from fastest to slowest.
• The winners time (fastest time) should correspond to "0".
• Each other time should show the time behind the winner, in the format "+M:SS".
For example, given ["1:25:32", "1:26:10", "1:27:05"], return ["0", "+0:38", "+1:33"]. """

def convert(sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    mini = sec // 60
    sec %= 60  
    m=str(mini)
    if sec<10:
       s="0"+str(sec)
    else:
        s=str(sec) 
    return "+"+m+":"+s

def get_relative_results(res):
    m=[]
    for i in range(len(res)):
        sp=res[i].split(":")
        m.append(int(sp[0])*3600+int(sp[1])*60+int(sp[2]))
    d=["0"]
    for i in range(1,len(res)):
        d.append(convert(m[i]-m[0]))
    return d
    
 """ 11-02-2026: 2026 Winter Games Day 6: Figure Skating
Given an array of judge scores and optional penalties, calculate the final score for a figure skating routine.
The first argument is an array of 10 judge scores, each a number from 0 to 10. Remove the highest and lowest judge scores and sum the remaining 8 scores to get the base score.
Any additional arguments passed to the function are penalties. Subtract all penalties from the base score to get the final score. """

def compute_score(judge_scores, *penalties):
    s=sorted(judge_scores)[1:-1]
    sn=0
    for i in range(len(s)):
        sn+=s[i]
    p=list(penalties)
    if len(p)>0:
        for i in range(len(p)):
            sn-=p[i]
    return sn

""" 12-02-2026: 2026 Winter Games Day 7: Speed Skating
Given two arrays representing the lap times (in seconds) for two speed skaters, return the lap number where the difference in lap times is the largest.
The first element of each array corresponds to lap 1, the second to lap 2, and so on. """

def largest_difference(sk1, sk2):
    lst=[]
    for i in range(len(sk1)):
        lst.append(abs(sk2[i]-sk1[i]))
    maxi=(sorted(lst))[-1]
    s=lst.copy()
    for i in range(len(s)):
        if abs(s[i]-maxi)<0.01:
            return i+1

""" 13-02-2026:  2026 Winter Games Day 8: Luge
Given an array of five numbers, each representing the time (in seconds) it took a luger to complete a segment of a track, determine which segment had the fastest speed and what that speed was.
The track is divided into the following segments:
• Segment 1: 320 meters
• Segment 2: 280 meters
• Segment 3: 350 meters
• Segment 4: 300 meters
• Segment 5: 250 meters
The first value in the given array corresponds to the time for segment 1, the second value to segment 2, and so on.
To calculate the speed (in meters per second) for a segment, divide the distance by the time.
Return "The luger's fastest speed was X m/s on segment Y.". Where X is the fastest speed, rounded to two decimal places, and Y is the segment number where the fastest speed occurred. """

def get_fastest_speed(times):
    l=[320,280,350,300,250]
    maxi=round(l[0]/times[0],2)
    ind=1
    for i in range(len(l)):
        v=l[i]/times[i]
        if v>maxi:
            maxi=round(v,2)
            ind=i+1
    return f"The luger's fastest speed was {maxi} m/s on segment {ind}."

""" 14-02-2026: 2026 Winter Games Day 9: Skeleton
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
"""

def get_difficulty(track):
    if track[0]!="S":
        sn=5
    else:
        sn=0
    for i in range(1,len(track)):
        if track[i-1]=="R" and track[i]=="L" or track[i-1]=="L" and track[i]=="R":
            sn+=15
        elif track[i]!="S":
            sn+=5
    if sn<=100:
        return "Easy"
    elif sn<=200:
        return "Medium"
    else:
        return "Hard"

