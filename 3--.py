a = int(input("Enter a side : "))
b = int(input("Enter b side : "))
c = int(input("Enter c side : "))

s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5

print (area)
