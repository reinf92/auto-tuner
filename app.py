import sys
import item

from PyQt5.QtWidgets import *
from initFuncs import *

class Application(QMainWindow):

    location = 1;
    item = [item.Item, item.Item, item.Item, item.Item, item.Item, item.Item, item.Item, item.Item]

    def __init__(self):
        super().__init__()
        initWindow(self)
                
        
    def radioButtonClicked(self):     
        if self.radio1.isChecked():
            self.radioValue = 1
        elif self.radio2.isChecked():
            self.radioValue = 2
        elif self.radio3.isChecked():
            self.radioValue = 3
        elif self.radio4.isChecked():
            self.radioValue = 4
        else:
            self.radioValue = 5
        QMessageBox.about(self, 'hello', str(self.radioValue))

    def btnStartClick(self):
        QMessageBox.about(self, "start", "hello")

    def btnStopClick(self):
        QMessageBox.about(self, "stop", "world")


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Application()
   ex.show()
   sys.exit(app.exec_())

