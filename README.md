# Sanskrit-letter-dataset

This dataset has been created for the research and development of a Sanskrit OCR.
The dataset contains 7702 images of sanskrit(Devanagari) letters belonging to 602 classes.

This is a publicly available dataset can be used for further research.

The dataset is structured in the following manner:
	The data is in the form of a 2D array.
	The first dimension indicates the indexed letter in the dataset.
	The second dimension is again a 1D dimensional array containing three elements- 
		 The first element is the image in array form.
		 The second element is the corresponding class index number.
		 The third element is the corresponding English class Annotation.

Sample Images of Sanskrit letters in the dataset:
![alt text](https://github.com/avadesh02/Sanskrit-letter-dataset/images/1.png)
![alt text](https://github.com/avadesh02/Sanskrit-letter-dataset/images/2.png)
![alt text](https://github.com/avadesh02/Sanskrit-letter-dataset/images/3.png)
![alt text](https://github.com/avadesh02/Sanskrit-letter-dataset/images/4.png)
![alt text](https://github.com/avadesh02/Sanskrit-letter-dataset/images/5.png)

Please run dbreader.py to read the dataset and understand the dataset.

print('reading...')
db = pickle.load(open("dev_letter_D.p","rb"))

print("Number of letter images in the dataset are:" + str(len(db)))


#Please run the code below to see an Example
```
i = 0
cv2.imshow('a',db[i][0])
cv2.waitKey()
print("The Class index number of the sanskrit letter Image is : " + str(db[i][1]))
print("English Class Annotation of the sanskrit Image(I-Trans) is : " + str(db[i][2]))
```