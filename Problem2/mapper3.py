#!/usr/bin/python

# We want elements file name(relative) and number of hits
# We need to write them out to standard output, separated by a tab

import sys

baseUrl = "http://www.the-associates.co.uk"
endPosition = len(baseUrl)

for line in sys.stdin:
    data = line.strip().split()
    if len(data) == 10:
	ip, userid, username, datetime, timezone, reqtype, resource, protocol, status, objectsize= data
        datetime = datetime[1:]
        timezone = timezone[:-1]
        reqtype = reqtype[1:]
        protocol = protocol[:-1]
	if resource.startswith(baseUrl):
		resource = resource[endPosition:]
		
        print "{0}\t{1}".format(resource, 1)

