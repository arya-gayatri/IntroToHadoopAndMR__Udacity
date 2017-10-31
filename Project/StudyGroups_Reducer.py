#!/usr/bin/python

import sys

oldKey = None
studentList = []

# Loop around the data
# It will be in the format key\tval
# Where key is the post id, val is the list of students active on that post

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisId = data_mapped
    if oldKey and oldKey != thisKey:
		print oldKey,"\t",studentList  
       		oldKey = thisKey
		studentList = []

    oldKey = thisKey
    studentList.append(thisId)

if oldKey != None:
	print oldKey,"\t",studentList

