n = input("Enter a number")
number = 0
while number <= 10:
    print(n, "x",number," = ",number,*number)
    number+=1