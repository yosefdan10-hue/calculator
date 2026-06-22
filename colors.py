"""
colors module
=============
Terminal output colors.
"""

RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'


def print_success(message):
    print(f"{GREEN}{message}{RESET}")


def print_error(message):
    print(f"{RED}{message}{RESET}")


def print_result(message):
    print(f"{BLUE}{message}{RESET}")