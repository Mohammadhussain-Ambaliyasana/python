import math

def sqrtRoot(a,b,c):
    dis_form = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis_form))
    if dis_form > 0:
        print(" real and different roots ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))
    elif dis_form == 0:
        print(" real and same roots")
        print(-b / (2 * a))
    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val) 


a = int(input("Enter a number : "))
b = int(input("Enter b number : "))
c = int(input("Enter c number : "))

if (a==0):
    print("Enter a value")
else:
    sqrtRoot(a,b,c)