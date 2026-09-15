#code with bug

i = 0
while i < 10:
    if i == 5:
        continue

    print(i)
    i += 1

    #the bug is that the code will indefinatly be stuck on 5 