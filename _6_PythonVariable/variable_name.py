"""
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

myvar = "John"
my_var = "Tom"
_my_var = "John1"
myVar = "John2"
MYVAR = "John3"
myvar2 = "Joh4"


print(myvar) #Jhon
print(my_var) #Tom
print(_my_var) #Jhon1
print(myVar) #Jhon2
print(MYVAR) #Jhon3
print(myvar2) #Jhon4

"""
Các trường hợp tên biến không hợp lệ:
2myvar = "John" (bắt đầu bởi 1 số)
my-var = "John" 
my var = "John"
"""

#Cú pháp đặt tên biến kiểu lạc đà(Camel Case)
# Chữ cái đầu của tên biến viết thường, các chữ cái đầu của các từ còn lại viết Hoa
myVariableName = "Trần"

#Pascal Case

MyVariableName = "Vũ"

# Snake Case

my_variable_name = "Hoàng"

print(myVariableName) # Trần 
print(MyVariableName) # Vũ
print(my_variable_name) # Hoàng



