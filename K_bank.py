import ast
import random

class Bank:

    def __init__(self, bankname, bankcode):

        self.bankname = bankname
        self.bankcode = bankcode

    def createAccount(self):

        print(f'Welcome to {self.bankname} bank ')
        customer_name = input('Please enter your full name : ')
        customer_sex = input("""Are you male or female? please use 'M/F' to indicate""")
        account_type = input('What kind of account would you like to open with us today? Savings or Current')
        customer_email = input('Please enter your email address : ')
        customer_password = input('Please enter a password for your login : ')
        print('well done you have successfully created an account with us')
        random_gen = ''
        for n in range(4):
            n = random.randint(1,9)
            n = str(n)
            random_gen += n

        account_number = int(self.bankcode + random_gen)
        profile_view = ProfileView(customer_sex,account_type,account_number,0,customer_email,customer_password)
        Storage(self).save(profile_view)
        print(f' your account number is {account_number}')

      
    def login(self):

        customer_email = input('Please enter your email address : ')
        customer_password = input('Please enter a password for your login : ')

    
   

#         pass
#     pass

class Customer: 


    
    def view_profile(self):

        profiles = Storage(self).read()
        print('Hello {}, below are your notes:\t\n'.format(self.bankname.customer_name.upper()))

        for profile in profiles:
            print('\t{} {} {} {} {} {}\n'.format(profile[0], profile[1], profile[2],profile[3], profile[4], profile[5]))
    
    def make_transfer(self):

        pass

    
    def close_account(self):

        pass
    def make_deposit(self):

        pass
    
    def make_withdrawal(self):

        pass

    pass

class ProfileView:

        def __init__(self, sex, account_type,account_number, account_balance, email,password):

            self.sex = sex
            self.account_type = account_type
            self.account_number = account_number
            self.account_balance = account_balance
            self.email = email
            self.password = password

        pass

class Storage:

    def __init__(self, bank):

        self.bank = bank
    
    def save(self,profile):

        data = self.__read_all()
        reg_customers = list(data.keys())
        customer_profile = [profile.sex, profile.account_type,profile.account_number,profile.account_balance,profile.email,profile.password]
        if self.bank.customer_name in reg_customers:

            data[self.bank.customer_name].append(customer_profile)

        else:

            data[self.bank.customer_name] = []
            data[self.bank.customer_name].append(customer_profile)

        with open('first.txt', 'w') as file:
            file.writelines(str(data)) 
            file.close()


    def __read_all(self):

        with open('first.txt', 'r') as file:

            data = file.read()
            file.close()

        return {} if len(data) < 1 else ast.literal_eval(data)

    def read(self):

        with open('first.txt', 'r') as file:

            data = file.read()
            file.close()

            try:

                return {} if len(data) < 1 else ast.literal_eval(data)[self.bank.customer_name]

            except:

                return [['NONE', 'NO BANK DATA YET']]

zenith = Bank('zenith', '2081')
zenith.createAccount()
Customer.view_profile('zenith')