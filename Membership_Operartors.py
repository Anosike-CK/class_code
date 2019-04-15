# MEMBERSHIP OPERATORS ARE USED TO CHECK FOR THE MEMBERSHIP OF A VARIABLE IN A SEQUENCE

a = 10
b = 20
num_list = [1, 2, 3, 4, 5 ]

if ( a in num_list ):
   print ("Line 1 - a is available in the given num_list")
else:
   print ("Line 1 - a is not available in the given num_list")

if ( b not in num_list ):
   print ("Line 2 - b is not available in the given num_list")
else:
   print ("Line 2 - b is available in the given num_list")

a = 2
if ( a in num_list ):
   print ("Line 3 - a is available in the given num_list")
else:
   print ("Line 3 - a is not available in the given num_list")

print("\n For IN operator")
name = "Adebayo"      
print("x" in name)  #print false because 'x' is not a member in name
print("a" in name)  #print true because 'a' is in name

print("x" not in name, "after adding not logigical operator")  #print true because not negates the original answer

print("\n mixing menbership operators with the logicaloperators for multiple tests\n")

test_list = [1,4,5,6,7,8]
print(1 in test_list, ", single test")

print(1 in test_list and 32 in test_list, ",multiple tests with 'AND' logical operator")

print(1 in test_list and 32 not in test_list, ",multiple tests with 'AND' logical operator and 'NOT' inverting factor")
print(1 in test_list and 32 not in test_list or 8 in test_list, ",multiple tests with 'AND' logical operator and 'NOT' inverting factor")
