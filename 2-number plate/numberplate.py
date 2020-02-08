# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 12:29:30 2020

@author: Hp-pc
"""
from PIL import Image
import cv2
import pytesseract
import imutils
pytesseract.pytesseract.tesseract_cmd=r"F:\Tesseract\tesseract.exe"

#read the input image
image=cv2.imread("sample1.jpg")

#resize the image
image = imutils.resize(image, width=min(500, len(image[0])))

#display original image
cv2.imshow("Original Image",image)
cv2.waitKey(0)

#RGB to Gray conversion
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("1-grayscale conversion",gray)
cv2.waitKey(0)

#Noise removal
gray=cv2.bilateralFilter(gray,11,17,17)
cv2.imshow("2- Bilateral Filter", gray)
cv2.waitKey(0)

#Edge Detection in image
edged=cv2.Canny(gray,170,200)
cv2.imshow("3- edge detected", edged)
cv2.waitKey(0)

#find Contours
cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#CRAETE copy of rgb image to draw all contours
img1 = image.copy() 
cv2.drawContours(img1, cnts ,-1, (0,255,0), 3)
cv2.imshow("4-all contours", img1)
cv2.waitKey(0)

#SORT CONTOURS BASED ON AREA KEEPING MINIMUM REQUIRED  AREA AS '30'
cnts = sorted(cnts, key=cv2.contourArea, reverse = True)[:30]
NumberPlateCnt = None # we do not have no number plate contour

#top 30 contours are extracted
img2 = image.copy()
cv2.drawContours(img2,cnts,-1, (0,255,0), 3)
cv2.imshow("5- Top 30 contours", img2)
cv2.waitKey(0)

#finding the best possible approx contour of number plate
count=0
idx=7
for c in cnts:
    peri=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.02*peri,True)   #output number of edge in contour
    if len(approx) == 4:                        #contour with 4 corners
        NumberPlateCnt = approx                 #our approx number plate contour
        
        #crop contours and store it into cropped images folder
        x,y,w,h = cv2.boundingRect(c)                                    #find co-ord for plate
        new_img = image[y:y+h, x:x+w]                                    #create new image
        cv2.imwrite('Cropped Images-Text/' + str(idx) + '.png', new_img) #store new image
        idx+=1
        break

#drawing selected contour in org image
cv2.drawContours(image, [NumberPlateCnt], -1, (0,255,0), 3)        
cv2.imshow("Final Image With No Plate detected", image)
cv2.waitKey(0)

Cropped_img_loc = 'Cropped Images-Text/7.png'
pic=cv2.imread(Cropped_img_loc)
cv2.imshow("Cropped Image",pic)
cv2.waitKey(0)

#Use tesseract to convert image into string 
text= pytesseract.image_to_string(Cropped_img_loc, lang='eng')
print("Number is :",text)       #showing result on console
cv2.waitKey(0)      #Wait for user imput before closing the images displayed
