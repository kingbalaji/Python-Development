import pandas as pd

# Data: Python keywords and meanings
data = [
    ("False", "Boolean false value"),
    ("None", "Represents the absence of a value, null"),
    ("True", "Boolean true value"),
    ("and", "Logical AND operator"),
    ("as", "Used to create an alias (e.g., import module as alias)"),
    ("assert", "Used for debugging purposes to check a condition"),
    ("async", "Defines asynchronous functions or blocks"),
    ("await", "Used to wait for an asynchronous operation"),
    ("break", "Exits the nearest enclosing loop"),
    ("class", "Used to define a class"),
    ("continue", "Skips the rest of the current loop iteration and moves to the next iteration"),
    ("def", "Defines a function"),
    ("del", "Deletes objects (variables, list items, dictionary entries, etc.)"),
    ("elif", "Else-if condition used in if statements"),
    ("else", "Defines a block of code for when if condition is false"),
    ("except", "Catches exceptions in try blocks"),
    ("finally", "A block that is executed no matter what after try/except"),
    ("for", "Used for looping over a sequence"),
    ("from", "Used to import specific parts from a module"),
    ("global", "Declares global variables within a function"),
    ("if", "Starts a conditional statement"),
    ("import", "Imports modules"),
    ("in", "Checks membership or iterates over sequences"),
    ("is", "Tests object identity (whether two references point to the same object)"),
    ("lambda", "Creates anonymous functions"),
    ("nonlocal", "Declares variables to refer to the nearest outer (non-global) variable"),
    ("not", "Logical NOT operator"),
    ("or", "Logical OR operator"),
    ("pass", "Null statement; does nothing"),
    ("raise", "Raises an exception"),
    ("return", "Returns a value from a function"),
    ("try", "Defines a block to catch exceptions"),
    ("while", "Loop that repeats while a condition is true"),
    ("with", "Used to wrap the execution of a block with methods defined by a context manager"),
    ("yield", "Used inside a function like return but returns a generator"),
]

# Create DataFrame
df = pd.DataFrame(data, columns=["Keyword", "Meaning"])

# Save to Excel
df.to_excel("python_keywords.xlsx", index=False)

print("Excel file 'python_keywords.xlsx' has been created successfully.")
