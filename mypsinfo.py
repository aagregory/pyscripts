#!/usr/bin/env python3

import subprocess

mycmd = 'ps -ef'
myproc = subprocess.Popen(mycmd, shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

myout = myproc.stdout

for myline in myout:
    if 'gregory' in myline:
        print(myline.strip())
