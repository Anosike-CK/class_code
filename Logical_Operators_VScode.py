#LOGICAL OPERATORS ARE USED TO WRITE CONDITIONAL STATEMENTS

# a = 10 > 5
# b = 5 < 3

# c = a and b  #CHECK BOTH OPERANDS LOGICAL TRUTH AND PRINTS RESULT ACCORDING TO THE AND METHOD
# d = a or b   #CHECK BOTH OPERANDS LOGICAL TRUTH AND PRINTS RESULT ACCORDING TO THE OR METHOD
# e = not(a or b)  #CHECKS FOR VALUES IN A OR B. IF THERE IS A VALUE, IT PRINTS FALSE. ELSE IT PRINTS TRUE

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

t = True
f = False

print("For AND operator")

print(t and t)
print(t and f)
print(f and f)
print(f and f)

print("\n For OR operator")
print(t or t)
print(t or f)
print(f or t)
print(f or f)

print("\n For IN operator")
name = "Adebayo"      
print("x" in name)  #print false because 'x' is not a member in name
print("a" in name)  #print true because 'a' is in name

print("x" not in name, "after adding not logigical operator")  #print true because not negatesthe original answer

