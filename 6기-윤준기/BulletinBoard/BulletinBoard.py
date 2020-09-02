class BulletinBoardFunc:
    def __init__(self):
        self.cnt = 0
        self.title = []
        self.content = []

    def PostArticle(self):
        self.title.insert(self.cnt, input('제목 : '))
        self.content.insert(self.cnt, input('내용 : '))
        self.cnt += 1

    def PrintList(self):

        for a in range(0, self.cnt):
            print('------------------')
            print(self.title[a])
            print(self.content[a])
            print('------------------')

    def DeleteArticle(self):
        DelTitle = input('삭제할 글의 제목을 입력하세요 : ')
        if DelTitle in self.title:
            index = self.title.index(DelTitle)
            del self.title[index]
            del self.content[index]
            self.cnt -= 1
        else:
            print('해당 제목의 글이 없습니다.')


BBF = BulletinBoardFunc()
while True:
    print("----------------------------")
    print("\t글 추가 : 1\n\t글 목록 : 2\n\t글 삭제 : 3\n\t종료 : Q")
    print("----------------------------")
    option = input("선택할 옵션을 고르세요 : ")
    if option == '1':
        BBF.PostArticle()
    elif option == '2':
        BBF.PrintList()
    elif option == '3':
        BBF.DeleteArticle()
    elif option == 'Q' or option == 'q':
        break
    else:
        print('1, 2, 3, Q 중 선택해 주세요!')
