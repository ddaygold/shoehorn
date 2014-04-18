#!/usr/bin/env python2
import pyiface
import subprocess
import redis
import argparse

def get_macvlans():
	a = pyiface.getIfaces()
	return [i for i in a if "mac" in i.name]

def make_macvlan(mac):
	name = "mac"+str(get_lowestIfaceNum())
	subprocess.check_call(["ip","link","add","link","eth0",name,"address",mac,"type","macvlan"])
	subprocess.check_call(["ifconfig",name,"up"])
	subprocess.check_call(["dhclient",name])

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

def make_interface(num=1):
	r = redis.StrictRedis(host='localhost', db=1)
	for i in range(num):
		mac = r.srandmember("MACS")
		make_macvlan(mac)

def make_ifacesUpTo(num=0):
	r = redis.StrictRedis(host='localhost', db=1)
	while len(get_macvlans()) < num:
		mac = r.srandmember("MACS")
		make_macvlan(mac)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n","--number",default=0)
    args = parser.parse_args()
    make_ifacesUpTo(int(args.number))

if __name__ == "__main__":
    main()
