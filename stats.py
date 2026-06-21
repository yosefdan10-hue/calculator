"""
stats מודול
===========
פונקציות סטטיסטיות בסיסיות.
"""

def average(numbers):
    """מחשב ממוצע של רשימת מספרים"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def find_max(numbers):
    """מוצא את המספר הגדול ביותר"""
    if not numbers:
        return None
    return max(numbers)


def find_min(numbers):
    """מוצא את המספר הקטן ביותר"""
    if not numbers:
        return None
    return min(numbers)

def median(numbers):
    """מחשב חציון"""
    if not numbers:
        return None

    numbers = sorted(numbers)
    n = len(numbers)
    mid = n // 2

    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2

    return numbers[mid]