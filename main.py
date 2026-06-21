from operations import add, subtract, multiply, divide
from advanced import power, square_root, factorial
from ui import get_number, show_menu

print("ברוכים הבאים למחשבון!")
print("====================")

while True:
    choice = show_menu()

    if choice == "0":
        print("להתראות!")
        break

    if choice in ["1", "2", "3", "4", "5"]:
        num1 = get_number("הכנס מספר ראשון: ")
        num2 = get_number("הכנס מספר שני: ")

        if choice == "1":
            print(f"תוצאה: {add(num1, num2)}")

        elif choice == "2":
            print(f"תוצאה: {subtract(num1, num2)}")

        elif choice == "3":
            print(f"תוצאה: {multiply(num1, num2)}")

        elif choice == "4":
            print(f"תוצאה: {divide(num1, num2)}")

        elif choice == "5":
            print(f"תוצאה: {power(num1, num2)}")

    elif choice == "6":
        num = get_number("הכנס מספר: ")
        print(f"תוצאה: {square_root(num)}")
    elif choice == "7":
        num = get_number("הכנס מספר: ")
        print(f"תוצאה: {factorial(num)}")
    else:
        print("בחירה לא חוקית!")