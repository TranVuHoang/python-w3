# Many Values to Multiple Variables

x, y, z = "Orange", "Banana", "Cherry"
print(x) # Orange
print(y) # Banana
print(z) # Cherry

# One Value to Multiple Variables

x = y = z = 2024
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
# <=> x, y, z = "apple", "banana", "cherry"
x, y, z = "apple", "banana", "cherry"

print(x) # apple
print(y) # banana
print(z) # cherry

