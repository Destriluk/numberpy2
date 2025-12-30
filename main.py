from math import sqrt
print("=======prime numbers========")
number = int(input("Enter number here :"))
print("  ")
if number > 1:
    for i in range(2,int(sqrt(number)) +1):
        if number % i == 0:
            print("the number is not a prime number :", number)
            break
    else:
        print("the number is a prime number:", number)
else:
    print("the number is not a prime number", number)