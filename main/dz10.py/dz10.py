a = int(input())
if a % 3 == 0:
    print("Fizz", end=' ')
if a % 5 ==0:
    print("Buzz", end=' ')
if a % 3 == 0 and a % 5 == 0:
    print("FizzBuzz", end=' ')
else:
    print(a, end=' ')