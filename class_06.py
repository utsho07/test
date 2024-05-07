# #data structure

# #1) User define data structure
# #2) Build in data structure

# # list

# my_list= [1,2,3,4]
# sum=0

# for item in my_list:
#     sum=sum+item
    
# print(sum/len(my_list))

# # print(my_list.reverse)

# list1=[1,3,2,4,5]

# list1.sort()
# print(list1)
# list1.reverse()
# print(list1)



list=[1,2,3,4,5,6,7,8,9,10]
list1=[]

for i in list:
    if i%2==0:
        list1.append(pow(i,2))
        
print(list1)

squre_list= [i**2 for i in range(1,11) if i%2==0]
print(squre_list)

words= ["hello", "word", "python"]
length= [len(word) for word in words]
print(length)

list2="TheBlackFoxToA list"

list3=[]

for i in range(0, len(list2)):
    if list2[i].isupper():
        list3.append(list2[i])
        
print(list3)

my_table= (1,'a','c','c')

print(my_table.count('d'))
        