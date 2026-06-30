class demo:
    # class var
    inst = "hello"
    #class method
    @classmethod
    def greet(cls):
        #print("hello")
        return "hello"
    
    @classmethod
    def modify(cls,new):
        cls.inst = new

print(demo.greet())
print(demo.inst)
demo.modify("Linkcode")
print(demo.inst)
