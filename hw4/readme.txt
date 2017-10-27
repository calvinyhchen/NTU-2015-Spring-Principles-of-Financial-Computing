Language: python 2.7.8

How to execute:
python hw4.py

my program read input from input.txt 

input.txt format
S (stock price at time 0)
X (strike price)
H (barrier, which is higher than S)	
t (maturity in years)
v (annual volatility)	
r (continuously compounded annual interest rate)	
n (number of periods)	
k (number of states per node)		 

sample input
100
80
130
1
30%
10%
100
300

sample output:
Call  = 17.3022
delta = 0.3152