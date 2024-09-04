txt = "The best things in life are free!"
print("free" in txt) # True

txt = "The best things in life are freeeee!"
print("free" in txt) # True

txt = "The best things in life are freae!"
print("free" in txt) # False

txt = "The best things in life are free!"

if "free" in txt:
  print("Yes, 'free' is present.") # Yes, 'free' is present.

txt = "learning python 2024"

if 'python' in txt:
    print("YES")

txt = "learning python 2024"
print('python' in txt) # True
print('react' in txt) # False
print('react' not in txt) # True

txt = "learning python 2024"

if "react" not in txt:
   print("react không có trong câu: ", txt)