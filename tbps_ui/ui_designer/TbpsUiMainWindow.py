'''
Author: gengyou.lu 1770591868@qq.com
Date: 2024-11-12 10:37:08
FilePath: /test/ui_designer/TbpsUiMainWindow.py
LastEditTime: 2024-11-13 11:46:13
Description: tbps ui 
'''
import sys
import json
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QGraphicsScene
from .Ui_tbps import Ui_MainWindow 


class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent =None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
        self.textBrowser_output.append("Hey, guys! Welcome to TBPS App!")        
        self.graphicsViewList = [self.graphicsView_1, self.graphicsView_2, self.graphicsView_3, 
                                 self.graphicsView_4, self.graphicsView_5, self.graphicsView_6, 
                                 self.graphicsView_7, self.graphicsView_8, self.graphicsView_9, self.graphicsView_10]
        self.displaySceneList = [QGraphicsScene() for i in range(10)]
        self.displayIdLabelList = [self.label_id1, self.label_id2, self.label_id3, self.label_id4, self.label_id5,
                                  self.label_id6, self.label_id7, self.label_id8, self.label_id9, self.label_id10]        
        self.displayShowIdList = [self.label_show_id1, self.label_show_id2, self.label_show_id3, self.label_show_id4, self.label_show_id5,
                                self.label_show_id6, self.label_show_id7, self.label_show_id8, self.label_show_id9, self.label_show_id10]
        self.displayProbLabelList = [self.label_p1, self.label_p2, self.label_p3, self.label_p4, self.label_p5,
                                    self.label_p6, self.label_p7, self.label_p8, self.label_p9, self.label_p10]
        self.displayShowProbList = [self.label_show_p1, self.label_show_p2, self.label_show_p3, self.label_show_p4, self.label_show_p5,
                                    self.label_show_p6, self.label_show_p7, self.label_show_p8, self.label_show_p9, self.label_show_p10]

    def slot_connectServer(self):
        ip = self.lineEdit_ip.text()
        port = self.lineEdit_port.text()        
        self.textBrowser_output.append("Connect to server ...")
        self.textBrowser_output.append(f"ip: {ip}")
        self.textBrowser_output.append(f"port: {port}")
        
    def slot_sclearInput(self):
        self.plainTextEdit_text.clear()
    
    def slot_search(self):        
        self.textBrowser_output.append("Search ...")
        self.textBrowser_output.append(f"input: {self.plainTextEdit_text.toPlainText()}")
        self.textBrowser_output.append(f"dataset: {self.comboBox_dataset.currentText()}")

    def slot_display(self):        
        seach_result = self.readJsonFile('result/seach_result.json')        
        if (len(seach_result) == 0):            
            return        
        display_setting = self.comboBox_display.currentText()
        if (display_setting == "Top1"):
            self.textBrowser_output.append("showing top1 result.")
            self.displayResultSample(seach_result, 1)
        elif (display_setting == "Top5"):
            self.textBrowser_output.append("showing top5 result.")
            self.displayResultSample(seach_result, 5)
        elif (display_setting == "Top10"):
            self.textBrowser_output.append("showing top10 result.")
            self.displayResultSample(seach_result, 10)
        else:
            self.textBrowser_output.append("clear display scene.")
            for i in range(10):
                self.displaySceneList[i].clear()
                self.displayIdLabelList[i].clear()
                self.displayShowIdList[i].clear()
                self.displayProbLabelList[i].clear()
                self.displayShowProbList[i].clear()


    # ************************ utils functions ************************ #
    def displayResultSample(self, seach_result, num):
        data = seach_result['search_result']
        for i in range(num):
            id = data[i]['id']
            prob = data[i]['probability']
            dataset = data[i]['dataset']
            filename = data[i]['filename']
            image_path = f"dataset/{dataset}/{filename}"
            image = QImage(image_path)
            self.displaySceneList[i].addPixmap(QPixmap.fromImage(image))
            self.graphicsViewList[i].setScene(self.displaySceneList[i])
            self.graphicsViewList[i].show()
            self.displayIdLabelList[i].setText("ID:")
            self.displayShowIdList[i].setText(str(id))
            self.displayProbLabelList[i].setText("Probability:")
            self.displayShowProbList[i].setText(str(prob))

    def readJsonFile(self, json_file):
        with open(json_file, 'r') as f:
            data = json.load(f)
        # self.textBrowser_output.append(json.dumps(data))
        if (len(data) == 0):
            self.textBrowser_output.append("No result found")            
        return data
