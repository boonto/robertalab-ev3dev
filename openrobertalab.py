#!/usr/bin/env python
import atexit
import gobject
import logging
import os
import sys
from dbus.mainloop.glib import DBusGMainLoop
from roberta.lab import Service

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('roberta')

gobject.threads_init()
service = None


def cleanup():
    if service:
        service.hal.clearDisplay()
        service.hal.stopAllMotors()
    os.system('setterm -cursor on')
    logger.info('--- done ---')
    logging.shutdown()


def main():
    logger.info('--- starting ---')
    logger.info('running on tty: %s' % os.ttyname(sys.stdin.fileno()))
    os.system('setterm -cursor off')

    atexit.register(cleanup)

    DBusGMainLoop(set_as_default=True)
    loop = gobject.MainLoop()
    service = Service('/org/openroberta/Lab1')
    logger.info('loop running')
    loop.run()

if __name__ == "__main__":
    main()
