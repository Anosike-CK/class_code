# TERNARY OPERATOR

# user_input = input("please enter your name in CAPS")
# name = user_input if user_input.isupper() else "input was not upper case"
# print(name)

# score = int(input("please enter your student score : "))

# status = "Qualified" if score >= 60 else "Not qualified"

# print(status)

# student_is_qualified = True if score >= 60 else False

# if student_is_qualified:
#     print("\nsending mail to student\n")
#     print("Content: you have qualified for admision please visit our page to continue your registration")
    
# thing = {'key':{'key':['ooo','ppp']}}

# reg_thing= list(thing.keys())
# reg_thing_list= list(thing['key'].keys())

# print(reg_thing)

customer_email = input('Please enter your email address : ')
customer_password = input('Please enter a password for your login : ')
bank_data = {'zenith': {'chukwuagoziem anosike': ['chukwuagoziem anosike', 'M', 'Savings', 20816731, 0, 'chukwuagoziemanosike@yahoo.com', 'anosike500']}}

for keys in bank_data:
    # print(keys)
    for customers in bank_data[keys]:

        # print(customers)

        if customer_email == bank_data[keys][customers][-2] and customer_password == bank_data[keys][customers][-1]:
        
            break
    
        elif customer_email != bank_data[keys][customers][-2] and customer_password == bank_data[keys][customers][-1]:

            print('Your email or password is incorrect,please try again')
            

print(f'{customers} you have successfully logged on')