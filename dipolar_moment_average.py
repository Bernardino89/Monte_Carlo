#! /usr/bin/env python2


"""
@author: bernardino.tirri@chimieparistech.psl.eu
"""
# The program compute the dipolar moment average

from sys import *
from collections import Counter

narg=0+1

filename=argv[1:]

# read the command line
if (len(argv) < narg) :
  print("Error in argument number")
  print("USAGE")
  print(argv[0]+"<g09_1.out> <g09_2.out> .... <g09_N.out>") 
  quit() 

dip=[]
count = 0
for file in filename :

  input=open(file,"r")	
  linee=input.readlines()
  
  dipol=0.0
#  for row in linee :
  for i in range(0, len(linee)):
       line = linee[i]
 #       print line
 #       if line[:5] == "anim ":
 #           ne = lines[i + 1] # you may want to check that i < len(lines)
 #           print ' ne ',ne,'\n'   
       if(line.find(" Dipole moment (field-independent basis, Debye):") != -1) : ####################
      
            ne = linee[i + 1] # you may want to check that i < len(lines)
            comment=ne.split()
            dipol=float(comment[7])        ######################################################
            print file,comment,"===>>",dipol          #####################################################
    
    

  dip.append(dipol)
    
  input.close()


for i in dip:
  a=dip.count(i)
  print i, a


print " Dipol moment average ====>> ", sum(dip)/len(dip)

