# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import background
import threading
from library import *
import os,Demo
import sys

f_stopMouseThread = False

class Ui_Form(object):
    filepath = None


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(831, 558)
        Form.setStyleSheet("background-image: url(:/background.png);")
        Form.setWindowIcon(QtGui.QIcon("images/birdIcon.png"))
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-10, 0, 841, 121))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-image: url(:/upbackground.png);")
        self.widget.setObjectName("widget")
        self.helpButton = QtWidgets.QPushButton(self.widget)
        self.helpButton.setGeometry(QtCore.QRect(730, 20, 81, 31))
        self.helpButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.helpButton.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(0, 170, 0);")
        self.helpButton.setObjectName("helpButton")
        self.aboutButton = QtWidgets.QPushButton(self.widget)
        self.aboutButton.setGeometry(QtCore.QRect(730, 60, 81, 31))
        self.aboutButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aboutButton.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(0, 170, 0);")
        self.aboutButton.setObjectName("aboutButton")
        self.tabButton1 = QtWidgets.QPushButton(self.widget)
        self.tabButton1.setGeometry(QtCore.QRect(70, 20, 71, 61))
        self.tabButton1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabButton1.setStyleSheet("border-image: url(:/homeIcon.png);\n"
"background: transparent;\n"
"")
        self.tabButton1.setText("")
        self.tabButton1.setObjectName("tabButton1")
        self.tabButton2 = QtWidgets.QPushButton(self.widget)
        self.tabButton2.setGeometry(QtCore.QRect(190, 20, 71, 61))
        self.tabButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabButton2.setStyleSheet("border-image: url(:/testIcon.png);\n"
"background: transparent;\n"
"")
        self.tabButton2.setText("")
        self.tabButton2.setObjectName("tabButton2")
        self.tabButton3 = QtWidgets.QPushButton(self.widget)
        self.tabButton3.setGeometry(QtCore.QRect(310, 20, 71, 61))
        self.tabButton3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabButton3.setStyleSheet("border-image: url(:/dynamicIcon.png);\n"
"background: transparent;\n"
"")
        self.tabButton3.setText("")
        self.tabButton3.setObjectName("tabButton3")
        self.tabButton4 = QtWidgets.QPushButton(self.widget)
        self.tabButton4.setGeometry(QtCore.QRect(430, 20, 71, 61))
        self.tabButton4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabButton4.setStyleSheet("border-image: url(:/staticIcon.png);\n"
"background: transparent;\n"
"")
        self.tabButton4.setText("")
        self.tabButton4.setObjectName("tabButton4")
        self.tabButton5 = QtWidgets.QPushButton(self.widget)
        self.tabButton5.setGeometry(QtCore.QRect(560, 20, 71, 61))
        self.tabButton5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabButton5.setStyleSheet("border-image: url(:/wordIcon.png);\n"
"background: transparent;\n"
"")
        self.tabButton5.setText("")
        self.tabButton5.setObjectName("tabButton5")
        self.downlabel1_2 = QtWidgets.QLabel(self.widget)
        self.downlabel1_2.setGeometry(QtCore.QRect(90, 90, 41, 31))
        self.downlabel1_2.setStyleSheet("background: transparent;\n"
"font: 12pt \"Adobe Devanagari\";\n"
"color: rgb(255, 255, 255);")
        self.downlabel1_2.setObjectName("downlabel1_2")
        self.downlabel1_3 = QtWidgets.QLabel(self.widget)
        self.downlabel1_3.setGeometry(QtCore.QRect(190, 90, 71, 31))
        self.downlabel1_3.setStyleSheet("background: transparent;\n"
"font: 12pt \"Adobe Devanagari\";\n"
"color: rgb(255, 255, 255);")
        self.downlabel1_3.setObjectName("downlabel1_3")
        self.downlabel1_4 = QtWidgets.QLabel(self.widget)
        self.downlabel1_4.setGeometry(QtCore.QRect(320, 90, 71, 31))
        self.downlabel1_4.setStyleSheet("background: transparent;\n"
"font: 12pt \"Adobe Devanagari\";\n"
"color: rgb(255, 255, 255);")
        self.downlabel1_4.setObjectName("downlabel1_4")
        self.downlabel1_5 = QtWidgets.QLabel(self.widget)
        self.downlabel1_5.setGeometry(QtCore.QRect(430, 90, 71, 31))
        self.downlabel1_5.setStyleSheet("background: transparent;\n"
"font: 12pt \"Adobe Devanagari\";\n"
"color: rgb(255, 255, 255);")
        self.downlabel1_5.setObjectName("downlabel1_5")
        self.downlabel1_6 = QtWidgets.QLabel(self.widget)
        self.downlabel1_6.setGeometry(QtCore.QRect(560, 90, 71, 31))
        self.downlabel1_6.setStyleSheet("background: transparent;\n"
"font: 12pt \"Adobe Devanagari\";\n"
"color: rgb(255, 255, 255);")
        self.downlabel1_6.setObjectName("downlabel1_6")
        self.lightLabel1 = QtWidgets.QLabel(self.widget)
        self.lightLabel1.setGeometry(QtCore.QRect(50, 60, 111, 61))
        self.lightLabel1.setStyleSheet("image: url(:/light.png);\n"
"background: transparent;")
        self.lightLabel1.setText("")
        self.lightLabel1.setObjectName("lightLabel1")
        self.lightLabel2 = QtWidgets.QLabel(self.widget)
        self.lightLabel2.setGeometry(QtCore.QRect(170, 60, 111, 61))
        self.lightLabel2.setStyleSheet("image: url(:/light.png);\n"
"background: transparent;")
        self.lightLabel2.setText("")
        self.lightLabel2.setObjectName("lightLabel2")
        self.lightLabel3 = QtWidgets.QLabel(self.widget)
        self.lightLabel3.setGeometry(QtCore.QRect(290, 60, 111, 61))
        self.lightLabel3.setStyleSheet("image: url(:/light.png);\n"
"background: transparent;")
        self.lightLabel3.setText("")
        self.lightLabel3.setObjectName("lightLabel3")
        self.lightLabel4 = QtWidgets.QLabel(self.widget)
        self.lightLabel4.setGeometry(QtCore.QRect(410, 60, 111, 61))
        self.lightLabel4.setStyleSheet("image: url(:/light.png);\n"
"background: transparent;")
        self.lightLabel4.setText("")
        self.lightLabel4.setObjectName("lightLabel4")
        self.lightLabel5 = QtWidgets.QLabel(self.widget)
        self.lightLabel5.setGeometry(QtCore.QRect(540, 60, 111, 61))
        self.lightLabel5.setStyleSheet("image: url(:/light.png);\n"
"background: transparent;")
        self.lightLabel5.setText("")
        self.lightLabel5.setObjectName("lightLabel5")
        self.lightLabel5.raise_()
        self.lightLabel4.raise_()
        self.lightLabel3.raise_()
        self.lightLabel2.raise_()
        self.lightLabel1.raise_()
        self.helpButton.raise_()
        self.aboutButton.raise_()
        self.tabButton1.raise_()
        self.tabButton2.raise_()
        self.tabButton3.raise_()
        self.tabButton4.raise_()
        self.tabButton5.raise_()
        self.downlabel1_2.raise_()
        self.downlabel1_3.raise_()
        self.downlabel1_4.raise_()
        self.downlabel1_5.raise_()
        self.downlabel1_6.raise_()
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 520, 831, 51))
        self.label.setStyleSheet("background-image: url(:/upbackground.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 100, 861, 431))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.openUrlButton = QtWidgets.QPushButton(self.page)
        self.openUrlButton.setGeometry(QtCore.QRect(620, 50, 75, 31))
        self.openUrlButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.openUrlButton.setObjectName("openUrlButton")
        self.urlTextEdit = QtWidgets.QTextEdit(self.page)
        self.urlTextEdit.setGeometry(QtCore.QRect(150, 50, 401, 31))
        self.urlTextEdit.setObjectName("urlTextEdit")
        self.wallLabel1 = QtWidgets.QLabel(self.page)
        self.wallLabel1.setGeometry(QtCore.QRect(300, 170, 91, 31))
        self.wallLabel1.setStyleSheet("background: transparent;\n"
"font: 14pt \"Microsoft YaHei UI\";")
        self.wallLabel1.setObjectName("wallLabel1")
        self.montorLabel2 = QtWidgets.QLabel(self.page)
        self.montorLabel2.setGeometry(QtCore.QRect(300, 290, 211, 21))
        self.montorLabel2.setStyleSheet("background: transparent;\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.montorLabel2.setObjectName("montorLabel2")
        self.montorLabelp = QtWidgets.QLabel(self.page)
        self.montorLabelp.setGeometry(QtCore.QRect(260, 250, 31, 31))
        self.montorLabelp.setStyleSheet("background-image: url(:/monitorIcon.png);")
        self.montorLabelp.setText("")
        self.montorLabelp.setObjectName("montorLabelp")
        self.mainLabel = QtWidgets.QLabel(self.page)
        self.mainLabel.setGeometry(QtCore.QRect(300, 110, 191, 51))
        self.mainLabel.setStyleSheet("background: transparent;\n"
"font: 75 18pt \"Microsoft YaHei UI\";")
        self.mainLabel.setObjectName("mainLabel")
        self.montorLabel1 = QtWidgets.QLabel(self.page)
        self.montorLabel1.setGeometry(QtCore.QRect(300, 250, 91, 31))
        self.montorLabel1.setStyleSheet("background: transparent;\n"
"font: 14pt \"Microsoft YaHei UI\";")
        self.montorLabel1.setObjectName("montorLabel1")
        self.reportLabel1 = QtWidgets.QLabel(self.page)
        self.reportLabel1.setGeometry(QtCore.QRect(300, 330, 91, 31))
        self.reportLabel1.setStyleSheet("background: transparent;\n"
"font: 14pt \"Microsoft YaHei UI\";")
        self.reportLabel1.setObjectName("reportLabel1")
        self.wallLabel2 = QtWidgets.QLabel(self.page)
        self.wallLabel2.setGeometry(QtCore.QRect(300, 210, 211, 21))
        self.wallLabel2.setStyleSheet("background: transparent;\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.wallLabel2.setObjectName("wallLabel2")
        self.wallLabelp = QtWidgets.QLabel(self.page)
        self.wallLabelp.setGeometry(QtCore.QRect(260, 170, 31, 31))
        self.wallLabelp.setStyleSheet("background-image: url(:/wallIcon.png);")
        self.wallLabelp.setText("")
        self.wallLabelp.setObjectName("wallLabelp")
        self.reportLabel2 = QtWidgets.QLabel(self.page)
        self.reportLabel2.setGeometry(QtCore.QRect(300, 370, 211, 21))
        self.reportLabel2.setStyleSheet("background: transparent;\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.reportLabel2.setObjectName("reportLabel2")
        self.reportLabelp = QtWidgets.QLabel(self.page)
        self.reportLabelp.setGeometry(QtCore.QRect(260, 330, 31, 31))
        self.reportLabelp.setStyleSheet("background-image: url(:/reportIcon.png);")
        self.reportLabelp.setText("")
        self.reportLabelp.setObjectName("reportLabelp")
        self.artLabelp = QtWidgets.QLabel(self.page)
        self.artLabelp.setGeometry(QtCore.QRect(550, 310, 221, 91))
        self.artLabelp.setStyleSheet("background-image: url(:/artword.png);")
        self.artLabelp.setText("")
        self.artLabelp.setObjectName("artLabelp")
        self.shieldLabelp = QtWidgets.QLabel(self.page)
        self.shieldLabelp.setGeometry(QtCore.QRect(30, 130, 201, 201))
        self.shieldLabelp.setStyleSheet("border-image: url(:/protectIcon.png);\n"
"background: transparent;")
        self.shieldLabelp.setText("")
        self.shieldLabelp.setObjectName("shieldLabelp")
        self.startButton = QtWidgets.QPushButton(self.page)
        self.startButton.setGeometry(QtCore.QRect(610, 130, 151, 71))
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startButton.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 22pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(0, 170, 0);")
        self.startButton.setObjectName("startButton")
        self.openUrlButton.raise_()
        self.urlTextEdit.raise_()
        self.wallLabel1.raise_()
        self.montorLabel2.raise_()
        self.montorLabelp.raise_()
        self.mainLabel.raise_()
        self.montorLabel1.raise_()
        self.reportLabel1.raise_()
        self.wallLabel2.raise_()
        self.wallLabelp.raise_()
        self.reportLabel2.raise_()
        self.reportLabelp.raise_()
        self.artLabelp.raise_()
        self.shieldLabelp.raise_()
        self.startButton.raise_()
        self.stackedWidget.addWidget(self.page)

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.plainTextEdit2 = QtWidgets.QPlainTextEdit(self.page_2)
        self.plainTextEdit2.setGeometry(QtCore.QRect(90, 80, 501, 321))
        self.plainTextEdit2.setStyleSheet("border-image: url(:/whitebackground.png);")
        self.plainTextEdit2.setObjectName("plainTextEdit2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(120, 30, 91, 31))
        self.label_2.setStyleSheet("background: transparent;\n"
                                   "font: 14pt \"Microsoft YaHei UI\";")
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.page_2)

        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.progressBar = QtWidgets.QProgressBar(self.page_3)
        self.progressBar.setGeometry(QtCore.QRect(90, 30, 501, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.showDataButton = QtWidgets.QPushButton(self.page_3)
        self.showDataButton.setGeometry(QtCore.QRect(610, 32, 91, 31))
        self.showDataButton.setStyleSheet("background: transparent;\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "font: 75 12pt \"Microsoft YaHei UI\";\n"
                                   "background-color: rgb(0, 170, 0);")
        self.showDataButton.setObjectName("showDataButton")
        self.plainTextEdit3 = QtWidgets.QPlainTextEdit(self.page_3)
        self.plainTextEdit3.setGeometry(QtCore.QRect(90, 80, 501, 321))
        self.plainTextEdit3.setStyleSheet("border-image: url(:/whitebackground.png);")
        self.plainTextEdit3.setObjectName("plainTextEdit3")
        self.webBtn1 = QtWidgets.QPushButton(self.page_3)
        self.webBtn1.setGeometry(QtCore.QRect(670, 160, 141, 31))
        self.webBtn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.webBtn1.setStyleSheet("background: transparent;\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "font: 75 12pt \"Microsoft YaHei UI\";\n"
                                   "background-color: rgb(0, 170, 0);")
        self.webBtn1.setObjectName("webBtn1")
        self.webBtn2 = QtWidgets.QPushButton(self.page_3)
        self.webBtn2.setGeometry(QtCore.QRect(670, 220, 141, 31))
        self.webBtn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.webBtn2.setStyleSheet("background: transparent;\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "font: 75 12pt \"Microsoft YaHei UI\";\n"
                                   "background-color: rgb(0, 170, 0);")
        self.webBtn2.setObjectName("webBtn2")
        self.webBtn3 = QtWidgets.QPushButton(self.page_3)
        self.webBtn3.setGeometry(QtCore.QRect(670, 280, 141, 31))
        self.webBtn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.webBtn3.setStyleSheet("background: transparent;\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "font: 75 12pt \"Microsoft YaHei UI\";\n"
                                   "background-color: rgb(0, 170, 0);")
        self.webBtn3.setObjectName("webBtn3")
        self.webBtn4 = QtWidgets.QPushButton(self.page_3)
        self.webBtn4.setGeometry(QtCore.QRect(670, 340, 141, 31))
        self.webBtn4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.webBtn4.setStyleSheet("background: transparent;\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "font: 75 12pt \"Microsoft YaHei UI\";\n"
                                   "background-color: rgb(0, 170, 0);")
        self.webBtn4.setObjectName("webBtn4")
        self.stackedWidget.addWidget(self.page_3)

        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.plainTextEdit4 = QtWidgets.QPlainTextEdit(self.page_4)
        self.plainTextEdit4.setGeometry(QtCore.QRect(120, 80, 471, 321))
        self.plainTextEdit4.setStyleSheet("border-image: url(:/whitebackground.png);")
        self.plainTextEdit4.setObjectName("plainTextEdit4")
        self.wallLabel1_2 = QtWidgets.QLabel(self.page_4)
        self.wallLabel1_2.setGeometry(QtCore.QRect(120, 30, 91, 31))
        self.wallLabel1_2.setStyleSheet("background: transparent;\n"
"font: 14pt \"Microsoft YaHei UI\";")
        self.wallLabel1_2.setObjectName("wallLabel1_2")
        self.shellingButton = QtWidgets.QPushButton(self.page_4)
        self.shellingButton.setGeometry(QtCore.QRect(680, 150, 111, 41))
        self.shellingButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.shellingButton.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 22pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(0, 170, 0);")
        self.shellingButton.setObjectName("shellingButton")
        self.testButton = QtWidgets.QPushButton(self.page_4)
        self.testButton.setGeometry(QtCore.QRect(680, 210, 111, 41))
        self.testButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.testButton.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 22pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(0, 170, 0);")
        self.testButton.setObjectName("testButton")
        self.analysisButton = QtWidgets.QPushButton(self.page_4)
        self.analysisButton.setGeometry(QtCore.QRect(680, 270, 111, 41))
        self.analysisButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.analysisButton.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 22pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(0, 170, 0);")
        self.analysisButton.setObjectName("analysisButton")
        self.lookReportButton = QtWidgets.QPushButton(self.page_4)
        self.lookReportButton.setGeometry(QtCore.QRect(680, 330, 111, 41))
        self.lookReportButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lookReportButton.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(0, 170, 0);")
        self.lookReportButton.setObjectName("lookReportButton")
        self.eyeLabel = QtWidgets.QLabel(self.page_4)
        self.eyeLabel.setGeometry(QtCore.QRect(690, 40, 91, 91))
        self.eyeLabel.setStyleSheet("border-image: url(:/staticIcon1.png);\n"
"background: transparent;")
        self.eyeLabel.setText("")
        self.eyeLabel.setObjectName("eyeLabel")

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.plainTextEdit5 = QtWidgets.QPlainTextEdit(self.page_5)
        self.plainTextEdit5.setGeometry(QtCore.QRect(90, 80, 471, 321))
        self.plainTextEdit5.setStyleSheet("border-image: url(:/whitebackground.png);")
        self.plainTextEdit5.setObjectName("plainTextEdit5")
        self.plainTextEdit6 = QtWidgets.QPlainTextEdit(self.page_5)
        self.plainTextEdit6.setGeometry(QtCore.QRect(630, 80, 151, 81))
        self.plainTextEdit6.setStyleSheet("border-image: url(:/whitebackground.png);")
        self.plainTextEdit6.setObjectName("plainTextEdit6")
        self.wallLabel1_4 = QtWidgets.QLabel(self.page_5)
        self.wallLabel1_4.setGeometry(QtCore.QRect(90, 30, 91, 31))
        self.wallLabel1_4.setStyleSheet("background: transparent;\n"
"font: 14pt \"Microsoft YaHei UI\";")
        self.wallLabel1_4.setObjectName("wallLabel1_4")

        self.stackedWidget.addWidget(self.page_5)
        self.downlabel1 = QtWidgets.QLabel(Form)
        self.downlabel1.setGeometry(QtCore.QRect(20, 530, 161, 21))
        self.downlabel1.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255);")
        self.downlabel1.setObjectName("downlabel1")
        self.updateButton = QtWidgets.QPushButton(Form)
        self.updateButton.setGeometry(QtCore.QRect(750, 530, 71, 20))
        self.updateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.updateButton.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font: 75 8pt \"Microsoft YaHei UI\";\n"
"background-color: rgb(0, 170, 0);")
        self.updateButton.setObjectName("updateButton")
        self.webBtn5 = QtWidgets.QPushButton(self.page_5)
        self.webBtn5.setGeometry(QtCore.QRect(640, 220, 141, 31))
        self.webBtn5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.webBtn5.setStyleSheet("background: transparent;\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "font: 75 12pt \"Microsoft YaHei UI\";\n"
                                   "background-color: rgb(0, 170, 0);")
        self.webBtn5.setObjectName("webBtn5")
        self.downlabel2 = QtWidgets.QLabel(Form)
        self.downlabel2.setGeometry(QtCore.QRect(190, 530, 161, 21))
        self.downlabel2.setStyleSheet("background: transparent;\n"
"color: rgb(255, 255, 255);")
        self.downlabel2.setObjectName("downlabel2")
        self.stackedWidget.raise_()
        self.widget.raise_()
        self.label.raise_()
        self.downlabel1.raise_()
        self.updateButton.raise_()
        self.downlabel2.raise_()
        self.lightLabel1.setVisible(True)
        self.lightLabel2.setVisible(False)
        self.lightLabel3.setVisible(False)
        self.lightLabel4.setVisible(False)
        self.lightLabel5.setVisible(False)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.choosedButton = 1

        #Mapping
        self.tabButton1.clicked.connect(self.StartTab1)
        self.tabButton2.clicked.connect(self.StartTab2)
        self.tabButton3.clicked.connect(self.StartTab3)
        self.tabButton4.clicked.connect(self.StartTab4)
        self.tabButton5.clicked.connect(self.StartTab5)
        self.tabButton5.clicked.connect(self.StartTab5)
        self.openUrlButton.clicked.connect(self.OpenUrl)
        self.startButton.clicked.connect(self.RunAnalyzer)
        self.webBtn1.clicked.connect(self.OpenWeb1)
        self.webBtn2.clicked.connect(self.OpenWeb2)
        self.webBtn3.clicked.connect(self.OpenWeb3)
        self.webBtn4.clicked.connect(self.OpenWeb4)
        self.webBtn5.clicked.connect(self.ShowGraph)
        self.StartMouseThread()



    def StartTab1(self):
        self.stackedWidget.setCurrentIndex(0)
        self.ChooseLightNum(1)

    def StartTab2(self):
        self.stackedWidget.setCurrentIndex(1)
        self.ChooseLightNum(2)
    def StartTab3(self):
        self.stackedWidget.setCurrentIndex(2)
        self.ChooseLightNum(3)
    def StartTab4(self):
        self.stackedWidget.setCurrentIndex(3)
        self.ChooseLightNum(4)
    def StartTab5(self):
        self.stackedWidget.setCurrentIndex(4)
        self.ChooseLightNum(5)
    def OpenUrl(self):
        getfile = QtWidgets.QFileDialog()
        self.filepath, filetype = getfile.getOpenFileNames(self,
                                                      "选择目标程序",
                                                      "C:/",
                                                      "aim program (*.exe)")
        self.urlTextEdit.setText(self.filepath[0])
    def RunAnalyzer(self):
        self.analyzerThread = AnalyzerThread(self)
        self.analyzerThread.start()
        self.stackedWidget.setCurrentIndex(2)
        self.ChooseLightNum(3)
    def OpenWeb1(self):
        os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://desktop-rtealdk:6006/#scalars&run=.')
    def OpenWeb2(self):
        os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://desktop-rtealdk:6006/#graphs&run=.')
    def OpenWeb3(self):
        os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://desktop-rtealdk:6006/#distributions&run=.')
    def OpenWeb4(self):
        os.system('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" http://desktop-rtealdk:6006/#histograms&run=.')
    def ShowGraph(self):
        Global.webWindow.show()

    def ChooseLightNum(self,num):
        if num == 1:
            self.lightLabel1.setVisible(True)
            self.lightLabel2.setVisible(False)
            self.lightLabel3.setVisible(False)
            self.lightLabel4.setVisible(False)
            self.lightLabel5.setVisible(False)
            self.choosedButton = 1
        if num == 2:
            self.lightLabel1.setVisible(False)
            self.lightLabel2.setVisible(True)
            self.lightLabel3.setVisible(False)
            self.lightLabel4.setVisible(False)
            self.lightLabel5.setVisible(False)
            self.choosedButton = 2
        if num == 3:
            self.lightLabel1.setVisible(False)
            self.lightLabel2.setVisible(False)
            self.lightLabel3.setVisible(True)
            self.lightLabel4.setVisible(False)
            self.lightLabel5.setVisible(False)
            self.choosedButton = 3
        if num == 4:
            self.lightLabel1.setVisible(False)
            self.lightLabel2.setVisible(False)
            self.lightLabel3.setVisible(False)
            self.lightLabel4.setVisible(True)
            self.lightLabel5.setVisible(False)
            self.choosedButton = 4
        if num == 5:
            self.lightLabel1.setVisible(False)
            self.lightLabel2.setVisible(False)
            self.lightLabel3.setVisible(False)
            self.lightLabel4.setVisible(False)
            self.lightLabel5.setVisible(True)
            self.choosedButton = 5

    def StartMouseThread(self):
        self.mouseThread = MouseThread(self)
        self.mouseThread.start()


    '''def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "BabyMal"))
        self.helpButton.setText(_translate("Form", "帮助"))
        self.aboutButton.setText(_translate("Form", "关于"))
        self.downlabel1_2.setText(_translate("Form", "主页"))
        self.downlabel1_3.setText(_translate("Form", "沙盒检测"))
        self.downlabel1_4.setText(_translate("Form", "动态分析"))
        self.downlabel1_5.setText(_translate("Form", "静态分析"))
        self.downlabel1_6.setText(_translate("Form", "检测报告"))
        self.openUrlButton.setText(_translate("Form", "选择程序"))
        self.wallLabel1.setText(_translate("Form", "隔离保护"))
        self.montorLabel2.setText(_translate("Form", "检测未知程序调用的API函数"))
        self.mainLabel.setText(_translate("Form", "检测未知程序"))
        self.montorLabel1.setText(_translate("Form", "监测检测"))
        self.reportLabel1.setText(_translate("Form", "生成报告"))
        self.wallLabel2.setText(_translate("Form", "避免计算机受到来自未知程序的伤害"))
        self.reportLabel2.setText(_translate("Form", "生成未知程序的测试报告"))
        self.startButton.setText(_translate("Form", "开始检测"))
        self.showDataButton.setText(_translate("Form", "显示信息"))
        self.label_2.setText(_translate("Form", "沙盒检测"))
        self.wallLabel1_2.setText(_translate("Form", "静态分析"))
        self.shellingButton.setText(_translate("Form", "脱壳"))
        self.testButton.setText(_translate("Form", "检测"))
        self.analysisButton.setText(_translate("Form", "分析"))
        self.lookReportButton.setText(_translate("Form", "查看报告"))
        self.webBtn1.setText(_translate("Form", "SCALARS"))
        self.webBtn2.setText(_translate("Form", "GRAPHS"))
        self.webBtn3.setText(_translate("Form", "DISTRIBUTIONS"))
        self.webBtn4.setText(_translate("Form", "HISTOGRAMS"))
        self.webBtn5.setText(_translate("Form", "显示神经网络"))
        self.wallLabel1_4.setText(_translate("Form", "检测报告"))
        self.downlabel1.setText(_translate("Form", "样本库更新：2018/4/13"))
        self.updateButton.setText(_translate("Form", "检查更新"))
        self.downlabel2.setText(_translate("Form", "已经更新到最新版本"))'''


class MainWindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint
                            |QtCore.Qt.WindowCloseButtonHint
                            |QtCore.Qt.MSWindowsFixedSizeDialogHint )        #no max,no change windows size
        self.setupUi(self)
    def closeEvent(self,event):
        global f_stopMouseThread
        f_stopMouseThread = True
        event.accept()

#create thread to do: if mouse in one titleButton,then this Button be light
class MouseThread (threading.Thread):

    def __init__(self, ui):
        threading.Thread.__init__(self)
        self.ui = ui

    def run(self):
        global f_stopMouseThread
        while not f_stopMouseThread:
            if self.ui.tabButton1.underMouse() == True:
                self.ui.lightLabel1.setVisible(True)
            elif(self.ui.choosedButton != 1):
                self.ui.lightLabel1.setVisible(False)
            if self.ui.tabButton2.underMouse() == True:
                self.ui.lightLabel2.setVisible(True)
            elif(self.ui.choosedButton != 2):
                self.ui.lightLabel2.setVisible(False)
            if self.ui.tabButton3.underMouse() == True:
                self.ui.lightLabel3.setVisible(True)
            elif(self.ui.choosedButton != 3):
                self.ui.lightLabel3.setVisible(False)
            if self.ui.tabButton4.underMouse() == True:
                self.ui.lightLabel4.setVisible(True)
            elif(self.ui.choosedButton != 4):
                self.ui.lightLabel4.setVisible(False)
            if self.ui.tabButton5.underMouse() == True:
                self.ui.lightLabel5.setVisible(True)
            elif(self.ui.choosedButton != 5):
                self.ui.lightLabel5.setVisible(False)

class AnalyzerThread (threading.Thread):

    def __init__(self, ui):
        threading.Thread.__init__(self)
        self.ui = ui

    def run(self):
        analyzer = Analyzer(self.ui.filepath[0])
        value, result = analyzer.dynamic_analyze
        value *= 100
        value = round(value,2)
        message = '该程序是恶意软件的概率为：{0}%'.format(value)

        #生成报告
        Demo.DoFilter('softsnoop/Demo/api.txt')
        self.ui.plainTextEdit6.setPlainText(message)
        self.ui.ChooseLightNum(5)
        self.ui.stackedWidget.setCurrentIndex(4)()
