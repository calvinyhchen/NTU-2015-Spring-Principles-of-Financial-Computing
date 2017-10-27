Language: python 2.7.9

How to execute:
python hw5.py

my program read input from input.txt 

input.txt format
S (stock price)
X (strike price) 
r (annual interest rate in percentage)
v (annual volatility in percentage)
t (year)
n (total number of periods)
m (number of sample paths of simulation)
e (see pp. 758ff)	 

sample input:
100
90
5%
40%
2
1000
1000000
0.001

sample output:

Monte Carlo:
Price: 0.48118
delta: 0.0049766
gamma: 2.71451225

Trinomial Tree:
Price: 0.47805
delta: 0.006262
gamma: -0.00007036

Remark:
For Monte Carlo, my price interval is slightly bigger than the interval on website.
For Trinomial Tree, I calculated delta by (Cu-Cd)/(Su-S/u) and for gamma,  ( (Cu-Cm)/(Su-S) - (Cm-Cd)/(S-S/u) ) / ((Su - Sd)/2)