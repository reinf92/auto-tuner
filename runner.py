import cv2
import os
import numpy
import item
import handler
import event
import win32gui
import pyautogui
import time
from PIL import Image
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PIL.ImageQt import ImageQt
import pytesseract

import win32ui
from ctypes import windll
import re

 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class Runner(QThread):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.itemLables = [app.item1, app.item2, app.item3, app.item4, app.item5, app.item6, app.item7, app.item8]
        self.failedLables = [app.failed1, app.failed2, app.failed3, app.failed4, app.failed5, app.failed6, app.failed7]

    def run(self):
        self.hwnd = handler.Handler(self.app.name)
        self.evnet = event.Event(self.hwnd.getContentHandle(), self.app.radioValue)
        self.status = True
        
        hwnd = self.hwnd.getContentHandle()
        win32gui.SetForegroundWindow(hwnd)
        x1, y1, x2, y2 = win32gui.GetClientRect(hwnd)
        x1, y1 = win32gui.ClientToScreen(hwnd, (x1, y1))
        x2, y2 = win32gui.ClientToScreen(hwnd, (x2 - x1, y2 - y1))

        targetLevel = int(self.app.levelOfItemsValue.text());
        loop = int(self.app.stopWhenNumOfItemsValue.text());
        items = [];

        for i in range(0, loop):
            items.append(item.Item())
        
        for i in range(0, loop):
            transaction = True

            while transaction:
                self.app.statusBar().showMessage('To buy and sell..')

                self.evnet.Board()
                self.evnet.Buy()
                self.evnet.Tune()

                while (items[i].level < targetLevel and items[i].status):

                    self.updateMessage('item', i, items[i]);
                    self.app.statusBar().showMessage('Tuning...')

                    self.evnet.Tuning(i)
                    self.evnet.Board()

                    im = self.captureImage(self.hwnd.getWarpHandle())
                    qim = ImageQt(im)
                    pixmap = QPixmap.fromImage(qim)
                    pixmap = pixmap.scaled(300,120)
                    self.app.imgLabel.setPixmap(pixmap)

                    image = numpy.array(im)
                    filename = "{}.png".format(os.getpid())
                    cv2.imwrite(filename, image)
                    text = pytesseract.image_to_string(Image.open(filename), lang=None)
                    os.remove(filename)

                    time.sleep(0.5)            

                    result = self.isSuccess(text)

                    if (result):
                        self.app.statusBar().showMessage('Success!!')
                        items[i].success()
                    else:
                        self.app.statusBar().showMessage('Failed..')
                        items[i].failed()
                    
                    

                if (items[i].status == False):

                    self.app.statusBar().showMessage('To buy and sell..')
                    self.updateMessage('fail', items[i].level-1, None)

                    self.evnet.Board()
                    self.evnet.Sell(i)
                    self.itemLables[i].setText('0(100)')

                    items[i].reset()
                else:
                    transaction = False

        self.app.btn1.setDisabled(False)
        self.app.btn2.setDisabled(True)
        self.app.btn3.setDisabled(False)
        self.app.radio1.setDisabled(False)
        self.app.radio2.setDisabled(False)
        self.app.radio3.setDisabled(False)
        self.app.radio4.setDisabled(False)
        self.app.radio5.setDisabled(False)
        self.app.levelOfItemsValue.setDisabled(False)
        self.app.stopWhenNumOfItemsValue.setDisabled(False)
        self.app.statusBar().showMessage('Ready')


    def isSuccess(self, str):
        if (str.__contains__('was') or str.__contains__('suc')):
            return True
        else:
            return False

    def updateMessage(self, flag, index, obj):
        if (flag == 'item'):
            self.itemLables[index].setText(str(obj.level) + '(' + str(obj.durability) + ')')
        else:
            text = self.failedLables[index].text()
            num = int(text[3:-1]) + 1
            self.failedLables[index].setText('v' + str((index + 1)) + '(' + str(num) + ')')

    def captureImage(self, hwnd):
        left, top, right, bot = win32gui.GetWindowRect(hwnd)
        w = right - left
        h = bot - top

        hwndDC = win32gui.GetWindowDC(hwnd)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()

        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

        saveDC.SelectObject(saveBitMap)

        result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)

        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)

        im = Image.frombuffer('RGB',
            (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
            bmpstr, 'raw', 'BGRX', 0, 1)

        cropping_area = (130,41,390,142)
        im = im.crop(cropping_area)

        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, hwndDC)

        return im