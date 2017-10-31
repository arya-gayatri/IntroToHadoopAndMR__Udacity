#!/usr/bin/python

# Problem
#Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.

import sys
import datetime
i=0
for line in sys.stdin:
    if i==0:
	i = i+1
	continue
    data = line.strip().split("\t")
    if len(data) == 19:
        tag = data[2]
	tagList = tag.split()
	for t in tagList:
        	print "{0}\t{1}".format(t.lower(),1)

