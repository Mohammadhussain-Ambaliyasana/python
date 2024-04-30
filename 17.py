a = int(input("Enter limit number : "))
pre = 0
now = 1
print (pre)
print (now)
next = 0
for i in range (1,a+1):
    next = pre+now
    print (next)
    pre = now
    now = next
