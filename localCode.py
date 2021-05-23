# 메모장 읽어와서 지역코드, 시군구이름 리스트에 넣기
# 시/도, 시군구 리스트 두 개 만들어서 시/도에 따른 시군구 리스트에 넣기
# 11: 서울
# 26: 부산
# 28: 인천
# 41: 경기
SEOUL = 0
BUSAN = 1
ICN = 2
GG = 3

Locallst = [0] * 4
Comboboxlst = [0] * 4
for i in range(4):
    Locallst[i] = []
for i in range(4):
    Comboboxlst[i] = []
def ReadLocalCode():
    file = open("MyData/LocalCode.txt", "r", encoding='UTF8')
    datalst = file.read().splitlines()

    for i in datalst:
        lst = i.split()
        if lst[0][0:2] == '11':
            Locallst[SEOUL].append(lst)
            Comboboxlst[SEOUL].append(lst[1])
        elif lst[0][0:2] == '26':
            Locallst[BUSAN].append(lst)
            Comboboxlst[BUSAN].append(lst[1])

        elif lst[0][0:2] == '28':
            Locallst[ICN].append(lst)
            Comboboxlst[ICN].append(lst[1])

        elif lst[0][0:2] == '41':
            Locallst[GG].append(lst)
            Comboboxlst[GG].append(lst[1])

    file.close()
    print("지역코드 읽기 완료!!")

