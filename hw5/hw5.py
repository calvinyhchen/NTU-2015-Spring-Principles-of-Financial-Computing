import sys
import math
import string
import random

def call(St,X):
	if(St>X):
		return 1.0
	else:
		return 0.0

if __name__ == '__main__':
	#read input
	fp  = open('input.txt', 'r')
	S 	= fp.readline()
	X 	= fp.readline()
	r	= fp.readline()
	v 	= fp.readline()
	t	= fp.readline()
	n	= fp.readline()
	m	= fp.readline()	  
	e	= fp.readline()	  
	fp.close()
	S = string.atof(S)
	X = string.atof(X)
	t = string.atof(t)
	v = v.replace("%","")
	v = string.atof(v)/100
	r = r.replace("%","")
	r = string.atof(r)/100
	n = string.atof(n)
	m = string.atof(m)
	e = string.atof(e)

#monte carlo
	C = 0.0
	delta = 0.0
	gamma = 0.0
	R = math.exp(-r*t)
	for i in range(int(m)):
		normal = random.normalvariate(0.0,1.0)
		expo = math.exp((r - v**2/2.0) * t + v * math.sqrt(t) * normal)
		St = S * expo
		Stp = (S+e) * expo 
		Stm = (S-e) * expo
		C += (call(St,X))*R
		delta += (call(Stp,X)-call(Stm,X))*R/(2.0*e)
		gamma += (call(Stp,X)+call(Stm,X)-2.0*(call(St,X)))*R/(e**2)		
	C /= m
	delta /= m
	gamma /= m
	print "\nMonte Carlo:"
	print 'Price: %.5f' % C
	print "delta: %.7f" % delta
	print "gamma: %.8f" % gamma
	
#tree	
	T = t/n
	lamda = (math.pi/2.0)**0.5
	pu = 1.0/(2.0*lamda**2) + ((r+v**2)*T**0.5)/(2.0*lamda*v)
	pd = 1.0/(2.0*lamda**2) - ((r-v**2*2.0)*T**0.5)/(2.0*lamda*v)
	pm = 1.0 - pu - pd
	u = math.exp(lamda*v*T**0.5)
	call_price = []
	for i in range(0,2*int(n)+1):
		if(S*u**(n-i)>X):
			call_price.append(1.0)
		else:
			call_price.append(0.0)
	for j in range(int(n)-1,-1,-1):
		if (j==0):
			call_u = call_price[0]
			call_m = call_price[1]
			call_d = call_price[2]
		for i in range(0,2*j+1):
			call_price[i] = (pu*call_price[i] + pm*call_price[i+1] + pd*call_price[i+2])/math.exp(r*T)
	print "\nTrinomial Tree:"
	print 'Price: %.5f' % (call_price[0])
	print 'delta: %.6f' %((call_u-call_d)/(S*u-S/u))
	print 'gamma: %.8f' %((((call_u-call_m)/(S*u-S))-((call_m-call_d)/(S-S/u)))/((S*u-S/u)/2.0))