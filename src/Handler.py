import win32gui

list = []

def appendChildList(hwnd, param):
    list.append(hwnd)
    return True

class Handler:

    def __init__(self, window):
        self.window = window
        self.window.wrapHwnd = win32gui.FindWindow(None, self.window.le_bluestacks_name.text())
        win32gui.EnumChildWindows(self.window.wrapHwnd, appendChildList, None)
        self.window.contentHwnd = list[0]
