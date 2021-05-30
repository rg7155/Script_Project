from tkinter import *
import threading
import sys, os
from tkinter import messagebox
# pip install folium
import folium
# pip install cefpython3==66.1
from cefpython3 import cefpython as cef
from selenium import webdriver


def showMap(frame):
    global browser

    sys.excepthook = cef.ExceptHook
    cef.Initialize()
    window_info = cef.WindowInfo(frame.winfo_id())
    window_info.SetAsChild(frame.winfo_id(), [0, 0, 800, 600])
    browser = cef.CreateBrowserSync(window_info, url='file:///map.html')
    print('show')
    cef.MessageLoop()


def Pressed(frame):
    # 브라우저를 위한 쓰레드 생성
    global thread
    thread = threading.Thread(target=showMap, args=(frame,))
    thread.daemon = True

    thread.start()

def Reload():
    browser.Reload()

def CreateHmtl(loc, popup):
    # 지도 저장
    # 위도 경도 지정
    m = folium.Map(location=[loc[0], loc[1]], zoom_start=17)
    # 마커 지정
    folium.Marker([loc[0], loc[1]], popup=popup).add_to(m)
    # html 파일로 저장
    m.save('map.html')


# window = Tk()
# Button(window, text='folium 지도', command=Pressed).pack()
# frame = Frame(window, width=800, height=600)
# frame.pack()
# window.mainloop()


