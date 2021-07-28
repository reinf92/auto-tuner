import item
import handler
import event
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Runner(QThread):

    def __init__(self, app):
        super().__init__()
        self.app = app
        
    def run(self):
        self.hwnd = handler.Handler()
        self.util = event.Event(self.hwnd.getHandle(),1)
        self.status = True
        
        level = int(self.app.levelOfItemsValue.text());
        loop = int(self.app.stopWhenNumOfItemsValue.text());
        items = [];

        for i in range(0, loop):
            items.append(item.Item())
        
        for i in range(0, loop):

            self.app.statusBar().showMessage('To buy and sell..')

            self.util.Board()
            self.util.Buy()
            self.util.Tune()

            while (items[i].level < level and items[i].durability > 1):

                self.app.statusBar().showMessage('Tuning...')

                self.util.Tuning(i)
                self.util.Board()
               
                

            

        # while self.status:

        #     self.util.Board()
        #     self.util.Buy()
        #     self.util.Tune()
        #     self.util.Tuning(0)
        #     self.sleep(3)

