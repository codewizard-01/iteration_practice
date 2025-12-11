# Task 1 
counter = 0 
while counter <= 20: 
    print(counter)
    counter += 1 
    if counter == 13: 
        break

# Task 2
numbers_entered = 0 
user_input = int(input("Enter a number: "))
while numbers_entered != 0: 
    user_input = int(input("Enter a number: "))
    numbers_entered += 1

print("You entered", numbers_entered, "numbers.")

# Task 3
name = "development"
for letter in name: 
    print(letter)

# Task 4
for i in range(2, 50): 
    if i % 2 == 0: 
        print(i)

# Task 5
for i in range(5): 
    for j in range(5):
        print("*", end=" ")
    print()

# Task 6
for i in range(6): 
    for j in range(i): 
        print("*", end=" ")
    print()


# Task 7 
matrix = [[1, 2 , 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()


# Task 8
numbers = [10, 60, 20, 90, 55, 12, 77]
total_greater_than_50 = 0
for num in numbers: 
    if num > 50: 
        total_greater_than_50 += num
print("Total of numbers greater than 50 is:", total_greater_than_50)

# Task 9
counts = 0 
for i in range(1, 201): 
    if i % 3 == 0: 
        counts += 1
print("There are", counts, "numbers divisible by 3.")

# Task 10
fruits = ["apple", "banana", "orange"]
fruits.append("mango")
fruits.remove("banana")
fruits[1] = "kiwi"
print(fruits)


# Task 11 
nums = [4, 8, 15, 16, 23, 42]
squared_nums = []
for num in nums: 
    squared_nums.append(num ** 2)
print(squared_nums)

# Task 12 
numbers = []
for i in range(1, 100): 
    if i % 5 == 0: 
        numbers.append(i)
print(numbers)

# Task 13 
for i in range(4): 
    for j in range(3):
        print(0, end=" ")
    print()


# Task 14 
student = {"name": "Alice", "age": 20, "grade": 88}
student["passed"] = True
student["grade"] = 92 
student.pop("age")
print(student)

# Task 15
inventory = {"milk": 10 , "bread": 5, "eggs": 12}
for keys, values in inventory.items(): 
    print(keys, ":", values)

# Task 16
names = ["John", "sarah", "mike"]
names_dic = {name: len(name) for name in names}
print(names_dic)

# Task 17
products = ["Phone", "laptop", "camera"]
new_dic = {product: len(product) for product in products}
print(new_dic)

# Task 18
temperatures = [12, 15, 20, 5, -1, 30, 22, 10]
positive_temps = [temp for temp in temperatures if temp > 0] 
greater_then_18 = [temp for temp in temperatures if temp > 18]
print("Positive temperatures:", positive_temps)
print("Temperatures greater than 18:", greater_then_18)

# Task 19
rows = {"Row 1": [1, 2, 3], "Row 2": [1, 2, 3], "Row 3": [1, 2, 3]}
for key, value in rows.items():
    print(key + ": ", end="")
    for item in value: 
        print(item, end=" ")
    print()

# Task 20
empty_list = []
counter = 0 
while counter <= 200:
    empty_list.append(counter)
    counter += 1 
print(empty_list)

odd_numbers = []
for i in range(201): 
    if i % 2 != 0:
        odd_numbers.append(i)
print(odd_numbers)



  
