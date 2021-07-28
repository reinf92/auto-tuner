import sys
import runner

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from initFuncs import *

class Application(QMainWindow):

    def __init__(self):
        super().__init__()
        initWindow(self)
        self.name = 'Blank'
        self.runner = runner.Runner(self)
        self.showDialog()
        self.setWindowIcon(QIcon("gaia.png"))
        
    def radioButtonClicked(self):     
        if self.radio1.isChecked():
            self.radioValue = 1
            self.statusBar().showMessage('Select the 1st item')
        elif self.radio2.isChecked():
            self.radioValue = 2
            self.statusBar().showMessage('Select the 2nd item')
        elif self.radio3.isChecked():
            self.radioValue = 3
            self.statusBar().showMessage('Select the 3rd item')
        elif self.radio4.isChecked():
            self.radioValue = 4
            self.statusBar().showMessage('Select the 4th item')
        else:
            self.radioValue = 5
            self.statusBar().showMessage('Select the 5th item')

    def btnStartClick(self):
        self.btn1.setDisabled(True)
        self.btn2.setDisabled(False)
        self.btn3.setDisabled(True)
        self.radio1.setDisabled(True)
        self.radio2.setDisabled(True)
        self.radio3.setDisabled(True)
        self.radio4.setDisabled(True)
        self.radio5.setDisabled(True)
        self.levelOfItemsValue.setDisabled(True)
        self.stopWhenNumOfItemsValue.setDisabled(True)
        self.runner.start()

    def btnStopClick(self):
        self.btn1.setDisabled(False)
        self.btn2.setDisabled(True)
        self.btn3.setDisabled(False)
        self.radio1.setDisabled(False)
        self.radio2.setDisabled(False)
        self.radio3.setDisabled(False)
        self.radio4.setDisabled(False)
        self.radio5.setDisabled(False)
        self.levelOfItemsValue.setDisabled(False)
        self.stopWhenNumOfItemsValue.setDisabled(False)
        self.statusBar().showMessage('Ready')
        self.runner.terminate()

    def btnReadMeClick(self):
        
        self.dialog.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'BlueStack', 'Enter your bluestack instance name:')

        if ok:
            self.name = str(text)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Application()
   ex.show()
   sys.exit(app.exec_())

