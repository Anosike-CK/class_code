# a = 20
# b = 20

# if ( a is b ):
#    print ("Line 1 - a and b have same identity")
# else:
#    print ("Line 1 - a and b do not have same identity")

# if ( id(a) == id(b) ):
#    print ("Line 2 - a and b have same identity")
# else:
#    print ("Line 2 - a and b do not have same identity")

# b = 30
# if ( a is b ):
#    print ("Line 3 - a and b have same identity")
# else:
#    print ("Line 3 - a and b do not have same identity")

# if ( a is not b ):
#    print ("Line 4 - a and b do not have same identity")
# else:
#    print ("Line 4 - a and b have same identity")


# x = 20
# y = 30

# print(x is y)

# y = x
# print(x is y)

import random
b = ''
random_four = random.randrange(1,100)
for n in range(4):

   n = random.randint(1,9)
   n = str(n)
   b += n 
   print(n)
print(b)