

try:
    a = 4
    b = 0
    print(a|b)

except TypeError:
    print("Unsupported operation")
except ZeroDivisionError:
    print("Division by zero not allowed")
    print("out of try except blocks")
finally:
    print("fuck you")