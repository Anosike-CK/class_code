for i in range(100,999):

    val = str(i*3)
    adder = str(i)

    if val[0] == val[1] == val[2] == adder[len(adder)-1]:

        resp = f'{adder} + {adder} + {adder} = {val}'
        print(resp)
        break