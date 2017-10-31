#!/usr/bin/python

import sys

quesLen = 0
ansLength = 0
ansCount = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the node id, val is the post_type and length of post

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisLen = data_mapped
    postType, postLen = thisLen.split("-")
    if oldKey and oldKey != thisKey:
		if ansCount==0:
			print oldKey, "\t", quesLen, "\t", ansCount
		else:	
			print oldKey,"\t", quesLen, "\t", float(ansLength/ansCount)  
       		oldKey = thisKey
		ansLength = 0
		ansCount = 0
		quesLen = 0

    oldKey = thisKey
    if postType == "question":
	quesLen = postLen
    elif postType == "answer":
    	ansLength += int(postLen)
	ansCount +=1

if oldKey != None:
	print oldKey, "\t", quesLen, "\t", float(ansLength/ansCount)

