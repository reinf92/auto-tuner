import sys
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
    
    def __del__(self):
        self.connect.close()

    def selectStoreLocation(self):
        setStoreLocation(self)

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

    def btnLanguegeClick(self):
        changeLanguege(self)

if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   ex = Application()
   ex.show()
   sys.exit(app.exec_())

