rows = int(input("Enter Right Triangle  Rows = "))

print("The Right Triangle of Consecutive Alphabets Pattern")
alphabet = 65

for i in range(rows):
    for j in range(i + 1):
        print('%c' %alphabet, end = ' ')
        alphabet = alphabet + 1
    print()
