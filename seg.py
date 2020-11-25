import numpy as np
import cv2
from matplotlib import pyplot as plt


charNames = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
im = cv2.imread('reference.png')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
#plt.imshow(imgray)
#plt.show()
ret,thresh = cv2.threshold(imgray,80,255,cv2.THRESH_BINARY_INV)
#plt.imshow(thresh)
#plt.show()    
 
kernel = np.ones((5,5), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
#find contours
    


_,ctrs,hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


#sort contours
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])
chars ={}
for i, ctr in enumerate(sorted_ctrs):
    # Get bounding box
    x, y, w, h = cv2.boundingRect(ctr)

    # Getting ROI
    roi = im[y:y+h, x:x+w]
    #roi = im[y-30:y+h+30, x-30:x+w+30]
    roi = cv2.resize(roi, dsize=(36,36), interpolation=cv2.INTER_CUBIC)
    ret,thresh = cv2.threshold(roi,80,255,cv2.THRESH_BINARY)
#    roi = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
   # roi = cv2.resize(roi, (36, 36)) 
    chars[i] = thresh
#    cv2.imshow('segment no:'+str(i),roi)
#    cv2.waitKey(0)
#    plt.imshow(chars[i])
#    plt.show() 




im = cv2.imread('cheqno_thresh.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,80,255,cv2.THRESH_BINARY_INV)
#plt.imshow(thresh)
#plt.show()    
 
kernel = np.ones((5,5), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
#find contours
    

_, ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)




#sort contours
sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

Output = []
for i, ctr in enumerate(sorted_ctrs):
	# Get bounding box
	x, y, w, h = cv2.boundingRect(ctr)

	# Getting ROI
	roi = im[y:y+h, x:x+w]

	#	roi = im[y-30:y+h+30, x-30:x+w+30]
	roi = cv2.resize(roi, dsize=(36,36), interpolation=cv2.INTER_CUBIC)
#	roi = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(roi,80,255,cv2.THRESH_BINARY)
	

#	cv2.imshow('segment no:'+str(i),thresh)
#	cv2.waitKey(0) 
#	plt.imshow(thresh)
#	plt.show() 
	scores=[]
	#	roi = cv2.resize(roi, (36, 36))
	for i in chars:
		# apply correlation-based template matching, take the
		# score, and update the scores list
		result = cv2.matchTemplate(thresh, chars[i],
			 cv2.TM_CCOEFF)
		(_, score, _, _) = cv2.minMaxLoc(result)
		scores.append(score)
		
	Output.append(charNames[np.argmax(scores)])
	
	
# display the output check OCR information to the screen
#print("Check OCR: {}".format(" ".join(Output)))

cheqno = ''.join(map(str,Output)) 
#print(cheqno)





