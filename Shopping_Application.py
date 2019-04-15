
# products_category = {'clothing': {
#                 'T-shirt': [('white',  300), ('black', 400), ('velvet',  500)],
#                 'Shoe': [('black', 5000), ('blue', 3000), ('brown', 4000)]},
#                 'Confectionery':{'chocolates':300, 'biscuits':100, 'lollipop':10},
#                 'Food':{'beans':100,'fish':200, 'rice': 200, 'garri':300, 'meat':400}
#                 }
products_category = {'clothing': {
                'T-shirt':  300, 
                'Shoe': 5000},
                'Confectionery':{'chocolates':300, 'biscuits':100, 'lollipop':10},
                'Food':{'beans':100,'fish':200, 'rice': 200, 'garri':300, 'meat':400}
                }

cart = []
def add_Item(consumer,Item, Price):


    # if consumer == 'consumer':

    #     cart.append(Item)

    # else:

    #     products[Item] = Price
    pass

def delete_Item():

    pass

def bill():

    pass


while True:

    prompt = input('please what do you want to do : ')

    if prompt == 'a' or 'y':

        print('CATEGORY'.center(15), 'SUB-CATEGORY'.center(13), 'PRICE'.center(10))

        for key in products_category:
            
            for item_key in products_category[key]:

                item = products_category[key]
                price = products_category[key][item_key]

                print(key.center(15), item_key.center(13), str(price).center(10))
        
        prompt = input('what do you want to add? ')
        if prompt in item:

            cart.append(prompt)
            print(f'you now have {cart} in your cart')

        prompt = input('do you want to add another item? y/n')
        if prompt == 'n':

            crt = ' , '.join(cart)
            bill = 0
            for items in cart:

                bill += price

            print(f'you have {crt} in your cart and your total bill is ₦{bill}')

    


 

                   


        # consumer_response = input('what do you want to add : ')
        # add_Item('consumer', consumer_response,0)
    
    # print(cart)