
# def fib(n):

#     a = 0
#     b = 1
    
#     if n == 0:

#         print(a)
    
#     elif n == 1:

#         print(a)
#         print(b)

#     else:

#         print(a)
#         print(b)

#         for i in range(2,n):

#             number = a + b
#             a = b
#             b = number
#             print(number)

def fib(n):
 
    if n == 0:

        return(n)

    elif n == 1:

        return 1

    else:
    
        return fib(n-1) + fib(n-2)

n = 50

for i in range(0, n):
    
    print(fib(i))
# fib(5)