#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

import asyncio
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_filters import AdvancedCustomFilter
from system.communication_manager import *
import common.common_definitions as comm_def

API_TOKEN = '5879367564:AAEzhOy0QCpGmeA5gI8qw7YUk-DV8PvD0yA'
bot = telebot.TeleBot(API_TOKEN)

def generate_buttons(btn_names,markup):
    for button in btn_names:
        markup.add(types.KeyboardButton(button))
    return markup

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2    
    return markup

def funmode_controls():
    markup = gen_markup()
    markup.add(InlineKeyboardButton("Left", callback_data=comm_def._FUN_LEFT),
                InlineKeyboardButton("Right", callback_data=comm_def._FUN_RIGHT),
			    InlineKeyboardButton("Up", callback_data=comm_def._FUN_UP),
			    InlineKeyboardButton("Down", callback_data=comm_def._FUN_DOWN))
    return markup
    
def alert_control():
    markup = gen_markup()
    markup.add(InlineKeyboardButton(comm_def._RESET, callback_data=comm_def._ALERT_RESET),
                InlineKeyboardButton(comm_def._CHANGE_SPACE_MODE, callback_data=comm_def._CHANGE_MODE),
			    InlineKeyboardButton(comm_def._HELP, callback_data=comm_def._ALERT_HELP))
    return markup
    
def move_control_buttons():
    markup = gen_markup()
    markup.add(InlineKeyboardButton("Left", callback_data=comm_def._CONTROL_LEFT),
                InlineKeyboardButton("Right", callback_data=comm_def._CONTROL_RIGHT),
			    InlineKeyboardButton("Forward", callback_data=comm_def._CONTROL_FORWORD),
			    InlineKeyboardButton("Backward", callback_data=comm_def._CONTROL_BACKWORD),
                InlineKeyboardButton("Stop", callback_data=comm_def._CONTROL_STOP))
    return markup

def get_startmenu():
    markup =gen_markup()
    markup.add(InlineKeyboardButton("Options", callback_data=comm_def._OPTIONS_CALLBACK),
                InlineKeyboardButton("Info", callback_data=comm_def._INFO_CALLBACK))
    return markup       
       
def get_mainmenu():
    markup = gen_markup()
    markup.add(InlineKeyboardButton("Manual", callback_data=comm_def._CONTROL_CALLBACK),
                               InlineKeyboardButton("Fun", callback_data=comm_def._FUN_CALLBACK),
                               InlineKeyboardButton("Guest", callback_data=comm_def._GUEST_CALLBACK),
                               InlineKeyboardButton("Security", callback_data=comm_def._SECURITY_CALLBACK))			       
    return markup
    
@bot.message_handler(commands=[comm_def._START])
def start_chat(message):
    bot.send_message(message.chat.id,"Hello Welcome back! I am listening !!!",reply_markup=get_startmenu())

@bot.callback_query_handler(lambda query: query.data in [comm_def._OPTIONS_CALLBACK])
def cb_options(query):    
    bot.send_message(query.message.chat.id,"I provide below services!",reply_markup=get_mainmenu())

@bot.callback_query_handler(lambda query: query.data in [comm_def._INFO_CALLBACK])
def cb_info(query):
    bot.send_message(query.message.chat.id,comm_def._INFO_MSG)

@bot.callback_query_handler(lambda query: query.data in [comm_def._CONTROL_CALLBACK,comm_def._CONTROL_LEFT,comm_def._CONTROL_RIGHT,comm_def._CONTROL_FORWORD,comm_def._CONTROL_BACKWORD,comm_def._CONTROL_STOP])
def cb_control_action(query):
    if query.data == comm_def._CONTROL_CALLBACK:
        change_mode(comm_def._MANUAL_MODE)
        bot.send_message(query.message.chat.id,"Manual Mode Activated, Take Control",reply_markup=move_control_buttons())
    else:
        print("1" + query.data)
        control_movement(query.data)
        
@bot.callback_query_handler(lambda query: query.data in [comm_def._FUN_CALLBACK,comm_def._FUN_LEFT,comm_def._FUN_RIGHT,comm_def._FUN_UP,comm_def._FUN_DOWN])
def cb_fun_action(query):
    if query.data == comm_def._FUN_CALLBACK:
        change_mode(comm_def._FUN_MODE)
        bot.send_message(query.message.chat.id,"Fun Mode Activated, Take Control",reply_markup=funmode_controls())
    else:
        print(query.data)
        fun_movement(query.data)

@bot.callback_query_handler(lambda query: query.data in [comm_def._GUEST_CALLBACK])
def cb_guest_action(query):
    if query.data == comm_def._GUEST_CALLBACK:
        change_mode(comm_def._GUEST_MODE)
        bot.send_message(query.message.chat.id, "Guest Mode Activated")

@bot.callback_query_handler(lambda query: query.data in [comm_def._SECURITY_CALLBACK])
def cb_security_action(query):
    if query.data == comm_def._SECURITY_CALLBACK:
        print("1" + comm_def._SECURITY_MODE)
        change_mode(comm_def._SECURITY_MODE)
        bot.send_message(query.message.chat.id, "Security Mode Activated")

@bot.callback_query_handler(lambda query: query.data in [comm_def._ALERT_CONTROL_CALLBACK, comm_def._ALERT_RESET, comm_def._CHANGE_MODE, comm_def._ALERT_HELP])
def cb_alert_action(query):
    if query.data == comm_def._ALERT_CONTROL_CALLBACK:
        bot.send_message(query.message.chat.id, "Performing Alert Action...")
    elif query.data == comm_def._CHANGE_MODE:
        bot.send_message(query.message.chat.id,"Available Modes",reply_markup=get_mainmenu())
    else:
        print(query.data)
        alert_handler(query.data)

def send_alert(chat_id, message):
    bot.send_message(chat_id, message, reply_markup=alert_control())

def send_photo(chat_id,file_path):
    photo = open(file_path,'rb')
    bot.send_photo(chat_id,photo)

def start_telegram_service():
    register_send_photo_callback(send_photo)
    register_send_alert_callback(send_alert)

    print("Telegram Polling Start")
    bot.infinity_polling()   
    print("Telegram Polling Ended")
