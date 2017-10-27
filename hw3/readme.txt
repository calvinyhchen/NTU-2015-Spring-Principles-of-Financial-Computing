Language: python 2.7.8

How to execute:
python hw3.py

my program read input from input.txt 

input.txt format
S (stock price at the starting date)
X (strike price)
v (annual volatility in percentage)
T0 (starting date)
T1 (maturity date of option)
m (the number of periods per day for the tree)
r (annual interest rate in percentage)
T2 (starting date when option can be exercised)
T3 (final date when option can be exercised)

sample input
100
95
35%
2015-04-21
2015-06-19
2
0%
2015-05-21
2015-06-19

sample output:
Call = 8.4471
Put  = 3.4471