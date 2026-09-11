# variables & data types
Student_name = "Ishimwe Tony"
print(Student_name)
print(type(Student_name))

#list, conditions & loops

Students_marks = [25,55,38,66,10,40]

for number in Students_marks:
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

#Functions

def great(name):
    print("Good luck",name)
    print("You gonna need it")
great("Turiho")
great("Calpephore")   

#file handling

file = open("students.txt", "w")
file.write("joshua")
file.write("Baraka")
file.close()

file = open("students.txt", "r")
Data = file.read()
print(Data)
file.close()

#  exception handling
try:
    age = int(input("Enter your age: "))
    print("thank you")
except:
    print("Please enter a number")

# class
class student:
    def __init__(self,name,age):
       self.name = name
       self.age = age
student = student("Kaliza", 22)

print(student.name)
print(student.age)





