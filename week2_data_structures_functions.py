"""
WEEK 2: Data Structures and Functions

Summary of concepts learned:
- List: ordered, mutable.  Tuple: ordered, immutable.
- Dictionary: key-value pairs.  Set: unordered, unique items only.
- Functions (def) package reusable logic; lambda = small anonymous function.
- Recursion: a function calling itself with a base case.
- List comprehension: compact way to build/filter lists: [x*x for x in data if x > 0]
"""


# ---------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------
def data_structure_demo():
    print("--- Data Structures ---")

    # List
    nums = [5, 3, 8, 1]
    nums.append(10)
    nums.sort()
    print("List:", nums)

    # Tuple
    point = (10, 20)
    x, y = point  # unpacking
    print("Tuple:", point, "-> x =", x, ", y =", y)

    # Dictionary
    student = {"name": "Asha", "age": 21, "marks": [80, 90, 85]}
    student["city"] = "Delhi"
    print("Dict:", student)
    for key, value in student.items():
        print(f"  {key}: {value}")

    # Set
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print("Union:", a | b, "| Intersection:", a & b, "| Difference:", a - b)


def sum_of_squares(numbers):
    return sum(n ** 2 for n in numbers)


def filter_even(numbers):
    return [n for n in numbers if n % 2 == 0]


def filter_above(numbers, threshold):
    return list(filter(lambda n: n > threshold, numbers))


def normalize(numbers):
    """Min-max scaling to the range 0-1."""
    lo, hi = min(numbers), max(numbers)
    if hi == lo:
        return [0.0 for _ in numbers]
    return [round((n - lo) / (hi - lo), 3) for n in numbers]


def factorial(n):
    """Recursion example."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Recursion example: nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def hands_on_demo():
    print("\n--- Hands-On: Functions & Transformations ---")
    data = [4, 7, 2, 9, 12, 5, 8, 3]

    print("Data               :", data)
    print("Sum of squares     :", sum_of_squares(data))
    print("Even numbers       :", filter_even(data))
    print("Greater than 5     :", filter_above(data, 5))
    print("Normalized         :", normalize(data))

    # lambda + map + sorted
    squares = list(map(lambda x: x ** 2, data))
    print("Squares (lambda)   :", squares)

    people = [("Ravi", 25), ("Neha", 22), ("Amit", 30)]
    print("Sorted by age      :", sorted(people, key=lambda p: p[1]))

    # list comprehension
    print("Squares of evens   :", [x ** 2 for x in data if x % 2 == 0])
    print("Factorial(5)       :", factorial(5))
    print("Fibonacci(0..9)    :", [fibonacci(i) for i in range(10)])


# ---------------------------------------------------------------
# Data cleaning script
# ---------------------------------------------------------------
def clean_customer_records(records):
    cleaned = []
    seen_emails = set()
    removed = {"missing": 0, "duplicate": 0, "invalid_age": 0}

    for rec in records:
        name = (rec.get("name") or "").strip()
        email = (rec.get("email") or "").strip().lower()
        age = rec.get("age")

        # 1. missing values
        if not name or not email:
            removed["missing"] += 1
            continue

        # 2. invalid age filter
        if not isinstance(age, (int, float)) or not (18 <= age <= 100):
            removed["invalid_age"] += 1
            continue

        # 3. duplicates
        if email in seen_emails:
            removed["duplicate"] += 1
            continue
        seen_emails.add(email)

        cleaned.append({
            "name": name.title(),
            "email": email,
            "age": int(age),
            "city": (rec.get("city") or "Unknown").strip().title(),
        })

    return cleaned, removed


def client_project_demo():
    print("\n--- Client Project: Data Cleaning ---")
    raw_data = [
        {"name": "  rahul sharma ", "email": "Rahul@Mail.com", "age": 28, "city": "delhi"},
        {"name": "Priya Verma", "email": "priya@mail.com", "age": 34, "city": "Mumbai"},
        {"name": "rahul sharma", "email": "rahul@mail.com", "age": 28, "city": "Delhi"},   # duplicate
        {"name": "", "email": "ghost@mail.com", "age": 40, "city": "Pune"},                # missing name
        {"name": "Aman Gupta", "email": "aman@mail.com", "age": 15, "city": "Jaipur"},     # invalid age
        {"name": "Sneha Raisingh", "email": "sneha@mail.com", "age": 29, "city": None},
        {"name": "Karan Singh", "email": None, "age": 31, "city": "Noida"},                # missing email
        {"name": "Meera Subramaniyam", "email": "meera@mail.com", "age": 45, "city": "chennai"},
    ]

    cleaned, removed = clean_customer_records(raw_data)

    print(f"Raw records     : {len(raw_data)}")
    print(f"Cleaned records : {len(cleaned)}")
    print(f"Removed         : {removed}\n")
    for r in cleaned:
        print(r)

    # Simple summary using dictionaries
    city_counts = {}
    for r in cleaned:
        city_counts[r["city"]] = city_counts.get(r["city"], 0) + 1
    print("\nCustomers per city:", city_counts)

    # Remove duplicates from a plain list (order preserved)
    values = [3, 1, 3, 2, 1, 5, 2]
    unique = list(dict.fromkeys(values))
    print("\nList with duplicates:", values)
    print("After removing dups :", unique)


if __name__ == "__main__":
    data_structure_demo()
    hands_on_demo()
    client_project_demo()
