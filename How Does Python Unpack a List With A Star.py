# https://www.youtube.com/watch?v=ZxvZIo0yFSg
# How Does Python Unpack a List With A Star?
my_list = [1,2,3,4,5]
first, *middle, last = my_list
print(f"extracting from {my_list}...")
print(f"first: {first}")  # 1
print(f"middle: {middle}") # [2, 3, 4]
print(f"middle is of type {type(middle)}")
print(f"last: {last}")   # 5
# Unpack first and last name...
# Middle names are unpacked together.
name = ["William", "Jefferson", "Blythe", "Clinton"]
first, *middle, last = name
print(f"first name: {first}")   
print(f"last name: {last}")   
print(f"middle names: {middle}")   
