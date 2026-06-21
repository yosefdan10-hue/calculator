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