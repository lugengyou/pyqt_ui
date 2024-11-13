# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/userdata/PyQt/test/ui_designer/test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(947, 792)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_server = QtWidgets.QFrame(self.centralwidget)
        self.frame_server.setGeometry(QtCore.QRect(170, 120, 145, 101))
        self.frame_server.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_server.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_server.setObjectName("frame_server")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_server)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_ip = QtWidgets.QLineEdit(self.frame_server)
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.verticalLayout.addWidget(self.lineEdit_ip)
        self.lineEdit_port = QtWidgets.QLineEdit(self.frame_server)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.verticalLayout.addWidget(self.lineEdit_port)
        self.pushButton_connect = QtWidgets.QPushButton(self.frame_server)
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.verticalLayout.addWidget(self.pushButton_connect)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 240, 79, 23))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 140, 80, 23))
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(350, 110, 131, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(500, 110, 91, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_id1 = QtWidgets.QLabel(self.frame)
        self.label_id1.setStyleSheet("")
        self.label_id1.setText("")
        self.label_id1.setTextFormat(QtCore.Qt.RichText)
        self.label_id1.setScaledContents(False)
        self.label_id1.setWordWrap(False)
        self.label_id1.setTextInteractionFlags(QtCore.Qt.TextEditable)
        self.label_id1.setObjectName("label_id1")
        self.verticalLayout_2.addWidget(self.label_id1)
        self.label_show_id1 = QtWidgets.QLabel(self.frame)
        self.label_show_id1.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_show_id1.setText("")
        self.label_show_id1.setObjectName("label_show_id1")
        self.verticalLayout_2.addWidget(self.label_show_id1)
        self.label_p1 = QtWidgets.QLabel(self.frame)
        self.label_p1.setText("")
        self.label_p1.setObjectName("label_p1")
        self.verticalLayout_2.addWidget(self.label_p1)
        self.label_show_p1 = QtWidgets.QLabel(self.frame)
        self.label_show_p1.setText("")
        self.label_show_p1.setObjectName("label_show_p1")
        self.verticalLayout_2.addWidget(self.label_show_p1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(160, 370, 571, 101))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(620, 200, 80, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 320, 80, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_sendMessage = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sendMessage.setGeometry(QtCore.QRect(260, 320, 461, 23))
        self.lineEdit_sendMessage.setObjectName("lineEdit_sendMessage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 947, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.pushButton_connect.clicked.connect(MainWindow.connectServer) # type: ignore
        self.pushButton.clicked.connect(MainWindow.slot_showImage) # type: ignore
        self.pushButton_2.clicked.connect(MainWindow.slot_clearShow) # type: ignore
        self.pushButton_3.clicked.connect(MainWindow.slot_sendMessage) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_ip.setText(_translate("MainWindow", "172.168.3.70"))
        self.lineEdit_port.setText(_translate("MainWindow", "6661"))
        self.pushButton_connect.setText(_translate("MainWindow", "connect"))
        self.comboBox.setItemText(0, _translate("MainWindow", "s1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "s2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "s3"))
        self.pushButton.setText(_translate("MainWindow", "show"))
        self.pushButton_2.setText(_translate("MainWindow", "clear"))
        self.pushButton_3.setText(_translate("MainWindow", "send"))
