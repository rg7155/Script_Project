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
from tkinter import ttk
from tkinter import font
#https://m.blog.naver.com/dukalee/221268775318
from PIL import ImageTk, Image

import localCode
from Bookmark import *
import tkinter.messagebox
import  random

WINCX = 800
WINCY = 600
window = Tk()
DataList = []
BACKCOLOR = 'LightSlateGray'
host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"
bookmark = BookMark()

class MainGui:
    def InitInputImage(self):
        #LogoImage = PhotoImage(file='MyImage/Search.jpg')

        self.LogoImage = ImageTk.PhotoImage(Image.open('MyImage/Logo.png'))
        self.LogoLabel = Label(window, image=self.LogoImage, bg=BACKCOLOR)
        self.LogoLabel.pack()
        self.LogoLabel.place(x=5, y=5)

        self.NameImage = ImageTk.PhotoImage(Image.open('MyImage/findhome.png'))
        self.NameLabel = Label(window, image=self.NameImage, bg=BACKCOLOR)
        self.NameLabel.pack()
        self.NameLabel.place(x=160, y=5)

        self.MenuButton=[0]*3
        self.MenuImage=[0]*3



        for x in range(3):
            if x == 0:
                self.MenuImage[x] = ImageTk.PhotoImage(Image.open('MyImage/Search.png'))
            elif x == 1:
                self.MenuImage[x] = ImageTk.PhotoImage(Image.open('MyImage/Bookmark.png'))
            else:
                self.MenuImage[x] = ImageTk.PhotoImage(Image.open('MyImage/Graph.png'))

            self.MenuButton[x] = Button(window, borderwidth=0, image=self.MenuImage[x], bg=BACKCOLOR)
            self.MenuButton[x].pack()
            self.MenuButton[x].place(x=30, y=220 + x*120)

    def InitInputEmailandFileButton(self):
        global EmailButton
        global EmailImage

        EmailImage = ImageTk.PhotoImage(Image.open('MyImage/Gmail.png'))
        EmailButton = Button(window, image=EmailImage, bg=BACKCOLOR, borderwidth=0, command=self.EmailButtonAction)
        EmailButton.pack()
        EmailButton.place(x=500, y=420)

        global FileButton
        global FileImage

        FileImage = ImageTk.PhotoImage(Image.open('MyImage/File.png'))
        # resize_img = img.resize((100, 80), Image.ANTIALIAS)
        # FileImage = ImageTk.PhotoImage(resize_img)
        FileButton = Button(window, image=FileImage, bg=BACKCOLOR, borderwidth=0, command=self.FileButtonAction)
        FileButton.pack()
        FileButton.place(x=650, y=420)

    def InitSearchListBox(self):
        global SearchComboBox #정렬조건

        self.TempFont = ('Consolas', 15)

        SearchComboBox = ttk.Combobox(window, font=self.TempFont,state="readonly", width=10, values=["정렬기준",
                                                                                  "날짜순",
                                                                                  "가격순",
                                                                                  "지역번호순"])
        SearchComboBox.bind("<<ComboboxSelected>>", self.sidoSelected)
        SearchComboBox.current(0)
        SearchComboBox.place(x=150, y=120)

        #정렬 라디오
        self.radioVar = IntVar()
        #radio = Radiobutton(window, text="1번", value=3, variable=RadioVariety_1, command=check)
        self.radioDownOrder = Radiobutton(window, text="내림차순", value=1, variable=self.radioVar)
        self.radioDownOrder.pack()
        self.radioDownOrder.place(x=300, y=120)
        #self.radioDownOrder.highlightcolor(1,1,1)

        self.radioUpOrder = Radiobutton(window, text="오름차순", value=2, variable=self.radioVar)
        self.radioUpOrder.pack()
        self.radioUpOrder.place(x=370, y=120)
        self.radioUpOrder.select()


    def InitSearchLocalList(self):
        self.sigungulst = ["시/군/구"]
        global sidoComboBox
        global sigunguComboBox

        sidoComboBox = ttk.Combobox(window, font=self.TempFont, state="readonly", width=7, values=["시/도",
                                                    "서울특별시",
                                                    "부산광역시",
                                                    "인천광역시",
                                                    "경기도"])

        sidoComboBox.option_add('*TCombobox*Listbox.font', self.TempFont)
        sidoComboBox.bind("<<ComboboxSelected>>", self.sidoSelected)
        sidoComboBox.current(0)
        sidoComboBox.place(x=150, y=160)

        sigunguComboBox = ttk.Combobox(window, font=self.TempFont, state="readonly", width=12, values=self.sigungulst)
        sigunguComboBox.option_add('*TCombobox*Listbox.font', self.TempFont)
        #sigunguComboBox.bind("<<ComboboxSelected>>", self.sigunguSelected)
        sigunguComboBox.current(0)
        sigunguComboBox.place(x=260, y=160)


        self.yearList = ['년도']
        for x in range(10):
            self.yearList.append(2020-x)

        self.monthList = ['월']
        for x in range(12):
            self.monthList.append(x+1)

        global yearComboBox
        global monthComboBox

        yearComboBox = ttk.Combobox(window,font=self.TempFont, state="readonly", width=7, values=self.yearList)
        yearComboBox.option_add('*TCombobox*Listbox.font', self.TempFont)
        yearComboBox.bind("<<ComboboxSelected>>")
        yearComboBox.current(0)
        yearComboBox.place(x=150, y=200)

        monthComboBox = ttk.Combobox(window,font=self.TempFont, state="readonly", width=7, values=self.monthList)
        monthComboBox.option_add('*TCombobox*Listbox.font', self.TempFont)
        monthComboBox.bind("<<ComboboxSelected>>")
        monthComboBox.current(0)
        monthComboBox.place(x=260, y=200)

    def sidoSelected(self, event):
        if event.widget.current() == 0:
            return
        print(event.widget.get())
        # 해당 시도와 일치하는 리스트 가져와서 시/군/구 리스트에 넣기
        self.sigungulst.append("시/도")
        self.sigungulst = localCode.Comboboxlst[event.widget.current()-1]
        sigunguComboBox['values'] = self.sigungulst

    def InitInputLabel(self):
        self.SearchButton = Button(window, font=self.TempFont, text="검색", command=self.SearchButtonAction,
                                   height=1, bg='DarkGray')
        self.SearchButton.pack()
        self.SearchButton.place(x=420, y=155)

    def SearchButtonAction(self):
        #RenderText.configure(state='normal')
        #RenderText.delete(0.0, END)

        self.SearchData()

        #RenderText.configure(state='disabled')

    def SearchData(self):
        import http.client
        from xml.dom.minidom import parse, parseString
        conn = http.client.HTTPConnection("openapi.molit.go.kr")

        Code = localCode.Locallst[sidoComboBox.current()-1][sigunguComboBox.current()][0]
        print("지역코드:", Code)
        year = str(2021-yearComboBox.current())
        print("년",year)
        month = str(monthComboBox.current())
        if monthComboBox.current() <= 9:
            month = '0' + str(monthComboBox.current())
        print("달",month)

        #year = '2016'
        #month = '12'

        conn.request("GET",
                     "/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?serviceKey=U9TRdwhUQTkPIk4fvhtKRx%2BGV970UoDYMjy%2Br3IHsDKyVaj5ToULtpWNGDe%2FGW1TvnVjX37G%2FwLhhk5TMP5IbQ%3D%3D&pageNo=1&numOfRows=1000&LAWD_CD=" + Code + "&DEAL_YMD=" + year + month)
        req = conn.getresponse()
        print(req.status, req.reason)

        global DataList, SearchComboBox
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
                        #print(subitems[10].firstChild)

                        fixIndex = 0
                        if subitems[8].firstChild.nodeValue != '0': # 도로명지상지하코드가 없을때 8이후 한칸씩 당김
                            fixIndex = -1

                        DataList.append((subitems[10 + fixIndex].firstChild.nodeValue,
                                         subitems[0].firstChild.nodeValue,
                                         int(subitems[2].firstChild.nodeValue), int(subitems[17 + fixIndex].firstChild.nodeValue),int(subitems[18 + fixIndex].firstChild.nodeValue)))

                #정렬
                iSearchIndex = SearchComboBox.current()
                print(iSearchIndex)

                if iSearchIndex == 1:
                    print("날짜")
                    if self.radioVar.get() == 1:
                        DataList.sort(key=lambda x : x[4], reverse= True)
                    else:
                        DataList.sort(key=lambda x : x[4])
                elif iSearchIndex == 2:
                    print("금액")
                    if self.radioVar.get() == 1:
                        DataList.sort(key=lambda x : x[1], reverse= True)
                    else:
                        DataList.sort(key=lambda x : x[1])
                elif iSearchIndex == 3:
                    print("지역이름")
                    if self.radioVar.get() == 1:
                        DataList.sort(key=lambda x: x[0], reverse=True)
                    else:
                        DataList.sort(key=lambda x: x[0])

                #스크롤 크기 재조정
                SearchCanvas.config(scrollregion=(0, 0, 50, len(DataList) * 88))

                #버튼 삭제
                for x in range(len(SearchDataButtonList)):
                    SearchDataButtonList[x].destroy()

                for i in range(len(DataList)):
                    but = Button(self.ButtonFrame, text="법정동: " + DataList[i][0] +
                                                        "\n 가격: " + DataList[i][1] +
                                                        "\n 날짜: " + str(DataList[i][2])+ "년 " + str(DataList[i][3]) + "월 " + str(DataList[i][4]) + "일", width=38, height=5,
                                 command=lambda col=i: self.DataButtonAction(col))

                    but.grid(row=i)
                    SearchDataButtonList.append(but)

                '''
                for i in range(len(DataList)):
                    RenderText.insert(INSERT, "[")
                    RenderText.insert(INSERT, i + 1)
                    RenderText.insert(INSERT, "] ")
                    RenderText.insert(INSERT, "법정동: ")
                    RenderText.insert(INSERT, DataList[i][0])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "거래금액: ")
                    RenderText.insert(INSERT, DataList[i][1])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "날짜: ")
                    RenderText.insert(INSERT, DataList[i][2])
                    RenderText.insert(INSERT, "년 ")
                    RenderText.insert(INSERT, DataList[i][3])
                    RenderText.insert(INSERT, "월 ")
                    RenderText.insert(INSERT, DataList[i][4])
                    RenderText.insert(INSERT, "일 ")
                    RenderText.insert(INSERT, "\n\n")
                '''
    def DataButtonAction(self, col):
        tkinter.messagebox.showinfo('저장성공','즐겨찾기에 저장했습니다.')
        bookmark.insertBookmark(DataList[col])
        print(DataList[col])
    def InitRenderText(self):
        global RenderText
        frame = Frame(window, width = 100, height = 170, relief = 'raised')
        frame.pack()
        frame.place(x=150, y=240)

        '''
        RenderTextScrollbar = Scrollbar(frame)
        RenderTextScrollbar.pack()
        #RenderTextScrollbar.place(x=450, y=200)

        TempFont = font.Font(frame, size=20, family='Consolas')
        RenderText = Text(frame, font=self.TempFont, width=27, height=14, borderwidth=1,
                          yscrollcommand=RenderTextScrollbar.set)
        RenderText.pack()
        #RenderText.place(x=150, y=200)

        RenderTextScrollbar.config(command=RenderText.yview)
        RenderTextScrollbar.pack(side=RIGHT, fill=Y)

        RenderText.configure(state='disabled')
        '''

        global SearchCanvas
        SearchCanvas = Canvas(frame, bg='#FFFFFF', width=300, height=300, scrollregion=(0, 0, 50, 1000))
        bar = Scrollbar(frame, orient=VERTICAL)
        bar.pack(side=RIGHT, fill=Y)
        bar.config(command=SearchCanvas.yview)
        SearchCanvas.config(width=300, height=300)
        SearchCanvas.config(yscrollcommand=bar.set)
        SearchCanvas.pack(side=LEFT, expand=True, fill=BOTH)
        self.ButtonFrame = Frame(frame)

        global SearchDataButtonList
        SearchDataButtonList = []
        for _ in range(10):
            but = Button(self.ButtonFrame, text=str(_) + "법정동:\n 가격:", width = 38, height = 5)
            but.grid(row=_)
            SearchDataButtonList.append(but)
        SearchDataButtonList[0].destroy()

        SearchCanvas.create_window(0, 0, anchor='nw', window=self.ButtonFrame)



    def EmailButtonAction(self):
        # 보내는 이메일 주소적기
        EmailWindow = Tk()
        EmailWindow.title("Email 주소입력")
        sw = window.winfo_screenwidth()
        sh = window.winfo_screenheight()

        x = (sw-350) // 2
        y = (sh-200) // 2

        EmailWindow.geometry("{0}x{1}+{2}+{3}".format(350, 50, x, y))
        Label(EmailWindow, text="Send To", font=("Consolas", 15)).pack()
        self.emailEntry = Entry(EmailWindow, width=25, bg='white', font=("Consolas", 15))
        self.emailEntry.pack(side='left')
        sendButton = Button(EmailWindow, text='send', font=("Consolas", 18),
                            command=self.sendMail)

        sendButton.pack(side='left')
        EmailWindow.mainloop()

    def sendMail(self):
        global host, port
        html = ""
        title = "아파트 매매 가격 정보"
        senderAddr = "sungzzuu@gmail.com"
        recipientAddr = self.emailEntry.get()
        passwd = "tjdwn*yunsj00"
        #html = MakeHtmlDoc(SearchBookTitle(keyword))

        import mysmtplib

        # MIMEMultipart의 MIME을 생성합니다.
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        # Message container를 생성합니다.
        msg = MIMEMultipart('alternative')

        # set message
        msg['Subject'] = title
        msg['From'] = senderAddr
        msg['To'] = recipientAddr
        msgtext = bookmark.getBookMarkList()
        msgPart = MIMEText(msgtext, 'plain')
        #bookPart = MIMEText(html, 'html', _charset='UTF-8')

        # 메세지에 생성한 MIME 문서를 첨부합니다.
        msg.attach(msgPart)
        #msg.attach(bookPart)

        print("connect smtp server ... ")
        s = mysmtplib.MySMTP(host, port)
        # s.set_debuglevel(1)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(senderAddr, passwd)  # 로긴을 합니다.
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())
        s.close()

        print("Mail sending complete!!!")

    def FileButtonAction(self):
        pass

    def LogoWindow(self):
        self.logoScreenImg = ImageTk.PhotoImage(Image.open('MyImage/logoScreen.PNG'))
        self.logoScreenImgButton = Button(window, image=self.logoScreenImg, command=self.logoButtonAction)
        self.logoScreenImgButton.pack()


        #LogoLabel.place(x=10, y=10)
    def logoButtonAction(self):
        Canvas(window, bg=BACKCOLOR, width=WINCX, height=WINCY).pack()
        self.logoScreenImgButton.destroy()
        self.InitInputImage()
        self.InitSearchListBox()
        self.InitSearchLocalList()
        self.InitInputLabel()
        self.InitInputEmailandFileButton()
        self.InitRenderText()
        localCode.ReadLocalCode()
        window.mainloop()

    def __init__(self):
        #window = Tk()
        window.title("Find Home")
        window.geometry("800x600")

        self.LogoWindow()
        # self.InitInputImage()
        # self.InitSearchListBox()
        # self.InitInputLabel()
        # self.InitInputEmailandFileButton()
        # self.InitRenderText()

        window.mainloop()


MainGui()