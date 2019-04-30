# LOOP STATEMENTS ALLOWS US TO EXECUTE A STATEMENT OR GROUP OF STATEMENTS MULTIPLE TIMES

#WHILE LOOP 
# THS CODE COUNTS NUMBERS FROM 0-8 AND 
#TERMINATES WHEN COUNT == 8 
# count = 0
# while (count < 9):
#     print("The count is : ", count)
#     count += 1
# else:
#     print("It is nice running you")


# # FOR LOOP
# # THIS EXAMPLE IS USED TO DESCRIBE HOW FOR LOOPS ARE USED FOR BOTH STRINGS AND LISTS
# # THIS EXAMPLE PRINTS THE LETTERS OF A STRING ONE AFTER THE OTHER 
# # THE SECOD EXAMPLE PRINTS THE ITEMS IN A LIST
# for letter in 'Python':     # First Example
#    print ('Current Letter :', letter)

# # fruits = ['banana', 'apple',  'mango']
# # for fruit in fruits:        # Second Example
# #    print ('Current fruit :', fruit)

# # print ("Good bye!")

# fruits = ['banana', 'apple',  'mango']
# length = len(fruits)
# for index in range(length): # iterate by the index in the list fruits
#     print("CURRENT FRUIT : ", fruits[index])
# # USING FOR LOOP WITH  CONDITIONAL STATEMENTS
# # THIS NEXT CODE FINDS OUT PRIME AND NON PRIME NUMBERS WITHIN A RANGE OF NUMBERS

# for num in range(100,110):                                  # TO ITERATE BETWEEN 10 TO 20
#     for i in range(2,num):                                   # TO ITERATE ON THE FACTORS OF THE NUMBERS
#         if (num % i == 0):                                     #TO DETERMINE THE FIRST FACTOR
#             non_prime = num / i                             # TO DETERMINE THE SECOND FACTOR
#             print('%d equals %d * %d'%(num, i, non_prime))
#             break                                           #to move to the next number, the #first FOR  else part of the loop
#     else:
#         print (num, "is a prime number")

# num = 1
# while num < 10:
#     i = 2
#     while (i <= (num / i)):
#         if not(num % i): break
#         i = i + 1
#     if (i > num / i) :
#         print(num, " is prime number")
#     num = num + 1

# for number in range(100,200):
#     for divisible in range(5,number):
#         if (number % divisible == 0):
#             number_divide = number / divisible
#             print("%i equals %i * %i and is not a prime number"%(number,divisible,number_divide))
#             break
#     else:
#         print(number,"is a prime number")

# # break state ment as used in python to terminate the current loop 
# # and start with the next statement 
# for letter in 'python':
#     print('current letter : ', letter)
#     if letter == 'h':
#         break
# #continue statement which rejects all the remaining statement in the current iteration of the loop
# #and moves control back to the topof the loop
# for letter in 'python':
#     if letter == 'h':
#         continue
#     print('current letter : ', letter)


# word = "Microparamecium"
# print(word[4])   

# for i in range(200):
#         print(i)

# for letter in 'chukwuagoziem':
#         print(letter)
# print(list('chukwuagoziem'))

# for number in reversed(range(20,40)):
#         print(number)


# word = "Microparamecium"

# index = 0

# while index < 15:

#         print(word[index])
#         index += 1


# i = 0
# while i < 5:     # This is an infinite loop
#         print(i)


# The codes below find even numbers within a range of values

# i = 0

# while i < 50:

#         if (i % 2 == 0): print(f"{i} is an even number")
#         i += 1

# for i in range (50):

#         if (i % 2 == 0): print(f"{i} is an even number")

# # The codes below find odd numbers within a range of values

# for i in range (50):

#         if (i % 2 != 0): print(f"{i} is an even number")

#Odd number counter

# number_odd = 0
# number_even = 0

# for i in range (50):

#         number_even += 1

#         if (i % 2 != 0): 

#                 print(f"{i} is an even number")
#                 number_odd += 1
#                 number_even += 1                #if only we get an odd number subtract the even counter by 1 
# print(f"The total odd number is {number_odd}")
# print(f"The total even number is {number_odd}")



# for i in range (50):

#         number_even += 1

#         if (i % 2 != 0): 

#                 print(f"{i} is an even number")
#                 number_odd += 1       #increase odd number count
#         else:
#                 number_even += 1      #increase even number count
        