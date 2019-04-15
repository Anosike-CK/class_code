item1_Name = input("please enter the first product name: ")
item1_Qty = int(input("please enter the first product quantity: "))
item1_Price = int(input("please enter the first product price: "))


item2_Name = input("please enter the second product name: ")
item2_Qty = int(input("please enter the second product quantity: "))
item2_Price = int(input("please enter the second product price: "))

item3_Name = input("please enter the third product name: ")
item3_Qty = int(input("please enter the third product quantity: "))
item3_Price = int(input("please enter the third product price: "))

item4_Name = input("please enter the fourth product name: ")
item4_Qty = int(input("please enter the fourth product quantity: "))
item4_Price = int(input("please enter the fourth product price: "))

##item1_Name = "Nike"
##item1_Qty = 45
##item1_Price = 23
##
##
##item2_Name = "shoes"
##item2_Qty = 4
##item2_Price = 300
##
##item3_Name = "Adidas"
##item3_Qty = 12
##item3_Price = 350
##
##item4_Name = "Puma"
##item4_Qty = 3
##item4_Price = 250




total_stock = ((item1_Qty * item1_Price) + (item2_Qty * item2_Price) + (item3_Qty * item3_Price) + (item4_Qty * item4_Price))
print("Name".center(13), "Qty".center(13), "Price".center(13), "Item_total".center(13), "\n")
print(item1_Name.center(13), str(item1_Qty).center(13), str(item1_Price).center(13), str(item1_Qty * item1_Price).center(13))
print(item2_Name.center(13), str(item2_Qty).center(13), str(item2_Price).center(13), str(item2_Qty * item2_Price).center(13))
print(item3_Name.center(13), str(item3_Qty).center(13), str(item3_Price).center(13), str(item3_Qty * item3_Price).center(13))
print(item4_Name.center(13), str(item4_Qty).center(13), str(item4_Price).center(13), str(item4_Qty * item4_Price).center(13))

print("Your total due payment is ", str(total_stock).center(26))

