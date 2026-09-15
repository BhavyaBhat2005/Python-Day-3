#calculate the sum of all numbers from 1 to N

n=int(input ("enter N"))

total = 0

for i in range(1, n + 1):
 total += i

 print("sum =", total)