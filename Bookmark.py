class BookMark():
    def __init__(self):
        self.BookMarkList = []

    def insertBookmark(self, data):
        self.BookMarkList.append(data)


    def getBookMarkList(self):
        dataStr = ''
        for i in range(len(self.BookMarkList)):
            tmp = "법정동: " + self.BookMarkList[i][0]
            tmp += "\n 가격: "
            tmp += self.BookMarkList[i][1]
            tmp += "\n 날짜: "
            tmp += str(self.BookMarkList[i][2])
            tmp += "년 "
            tmp += str(self.BookMarkList[i][3])
            tmp += "월 "
            tmp += str(self.BookMarkList[i][4])
            tmp += "일\n\n"
            dataStr += tmp

        return str(dataStr)


    def InitBookmarkPage(self):
        pass
        # global SearchCanvas
        # global frame
        # SearchCanvas = Canvas(frame, bg='#FFFFFF', width=300, height=300, scrollregion=(0, 0, 50, 1000))
        # bar = Scrollbar(frame, orient=VERTICAL)
        # bar.pack(side=RIGHT, fill=Y)
        # bar.config(command=SearchCanvas.yview)
        # SearchCanvas.config(width=300, height=300)
        # SearchCanvas.config(yscrollcommand=bar.set)
        # SearchCanvas.pack(side=LEFT, expand=True, fill=BOTH)
        # self.ButtonFrame = Frame(frame)
        #
        # global SearchDataButtonList
        # SearchDataButtonList = []
        # for i in range(len(self.BookMarkList)):
        #     but = Button(self.ButtonFrame, text="법정동: " + self.BookMarkList[i][0] +
        #                                         "\n 가격: " + self.BookMarkList[i][1] +
        #                                         "\n 날짜: " + str(self.BookMarkList[i][2]) + "년 " + str(
        #         self.BookMarkList[i][3]) + "월 " + str(self.BookMarkList[i][4]) + "일", width=38, height=5)
        #
        #     but.grid(row=i)
        #     SearchDataButtonList.append(but)
        # SearchDataButtonList[0].destroy()
        #
        # SearchCanvas.create_window(0, 0, anchor='nw', window=self.ButtonFrame)

