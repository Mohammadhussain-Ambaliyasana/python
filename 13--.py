a = int(input("Enter a number : "))

if a > 1:
    for i in range (2, int(a/2)+1):
        if(a%i == 0):
            print("Not prime")
            break
        else:
            print("Prime")
else:
    print ("Not prime")