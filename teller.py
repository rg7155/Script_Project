#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

import noti

bookmarkList = ''
def replyAptData(user):
    global bookmarkList
    if bookmarkList:
        noti.sendMessage( user, bookmarkList )
    else:
        noti.sendMessage( user, '즐겨찾기 목록에 데이터가 없습니다.')

def save( user, loc_param ):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    try:
        cursor.execute('INSERT INTO users(user, location) VALUES ("%s", "%s")' % (user, loc_param))
    except sqlite3.IntegrityError:
        noti.sendMessage( user, '이미 해당 정보가 저장되어 있습니다.' )
        return
    else:
        noti.sendMessage( user, '저장되었습니다.' )
        conn.commit()

def check( user ):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    cursor.execute('SELECT * from users WHERE user="%s"' % user)
    for data in cursor.fetchall():
        row = 'id:' + str(data[0]) + ', location:' + data[1]
        noti.sendMessage( user, row )


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('즐겨찾기') or text.startswith('즐찾'):
        replyAptData(chat_id)
    else:
        noti.sendMessage(chat_id, """ 모르는 명령어입니다. "즐겨찾기"를 입력하세요. """)

def InitTele(bookmarklst):
    global bookmarkList

    bookmarkList = bookmarklst
    today = date.today()
    current_month = today.strftime('%Y%m')

    print('[', today, ']received token :', noti.TOKEN)

    bot = telepot.Bot(noti.TOKEN)
    pprint(bot.getMe())

    bot.message_loop(handle)

    print('Listening...')
    noti.sendMessage(1773658412, """ 어서오세요. Find Home 텔레그램입니다.\n\n<명령어 메뉴>\n1.즐겨찾기: 즐겨찾기된 데이터를 출력합니다.\n
    """)
    while 1:
        time.sleep(10)
