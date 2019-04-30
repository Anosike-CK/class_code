import ast
import random

class Bank:


    def __init__(self, bankname, bankcode, customer = ''):

        self.bankname = bankname
        self.bankcode = bankcode
        self.customer = customer

    def createAccount(self):

        print(f'Welcome to {self.bankname} bank ')

        customer_name = input('Please enter your full name : ')
        self.customer = customer_name
        customer_sex = input("""Are you male or female? please use 'M/F' to indicate""")
        account_type = input('What kind of account would you like to open with us today? Savings or Current')
        customer_email = input('Please enter your email address : ')
        customer_password = input('Please enter a password for your login : ')
        print('well done you have successfully created an account with us')
        random_gen = ''
        
        for n in range(4):
            n = random.randint(0,10)
            n = str(n)
            random_gen += n

        account_number = int(self.bankcode + random_gen)
        Customer_profile = CustomerProfile(customer_name, customer_sex,account_type,account_number,0,customer_email,customer_password)
        Storage(self).save(Customer_profile)
        print(f' your account number is {account_number}')

      
    def customer_login(self):        

        user_name = input('Please enter your user name : ')
        customer_password = input('Please enter a password for your login : ')
        bank_data = Storage(self).read()
        try:
            print(bank_data[user_name])
            if bank_data[user_name]['password'] == customer_password:

                print("logged in")
                
            else:
                print("incorrect authentication data")
                
        except:
            print("incorrect authentication data")
        

        return [user_name, True]
            
    def view_profile(self):

        login_details = self.customer_login()
        customer = login_details[0]
        login_status = login_details[1]
        is_customer_logged_in = True if login_status == True else False

        if is_customer_logged_in is True:

            profiles = Storage(self).read()
            customer_profile = profiles[customer]
            print('Hello {}:\t\n'.format(customer))
            print('Name'.center(13), 'Account Type'. center(30), 'Account Number'.center(5), 'Account Balance'.center(10))

            print(customer_profile['name'].center(13), customer_profile['account type'].center(30),  str(customer_profile['account number']).center(10),  str(customer_profile['account balance']).center(15))

            
class CustomerProfile:

        def __init__(self, name, sex, account_type,account_number, account_balance, email,password):

            self.name = name
            self.sex = sex
            self.account_type = account_type
            self.account_number = account_number
            self.account_balance = account_balance
            self.email = email
            self.password = password


class Storage:

    def __init__(self, bank):

        self.bank = bank
    
    def save(self,profile):

        customer_profile = {}
        data = self.__read_all()
        reg_banks = list(data.keys())
        customer_profile[profile.name] = {'name':profile.name, 'sex':profile.sex, 'account type': profile.account_type, 'account number':profile.account_number, 'account balance':profile.account_balance,'email':profile.email,'password':profile.password}

        if self.bank.bankname in reg_banks:

            data[self.bank.bankname][profile.name] = customer_profile[profile.name]

        elif self.bank.bankname not in reg_banks:

            data[self.bank.bankname] = {}
            # data[self.bank.bankname].append(customer_profile)
            data[self.bank.bankname][profile.name] = customer_profile[profile.name]

        with open('bank.txt', 'w') as file:
            file.writelines(str(data)) 
            file.close()


    def __read_all(self):

        with open('bank.txt', 'r') as file:

            data = file.read()
            file.close()

        return {} if len(data) < 1 else ast.literal_eval(data)

    def read(self):

        with open('bank.txt', 'r') as file:

            data = file.read()
            file.close()

            try:

                return {} if len(data) < 1 else ast.literal_eval(data)[self.bank.bankname]

            except:

                return {{'NONE': 'NO BANK DATA YET'}}

# zenith = Bank('zenith','2081')
access = Bank('Access', '2097')
# access.createAccount()
# zenith.createAccount()
# access.customer_login()
access.view_profile()