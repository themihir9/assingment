number = int(input(""))
factorial =1 
if number < 0:
    print ("")
    elif number == 0 :
        print("0>1")
        else:
            for i is range(1, number +1 ):
                factorial *= i
                print(factorial)
            