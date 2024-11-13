'''
Author: gengyou.lu 1770591868@qq.com
Date: 2024-11-11 17:31:38
FilePath: /test/test.py
LastEditTime: 2024-11-13 14:52:28
Description: test ui main program
'''
import sys
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QGraphicsScene
from ui_designer.testUiMainWindow import MyMainWindow  #导入你写的界面类
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())    
    