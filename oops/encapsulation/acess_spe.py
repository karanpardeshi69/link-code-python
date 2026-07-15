class xyz:
    # class var
    __a=90
    b=80
    def  geta(self):
        return self.__a
    def __show(self):
        return "private method"
    
    def call_show(self):
        return self.__show()
    
    def abc(self):
        return "Public method"
    
    def new_value(self,new_val):
        self.__a = new_val
        print("Value updated to ",self.geta())
        

    
obj = xyz()
print(obj.geta())
print(obj.call_show())
print(obj.abc())
obj.new_value(20)
print(obj.geta())