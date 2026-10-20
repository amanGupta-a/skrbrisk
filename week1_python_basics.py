"""
WEEK 1: Introduction to Python Programming

Summary of concepts learned:
- Variables & data types: int, float, str, bool store different kinds of values.
- Operators: arithmetic (+ - * / // % **), comparison (== != < >), logical (and, or, not).
- Input/Output: input() reads text from the user, print() shows output; f-strings format text.
- Conditionals: if / elif / else let a program choose between paths.
- Loops: `for` iterates over a sequence; `while` repeats until a condition is False.
"""


# ---------------------------------------------------------------
# Temperature converter
# ---------------------------------------------------------------
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def temperature_converter():
    print("\n--- Temperature Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose (1/2): ").strip()

    try:
        if choice == "1":
            c = float(input("Enter temperature in Celsius: "))
            print(f"{c:.2f} C = {celsius_to_fahrenheit(c):.2f} F")
        elif choice == "2":
            f = float(input("Enter temperature in Fahrenheit: "))
            print(f"{f:.2f} F = {fahrenheit_to_celsius(f):.2f} C")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")


# ---------------------------------------------------------------
# Calculator
# ---------------------------------------------------------------
def calculator():
    print("\n--- Calculator ---")
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /, //, %, **): ").strip()
        b = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b if b != 0 else "Error: division by zero"
    elif op == "//":
        result = a // b if b != 0 else "Error: division by zero"
    elif op == "%":
        result = a % b if b != 0 else "Error: division by zero"
    elif op == "**":
        result = a ** b
    else:
        result = "Invalid operator"
    print(f"Result: {result}")


# ---------------------------------------------------------------
# Examples of loops
# ---------------------------------------------------------------
def loop_examples():
    print("\n--- Loop Examples ---")
    # for loop: multiplication table
    n = 5
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

    # while loop: countdown
    count = 5
    while count > 0:
        print("Countdown:", count)
        count -= 1

    # even / odd check with if-else
    for num in range(1, 6):
        print(num, "is even" if num % 2 == 0 else "is odd")


# ---------------------------------------------------------------
# CLIENT PROJECT: Basic data processing - average temperature
# ---------------------------------------------------------------
def average_temperature_report():
    print("\n--- Client Project: Weekly Temperature Report ---")
    temperatures = {
        "Monday": 28.5,
        "Tuesday": 30.1,
        "Wednesday": 27.8,
        "Thursday": 31.4,
        "Friday": 29.0,
        "Saturday": 32.2,
        "Sunday": 26.9,
    }

    total = 0
    for temp in temperatures.values():
        total += temp
    average = total / len(temperatures)

    hottest_day = max(temperatures, key=temperatures.get)
    coldest_day = min(temperatures, key=temperatures.get)

    print(f"Number of days   : {len(temperatures)}")
    print(f"Average temp     : {average:.2f} C")
    print(f"Hottest day      : {hottest_day} ({temperatures[hottest_day]} C)")
    print(f"Coldest day      : {coldest_day} ({temperatures[coldest_day]} C)")

    print("\nDay-wise status:")
    for day, temp in temperatures.items():
        if temp > average:
            status = "Above average"
        elif temp < average:
            status = "Below average"
        else:
            status = "Average"
        print(f"  {day:<10} {temp:>5.1f} C  -> {status}")


def main():
    while True:
        print("\n===== WEEK 1 MENU =====")
        print("1. Temperature Converter")
        print("2. Calculator")
        print("3. Loop Examples")
        print("4. Average Temperature Report (Client Project)")
        print("5. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            temperature_converter()
        elif choice == "2":
            calculator()
        elif choice == "3":
            loop_examples()
        elif choice == "4":
            average_temperature_report()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
