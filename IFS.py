





from PIL import Image
from pytesseract import image_to_string 
import cv2


im = Image.open('3.png')
#im=img.rotate(90)
im.save('cheqw.jpg')



a = (0,0,2300,300)   
img= im.crop(a) 
img.save("IFS.jpg")
IFS=image_to_string(img)
#print(IFS)
word_list=['SBIN0021464','UTIB0000395', 'DMKJ0000002' ] 
for word in word_list:
	if word in IFS:
		if word=='SBIN0021464':
			#print("SBI")
			import SBI
			

		if word=='UTIB0000395':
			#print('AXIS')
			import AXIS

			
		if word=='DMKJ0000002':
			#print('DMK')
			import DMK


		

		
