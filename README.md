# License-Plate-Detector

This is a program that can detecto the license plate of cars and then recognize what it is written on it.
To make this project i decided to follow this steps:
1)  I collected my own dataset (some images of cars )
2)  I annotated then using Vott (u can use also LabelImg)
3)  I trained my dataset using the yolov3 model ( i found a keras implementation of this net) 
4)  Then i used the deep learning based OCR model to recognize text on the predicted plate license ( I suggest you to use the keras-ocr implementation if you have a gpu in your machine because it gives very good predictions)

My model gives very good results even if my dataset is so small
![Capture](https://user-images.githubusercontent.com/58142887/84896432-dea50e80-b09b-11ea-8bcc-f591d0712bc6.PNG)
