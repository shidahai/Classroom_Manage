# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Teacher_change.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Teacher_change(object):
    def setupUi(self, Teacher_change):
        Teacher_change.setObjectName("Teacher_change")
        Teacher_change.resize(1040, 646)
        Teacher_change.setStyleSheet("background-image: url(:D:/PyQt/2.png);")
        self.label = QtWidgets.QLabel(Teacher_change)
        self.label.setGeometry(QtCore.QRect(390, 30, 661, 131))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Teacher_change)
        self.label_2.setGeometry(QtCore.QRect(580, 210, 211, 51))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Teacher_change)
        self.lineEdit.setGeometry(QtCore.QRect(710, 210, 251, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Teacher_change)
        self.label_3.setGeometry(QtCore.QRect(560, 290, 211, 51))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Teacher_change)
        self.pushButton.setGeometry(QtCore.QRect(710, 500, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Teacher_change)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 570, 171, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Teacher_change)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 570, 171, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(Teacher_change)
        self.label_4.setGeometry(QtCore.QRect(560, 360, 211, 51))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Teacher_change)
        self.label_5.setGeometry(QtCore.QRect(560, 430, 211, 51))
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(Teacher_change)
        self.lineEdit_2.setGeometry(QtCore.QRect(710, 290, 251, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Teacher_change)
        self.lineEdit_3.setGeometry(QtCore.QRect(710, 370, 251, 31))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_8 = QtWidgets.QLabel(Teacher_change)
        self.label_8.setGeometry(QtCore.QRect(90, 100, 241, 51))
        self.label_8.setObjectName("label_8")
        self.lineEdit_4 = QtWidgets.QLineEdit(Teacher_change)
        self.lineEdit_4.setGeometry(QtCore.QRect(710, 440, 251, 31))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_10 = QtWidgets.QLabel(Teacher_change)
        self.label_10.setGeometry(QtCore.QRect(90, 210, 211, 51))
        self.label_10.setObjectName("label_10")
        self.pushButton_4 = QtWidgets.QPushButton(Teacher_change)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 520, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textEdit = QtWidgets.QTextEdit(Teacher_change)
        self.textEdit.setGeometry(QtCore.QRect(90, 280, 371, 201))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.lineEdit_8 = QtWidgets.QLineEdit(Teacher_change)
        self.lineEdit_8.setGeometry(QtCore.QRect(90, 160, 251, 31))
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.retranslateUi(Teacher_change)
        QtCore.QMetaObject.connectSlotsByName(Teacher_change)

    def retranslateUi(self, Teacher_change):
        _translate = QtCore.QCoreApplication.translate
        Teacher_change.setWindowTitle(_translate("Teacher_change", "教师信息修改"))
        self.label.setText(_translate("Teacher_change", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#00aaff;\">教师信息修改</span></p></body></html>"))
        self.label_2.setText(_translate("Teacher_change", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aaff;\">教师号：</span></p></body></html>"))
        self.label_3.setText(_translate("Teacher_change", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aaff;\">教师姓名：</span></p></body></html>"))
        self.pushButton.setText(_translate("Teacher_change", "修改"))
        self.pushButton_2.setText(_translate("Teacher_change", "返回教师信息管理模块"))
        self.pushButton_3.setText(_translate("Teacher_change", "返回主菜单"))
        self.label_4.setText(_translate("Teacher_change", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aaff;\">所在院系：</span></p></body></html>"))
        self.label_5.setText(_translate("Teacher_change", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aaff;\">联系电话：</span></p></body></html>"))
        self.label_8.setText(_translate("Teacher_change", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aaff;\">请输入修改前的教师号：</span></p></body></html>"))
        self.label_10.setText(_translate("Teacher_change", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aaff;\">修改前的教师信息：</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Teacher_change", "查询"))
