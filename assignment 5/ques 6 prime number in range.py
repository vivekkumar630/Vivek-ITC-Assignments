A=int(input("eneter the number"))
for number in range (A + 1):
    if number > 1:
        for i in range (2, number):
            if (number % i) == 0:
                break
        else:
            print (number)
