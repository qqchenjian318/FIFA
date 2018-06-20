

class DataBean:
    def __init__(self,name,first_main,first_pan,first_ke,
                 new_main,new_pan,new_ke,kai_main,kai_ke,pei_fu):
        self.name = name
        self.first_main = first_main
        self.first_pan = first_pan
        self.first_ke = first_ke
        self.new_main = new_main
        self.new_pan = new_pan
        self.new_ke = new_ke
        self.kai_main = kai_main
        self.pei_fu = pei_fu
        self.kai_ke = kai_ke

    def get(self):
        return self
