drink = 'Available'
food = None

def menu(x):
    ''' use this function to test values of x'''
    if x == drink:
        print(drink)
    else:
        print(food)
menu(drink)
menu(food)
print(menu.__doc__)