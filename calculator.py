"""A simple calculator"""

print("Give me two numbers, and I'll help you calculate an answer.")
print("Enter 'q' to quit.")

exit_calculator = False  # Flag to control exiting the entire loop structure

while not exit_calculator:
    first_number = input("\nFirst number: ")
    if first_number.lower() == 'q':
        exit_calculator = True  # Set the flag to True to exit all loops
        break  # Exit the first loop

    try:
        first_number = float(first_number)
    except ValueError:
        print("You must input a valid number!")
        continue

    if not exit_calculator:
        second_number = input("\nSecond number: ")
        if second_number.lower() == 'q':
            exit_calculator = True  # Set the flag to True to exit all loops
            break  # Exit the second loop

        try:
            second_number = float(second_number)
        except ValueError:
            print("You must input a valid number!")
            continue

    if not exit_calculator:
        operation = input("\nChoose an operation (+, -, *, /): ")
        if operation.lower() == 'q':
            exit_calculator = True  # Set the flag to True
            # to exit all loops
            break  # Exit the operation loop

        if operation in ['+', '-', '*', '/']:
            answer = None

            try:
                if operation == '+':
                    answer = first_number + second_number
                elif operation == '-':
                    answer = first_number - second_number
                elif operation == '*':
                    answer = first_number * second_number
                elif operation == '/':
                    if second_number == 0:
                        print("You can't divide by 0!")
                        continue
                    answer = first_number / second_number

                print(f"{first_number} {operation} "
                      f"{second_number} = {answer}")
                # exit_calculator = True  # Set the flag to True
                # to exit all loops
                # break  # Exit the operation loop after printing the answer

            except ZeroDivisionError:
                print("You can't divide by 0!")

        else:
            print("Invalid operation, please choose +, -, *, /")
            continue  # Continue to the operation input
