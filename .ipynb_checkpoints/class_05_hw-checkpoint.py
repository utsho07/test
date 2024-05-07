import re
text= "2 ball, 3 bat, 6 apple"
pattern= r"\d"
match= re.findall(pattern, text)
print(match)


text1= "The meeting is scheduled for 2024-05-06"
pattern1= r"\d{4}-\d{2}-\d{2}"

try:
    match1= re.search(pattern1, text1)
    print(match1.group())
except Exception as e:
    print(e)
    print(type(e))