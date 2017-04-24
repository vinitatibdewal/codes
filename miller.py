from Tkinter import *
from random import randint

def calc(number):
	temp=number-1
	count=0
	while(temp%2)==0:
		count=count+1
		temp=temp/2
	return temp,count

def isnumber(d,s,number):
	for k in range (1,50):
		a=randint(2,number-1)
		x=(a**d)%number
		if x==1 or x==number-1:
			return True
		while d!=number-1:
			x=(x*x)%number
			d=d*2
			if x==1:
				return False
			if x==number-1:
				return True
		return False

def main(number):
	d,s=calc(number)
	return isnumber(d,s,number)

def isprime():
	if main(int(entry.get())):
		result.config(text="Result: prime")
	else:
		result.config(text="Result: composite")

window=Tk()
window.height=400
window.width=200

label=Label(window,text="Number")
label.place(x=20,y=25)

entry=Entry(window)
entry.place(x=100,y=20)

button=Button(window,text="Check",command=isprime)
button.place(x=100,y=80)

result=Label(window,text="Result:")
result.place(x=20,y=150)

window.mainloop()
