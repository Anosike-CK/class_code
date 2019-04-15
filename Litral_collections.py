# fruits = ["apple", "mango", "orange"] # List literal
# numbers = (1,2,3) # tuple literal
# alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} # dictionary literal
# vowels = {'a', 'e', 'i', 'o', 'u'} #set literal

# print(fruits)
# print(numbers)
# print(alphabets)
# print(vowels)



students = ["azeez","gozie","abibat","shayo","samuel","di'ja", "kunle","awele"]
students2 = ["azeez","gozie","abibat","shayo","samuel","di'ja", "kunle","awele"]

print(type(students))
print(type(students2))

# students.append(0) #adds 0 to the students list
# print(students)
# students.remove(0)  #removes 0 from the student list
# print(students)
# students.clear()    # clear the whole list
# print(students)
# students2.pop(2)
# print(students2)
print(students2.count(students2[1])) #prints how many times an object occurs in a list

strip = "obi is not coming back"
splitti = strip.split()
print(''.join(splitti))

