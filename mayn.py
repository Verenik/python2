result = []

def divider(a, b):
    if a < b:
        raise ValueError("The first number must be greater than or equal to the second number.")
    if b > 100:
        raise IndexError("The second number must not be greater than 100.")
    return a / b

data = {10: 2,2: 5,18: 0,  8: 4, 123: 4 }

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError, TypeError) as e:
        print(f"Error for key {key}: {e}")
        result.append(None)

print(result)
