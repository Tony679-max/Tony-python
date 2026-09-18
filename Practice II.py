
try:

    marks = int(input("enter your marks:"))

    if marks > 100:
        print("Invalid marks !")
    elif marks < 0:
     print("Invalid marks !")

    else:
       if marks >= 80:
          print("A")
       elif marks >= 70:
          print("B")
       elif marks >= 60:
          print("C")
       elif marks >= 50:
          print("D")
       else:
          print("F")

except:
   print("Please enter a number !")

