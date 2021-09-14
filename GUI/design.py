# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 650)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color: rgb(235, 255, 252);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.count = QtWidgets.QLabel(self.centralwidget)
        self.count.setGeometry(QtCore.QRect(0, 0, 50, 50))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        self.count.setFont(font)
        self.count.setStyleSheet("border-radius: 25px;\n"
"border: 1px solid #289591;")
        self.count.setText("")
        self.count.setAlignment(QtCore.Qt.AlignCenter)
        self.count.setObjectName("count")
        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.settings_button.setGeometry(QtCore.QRect(971, -1, 50, 50))
        self.settings_button.setStyleSheet("image: url(:/settings/settings.png);\n"
"border-radius: 30px;")
        self.settings_button.setText("")
        self.settings_button.setObjectName("settings_button")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 1024, 1))
        self.line.setStyleSheet("background-color: #000")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.addTab = QtWidgets.QPushButton(self.centralwidget)
        self.addTab.setGeometry(QtCore.QRect(55, 14, 34, 34))
        self.addTab.setStyleSheet("border-radius: 17px;\n"
"border: 1 px solid #000;\n"
"image: url(:/addTab/addTab.png);")
        self.addTab.setText("")
        self.addTab.setObjectName("addTab")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Parsing HTML"))
import source_rc
