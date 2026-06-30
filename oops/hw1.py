from reportlab.pdfgen import canvas
class product:
    def __init__(self,id,name,brand,mfg,exp,qty,price):
        self.id = id
        self.name = name
        self.brand = brand
        self.mfg = mfg
        self.exp = exp
        self.qty = qty
        self.price = price

p1 = product(101,"creamy","lays",2026,2028,22,40)
p2 = product(102,"spicy","lays",2024,2028,39,45)
p3 = product(103,"classic","balaji",2025,2027,65,30)
p4 = product(104,"chilli","balaji",2022,2027,23,20)
all_prod = [p1,p2,p3,p4]

def print_all(all):
    for i in all:
            print("Product ID:",i.id)
            print("Name:",i.name)
            print("Brand:",i.brand)
            print("Manufacturing date:",i.mfg)
            print("Expiry date:",i.exp)
            print("Available Quantity:",i.qty)
            print("price:",i.price)
            print("---------------------------------------")


while True:
    print("Hello.. please select any option\n1.all details\n2.search\n3.purchase\n4.exit")
    ch = int(input("Enter your choice:"))
    match ch:
        case 1:
            print_all(all_prod)
        case 2:
            print("select from below:\n1.brand\n2.name")
            ch1 = int(input("Enter your choice:"))
            match ch1:
                case 1:
                     brand_1 = input("Enter brand name to search:")
                     for i in all:
                        if i.brand == brand_1:
                            print("---------------------------------------")
                            print("Product ID:",i.id)
                            print("Name:",i.name)
                            print("Brand:",i.brand)
                            print("Manufacturing date:",i.mfg)
                            print("Expiry date:",i.exp)
                            print("Available Quantity:",i.qty)
                            print("price:",i.price)
                            print("---------------------------------------")

                case 2:
                    name_1 = input("Enter product name to search:")
                    for i in all:
                        if i.name == name_1:
                            print("---------------------------------------")
                            print("Product ID:",i.id)
                            print("Name:",i.name)
                            print("Brand:",i.brand)
                            print("Manufacturing date:",i.mfg)
                            print("Expiry date:",i.exp)
                            print("Available Quantity:",i.qty)
                            print("price:",i.price)
                            print("---------------------------------------")

        case 3:
            pid = int(input("Enter Product ID: "))
            buy_qty = int(input("Enter Quantity to purchase: "))

            for i in all_prod:
                if i.id == pid:
                    if buy_qty <= i.qty:
                        i.qty -= buy_qty
                        total = buy_qty * i.price

                        print("Purchase Successful")
                        print("Remaining Quantity:", i.qty)
                        print("Total Bill:", total)

                        bill = input("Do you want to save the bill? (y/n): ")

                        if bill == "y":
                            name = input("Enter Customer Name: ")

                            pdf = canvas.Canvas(f"{name}_bill.pdf")

                            pdf.drawString(100, 800, "PURCHASE BILL")
                            pdf.drawString(100, 780, f"Customer Name : {name}")
                            pdf.drawString(100, 760, f"Product ID : {i.id}")
                            pdf.drawString(100, 740, f"Product Name : {i.name}")
                            pdf.drawString(100, 720, f"Brand : {i.brand}")
                            pdf.drawString(100, 700, f"Quantity : {buy_qty}")
                            pdf.drawString(100, 680, f"Price : {i.price}")
                            pdf.drawString(100, 660, f"Total Bill : {total}")

                            pdf.save()

                            print(f"Bill saved as {name}_bill.pdf")

                    else:
                        print("Insufficient Stock")
                    break
            else:
                print("Product Not Found")

        case 4:
            break         
                    