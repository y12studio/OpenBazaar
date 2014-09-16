from os import system
from os import uname
from enum import Enum

LogMsgType = Enum('LogType', 'ONMSG PING')

def open_default_webbrowser(url):
    open_browser_cmds = {'Darwin': 'open',
                         'Linux': 'xdg-open',
                         'Windows': 'start'}
    try:
        system("%s %s" % (open_browser_cmds[uname()[0]], url))
    except:
        print "[openbazaar:utils.open_default_webbrowser] Could not open default web browser at", url

def logmsg(logger, logMsgType, msg):
    logger('%s : %s' % (logMsgType.name, msg))