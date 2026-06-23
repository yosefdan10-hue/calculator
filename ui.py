"""
ui מודול
========
מכיל פונקציות לממשק המשתמש.
"""

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
    print("7. עצרת")
    print("8. חציון")
    print("--- היסטוריה ---")
    print("9. הצג היסטוריה")
    print("10. נקה היסטוריה")
    print("11. הצג קבועים מתמטיים")
    print("12. שטח עיגול")
    print("13. שטח מלבן")
    print("14. שטח משולש")
    print("0. יציאה")
    return input("בחר פעולה: ")