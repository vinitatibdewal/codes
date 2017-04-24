from Tkinter import *
import socket 
import hashlib
import tkMessageBox	

tcpip='localhost'
port=9001
s=socket.socket()
s.connect((tcpip,port))

def sha1():
	global data
	data = s.recv(40)
	print data
	msg = Message(window, text = data,aspect=500)
	#msg.config(bg='lightgreen', font=('times', 12, 'italic'))
	msg.grid(row=7)
	print "hashkey recieved is: ",data

def md5():
	global data3
	data3 = s.recv(32)
	print data3
	msg = Message(window, text = data3,aspect=500)
	#msg.config(bg='lightgreen', font=('times', 12, 'italic'))
	msg.grid(row=7,column=2)
	print "hashkey recieved is: ",data3

def matchsha():
	global data,data1
	h = hashlib.sha1()
	h.update(data1)
	hashkey=h.hexdigest()
	if data==hashkey:
		msg = Message(window, text = "MATCHED!!",aspect=500)
		#msg.config(bg='lightgreen', font=('times', 12, 'italic'))
		msg.grid(row=12,column=0)
		tkMessageBox.showinfo("Title", " NO Tampering Found\n Integrity is maintained ")
	else:
		msg = Message(window, text = "NOT MATCHED!!",aspect=500)
		#msg.config(bg='lightgreen', font=('times', 12, 'italic'))
		msg.grid(row=12,column=0)

def matchmd():
	global data3,data1
	h = hashlib.md5()
	h.update(data1)
	hashkey=h.hexdigest()
	if data3==hashkey:
		msg = Message(window, text = "MATCHED!!",aspect=500)
		#msg.config(bg='lightgreen', font=('times', 12, 'italic'))
		msg.grid(row=12,column=1)
		tkMessageBox.showinfo("Title", " NO Tampering Found\n Integrity is maintained ")
	else:
		msg = Message(window, text = "NOT MATCHED!!")
		#msg.config(bg='lightgreen', font=('times', 12, 'italic'))
		msg.grid(row=12,column=1)

def plain():
	global data1
	data1=s.recv(100)
	print "data recieved is: ",data1
	print type(data1)


window=Tk()

button1=Button(window,text="receive sha1",command=sha1)
button1.grid(row=0,column=0)

button2=Button(window,text="receive md5",command=md5)
button2.grid(row=0,column=2)

button3=Button(window,text="match sha1",command=matchsha)
button3.grid(row=2,column=0)

button4=Button(window,text="match md5",command=matchmd)
button4.grid(row=2,column=2)

button5=Button(window,text="receive plain data",command=plain)
button5.grid(row=3,column=1)

window.mainloop()
