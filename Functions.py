# def do_something():
#     """ this function does absolutely nothing you cheeky geezer"""
#     if True:
#         print("hello function")
# do_something()

# def greet(person):

#     #person = capitalize(person)
#     print(f'Hello {person}')

# def capitalize(word):

#     return word.capitalize()

# users = ['Bola', 'attah', 'shayo']
# for user in users:

#     user = capitalize(user)
#     greet(user)

# def dict_sum(_dict):
    
#     sum = 0
#     for key in _dict:
#         print(sum)
#         sum += _dict[key]

#     print(sum)


# students_per_class = {'ss1':15, 'ss2':20, 'ss3':34 }

# dict_sum(students_per_class)

# def calculate_fraction():
#     frac1 = (tuple(input('first frac : ').split('/')))
#     frac2 = (tuple(input('second frac : ').split('/')))
#     num1,den1 = int(frac1[0]), int(frac1[1])
#     num2,den2 = int(frac2[0]), int(frac2[1])
    
#     numerator1 = den2 * num1
#     numerator2 = num2 * den1
#     numerator = numerator1 + numerator2
#     denominator = den1 * den2

#     return(f'{numerator}/{denominator}')

# # def simplify_fraction(val):

# #     val = val.split('/')
# #     numerator = int(val[0])
# #     denominator =  int(val[1])
# #     print(f'{numerator} / {denominator}')

# #     i = 0
# #     while i < 50:

# #         for j in range(1,10):

# #             if numerator % j != 0 and denominator % j != 0:
# #                 pass

# #             elif ((numerator % j == 0) and (denominator % j == 0)):

# #                 numerator = numerator / j
# #                 denominator = denominator / j
# #         i += 1
        
# #     print(f'Your fractional value is : {numerator} / {denominator}')

# def simplify_fraction(val):

#     val = val.split('/')
#     numerator = int(val[0])
#     denominator =  int(val[1])
#     print(f'{numerator} / {denominator}')


#     for i in reversed(range(2,11)):

#         while numerator % i == 0 and denominator % i == 0:
            
#             numerator = numerator / i
#             denominator = denominator / i
#             print(numerator % i == 0 and denominator % i == 0)

        
#     print(f'Your fractional value is : {numerator} / {denominator}')
# simplify_fraction(calculate_fraction())

# def name_concat(name, surname):

#     fullname = surname + ' ' + name 

#     print(fullname)

# name_concat(username, user_surname) # Positional args

# name_concat(surname = username, name = user_surname) # Keyword args

# def name_concat(name, surname, age, sex, mood):

#     fullname = f'My name is {surname} {name} i am a {age} years old {sex} and i am {mood}'

#     print(fullname)
    
# user_name = input('please enter your name : ')
# user_surname = input('please enter your surname : ')
# user_age = input('How old are you : ')
# user_sex = input('Are you male/female : ')
# user_mood = input('How do you feel today : ')

# name_concat(user_name, user_surname, user_age, sex = user_sex, mood = user_mood) #Due to the nture of positional and key word args, positional arguments always comes befor keyword arguments

# names = ['Dele', 'Bolu', 'sule', 'Bala'],
# surnames = ['Momodu', 'Ogunse', 'Gimba', 'Bature'],
# ages = [29, 17, 25, 40],
# sexes = ['male', 'female', 'male', 'male'],
# moods = ['happy', 'happy', 'indifferent', 'just there']


# def name_concat(name,surname,age,sex,mood):

#     fullname = f'My name is {surname} {name} i am a {age} years old {sex} and i am {mood}'

#     print(fullname)

# for detail in zip(names,surnames, ages, sexes, moods):

#     name_concat(detail[0], detail[1], detail[2], detail[3], detail[4])
#print(synonym)

# for person in names:

#     index = names.index(person)
#     name_concat(person, surnames[index], ages[index], sexes[index], [moods[index]])

# index = 0

# while index < len(names):

#     name_concat(person, surnames[index], ages[index], sexes[index], [moods[index]])
#     index += 1    

# def variable_args(*v_args, **v_kwargs):

#     print(v_args)
#     print(v_kwargs)

#     for arg in v_args:

#         print(arg)
    
#     for key in v_kwargs:

#         print(key, v_kwargs[key])

# variable_args(1,2,3,4,5,"hello", [1,2,3,4,5], greeting = "hello", name = "miniso", drama = "sequel")

list1 = ['beans','fish',29,15]

print(list1[:1], list1[1], list1[2:])
