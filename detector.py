import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtWidgets,QtCore, QtGui
import cv2
import numpy as np
import glob
import random
import imutils
import pytesseract
from PIL import Image, ImageEnhance
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.resize(872, 414)
        self.setWindowTitle('License Plates Detection')
        self.initUI()

    def initUI(self):
        #label
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(300, 300, 171, 21))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(650, 300, 141, 21))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(210, 50, 311, 241))
        self.label.setAutoFillBackground(True)
        self.label.setStyleSheet("border-color: rgb(50, 50, 50);\n"
"selection-color: rgb(206, 207, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(550, 50, 311, 241))
        self.label_7.setAutoFillBackground(True)
        self.label_7.setStyleSheet("border-color: rgb(50, 50, 50);\n"
"selection-color: rgb(206, 207, 255);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(30, 50, 141, 41))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 100, 141, 41))
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 340, 141, 41))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(300, 330, 161, 31))
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(190, 40, 20, 351))
        self.line.setAutoFillBackground(True)
        self.line.setStyleSheet("")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self)
        self.line_2.setGeometry(QtCore.QRect(0, 30, 881, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(270, 10, 341, 21))
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 150, 141, 41))
        self.pushButton_4.setAutoFillBackground(True)
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 200, 141, 41))
        self.pushButton_5.setAutoFillBackground(True)
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(650, 330, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.line_3 = QtWidgets.QFrame(self)
        self.line_3.setGeometry(QtCore.QRect(0, 380, 871, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(410, 390, 111, 21))
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form","License plate detector"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Detected license plate:</span></p><h6 style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600;\"><br/></h6></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><h6 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Predicted Number:</span></h6><h6 style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600;\"><br/></h6></body></html>"))
        self.pushButton.setText(_translate("Form", "Load Image"))
        self.pushButton_2.setText(_translate("Form", "Load Video "))
        self.pushButton_3.setText(_translate("Form", "Exit"))
        self.label_4.setText(_translate("Form", ""))
        self.label_5.setText(_translate("Form", "<html><head/><body><h6 align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">LICENSE PLATES DETECTOR</span></h6></body></html>"))
        self.pushButton_4.setText(_translate("Form", "Open Camera"))
        self.pushButton_5.setText(_translate("Form", "Stop Camera"))
        self.label_6.setText(_translate("Form", "<html><head/><body><h6 style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">made by bougrine imane</span></h6></body></html>"))
        self.pushButton.clicked.connect(self.load_image)
        self.pushButton_3.clicked.connect(self.exit_func)

    def exit_func(self):
        sys.exit(1)
    def load_image(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=QtWidgets.QFileDialog.Options())
        myimg=cv2.imread(fileName)
        myimg=cv2.resize(myimg,(311,241))
        cv2.imwrite('resized.jpg',myimg)
        self.label.setPixmap(QtGui.QPixmap('resized.jpg'))
        self.label.setScaledContents(True)
        self.label.adjustSize()
        self.plate_detected(fileName)

    def plate_detected(self,filename):
        #binarization function to preprocess the image
        def binarize(image,threshold):
            binary_image=image.convert("L")
            for x in range(binary_image.width):
              for y in range(binary_image.height):
                if binary_image.getpixel((x,y))< threshold:
                  binary_image.putpixel( (x,y), 0 )
                else:
                  binary_image.putpixel( (x,y), 255 )
            return binary_image
        # Load Yolo
        net = cv2.dnn.readNet("yolov3_training_last.weights", "yolov3_testing.cfg")
        # Name custom object
        classes = ["License plate"]
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        colors = np.random.uniform(0, 255, size=(len(classes), 3))
        # loop through all the images
        img = cv2.imread(filename)
        #img = cv2.resize(img, None, fx=0.8, fy=0.8)
        height, width, channels = img.shape
        # Detecting objects
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)
        # Showing informations on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.3:
                    # Object detected
                    print(class_id)
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color = colors[class_ids[i]]
                color=[0, 0, 255]
                print("color is ",color)
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                instance=img.copy()
                gray = cv2.cvtColor(instance, cv2.COLOR_BGR2GRAY)
                gray = cv2.bilateralFilter(gray, 11, 25, 32)
                #gray = cv2.Canny(gray, 100, 250)
                new_img=gray[y:y + h, x:x + w]
                cv2.imwrite('immatric.jpg', new_img)
                cv2.putText(img, label, (x, y + 60), font,2 , color, 3)
                cv2.resize(img,(311,241))
                cv2.imwrite('plate_box.jpg', img)

        self.label_7.setPixmap(QtGui.QPixmap('plate_box.jpg'))
        self.label_7.setScaledContents(True)
        Cropped_img_loc = 'immatric.jpg'
        self.label_4.setPixmap(QtGui.QPixmap(Cropped_img_loc))
        self.label_4.setScaledContents(True)
        # Use tesseract to covert image into string
        #img= cv2.imread(Cropped_img_loc)
        img=Image.open(Cropped_img_loc )
        #img= binarize(img,150)
        text = pytesseract.image_to_string(img)
        #cv2.imshow("Cropped Image ", cv2.imread('22.jpg'))
        print("Number is :", text)
        self.lineEdit.setText(text)

def window():
    app=app = QApplication([])
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

window()
