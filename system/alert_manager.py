# -*- coding: utf-8 -*-
"""
@Author: Mathiyazhagan Ramaniselva
@Date: 27.03.2023
"""

import threading
import queue
import time

from application_modules.logger_module import Logger_Module
import common.common_definitions as comm_def
from system.communication_manager import *

class Alert_Manager:
    _logger = Logger_Module()
    def __init__(self, gpio_worker, update_mode):
        self._logger.logInfo("Alert_Manager Init Started")

        self.__alert_queue = queue.Queue()
        self.__alert_handle_queue = queue.Queue()

        self.__update_mode = update_mode
        self.__gpio_worker = gpio_worker

        self.__alert_callback_list = []
        self.__is_public_alert_enabled = 0

        threading.Thread(target=self.__Alert_Manager, daemon=True).start()

        self._logger.logInfo("Alert_Manager Init Completed")

    def register_alert_callback(self, callback):
        self.__alert_callback_list.append(callback)

    def set_alert(self, alert_type, data):
        self.__alert_queue.put((alert_type, data))

    def handle_alert(self, alert_handle, data):
        self.__alert_handle_queue.put((alert_handle, data))

        print("handle_alert" + alert_handle + " " + data)

    def __Alert_Manager(self):
        self._logger.logInfo("Alert_Manager Thread Started")

        while True:
            if self.__alert_queue.empty() != True:
                __alert_item = self.__alert_queue.get()

                if __alert_item[0] == comm_def._ALERT_1:
                    send_private_photo_to_telegram(__alert_item[1])

                    if self.__is_public_alert_enabled == 1:
                        self.__gpio_worker.set_gpio(comm_def._LED, True)
                        send_public_photo_to_telegram(__alert_item[1])  

                elif __alert_item[0] == comm_def._ALERT_2:
                    send_private_alert_message(__alert_item[1])

                    if self.__is_public_alert_enabled == 1:
                        send_public_alert_message(__alert_item[1])  

            if self.__alert_handle_queue.empty() != True:
                __alert_handle_item = self.__alert_handle_queue.get()

                for __item in self.__alert_callback_list:
                    __item(__alert_handle_item)

                if __alert_handle_item[0] == comm_def._ALERT_RESET:
                    self._logger.logDebug("Reset Alaram")
                    self.__is_public_alert_enabled = 0
                    self.__gpio_worker.set_gpio(comm_def._LED, False)

                    self._logger.logDebug("Send Reset Response To Telegram")
                elif __alert_handle_item[0] == comm_def._CHANGE_MODE:
                    self.__is_public_alert_enabled = 0
                    self.__gpio_worker.set_gpio(comm_def._LED, False)

                    self._logger.logDebug("Send changeMode Response To Telegram" + __alert_handle_item[1])  
                elif __alert_handle_item[0] == comm_def._ALERT_HELP:
                    self.__is_public_alert_enabled = 1

                    self._logger.logDebug("Send changeMode Response To Telegram" + __alert_handle_item[1]) 

            time.sleep(0.1)