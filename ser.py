import hashlib
import socket
from Tkinter import *
root=Tk()
root.wm_title("SENDER")
l_1=Label(root,text="Enter IP")
l_1.grid(row=0,sticky=E)
ent_1=Entry(root)
ent_1.grid(row=0,column=1)

TCP_IP = ent_1.get()
TCP_PORT = 9001
hashkey=""
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
tcpsock.listen(5)
label_1=Label(root,text="Enter Plain Text")
label_1.grid(row=1,sticky=E)
entry_1=Entry(root)
entry_1.grid(row=1,column=1)



def acceptconn(event):
	global conn
	conn,addr=tcpsock.accept()
button_5= Button(root,text="Connect")
button_5.grid(row=0,column=3)
button_5.bind("<Button-1>",acceptconn)



def sha(event):
	global str1
	str1=entry_1.get()
	print str1
	global hashkey
	h = hashlib.sha1()
	h.update(str1)
	hashkey=h.hexdigest()
	print hashkey
button_1= Button(root,text="SHA")
button_1.grid(row=3)
button_1.bind("<Button-1>",sha)
def md5(event):
	global str1
	str1=entry_1.get()
	print str1
	global hashkey
	h = hashlib.md5()
	h.update(str1)
	hashkey=h.hexdigest()
	print hashkey
button_2= Button(root,text="MD5")
button_2.grid(row=3,column=1)
button_2.bind("<Button-1>",md5)
def printname(event):
	global hashkey
	msg = Message(root, text = hashkey)
	msg.config(bg='lightgreen', font=('times', 12, 'italic'))
	msg.grid(row=9)
button_3= Button(root,text="SHOW")
button_3.grid(row=5)
button_3.bind("<Button-1>",printname)
####

####
def send(event):
		global conn
		#conn,addr=tcpsock.accept()
		conn.send(hashkey)	
		conn.send(str1)
button_4= Button(root,text="SEND")
button_4.grid(row=5,column=1)
button_4.bind("<Button-1>",send)

#button_4= Button(root,text="CLOSE CONNECTION",command=close())
#button_4.grid(row=9)'''

root.mainloop()


