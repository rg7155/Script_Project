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

host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"

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

    def InitInputEmailandFileButton(self):
        global EmailButton
        global EmailImage

        img = Image.open('MyImage/Gmail.png')
        resize_img = img.resize((100, 80), Image.ANTIALIAS)
        EmailImage = ImageTk.PhotoImage(resize_img)
        EmailButton = Button(window, image=EmailImage, bg='white', command=self.EmailButtonAction)
        EmailButton.pack()
        EmailButton.place(x=450, y=450)

        global FileButton
        global FileImage

        img = Image.open('MyImage/File.png')
        resize_img = img.resize((100, 80), Image.ANTIALIAS)
        FileImage = ImageTk.PhotoImage(resize_img)
        FileButton = Button(window, image=FileImage, bg='white', command=self.FileButtonAction)
        FileButton.pack()
        FileButton.place(x=570, y=450)

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

        RenderText.configure(state='normal')
        RenderText.delete(0.0, END)

        self.SearchData()

        RenderText.configure(state='disabled')

    def SearchData(self):
        import http.client
        from xml.dom.minidom import parse, parseString
        conn = http.client.HTTPConnection("openapi.molit.go.kr")

        localCode = "41390"
        year = "2016"
        month = "12"

        conn.request("GET",
                     "/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?serviceKey=U9TRdwhUQTkPIk4fvhtKRx%2BGV970UoDYMjy%2Br3IHsDKyVaj5ToULtpWNGDe%2FGW1TvnVjX37G%2FwLhhk5TMP5IbQ%3D%3D&pageNo=1&numOfRows=1000&LAWD_CD=" + localCode + "&DEAL_YMD=" + year + month)
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
                        #print(subitems[10].firstChild)

                        fixIndex = 0
                        if subitems[8].firstChild.nodeValue != '0': # 도로명지상지하코드가 없을때 8이후 한칸씩 당김
                            fixIndex = -1

                        DataList.append((subitems[10 + fixIndex].firstChild.nodeValue,
                                         subitems[0].firstChild.nodeValue,
                                         int(subitems[2].firstChild.nodeValue), int(subitems[17 + fixIndex].firstChild.nodeValue),int(subitems[18 + fixIndex].firstChild.nodeValue)))

                #정렬
                iSearchIndex = SearchListBox.curselection()[0]
                if iSearchIndex == 0:
                    print("날짜")
                    DataList.sort(key=lambda x : x[4])
                elif iSearchIndex == 1:
                    print("금액")
                    DataList.sort(key=lambda x : x[1])


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

    def InitRenderText(self):
        global RenderText
        RenderTextScrollbar = Scrollbar(window)
        RenderTextScrollbar.pack()
        RenderTextScrollbar.place(x=450, y=200)

        TempFont = font.Font(window, size=20, family='Consolas')
        RenderText = Text(window, width=45, height=35, borderwidth=6, relief='ridge',
                          yscrollcommand=RenderTextScrollbar.set)
        RenderText.pack()
        RenderText.place(x=100, y=130)
        RenderTextScrollbar.config(command=RenderText.yview)
        #RenderTextScrollbar.pack(side=RIGHT, fill=Y)

        RenderText.configure(state='disabled')

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
        msgtext = 'Test'
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
    def __init__(self):
        #window = Tk()
        window.title("Find Home")
        window.geometry("800x600")
        #Canvas(window, bg='white', width=WINCX, height=WINCY).pack()

        self.InitInputImage()
        self.InitSearchListBox()
        self.InitInputLabel()
        self.InitInputEmailandFileButton()
        self.InitRenderText()

        window.mainloop()


MainGui()