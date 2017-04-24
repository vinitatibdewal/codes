from Tkinter import *
################################ railfence ###############
def railFence(tList, depth):
    tList = list(tList)
    print tList
    length = len(tList)
    cipherRf = [[] for i in range(depth)]
    lenRails = range(depth - 1) + range(depth-1,0,-1)
    print "lenRails",lenRails
    m=0
    while m != length:

        for i in lenRails:
            if(m == length):
                break
            else:

                cipherRf[i].append(tList[m])
            m+=1
    print "cipherRf",cipherRf

    cipherList=[]
    for i in cipherRf:
        for m in i:
            cipherList.append(m)
    return cipherList

def decryptRailFence(cipherRF, depth):
    decryptRange = range(len(cipherRF))
    decryptRails = railFence(decryptRange,depth)
    plainText = [] * len(cipherRF)
    for i in range(len(cipherRF)):
        plainText.append(cipherRF[decryptRails.index(i)])
    return plainText

def buttonRailfence():
	text=entry1.get()
	depth=int(entry2.get())
	enmsg=railFence(text,depth)
	str1=''.join(enmsg)
	demsg=decryptRailFence(enmsg,depth)
	encrypted.config(text="Encrypted text:"+str1)
	str2=''.join(demsg)
	decrypted.config(text="Decrypted text:"+str2)

####################### playfair ##################################

def playfair(text,key):
    global cipher,finalPlay
    
    tList = list(text)
    print tList
    textList = list(set(list(text)))
    print textList
    #key=raw_input("Enter the key : ")

    m = key + 'abcdefghiklmnopqrstuvwxyz'

    a = []
    print m

    for i in m:
        if i not in a:
            a.append(i)
    print a

    finalPlay = []

    for i in range(5):
        temp = []
        for z in range(5):
            temp.append(a[z + 5 * i])
	#print temp
        finalPlay.append(temp)

    print finalPlay



    for i in range(0, len(tList) - 1):
        if tList[i] == tList[i + 1]:
            tList.insert(i + 1, 'x')


    cipher = []
    for i in range(0, len(tList) - 1, 2):
        xIndex = yIndex = -1
        xxIndex = yyIndex = -1
        for uu in range(0, 5):
            if tList[i] in finalPlay[uu]:
		print "i",tList[i]
                xIndex = uu
		print "xindex:",xIndex
                yIndex = finalPlay[uu].index(tList[i])
		print "yIndex:",yIndex
                break
        for uu in range(0, 5):
            if tList[i + 1] in finalPlay[uu]:
		print "i+1",tList[i+1]
                xxIndex = uu
		print "xxIndex:",xxIndex
                yyIndex = finalPlay[uu].index(tList[i + 1])
		print "yyIndex:",yyIndex
                break

        if xIndex == xxIndex:
	    		
            cipher.append(finalPlay[xIndex][(yIndex + 1) % 5])
		
            cipher.append(finalPlay[xxIndex][(yyIndex + 1) % 5])
        elif yIndex == yyIndex:
            cipher.append(finalPlay[(xIndex + 1) % 5][yIndex])
            cipher.append(finalPlay[(xxIndex + 1) % 5][yyIndex])
        else:
            cipher.append(finalPlay[xIndex][yyIndex])
            cipher.append(finalPlay[xxIndex][yIndex])


            # print tList[i] , tList[i+1] , xIndex , xxIndex , yIndex , yyIndex

    #print "Playfair Cipher : " , cipher
    return cipher


def decryptPlayFair():
    global cipher,finalPlay

    tList= list(cipher)
    cipher = []
    for i in range(0, len(tList) - 1, 2):
        xIndex = yIndex = -1
        xxIndex = yyIndex = -1
        for uu in range(0, 5):
            if tList[i] in finalPlay[uu]:
		
                xIndex = uu
                yIndex = finalPlay[uu].index(tList[i])
                break
        for uu in range(0, 5):
            if tList[i + 1] in finalPlay[uu]:
		
                xxIndex = uu
                yyIndex = finalPlay[uu].index(tList[i + 1])
                break

        if xIndex == xxIndex:
            cipher.append(finalPlay[xIndex][(yIndex - 1) % 5])
            cipher.append(finalPlay[xxIndex][(yyIndex - 1) % 5])
        elif yIndex == yyIndex:
            cipher.append(finalPlay[(xIndex - 1) % 5][yIndex])
            cipher.append(finalPlay[(xxIndex - 1) % 5][yyIndex])
        else:
            cipher.append(finalPlay[xIndex][yyIndex])
            cipher.append(finalPlay[xxIndex][yIndex])

	
            # print tList[i] , tList[i+1] , xIndex , xxIndex , yIndex , yyIndex
    plainT=""
    for i in range(len(cipher)):
            if cipher[i] != 'x':
                plainT += cipher[i]
    #print "PlainText is : " , plainT
    return plainT

def buttonPlayfair():
	text=entry1.get()
	key=entry3.get()
	cipher1=playfair(text,key)
	st1=''.join(cipher1)
	plaintext=decryptPlayFair()
	encrypted.config(text="Encrypted text:"+st1)
        decrypted.config(text="Decrypted text:"+plaintext)



#########################################################################

window=Tk()

label1=Label(window,text="Enter input text:")
label1.grid(row=0,column=0)

entry1=Entry(window)
entry1.grid(row=0,column=1)

label2=Label(window,text="Enter depth:")
label2.grid(row=1,column=0)

entry2=Entry(window)
entry2.grid(row=1,column=1)

button1=Button(window,text="Railfence",command=buttonRailfence)
button1.grid(row=2,column=0)

encrypted=Label(window,text="Encrypted text:")
encrypted.grid(row=3,column=0)

decrypted=Label(window,text="Decrypted text:")
decrypted.grid(row=3,column=2)

label3=Label(window,text="Enter key:")
label3.grid(row=1,column=2)

entry3=Entry(window)
entry3.grid(row=1,column=3)

button2=Button(window,text="Playfair",command=buttonPlayfair)
button2.grid(row=2,column=2)

window.mainloop()
