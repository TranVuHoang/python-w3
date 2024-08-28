#=============================================
# Các kiểu dữ liệu trong python
# Text Type:	    str(kiểu chuỗi)
# Numeric Types:	int, float, complex(kiểu số nguyên, số thực, complex)
# Sequence Types:	list, tuple, range(kiểu danh sách)
# Mapping Type:	    dict
# Set Types:	    set, frozenset
# Boolean Type:	    bool(kiểu luận lý trả về giá trị đúng sai)
# Binary Types:	    bytes, bytearray, memoryview
# None Type:	    NoneType

# kiểm tra kiểu dữ liệu dùng hàm type()
#=============================================

# kiểm tra kiểu dữ liệu dùng hàm type()
# Ex1
x = 5
print(type(x)) #<class 'int'>

x = "Hello World"

#display x:
print(x) # Hello World

#display the data type of x:
print(type(x)) # <class str>

#============================================
# Ex1: Kiểu Number(số thực)
#============================================
x = 20

#display x:
print(x) #20

#display the data type of x:
print(type(x)) # <class int>



#============================================
# Ex3: Kiểu Number(số thực)
#============================================
x = 20.5

#display x:
print(x) #20.5

#display the data type of x:
print(type(x)) #<class float>



#============================================
# Ex4 Kiểu list
#============================================
x = ["apple", "banana", 1]

#display x:
print(x)

#display the data type of x:
print(type(x)) 

#============================================
# Ex6 Kiểu dict(object)
#============================================
x = {"name" : "John", "age" : 36}
#display x:
print(x)

#display the data type of x:
print(type(x)) 

#============================================
# Ép kiểu trong python
# str(variableName)
# int(variableName)
#============================================


#============================================
# Ex1 Ép Kiểu chuỗi(object)
#============================================
x = 2024
print(type(x)) #<class 'int'>
x = str(x)
print(type(x)) #<class 'str'>


