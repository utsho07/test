try: 
    roll= int(input("Enter the roll number: "))
    if roll<1:
        raise IndexError
    else:
        print(f"roll number is {roll}")
    
except IndexError as e:
    print(e)
    print(type(e))
    
# print("successfully completed")

# string= "C:\path\to\file.txt"
# print(string)

# string1= r"C:\path\to\file.txt"
# print(string1)

#regualar expression function



# import re
# text= "The quick brown fox jump over the lazy dog"

# pattern = r"Fox"

# match= re.search(pattern, text, re.IGNORECASE)
# print(match.group())


# pattern1= r"o"
# match1= re.findall(pattern1, text)
# print(match1)

# new=re.sub(pattern,"cat", text,re.IGNORECASE)
# print(new)
#re.compile

import re
text= "apple, banana; cheryry -date"
pattern = r"[,;\s-]+"
tokens=re.split(pattern,text)
print("Token: ", tokens)


text1= "apple123banna234cherry7789date"
pattern1= r"\d+"

tokens1= re.split(pattern1, text1)
print(tokens1)

text3= "The event is schedule for 2024-05-10"

pa= r"\d{4}-\d{2}-\d{2}"
m= re.search(pa,text3)
print(m.group())

text2="Islamic university,ict dept"

pat= r"[aeiou]"
ans= re.findall(pat,text2)
print(ans)