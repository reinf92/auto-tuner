import cv2
import os
import numpy
import win32gui
import time
import pytesseract
import win32ui

from PIL import Image
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PIL.ImageQt import ImageQt
from ctypes import windll
from Item import *
from Event import *
from Action import *
from Handler import *
 
pytesseract.pytesseract.tesseract_cmd = r'.\resources\ocr\tesseract.exe'

class Runner(QThread):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.handler = Handler(window)
        self.action = Action(window)

    def run(self):
        resetLables(self.window)

        level = int(self.window.le_level_of_items.text());
        loop = int(self.window.le_stop_when_num_of_items.text());

        items = [];

        for i in range(0, loop):
            items.append(Item())
        
        for i in range(0, loop):
            transaction = True

            while transaction:

                self.action.boardAction()
                self.action.buyAction()
                self.action.tuneAction()

                while (items[i].level < level and items[i].status):

                    self.setStatusBoard('item', i, items[i]);

                    self.action.tuningAction(i)
                    self.action.boardAction()

                    image = self.captureImage(self.window.wrapHwnd)

                    qImage = ImageQt(image)
                    pixmap = QPixmap.fromImage(qImage)
                    pixmap = pixmap.scaled(260,100)
                    self.window.lb_pixmap.setPixmap(pixmap)

                    imageNumpy = numpy.array(image)
                    filename = "{}.png".format(os.getpid())
                    cv2.imwrite(filename, imageNumpy)
                    text = pytesseract.image_to_string(Image.open(filename), lang=self.window.languege)
                    os.remove(filename)
                    time.sleep(0.5)            

                    if (self.isSuccess(text)):
                        items[i].success()
                    else:
                        items[i].failed()
                    
                if (items[i].status == False):

                    self.setStatusBoard('fail', items[i].level-1, None)

                    self.action.boardAction()
                    self.action.sellAction(i)

                    self.window.items[i].setText('0(100)')

                    items[i].reset()
                else:
                    self.setStatusBoard('item', i, items[i]);
                    transaction = False

        self.window.btn_start.setDisabled(True)
        self.window.btn_stop.setDisabled(False)
        self.window.btn_help.setDisabled(True)
        self.window.btn_languege.setDisabled(True)
        self.window.rd_one.setDisabled(True)
        self.window.rd_two.setDisabled(True)
        self.window.rd_three.setDisabled(True)
        self.window.rd_four.setDisabled(True)
        self.window.rd_five.setDisabled(True)
        self.window.le_level_of_items.setDisabled(True)
        self.window.le_stop_when_num_of_items.setDisabled(True)
        self.window.le_bluestacks_name.setDisabled(True)

        QMessageBox.about(self.window, "알림", "개조가 완료되었습니다.")

    def isSuccess(self, str):
        if (self.window.languege == None):
            if (str.__contains__('was') or str.__contains__('suc')):
                return True
            else:
                return False
        else:
            if (str.__contains__('개조가') or str.__contains__('되었네')):
                return True
            else:
                return False

    def setStatusBoard(self, flag, index, obj):
        if (flag == 'item'):
            self.window.items[index].setText(str(obj.level) + '(' + str(obj.durability) + ')')
        else:
            text = self.window.failures[index].text()
            num = int(text[4:-1]) + 1
            self.window.failures[index].setText('Lv' + str((index + 1)) + '(' + str(num) + ')')

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

        windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)

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