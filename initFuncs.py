from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import *

def initWindow(self):
    self.setWindowTitle('Astro-N Auto Tune ^0^')
    self.setGeometry(0,0,600,360)
    self.statusBar().showMessage('Ready')
    self.radioValue = 1

    initTitle(self)
    initImageLable(self)
    initTextEdits(self)
    initRadioButtons(self) 
    initStatusLabels(self)
    initButton(self)
    initDialog(self)

def initDialog(self):
    self.dialog = QDialog()
    self.dialog.setWindowTitle('ReadMe')
    self.dialog.resize(955, 510)
    
    self.dialog.lable1 = QLabel('1. 프로그램 실행 시 블루스택 이름을 꼭 명시해야합니다.', self.dialog)
    self.dialog.lable1.move(50,50)

    self.dialog.lable2 = QLabel('2. 블루스택 사이즈를 ReadMe 대화 상자와 동일하게 맞추어주세요.', self.dialog)
    self.dialog.lable2.move(50,80)

    

    self.dialog.lable3 = QLabel('Shr.cell', self.dialog)
    self.dialog.lable3.move(820,460)

    self.dialog.lable4 = QLabel('reinf92@naver.com', self.dialog)
    self.dialog.lable4.move(820,480)

def initTitle(self):    
    self.title = QLabel('Astro-N Auto Tune Program', self)
    self.title.move(20, 25)
    self.title.resize(500,20)
    self.title.setStyleSheet('font-weight: bold; font-size:20px; font-family:Malgun Gothic;')


def initImageLable(self):  
    self.imgLabel = QLabel(self)
    self.imgLabel.move(20, 70)
    self.imgLabel.resize(300, 120)
    self.imgLabel.setStyleSheet("border:1px solid black;")


def initTextEdits(self):
    self.levelOfItems = QLabel('Level of items', self)
    self.levelOfItems.move(20, 210)
    self.levelOfItems.resize(500,20)

    self.stopWhenNumOfItems = QLabel('Stop when num of items', self)
    self.stopWhenNumOfItems.move(20, 240)
    self.stopWhenNumOfItems.resize(500,20)

    self.levelOfItemsValue = QLineEdit(self)
    self.levelOfItemsValue.move(200, 210)
    self.levelOfItemsValue.resize(70,20)
    self.levelOfItemsValue.setMaxLength(1)
    self.levelOfItemsValue.setText('7')
    self.levelOfItemsValue.setPlaceholderText("ex)7")
    
    self.stopWhenNumOfItemsValue = QLineEdit(self)
    self.stopWhenNumOfItemsValue.move(200, 240)
    self.stopWhenNumOfItemsValue.resize(70,20)
    self.stopWhenNumOfItemsValue.setMaxLength(1)
    self.stopWhenNumOfItemsValue.setText('8')
    self.stopWhenNumOfItemsValue.setPlaceholderText("ex)8")


def initRadioButtons(self):
    self.groupBox = QGroupBox('Location', self)
    self.groupBox.move(10, 290)
    self.groupBox.resize(310, 50)

    self.radio1 = QRadioButton('1st', self);
    self.radio1.move(20, 305)
    self.radio1.setChecked(True)
    self.radio1.clicked.connect(self.radioButtonClicked)

    self.radio2 = QRadioButton('2nd', self);
    self.radio2.move(80, 305)
    self.radio2.clicked.connect(self.radioButtonClicked)

    self.radio3 = QRadioButton('3rd', self);
    self.radio3.move(140, 305)
    self.radio3.clicked.connect(self.radioButtonClicked)

    self.radio4 = QRadioButton('4th', self);
    self.radio4.move(200, 305)
    self.radio4.clicked.connect(self.radioButtonClicked)

    self.radio5 = QRadioButton('5th', self);
    self.radio5.move(260, 305)
    self.radio5.clicked.connect(self.radioButtonClicked)

    
def initStatusLabels(self):
    self.inventoryArea = QLabel('Inventory', self)
    self.inventoryArea.move(380, 20)
    self.inventoryArea.setStyleSheet("font-weight: bold; font-size:18px; font-family:Malgun Gothic;")

    self.failedArea = QLabel('Failed', self)
    self.failedArea.move(500, 20)
    self.failedArea.setStyleSheet("font-weight: bold; font-size:18px; font-family:Malgun Gothic;")

    initItemLabels(self)
    initFailedLabels(self)


def initItemLabels(self):
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


def initFailedLabels(self):  
    self.failed1 = QLabel('v1(0)', self)
    self.failed1.move(485, 60)
    self.failed1.setStyleSheet("color: RED; font-weight: bold;")
    
    self.failed2 = QLabel('v2(0)', self)
    self.failed2.move(535, 60)
    self.failed2.setStyleSheet("color: RED; font-weight: bold;")

    self.failed3 = QLabel('v3(0)', self)
    self.failed3.move(485, 90)
    self.failed3.setStyleSheet("color: RED; font-weight: bold;")

    self.failed4 = QLabel('v4(0)', self)
    self.failed4.move(535, 90)
    self.failed4.setStyleSheet("color: RED; font-weight: bold;")
    
    self.failed5 = QLabel('v5(0)', self)
    self.failed5.move(485, 120)
    self.failed5.setStyleSheet("color: RED; font-weight: bold;")

    self.failed6 = QLabel('v6(0)', self)
    self.failed6.move(535, 120)
    self.failed6.setStyleSheet("color: RED; font-weight: bold;")

    self.failed7 = QLabel('v7(0)', self)
    self.failed7.move(485, 150)
    self.failed7.setStyleSheet("color: RED; font-weight: bold;")


def initButton(self):
    self.btn1 = QPushButton("Start", self)
    self.btn1.move(370, 310)
    self.btn1.clicked.connect(self.btnStartClick)

    self.btn2 = QPushButton("Stop", self)
    self.btn2.move(480, 310)
    self.btn2.clicked.connect(self.btnStopClick)
    self.btn2.setDisabled(True)

    self.btn3 = QPushButton("ReadMe", self)
    self.btn3.move(370, 210)
    self.btn3.resize(210, 60)
    self.btn3.clicked.connect(self.btnReadMeClick)