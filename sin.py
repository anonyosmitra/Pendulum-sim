import math
def factorial(i):
	if i==0 or i==0:
		return 1
	return i*factorial(i-1)

def isEven(i):
	if i%2==0:
		return 1
	else:
		return -1


def poly(x):
	rng=list(range(1,11,2))
	a=0
	for i in rng:
		a+=(math.pow(x,i)/factorial(i))*isEven(rng.index(i))
	return a



def mySin(x):
	si=1
	if x<0:
		x=-1*x
		si=-1
	while(x>=2*math.pi):
		x-=2*math.pi
	if(x<math.pi/2):
		return poly(x)*si
	elif(x<math.pi):
		return poly(math.pi-x)*si
	elif(x<math.pi*3/2):
		return -poly((x-math.pi))*si
	else:
		return poly(x-2*math.pi)*si