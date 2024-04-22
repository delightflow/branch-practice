i=1
for i in range(16):
    if i%3!=0 and i%5!=0:
        print(i)
    elif i%5==0 and i%3!=0:
        print("buzz")
    elif i%3==0 and i%5!=0:
        print("fizz")
    else:
        print("fizzbuzz")

