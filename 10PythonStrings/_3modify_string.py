#===============================
# upper case
# upper()
#===============================

a = "Trần Vũ Hoàng"
print(a.upper()) # TRẦN VŨ HOÀNG

#===============================
# Lower Case
# lower()
#===============================

a = "Nguyễn Mai Trang"
print(a.lower()) # nguyễn mai trang

#========================================
# Xóa khoảng trắng thừa đầu và cuối chuỗi
# strip()
#========================================

a = '     Nguyễn      Mạnh  Cường     '
print(a.strip())

#========================================
# Replace String
# Thay thế ký tự trong chuỗi
#========================================

a = "Hello, World! Hoàng"
print(a.replace("H", "J")) # Jello, world

#===============================================================
# Split String
# split() tách(theo khoảng trắng), chuyển đổi chuỗi thành list
#===============================================================
x = "Hello World!"
b = x.split()
print(b, type(b)) #['Hello', 'World!'] <class 'list'>

x = "Hello World!"
b = x.split(',')
print(b, type(b)) #['Hello World!'] <class 'list'>

x = "Hello, World!"
b = x.split(',')
print(b, type(b)) #['Hello', 'World!'] <class 'list'>



