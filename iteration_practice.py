# Task 1 
a = 1
while a <= 10: 
    print(a)
    a += 1 

# Task 2
b = 10
while b != 0: 
    print("Blast off!")
    b -= 1

# Task 3
total = 0 
your_number = int(input("Enter an integer: "))
while your_number != 0: 
    total += your_number
    your_number = int(input("Enter an integer: "))
print("The total is:", total)

# Task 4
password = input("Enter the password: ")
while password != "python123":
    password = input("Incorrect password. Try again: ")
print("Access granted.")

# Task 5
my_list = ["apple", "banana", "cherry", "orange"]
for fruit in my_list:
    print(fruit)

# Task 6
for i in range(2, 21): 
    if i % 2 == 0:
        print(i)

# Task 7
text = "Python"
for i in text:
    print(i)

# Task 8
numbers = [3, 10, 6, 15, 2, 9]
for num in numbers:
    if num > 5:
        print(num)

# Task 9
li = [5, 12, 18, 9]
total = 0 
for number in li:
    total += number
print("The total is:", total)

# Task 10
for i in range(3): 
    for j in range(3): 
        print("*", end=" ")
    print()  

# Task 11
num = int(input("Enter a positive integer: "))
while num > 0: 
    num = int(input("Enter a positive integer: "))
print("Stopped.")
    

# Task 12
for i in range(1, 21):
    if i % 4 == 0: 
        continue 
    print(i)


# Task 13
count = 0 
while count != 20: 
    count += 1
    if count % 4 == 0: 
        continue
    print(count)

# Task 14
print('''
1. Say Hello
2. Show a number
3. Exit
''')
choice = int(input("Choose an option (1-3): "))
while choice != 3: 
    if choice == 1:
        print("Hello!")
    elif choice == 2:
        print("42")
    else:
        print("Invalid choice. Please try again.")
    choice = int(input("Choose an option (1-3): "))
print("Exiting the program.")

# Task 15
students = ["Ali", "Burak", "Sofia", "Aisha", "Tom"]
for student in students:
    if student.startswith("A"):
        print(student)

# Task 16
scores = [70, 80, 85, 90, 75]
total = sum(scores)
average = total / len(scores)
print("Total score:", total)
print("Average score:", average)

# Task 17
sentence = "Banana is an amazing fruit." 
count = 0 
for char in sentence:
    if char.lower() == 'a':
        count += 1
print("Number of 'a' characters:", count)

# Task 18
ages = [12, 25, 17, 30, 18, 14]
for age in ages: 
    if age >= 18:
        print(age)

# Task 19
word = "developer"
new_word = ""
for letter in word: 
    if letter in 'aeiou':
        new_word += letter
print("Vowels in the word:", new_word)

# Task 20
numbers = []
for i in range(5): 
    nums = int(input("Enter a number: "))
    numbers.append(nums)

print("Highest number:", max(numbers))
print("Lowest number:", min(numbers))
print("Sum of numbers:", sum(numbers))
avg = sum(numbers) / len(numbers)
for num in numbers: 
    if num > avg:
        print("Numbers greater than average:", num)

