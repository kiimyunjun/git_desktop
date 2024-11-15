from ShowData import ShowData

class Addr(ShowData):
    def __init__(self, name, tel, email, address, group, b_day):
        self.name = name
        self.tel = tel
        self.email = email
        self.address = address
        self.group = group
        self.b_day= b_day

    # getters
    def get_name(self):
        return self.name
    def get_tel(self):
        return self.tel
    def get_email(self):
        return self.email
    def get_address(self):
        return self.address
    def get_group(self):
        return self.group
    def get_b_day(self):
        return self.b_day

    # setters
    def set_name(self,value):
        self.name = value
    def set_tel(self,value):
        self.tel = value
    def set_email(self,value):
        self.email = value
    def set_address(self,value):
        self.address = value
    def set_group(self,value):
        self.group = value
    def set_b_day(self,value):
        self.b_day = value

    
    def print_info(self):
        pass
        # print("""
        #     ------------------
        #     이름 : {}
        #     번호 : {}
        #     메일 : {}
        #     주소 : {}
        #     그룹 : {}
        #     생일 : {}
        #     ------------------
        #         """.format(self.get_name(), self.get_tel(), self.get_email(),
        #                    self.get_address(), self.get_group(), self.get_b_day()))

    def show_data(self):
        print("""
            --------------------
            이름 : {}
            번호 : {}
            --------------------
              """.format(self.get_name(), self.get_tel()))