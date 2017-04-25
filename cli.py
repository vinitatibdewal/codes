import hashlib
import socket
from Tkinter import *
import tkMessageBox
root=Tk()
root.wm_title("RECEIVER")
TCP_IP = 'localhost'
TCP_PORT = 9001
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
def clear():
	
	msg = Message(root, text ="         ",justify=LEFT,borderwidth=10,aspect=500)
	msg.config(bg='lightgreen',bd=5,font=('times', 12, 'italic'))
	msg.grid(row=7)
def clear1():
	msg = Message(root, text ="         ",justify=LEFT,borderwidth=10,aspect=500)
	msg.config(bg='lightgreen',bd=5,font=('times', 12, 'italic'))
	msg.grid(row=7,column=2)
def sha(event):
	clear()
	global data
	data = s.recv(40)
	print data
	msg = Message(root, text = data,aspect=500)
	msg.config(bg='lightgreen', font=('times', 12, 'italic'))
	msg.grid(row=7)
	print "hashkey recieved is: ",data
button_1= Button(root,text=" RECIEVE SHA")
button_1.grid(row=1)
button_1.bind("<Button-1>",sha)
###
def md5(event):
	clear1()
	global data3
	data3 = s.recv(32)
	print data3
	msg = Message(root, text = data3,aspect=500)
	msg.config(bg='lightgreen', font=('times', 12, 'italic'))
	msg.grid(row=7,column=2)
	print "hashkey recieved is: ",data3
button_4= Button(root,text=" RECIEVE MD5")
button_4.grid(row=1,column=1)
button_4.bind("<Button-1>",md5)
###
def plaindata(event):
	global data1
	data1=s.recv(100)
	print "data recieved is: ",data1
	print type(data1)
button_3= Button(root,text=" RECIEVE PLAIN DATA")
button_3.grid(row=3)
button_3.bind("<Button-1>",plaindata)

def matchsha(event):
	global data,data1
	
	h = hashlib.sha1()
	h.update(data1)
	hashkey=h.hexdigest()
	if data==hashkey:
		msg = Message(root, text = "MATCHED!!",aspect=500)
		msg.config(bg='lightgreen', font=('times', 12, 'italic'))
		msg.grid(row=12,column=0)
		tkMessageBox.showinfo("Title", " NO Tampering Found\n Integrity is maintained ")
	else:
		msg = Message(root, text = "NOT MATCHED!!",aspect=500)
		msg.config(bg='lightgreen', font=('times', 12, 'italic'))
		msg.grid(row=12,column=0)

button_2= Button(root,text="MATCH SHA")
button_2.grid(row=10)
button_2.bind("<Button-1>",matchsha)

###
def matchmd5(event):
	global data3,data1
	
	h = hashlib.md5()
	h.update(data1)
	hashkey=h.hexdigest()
	if data3==hashkey:
		msg = Message(root, text = "MATCHED!!",aspect=500)
		msg.config(bg='lightgreen', font=('times', 12, 'italic'))
		msg.grid(row=12,column=1)
		tkMessageBox.showinfo("Title", " NO Tampering Found\n Integrity is maintained ")
	else:
		msg = Message(root, text = "NOT MATCHED!!")
		msg.config(bg='lightgreen', font=('times', 12, 'italic'))
		msg.grid(row=12,column=1)
	
button_5= Button(root,text="MATCH MD5 ")
button_5.grid(row=10,column=1)
button_5.bind("<Button-1>",matchmd5)

###
root.mainloop()

	
