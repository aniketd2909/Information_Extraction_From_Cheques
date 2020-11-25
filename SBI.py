from PIL import Image
from pytesseract import image_to_string 
import pandas as pd 
import numpy as np
import dic
#import numpy as np

import IFS

from word2number import w2n
import cv2
#import numpy as np
#from matplotlib import pyplot as plt


#im = Image.open('1.png')

im=IFS.im


a = (330,120,1000,250)  #bank name
img= im.crop(a) 
img.save("bank_name.jpg")
bank_name=image_to_string(Image.open('bank_name.jpg'))
print("BANK NAME =",bank_name)
#print(bank_name)

a=(1000,30,2200,300)            #address
img= im.crop(a) 
img.save("address.jpg")
address=image_to_string(Image.open('address.jpg'))
print("BANK ADDRESS =",address)


a = (2150,80,3000,200)    #date
img= im.crop(a) 
img.save("date.jpg")
img= cv2.imread('date.jpg')
ret,thresh1 = cv2.threshold(img,190,255,cv2.THRESH_BINARY)
cv2.imwrite("date_thresh.jpg",thresh1);
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(thresh1,kernel,iterations =1)
cv2.imwrite("date_erode.jpg",dilation)
date=image_to_string(dilation)
print("DATE =",date)


a = (200,280,2200,450)          #name
img= im.crop(a) 
img.save("name.jpg")
img= cv2.imread('name.jpg')
ret,thresh1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
cv2.imwrite("name_thresh.jpg",thresh1);
#kernel = np.ones((5,5),np.uint8)
#erosion = cv2.erode(thresh1,kernel,iterations =1)
#dilation = cv2.dilate(erosion,kernel,iterations =1)

#cv2.imwrite("name_erosion.jpg",thresh1);
name=image_to_string(thresh1)
print("PAYEE NAME =",name)
#print(name)



a = (450,440,2800,560)          #amount_word
img= im.crop(a) 
img.save("amount_words.jpg")
img= cv2.imread('amount_words.jpg')
ret,thresh1 = cv2.threshold(img,110,255,cv2.THRESH_BINARY)
cv2.imwrite("amount_word_thresh.jpg",thresh1);
kernel = np.ones((5,5),np.uint8)
#dilation = cv2.dilate(thresh1,kernel,iterations =1)
erosion = cv2.erode(thresh1,kernel,iterations =1)
cv2.imwrite("amount_words_erosion.jpg",erosion)
amount_words=image_to_string(erosion)

a= (100,550,1800,670)
img= im.crop(a) 
img.save("amount_append_words.jpg")
img= cv2.imread('amount_append_words.jpg')
ret,thresh1 = cv2.threshold(img,110,255,cv2.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(thresh1,kernel,iterations =1)
cv2.imwrite("amount_append_words_erosion.jpg",erosion);
append=image_to_string(erosion)
print("AMOUNT (in words) =",amount_words+append)


amount_num=w2n.word_to_num(amount_words+append)


a = (2250,520,2850,690)          #amount
img= im.crop(a) 
img.save("amount.jpg")
img= cv2.imread('amount.jpg')
ret,thresh1 = cv2.threshold(img,185,255,cv2.THRESH_BINARY)
#kernel = np.ones((5,5),np.uint8)

dilation = cv2.dilate(thresh1,kernel,iterations =1)
#erosion = cv2.erode(dilation,kernel,iterations =1)
cv2.imwrite("amount_thresh.jpg",dilation)
amount=image_to_string(dilation)
#print(amount)



bad_chars = ['.', '|','/','-','_',' ','[',']','--']
for i in bad_chars : 
    amount = amount.replace(i,"") 
print("AMOUNT =",amount)


if  str(amount_num)==amount: 
    print("Valid Check amount")
    b="Valid" 
else: 
    print("Not a Valid check amount") 
    b="Not_Valid"



a = (300,700,1000,850)  #acc no.
img= im.crop(a) 
img.save("accno.jpg")
img= cv2.imread('accno.jpg')
ret,thresh1 = cv2.threshold(img,130,255,cv2.THRESH_BINARY)
#cv2.imwrite("accno.jpg",thresh1)

accno=image_to_string(thresh1)
print("ACCOUNT NO =",accno)



a=(790,1300,1060,1420) #cheque number
img=im.crop(a)
img.save("cheqno.jpg")
img= cv2.imread('cheqno.jpg')

ret,thresh1 = cv2.threshold(img,140,255,cv2.THRESH_BINARY)
cv2.imwrite("cheqno_thresh.jpg",thresh1);

#cheqno=image_to_string(Image.open('cheqno1.jpg'))
#print(cheqno)

import seg

Cheqnumber=seg.cheqno
print("CHEQUE NUMBER=",Cheqnumber)


if Cheqnumber[0]=='0':
	Cheqnumber=Cheqnumber[1:]


for key, value in dic.multidict.items():  #Cheque no validation 
	for i in value:
		if int(Cheqnumber) == i:
			if key==accno:
				print("Valid Cheqno")
				z="Valid Cheqno"
			else:
				print("Invalid Cheqno")
				z="Invalid Cheqno"




# dictionary of lists  
#dict = {'BANK NAME':nme,'ADDRESS':add,'AMOUNT NO':amt,'ACCOUNT NO':acc, 'DATE':date1} 
dict = {'Amount Validation':[b],'Cheque No. Validation':[z],'Payee Name':[name],'BANK NAME':[bank_name],'ADDRESS':[address],'AMOUNT':[amount],'ACCOUNT NO':[accno], 'DATE':[date], 'CHEQUE NO':[Cheqnumber]} 
df = pd.DataFrame(dict) 
  
# saving the dataframe 
#df.to_csv('file.csv',header='file.csv'.tell()==0,index=False) 

#to save to csv file
with open('file.csv','a') as f:
	df.to_csv(f,mode='a',header=f.tell()==0,index=False)






























