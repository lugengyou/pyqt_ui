'''
Author: gengyou.lu 1770591868@qq.com
Date: 2024-11-11 17:31:38
FilePath: /test/ui_designer/testUiMainWindow.py
LastEditTime: 2024-11-13 16:55:41
Description: 
'''
import sys
import socket
import json
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow,QWidget,QGraphicsScene
from .Ui_test import Ui_MainWindow  #导入你写的界面类
 
 
class MyMainWindow(QMainWindow,Ui_MainWindow): #这里也要记得改
    def __init__(self,parent =None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.textBrowser.append("Hey, guys! Welcome to tbps App!")
        self.s = None
        self.inferResult = None

    def connectServer(self):
        ip = self.lineEdit_ip.text()
        port = self.lineEdit_port.text()
        comboBoxText = self.comboBox.currentText()
        self.textBrowser.append(ip)
        self.textBrowser.append(port)
        self.textBrowser.append(comboBoxText) 
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((ip, int(port)))
            self.textBrowser.append("connect server success.") 
        except socket.error as msg:
            print(msg)                       

    def slot_sendMessage(self):
        if self.s == None:
            self.textBrowser.append("please connect server first.")
            return
        message = self.lineEdit_sendMessage.text()
        self.textBrowser.append(message)
        self.s.send(message.encode())
        self.textBrowser.append("send message success.")
        # 等待搜索结果
        response = self.s.recv(1024).decode()
        print(f'Received from server: {response}')
        self.inferResult = json.loads(response)

    def slot_showImage(self):
        self.textBrowser.append("show image")        
        image = QImage("dataset/CUHK-PEDES/0001001.png")
        self.scene = QGraphicsScene()
        self.scene.addPixmap(QPixmap.fromImage(image))
        self.graphicsView.setScene(self.scene)        
        self.graphicsView.show()
        self.label_id1.setText("id:")
        self.label_show_id1.setText("0001001")
        self.label_p1.setText("p:")
        self.label_show_p1.setText("0.99")

    def slot_clearShow(self):
        self.textBrowser.append("clear show")
        self.scene.clear()
        self.label_id1.clear()
        self.label_show_id1.clear()
        self.label_p1.clear()
        self.label_show_p1.clear()
