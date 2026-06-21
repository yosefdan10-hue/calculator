"""
advanced מודול
==============
מכיל פעולות חשבון מתקדמות: חזקה, שורש, מודולו.
"""

def	power(base,	exponent):
    "העלאה בחזקה"

    return	base	**	exponent

def	square_root(n):
    """שורש	ריבועי"""

    if	n	<	0:
        print("שלילי	למספר	שורש	אין	שגיאה:!")
        return
    return n ** (0.5)

def modulo(a,b):
    "שאריות מחולק"
    return a % b

def factorial(n):
    """מחשב עצרת של מספר"""
    if n < 0:
        print("שגיאה: אין עצרת למספר שלילי!")
        return

    result = 1
    for i in range(1, int(n) + 1):
        result *= i

    return result