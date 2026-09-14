# strengthening my PY skills
 
name = input("Enter your name: ")

valid = True

for letter in name:
    if not letter.isalpha() and letter != " ":
        valid = False

if valid:
    print("Thank you!")
else:
    print("Please enter a valid name!")

try:
    marks = int(input("Enter your marks:"))

    if marks > 100:
            print("maximum is 100 !")
    elif marks < 0:
        print("minimum is 0 !")

    else:
        if marks >= 70:
          print("A")
        elif marks >= 60:
          print("B")
        elif marks >= 50:
          print("C")
        else:
          print("F") 

except:
    print("please enter your marks !")

   

