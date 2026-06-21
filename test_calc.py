"""בדיקות למחשבון"""

from operations import add, subtract, multiply, divide
from advanced import power, square_root
from stats import average, find_max, find_min, median

# בדיקות פעולות בסיסיות
assert add(2, 3) == 5, "בדיקת חיבור נכשלה"
assert subtract(10, 4) == 6, "בדיקת חיסור נכשלה"
assert multiply(3, 4) == 12, "בדיקת כפל נכשלה"
assert divide(20, 4) == 5, "בדיקת חילוק נכשלה"

# בדיקות פעולות מתקדמות
assert power(2, 3) == 8, "בדיקת חזקה נכשלה"
assert square_root(16) == 4, "בדיקת שורש נכשלה"

# בדיקות סטטיסטיקה
assert average([2, 4, 6]) == 4, "בדיקת ממוצע נכשלה"
assert find_max([2, 9, 5]) == 9, "בדיקת מקסימום נכשלה"
assert find_min([2, 9, 5]) == 2, "בדיקת מינימום נכשלה"
assert median([2, 4, 5, 7]) == 4.5, "בדיקת חציון נכשלה"

print("✅ כל הבדיקות עברו בהצלחה!")