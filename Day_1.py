# Nov_19-20_2026

# Task 1 - Ask for my name and age
print("Hello Welcome!")
User_name=input("Emter your full name ")
print("It's nice to have you back " + User_name)
User_age=int(input(User_name + ", how old are you now? "))


# Task 2 - Ask for my name, age and tell me how old i will be in 10 years 
User_name=input("Enter your full name ")
User_age=int(input("How old are you? "))
print(User_name + " in 10 years you will be " + str(User_age + 10) + " years old!")


# Task 3 - Tell me how much money i made
User_name=input("What is your name? ")
total_item_sold=int(input("How many orange did you sell? "))
cost_of_1_item=int(input("How much is 1 orange? (in Leonces) "))
total_earn=total_item_sold*cost_of_1_item
print(User_name + ", you made " + str(total_earn) + " Leonce!")


# Task 4 - Give back change to the customer
User_name=input("Enter your full name ")
total_cost_of_item=int(input("How much is the total? "))
amount_paid_by_customer=int(input("How much did the customer give you? "))
Customer_balance=amount_paid_by_customer-total_cost_of_item

if Customer_balance > 0:
    print(User_name + ", give back " + str(Customer_balance) + " Leones change!")

if Customer_balance == 0:
    print("Customer has no change, paid exact!")

if Customer_balance < 0:
    print(User_name + ", customer still need to add " + str(-Customer_balance) + " Leonces!")


# Task 5 - Give discount to the customer
User_name=input("Enter your full name ")
total=int(input("How much is the total? "))

if total >= 50000:
    print("You are a VIP! You get 5000 discount!")

elif total >= 20000:
    print("You get 1000 discount!")

else:
    print("No discount sorry!")


# Task 6 - Give discount to the customer and tell them how much they need to pay
User_name=input("Enter your full name ")
total=int(input("How much is the total? "))

if total >= 50000:
    discount=5000

elif total >= 20000:
    discount=1000

else:
    discount=0

final_total=total-discount
print(User_name + ", the final total is " + str(final_total) + " Leonce!")

paid=int(input("How much did the customer pay? "))
change=paid-final_total

if change > 0:
    print(User_name + ", give back " + str(change) + " Leones change!")

elif change == 0:
    print("Customer has no change, paid exact!")

else:
    print(User_name + ", customer still need to add " + str(-change) + " Leonces!")


# Task 7 
while True:
    User_name=input("Enter your customer name (or type 'close' to close the shop): ").lower()

    if User_name == "close":
        print("Shop closed! Good job!")
        break

    total=int(input("How much is the total? "))

    if total >= 50000:
        discount=5000

    elif total >= 20000:
        discount=1000

    else:
        discount=0

    final_total=total-discount
    print(User_name + ", the final total is " + str(final_total) + " Leonce!")

    paid=int(input("How much did the customer pay? "))
    change=paid-final_total

    if change > 0:
        print(User_name + ", give back " + str(change) + " Leones change!")

    elif change == 0:
        print("Customer has no change, paid exact!")

    else:
        print(User_name + ", customer still need to add " + str(-change) + " Leonces!")


# Task 8 - Keep track of how many customers you served and how much money you made
total_sales=0
total_customers=0
while True:
    User_name=input("Enter your customer name (or type 'close' to close the shop): ").lower()

    if User_name == "close":
        print("Today you served " + str(total_customers) + " customers.")
        print("Total you made " + str(total_sales) + " Leonces.")
        break

    total=int(input("How much is the total? "))

    if total >= 50000:
        discount=5000

    elif total >= 20000:
        discount=1000

    else:
        discount=0

    final_total=total-discount
    print(User_name + ", the final total is " + str(final_total) + " Leonce!")

    paid=int(input("How much did the customer pay? "))
    change=paid-final_total

    if change > 0:
        print(User_name + ", give back " + str(change) + " Leones change!")

    elif change == 0:
        print("Customer has no change, paid exact!")

    else:
        print(User_name + ", customer still need to add " + str(-change) + " Leonces!")

    total_sales = final_total + total_sales
    total_customers = total_customers + 1


# Task 9 - Keep track of how many customers you served, how much money you made and who your customers were
total_sales=0
total_customers=0
customer_list=[]
while True:
    User_name=input("Enter your customer name (or type 'close' to close the shop): ").lower()

    if User_name == "close":
        print("Today you served " + str(total_customers) + " customers.")
        print("Total you made " + str(total_sales) + " Leonces.")
        print("Today's customers were:")
        print(customer_list)
        break

    customer_list.append(User_name)

    total=int(input("How much is the total? "))

    if total >= 50000:
        discount=5000

    elif total >= 20000:
        discount=1000

    else:
        discount=0

    final_total=total-discount
    print(User_name + ", the final total is " + str(final_total) + " Leonce!")

    paid=int(input("How much did the customer pay? "))
    change=paid-final_total

    if change > 0:
        print(User_name + ", give back " + str(change) + " Leones change!")

    elif change == 0:
        print("Customer has no change, paid exact!")

    else:
        print(User_name + ", customer still need to add " + str(-change) + " Leonces!")

    total_sales = final_total + total_sales
    total_customers = total_customers + 1


# Task 10
total_sales=0
total_customers=0
customer_list=[]
menu = {"rice": 50000, "oil": 30000, "sugar": 20000, "soap": 10000}
while True:
    User_name=input("Enter your customer name (or type 'close' to close the shop): ").lower()

    if User_name == "close":
        print("Today you served " + str(total_customers) + " customers.")
        print("Total you made " + str(total_sales) + " Leonces.")
        print("Today's customers were:")
        print(customer_list)
        break

    customer_list.append(User_name)

    item=input("What do you want to buy? (rice, oil, sugar, soap) ").lower()
    total=menu[item]
    print("This is " + item + " is " + str(total) + " Leonces!")

    if total >= 50000:
        discount=5000

    elif total >= 20000:
        discount=1000

    else:
        discount=0

    final_total=total-discount
    print(User_name + ", the final total is " + str(final_total) + " Leonce!")

    paid=int(input("How much did the customer pay? "))
    change=paid-final_total

    if change > 0:
        print(User_name + ", give back " + str(change) + " Leones change!")

    elif change == 0:
        print("Customer has no change, paid exact!")

    else:
        print(User_name + ", customer still need to add " + str(-change) + " Leonces!")

    total_sales = final_total + total_sales
    total_customers = total_customers + 1


