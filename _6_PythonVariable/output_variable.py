"""Hàm in ra màn hình""" 
x = "Python is awesome"
print(x) # Python is awesome

x = "Python"
y = "is"
z = "awesome"
print(x, y, z) # Python is awesome(mặc định các biến sẽ hiển thị giá trị cách nhau dấu cách)

#### Nối chuỗi(dùng ký tự + để nối 2 chuỗi trở lên)
# dùng +
x = "Python"
y = "is"
z = "awesome"
print(x + y + z) #Pythonisawesome

x = "Python "
y = "is "
z = "awesome "
print(x + y + z) #Python is awesome (có thể dùng dấu các ở cuối muỗi chuỗi để hiển thị)
## Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

x = "Python"
y = "is"
z = "awesome"
print(x + " " + y + " " + z)#Python is awesome(hoặc có thể nối các chuỗi vs nhau bằng cặp nháy kép " ")

####### ký tự + vs số sẽ thành phép toán
x = 5
y = 10
print(x + y) # 15

"""
In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
Không được kết hợp 1 chuỗi và 1 số bằng toán tử +, vì chúng khác kiểu nhau
ví dụ:
x = 5
y = "John"
print(x + y) chương trình sẽ báo lỗi

"""
# Cách tốt nhất để xuất nhiều biến trong hàm print() là phân tách chúng bằng dấu phẩy, thậm chí dấu phẩy này còn hỗ trợ các loại dữ liệu khác nhau:
x = 5
y = "John"
print(x, y, 8) # 5 John 8





