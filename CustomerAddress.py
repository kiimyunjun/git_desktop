from mini2.Address import Addr

class CustomerAddr(Addr):
    def __init__(self, name, tel, email, address, group, b_day,
                 comp_name, prod_name, position):
        super().__init__(name, tel, email, address, group, b_day)
        self.comp_name = comp_name
        self.prod_name = prod_name
        self.position = position

    # more getters and setters
    def get_comp_name(self):
        return self.comp_name
    def get_prod_name(self):
        return self.prod_name
    def get_position(self):
        return self.position
    
    def set_comp_name(self,value):
        self.comp_name = value
    def set_prod_name(self,value):
        self.prod_name = value
    def set_position(self,value):
        self.position = value

    # customer form print
    def print_info(self):
        print("""
            --------------------
            이름 : {}
            번호 : {}
            메일 : {}
            주소 : {}
            그룹 : {}
            생일 : {}
            거래처 이름 : {}
            품목 : {}
            직급 : {}
            --------------------
                """.format(self.get_name(), self.get_tel(), self.get_email(),
                           self.get_address(), self.get_group(), self.get_b_day(),
                           self.get_comp_name(), self.get_prod_name(), self.get_position()))