import sys
from typing import Text
from Initialization import *
from Event import *
from PyQt5 import QtWidgets
from Runner import *

class Application(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        
        initLayout(self)
        initValues(self)
        layeredControl(self)

        if (self.ver != self.lastst_ver):
            QMessageBox.about(self, '안내', "<div><span>최신 버전 사용을 권장드립니다.</span><br><br><span>현재 버전 : "+self.ver+"</span><br><span>최신 버전 : <a href='" + self.lastst_ver_link + "'>"+self.lastst_ver+"</a></span></div>")
    
    def __del__(self):
        self.connect.close()

    def selectStoreLocation(self):
        setStoreLocation(self)

    def selectAfterExec(self):
        setAfterExec(self)

    def btnStartClick(self):
        if not self.le_bluestacks_name.text():
            QMessageBox.about(self, '안내', '블루스택 이름은 필수값입니다.')
        else:
            if (checkAuth(self)):
                layeredControl(self)
                self.le_bluestacks_name.setDisabled(True)
                self.runner = Runner(self)
                self.runner.start()
            else:
                QMessageBox.about(self, '안내', '등록되지 않은 사용자입니다.\nreinf92@naver.com로 문의주세요.')
        
    def btnStopClick(self):
        layeredControl(self)
        resetLables(self)
        self.runner.terminate()
        self.runner = None

    def btnHelpClick(self):
        showHelpBox(self)

    def btnVersionClick(self):
        showVersionBox(self)

    def btnLanguegeClick(self):
        changeLanguege(self)

    def sliderChange(self, value):
        self.sliderValue = value

if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   ex = Application()
   ex.show()
   sys.exit(app.exec_())

