#!/usr/bin/python

import sys

hitsTotal = 0
oldKey = None
maxhits = 0
maxhitsurl = None

# Loop around the data
# It will be in the format key\tval
# Where key is the file name, val is the number of hits
#
# All the sales for a particular file will be presented,
# then the key will change and we'll be dealing with the next file
# We find file with the maximum hits

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisHits = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", hitsTotal
	if maxhitsurl==None or hitsTotal>maxhits:
		maxhits = hitsTotal
		maxhitsurl = thisKey
        oldKey = thisKey;
        hitsTotal = 0

    oldKey = thisKey
    hitsTotal += int(thisHits)

if oldKey != None:
    print oldKey, "\t", hitsTotal

print "maxhits=", maxhits
print "maxhitsurl=", maxhitsurl
