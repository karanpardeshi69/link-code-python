from GP import gp
class p(gp):
    abc = "heyy"

    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
