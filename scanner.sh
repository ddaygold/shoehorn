#!/bin/bash
#Simple script to search for all the MACS on the LAN, then filter the output
#to just the MACS
sudo nmap -sP -n 198.37.25.210/23 | grep MAC | cut -b14-30 | ./inserter.py
