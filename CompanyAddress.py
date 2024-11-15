from mini2.Address import Addr

class CompanyAddr(Addr):
    def __init__(self, name, tel, email, address, group, b_day,
                 comp_name, team_name, position):
        super().__init__(name, tel, email, address, group, b_day)
        self.comp_name = comp_name
        self.team_name = team_name
        self.position = position

    # more getters and setters
    def get_comp_name(self):
        return self.comp_name
    def get_team_name(self):
        return self.team_name
    def get_position(self):
        return self.position
    
    def set_comp_name(self,value):
        self.comp_name = value
    def set_team_name(self,value):
        self.team_name = value
    def set_position(self,value):
        self.position = value

    # company form print
    def print_info(self):
        print("""
            --------------------
            이름 : {}
            번호 : {}
            메일 : {}
            주소 : {}
            그룹 : {}
            생일 : {}
            회사 이름 : {}
            부서 이름 : {}
            직급 : {}
            --------------------
                """.format(self.get_name(), self.get_tel(), self.get_email(),
                           self.get_address(), self.get_group(), self.get_b_day(),
                           self.get_comp_name(), self.get_team_name(), self.get_position()))
        