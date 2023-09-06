#! /usr/bin/env python

"""
@author: bernardino.tirri@chimieparistech.psl.eu
"""

# Remember, the program must be initialized within the folder where you want to process the files.
# In the folder, there should only be the file to be analyzed.
# The program determines the alternation in bond length and calculates the average based on the file number.
# argv 1 --> Atom position such as C24 = 24 + 7; 7 because the program reads the file from the first row.
# argv 2 --> Atom position such as C25 = 25 + 7; 7 because the program reads the file from the first row.
# argv 3 --> Atom position such as C26 = 26 + 7; 7 because the program reads the file from the first row.
# argv 4 --> Atom position such as C27 = 27 + 7; 7 because the program reads the file from the first row.
# Usage: bla_mc.py 24 25 26 27



from sys import *
from math import pi,sqrt,exp,log
import os, string
from operator import itemgetter
import shutil
import os.path
import numpy as np
import sys


# read all files .out

narg= 1 + 0

A= int(sys.argv[1])
B= int(sys.argv[2])
C= int(sys.argv[3])
D= int(sys.argv[4])

# generate the full path for the current directory
full_path = os.path.realpath(__file__)
print (full_path)

path, filename = os.path.split(full_path)
print(path + ' --> ' + filename + "\n")

files = []

for i in os.listdir(path):
    if i.endswith(".com"):
        files.append(i)
print "the file are equal" ,files
average = len(files)
print "the file number is", average
X1=[]
Y1=[]
Z1=[]
X2=[]
Y2=[]
Z2=[]

for k in files :

    input=open(k,"r")	
  	linee=input.readlines()
	for n, raw in enumerate(linee) :
            if n == A:
                atom1=raw.split()
                x1=float(atom1[1].split()[0])
                y1=float(atom1[2].split()[0])
                z1=float(atom1[3].split()[0])
                X1.append(x1)
                Y1.append(y1)
                Z1.append(z1)
                print raw

            if n == B:

                atom2=raw.split()
                x2=float(atom2[1].split()[0])
                y2=float(atom2[2].split()[0])
                z2=float(atom2[3].split()[0])
                X2.append(x2)
                Y2.append(y2)
                Z2.append(z2)
#print "the X1 coordibnates are:", X1
B1=[(np.sqrt(((x2-x1)**2) + ((y2-y1)**2) + ((z2-z1)**2))) for x1,x2, y1,y2, z1, z2 in zip(X1, X2,Y1, Y2, Z1, Z2)]
                        
                            
print " the first bond lenght is",B1

########################## second Bond ##########################################################

X3=[]
Y3=[]
Z3=[]
X4=[]
Y4=[]
Z4=[]
for k in files :

        input=open(k,"r")	
  	linee=input.readlines()
	for n, raw in enumerate(linee) :
            if n == C:
                atom3=raw.split()
                x3=float(atom3[1].split()[0])
                y3=float(atom3[2].split()[0])
                z3=float(atom3[3].split()[0])
                X3.append(x3)
                Y3.append(y3)
                Z3.append(z3)
#                print raw

            if n == D:

                atom4=raw.split()
                x4=float(atom4[1].split()[0])
                y4=float(atom4[2].split()[0])
                z4=float(atom4[3].split()[0])
                X4.append(x4)
                Y4.append(y4)
                Z4.append(z4)
#                print raw


B2=[(np.sqrt(((x2-x1)**2) + ((y2-y1)**2) + ((z2-z1)**2))) for x1,x2, y1,y2, z1, z2 in zip(X3, X4,Y3, Y4, Z3, Z4)]
print " the second bond lenght is", B2

########################## Bond Lenght Alternation #################################

BLA=[ abs(G - g) for G, g in zip(B1, B2)]


print "The BLA is",BLA

sum = 0
for element in BLA:
    sum += abs(element)/average
print("the average value is",sum)

