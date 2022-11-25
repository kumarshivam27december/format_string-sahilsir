Skip to content
Search or jump to…
Pull requests
Issues
Codespaces
Marketplace
Explore
 
@kumarshivam27december 
sash9696
/
python-cipher
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
python-cipher/format.cpp
@sash9696
sash9696 Add files via upload
Latest commit c3440e2 1 minute ago
 History
 1 contributor
37 lines (19 sloc)  751 Bytes


#age = 20

#print('My name is John. My age is' + age)

#format()

#age = 20

#text = 'My name is John. My age is {}'

#print(text.format(age))

quantity = 5
items = 3
money = 100

text = 'The amount for these {2} quantity is {1} rupees. Total items {0}'

print(text.format(items, money, quantity))

#Escape Characters
print("We are \"good\" players of football")

print("Hello\nWorld")

text = 'my name is john'

print(text.capitalize())

print('HELLO'.casefold())

print('My age is 20. My lucky num is also 20'.count('is'))

print('My age is 20. My lucky num is also 20'.endswith('.'))

print('My age is 20. My lucky num is also 20'.find('z'))
