# -*- coding: utf-8 -*-
"""
@Author: Mathiyazhagan Ramaniselva
@Date: 26.03.2023
"""

import threading
import queue
import time

class Mode_Monitor:

    def __init__(self):
        print("Mode_Monitor Init Started")

        self.__mode_queue = queue.Queue()
        self.__callback_list = []

        threading.Thread(target=self.__mode_monitor, daemon=True).start()

        print("Mode_Monitor Init Completed")

    def register_mode_monitor_callback(self, callback):
        self.__callback_list.append(callback)

    def update_mode(self, mode):
        self.__mode_queue.put(mode)

    def __mode_monitor(self):
        print("Mode_Monitor Thread Started")

        while True:
            if self.__mode_queue.empty() != True:
                __mode = self.__mode_queue.get()

                for __item in self.__callback_list:
                    __item(__mode)

            time.sleep(0.1)