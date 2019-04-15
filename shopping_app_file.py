import ast
# products_category = {'clothing': {
#                 'T-shirt': [('white',  300), ('black', 400), ('velvet',  500)],
#                 'Shoe': [('black', 5000), ('blue', 3000), ('brown', 4000)]},
#                 'Confectionery':{'chocolates':300, 'biscuits':100, 'lollipop':10},
#                 'Food':{'beans':100,'fish':200, 'rice': 200, 'garri':300, 'meat':400}
#                 }
# products_category = ''''{'clothing': {'T-shirt':  300, 'Shoe': 5000},
#                 'Confectionery':{'chocolates':300, 'biscuits':100, 'lollipop':10},
#                 'Food':{'beans':100,'fish':200, 'rice': 200, 'garri':300, 'meat':400}}'''


products_file = open('products.txt', 'r')
products_category = ast.literal_eval(products_file.read())
# product_category = ast.literal_eval(product_category)
products_file.close()


un_categorized_products = {}

cart = []

def display_stock():

    print('CATEGORY'.center(15), 'SUB-CATEGORY'.center(13), 'PRICE'.center(10))

    for key in products_category:

        for item in products_category[key]:

            un_categorized_products[item] = products_category[key][item]
            price = products_category[key][item]
            print(key.center(15), item.center(13), f'₦{str(price)}'.center(10))


def add_Item(consumer,_object):

    if consumer == 'consumer':

        cart.append(_object)

    elif consumer == "admin":

        products_category[_object[0]][_object[1]] = _object[2]
        print(products_category)

def remove_Item(consumer, item):

    if consumer == 'consumer':

        if item in cart:

            cart.remove(item)

    elif consumer == 'admin':

        del un_categorized_products[item]

def bill(item):

    bill = 0
    
    for item in cart:

        for key in item:

            cost = item[key]
            bill += cost

    return bill
        

while True:

    print('welcome to the shopping store')
    prompt = input('please what do you want to do : ')

    if prompt == 'add':

        display_stock()
        prompt = input('what do you want to add? ')

        add_Item("consumer",{prompt:un_categorized_products[prompt]})
        print(f'you now have {cart} in your cart')
        
        continue
    elif prompt == 'bill':

        print('Your total bill is', '₦',bill(cart))

    elif prompt == 'remove':

        print(f'you have {cart}')

        delete = input('what you you want to delete? ')
        remove_Item('consumer', {delete:un_categorized_products[delete]})
        print(cart)

    elif prompt == 'admin':

        while prompt == 'admin':

            prompt = input('do you want to add or remove? ')

            if prompt == 'add':

                key = input('what is the product category? ')
                item_name = input('what do you want to add? ')
                item_price = int(input('how much is the item? '))

                add_Item('admin', [key,item_name, item_price])
                open('products.txt', 'w').write(str(products_category))



            prompt = input('are you finished? y/n')

        if prompt == 'y':

            continue

        

        #     print(f'you have {crt} in your cart and your total bill is ₦{bill}')
    
# _object = [{'beans':300}, {'fish':400}]
# delt = {'beans':300}
# for i in _object:
#     for key in i:
#         print(i[key])

# if delt in _object:

#     _object.remove(delt)
#     print(_object)

# cart = dict(_object)

# print(cart)
    


 

                   


        # consumer_response = input('what do you want to add : ')
        # add_Item('consumer', consumer_response,0)
    
    # print(cart)