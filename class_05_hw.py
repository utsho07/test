import re
text= "2 ball, 3 bat, 6 apple"
pattern= r"\d"
match= re.findall(pattern, text) 
print(match)


text1= "The meeting is scheduled for"
pattern1= r"\d{4}-\d{2}-\d{2}"

try:
    match1= re.search(pattern1, text1)
    if match1: 
     print(match1.group())
    else:
        raise IndexError
except Exception as e:
    print(e) 
    print(type(e))