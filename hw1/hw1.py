import sys

start = 0
end = 0
count = 0

my_list = []

s = sys.argv[2]

for i in s:
	if i == ',':
		count += 1
		my_list.append(float(s[start:end]))
		end += 1
		start = end
	elif i == '[':
		start += 1
		end += 1
	elif i == ']':
		end = end
		my_list.append(float(s[start:end]))
	else:
		end += 1

y = float(sys.argv[1])	
w = float(sys.argv[3])	
	
print "y =", y
print "C =", my_list
print "w =", w

expo = []

temp = (1+y)**w
expo.append(temp)

for i in range(0,count+2,1):
	expo.append(expo[i]*(1+y))
	
price = []
for i in range(0,count+1,1):
	price.append(my_list[i]/expo[i])

MD1 = 0.0
MD2 = 0.0

for i in range(0,count+1,1):
	MD1 += price[i]*(w+i)
	MD2 += price[i]
	
MD = MD1/MD2
md = MD/(1+y)

print "md = %04.4f" % md

price_ = []
for i in range(0,count+1,1):
	price_.append((w+i)*(w+i+1)*my_list[i]/expo[i+2])

dP = 0	
for i in range(0,count+1,1):
	dP += price_[i]
	
convexity = dP/MD2
print "convexity = %04.4f " % convexity