from Tkinter import *
import hashlib
import socket

def con():
	global conn
	conn,addr=tcpsoc.accept()
	
def sha1():
	global str1
	str1=entry2.get()
	print str1
	global hashkey
	h = hashlib.sha1()
	h.update(str1)
	hashkey=h.hexdigest()
	print hashkey

def md5():
	global str1
	str1=entry2.get()
	print str1
	global hashkey
	h = hashlib.md5()
	h.update(str1)
	hashkey=h.hexdigest()
	print hashkey

def show():
	global hashkey
	msg = Message(root, text = hashkey)
	#msg.config(bg='lightgreen', font=('times', 12, 'italic'))
	msg.grid(row=9)

def send1():
	global conn
	conn.send(hashkey)	
	conn.send(str1)

window=Tk()

label1=Label(window, text="Enter IP")
label1.grid(row=0, column=0)

entry1=Entry(window)
entry1.grid(row=0,column=1)

tcpip=entry1.get()
port=9001
hashkey=""
tcpsoc=socket.socket()
tcpsoc.bind((tcpip,port))
tcpsoc.listen(5)

button1=Button(window,text="connect",command=con)
button1.grid(row=0,column=2)

label2=Label(window, text="Enter text")
label2.grid(row=1, column=0)

entry2=Entry(window)
entry2.grid(row=1,column=1)

button2=Button(window,text="SHA1",command=sha1)
button2.grid(row=2,column=0)

button3=Button(window,text="MD5",command=md5)
button3.grid(row=2,column=2)

button4=Button(window,text="show",command=show)
button4.grid(row=3,column=2)

button5=Button(window,text="send",command=send1)
button5.grid(row=1,column=2)

window.mainloop()
