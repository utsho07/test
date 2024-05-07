#control statement

#code->01
# x=int(input("Enter a number: "))
# if(x%2==0):
#     print("The number is even")
# else:
#     print("The number is odd")


# code->02  
# age = int(input("Enter the age: "))  

# if (0<= age <13):
#     print("child")
# elif(13<= age <20):
#     print("Teenage")
# elif(20<=age and age<60):
#     print("Adult")
# else:
#     print("senior citizen")


# code->3

# year=int(input("Enter the year: "))
# if((year%4==0) and ((year%100!=0) or (year %400==0) )):
#     print("The year is leap year")
# else:
#     print("The year is not a leap year")

# code->4

# num1= int(input("Enter the number 1 value: "))
# num2=  int(input("Enter the number 2 value: "))
# operator=  input("Enter any of this operation +,-,*,/,% : ")

# if(operator=="+"):
#     result = num1+num2
# elif(operator == "-"):
#     result = num1 -num2
# elif(operator == "*"):
#     result = num1*num2
# elif(operator == "/"):
#     result = num1/num2
# elif(operator == "%"):
#     result = num1%num2
# print(f"The result is {result}")

# code->5
dept ="ict,iu"
print(dept.upper())
print(dept.lower())

district = " kustia"
print(dept+district)
print(len(dept))
print(dept[0:5])
print(dept[2:])
print(dept[-1:-3:-1])

#find
bio= "i live in kushtia"
print(bio.find("kushtia"))

#replace
print(bio.replace("kushtia", "magura"))

#split
print(bio.split())