#!/usr/bin/python

import os
import sys 
import re
from cmd_color_printers import *  


def addKeyWork(line,outfile):
    if "Starts to dump Bugreport" in line:
        outfile.write("<perflogkeyword>xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n\n")
    else :
        outfile.write("<perflogkeyword>==========================================================\n\n")

def parseKeyWorld(keywordpath="./keyword.txt"):
    try:
        keywordfile=open(keywordpath,"r")
        strArray =[] 
        for line in keywordfile:
            strArray.append(line.strip())
        return strArray
    finally:
        keywordfile.close()

inpath = sys.argv[1].strip()


outpath =""

if len(sys.argv)>2:
    outpath = sys.argv[2].strip()
keywordpath =""

if len(sys.argv)>3:
    keywordpath = sys.argv[3].strip()

if not outpath.strip():
    outpath = "./perfresult.txt"

if not keywordpath.strip():
    keywordpath = "/home/mi/bin/perfkeyword.txt"

logfile = open(inpath,'r')
outfile = open(outpath,"w")
print keywordpath
keywords = parseKeyWorld(keywordpath)

for line in logfile:
    for keyword in keywords:
        if keyword in line:
            addKeyWork(line,outfile)
    outfile.write(line)
            
logfile.close()
logfile.close()
