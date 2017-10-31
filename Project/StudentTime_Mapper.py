#!/usr/bin/python

#Problem
#Our students come from all around the world, so we need to know both at what times of day the activity is the highest, and to know which of the students are active at that time.
#In this exercise your task is to find for each student what is the hour during which the student has posted the most posts

import sys
import datetime
i=0
for line in sys.stdin:
    if i==0:
	i = i+1
	continue
    data = line.strip().split("\t")
    if len(data) == 19:
        authorid = data[3]
	dateadded = data[8]
	timeadded = dateadded.split()[1]
	ind = timeadded.index(":")
	houradded = timeadded[:ind]
        print "{0}\t{1}".format(authorid,houradded)

