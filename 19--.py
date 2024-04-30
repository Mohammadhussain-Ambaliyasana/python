lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
for num in range(lower, upper + 1):
    sum = 0
    temp = num
    l = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum += digit ** l
        temp //= 10
    if num == sum:
        print(num)