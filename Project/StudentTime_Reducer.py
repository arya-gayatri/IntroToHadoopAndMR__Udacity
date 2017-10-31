#!/usr/bin/python

import sys

hoursCount = [0]*24
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the author name, val is the hour of post

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHour = data_mapped
    if oldKey and oldKey != thisKey:
		maxCount = 0
		maxHour = 0
		for i in range(0,len(hoursCount)):
			if hoursCount[i]>maxCount:
				maxCount = hoursCount[i]
				maxHour = i	
		print oldKey,"\t", maxHour 
       		oldKey = thisKey
		hoursCount = [0]*24

    oldKey = thisKey
    hoursCount[int(thisHour)] += 1

if oldKey != None:
	for hour, count in enumerate(hoursCount):
		if count==max(hoursCount):
			print oldKey,"\t",hour

