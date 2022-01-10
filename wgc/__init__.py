from pywhatkit import sendwhatmsg, sendwhats_image, send_mail, send_hmail
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from sys import argv, exit

if __name__ == '__main__':
    sendwhatmsg("+27735550878", "teste WGC", 7, 57, tab_close=True, close_time=20)
