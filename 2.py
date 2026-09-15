correct_pass = "some pass"
not_found = True

while not_found:
    passw = input("Enter pass: ")
    if passw == correct_pass:
     not_found = False

print("Password Matched!")