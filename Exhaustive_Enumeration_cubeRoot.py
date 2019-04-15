
val = int(input("Enter a value"))
step = 0
ans = 0

for ans in range (0,val):
    if ans * ans * ans == val:
        print(f"The cube root of {val} is {ans}")





# while step < val:

#     multiple = step * step * step

#     if multiple - val <= 0.5 and multiple >= val:
#         print(f"""Approximate cube root od {val} is {step} 
#                 because {step} cube is {step ** 3}""")
#         break
#     step += 0.01
