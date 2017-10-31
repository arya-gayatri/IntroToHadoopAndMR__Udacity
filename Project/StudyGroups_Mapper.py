#!/usr/bin/python

# Problem
#Write a mapreduce program that for each forum thread (that is a question node with all it's answers and comments) would give us a list of students that have posted there - either asked the question, answered a question or added a comment.

import sys
import datetime
i=0
for line in sys.stdin:
    if i==0:
	i = i+1
	continue
    data = line.strip().split("\t")
    if len(data) == 19:
        qid = data[0]
	studentId = data[3]
        print "{0}\t{1}".format(qid,studentId)

