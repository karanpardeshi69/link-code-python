menu = ((1,"Paneer",400),
        (2,"Chicken",600),
        (3,"Dessert",150),
        (4,"Noodles",350)
        )
order = []
while True:
    print("Hotel menu Card\n1.View menu\n2.Order\n3.View order\n4.Generate Bill\n5.Exit")
    ch = int(input("Enter your choice:"))
    match ch:
        case 1:
            print("items are:\nitem     id      price")
            for i in menu:
                print(f"item {i[0]}   {i[1]}   {i[2]}")
        case 2:
            item_id = int(input("Enter item Id:"))
            for i in menu:
                if item_id == i[0]:
                    item_qty = int(input("Enter item Quantity:"))
                    amount = i[2]*item_qty
                    order.append([i[1],item_qty,amount])
                    print("Order added")
        case 3:
            print("Your order")
            for i in order:
                print(i)
        case 4:
            total_bill = 0

            print("---------------- BILL ----------------")
            print("Item\tQty\tAmount")

            for i in order:
                print(i[0], "\t", i[1], "\t", i[2])
                total_bill += i[2]

            gst = total_bill * 18 / 100
            final_amount = total_bill + gst

            print("------------------------------------------")
            print("Subtotal:", total_bill)
            print("GST (18%) :", gst)
            print("Final Amount :", final_amount)
            
        case 5:
            print("Thank You....!! Visit Again....!!")
            break
        case _:
            print("Invalid Choice")