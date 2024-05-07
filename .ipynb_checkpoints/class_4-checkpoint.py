#print the odd number between 0-10

# num=0
# while num<=10:
#     if num%2 == 0:
#         num+=1
#         continue
#     print(num ,end="")
#     num+=1

# i=1
# while i<=10:
#     if i==6:
#         i+=1
#         continue
#     print(i, end=" ")
#     i+=1


#list is a set of data .. we can enter different kind of data in a single list

# numbers= [1,2,3,"ict, dept",5]
# print(len(numbers))
# for num in numbers:
#     print(num, end=" ")

#range is a prebuild number which is used to 
# for num in range(2,20,2):
#     print(num, end=" ")

# number1= int(input("Enter a number: "))
# count= number1//2
# data = True



# for i in range(2, count+1):
#     if(number1%2==0):
#         data=False
    
# if data==True:
#     print("Is prime")
# else:
#     print("is not prime")


#define the range of number for the multiplication table 

# start= 1
# end =10

# for i in range(start,end+1):
#     for j in range(1,11):
#         result= i*j
#         print(f"{i} * {j}={result} ")
#     print(end="\n")
    
    
    
#error handling

# try:
#     print(10/0)
# except Exception as e:
#     print(e)
#     print(type(e))

try:
    result = 18 + "hello"
except Exception as k:
    print(k)
    print(type(k))
    
try:
    my_list= [1,2,3]
    print(my_list[3])

except Exception as e:
    print(e)
    print(type(e))
    
