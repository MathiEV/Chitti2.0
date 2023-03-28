from system.telegram_module import *

def control_mode(message:str):
    print(message)
        
def fun_mode(message:str):
    print(message) 

def send_alert_message(message):
    chat_id=''
    send_alert(chat_id)

def send_photo_to_telegram(file_path):
    chat_id = ''
    send_photo(chat_id,file_path)
    