#!/usr/bin/env python
import pyiface
import subprocess

def get_macvlans():
	a = pyiface.getIfaces()
	return [i for i in a if "mac" in i.name]

def make_macvlan(mac):
	subprocess.check_call("ip","link","add","link","eth0","mac"+str(get_lowestIfaceNum()),"address",mac,"type","macvlan")

def get_lowestIfaceNum():
	#sort list
	ilist = sorted(get_macvlans(), key=lambda iface: int(iface.name[-1:]))
	expectation = 0
	for iface in ilist:
		if iface.name[-1:] != str(expectation):
			return expectation
		else:
			expectation += 1
	return expectation

