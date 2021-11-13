end_value = int(input("Enter the end value. "))
c = 0
while c <= end_value - 1: 
    c+=1
    if c % 5 == 0: 
        print("PASS")
    else: 
        print(c)
        