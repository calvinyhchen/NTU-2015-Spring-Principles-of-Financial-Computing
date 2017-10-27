import sys
import math
import string

#read input
S = input('stock price at time 0 : ')
X = input('strike price : ')
v = raw_input('annual volatility in percentage : ')
t = input('maturity in years : ')
n = input('the number of period : ')
r = raw_input('interest rate in percentage : ')

#type -> float
S = float(S)
X = float(X)
t = float(t)
N = n
n = float(n)
v = v.replace("%","")
r = r.replace("%","")
v = string.atof(v)/100
r = string.atof(r)/100

#used variable
R = math.exp(r*(t/n))
u = math.exp(v*((t/n)**(0.5)))
d = 1/u
q = (R-d)/(u-d)

option_price = []
stock_price = []
put_eu = []
for i in range(0,N + 1,1):
	stock_price.append(S*u**(N-i)*d**i)
	option_price.append(max(0.0,stock_price[i] - X))
	put_eu.append(max(0.0,X - stock_price[i]))

for i in range(0,N + 1,1):
	for j in range(0,N - i,1):
		option_price[j] = (option_price[j]*q + option_price[j+1]*(1-q))/R 
		put_eu[j] = (put_eu[j]*q + put_eu[j+1]*(1-q))/R 

call_euro = option_price[0]
call_am = option_price[0]
put_euro = put_eu[0]

for i in range(0,N + 1,1):
	stock_price[i] = (S*u**(N-i)*d**i)
	option_price[i] = (max(0.0,X - stock_price[i]))

for i in range(0,N + 1,1):
	for j in range(0,N - i,1):
		stock_price[j] = stock_price[j]/u
		option_price[j] = max((option_price[j]*q + option_price[j+1]*(1-q))/R,(X - stock_price[j])) 

put_am = option_price[0]
print("--------------------------------------")
print "European Call = %04.4f" % call_euro
print "European Put  = %04.4f" % put_euro
print "American Call = %04.4f" % call_am
print "American Put  = %04.4f" % put_am