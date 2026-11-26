"""
ADVANCED PYTHON TEACHING GUIDE
TOPIC: PEP 8 — PYTHON CODE STYLE GUIDE

A simplified, practical, step-by-step classroom guide for VS Code.

WHAT THIS LESSON COVERS
1. What PEP 8 is and why it matters.
2. Indentation and code layout.
3. Line length and line continuation.
4. Blank lines and spacing.
5. Naming conventions for variables, functions, classes, and constants.
6. Imports and module organisation.
7. Comments and docstrings.
8. Strings, comparisons, exceptions, and other recommendations.
9. Class and method naming.
10. Checking code style with pycodestyle and flake8.
11. A practical before-and-after exercise.
12. Student exercises and 20 objective questions.

IMPORTANT
PEP 8 is a style guide. It helps developers write consistent, readable code.
Most style issues do not stop Python from running. They make code harder to
read or maintain. Python syntax rules are different from style recommendations.

HOW TO USE THIS FILE
- Open this .py file in VS Code.
- Teach one numbered section at a time.
- The explanations are comments/docstrings.
- The runnable examples demonstrate good style.
- Commands shown in teaching notes should be typed in the VS Code terminal.
"""

import math
import os
import sys
from pathlib import Path

# ============================================================
# 1. WHAT IS PEP 8?
# ============================================================

"""
PEP means Python Enhancement Proposal.

PEP 8 is the official style guide for writing Python code. It recommends
how Python code should be formatted and how names should be written.

Think of PEP 8 as presentation rules for Python code.

Two programs can produce the same result, but one may be easier to read
because its spacing, names, and structure are consistent.

WHY PEP 8 IS IMPORTANT
- Makes code easier to read.
- Helps teams follow the same coding style.
- Makes code reviews easier.
- Helps developers understand code written by others.
- Makes projects easier to maintain.

PEP 8 does not replace Python syntax rules. A program can run and still
violate PEP 8 recommendations.

Official reference:
https://peps.python.org/pep-0008/
"""

# ============================================================
# 2. INDENTATION
# ============================================================

"""
Indentation means the spaces at the beginning of a line.

PEP 8 recommends four spaces for each indentation level.
Do not mix tabs and spaces in the same file.

Incorrect style example:

if True:
  print("Welcome")

The code may run, but it uses only two spaces.

Recommended style:

if True:
    print("Welcome")

When a block is nested inside another block, add another four spaces.
"""

print("\n--- INDENTATION EXAMPLE ---")

student_score = 75

if student_score >= 50:
    print("Student passed.")
    if student_score >= 70:
        print("Good performance.")

# ============================================================
# 3. LINE LENGTH
# ============================================================

"""
PEP 8 recommends:
- Maximum of 79 characters for code lines.
- Maximum of 72 characters for comments and docstrings.

A very long line can be difficult to read on a screen.

Long expression — difficult to read:

    final_student_result = calculate_student_average(first_score, second_score, third_score, fourth_score)

Better: use parentheses to continue the expression across lines.

    final_student_result = calculate_student_average(
        first_score,
        second_score,
        third_score,
        fourth_score,
    )

Python allows implicit line continuation inside parentheses, brackets,
and braces. Prefer this over using a backslash for most line wrapping.
"""

def calculate_average(*scores):
    """Return the average of the supplied scores."""
    if not scores:
        return 0

    return sum(scores) / len(scores)


average_score = calculate_average(
    75,
    80,
    90,
    85,
)

print("\n--- LINE LENGTH EXAMPLE ---")
print("Average score:", average_score)

# ============================================================
# 4. BLANK LINES
# ============================================================

"""
PEP 8 recommends blank lines to separate different parts of a program.

Common rules:
- Use two blank lines around top-level function definitions.
- Use two blank lines around top-level class definitions.
- Use one blank line between methods inside a class.
- Use blank lines inside functions when they separate logical sections.

Do not put a blank line after every single statement. Use blank lines to
make the structure easier to understand.
"""

def calculate_total(first_score, second_score):
    """Return the total of two scores."""
    return first_score + second_score


def calculate_pass_status(score):
    """Return whether a student has passed."""
    return score >= 50


# ============================================================
# 5. SPACING AROUND OPERATORS
# ============================================================

"""
Use one space around common operators such as:
=, +, -, *, /, ==, !=, <, >, <=, >=

Less readable:
    total=first+second
    is_passed=score>=50

Recommended:
    total = first + second
    is_passed = score >= 50

Do not add unnecessary spaces inside brackets or before commas.

Less readable:
    student = [ "Ada" , "Tunde" ]

Recommended:
    student = ["Ada", "Tunde"]
"""

print("\n--- SPACING EXAMPLE ---")

first_number = 10
second_number = 5
total = first_number + second_number
is_valid = total >= 10

print("Total:", total)
print("Is valid:", is_valid)

# ============================================================
# 6. NAMING CONVENTIONS
# ============================================================

"""
Naming conventions are rules for choosing names for variables, functions,
classes, modules, and constants.

The main naming styles are:

1. VARIABLES: lowercase_with_underscores
   Examples:
       student_name
       total_score
       account_balance

2. FUNCTIONS: lowercase_with_underscores
   Examples:
       calculate_total()
       get_student()
       send_email()

3. CLASSES: CapWords / PascalCase
   Examples:
       Student
       BankAccount
       StudentManager

4. CONSTANTS: UPPERCASE_WITH_UNDERSCORES
   Examples:
       MAX_ATTEMPTS
       TAX_RATE
       SCHOOL_NAME

5. MODULES: short, lowercase names
   Examples:
       student.py
       calculations.py
       file_reader.py

6. PACKAGES: short, lowercase names.
   Underscores are generally discouraged in package names.

Use descriptive names. Avoid unclear names such as x1, abc, or temp when
a more meaningful name can describe the purpose.

Avoid using single-character variable names l, O, and I because they can
look like the numbers 1 and 0 in some fonts.
"""

# Recommended variable names.
student_name = "Ada"
total_score = 88
MAX_ATTEMPTS = 3
SCHOOL_NAME = "Python Learning Centre"


def calculate_final_score(course_score, exam_score):
    """Return the combined course and exam score."""
    return course_score + exam_score


print("\n--- NAMING EXAMPLE ---")
print(student_name)
print(calculate_final_score(35, 55))
print("School:", SCHOOL_NAME)
print("Maximum attempts:", MAX_ATTEMPTS)

# ============================================================
# 7. CLASS AND ATTRIBUTE NAMING
# ============================================================

"""
PEP 8 class names use CapWords.
Methods and instance attributes use lowercase_with_underscores.

Example:
    class StudentRecord:
        def __init__(self, student_name, student_age):
            self.student_name = student_name
            self.student_age = student_age

Here:
- StudentRecord is a class name.
- __init__ is a special method.
- self is the conventional name for the current instance.
- student_name and student_age are instance attributes.
- display_details is a method name.

A class attribute is shared at the class level. Use a descriptive name.
Constants are commonly written in uppercase_with_underscores.
"""

class StudentRecord:
    """Represent a student's basic details."""

    school_name = "Python Learning Centre"

    def __init__(self, student_name, student_age):
        self.student_name = student_name
        self.student_age = student_age

    def display_details(self):
        """Display the student's details."""
        print("Name:", self.student_name)
        print("Age:", self.student_age)
        print("School:", self.school_name)


print("\n--- CLASS AND ATTRIBUTE EXAMPLE ---")
student = StudentRecord("Ada", 20)
student.display_details()

# ============================================================
# 8. NAMING SPECIAL CASES
# ============================================================

"""
Some other naming conventions:

_instance_variable
    A leading single underscore suggests that the name is intended for
    internal use. It is a convention, not strict access control.

__name
    Two leading underscores inside a class trigger name mangling. This is
    mainly used to avoid accidental name clashes in subclasses. It is not
    a general way to make data truly private.

name_
    A trailing underscore can avoid a conflict with a Python keyword.
    Example: class_ can be used instead of class.

self
    Conventional first parameter name for instance methods.

cls
    Conventional first parameter name for class methods.

Exception classes
    Usually use CapWords and commonly end with Error.
    Example: InvalidAgeError.
"""

class InvalidAgeError(ValueError):
    """Raised when a supplied age is invalid."""


def validate_age(age):
    """Check that age is a positive number."""
    if age <= 0:
        raise InvalidAgeError("Age must be greater than zero.")

    return age


# ============================================================
# 9. IMPORTS
# ============================================================

"""
PEP 8 recommends putting imports at the top of the file, after the module
docstring and before regular code.

Separate imports into groups, with a blank line between groups:

1. Standard library imports.
2. Third-party imports.
3. Local application imports.

Recommended:

    import os
    import sys

    import requests

    from my_project.models import Student

Avoid combining unrelated imports on one line:

    import os, sys

For a small example, one import per line is easier to read.
Avoid wildcard imports such as:

    from math import *

They make it harder to see where names came from.
"""

# Standard library imports are grouped at the top of this teaching file.

# Third-party imports would be grouped below standard library imports.
# Example:
# import requests

# Local project imports would be grouped after third-party imports.
# Example:
# from student_project.models import Student

print("\n--- IMPORT EXAMPLE ---")
print("Square root of 81:", math.sqrt(81))
print("Current example filename:", Path(__file__).name)

# ============================================================
# 10. COMMENTS
# ============================================================

"""
Comments explain why code exists or clarify something that is not obvious.

A good comment:
- Is clear and relevant.
- Uses complete sentences where appropriate.
- Is updated when the code changes.
- Does not simply repeat what the code already says.

Useful:
    # Apply the discount before calculating the final invoice total.

Not useful:
    # Add 1 to x.
    x = x + 1

Use comments sparingly. Too many unnecessary comments can make code harder
to read.
"""

# Apply a discount before calculating the final invoice amount.
invoice_total = 1000
discount = 100
final_invoice = invoice_total - discount

print("\n--- COMMENT EXAMPLE ---")
print("Final invoice:", final_invoice)

# ============================================================
# 11. DOCSTRINGS
# ============================================================

"""
A docstring documents a module, class, function, or method.

A docstring is written immediately after a def or class line, using triple
quotes.

One-line example:
    def greet(name):
        \"\"\"Return a greeting for a person.\"\"\"
        return f"Hello, {name}!"

Multi-line docstrings:
- Start with a short summary line.
- Leave a blank line before the detailed explanation if needed.
- Close the triple quotes on their own line.

PEP 8 refers to PEP 257 for more detailed docstring conventions.
"""

def calculate_discount(price, discount_rate):
    """Calculate the discount amount for a price.

    Args:
        price: Original price.
        discount_rate: Discount percentage.

    Returns:
        The amount to subtract from the original price.
    """
    return price * discount_rate / 100


print("\n--- DOCSTRING EXAMPLE ---")
print("Discount:", calculate_discount(5000, 10))
print(calculate_discount.__doc__)

# ============================================================
# 12. STRINGS AND QUOTATION MARKS
# ============================================================

"""
PEP 8 does not require one universal choice between single and double quotes.
Choose a style and use it consistently.

Use double quotes when the string contains an apostrophe:
    message = "It's a Python lesson"

Use single quotes when that makes the string easier to read:
    message = 'Welcome to Python'

Triple double quotes are commonly used for docstrings.

The important point is consistency and readability.
"""

welcome_message = "Welcome to the PEP 8 lesson"
teacher_message = "It's time to practise"

print("\n--- STRING EXAMPLE ---")
print(welcome_message)
print(teacher_message)

# ============================================================
# 13. COMPARISONS WITH NONE AND BOOLEAN VALUES
# ============================================================

"""
Use 'is None' or 'is not None' when checking for None.

Recommended:
    if student_name is None:
        print("Name was not supplied.")

Avoid:
    if student_name == None:

For booleans, write:
    if is_active:

Avoid:
    if is_active == True:

For a false condition:
    if not is_active:

The 'is' operator checks object identity. Use == for value equality,
such as comparing two strings or numbers.
"""

student_email = None
is_active = True

print("\n--- COMPARISON EXAMPLE ---")

if student_email is None:
    print("No email address was supplied.")

if is_active:
    print("Student account is active.")

# ============================================================
# 14. WHITESPACE INSIDE EXPRESSIONS
# ============================================================

"""
Avoid unnecessary spaces:
- Immediately inside parentheses, brackets, or braces.
- Before commas, semicolons, or colons.
- Between a function name and its opening parenthesis.
- Before an opening parenthesis used for a function call.

Recommended:
    student_names = ["Ada", "Tunde"]
    greet("Ada")
    if score >= 50:
        print(score)

Avoid:
    student_names = [ "Ada" , "Tunde" ]
    greet ("Ada")
    if score>=50 :
        print (score)

Use one space after a comma.
"""

student_names = ["Ada", "Tunde", "Mina"]

print("\n--- WHITESPACE EXAMPLE ---")
for name in student_names:
    print(name)

# ============================================================
# 15. AVOID MULTIPLE STATEMENTS ON ONE LINE
# ============================================================

"""
Avoid putting several statements on one line, especially after if, for,
while, or def.

Less readable:
    if score >= 50: print("Passed")

Recommended:
    if score >= 50:
        print("Passed")

Less readable:
    first = 10; second = 20

Recommended:
    first = 10
    second = 20

One statement per line is easier to debug and review.
"""

first_score = 70
second_score = 80

if first_score >= 50:
    print("\nFirst student passed.")

if second_score >= 50:
    print("Second student passed.")

# ============================================================
# 16. TRAILING COMMAS IN MULTI-LINE COLLECTIONS
# ============================================================

"""
A trailing comma is useful when a list, tuple, dictionary, or function call
is spread across multiple lines.

It makes future edits easier because a new item can be added without
changing the previous line.
"""

student_record = {
    "name": "Ada",
    "age": 20,
    "course": "Python",
}

print("\n--- TRAILING COMMA EXAMPLE ---")
print(student_record)

# ============================================================
# 17. EXCEPTION HANDLING STYLE
# ============================================================

"""
Use specific exception types where possible.

Recommended:
    try:
        number = int(user_input)
    except ValueError:
        print("Enter a valid whole number.")

Avoid catching every exception without a good reason:

    except:
        pass

A bare except can hide problems and make debugging difficult.
Do not silently ignore errors that should be handled or reported.
"""

def convert_to_integer(value):
    """Convert a value to an integer, or return None if invalid."""
    try:
        return int(value)
    except ValueError:
        print("Please provide a valid whole number.")
        return None


print("\n--- EXCEPTION EXAMPLE ---")
print(convert_to_integer("25"))
print(convert_to_integer("twenty"))

# ============================================================
# 18. USE with FOR FILE HANDLING
# ============================================================

"""
Use a with statement when working with resources such as files.
It helps ensure the file is closed after the block finishes.

Recommended:
    with open("notes.txt", "w", encoding="utf-8") as file:
        file.write("Hello")

This is clearer and safer than manually opening and closing the file.
"""

with open("pep8_class_example.txt", "w", encoding="utf-8") as file:
    file.write("Learning Python style with PEP 8.\n")

print("\n--- FILE HANDLING EXAMPLE ---")
print("Created pep8_class_example.txt")

# ============================================================
# 19. FUNCTION AND METHOD STYLE
# ============================================================

"""
Functions should:
- Have descriptive lowercase_with_underscores names.
- Do one clear job where possible.
- Use spaces around operators.
- Use blank lines to separate logical sections.
- Have docstrings when they are public/reusable.
- Keep parameter lists readable.

Methods are functions defined inside classes.
Instance methods normally use self as their first parameter.
Class methods normally use cls as their first parameter.
Static methods do not receive self or cls automatically.
"""

class Calculator:
    """Perform simple arithmetic operations."""

    def add(self, first_number, second_number):
        """Return the sum of two numbers."""
        return first_number + second_number

    @classmethod
    def description(cls):
        """Return a description of this class."""
        return f"{cls.__name__} provides basic calculations."

    @staticmethod
    def is_positive(number):
        """Return True when the supplied number is positive."""
        return number > 0


calculator = Calculator()

print("\n--- METHOD STYLE EXAMPLE ---")
print("Addition:", calculator.add(4, 6))
print("Description:", Calculator.description())
print("Is 10 positive?", Calculator.is_positive(10))

# ============================================================
# 20. CONSTANTS
# ============================================================

"""
A constant is a value intended not to change during normal program use.

Python does not enforce constants. The uppercase naming style communicates
that developers should treat the value as constant.

Example:
    MAX_LOGIN_ATTEMPTS = 5
    VAT_RATE = 0.075

Use descriptive uppercase names with underscores.
"""

MAX_LOGIN_ATTEMPTS = 5
VAT_RATE = 0.075

print("\n--- CONSTANT EXAMPLE ---")
print("Maximum login attempts:", MAX_LOGIN_ATTEMPTS)
print("VAT rate:", VAT_RATE)

# ============================================================
# 21. COMMON PEP 8 STYLE CHECKING TOOLS
# ============================================================

"""
You can check code style automatically.

Option 1: pycodestyle
Install:
    python -m pip install pycodestyle

Check one file:
    python -m pycodestyle student_app.py

Option 2: flake8
Install:
    python -m pip install flake8

Check one file:
    python -m flake8 student_app.py

pycodestyle checks many PEP 8 style issues.
flake8 combines pycodestyle checks with other basic code checks.

These tools report issues; they do not automatically rewrite your code.

Option 3: autopep8
Install:
    python -m pip install autopep8

Format a file:
    python -m autopep8 --in-place --aggressive student_app.py

Always review automatically changed code. A formatter cannot decide every
design or readability question for you.
"""

# ============================================================
# 22. PRACTICAL BEFORE-AND-AFTER CLASS EXERCISE
# ============================================================

"""
The following example is deliberately written in a poor style.
It is stored as text so it does not affect the runnable guide.
Ask students to identify the problems before showing the improved version.

POOR STYLE:

    import os,sys
    studentName="Ada"
    MAXattempts=3
    def calculateTotal(a,b):
      total=a+b
      return total
    class student:
      def __init__(self,name):
        self.Name=name
      def show(self):
        print(self.Name)

Problems:
- Imports are combined.
- Variable names do not follow the recommended style.
- Constant does not use uppercase_with_underscores consistently.
- Function name is not lowercase_with_underscores.
- Indentation uses two spaces.
- Class name is not CapWords.
- Attribute name starts with uppercase.
- There are no docstrings for public functions/classes.

IMPROVED VERSION:
"""

STUDENT_NAME = "Ada"
MAX_ATTEMPTS = 3


def calculate_total(first_number, second_number):
    """Return the sum of two numbers."""
    total = first_number + second_number
    return total


class Student:
    """Represent a student."""

    def __init__(self, name):
        self.name = name

    def show(self):
        """Display the student's name."""
        print(self.name)


print("\n--- IMPROVED PEP 8 EXAMPLE ---")
print("Student:", STUDENT_NAME)
print("Maximum attempts:", MAX_ATTEMPTS)
print("Total:", calculate_total(10, 20))

student = Student("Ada")
student.show()

# ============================================================
# 23. PRACTICAL STUDENT TASK
# ============================================================

"""
TASK: REFACTOR A STUDENT REPORT PROGRAM

Students should create a file called student_app.py.

Requirements:
1. Create a constant named PASS_MARK.
2. Create a class named Student.
3. Store student_name and student_score as instance attributes.
4. Create a method named has_passed().
5. Create a function named calculate_average().
6. Use four spaces for indentation.
7. Use descriptive variable and function names.
8. Add docstrings to public classes and functions.
9. Separate imports into the correct groups.
10. Keep lines within the PEP 8 recommended limit.
11. Run pycodestyle or flake8 against the file.
12. Fix reported issues and run the checker again.

STARTER CODE:
"""

PASS_MARK = 50


class Student:
    """Represent a student and their examination score."""

    def __init__(self, student_name, student_score):
        self.student_name = student_name
        self.student_score = student_score

    def has_passed(self):
        """Return True if the student meets the pass mark."""
        return self.student_score >= PASS_MARK


def calculate_average(scores):
    """Return the average of a list of scores."""
    if not scores:
        return 0

    return sum(scores) / len(scores)


classroom_students = [
    Student("Ada", 85),
    Student("Tunde", 42),
    Student("Mina", 73),
]

print("\n--- STUDENT REPORT TASK ---")

for classroom_student in classroom_students:
    result = "Passed" if classroom_student.has_passed() else "Failed"
    print(classroom_student.student_name, result)

class_scores = [
    classroom_student.student_score
    for classroom_student in classroom_students
]

print("Class average:", calculate_average(class_scores))

# ============================================================
# 24. LESSON SUMMARY
# ============================================================

"""
Remember the most important PEP 8 conventions:

INDENTATION
- Use four spaces.
- Do not mix tabs and spaces.

LINE LENGTH
- Keep code lines to 79 characters where practical.
- Keep comments and docstrings to 72 characters where practical.
- Use parentheses to split long expressions.

BLANK LINES
- Two blank lines around top-level classes and functions.
- One blank line between methods.

NAMING
- variables and functions: snake_case.
- classes: CapWords.
- constants: UPPER_CASE.
- modules: short lowercase names.
- use self for instance methods and cls for class methods.

IMPORTS
- Put imports near the top.
- Group standard library, third-party, and local imports.
- Separate groups with blank lines.
- Avoid wildcard imports.

COMMENTS AND DOCSTRINGS
- Write clear comments.
- Avoid comments that merely repeat the code.
- Document public modules, classes, and functions.

OTHER STYLE
- Use spaces around operators.
- Avoid multiple statements on one line.
- Compare with None using is None.
- Catch specific exceptions.
- Use with for file handling.
- Keep the code consistent and easy to read.
"""

# ============================================================
# 25. OBJECTIVE TEST — 20 QUESTIONS
# ============================================================

"""
Instructions:
- Choose ONE correct option: A, B, C, or D.
- Each question carries 1 mark.
- Total score: 20 marks.
- The teacher's answer key is at the bottom. Hide it before sharing.

QUESTION 1
What is PEP 8?
A. A Python database
B. A style guide for Python code
C. A web framework
D. A testing library

QUESTION 2
What does PEP stand for?
A. Python Enhancement Proposal
B. Python Execution Process
C. Program Error Prevention
D. Python Extension Package

QUESTION 3
How many spaces are recommended for each indentation level?
A. 2
B. 3
C. 4
D. 8

QUESTION 4
What is the recommended maximum code line length in PEP 8?
A. 40 characters
B. 79 characters
C. 100 characters in every project
D. 120 characters

QUESTION 5
Which name follows the recommended variable naming style?
A. studentName
B. StudentName
C. student_name
D. STUDENTNAME

QUESTION 6
Which name follows the recommended class naming style?
A. student_record
B. StudentRecord
C. studentRecord
D. STUDENT_RECORD

QUESTION 7
Which name is suitable for a constant?
A. max_attempts
B. MaxAttempts
C. MAX_ATTEMPTS
D. maxAttempts

QUESTION 8
Which is the recommended function name?
A. CalculateTotal
B. calculate_total
C. calculateTotal
D. CALCULATE_TOTAL

QUESTION 9
Where should imports normally appear?
A. At the bottom of the file
B. Near the top of the file
C. Inside every function
D. After the return statement

QUESTION 10
Which import style is preferred?
A. import os, sys
B. import os followed by import sys on separate lines
C. import everything
D. imports should be written as comments

QUESTION 11
Which is the correct order for grouping imports?
A. Local, standard library, third-party
B. Third-party, local, standard library
C. Standard library, third-party, local
D. Any order is required

QUESTION 12
What is a docstring used for?
A. Documenting a module, class, function, or method
B. Installing a package
C. Creating a database
D. Renaming a variable

QUESTION 13
Which is a recommended way to check for None?
A. value == None
B. value is None
C. value equals None
D. value = None

QUESTION 14
Which is the recommended boolean condition?
A. if is_active == True:
B. if True is is_active:
C. if is_active:
D. if is_active = True:

QUESTION 15
Which method parameter name is conventional for an instance method?
A. this
B. self
C. object
D. current

QUESTION 16
Which attribute name follows the recommended naming style?
A. self.StudentName
B. self.student_name
C. self.STUDENTNAME
D. self.studentName

QUESTION 17
What is the purpose of a leading underscore in a name such as _internal_value?
A. It suggests the name is intended for internal use
B. It makes the value a constant
C. It makes the value public
D. It installs a package

QUESTION 18
Which tool can check many PEP 8 style issues?
A. pycodestyle
B. requests
C. pandas
D. selenium

QUESTION 19
Which command checks a file with pycodestyle?
A. python -m pycodestyle student_app.py
B. git install student_app.py
C. python student_app.py --format-pep
D. pip run student_app.py

QUESTION 20
Does PEP 8 determine whether Python syntax is valid?
A. Yes, it replaces Python syntax rules
B. No, it is a style guide for readability and consistency
C. Yes, it only applies to classes
D. No, it is a database specification
"""

# ============================================================
# 26. TEACHER'S ANSWER KEY
# ============================================================

"""
Hide or remove this section before giving the test to students.

1. B
2. A
3. C
4. B
5. C
6. B
7. C
8. B
9. B
10. B
11. C
12. A
13. B
14. C
15. B
16. B
17. A
18. A
19. A
20. B
"""

# ============================================================
# 27. OPTIONAL TEACHER DEMONSTRATION: CHECK THIS FILE
# ============================================================

"""
Install pycodestyle in your active virtual environment:
    python -m pip install pycodestyle

Check this teaching file:
    python -m pycodestyle pep8_advanced_python_teaching_guide.py

The checker may report style findings in a long teaching file because it
contains many code examples, comments, and classroom sections. Use it to
demonstrate how a checker reports issues; do not assume every teaching note
file must itself be a perfectly formatted production application.

For a student's actual project, run:
    python -m pycodestyle student_app.py

A style checker reports issues; it does not prove that a program is correct.
"""

if __name__ == "__main__":
    print("\nPEP 8 — PYTHON CODE STYLE GUIDE")
    print("This teaching file is valid Python.")
    print("Follow the sections and run the practical examples in VS Code.")
    print("Install a checker with: python -m pip install pycodestyle")
