def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

if __name__ == "__main__":
    print("Add 1 + 2:", add(1, 2))
    print("Divide 1 / 0:", divide(1, 0))
