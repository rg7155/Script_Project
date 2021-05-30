'''
import urllib
import http.client
conn = http.client.HTTPConnection("openapi.molit.go.kr")
conn.request("GET","/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?serviceKey=U9TRdwhUQTkPIk4fvhtKRx%2BGV970UoDYMjy%2Br3IHsDKyVaj5ToULtpWNGDe%2FGW1TvnVjX37G%2FwLhhk5TMP5IbQ%3D%3D&pageNo=1&numOfRows=10&LAWD_CD=11110&DEAL_YMD=202012")
req = conn.getresponse()
print(req.status,req.reason)
print(req.read().decode('utf-8'))
'''
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image

import localCode
from Bookmark import *
import tkinter.messagebox
import map
import  random

WINCX = 1280
WINCY = 720
window = Tk()
DataList = []
BACKCOLOR = 'LightSlateGray'
host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"
bookmark = BookMark()

class MainGui:
    def InitNoteBook(self):
        style = ttk.Style(window)
        style.configure('lefttab.TNotebook', tabposition='w', background=BACKCOLOR)

        notebook = ttk.Notebook(window, style='lefttab.TNotebook', width=WINCX, height=WINCY)

        global FrSearch, FrBookMark, FrGraph
        FrSearch = tk.Frame(notebook, bg=BACKCOLOR)
        FrBookMark = tk.Frame(notebook, bg=BACKCOLOR)
        FrGraph = tk.Frame(notebook, bg=BACKCOLOR)

        self.im = Image.open('MyImage/Search.png')
        self.ph = ImageTk.PhotoImage(self.im)
        notebook.add(FrSearch, image = self.ph, compound=tk.TOP)

        self.im1 = Image.open('MyImage/Bookmark.png')
        self.ph1 = ImageTk.PhotoImage(self.im1)
        notebook.add(FrBookMark, image = self.ph1, compound=tk.TOP)

        self.im2 = Image.open('MyImage/Graph.png')
        self.ph2 = ImageTk.PhotoImage(self.im2)
        notebook.add(FrGraph, image = self.ph2, compound=tk.TOP)

        notebook.pack()

    def InitInputImage(self):
        #LogoImage = PhotoImage(file='MyImage/Search.jpg'))

        '''
        self.LogoImage = ImageTk.PhotoImage(Image.open('MyImage/Logo.png'))
        self.LogoLabel = Label(FrSearch, image=self.LogoImage, bg=BACKCOLOR)
        self.LogoLabel.pack()
        self.LogoLabel.place(x=5, y=5)
        '''

        self.NameImage = ImageTk.PhotoImage(Image.open('MyImage/findhome.png'))
        self.NameLabel = Label(FrSearch, image=self.NameImage, bg=BACKCOLOR)
        self.NameLabel.pack()
        self.NameLabel.place(x=160, y=5)

        self.MenuButton=[0]*3
        self.MenuImage=[0]*3


        '''
        for x in range(3):
            if x == 0:
                self.MenuImage[x] = ImageTk.PhotoImage(Image.open('MyImage/Search.png'))
            elif x == 1:
                self.MenuImage[x] = ImageTk.PhotoImage(Image.open('MyImage/Bookmark.png'))
            else:
                self.MenuImage[x] = ImageTk.PhotoImage(Image.open('MyImage/Graph.png'))

            self.MenuButton[x] = Button(FrSearch, borderwidth=0, image=self.MenuImage[x], bg=BACKCOLOR)
            self.MenuButton[x].pack()
            self.MenuButton[x].place(x=30, y=220 + x*120)
        '''


    def InitInputEmailandFileButton(self):
        global EmailButton
        global EmailImage

        EmailImage = ImageTk.PhotoImage(Image.open('MyImage/Gmail.png'))
        EmailButton = Button(FrSearch, image=EmailImage, bg=BACKCOLOR, borderwidth=0, command=self.EmailButtonAction)
        EmailButton.pack()
        EmailButton.place(x=500, y=560)

        global FileButton
        global FileImage

        FileImage = ImageTk.PhotoImage(Image.open('MyImage/File.png'))
        # resize_img = img.resize((100, 80), Image.ANTIALIAS)
        # FileImage = ImageTk.PhotoImage(resize_img)
        FileButton = Button(FrSearch, image=FileImage, bg=BACKCOLOR, borderwidth=0, command=self.FileButtonAction)
        FileButton.pack()
        FileButton.place(x=650, y=560)

    def InitSearchListBox(self):
        global SearchComboBox #정렬조건

        self.TempFont = ('Consolas', 15)

        SearchComboBox = ttk.Combobox(FrSearch, font=self.TempFont,state="readonly", width=10, values=["정렬기준",
                                                                                  "날짜순",
                                                                                  "가격순",
                                                                                  "지역번호순"])
        SearchComboBox.bind("<<ComboboxSelected>>", self.sidoSelected)
        SearchComboBox.current(0)
        SearchComboBox.place(x=150, y=120)



    def InitRadioButton(self):
        # 정렬 라디오
        self.radioUpDownVar = IntVar()
        radioDownOrder = Radiobutton(FrSearch, text="내림차순", value=1, variable=self.radioUpDownVar)
        radioDownOrder.pack()
        radioDownOrder.place(x=300, y=120)
        # self.radioDownOrder.highlightcolor(1,1,1)

        radioUpOrder = Radiobutton(FrSearch, text="오름차순", value=2, variable=self.radioUpDownVar)
        radioUpOrder.pack()
        radioUpOrder.place(x=370, y=120)
        radioUpOrder.select()

        # 검색 라디오
        self.radioSearchTypeVar = IntVar()
        radioSale = Radiobutton(FrSearch, text="매매", value=1, variable=self.radioSearchTypeVar)
        radioSale.pack()
        radioSale.place(x=250, y=80)
        radioSale.select()

        radioJeonse = Radiobutton(FrSearch, text="전세", value=2, variable=self.radioSearchTypeVar)
        radioJeonse.pack()
        radioJeonse.place(x=300, y=80)

        radioMonthRent = Radiobutton(FrSearch, text="월세", value=3, variable=self.radioSearchTypeVar)
        radioMonthRent.pack()
        radioMonthRent.place(x=350, y=80)

    def InitSearchLocalList(self):
        self.sigungulst = ["시/군/구"]
        global sidoComboBox
        global sigunguComboBox

        sidoComboBox = ttk.Combobox(FrSearch, font=self.TempFont, state="readonly", width=7, values=["시/도",
                                                    "서울특별시",
                                                    "부산광역시",
                                                    "인천광역시",
                                                    "경기도"])

        sidoComboBox.option_add('*TCombobox*Listbox.font', self.TempFont)
        sidoComboBox.bind("<<ComboboxSelected>>", self.sidoSelected)
        sidoComboBox.current(0)
        sidoComboBox.place(x=150, y=160)

        sigunguComboBox = ttk.Combobox(FrSearch, font=self.TempFont, state="readonly", width=12, values=self.sigungulst)
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

        yearComboBox = ttk.Combobox(FrSearch,font=self.TempFont, state="readonly", width=7, values=self.yearList)
        yearComboBox.option_add('*TCombobox*Listbox.font', self.TempFont)
        yearComboBox.bind("<<ComboboxSelected>>")
        yearComboBox.current(0)
        yearComboBox.place(x=150, y=200)

        monthComboBox = ttk.Combobox(FrSearch,font=self.TempFont, state="readonly", width=7, values=self.monthList)
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
        self.SearchButton = Button(FrSearch, font=self.TempFont, text="검색", command=self.SearchButtonAction,
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

        Code = localCode.Locallst[sidoComboBox.current()-1][sigunguComboBox.current()][0]
        print("지역코드:", Code)
        year = str(2021-yearComboBox.current())
        #print("년",year)
        month = str(monthComboBox.current())
        if monthComboBox.current() <= 9:
            month = '0' + str(monthComboBox.current())
        #print("달",month)
        #year = '2016'
        #month = '12'

        str1 = "openapi.molit.go.kr"
        str2 = "/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?serviceKey=U9TRdwhUQTkPIk4fvhtKRx%2BGV970UoDYMjy%2Br3IHsDKyVaj5ToULtpWNGDe%2FGW1TvnVjX37G%2FwLhhk5TMP5IbQ%3D%3D&pageNo=1&numOfRows=1000&LAWD_CD="

        if self.radioSearchTypeVar.get() != 1:
            str1 += ":8081"
            str2 = "/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent?serviceKey=U9TRdwhUQTkPIk4fvhtKRx%2BGV970UoDYMjy%2Br3IHsDKyVaj5ToULtpWNGDe%2FGW1TvnVjX37G%2FwLhhk5TMP5IbQ%3D%3D&LAWD_CD="

        conn = http.client.HTTPConnection(str1)
        conn.request("GET", str2 + Code + "&DEAL_YMD=" + year + month)

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

                        indList = [0]*5 #지역,금액,년,월,일

                        if self.radioSearchTypeVar.get() == 1: #매매
                            fixIndex = 0
                            if subitems[8].firstChild.nodeValue != '0': # 도로명지상지하코드가 없을때 8이후 한칸씩 당김
                                fixIndex = -1

                            indList[0] = 10 + fixIndex
                            indList[1] = 0
                            indList[2] = 2
                            indList[3] = 17 + fixIndex
                            indList[4] = 18 + fixIndex

                        else:
                            indList[0] = 2
                            if self.radioSearchTypeVar.get() == 2:
                                indList[1] = 3
                            else:
                                indList[1] = 6

                            indList[2] = 1
                            indList[3] = 5
                            indList[4] = 7

                            if (self.radioSearchTypeVar.get() == 2 and (subitems[6].firstChild.nodeValue).replace(" ","") != '0')\
                                    or (self.radioSearchTypeVar.get() == 3 and (subitems[6].firstChild.nodeValue).replace(" ","") == '0'):
                                continue

                        if self.radioSearchTypeVar.get() != 3:
                            DataList.append((subitems[indList[0]].firstChild.nodeValue,
                                         subitems[indList[1]].firstChild.nodeValue,
                                         int(subitems[indList[2]].firstChild.nodeValue), int(subitems[indList[3]].firstChild.nodeValue),int(subitems[indList[4]].firstChild.nodeValue)))
                        else:
                            DataList.append((subitems[indList[0]].firstChild.nodeValue,
                                             subitems[indList[1]].firstChild.nodeValue,
                                             int(subitems[indList[2]].firstChild.nodeValue), int(subitems[indList[3]].firstChild.nodeValue), int(subitems[indList[4]].firstChild.nodeValue),
                                             subitems[3].firstChild.nodeValue))

                #정렬
                iSearchIndex = SearchComboBox.current()
                if iSearchIndex == 1:
                    if self.radioUpDownVar.get() == 1:
                        DataList.sort(key=lambda x : x[4], reverse= True)
                    else:
                        DataList.sort(key=lambda x : x[4])
                elif iSearchIndex == 2:
                    if self.radioUpDownVar.get() == 1:
                        DataList.sort(key=lambda x : x[1], reverse= True)
                    else:
                        DataList.sort(key=lambda x : x[1])
                elif iSearchIndex == 3:
                    if self.radioUpDownVar.get() == 1:
                        DataList.sort(key=lambda x: x[0], reverse=True)
                    else:
                        DataList.sort(key=lambda x: x[0])

                #스크롤 크기 재조정
                SearchCanvas.config(scrollregion=(0, 0, 50, len(DataList) * 88))

                #버튼 삭제
                for x in range(len(SearchDataButtonList)):
                    SearchDataButtonList[x].destroy()

                for i in range(len(DataList)):
                    str1 = "법정동: " + DataList[i][0] + "\n 가격: " + DataList[i][1]

                    if self.radioSearchTypeVar.get() == 3:
                        str1 += "\n보증금: " + DataList[i][5]

                    but = Button(self.ButtonFrame, text=str1 + "\n 날짜: " + str(DataList[i][2])+ "년 " + str(DataList[i][3]) + "월 " + str(DataList[i][4]) + "일", width=38, height=5,
                                 command=lambda col=i: self.DataButtonAction(col))

                    but.grid(row=i)
                    SearchDataButtonList.append(but)


    def DataButtonAction(self, col):
        tkinter.messagebox.showinfo('저장성공','즐겨찾기에 저장했습니다.')
        bookmark.insertBookmark(DataList[col])
        print(DataList[col])

        # 데이터에서 위도 경도 얻어와서 해당하는 위도 경도 넣고 아파트이름 문자열 넣기
        map.CreateHmtlandReload([37.36636, 127.10654], '샘플데이터')




    def InitRenderText(self):
        global RenderText
        frame = Frame(FrSearch, width = 100, height = 170, relief = 'raised')
        frame.pack()
        frame.place(x=150, y=240)

        global SearchCanvas
        SearchCanvas = Canvas(frame, bg='#FFFFFF', width=300, height=300, scrollregion=(0, 0, 50, 0))
        bar = Scrollbar(frame, orient=VERTICAL)
        bar.pack(side=RIGHT, fill=Y)
        bar.config(command=SearchCanvas.yview)
        SearchCanvas.config(width=300, height=300)
        SearchCanvas.config(yscrollcommand=bar.set)
        SearchCanvas.pack(side=LEFT, expand=True, fill=BOTH)
        self.ButtonFrame = Frame(frame)

        global SearchDataButtonList
        SearchDataButtonList = []
        '''

        for _ in range(10):
            but = Button(self.ButtonFrame, text=str(_) + "법정동:\n 가격:", width = 38, height = 5)
            but.grid(row=_)
            SearchDataButtonList.append(but)
        SearchDataButtonList[0].destroy()
        '''

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

    def InitGraph(self):
        data2 = [100, 550]
        start = 0
        s = sum(data2)
        c2 = tk.Canvas(FrGraph, width=300, height=300, bg=BACKCOLOR, borderwidth=0, relief = 'raised')
        c2.pack()
        c2.place(x=100,y=300)
        for i in range(len(data2)):
            extent = data2[i] / s * 360
            color = '#'
            colors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            for i in range(6):
                color += colors[random.randint(0, 15)]
            c2.create_arc((0, 0, 300, 300), fill=color, outline='white', start=start, extent=extent)
            start = start + extent

    def logoButtonAction(self):
        #Canvas(window, bg=BACKCOLOR, width=WINCX, height=WINCY).pack()
        self.InitNoteBook()
        self.logoScreenImgButton.destroy()
        self.InitInputImage()
        self.InitSearchListBox()
        self.InitRadioButton()
        self.InitSearchLocalList()
        self.InitInputLabel()
        self.InitInputEmailandFileButton()
        self.InitRenderText()
        self.InitGraph()
        localCode.ReadLocalCode()

        self.mapFrame = Frame(window, width=600, height=400, relief='raised')
        self.mapFrame.pack()
        self.mapFrame.place(x=500, y=145)


        map.CreateHmtl([37.39298, 126.90521], '우리집')
        map.SetChild(self.mapFrame)
        map.Pressed(self.mapFrame)

    def __init__(self):
        #window = Tk()
        window.title("Find Home")
        window.geometry(str(WINCX) + "x" + str(WINCY))

        self.LogoWindow()
        # self.InitInputImage()
        # self.InitSearchListBox()
        # self.InitInputLabel()
        # self.InitInputEmailandFileButton()
        # self.InitRenderText()

        window.mainloop()


MainGui()