#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
#from system.driver import Driver
import asyncio
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_filters import AdvancedCustomFilter
from system.telegram_interface import *

API_TOKEN = '5879367564:AAEzhOy0QCpGmeA5gI8qw7YUk-DV8PvD0yA'
bot = AsyncTeleBot(API_TOKEN)
#driver = Driver()
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
    markup.add(InlineKeyboardButton("Left", callback_data="fun_left"),
                InlineKeyboardButton("Right", callback_data="fun_right"),
			    InlineKeyboardButton("Up", callback_data="fun_front"),
			    InlineKeyboardButton("Down", callback_data="fun_back"))
    return markup
    
    
def move_control_buttons():
    markup = gen_markup()
    markup.add(InlineKeyboardButton("Left", callback_data="control_left"),
                InlineKeyboardButton("Right", callback_data="control_right"),
			    InlineKeyboardButton("Forward", callback_data="control_front"),
			    InlineKeyboardButton("Backward", callback_data="control_back"))
    return markup


def get_mainmenu():
    markup = gen_markup()
    markup.add(InlineKeyboardButton("Control", callback_data="cb_control"),
                               InlineKeyboardButton("Fun", callback_data="cb_fun"))			       
    return markup

    
@bot.message_handler(commands=['start'])
async def start_chat(message):    
    markup = get_mainmenu()
    await bot.send_message(message.chat.id,"choose mode?",reply_markup=markup)


@bot.callback_query_handler(lambda query: query.data in ['cb_control','control_left','control_right','control_front','control_back'])
async def cb_control_action(query):
    if query.data == 'cb_control':
        await bot.send_message(query.message.chat.id,"choose direction",reply_markup=move_control_buttons())
    else:        
        control_mode(query.data)
        
@bot.callback_query_handler(lambda query: query.data in ['cb_fun','fun_left','fun_right','fun_up','fun_down'])
async def cb_fun_action(query):
    if query.data == 'cb_fun':
        await bot.send_message(query.message.chat.id,"choose direction",reply_markup=funmode_controls())
    else:
        print(query.data)
        fun_mode(query.data)
 
async def send_alert(chat_id,message):
    await bot.send_message(chat_id,message)

async def send_photo(chat_id,file_path):
    photo = open(file_path,'rb')
    await bot.send_photo(chat_id,photo)

def start_telegram_service():      
    asyncio.run(bot.polling())  
