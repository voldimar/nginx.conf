#!/usr/bin/env python

import jinja2

accname = {}
index = 0
for line in open("sources/domains.list").readlines():
	s = line.split()
	print s
	if s[0][0] == "#":
		continue
	acc = {}
	acc["accname"], acc["basedir"], acc["name"] = s[0],s[1],s[2]
	accname[index]= acc
	index+=1

for line in open("sources/suspend.list").readlines():
	s = line.split()
	if s[0][0] == "#":
		continue
	for item in accname:
		if accname[item]["name"] == s[0]:
			accname[item]["suspend"] = True
			accname[item]["locale"] = s[1]

for line in open("sources/ddos.list").readlines():
	s = line.split()
	
	if s[0][0] == "#":
		continue
	for item in accname:
		if accname[item]["name"] == s[0]:
			accname[item]["ddos"] = True



template = jinja2.Template(open("nginx.conf").read())
for item in accname:
	print item
	with open("output/"+accname[item]["name"]+".conf","wb") as f:
		f.write(template.render(accname=accname[item]))

