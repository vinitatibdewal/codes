import os, sys
import pyDes
from Tkinter import *
root=Tk()
root.wm_title("Cipher")
lb1=Label(root, text="Enter plaintext")
lb1.grid(row=0,sticky=E)
entry_1=Entry(root)
entry_1.grid(row=0,column=1)
lb2=Label(root, text="Cipher")
lb2.grid(row=1,column=1)
lb2=Label(root, text="Plain")
lb2.grid(row=1,column=2)
def caesarCipher(event):
	cipherText=[]
	decrText=[]
	plainText=entry_1.get()
	for i in range(len(plainText)):
		cipherText.append(chr((ord(plainText[i])+4)%256))	#chr()->takes ascii amd returns char, ord()->viceversa
	
	msg=Message(root, text=cipherText)
	msg.grid(row=2, column=1)
	for i in range (len(cipherText)):
		decrText.append(chr((ord(cipherText[i])-4)%256))	
	msg1=Message(root, text=decrText, aspect=500)
	msg1.grid(row=2, column=2)

bt1=Button(root, text="Caesar")
bt1.grid(row=2, column=0)
bt1.bind("<Button-1>", caesarCipher)
def railFence(event):
	a1=[]
	a2=[]
	mainList=[]
	decrText=[]
	plainText=entry_1.get()
	for i in range (len(plainText)):
		if i%2==0:
			a1.append(plainText[i])
		else:
			a2.append(plainText[i])
	a1s=''.join(a1)
	a2s=''.join(a2)
	m=a1s+a2s
	msg=Message(root, text=m, aspect=500)
	msg.grid(row=3, column=1)
	j=0
	for i in range (len(m)):
		
		if i%2==0:
			decrText.append(a1[j])
		else:
			decrText.append(a2[j])
			j=j+1
	msg1=Message(root, text=decrText, aspect=500)
	msg1.grid(row=3, column=2)
bt2=Button(root, text="Rail Fence")
bt2.grid(row=3, column=0)
bt2.bind("<Button-1>", railFence)

def playfair(event):
	str1=entry_1.get()
	a=[['k','e','y','a','b'],['c','d','f','g','h'],['i','l','m','n','o'],['p','q','r','s','t'],['u','v','w','x','z']]
	result=""
	for i in range(len(str1)):
		if(str1[i]=='j'):
			result=result+'l'
		for j in range(5):
			for k in range(5):
				if(a[j][k]==str1[i]):
					if(k!=4):
						result=result+a[j][k+1];
					else:
						result=result+a[j][0]
						
	str2=""
	for i in range(len(result)):
		if(result[i]=='j'):
			str2=str2+'l'
		for j in range(5):
			for k in range(5):
				if(a[j][k]==result[i]):
					if(k!=0):
						str2=str2+a[j][k-1];
					else:
						str2=str2+a[j][4]
	msg=Message(root, text=result, aspect=500)
	msg.grid(row=4, column=1)
	msg1=Message(root, text=str2, aspect=500)
	msg1.grid(row=4, column=2)
bt2=Button(root, text="Play Fair")
bt2.grid(row=4, column=0)
bt2.bind("<Button-1>", playfair)	

def DES(event):
	data=entry_1.get()
	k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
	d = k.encrypt(data)
	s1=repr(d)
	
	res=k.decrypt(d)
	s2=repr(res)
	msg=Message(root, text=s1, aspect=500)
	msg.grid(row=5, column=1)
	msg1=Message(root, text=s2, aspect=500)
	msg1.grid(row=5, column=2)
bt3=Button(root, text="DES")
bt3.grid(row=5, column=0)
bt3.bind("<Button-1>", DES)
root.mainloop()
