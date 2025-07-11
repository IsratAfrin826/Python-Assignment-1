# Write a program using a for loop that calculates the sum of even numbers between 1 and 100.

sum = 0
for x in range(2, 101, 2):
    sum = sum + x
print(sum)