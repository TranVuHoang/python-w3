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





