# -*- coding: utf-8 -*-
# Calvin Chen

#Ho_Lee model
#Binomial Tree

import sys
import math
import string

if __name__ == '__main__':
	#read input
	fp  = open('input.txt', 'r')
	x 	= fp.readline()
	y 	= fp.readline()
	E	= fp.readline()
	F 	= fp.readline()
	G	= fp.readline()
	v	= fp.readline()
	n	= fp.readline()
	X	= fp.readline()	  
	fp.close()
	x = string.atof(x)
	y = string.atof(y)
	E = string.atof(E)
	F = string.atof(F)
	G = string.atof(G)
	v = v.replace("%","")
	
	sigma = string.atof(v)/100.0
	n = string.atof(n)
	X = X.replace("%","")
	X = string.atof(X)/100.0
	n = n/y
	vol_period = 2.0*sigma/(n**0.5)
#	print vol_period
	P = []
	temp = []
	temp2 = []
	
	P = [[[0 for x in range(int(n)+1)] for y in range(int(n*y/x)+1)] for z in range(int(n*y/x)+1)]
	for i in range(1,int(n*y/x)+1):
		P[0][i][0] = 1.0/math.exp((E - F*math.exp(-G*i/n))*i/n)

	for k in range(1,int(n)+1):
		for i in range(0,k):
			for j in range(k+1,int(n*y/x)+1):
				expo = math.exp(vol_period*(j-k)/n)
				down = 2.0*expo / (1.0+expo)
				up = 2.0 - down
				P_divide = P[k-1][j][i]/P[k-1][k][i]
				P[k][j][i] = P_divide * down
#				print P[k][j][i]
				P[k][j][i+1] = P_divide * up;
	Call = []
	temp3 = []
	for i in range(0,int(n)+1):
		temp3.append(0.0)
	for i in range(0,int(n)+1):
		Call.append(temp3)	
	for i in range(0,int(n)+1):
		if(P[int(n)][int(n*y/x)][i] >= X):
			Call[int(n)][i] = P[int(n)][int(n*y/x)][i] - X
		else:
			Call[int(n)][i] = 0.0
			
	for i in range(int(n)-1,-1,-1):
		for j in range(0,i+1):
			Call[i][j] = (Call[i+1][j]+Call[i+1][j+1])*P[i][i+1][j]/2.0
	
	Call[0][0] = Call[0][0]*100.0
	print "Call  = %04.4f" % Call[0][0]