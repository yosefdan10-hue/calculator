from operations import add, subtract, multiply, divide
from advanced import power, square_root, factorial
from stats import median
from ui import get_number, show_menu
from history import add_to_history, show_history, clear_history
from constants import show_constants

print("*" * 30)
print("ברוכים הבאים למחשבון!")
print("גרסה 4.0")
print("*" * 30)

while True:
    choice = show_menu()

    if choice == "0":
        print("להתראות!")
        break

    if choice in ["1", "2", "3", "4", "5"]:
        num1 = get_number("הכנס מספר ראשון: ")
        num2 = get_number("הכנס מספר שני: ")

        if choice == "1":
            result = add(num1, num2)
            print(f"תוצאה: {result}")
            add_to_history(f"{num1} + {num2}", result)

        elif choice == "2":
            result = subtract(num1, num2)
            print(f"תוצאה: {result}")
            add_to_history(f"{num1} - {num2}", result)

        elif choice == "3":
            result = multiply(num1, num2)
            print(f"תוצאה: {result}")
            add_to_history(f"{num1} * {num2}", result)

        elif choice == "4":
            result = divide(num1, num2)
            print(f"תוצאה: {result}")
            add_to_history(f"{num1} / {num2}", result)

        elif choice == "5":
            result = power(num1, num2)
            print(f"תוצאה: {result}")
            add_to_history(f"{num1} ^ {num2}", result)

    elif choice == "6":
        num = get_number("הכנס מספר: ")
        result = square_root(num)
        print(f"תוצאה: {result}")
        add_to_history(f"sqrt({num})", result)

    elif choice == "7":
        num = get_number("הכנס מספר: ")
        result = factorial(num)
        print(f"תוצאה: {result}")
        add_to_history(f"{num}!", result)

    elif choice == "8":
        numbers = []
        count = int(get_number("כמה מספרים תרצה להכניס? "))

        for i in range(count):
            num = get_number(f"הכנס מספר {i + 1}: ")
            numbers.append(num)

        result = median(numbers)
        print(f"תוצאה: {result}")
        add_to_history(f"חציון של {numbers}", result)

    elif choice == "9":
        show_history()

    elif choice == "10":
        clear_history()

    elif choice == "11":
        show_constants()



    else:
        print("בחירה לא חוקית!")