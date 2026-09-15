#write a program to calculate the average of a given list

numbers = [1,20,30,40]

total = 0

for num in numbers:
    total += num

average = total / len(numbers)

print(numbers)
print("Average =", average)