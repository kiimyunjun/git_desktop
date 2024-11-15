from SmartPhone import *

class SmartPhoneMain:
    def __init__(self):
        self.smartphone = SmartPhone()

    def show_options(self):
        print("""
            ========================
            1. 연락처 등록 (회사)
            2. 연락처 등록 (거래처)
            3. 연락처 검색
            4. 연락처 수정
            5. 연락처 삭제
            6. 연락처 정보 전부 출력
            7. 연락처 간단히 출력
            8. 종료
            ========================
            """)

    def turn_on(self):

        while True:
            self.show_options()
            select = int(input("선택 : "))
            print('')
            
            if select == 1:
                self.smartphone.save_info(1)

            elif select == 2:
                self.smartphone.save_info(2)    

            elif select == 3:
                name = input("찾고자 하는 연락처의 이름 : ")
                self.smartphone.search_info(name)
                
            elif select == 4:
                name = input("수정하고자 하는 연락처의 이름 :  ")
                self.smartphone.update_info(name)

            elif select == 5:
                name = input("삭제하고자 하는 연락처의 이름 : ")
                self.smartphone.del_info(name)

            elif select == 6:
                self.smartphone.print_all_contacts()

            elif select == 7:
                self.smartphone.print_contact()

            elif select == 8:
                print("종료합니다.")
                break


# main
if __name__ == "__main__":

    smartphone = SmartPhoneMain()

    smartphone.turn_on()
