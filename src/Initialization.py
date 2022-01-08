import getmac

from requests import get
from PyQt5 import QtCore, QtGui, QtWidgets

def initValues(self):
    self.storeLocation = 1
    self.afterExec = 1
    self.languege = "kor"
    self.status = "start"
    self.ip = get("https://api.ipify.org").text
    self.mac = getmac.get_mac_address()
    self.sliderValue = 1

    _translate = QtCore.QCoreApplication.translate

    self.lb_pixmap.setText("")
    self.rd_one.setChecked(True)
    self.rd_none.setChecked(True)
    self.le_level_of_items.setText(_translate("MainWindow", "7"))
    self.le_stop_when_num_of_items.setText(_translate("MainWindow", "8"))
    self.lb_item1.setText(_translate("MainWindow", "0(100)"))
    self.lb_item2.setText(_translate("MainWindow", "0(100)"))
    self.lb_item3.setText(_translate("MainWindow", "0(100)"))
    self.lb_item5.setText(_translate("MainWindow", "0(100)"))
    self.lb_item7.setText(_translate("MainWindow", "0(100)"))
    self.lb_item4.setText(_translate("MainWindow", "0(100)"))
    self.lb_item6.setText(_translate("MainWindow", "0(100)"))
    self.lb_item8.setText(_translate("MainWindow", "0(100)"))
    self.lb_failure1.setText(_translate("MainWindow", "Lv1(0)"))
    self.lb_failure2.setText(_translate("MainWindow", "Lv2(0)"))
    self.lb_failure3.setText(_translate("MainWindow", "Lv3(0)"))
    self.lb_failure4.setText(_translate("MainWindow", "Lv4(0)"))
    self.lb_failure5.setText(_translate("MainWindow", "Lv5(0)"))
    self.lb_failure6.setText(_translate("MainWindow", "Lv6(0)"))
    self.lb_failure7.setText(_translate("MainWindow", "Lv7(0)"))

    self.setWindowTitle(_translate("MainWindow", "자동 개조 프로그램"))
    self.help.setWindowTitle(_translate("MainWindow", "도움말"))
    self.btn_stop.setText(_translate("MainWindow", "정지"))
    self.btn_start.setText(_translate("MainWindow", "시작"))
    self.lb_level_of_items.setText(_translate("MainWindow", "아이템 레벨"))
    self.lb_stop_when_num_of_items.setText(_translate("MainWindow", "아이템 개수"))
    self.gb_store_location.setTitle(_translate("MainWindow", "아이템 위치"))
    self.gb_after_exec.setTitle(_translate("MainWindow", "개조 완료 후 작업"))
    self.rd_one.setText(_translate("MainWindow", "1번"))
    self.rd_two.setText(_translate("MainWindow", "2번"))
    self.rd_three.setText(_translate("MainWindow", "3번"))
    self.rd_four.setText(_translate("MainWindow", "4번"))
    self.rd_five.setText(_translate("MainWindow", "5번"))
    self.rd_none.setText(_translate("MainWindow", "없음"))
    self.rd_exit.setText(_translate("MainWindow", "컴퓨터 종료"))
    self.btn_languege.setText(_translate("MainWindow", "언어 변경"))
    self.btn_help.setText(_translate("MainWindow", "도움말"))
    self.gb_trunk.setTitle(_translate("MainWindow", "인벤토리"))
    self.gb_failed.setTitle(_translate("MainWindow", "실패 수"))
    self.lb_bluestacks_name.setText(_translate("MainWindow", "블루스택 이름"))
    self.statusBar().showMessage(_translate("MainWindow", "주의: 블루스택 창을 최소화 하지마세요. & 화면보호기를 해제해주세요."))
    
def initLayout(self):
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("./resources/gaia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    self.setWindowIcon(icon)
    self.setGeometry(0, 0, 500, 355)
    self.btn_stop = QtWidgets.QPushButton(self)
    self.btn_stop.setGeometry(QtCore.QRect(400, 295, 80, 25))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    self.btn_stop.setFont(font)
    self.btn_stop.setObjectName("btn_stop")
    self.btn_stop.clicked.connect(self.btnStopClick)
    self.btn_start = QtWidgets.QPushButton(self)
    self.btn_start.setGeometry(QtCore.QRect(310, 295, 80, 25))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    self.btn_start.setFont(font)
    self.btn_start.setObjectName("btn_start")
    self.btn_start.clicked.connect(self.btnStartClick)
    self.lb_pixmap = QtWidgets.QLabel(self)
    self.lb_pixmap.setGeometry(QtCore.QRect(20, 20, 260, 100))
    self.lb_pixmap.setMouseTracking(False)
    self.lb_pixmap.setStyleSheet("border:1px solid black;")
    self.lb_pixmap.setWordWrap(False)
    self.lb_pixmap.setObjectName("lb_pixmap")
    self.lb_level_of_items = QtWidgets.QLabel(self)
    self.lb_level_of_items.setGeometry(QtCore.QRect(20, 170, 140, 20))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    self.lb_level_of_items.setFont(font)
    self.lb_level_of_items.setObjectName("lb_level_of_items")
    self.lb_stop_when_num_of_items = QtWidgets.QLabel(self)
    self.lb_stop_when_num_of_items.setGeometry(QtCore.QRect(20, 200, 140, 20))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    self.lb_stop_when_num_of_items.setFont(font)
    self.lb_stop_when_num_of_items.setObjectName("lb_stop_when_num_of_items")
    self.le_level_of_items = QtWidgets.QLineEdit(self)
    self.le_level_of_items.setGeometry(QtCore.QRect(190, 170, 90, 20))
    self.le_level_of_items.setObjectName("le_level_of_items")
    self.le_stop_when_num_of_items = QtWidgets.QLineEdit(self)
    self.le_stop_when_num_of_items.setGeometry(QtCore.QRect(190, 200, 90, 20))
    self.le_stop_when_num_of_items.setObjectName("le_stop_when_num_of_items")
    self.gb_store_location = QtWidgets.QGroupBox(self)
    self.gb_store_location.setGeometry(QtCore.QRect(15, 230, 270, 45))
    self.gb_after_exec = QtWidgets.QGroupBox(self)
    self.gb_after_exec.setGeometry(QtCore.QRect(15, 275, 270, 45))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    self.gb_store_location.setFont(font)
    self.gb_store_location.setObjectName("gb_store_location")
    self.gb_after_exec.setFont(font)
    self.gb_after_exec.setObjectName("gb_after_exec")
    self.rd_one = QtWidgets.QRadioButton(self.gb_store_location)
    self.rd_one.setGeometry(QtCore.QRect(20, 20, 50, 20))
    self.rd_one.setObjectName("rd_one")
    self.rd_one.clicked.connect(self.selectStoreLocation)
    self.rd_two = QtWidgets.QRadioButton(self.gb_store_location)
    self.rd_two.setGeometry(QtCore.QRect(70, 20, 50, 20))
    self.rd_two.setObjectName("rd_two")
    self.rd_two.clicked.connect(self.selectStoreLocation)
    self.rd_three = QtWidgets.QRadioButton(self.gb_store_location)
    self.rd_three.setGeometry(QtCore.QRect(120, 20, 50, 20))
    self.rd_three.setObjectName("rd_three")
    self.rd_three.clicked.connect(self.selectStoreLocation)
    self.rd_four = QtWidgets.QRadioButton(self.gb_store_location)
    self.rd_four.setGeometry(QtCore.QRect(170, 20, 50, 20))
    self.rd_four.setObjectName("rd_four")
    self.rd_four.clicked.connect(self.selectStoreLocation)
    self.rd_five = QtWidgets.QRadioButton(self.gb_store_location)
    self.rd_five.setGeometry(QtCore.QRect(220, 20, 50, 20))
    self.rd_five.setObjectName("rd_five")
    self.rd_five.clicked.connect(self.selectStoreLocation)
    self.rd_none = QtWidgets.QRadioButton(self.gb_after_exec)
    self.rd_none.setGeometry(QtCore.QRect(20, 20, 50, 20))
    self.rd_none.setObjectName("rd_none")
    self.rd_none.clicked.connect(self.selectAfterExec)
    self.rd_exit = QtWidgets.QRadioButton(self.gb_after_exec)
    self.rd_exit.setGeometry(QtCore.QRect(80, 20, 180, 20))
    self.rd_exit.setObjectName("rd_exit")
    self.rd_exit.clicked.connect(self.selectAfterExec)
    self.btn_languege = QtWidgets.QPushButton(self)
    self.btn_languege.setGeometry(QtCore.QRect(310, 265, 170, 25))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    self.btn_languege.setFont(font)
    self.btn_languege.setObjectName("btn_languege")
    self.btn_languege.clicked.connect(self.btnLanguegeClick)
    self.btn_help = QtWidgets.QPushButton(self)
    self.btn_help.setGeometry(QtCore.QRect(310, 235, 170, 25))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    self.btn_help.setFont(font)
    self.btn_help.setObjectName("btn_help")
    self.btn_help.clicked.connect(self.btnHelpClick)
    self.gb_trunk = QtWidgets.QGroupBox(self)
    self.gb_trunk.setGeometry(QtCore.QRect(310, 15, 100, 105))
    self.gb_trunk.setObjectName("gb_trunk")
    self.lb_item1 = QtWidgets.QLabel(self.gb_trunk)
    self.lb_item1.setGeometry(QtCore.QRect(10, 20, 40, 15))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    font.setBold(True)
    font.setWeight(75)
    self.lb_item1.setFont(font)
    self.lb_item1.setStyleSheet("color:#008000;")
    self.lb_item1.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.lb_item1.setAlignment(QtCore.Qt.AlignCenter)
    self.lb_item1.setObjectName("lb_item1")
    self.lb_item2 = QtWidgets.QLabel(self.gb_trunk)
    self.lb_item2.setGeometry(QtCore.QRect(50, 20, 40, 15))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    font.setBold(True)
    font.setWeight(75)
    self.lb_item2.setFont(font)
    self.lb_item2.setStyleSheet("color:#008000;")
    self.lb_item2.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.lb_item2.setAlignment(QtCore.Qt.AlignCenter)
    self.lb_item2.setObjectName("lb_item2")
    self.lb_item3 = QtWidgets.QLabel(self.gb_trunk)
    self.lb_item3.setGeometry(QtCore.QRect(10, 40, 40, 15))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    font.setBold(True)
    font.setWeight(75)
    self.lb_item3.setFont(font)
    self.lb_item3.setStyleSheet("color:#008000;")
    self.lb_item3.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.lb_item3.setAlignment(QtCore.Qt.AlignCenter)
    self.lb_item3.setObjectName("lb_item3")
    self.lb_item5 = QtWidgets.QLabel(self.gb_trunk)
    self.lb_item5.setGeometry(QtCore.QRect(10, 60, 40, 15))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    font.setBold(True)
    font.setWeight(75)
    self.lb_item5.setFont(font)
    self.lb_item5.setStyleSheet("color:#008000;")
    self.lb_item5.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.lb_item5.setAlignment(QtCore.Qt.AlignCenter)
    self.lb_item5.setObjectName("lb_item5")
    self.lb_item7 = QtWidgets.QLabel(self.gb_trunk)
    self.lb_item7.setGeometry(QtCore.QRect(10, 80, 40, 15))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    font.setBold(True)
    font.setWeight(75)
    self.lb_item7.setFont(font)
    self.lb_item7.setStyleSheet("color:#008000;")
    self.lb_item7.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.lb_item7.setAlignment(QtCore.Qt.AlignCenter)
    self.lb_item7.setObjectName("lb_item7")
    self.lb_item4 = QtWidgets.QLabel(self.gb_trunk)
    self.lb_item4.setGeometry(QtCore.QRect(50, 40, 40, 15))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    font.setBold(True)
    font.setWeight(75)
    self.lb_item4.setFont(font)
    self.lb_item4.setStyleSheet("color:#008000;")
    self.lb_item4.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.lb_item4.setAlignment(QtCore.Qt.AlignCenter)
    self.lb_item4.setObjectName("lb_item4")
    self.lb_item6 = QtWidgets.QLabel(self.gb_trunk)
    self.lb_item6.setGeometry(QtCore.QRect(50, 60, 40, 15))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    font.setBold(True)
    font.setWeight(75)
    self.lb_item6.setFont(font)
    self.lb_item6.setStyleSheet("color:#008000;")
    self.lb_item6.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.lb_item6.setAlignment(QtCore.Qt.AlignCenter)
    self.lb_item6.setObjectName("lb_item6")
    self.lb_item8 = QtWidgets.QLabel(self.gb_trunk)
    self.lb_item8.setGeometry(QtCore.QRect(50, 80, 40, 15))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    font.setBold(True)
    font.setWeight(75)
    self.lb_item8.setFont(font)
    self.lb_item8.setStyleSheet("color:#008000;")
    self.lb_item8.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.lb_item8.setAlignment(QtCore.Qt.AlignCenter)
    self.lb_item8.setObjectName("lb_item8")
    self.gb_failed = QtWidgets.QGroupBox(self)
    self.gb_failed.setGeometry(QtCore.QRect(420, 15, 70, 165))
    self.gb_failed.setObjectName("gb_failed")
    self.lb_failure1 = QtWidgets.QLabel(self.gb_failed)
    self.lb_failure1.setGeometry(QtCore.QRect(10, 20, 50, 15))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    font.setBold(True)
    font.setWeight(75)
    self.lb_failure1.setFont(font)
    self.lb_failure1.setStyleSheet("color:#ff0000;")
    self.lb_failure1.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.lb_failure1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
    self.lb_failure1.setObjectName("lb_failure1")
    self.lb_failure2 = QtWidgets.QLabel(self.gb_failed)
    self.lb_failure2.setGeometry(QtCore.QRect(10, 40, 50, 15))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    font.setBold(True)
    font.setWeight(75)
    self.lb_failure2.setFont(font)
    self.lb_failure2.setStyleSheet("color:#ff0000;")
    self.lb_failure2.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.lb_failure2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
    self.lb_failure2.setObjectName("lb_failure2")
    self.lb_failure3 = QtWidgets.QLabel(self.gb_failed)
    self.lb_failure3.setGeometry(QtCore.QRect(10, 60, 50, 15))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    font.setBold(True)
    font.setWeight(75)
    self.lb_failure3.setFont(font)
    self.lb_failure3.setStyleSheet("color:#ff0000;")
    self.lb_failure3.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.lb_failure3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
    self.lb_failure3.setObjectName("lb_failure3")
    self.lb_failure4 = QtWidgets.QLabel(self.gb_failed)
    self.lb_failure4.setGeometry(QtCore.QRect(10, 80, 50, 15))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    font.setBold(True)
    font.setWeight(75)
    self.lb_failure4.setFont(font)
    self.lb_failure4.setStyleSheet("color:#ff0000;")
    self.lb_failure4.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.lb_failure4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
    self.lb_failure4.setObjectName("lb_failure4")
    self.lb_failure5 = QtWidgets.QLabel(self.gb_failed)
    self.lb_failure5.setGeometry(QtCore.QRect(10, 100, 50, 15))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    font.setBold(True)
    font.setWeight(75)
    self.lb_failure5.setFont(font)
    self.lb_failure5.setStyleSheet("color:#ff0000;")
    self.lb_failure5.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.lb_failure5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
    self.lb_failure5.setObjectName("lb_failure5")
    self.lb_failure6 = QtWidgets.QLabel(self.gb_failed)
    self.lb_failure6.setGeometry(QtCore.QRect(10, 120, 50, 15))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    font.setBold(True)
    font.setWeight(75)
    self.lb_failure6.setFont(font)
    self.lb_failure6.setStyleSheet("color:#ff0000;")
    self.lb_failure6.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.lb_failure6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
    self.lb_failure6.setObjectName("lb_failure6")
    self.lb_failure7 = QtWidgets.QLabel(self.gb_failed)
    self.lb_failure7.setGeometry(QtCore.QRect(10, 140, 50, 15))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    font.setBold(True)
    font.setWeight(75)
    self.lb_failure7.setFont(font)
    self.lb_failure7.setStyleSheet("color:#ff0000;")
    self.lb_failure7.setFrameShape(QtWidgets.QFrame.NoFrame)
    self.lb_failure7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
    self.lb_failure7.setObjectName("lb_failure7")
    self.lb_bluestacks_name = QtWidgets.QLabel(self)
    self.lb_bluestacks_name.setGeometry(QtCore.QRect(20, 140, 140, 20))
    font = QtGui.QFont()
    font.setFamily("Malgun Gothic")
    self.lb_bluestacks_name.setFont(font)
    self.lb_bluestacks_name.setObjectName("lb_bluestacks_name")
    self.le_bluestacks_name = QtWidgets.QLineEdit(self)
    self.le_bluestacks_name.setGeometry(QtCore.QRect(190, 140, 90, 20))
    self.le_bluestacks_name.setObjectName("le_bluestacks_name")

    self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
    self.slider.setGeometry(QtCore.QRect(310, 140, 100, 20))
    self.slider.setObjectName("slider")
    self.slider.setRange(1, 5)
    self.slider.setTickInterval(1)
    self.slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
    self.slider.valueChanged.connect(self.sliderChange);

    self.help = QtWidgets.QDialog()
    self.help.resize(960, 515)
    self.help.lb_memo = QtWidgets.QLabel('블루스택 사이즈를 이 대화 상자와 동일하게 맞추어주세요!!!!!', self.help)
    self.help.lb_memo.setGeometry(QtCore.QRect(50, 50, 500, 20))
    self.help.lb_memo.setObjectName("help.lb_memo1")
    self.help.lb_writer = QtWidgets.QLabel('Shr.cell', self.help)
    self.help.lb_writer.setGeometry(QtCore.QRect(820, 460, 200, 20))
    self.help.lb_writer.setObjectName("help.lb_writer")
    self.help.lb_email = QtWidgets.QLabel('reinf92@naver.com', self.help)
    self.help.lb_email.setGeometry(QtCore.QRect(820, 480, 200, 20))
    self.help.lb_email.setObjectName("help.lb_email")
    
    self.items = [self.lb_item1, self.lb_item2, self.lb_item3, self.lb_item4, self.lb_item5, self.lb_item6, self.lb_item7, self.lb_item8]
    self.failures = [self.lb_failure1, self.lb_failure2, self.lb_failure3, self.lb_failure4, self.lb_failure5, self.lb_failure6, self.lb_failure7]