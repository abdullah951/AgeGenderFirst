# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitledNew.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import cv2 as cv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
import time
import argparse



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 521)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 731, 521))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-image: url(imgBacknew.png);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.ag_identification_image = QtWidgets.QRadioButton(self.tab)
        self.ag_identification_image.setGeometry(QtCore.QRect(230, 400, 121, 20))
        self.ag_identification_image.setStyleSheet("")
        self.ag_identification_image.setObjectName("ag_identification_image")
        self.identify = QtWidgets.QPushButton(self.tab)
        self.identify.setGeometry(QtCore.QRect(430, 400, 91, 23))
        self.identify.setObjectName("identify")

        self.identify.clicked.connect(lambda: self.whichbtn(self.identify))

        self.load_image = QtWidgets.QPushButton(self.tab)
        self.load_image.setGeometry(QtCore.QRect(230, 320, 75, 23))
        self.load_image.setStyleSheet("")
        self.load_image.setObjectName("load_image")

        self.load_image.clicked.connect(lambda:self.whichbtn(self.load_image))

        self.age_identification_image = QtWidgets.QRadioButton(self.tab)
        self.age_identification_image.setGeometry(QtCore.QRect(230, 360, 121, 17))
        self.age_identification_image.setStyleSheet("")
        self.age_identification_image.setObjectName("age_identification_image")
        self.capture_image = QtWidgets.QPushButton(self.tab)
        self.capture_image.setGeometry(QtCore.QRect(370, 320, 151, 23))
        self.capture_image.setObjectName("capture_image")

        self.capture_image.clicked.connect(lambda: self.whichbtn(self.capture_image))

        self.save_image = QtWidgets.QPushButton(self.tab)
        self.save_image.setGeometry(QtCore.QRect(320, 440, 80, 23))
        self.save_image.setObjectName("save_image")
        self.save_image.clicked.connect(lambda: self.whichbtn(self.save_image))

        self.original_image = QtWidgets.QLabel(self.tab)
        self.original_image.setGeometry(QtCore.QRect(70, 30, 271, 241))
        self.original_image.setMinimumSize(QtCore.QSize(271, 0))
        self.original_image.setMaximumSize(QtCore.QSize(271, 16777215))
        self.original_image.setStyleSheet("")
        self.original_image.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.original_image.setObjectName("original_image")
        self.gender_identification_image = QtWidgets.QRadioButton(self.tab)
        self.gender_identification_image.setGeometry(QtCore.QRect(230, 380, 121, 17))
        self.gender_identification_image.setStyleSheet("")
        self.gender_identification_image.setObjectName("gender_identification_image")
        self.converted_image = QtWidgets.QLabel(self.tab)
        self.converted_image.setGeometry(QtCore.QRect(380, 30, 271, 241))
        self.converted_image.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.converted_image.setObjectName("converted_image")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gender_identification_video = QtWidgets.QRadioButton(self.tab_2)
        self.gender_identification_video.setGeometry(QtCore.QRect(230, 380, 121, 17))
        self.gender_identification_video.setStyleSheet("")
        self.gender_identification_video.setObjectName("gender_identification_video")
        self.save_video = QtWidgets.QPushButton(self.tab_2)
        self.save_video.setGeometry(QtCore.QRect(320, 440, 80, 23))
        self.save_video.setObjectName("save_video")

        self.save_video.clicked.connect(lambda: self.whichbtn(self.save_video))

        self.age_identification_video = QtWidgets.QRadioButton(self.tab_2)
        self.age_identification_video.setGeometry(QtCore.QRect(230, 360, 121, 17))
        self.age_identification_video.setStyleSheet("")
        self.age_identification_video.setObjectName("age_identification_video")
        self.ag_identification_video = QtWidgets.QRadioButton(self.tab_2)
        self.ag_identification_video.setGeometry(QtCore.QRect(230, 400, 121, 20))
        self.ag_identification_video.setStyleSheet("")
        self.ag_identification_video.setObjectName("ag_identification_video")
        self.identify_2 = QtWidgets.QPushButton(self.tab_2)
        self.identify_2.setGeometry(QtCore.QRect(450, 400, 75, 23))
        self.identify_2.setObjectName("identify_2")

        self.identify_2.clicked.connect(lambda: self.whichbtn(self.identify_2))

        self.original_video = QtWidgets.QLabel(self.tab_2)
        self.original_video.setGeometry(QtCore.QRect(70, 30, 271, 241))
        self.original_video.setMinimumSize(QtCore.QSize(271, 0))
        self.original_video.setMaximumSize(QtCore.QSize(271, 16777215))
        self.original_video.setStyleSheet("")
        self.original_video.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.original_video.setObjectName("original_video")
        self.load_video = QtWidgets.QPushButton(self.tab_2)
        self.load_video.setGeometry(QtCore.QRect(230, 320, 75, 23))
        self.load_video.setStyleSheet("")
        self.load_video.setObjectName("load_video")

        self.load_video.clicked.connect(lambda: self.whichbtn(self.load_video))

        self.capture_video = QtWidgets.QPushButton(self.tab_2)
        self.capture_video.setGeometry(QtCore.QRect(370, 320, 151, 23))
        self.capture_video.setObjectName("capture_video")

        self.capture_video.clicked.connect(lambda: self.whichbtn(self.capture_video))

        self.converted_video = QtWidgets.QLabel(self.tab_2)
        self.converted_video.setGeometry(QtCore.QRect(380, 30, 271, 241))
        self.converted_video.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.converted_video.setObjectName("converted_video")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    currently_selected_image_url = ''

    def whichbtn(self, b):
        if b.text() == 'Load Image':
            print("clicked button is " + b.text())


            #OPEN FILE DIALOG

            fileName = QFileDialog.getOpenFileName(None,
                                                    "Open Image", "/home/jana",
                                                    "Image Files (*.png *.jpg *.bmp *.jpeg)")
            global currently_selected_image_url
            currently_selected_image_url = fileName[0]
            print(fileName[0])
            pixmap1 = QtGui.QPixmap(fileName[0])

            #GET LABEL SIZE

            w = self.original_image.width()
            h = self.original_image.height()

            #SET IMAGE

            self.original_image.setPixmap(pixmap1.scaled(w, h, Qt.KeepAspectRatio))
            self.original_image.setAlignment(QtCore.Qt.AlignCenter)

        elif b.text() == 'Capture Image from Webcam':
            cam = cv.VideoCapture(0)

            while True:
                ret, frame = cam.read()
                cv.imshow("Capture Image", frame)
                if not ret:
                    break
                k = cv.waitKey(1)

                #ASCII For ESC == 27
                #27%256 == 27
                if k % 256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k % 256 == 32:
                    # SPACE pressed
                    img_name = "opencv_frame_.png"
                    cv.imwrite(img_name, frame)

                    pixmap1 = QtGui.QPixmap(img_name)
                    w = self.original_image.width()
                    h = self.original_image.height()
                    self.original_image.setPixmap(pixmap1.scaled(w, h, Qt.KeepAspectRatio))
                    self.original_image.setAlignment(QtCore.Qt.AlignCenter)

                    print("{} written!".format(img_name))


            cam.release()

            cv.destroyAllWindows()
            print("clicked button is " + b.text())
        elif b.text() == 'Identify':

            if currently_selected_image_url == '':
                return;


            print("clicked button is " + b.text())
        elif b.text() == 'Save Image':
            print("clicked button is " + b.text())
        elif b.text() == 'Load Video':
            fileName = QFileDialog.getOpenFileName(None,
                                                   "Open Video", "",
                                                   "Video Files (*.avi *.flv *.wmv *.mov *.mp4)")
            print(fileName[0])
            vcap = cv.VideoCapture(fileName[0])
            res, im_ar = vcap.read()
            threshold = 0.7
            while im_ar.mean() < threshold and res:
                res, im_ar = vcap.read()
            img_name = "thumbnail_{}.png".format(0)
            cv.imwrite(img_name, im_ar)

            pixmap1 = QtGui.QPixmap(img_name)
            w = self.original_video.width()
            h = self.original_video.height()
            self.original_video.setPixmap(pixmap1.scaled(w, h, Qt.KeepAspectRatio))
            self.original_video.setAlignment(QtCore.Qt.AlignCenter)
            print("clicked button is " + b.text())
        elif b.text() == 'Capture Video from Webcam':
            cap = cv.VideoCapture(0)
            import cv2
            # Define the codec and create VideoWriter object
            frame_width = int(cap.get(3))
            frame_height = int(cap.get(4))
            out = cv.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20.0, (frame_width, frame_height))


            while (cap.isOpened()):
                ret, frame = cap.read()
                if ret == True:
                    frame = cv.flip(frame, 0)

                    # write the flipped frame
                    out.write(frame)

                    cv.imshow('frame', frame)
                    if cv.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            vcap = cv.VideoCapture('output.avi')
            res, im_ar = vcap.read()
            threshold = 0.7
            while im_ar.mean() < threshold and res:
                res, im_ar = vcap.read()
            img_name = "thumbnail_{}.png".format(0)
            cv.imwrite(img_name, im_ar)

            pixmap1 = QtGui.QPixmap(img_name)
            w = self.original_video.width()
            h = self.original_video.height()
            self.original_video.setPixmap(pixmap1.scaled(w, h, Qt.KeepAspectRatio))
            self.original_video.setAlignment(QtCore.Qt.AlignCenter)
            # Release everything if job is finished
            cap.release()
            out.release()
            cv.destroyAllWindows()
            print("clicked button is " + b.text())
        elif b.text() == 'Identify_2':
            print("clicked button is " + b.text())
        elif b.text() == 'Save Video':
            print("clicked button is " + b.text())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "A&G Identification"))
        self.ag_identification_image.setText(_translate("MainWindow", "A&G Identification"))
        self.identify.setText(_translate("MainWindow", "Identify"))
        self.load_image.setText(_translate("MainWindow", "Load Image"))
        self.age_identification_image.setText(_translate("MainWindow", "Age Identification"))
        self.capture_image.setText(_translate("MainWindow", "Capture Image from Webcam"))
        self.save_image.setText(_translate("MainWindow", "Save Image"))
        self.original_image.setText(_translate("MainWindow", "Origional Image"))
        self.gender_identification_image.setText(_translate("MainWindow", "Gender Identification"))
        self.converted_image.setText(_translate("MainWindow", "Converted Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Image Classification"))
        self.gender_identification_video.setText(_translate("MainWindow", "Gender Identification"))
        self.save_video.setText(_translate("MainWindow", "Save Video"))
        self.age_identification_video.setText(_translate("MainWindow", "Age Identification"))
        self.ag_identification_video.setText(_translate("MainWindow", "A&G Identification"))
        self.identify_2.setText(_translate("MainWindow", "Identify"))
        self.original_video.setText(_translate("MainWindow", "Preview Of Origional Video"))
        self.load_video.setText(_translate("MainWindow", "Load Video"))
        self.capture_video.setText(_translate("MainWindow", "Capture Video from Webcam"))
        self.converted_video.setText(_translate("MainWindow", "Preview Of Converted Video"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Video Classification"))

    def getFaceBox(net, frame, conf_threshold=0.7):
        frameOpencvDnn = frame.copy()
        frameHeight = frameOpencvDnn.shape[0]
        frameWidth = frameOpencvDnn.shape[1]
        blob = cv.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

        net.setInput(blob)
        detections = net.forward()
        bboxes = []
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > conf_threshold:
                x1 = int(detections[0, 0, i, 3] * frameWidth)
                y1 = int(detections[0, 0, i, 4] * frameHeight)
                x2 = int(detections[0, 0, i, 5] * frameWidth)
                y2 = int(detections[0, 0, i, 6] * frameHeight)
                bboxes.append([x1, y1, x2, y2])
                cv.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight / 150)), 8)
        return frameOpencvDnn, bboxes



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

