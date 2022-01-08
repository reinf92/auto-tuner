from PyQt5 import QtCore
from Connect import *

def checkAuth(self):
    self.connect = Connect()
    data = self.connect.selectUser(self.ip, self.mac)

    if (data > 0):
        self.connect.insertUseHistory(self.ip, self.mac)
        self.connect.close()
        return True
    else:
        self.connect.insertNotAuthorized(self.ip, self.mac)
        self.connect.close()
        return False

def getLaststVersion(self):
    self.connect = Connect()
    data = self.connect.selectVersion()
    self.connect.close()
    return data

def showHelpBox(self):
    self.help.show()

def setStoreLocation(self):
    if self.rd_one.isChecked():
        self.storeLocation = 1
    elif self.rd_two.isChecked():
        self.storeLocation = 2
    elif self.rd_three.isChecked():
        self.storeLocation = 3
    elif self.rd_four.isChecked():
        self.storeLocation = 4
    elif self.rd_five.isChecked():
        self.storeLocation = 5

def setAfterExec(self):
    if self.rd_none.isChecked():
        self.afterExec = 1
    elif self.rd_exit.isChecked():
        self.afterExec = 2

def changeLanguege(self):
    _translate = QtCore.QCoreApplication.translate       
    if(self.languege == "kor"):
        self.setWindowTitle(_translate("MainWindow", "Auto Tune Program"))
        self.help.setWindowTitle(_translate("MainWindow", "Help"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.lb_level_of_items.setText(_translate("MainWindow", "Level of items"))
        self.lb_stop_when_num_of_items.setText(_translate("MainWindow", "Stop when num of items"))
        self.gb_store_location.setTitle(_translate("MainWindow", "Store Locations"))
        self.gb_after_exec.setTitle(_translate("MainWindow", "Workflow after tune"))
        self.rd_one.setText(_translate("MainWindow", "1st"))
        self.rd_two.setText(_translate("MainWindow", "2nd"))
        self.rd_three.setText(_translate("MainWindow", "3rd"))
        self.rd_four.setText(_translate("MainWindow", "4th"))
        self.rd_five.setText(_translate("MainWindow", "5th"))
        self.rd_none.setText(_translate("MainWindow", "None"))
        self.rd_exit.setText(_translate("MainWindow", "Shutdown the Computer"))
        self.btn_languege.setText(_translate("MainWindow", "Change Languege"))
        self.btn_help.setText(_translate("MainWindow", "Help"))
        self.gb_trunk.setTitle(_translate("MainWindow", "Trunk"))
        self.gb_failed.setTitle(_translate("MainWindow", "Failed"))
        self.lb_bluestacks_name.setText(_translate("MainWindow", "BlueStacks Name"))
        self.statusBar().showMessage(_translate("MainWindow", "Warning: Do not minimize the bluestacks. && Turn off the screen saver."))
        self.languege = None
    else:
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
        self.languege = "kor"

def layeredControl(self):
    if (self.status == "stop"):
        self.btn_start.setDisabled(True)
        self.btn_stop.setDisabled(False)
        self.btn_help.setDisabled(True)
        self.btn_languege.setDisabled(True)
        self.rd_one.setDisabled(True)
        self.rd_two.setDisabled(True)
        self.rd_three.setDisabled(True)
        self.rd_four.setDisabled(True)
        self.rd_five.setDisabled(True)
        self.le_level_of_items.setDisabled(True)
        self.le_stop_when_num_of_items.setDisabled(True)
        self.status = "start"
    else:
        self.btn_start.setDisabled(False)
        self.btn_stop.setDisabled(True)
        self.btn_help.setDisabled(False)
        self.btn_languege.setDisabled(False)
        self.rd_one.setDisabled(False)
        self.rd_two.setDisabled(False)
        self.rd_three.setDisabled(False)
        self.rd_four.setDisabled(False)
        self.rd_five.setDisabled(False)
        self.le_level_of_items.setDisabled(False)
        self.le_stop_when_num_of_items.setDisabled(False)
        self.status = "stop"

def resetLables(self):
    _translate = QtCore.QCoreApplication.translate   
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