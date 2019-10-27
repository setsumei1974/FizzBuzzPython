def FizzBuzz(x):
    if (x % 3 == 0) and (x % 5 == 0):
        return "FizzBuzz"
    if x % 3 == 0:
        return "Fizz"
    if x % 5 == 0:
        return "Buzz"
    return x

Response = int(input("Please select a number between 1 and 100.  "))
print(FizzBuzz(Response))