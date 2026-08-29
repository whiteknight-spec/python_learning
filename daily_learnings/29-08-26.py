#length of a string
"""a=" python, java"
print(len(a))
print(a[0])
print(a[-1])
print(a[:3])
print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a.strip())
print(a.replace("java","css"))
print(a.count("a"))
print(a.find("j"))

#ask the user for input and check its a number

numb=input()
if numb.isdigit():
    print("its a number") 
else:
    print("not a number")

#convert a sentence in to a list

a="i like python"
words=a.split()
print(words)

# join a list in to a string

a=['i', 'like', 'python']
text=" ".join(a)
print(text)

#print every char

txt="python"
for i in txt:
    print(i)

#count vowels

txt="python is my pet"
count=0
for i in txt:
    if i in "aeiou":
        count+=1
print(count)"""

#check palindrome

a=input()
if a==a[::-1]:
    print("its a palindrome")
else:
    print("not a palindrome")    