import sys
import math
import string
import datetime

#read input
fp  = open('input.txt', 'r')
S 	= fp.readline()
X 	= fp.readline()
v 	= fp.readline()
T0 	= fp.readline()
T1 	= fp.readline()
m 	= fp.readline()	
r 	= fp.readline()
T2 	= fp.readline()
T3 	= fp.readline()       
fp.close()

#float
S = string.atof(S)
X = string.atof(X)
m = string.atoi(m)
v = v.replace("%","")
v = string.atof(v)/100
r = r.replace("%","")
r = string.atof(r)/100

#time-yyyy
y0 = string.atoi(T0[3]) + string.atoi(T0[2])*10 + string.atoi(T0[1])*100 + string.atoi(T0[0])*1000 
y1 = string.atoi(T1[3]) + string.atoi(T1[2])*10 + string.atoi(T1[1])*100 + string.atoi(T1[0])*1000
y2 = string.atoi(T2[3]) + string.atoi(T2[2])*10 + string.atoi(T2[1])*100 + string.atoi(T2[0])*1000
y3 = string.atoi(T3[3]) + string.atoi(T3[2])*10 + string.atoi(T3[1])*100 + string.atoi(T3[0])*1000
#time-mm
m0  = string.atoi(T0[6]) + string.atoi(T0[5])*10 
m1  = string.atoi(T1[6]) + string.atoi(T1[5])*10 
m2  = string.atoi(T2[6]) + string.atoi(T2[5])*10 
m3  = string.atoi(T3[6]) + string.atoi(T3[5])*10 
#time-dd
d0  = string.atoi(T0[9]) + string.atoi(T0[8])*10
d1  = string.atoi(T1[9]) + string.atoi(T1[8])*10
d2  = string.atoi(T2[9]) + string.atoi(T2[8])*10
d3  = string.atoi(T3[9]) + string.atoi(T3[8])*10
#time
T0 = datetime.datetime(y0, m0, d0)
T1 = datetime.datetime(y1, m1, d1)
T2 = datetime.datetime(y2, m2, d2)
T3 = datetime.datetime(y3, m3, d3)
W0 = datetime.datetime(y0, m0, d0).weekday()
W1 = datetime.datetime(y1, m1, d1).weekday()
W2 = datetime.datetime(y2, m2, d2).weekday()
W3 = datetime.datetime(y3, m3, d3).weekday()

#variable
mature =  (T1-T0).days + 1
exercise = (T3-T2).days + 1
holiday = 0
w=W0
for i in range(0, mature,1):
	if((w==5)or (w==6)):
		holiday += 1
		w = (w+8)%7
	else:
		w = (w+8)%7
trading = mature - holiday
rest = (T1-T3).days
T = trading*m
N = mature*m 
m = float(m)
trading = float(trading)
R = math.exp(r*(1.0/(365*m)))
u = math.exp(v*(((trading/(261.0*m*trading))**(0.5))))
d = 1/u
q = (R-d)/(u-d)
H = holiday*m
#option pricing
#call
option_price = []
stock_price = []
for i in range(0,T + 1,1):
	stock_price.append( S * u**(T-i) * d**i * R**H)
	option_price.append( max(0.0 , stock_price[i] - X ))
w = W1
for i in range(0,N,1):
	if( (w==5) or (w==6) ):
		for j in range(0,T+1,1):
			option_price[j] = option_price[j] / R
	else:
		for j in range(0,T,1):
			option_price[j] = ( option_price[j]*q + option_price[j+1]*(1-q) ) / R
	if( (i%m) == 0):
		w = ( w + 6 ) % 7
		
call_bermuda = option_price[0]

#put
for i in range(0,T + 1,1):
	stock_price[i] = (S*u**(T-i)*d**i * R**H)
	option_price[i] = (max(0.0,X - stock_price[i]))
w = W1
for i in range(0,N,1):
	if((w==5)or(w==6)):
		for j in range(0,T+1,1):
			stock_price[j] = stock_price[j] / R
			option_price[j] = option_price[j] / R
	else:	
		for j in range(0,T,1):
			stock_price[j] = stock_price[j] / u
			if( rest == 0 and exercise > 0 and ((i%m)==(m-1)) ):
				option_price[j] = max( (option_price[j]*q + option_price[j+1]*(1-q)) / R , (X - stock_price[j]) )
			else:
				option_price[j] = (option_price[j]*q + option_price[j+1]*(1-q)) / R
	if( (i%m) == 0 ):
		if( (rest == 0) ):
			exercise -= 1
		else:
			rest -= 1
	if( (i%m) == 0 ):
		w = ( w + 6 ) % 7
		
put_bermuda = option_price[0]
#output

print "Call = %04.4f" % call_bermuda
print "Put  = %04.4f" % put_bermuda