def ref_calculator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except Exception as e:
            print(f"Error: {e}. Check the example.")
    return wrapper

@ref_calculator
def calculate(expression):
    return eval(expression)

print(calculate("4 + 6"))
print(calculate("20 / 0"))
