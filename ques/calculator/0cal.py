#create a calculator where you add, subract, multiply, divide, factorial, enter input. do not use functions.
#write a calculator program that has a menu system where it asks for a choice from the user (+,-,*,/,!(factorial)). it should display the putput until the user explicitly terminated the program by writing exit.

# Calculator using match-case without functions

while True:
    print("\n----- CALCULATOR -----")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("!  Factorial")
    print("exit  Terminate")

    choice = input("Enter your choice: ")

    match choice:
        case "exit":
            print("Calculator terminated.")
            break

        case "+":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result =", num1 + num2)

        case "-":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result =", num1 - num2)

        case "*":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print("Result =", num1 * num2)

        case "/":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                print("Result =", num1 / num2)

        case "!":
            num = int(input("Enter a non-negative integer: "))

            if num < 0:
                print("Error: Factorial is not defined for negative numbers.")
            else:
                factorial = 1

                for i in range(1, num + 1):
                    factorial = factorial * i

                print("Factorial =", factorial)

        case _:
            print("Invalid choice. Please try again.")