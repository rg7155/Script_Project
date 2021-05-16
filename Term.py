'''
import urllib
import http.client
conn = http.client.HTTPConnection("openapi.molit.go.kr")
conn.request("GET","/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?serviceKey=U9TRdwhUQTkPIk4fvhtKRx%2BGV970UoDYMjy%2Br3IHsDKyVaj5ToULtpWNGDe%2FGW1TvnVjX37G%2FwLhhk5TMP5IbQ%3D%3D&pageNo=1&numOfRows=10&LAWD_CD=11110&DEAL_YMD=202012")
req = conn.getresponse()
print(req.status,req.reason)
print(req.read().decode('utf-8'))
'''

from tkinter import *
from tkinter import font
#https://m.blog.naver.com/dukalee/221268775318
from PIL import ImageTk, Image

import tkinter.messagebox
import  random

WINCX = 800
WINCY = 600
window = Tk()

class MainGui:
    def InitInputImage(self):
        global LogoLabel
        global LogoImage
        #LogoImage = PhotoImage(file='MyImage/Search.jpg')
        LogoImage = ImageTk.PhotoImage(Image.open('MyImage/Logo.png'))
        LogoLabel = Label(window, image=LogoImage)
        LogoLabel.pack()
        LogoLabel.place(x=10, y=10)

        global MenuButton
        global MenuImage
        MenuButton=[0]*3
        MenuImage=[0]*3

        for x in range(3):
            if x == 0:
                MenuImage[x] = ImageTk.PhotoImage(Image.open('MyImage/Search.jpg'))
            elif x == 1:
                MenuImage[x] = ImageTk.PhotoImage(Image.open('MyImage/Bookmark.png'))
            else:
                MenuImage[x] = ImageTk.PhotoImage(Image.open('MyImage/Graph.png'))

            MenuButton[x] = Button(window, image=MenuImage[x])
            MenuButton[x].pack()
            MenuButton[x].place(x=10, y=200 + x*150)



    def InitSearchListBox(self):
        global SearchListBox
        ListBoxScrollbar = Scrollbar(window)
        ListBoxScrollbar.pack()
        ListBoxScrollbar.place(x=230, y=5)

        TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
        SearchListBox = Listbox(window, font=TempFont, activestyle='none',
                                width=10, height=1, borderwidth=6, relief='ridge',
                                yscrollcommand=ListBoxScrollbar.set)

        SearchListBox.insert(1, "날짜")
        SearchListBox.insert(2, "금액")
        SearchListBox.insert(3, "지역 번호")
        SearchListBox.pack()
        SearchListBox.place(x=100, y=10)

        ListBoxScrollbar.config(command=SearchListBox.yview)

    def InitInputLabel(self):
        global InputLabel
        TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
        InputLabel = Entry(window, font=TempFont, width=15, borderwidth=6, relief='ridge')
        InputLabel.pack()
        InputLabel.place(x=100, y=50)

        SearchButton = Button(window, font=TempFont, text="검색", command=self.SearchButtonAction)
        SearchButton.pack()
        SearchButton.place(x=300, y=50)


    def SearchButtonAction(self):
        pass

    def __init__(self):
        #window = Tk()
        window.title("Find Home")

        self.canvas = Canvas(window,bg='white', width=WINCX, height=WINCY)
        self.canvas.pack()

        self.InitInputImage()
        self.InitSearchListBox()
        self.InitInputLabel()

        window.mainloop()

MainGui()