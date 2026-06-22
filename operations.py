"""
operations מודול
================
מכיל פעולות חשבון בסיסיות: חיבור, חיסור, כפל, חילוק.
"""

from colors import print_error

def	add(a,	b):
    "מחבר שני מספרים"

    return	a	+	b
def	subtract(a,	b):
    "מחסר שני מספרים"

    return	a	-	b

def multiply(a, b):
    "מכפיל שני מספרים"
    return a * b

def divide(a, b):
    "מחלק שני מספרים"
    if b == 0:
        print_error("שגיאה: אי אפשר לחלק באפס!")
        return None
    return a / b