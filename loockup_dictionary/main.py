import pymouse
from .keyhandlers.KeyListener import KeyListener
from .keyhandlers.HandleClass import Handler
from .ui.lookupBox2 import Ui_Form

import pyperclip
import pyautogui
from pynput.keyboard import Key, Controller
from PyQt4 import QtGui
from PyQt4 import QtCore

error=False
class DictionBox(QtGui.QWidget, Ui_Form):
    global error
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        text = pyperclip.paste()
        self.setupUi(self, text,error)


def StartCopy():
    import sys
    keyboard = Controller()
    with keyboard.pressed(Key.ctrl):
        keyboard.press('c')
        keyboard.release('c')

    app = QtGui.QApplication(sys.argv)
    window = DictionBox()
    mouse = pymouse.PyMouse()
    x,y=mouse.position()
    if x - 130 >=0:
    	x=x-139

    y=y+20

    window.move(x,y)
    window.show()
    app.quit()
    app.exec_()
    while True:
        keylistener = KeyListener()
        keylistener.addKeyListener("L_CTRL+m", StartCopy)
        handle = Handler(keylistener)

try:
    keylistener = KeyListener()
    keylistener.addKeyListener("L_CTRL+m", StartCopy)
    handle = Handler(keylistener)
except:
    error=True
