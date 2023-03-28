import threading
import queue
import time

from application_modules.logger_module import Logger_Module
import common.common_definitions as comm_def

_PRIVETE_KEY = '800650430'
_PUBLIC_KEY = '-928569638'

__callback_list = {}

def __communication_manager_init__(mode_monitor, alert_manager, driver, entertainer):
    global __mode_monitor
    global __alert_manager
    global __driver
    global __entertainer
    
    __mode_monitor = mode_monitor
    __alert_manager = alert_manager
    __driver = driver
    __entertainer = entertainer

def register_send_alert_callback(callback):
    global __send_alert_callback
    __send_alert_callback = callback

def register_send_photo_callback(callback):
    global __send_photo_callback
    __send_photo_callback = callback

def register_communication_callback(topic, callback):
    global __callback_list
    __callback_list.update({topic, callback})

def control_movement(direction:str):
    __driver.com_callback(direction)
        
def fun_movement(direction:str):
    __entertainer.entertainer_callback(direction)
    print(message)

def change_mode(mode:str):
    __mode_monitor.update_mode(mode)

def alert_handler(alert_handle:str):
    print(alert_handle)
    __alert_manager.handle_alert(alert_handle, "+")

def send_public_alert_message(message):
    __send_alert_callback(_PUBLIC_KEY, message)

def send_private_alert_message(message):
    __send_alert_callback(_PRIVETE_KEY, message)

def send_public_photo_to_telegram(file_path):
    __send_photo_callback(_PUBLIC_KEY,file_path)

def send_private_photo_to_telegram(file_path):
    __send_photo_callback(_PRIVETE_KEY,file_path)
    
