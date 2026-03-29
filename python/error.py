def divide(a, b):
    if b == 0:
        raise ValueError
    return a / b

try:
    result = divide(10, 0)
    print(result)
except ValueError as e:
    print(f"Error: {e}")

print("Program continues after handling the error.")