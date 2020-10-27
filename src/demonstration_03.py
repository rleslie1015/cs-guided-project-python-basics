"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
def string_int(txt: str) -> int:
    # Your code here
    try:
        converted_int = int(txt)
        # return int(str)
        return converted_int
    except ValueError: 
        return f"{txt} is not a value number"

print(string_int('3d'))