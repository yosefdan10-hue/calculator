# ממשק משתמש

def get_number(prompt):
    """מקבל מספר מהמשתמש"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("שגיאה: נא להזין מספר!")


def show_menu():
    """מציג את התפריט"""
    print("\n=== תפריט ===")
    print("1. חיבור")
    print("2. חיסור")
    print("3. כפל")
    print("4. חילוק")
    print("5. חזקה")
    print("6. שורש")
    print("0. יציאה")
    return input("בחר פעולה: ")