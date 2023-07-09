a = int(input("Enter a number: "))
if a % 2 == 0:
    print("The given number is even")
    t = a
    rev = 0
    while a > 0:
        digit = a % 10
        rev = rev * 10 + digit
        a = a // 10
    if t == rev:
        print("The number is a palindrome")
    else:
        print("Not a palindrome")
else:
    print("The number is odd")

    fact = 1
    if a < 0:
        print("Negative numbers are not accepted")
    else:
        for i in range(1, a + 1):
            fact = fact * i
        print("Factorial of the given number is:", fact)
        print("Number of digits:", len(str(fact)))
