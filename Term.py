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
DataList = []

class MainGui:
    def InitInputImage(self):
        #LogoImage = PhotoImage(file='MyImage/Search.jpg')
        self.LogoImage = ImageTk.PhotoImage(Image.open('MyImage/Logo.png'))
        self.LogoLabel = Label(window, image=self.LogoImage)
        self.LogoLabel.pack()
        self.LogoLabel.place(x=10, y=10)

        self.MenuButton=[0]*3
        self.MenuImage=[0]*3

        for x in range(3):
            if x == 0:
                self.MenuImage[x] = ImageTk.PhotoImage(Image.open('MyImage/Search.jpg'))
            elif x == 1:
                self.MenuImage[x] = ImageTk.PhotoImage(Image.open('MyImage/Bookmark.png'))
            else:
                self.MenuImage[x] = ImageTk.PhotoImage(Image.open('MyImage/Graph.png'))

            self.MenuButton[x] = Button(window, image=self.MenuImage[x])
            self.MenuButton[x].pack()
            self.MenuButton[x].place(x=10, y=200 + x*150)

    def InitSearchListBox(self):
        global SearchListBox #정렬조건
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
        global SearchListBox

        #SearchListBox.delete(0, 'end')

        #RenderText.configure(state='normal')
        #RenderText.delete(0.0, END)
        iSearchIndex = SearchListBox.curselection()[0]
        if iSearchIndex == 0:
            self.SearchData()
        elif iSearchIndex == 1:
            pass  # SearchGoodFoodService()
        elif iSearchIndex == 2:
            pass  # SearchMarket()
        elif iSearchIndex == 3:
            pass  # SearchCultural()

        #RenderText.configure(state='disabled')

    def SearchData(self):
        import http.client
        from xml.dom.minidom import parse, parseString
        conn = http.client.HTTPConnection("openapi.molit.go.kr")
        conn.request("GET",
                     "/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?serviceKey=U9TRdwhUQTkPIk4fvhtKRx%2BGV970UoDYMjy%2Br3IHsDKyVaj5ToULtpWNGDe%2FGW1TvnVjX37G%2FwLhhk5TMP5IbQ%3D%3D&pageNo=1&numOfRows=10&LAWD_CD=11110&DEAL_YMD=202012")
        req = conn.getresponse()
        print(req.status, req.reason)

        global DataList
        DataList.clear()

        if req.status == 200:
            BooksDoc = req.read().decode('utf-8')
            if BooksDoc == None:
                print("에러")
            else:
                parseData = parseString(BooksDoc)
                top = parseData.childNodes
                response = top[0].childNodes
                body = response[1].childNodes
                items = body[0].childNodes
                for item in items:
                    #print(item.nodeName)
                    if item.nodeName == "item":
                        subitems = item.childNodes
                        print(subitems)
                        if subitems[3].firstChild.nodeValue == InputLabel.get():
                            pass
                        elif subitems[5].firstChild.nodeValue == InputLabel.get():
                            pass
                        else:
                            continue

                        if subitems[29].firstChild is not None:
                            tel = str(subitems[29].firstChild.nodeValue)
                            pass  # ?꾩떆
                            if tel[0] is not '0':
                                tel = "02-" + tel
                                pass
                            DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, tel))
                        else:
                            DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, "-"))

                for i in range(len(DataList)):
                    RenderText.insert(INSERT, "[")
                    RenderText.insert(INSERT, i + 1)
                    RenderText.insert(INSERT, "] ")
                    RenderText.insert(INSERT, "시설명: ")
                    RenderText.insert(INSERT, DataList[i][0])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "주소: ")
                    RenderText.insert(INSERT, DataList[i][1])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "전화번호: ")
                    RenderText.insert(INSERT, DataList[i][2])
                    RenderText.insert(INSERT, "\n\n")

    def InitRenderText(self):
        global RenderText

        RenderTextScrollbar = Scrollbar(window)
        RenderTextScrollbar.pack()
        RenderTextScrollbar.place(x=375, y=200)

        TempFont = font.Font(window, size=10, family='Consolas')
        RenderText = Text(window, width=45, height=35, borderwidth=6, relief='ridge',
                          yscrollcommand=RenderTextScrollbar.set)
        RenderText.pack()
        RenderText.place(x=100, y=130)
        RenderTextScrollbar.config(command=RenderText.yview)
        RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

        RenderText.configure(state='disabled')

    def __init__(self):
        #window = Tk()
        window.title("Find Home")

        # window.geometry("800x600")

        Canvas(window, bg='white', width=WINCX, height=WINCY).pack()

        self.InitInputImage()
        self.InitSearchListBox()
        self.InitInputLabel()
        self.InitRenderText()

        window.mainloop()

MainGui()