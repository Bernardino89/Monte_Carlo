#!/usr/bin/python

"""
@author: bernardino.tirri@chimieparistech.psl.eu
"""


# the program compute the bond lenght alternation

from sys import argv
import numpy as np
import math 
import  os
import subprocess

NARG=1+2
#----------------------------------------------------------------------
# Required Input file:
# 1) file.xyz
# 2) NAtm : number of atoms 
#----------------------------------------------------------------------

if (len(argv) != NARG) :
  print argv[0],": error in argument number"
  print "USAGE :"
  print argv[0]," <file.xyz (file.xyz format without the first line)> <NAtm>"
  exit(33)


filename = argv[1]       # input geometry filename.xyz  #traj.xyz (standard xyz format)
NAtm = int(argv[2])    # number of atoms


#----------------------------------------------------------------------
#----------------------      FUNCTIONS     -----------------------------
#----------------------------------------------------------------------

# Compute center of mass 


# Dictionary with atomic mass  
atomic_weight = {'H':1.008000, 'He':4.00300, 'Li':6.94100, 'Be':9.01200, \
                 'B':10.81100, 'C':12.01100, 'N':14.00700, 'O':15.99900, \
                 'F':18.99800, 'Ne':20.1800, 'Na':22.9900, 'Mg':24.3050, \
                 'Al':26.9820, 'Si':28.0860, 'P':30.97400, 'S':32.06500, \
                 'Cl':35.4530, 'K':39.09800, 'Ar':39.9480, 'Ca':40.0780, \
                 'Sc':44.9560, 'Ti':47.8670, 'V':50.94200, 'Cr':51.9960, \
                 'Mn':54.9380, 'Fe':55.8450, 'Ni':58.6930, 'Co':58.9330, \
                 'Cu':63.5460, 'Zn':65.3900, 'Ga':69.7230, 'Ge':72.6400, \
                 'As':74.9220, 'Se':78.9600, 'Br':79.9040, 'Kr':83.8000, \
                 'Rb':85.4680, 'Sr':87.6200, 'Y':88.90600, 'Zr':91.2240, \
                 'Nb':92.9060, 'Mo':95.9400, 'Tc':98.0000, 'Ru':101.070, \
                 'Rh':102.906, 'Pd':106.420, 'Ag':107.868, 'Cd':112.411, \
                 'In':114.818, 'Sn':118.710, 'Sb':121.760, 'I':126.9050, \
                 'Te':127.600, 'Xe':131.293, 'Cs':132.906, 'Ba':137.327, \
                 'La':138.906, 'Ce':140.116, 'Pr':140.908, 'Nd':144.240, \
                 'Pm':145.000, 'Sm':150.360, 'Eu':151.964, 'Gd':157.250, \
                 'Tb':158.925, 'Dy':162.500, 'Ho':164.930, 'Er':167.259, \
                 'Tm':168.934, 'Yb':173.040, 'Lu':174.967, 'Hf':178.490, \
                 'Ta':180.948, 'W':183.8400, 'Re':186.207, 'Os':190.230, \
                 'Ir':192.217, 'Pt':195.078, 'Au':196.967, 'Hg':200.590, \
                 'Tl':204.383, 'Pb':207.200, 'Bi':208.980, 'Po':209.000, \
                 'At':210.000, 'Rn':222.000, 'Fr':223.000, 'Ra':226.000, \
                 'Ac':227.000, 'Pa':231.036, 'Th':232.038, 'Np':237.000, \
                 'U':238.0290, 'Am':243.000, 'Pu':244.000, 'Cm':247.000, \
                 'Cf':251.000, 'Es':252.000, 'Fm':257.000, 'Md':258.000, \
                 'No':259.000, 'Rf':261.000, 'Lr':262.000, 'Bh':264.000, \
                 'Sg':266.000, 'Mt':268.000, 'Hs':277.000, }



print '# I m computing the center of mass .... ' 


coordinates = []
x = []
y = []
z = []
masses = []

dimension = []
for i in range(1,NAtm+1,1):
       #print range(0,NAtm-1,1)
       dimension.append(i)
#print dimension


i = 0

with open (filename, "r") as data:
    #for line in range(0,len(dimension)):
    #    print range(0,len(dimension))

    for line in data:
        i +=1
        fragment = line.split()
        if (i >= 0 and i <= len(dimension) ) : 

            print line

            coordinates.append([float(fragment[1]),    # x_coord
                                float(fragment[2]),    # y_coord
                                float(fragment[3])     # z_coord
                               ])
            print coordinates
            element_name = fragment[0].strip()[0:]
            print element_name
            masses.append(atomic_weight[element_name])
            print masses



if len(coordinates) == len(masses):

    # calculate relative weight of every atomic mass
    total_mass = sum(masses)
    weights = [float(atom_mass/total_mass) for atom_mass in masses]
    print 'weight', weights
else:
    print ('# there is something wrong the lists do not have the same lenght')

        

# calculate center of mass
center = [sum([coordinates[i][j] * weights[i]  for i in range(len(weights))]) for j in range(3)]
center_rounded = [round(center[i], 3) for i in range(3)]

print center
print center_rounded




