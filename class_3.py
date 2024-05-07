#excercise_01

# a= input("Enter a strings that you want to reverse: ")
# length= len(a);
# print(length)
# while length >0:
#     print(a[length-1], end="")
#     length-=1
    
    

#excercise_02

inp= input("Enter the string that you want to count: ")
count= 0
length= len(inp)
i=0

while i<length:
    if inp[i] in "aeiouAEIOU": 
        count= count+1
    i+=1
    
print(f"The number of vowels is {count}")