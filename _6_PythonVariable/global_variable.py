
#==================================================================================================
# Biến toàn cục
# Các biến được tạo bên ngoài hàm (như trong tất cả các ví dụ ở các trang trước) được gọi là biến toàn cục. Mọi người đều có thể sử dụng biến toàn cục, cả bên trong và bên ngoài hàm.
#==================================================================================================


x = "awesome" # Tạo biến toàn cục x và gán tría trị là 1 chuỗi

def myfunc():
    print("Python is " + x) 

myfunc() # Python is awesome

"""Biến cục bộ(local)"""
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x) 

myfunc() # Python is fantastic

print("Python is " + x) # Python is awesome


#====================================================
# Ép kiểu cho biến local thành biến global
#====================================================
x = "15"
def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x) #Python is fantastic

myfunc() #fantastic

print("Python is " + x) #Python is fantastic
#====================================================
