# list1 = ['physics', 'chemistry', 'bible studies', 1997,2001,2006]
# list2 = ['Igbo', 'yoruba', 'hausa']

# # print(list1)
# # print(list1[0])  #prints the value of index 0 in list 1
# print(list1[0:3])  # print elements of the index 0 - 2

# # list1.remove('physics') # to remove physics from list1
# # #del list1[1] # also another way to delete an element in the sequence list1
# # list1.pop(1)  # pop is used to also delete an element directly using the index as a reference
# # print(list1)


# # print(len(list1))  # this is to print the total length of list 1

# # print(list1 + list2)  # + is used to concatenate list1 and list2

# # print(list2 * 2) # this is used to replicate the elements of list 2 twice

# # print('Igbo' in list2)  # used to check if 'igbo' can be found in list2

# # for elements in list2: # this is used to iterate through every element in the list
# #     print(elements)    # print the elements

# # #indexing, slicing and matrices

# # print(list2[-1])   # this is using the negative indexing to print from the end of the list

# # #BUILT IN MEHODS AND FUNCTIONS
# # print(max(list2))   # used to find the maximum element in list2
# # print(min(list2))  # used to find the minimum in list2

# a = ('love', 'triump', 'hate', 'pepperdem')
# e = [2000,2015,2001,2007]
# b = list(a)
# print(b)  # use the list to convert a tuple to a list

# sorted_b = sorted(b) # used to store the sorted version of a list
# #print(b)
# print(sorted_b)

# b.sort(reverse = True)  # sorts list b in the reverse alphabetical order
# print(b)


# e.sort() # to sort the list e in an ascending order
# print(e)

# e.sort(reverse = True)  # this is used to reverse the sorting order from ascending to descending
# print(e)



# b.append('art')  #used to append'art' to the end of the list 
# print(b)

# b.insert(1, 'desire')  #used to append 'desire' to index 1
# print(b)

# b.extend(e)  #we use extend to extend the originl list in such a way that it collets the elements from another list e
# print(b)


# print(sum(e)) # to sum up the elements of an integer list

# print(b.index('love')) # use the index method to search for the index of an element in a list

# courses = ['HIstory', 'Math','Physics','CompSci']

# for index, course in enumerate(courses):  # enumerate in this instance is used to get the index of the elements
#     print(index, course)


#list comprehension
name = 'ada'
my_number_with_list_comp = [i for i in name]

print(my_number_with_list_comp)

numbers = [x for x in range(20)]             # Creat a list form 0 - 5
squared = [x ** 2 for x in numbers]

# print(squared)


x_bar = sum(numbers) / len(numbers)
# print(x_bar)

x_xbar = [x - x_bar for x in numbers]
print(x_xbar)

# # iterative enumeration with ternary operator
# combs =[(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(combs)

# combs = []

# for x in range(1,4):
#     for y in (3,1,4):
#         if x != y:
#             combs.append((x,y))
# print(combs)

# negativ_nums = x_xbar[0:10:1]
# print(negativ_nums)


# positiv_nums = x_xbar[10:-1]
# print(positiv_nums)

# positiv_nums = x_xbar[10:-1:2]
# print(positiv_nums)


# positiv_nums = x_xbar[::-1]
# print(positiv_nums)

# products = ["dried beans", "canned corn", "jewelry", "quality furniture", "automobile parts"]

# reversed_products = products[::-1]
# #print(reversed_products)


# number = [('ade', 1220031203),('jolade',1220031205),('shade',1220031208),('azeez',1220031209)]

# print("Name".center(10),'ID'.center(5),"\n")

# # for student in number:

# #     print(f'{student[0]}'.center(10), f'{str(student[1])[-3:]}'.center(5))

# for student in number:
#     print(student[0])
#     for letter in student[0]:
#         print(letter)

    
# a = ''.join(student[0])
# print(f'{a}')