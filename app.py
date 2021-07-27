import sys
from PyQt5.QtGui import QTextLine
from PyQt5.QtWidgets import *

import Item

class MyApp(QMainWindow):

    location = 1;
    item = [Item.Item, Item.Item, Item.Item, Item.Item, Item.Item, Item.Item, Item.Item, Item.Item]

    def __init__(self):
        super().__init__()
        self.initUI()
        
        

    def initUI(self):
        self.setWindowTitle('Astro-N Auto Tuner')
        self.setGeometry(500,300,600,400)
        
        self.initTitle()
        self.initRadio()
        self.initButton()

        

        self.show()

    def initTitle(self):
        title = QLabel('Astro-N Auto Tune Program', self)
        title.move(20, 20)
        title.resize(500,20)
        font = title.font()
        font.setPointSize(15)
        font.setBold(True)
        font.setFamily('Malgun Gothic')
        title.setFont(font)

        self.levelOfItems = QLabel('Level of items', self)
        self.levelOfItems.move(20, 250)
        self.levelOfItems.resize(500,20)

        self.stopWhenNumOfItems = QLabel('Stop when num of items', self)
        self.stopWhenNumOfItems.move(20, 280)
        self.stopWhenNumOfItems.resize(500,20)
        
        #QInputDialog.getInt(self, '매수 수량', '매수 수량을 입력하세요.')

        self.item1 = QLabel('0(100)', self)
        self.item1.move(375, 60)
        self.item1.setStyleSheet("color: #009900; font-weight: bold;")
        
        self.item2 = QLabel('0(100)', self)
        self.item2.move(425, 60)
        self.item2.setStyleSheet("color: #009900; font-weight: bold;")

        self.item3 = QLabel('0(100)', self)
        self.item3.move(375, 90)
        self.item3.setStyleSheet("color: #009900; font-weight: bold;")

        self.item4 = QLabel('0(100)', self)
        self.item4.move(425, 90)
        self.item4.setStyleSheet("color: #009900; font-weight: bold;")
        
        self.item5 = QLabel('0(100)', self)
        self.item5.move(375, 120)
        self.item5.setStyleSheet("color: #009900; font-weight: bold;")

        self.item6 = QLabel('0(100)', self)
        self.item6.move(425, 120)
        self.item6.setStyleSheet("color: #009900; font-weight: bold;")

        self.item7 = QLabel('0(100)', self)
        self.item7.move(375, 150)
        self.item7.setStyleSheet("color: #009900; font-weight: bold;")

        self.item8 = QLabel('0(100)', self)
        self.item8.move(425, 150)
        self.item8.setStyleSheet("color: #009900; font-weight: bold;")

    def initRadio(self):
        self.groupBox = QGroupBox('Location', self)
        self.groupBox.move(10, 330)
        self.groupBox.resize(260, 50)

        self.radio1 = QRadioButton('1st', self);
        self.radio1.move(20, 345)
        self.radio1.setChecked(True)
        self.radio1.clicked.connect(self.radioButtonClicked)

        self.radio2 = QRadioButton('2nd', self);
        self.radio2.move(70, 345)
        self.radio2.clicked.connect(self.radioButtonClicked)

        self.radio3 = QRadioButton('3rd', self);
        self.radio3.move(120, 345)
        self.radio3.clicked.connect(self.radioButtonClicked)

        self.radio4 = QRadioButton('4th', self);
        self.radio4.move(170, 345)
        self.radio4.clicked.connect(self.radioButtonClicked)

        self.radio5 = QRadioButton('5th', self);
        self.radio5.move(220, 345)
        self.radio5.clicked.connect(self.radioButtonClicked)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)
    
    def radioButtonClicked(self):

        msg = ""
        if self.radio1.isChecked():
            msg = "1"
        elif self.radio2.isChecked():
            msg = "2"
        elif self.radio3.isChecked():
            msg = "3"
        elif self.radio4.isChecked():
            msg = "4"
        else:
            msg = "5"
        self.statusBar.showMessage(msg + "선택 됨")

    def initButton(self):
        self.btn1 = QPushButton("Start", self)
        self.btn1.move(370, 350)
        self.btn1.clicked.connect(self.btnStartClick)

        self.btn2 = QPushButton("Stop", self)
        self.btn2.move(480, 350)
        self.btn2.clicked.connect(self.btnStopClick)

    def btnStartClick(self):
        QMessageBox.about(self, "start", "clicked")

    def btnStopClick(self):
        QMessageBox.about(self, "stop", "clicked")

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   ex.show()
   sys.exit(app.exec_())

