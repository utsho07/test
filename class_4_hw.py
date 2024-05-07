
# Exercise 1: Calculating Factorials with Exception Handling
# Write a Python program that prompts the user to enter a positive integer and calculates its factorial. Handle any input errors (e.g., non-integer input, negative integer input) using exception handling.
#exercise-1

# try:
#     input1=  int(input("Enter a number: "))
#     result=1
#     if input1>=0:
#         for i in range(1,input1+1):
#             result= result*i
#         print(result)
#     else:
#         print("Can't find factorial of the negative number")
        
            
# except Exception as e:
#     print(e)
#     print(type(e))
        
         
         
         
# Exercise 2: Password Verification with Exception Handling


# Write a Python program that prompts the user to enter a password and verifies whether the password meets certain criteria (e.g., minimum length, containing at least one uppercase letter and one digit) using exception handling

# excercise-2:
while True: 
    try: 
        password = input("Enter your password: ")
        
        if len(password) < 6:
            raise Exception("Password must be at least 6 letter")
        if not any(char.isupper() for char in password):
            raise Exception("Password must contain at least one uppercase letter")
        if not any(char.islower() for char in password):
            raise Exception("Password must contain at least one lowercase letter")
        if not any(char.isdigit() for char in password):
            raise Exception("Password must contain at least one digit")
        
        print("Your password is set.")
        break
    except Exception as e:
        print(e)


