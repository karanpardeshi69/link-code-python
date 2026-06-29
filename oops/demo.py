class demo():
    inst_name = "Linkcode"
    def __init__(self):
        print("Default constructor called")

obj = demo()
print(demo.inst_name)
print(obj.inst_name)