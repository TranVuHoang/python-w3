#=======================
"""
Kiểu số trong python
1. int
2. float
3. complex
"""
#=======================

x = 1
y = 2.1
z = 2j

print(type(x)) # <class int>
print(type(y)) # <class float>
print(type(z)) # <class complex>

#===============================================
#Kiểu int
#===============================================

x =1
y = 2014
z = -9999

print(type(x)) #<class int>
print(type(y)) #<class int>
print(type(z)) #<class int>

#===============================================
#Kiểu float
#===============================================

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print((y))
print(type(z), z)

#===============================================
#Kiểu complex(số phức)
#===============================================

x = 4 + 5j
y = 5j
z = -5j
print(x, type(x))


x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(x)
print(y)
print(z)

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))