from PyQt5.QtWidgets import *

def initWindow(self):
    self.setWindowTitle('Astro-N Auto Tuner')
    self.setGeometry(1000,300,600,400)

    initTitle(self)
    initImageLable(self)
    initTextEdits(self)
    initRadioButtons(self) 
    initStatusLabels(self)
    initButton(self)


def initTitle(self):    
    self.title = QLabel('Astro-N Auto Tune Program', self)
    self.title.move(20, 25)
    self.title.resize(500,20)
    self.title.setStyleSheet('font-weight: bold; font-size:20px; font-family:Malgun Gothic;')


def initImageLable(self):  
    imgLabel = QLabel(self)
    imgLabel.move(20, 70)
    imgLabel.resize(300, 150)
    imgLabel.setStyleSheet("border:1px solid black;")


def initTextEdits(self):
    self.levelOfItems = QLabel('Level of items', self)
    self.levelOfItems.move(20, 250)
    self.levelOfItems.resize(500,20)

    self.stopWhenNumOfItems = QLabel('Stop when num of items', self)
    self.stopWhenNumOfItems.move(20, 280)
    self.stopWhenNumOfItems.resize(500,20)

    self.levelOfItemsValue = QLineEdit(self)
    self.levelOfItemsValue.move(200, 250)
    self.levelOfItemsValue.resize(70,20)
    self.levelOfItemsValue.setMaxLength(1)
    self.levelOfItemsValue.setText('7')
    self.levelOfItemsValue.setPlaceholderText("ex)7")
    
    self.stopWhenNumOfItemsValue = QLineEdit(self)
    self.stopWhenNumOfItemsValue.move(200, 280)
    self.stopWhenNumOfItemsValue.resize(70,20)
    self.stopWhenNumOfItemsValue.setMaxLength(1)
    self.stopWhenNumOfItemsValue.setText('8')
    self.stopWhenNumOfItemsValue.setPlaceholderText("ex)8")


def initRadioButtons(self):
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


def initStatusLabels(self):
    self.statusArea = QLabel('Status', self)
    self.statusArea.move(450, 20)
    self.statusArea.setStyleSheet("font-weight: bold; font-size:18px; font-family:Malgun Gothic;")

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
    self.btn1.move(370, 350)
    self.btn1.clicked.connect(self.btnStartClick)

    self.btn2 = QPushButton("Stop", self)
    self.btn2.move(480, 350)
    self.btn2.clicked.connect(self.btnStopClick)