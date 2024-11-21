'''
Author: gengyou.lu 1770591868@qq.com
Date: 2024-11-12 10:37:08
FilePath: /tbps_ui/ui_designer/TbpsUiMainWindow.py
LastEditTime: 2024-11-21 14:28:38
Description: tbps ui 
'''
import os
import json
import socket
import shutil
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
        self.clientSocket = None
        self.inferResult = None
        self.currentShow = None

    def slot_connectServer(self):
        ip = self.lineEdit_ip.text()
        port = self.lineEdit_port.text()        
        self.textBrowser_output.append("Connect to server ...")
        self.textBrowser_output.append(f"ip: {ip}")
        self.textBrowser_output.append(f"port: {port}")
        try:
            self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientSocket.connect((ip, int(port)))
            self.textBrowser_output.append("connect server success.") 
        except socket.error as msg:
            self.textBrowser_output.append(str(msg))            

    def slot_clearInput(self):
        self.plainTextEdit_text.clear()

    def slot_clearOutput(self):
        self.textBrowser_output.clear()
    
    def slot_search(self):  
        try:                        
            self.textBrowser_output.append("Search ...")
            self.textBrowser_output.append(f"input: {self.plainTextEdit_text.toPlainText()}")
            self.textBrowser_output.append(f"dataset: {self.comboBox_dataset.currentText()}")
            # 发送搜索请求 json 数据
            message = {"input": self.plainTextEdit_text.toPlainText(), "dataset": self.comboBox_dataset.currentText()}
            message = json.dumps(message)        
            self.send_message_to_server(self.clientSocket, message.encode())
            self.textBrowser_output.append("send message success.")
            # 等待搜索结果        
            self.receiveAndSaveResult()
        except:
            self.textBrowser_output.append("Please connect to server first!")

    def slot_display(self):        
        # 获取显示设置
        display_setting = self.comboBox_display.currentText()
        display_history = self.comboBox_history.currentText()        
        # 清空显示
        self.clearDisplayScene()
        # 显示搜索结果
        if (display_setting == "Top1"):
            self.textBrowser_output.append("showing top1 result.")
            self.displayResultSample(1, display_history)
        elif (display_setting == "Top5"):
            self.textBrowser_output.append("showing top5 result.")
            self.displayResultSample(5, display_history)
        elif (display_setting == "Top10"):
            self.textBrowser_output.append("showing top10 result.")
            self.displayResultSample(10, display_history)
        else:
            self.textBrowser_output.append("clear display scene.")
            
    # ************************ utils functions ************************ #
    def clearDisplayScene(self): 
        # 清空显示                         
        for i in range(10):
            self.displaySceneList[i].clear()
            self.displayIdLabelList[i].clear()
            self.displayShowIdList[i].clear()
            self.displayProbLabelList[i].clear()
            self.displayShowProbList[i].clear()

    def displayResultSample(self, num, display_history):  
        # 判断是否有搜索结果
        save_folder = f"search_result/{display_history}"
        if not os.path.exists(save_folder):
            self.clearDisplayScene()
            self.textBrowser_output.append("No result found")
            return
        # 如果当前显示的历史记录不是当前选择的历史记录，则重新读取json文件
        if self.currentShow != display_history:
            self.inferResult = self.readJsonFile(f"search_result/{display_history}/search_result.json")
        self.currentShow = display_history        
        # 显示搜索结果
        data = self.inferResult['search_result']
        input = self.inferResult['input']
        self.textBrowser_currentDisplayInput.clear()
        self.textBrowser_currentDisplayInput.append(input)
        for i in range(num):
            id = data[i]['id']            
            prob = data[i]['similarity']
            dataset = data[i]['dataset']
            filename = data[i]['filename']
            image_path = f"{save_folder}/{dataset}/{filename}"
            image = QImage(image_path)
            self.displaySceneList[i].addPixmap(QPixmap.fromImage(image))
            self.graphicsViewList[i].setScene(self.displaySceneList[i])
            self.graphicsViewList[i].show()
            self.displayIdLabelList[i].setText("ID:")
            self.displayShowIdList[i].setText(str(id))
            self.displayProbLabelList[i].setText("Similarity:")
            self.displayShowProbList[i].setText(str(prob))

    def readJsonFile(self, json_file):
        # 读取 json 文件
        with open(json_file, 'r') as f:
            data = json.load(f)        
        if (len(data) == 0):
            self.textBrowser_output.append("No result found")            
        return data

    def receiveAndSaveResult(self):
        try:
            # 接收 json 检索结果                                
            response = self.receive_message(self.clientSocket).decode()                         
            if not response:
                self.textBrowser_output.append("Received empty response")
                return                 
            # 解析 json 数据
            try:
                json_result = json.loads(response)
                self.currentShow = "current"
                self.inferResult = json_result
            except json.JSONDecodeError as e:
                self.textBrowser_output.append(f"JSON decode error: {str(e)}")
                return

            data = json_result['search_result']  
            
            save_folder = "search_result/current"
            # 修改历史记录文件夹名
            if os.path.exists(save_folder):                                    
                for i in range(6, 1, -1):
                    old_name = f"search_result/last_{i-1}"
                    new_name = f"search_result/last_{i}"
                    if os.path.exists("search_result/last_6"):
                        # 删除最早的历史记录
                        shutil.rmtree("search_result/last_6")
                    if os.path.exists(old_name):
                        os.rename(old_name, new_name)
                os.rename("search_result/current", "search_result/last_1")                         
            
            # 创建存储当前搜索结果文件夹                   
            save_folder = f"search_result/current/{data[0]['dataset']}"
            os.makedirs(save_folder)                            
            # 保存 json 数据
            with open(f"search_result/current/search_result.json", 'w') as f:
                json.dump(json_result, f, indent=4, ensure_ascii=False)
            # 接收图片数据并保存
            for i in range(10):
                # Receive the size of the image
                image_size_data = self.clientSocket.recv(4)
                if not image_size_data:
                    break
                image_size = int.from_bytes(image_size_data, 'big')
                # Receive the image data
                image_data = b''
                while len(image_data) < image_size:
                    packet = self.clientSocket.recv(image_size - len(image_data))
                    if not packet:
                        break
                    image_data += packet
                # Save the image to the specified folder
                filename = data[i]['filename']
                image_path = os.path.join(save_folder, filename)                
                os.makedirs(os.path.dirname(image_path), exist_ok=True) # 确保存储目录存在
                with open(image_path, 'wb') as img_file:
                    img_file.write(image_data)  

        except Exception as e:
            self.textBrowser_output.append(f"Error receiving data: {str(e)}")
            self.textBrowser_output.append(f"Please connect to the server again.")    

    def send_message_to_server(self, client_socket, message):
        # message 为字符串信息，先发送信息长度，再发送信息
        client_socket.sendall(len(message).to_bytes(4, 'big'))  # Send the size of the image
        client_socket.sendall(message)

    def receive_message(self, client_socket):
        # 接收 message 信息，先接收信息长度，再接收信息
        message_size_data = client_socket.recv(4)
        message_size = int.from_bytes(message_size_data, 'big')
        message_data = b''
        while len(message_data) < message_size:
            packet = client_socket.recv(message_size - len(message_data))
            if not packet:
                break
            message_data += packet
        return message_data

