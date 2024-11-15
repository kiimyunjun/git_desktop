# from Address import Addr
from CompanyAddress import CompanyAddr
from CustomerAddress import CustomerAddr

class SmartPhone:
    def __init__(self):
        self.contacts = []

    # search by name
    def search_by_name(self, name):
        for addr in self.contacts:
            if addr.get_name() == name:
                return addr

    # 1 company form save
    # 2 customer form save
    def input_info_comp(self):
        temp_name = input("이름 입력: ")
        temp_tel = input("번호 입력 : ")
        temp_email = input("메일 입력 : ")
        temp_address = input("주소 입력: ")
        temp_group = input("그룹 입력 : ")
        temp_b_day = input("생일 입력 : ")
        temp_comp_name = input("회사 입력 : ")
        temp_team_name = input("부서 입력 : ")
        temp_position = input("직급 입력 : ")

        return CompanyAddr(temp_name, temp_tel, temp_email,
                    temp_address, temp_group, temp_b_day,
                    temp_comp_name, temp_team_name, temp_position)
    
    def input_info_cust(self):
        temp_name = input("이름 입력: ")
        temp_tel = input("번호 입력 : ")
        temp_email = input("메일 입력 : ")
        temp_address = input("주소 입력: ")
        temp_group = input("그룹 입력 : ")
        temp_b_day = input("생일 입력 : ")
        temp_comp_name = input("거래처 입력 : ")
        temp_prod_name = input("품목 입력 : ")
        temp_position = input("직급 입력 : ")

        return CustomerAddr(temp_name, temp_tel, temp_email,
                    temp_address, temp_group, temp_b_day,
                    temp_comp_name, temp_prod_name, temp_position)

    def save_info(self, comp_or_cust):
        if len(self.contacts) < 10:
            if comp_or_cust == 1:
                addr = self.input_info_comp()
            else:
                addr = self.input_info_cust()
            self.contacts.append(addr)
            addr.show_data()
            print(f">>> 저장 완료 ({len(self.contacts)}/10)")
        else :
                print("주소록에 공간이 없습니다 . (10/10)")       

    # 3   
    def search_info(self, name):
        try:
            (self.search_by_name(name)).print_info()
        except:
            print("찾으시는 연락처가 없습니다.")

    # 4
    def update_info(self, name):
        try:
            addr = self.search_by_name(name)
            updated_tel = input("수정할 전화번호 입력 : ")
            addr.set_tel(updated_tel)
            addr.show_data()
            print(">>> 수정 완료")
        except:
            print("수정할 연락처가 없습니다.")

    # 5
    def del_info(self, name):
        try:
            addr = self.search_by_name(name)
            addr.show_data()
            self.contacts.remove(addr)
            print(">>> 삭제 완료")
        except:
            print("삭제하시려는 연락처가 없습니다.")

    # 6
    def print_all_contacts(self):
        if len(self.contacts) < 1:
            print("연락처가 비어있습니다.")
        else:
            for i,addr in enumerate(self.contacts):
                print(f"\t\t{i+1}번째 연락처",end='')
                addr.print_info()

    # 7 
    def print_contact(self):
        if len(self.contacts) < 1:
            print("연락처가 비어있습니다.")
        else:
            for i,addr in enumerate(self.contacts):
                print(f"\t\t{i+1}번째 연락처",end='')
                addr.show_data()

            




