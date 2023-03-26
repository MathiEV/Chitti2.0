# -*- coding: utf-8 -*-
"""
@Author: Mathiyazhagan Ramaniselva
@Date: 26.03.2023
"""

import signal
import sys

from System.mode_monitor import ModeMonitor

def signal_handler(_SIGNO, _STACK_FRAME):
    print("Signal Received : Exiting...")
    sys.exit(0)

def main():
    mode_monitor = ModeMonitor()

    signal.pause()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    main()
