import cv2
import numpy as np
import pickle
import os
#use this code to extract the images from the p file.
#you can make changes to the files and folders in the code as per your need
def extract(db):
	spc = ['/','?','%','*',':','|','"','<','>','.',''] #special characters that restrict your from creating a folder name
	if os.path.isdir('dataset'):
		os.chdir('dataset')
	else:
		os.makedirs('dataset')
		os.chdir('dataset')
	for i in range (0,len(db)):
		path = db[i][2]
		if path in spc:
			path = "special characters"
		if not os.path.exists(path):
			os.makedirs(path)
		cv2.imwrite((path+'/'+str(db[i][1])+"_"+str(i)+'.png'), db[i][0])
f = open("dev_letter_D.p", "rb")
db = pickle.load(f,encoding = "ISO-8859-1")
extract(db)
