#! /usr/bin/env python

"""
@author: bernardino.tirri@chimieparistech.psl.eu
"""

# The program compute the SCF distribution


from sys import *
from math import pi,sqrt,exp,log
import os, string
from operator import itemgetter
import shutil
import os.path

narg=1+0                     # number of argv
kb=8.617e-5                  # eV K**-1
T=300.0                      # temperature
cutoff=0.36787944117         # factor 1/e
Ha_eV = 27.2107              # conversion factor from Ha to eV


# read all files .out
if (len(argv) <= narg) :
  print("Error in argument number")
  print("USAGE")
  print(argv[0]+" <g09_1.out> <g09_2.out> .... <g09_N.out>") 
  quit() 

filename=argv[1:]




SCF_Done=[]
SCF=[]

difference = []
start = 0.0
difference.append(start)

for file in filename :

	input=open(file,"r")	
  	linee=input.readlines()
	for row in linee :

  		if (row.find("SCF Done") != -1) :
			
			energy=row.split("=")
			E0=float(energy[1].split()[0])
#			print 'SCF Done',E0
			SCF.append(E0)
			SCF_num = map (float,SCF)
			SCF_min = min (SCF_num)
#			print 'the minimum SCF value found is', SCF_min

			for i in range(1,len(SCF)):
				diff = (SCF [i] - SCF_min)*Ha_eV
				difference.append(diff)
#print 'SCF difference', difference



#########################################################################################

#                               BOLTZMANN DISTRIBUTION                                  #

boltz=[ exp( - ((k-SCF_min)*Ha_eV)/(kb*T)) for k in SCF]
distrib = []
distrib.append (boltz)

print 'boltzman distribution is \n', distrib


#########################################################################################


# generation list of lists


value = 1

my_list = [filename, SCF, boltz]
new_list = []
new_list.append(my_list)

a = 1. - cutoff

list1 = []
list2 = []
list3 = []
list4 = []
le= len(my_list[2])

for i,j in zip(filename, boltz):
#	print i,j

	if j >  a or j == a:
		list2.append(i)
		list1.append(j)
	
	elif j < a : 
		list4.append(i)
		list3.append(j)
	
elite_list = [list2,list1]
trash_list = [list4, list3]

#print 'the elite list is ', elite_list
#print 'the trash list is', trash_list

dirName = 'elite_configuration'
 
try:
    # Create target Directory
    os.mkdir(dirName)
    print 'Directory'  , dirName ,  ' Created ' 
except FileExistsError:
    print("Directory " , dirName ,  " already exists, rm -rf the", dirName, "and run again the script")

# generate the full path for the current directory
full_path = os.path.realpath(__file__)

#print("This file directory and name of the python script")
path, filename = os.path.split(full_path)
#print(path + ' --> ' + filename + "\n")

#print("This file directory only")
#print(os.path.dirname(full_path))


#for i in list2:
#	if i == filename:
#		print i, filename
#	shutil.copyfile(filename, 'elite_configuration')

cur_dir = os.getcwd() # Dir from where search starts can be replaced with any path
#print 'my current directory is', cur_dir

#########################################################################################################

PATH0=[]
PATH0.append(cur_dir+'/'+dirName)


src_files = os.listdir(cur_dir)
#print 'these are the file in the folder ',src_files 
for filename in src_files:
#	print filename
	for i in list2:
#		print i
		if filename == i:
#        		print 'File Exists in: ', cur_dir
			shutil.copy(filename , cur_dir+'/'+dirName)
			break
    		else:
			if i != filename: 			#if dir is root dir
#				print "File not found"
          			break
			else:
				cur_dir = parent_dir






