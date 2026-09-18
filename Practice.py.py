# from chat

try:
    age = int(input("Enter your age:"))

    if age < 0:
     print("Invalid age")

    else:
     if age >= 18:
        print("Adult")

     else:
        print("Minor")

except:
 print("Please enter a number !")
 