'''
Author: gengyou.lu 1770591868@qq.com
Date: 2024-11-12 10:37:08
FilePath: /test/main.py
LastEditTime: 2024-11-13 11:45:53
Description: tbps ui main program
'''
import sys
from PyQt5.QtWidgets import QApplication
from ui_designer.TbpsUiMainWindow import MyMainWindow 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())

