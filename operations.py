"""
operations מודול
================
מכיל פעולות חשבון בסיסיות: חיבור, חיסור, כפל, חילוק.
"""

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
        print("error")
        return
    return a / b