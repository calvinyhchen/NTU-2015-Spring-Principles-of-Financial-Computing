import sys
import math
import string

def Amax(j, i, S, u, d):
	return ( S * ( ( ( 1 - u**(j-i+1) ) / ( 1 - u ) ) + u**(j-i) * d * ( ( 1 - d**i ) / ( 1 - d ) ) ) / (j+1) )

def Amin(j, i, S, u, d):
	return ( S * ( (( 1 - d**(i+1) ) / ( 1 - d )) + ( d**i * u * ( ( 1 - u**(j-i) ) / ( 1 - u ) ) ) ) / (j+1) )

if __name__ == '__main__':
	#read input
	fp  = open('input.txt', 'r')
	S 	= fp.readline()
	X 	= fp.readline()
	H	= fp.readline()
	t 	= fp.readline()
	v	= fp.readline()
	r	= fp.readline()
	n	= fp.readline()
	k	= fp.readline()	  
	fp.close()
	S = string.atof(S)
	X = string.atof(X)
	H = string.atof(H)
	v = v.replace("%","")
	v = string.atof(v)/100
	r = r.replace("%","")
	r = string.atof(r)/100
	k = string.atof(k)
	n = string.atof(n)
	t = string.atof(t)
	R = math.exp(r*(t/n))
	u = math.exp(v*((t/n)**(0.5)))
	d = 1.0/u
	q = (R-d)/(u-d)
	
	A = [[0 for x in range(int(k)+1)] for y in range(int(n)+1)] 	#A[n+1][k+1]
	C = [[0 for x in range(int(k)+1)] for y in range(int(n)+1)] 	#C[n+1][k+1]
	T = [0 for x in range(int(k)+1)]								#Temp_C[k]	
	
	for i in range(0,int(n)+1):
		min = Amin(n,i,S,u,d)
		max = Amax(n,i,S,u,d)
		for m in range(0,int(k)):
			A[i][m] = ((k-float(m))/k) * min + (float(m)/k) * max
			if((A[i][m] >= X) and (A[i][m] < H)):
				C[i][m] = A[i][m] - X
			else:
				C[i][m] = 0.0
	
	Cud = 0.0
	
	#backward induction
	for j in range(int(n)-1, -1, -1):
		for i in range(0,j+1):
			S_current = S*u**(j-i)*d**i
			min = Amin(j,i,S,u,d)
			max = Amax(j,i,S,u,d)
			for m in range(0,int(k)+1):
				a_current = ((k-float(m))/(k)) * min + (float(m)/(k)) * max
				Au = ( (float(j)+1) * a_current + S_current * u ) / ( float(j) + 2.0 )
				if(Au >= H):
					Cu = 0
				else:
					for l in range(0,int(k)):
						if ( (A[i][l]<=Au) and ((Au<=A[i][l+1])) ):
							break
					if(A[i][l]==A[i][l+1]):
						x = 1.0
					else:
						x = (Au-A[i][l+1])/(A[i][l]-A[i][l+1])
					if(x > 1.0):
						x = x - k/25.0 
					Cu = x * C[i][l] + (1-x) * C[i][l+1]
				Ad = ( (float(j)+1.0) * a_current + S_current * d ) / ( float(j) + 2.0 )
				if(Ad >= H):
					Cd = 0
				else:
					for l in range(0,int(k)):
						if ( (A[i+1][l]<=Ad) and ((Ad<=A[i+1][l+1])) ):
							break
					if(A[i+1][l]==A[i+1][l+1]):
						x = 1.0
					else:
						x = (Ad-A[i+1][l+1])/(A[i+1][l]-A[i+1][l+1])
					if(x > 1.0):
						x = x - k/25.0 					
					Cd = x * C[i+1][l] + (1-x) * C[i+1][l+1]
				T[m] = ( q * Cu + (1-q) * Cd ) / R
			for m in range(0, int(k)+1):
				C[i][m] = T[m]
				A[i][m] = (k- float(m)) / (k) * min + (float(m) / (k)) * max
		if(j == 1):
			Cud = C[0][0] - C[1][0]
	delta = Cud/(S*u-S*d)
	print "Call  = %04.4f" % C[0][0]
	print "delta = %04.4f" % delta