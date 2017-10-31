#!/usr/bin/python

#Problem
#Write a mapreduce program that would process the forum_node data and output the length of the post and the average answer (just answer, not comment) length for each post.

import sys
import datetime
i=0
for line in sys.stdin:
    if i==0:
	i = i+1
	continue
    data = line.strip().split("\t")
    if len(data) == 19:
        nodeid = data[0]
	post = data[4]
	postType = data[5]
        print "{0}\t{1}".format(nodeid,postType+"-"+str(len(post)))

