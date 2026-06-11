# =========================
#     PYHTON CALCULATOR
# =========================

# Display welcome message
print("=========================")
print("     PYHTON CALCULATOR")
print("=========================")
print("Examples:")
print("  2 + 3")
print("10 - 5 +8")
print("2 * 3 * 4")
print("(10 + 5) * 2")
print("Type 'q' to quit")
print("=========================")

#Run the calculator untill the user quits
while True:

    # Take mathematical expression as input
    expression = input("\nEnter your expression:")

    # Check if the user want to exit
    if expression.lower() == 'q':
        print("Thank you for using the calculator!")
        break

    # Try to calculate the expression
    try:
        #Evaluate the matehmical expression 
        answer = eval(expression)

        # Display the result
        print("Answer =", answer)

    # Handle division by zero
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    # Handle any other invalid input
    except:
        print("Invalid expression!")