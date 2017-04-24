import json

def queen(k):
	global flag
	for i in range (1,n+1):
		if (place(k,i)==True):
			x[k]=i
			if(k==n):
				if(flag==0):
					print "Solution::::::"
				print x[1:n-1]
				flag=1
			else:	
				queen(k+1)	


def place(k,i):
	for j in range (1,k):
		if((x[j]==i) or (abs(x[j]-i)==abs(j-k))):
			return False
	return True

x=[20,21,22,23,24,25,26,27,28]
n=8
global flag
flag=0
data=[]

with open('input.json') as f:
	data=json.load(f)

if(data["start"]>8 or data["start"]<1):
	print "Invalid input\n"
	exit()

print "Given condition: First queen is place in column ",data["start"],"\n"
x[1]=data["start"]

queen(2)

if(flag==0):
	print "No solution found\n"
