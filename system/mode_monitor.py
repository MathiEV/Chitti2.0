# -*- coding: utf-8 -*-
"""
@Author: Mathiyazhagan Ramaniselva
@Date: 26.03.2023
"""

import threading
import queue
import time

from application_modules.logger_module import Logger_Module
import common.common_definitions as comm_def

class Mode_Monitor:
    _logger = Logger_Module()
    def __init__(self):
        self._logger.logInfo("Mode_Monitor Init Started")

        self.__mode_queue = queue.Queue()
        self.__callback_list = []
        self.mode = comm_def._GUEST_MODE

        threading.Thread(target=self.__mode_monitor, daemon=True).start()

        self._logger.logInfo("Mode_Monitor Init Completed")

    def register_mode_monitor_callback(self, callback):
        self.__callback_list.append(callback)

    def update_mode(self, mode:str):
        self.__mode_queue.put(mode)
        print("changeMode" + mode)

    def get_mode(self):
        return self.mode

    def __mode_monitor(self):
        self._logger.logInfo("Mode_Monitor Thread Started")

        while True:
            if self.__mode_queue.empty() != True:
                __mode = self.__mode_queue.get()

                for __item in self.__callback_list:
                    __item(__mode)

            time.sleep(0.1)