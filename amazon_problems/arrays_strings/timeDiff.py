Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list. 
Example 1:
Input: ["23:59","00:00"]
Output: 1

1. 1.	The number of time points in the given list is at least 2
2. 2.	The input time is legal and ranges from 00:00 to 23:59

["23:59","23:50", "09:10", "09:05"]
output : 5

["23:59","23:50", "09:10", "09:05", "00:00"]

["00:00", "00:00","00:03", "09:10", "09:05","23:50", "23:59", "24:00" ]
output: 1

["01:59","13:50", "23:10"]

def minimumTimeDiff(timeList):
    # Sort the input list
    timeList.sort()
    return calcDiff(timeList)

def calcDiff(timeList):
    minimumDiff = float('inf')
    # get the len of the list
    lenList = len(timeList)
    for index, time in enumerate(timeList):
        #fetch current hour and minutes
        hours = int(time.split(':'))[0]
        minutes = int(time.split(':'))[1]
        
        #fetch next hour and minutes in sorted list
        nextHour = int(timeList[index+1].split(':'))[0]
        nextMinute = int(timeList[index+1].split(':'))[1]
        
        diffHour = nextHour - hours
        diffMin = nextMinute - minutes
        
        #Convert the diff to minutes
        resMinutes = diffHour * 60 + diffMin
        
        if minimumDiff > resMinutes:
            minimumDiff = resMinutes
        
        #Early break for minimum viable difference
        if minimumDiff == 0:
            return minimumDiff
    
    #handling the edge case
    hours = int(timeList[0].split(':'))[0]
    minutes = int(timeList[0].split(':'))[1]
    
    if hours == 0:
        nextHour = int(timeList[lenList-1].split(':'))[0]
        hours = nextHour
        nextMinute = int(timeList[lenList-1].split(':'))[1]
        
        diffHour = nextHour - hours
        diffMin = nextMinute - minutes
        
        #Convert the diff to minutes
        resMinutes = diffHour * 60 + diffMin
        
        if minimumDiff > resMinutes:
            minimumDiff = resMinutes
        
    return minimumDiff