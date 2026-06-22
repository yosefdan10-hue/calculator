"""
history module
==============
Stores a history of calculations.
"""

calculation_history = []


def add_to_history(expression, result):
    """Adds a calculation to the history"""
    entry = f"{expression} = {result}"
    calculation_history.append(entry)


def show_history():
    """Displays the full history"""
    if not calculation_history:
        print("No history yet")
        return

    print("\n=== History ===")
    for i, entry in enumerate(calculation_history, 1):
        print(f"{i}. {entry}")


def clear_history():
    """Clears the history"""
    calculation_history.clear()
    print("History cleared")