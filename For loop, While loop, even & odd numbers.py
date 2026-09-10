
# for loop
print("For loop:")

for number in range(1, 6):
    print(number)


# while loop
print("While loop:")

number = 1

while number <= 5:
    print(number)
    number += 1


# even/odd analysis
print("Even/Odd numbers:")

for number in range(1, 11):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")