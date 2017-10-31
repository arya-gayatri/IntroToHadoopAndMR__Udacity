#!/usr/bin/python

import sys

tagCount = 0
oldKey = None
tagMap = {}

# Loop around the data
# It will be in the format key\tval
# Where key is the tag, val is the number of times tag comes

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisCount = data_mapped
    if oldKey and oldKey != thisKey:
		tagMap[oldKey] = tagCount  
       		oldKey = thisKey
		tagCount = 0

    oldKey = thisKey
    tagCount +=int(thisCount)

if oldKey != None:
	tagMap[oldKey]=tagCount

i=0

for key, value in sorted(tagMap.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    if i<10:
    	print key,"\t",value
	i +=1

