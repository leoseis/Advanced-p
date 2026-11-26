"""
PYTHON FOR COMPLETE BEGINNERS
TEACHING GUIDE: FUNDAMENTAL DATA TYPES AND OPERATORS
===================================================

Instructor: Leonard Emelieze
Level: Complete Beginners
Suggested duration: 2-3 hours

HOW TO USE THIS FILE
--------------------
1. Open this file in VS Code.
2. Teach the explanations in order.
3. Run the file with: python beginner_data_types_and_operators.py
4. Ask students to predict the output before running each example.
5. Students should complete the exercises and multiple-choice questions.

A Python file can contain explanations as comments and executable examples as code.
This file is designed to be both a teaching note and a practical lesson.

LEARNING OBJECTIVES
-------------------
By the end of this lesson, students should be able to:
- Explain what a data type is.
- Recognise int, float, str, bool, and NoneType.
- Use type() to inspect a value's type.
- Create variables and assign values.
- Use arithmetic, comparison, assignment, logical, membership, and identity operators.
- Convert simple values from one type to another.
- Read basic expressions and predict their results.
- Answer the multiple-choice questions at the end.

===========================================================
SECTION 1: WHAT IS PYTHON?
===========================================================

Python is a programming language. We use it to give instructions to a computer.

Example:
    print("Hello, world!")

The print() function displays information on the screen.

Try this:
"""

print("Hello, world!")
print("Welcome to Python!")

"""
===========================================================
SECTION 2: VARIABLES
===========================================================

A variable is a name used to refer to a value.

Example:
    student_name = "Ada"
    age = 18

Here:
- student_name is a variable containing the text "Ada".
- age is a variable containing the number 18.
- The = symbol assigns a value to a variable.

Variable naming rules for beginners:
- A name can contain letters, numbers, and underscores.
- A name must not begin with a number.
- Variable names are case-sensitive: age and Age are different.
- Do not use Python keywords such as if, for, or class as variable names.
- Use meaningful names, such as student_age rather than x when possible.

Try:
"""

student_name = "Ada"
age = 18
print("Student:", student_name)
print("Age:", age)

"""
===========================================================
SECTION 3: FUNDAMENTAL PYTHON DATA TYPES
===========================================================

A data type describes the kind of value a variable contains.

The main beginner types are:
1. int      - whole numbers
2. float    - numbers with a decimal point
3. str      - text
4. bool     - True or False
5. NoneType - represents the absence of a value

-----------------------------------------------------------
3.1 INTEGER (int)
-----------------------------------------------------------

An integer is a whole number without a decimal point.

Examples:
    number_of_students = 25
    temperature = -4
    score = 100

Integers can be positive, negative, or zero.
"""

number_of_students = 25
temperature = -4
score = 100

print("\nINTEGER EXAMPLES")
print(number_of_students)
print(temperature)
print(score)
print(type(number_of_students))  # <class 'int'>

"""
-----------------------------------------------------------
3.2 FLOAT (float)
-----------------------------------------------------------

A float is a number that contains a decimal point.

Examples:
    price = 1500.50
    height = 1.75
    average_score = 72.5

Python may also represent some very large or very small numbers using
scientific notation.
"""

price = 1500.50
height = 1.75
average_score = 72.5

print("\nFLOAT EXAMPLES")
print(price)
print(height)
print(average_score)
print(type(price))  # <class 'float'>

"""
-----------------------------------------------------------
3.3 STRING (str)
-----------------------------------------------------------

A string is text. Put text inside quotation marks.

Single quotes:
    first_name = 'Leonard'

Double quotes:
    greeting = "Good morning"

Both are valid. Use matching opening and closing quotation marks.

A string can contain letters, digits, spaces, and symbols:
    message = "Python is fun!"
    phone_label = "08012345678"

Important:
    age = 20       # integer
    age_text = "20"  # string

Although both contain the characters 2 and 0, they are different types.
You can perform arithmetic with the integer 20, but "20" is text.
"""

first_name = "Leonard"
greeting = "Good morning"
message = "Python is fun!"
age_as_number = 20
age_as_text = "20"

print("\nSTRING EXAMPLES")
print(first_name)
print(greeting)
print(message)
print(type(first_name))
print(type(age_as_number))
print(type(age_as_text))

"""
String concatenation means joining strings with +.
"""

first = "Python"
second = "Programming"
combined = first + " " + second
print("\nSTRING CONCATENATION:", combined)

"""
Do not try to add a string and an integer directly:
    print("Age: " + 20)  # TypeError

Convert the number to a string or use an f-string:
"""
age = 20
print("Age:", age)
print("Age: " + str(age))
print(f"Age: {age}")

"""
An f-string lets you place variable values inside a string using { }.
It is often a clear way to display information.
"""

"""
-----------------------------------------------------------
3.4 BOOLEAN (bool)
-----------------------------------------------------------

A Boolean has only two possible values:
    True
    False

Booleans are useful when a program needs to make a decision.

Examples:
    is_registered = True
    has_paid = False

Remember: True and False begin with capital letters.
"""

is_registered = True
has_paid = False

print("\nBOOLEAN EXAMPLES")
print(is_registered)
print(has_paid)
print(type(is_registered))

"""
-----------------------------------------------------------
3.5 NONE (NoneType)
-----------------------------------------------------------

None represents no value or an absence of a value.
It is not the same as 0, False, or an empty string.

Example:
    middle_name = None

A program might use None when information has not been provided yet.
"""

middle_name = None
print("\nNONE EXAMPLE:", middle_name)
print(type(middle_name))  # <class 'NoneType'>

"""
-----------------------------------------------------------
3.6 CHECKING A VALUE'S TYPE
-----------------------------------------------------------

Use type(value) to check the data type of a value.
"""

print("\nCHECKING TYPES")
print(type(45))          # int
print(type(3.14))        # float
print(type("Hello"))     # str
print(type(False))       # bool
print(type(None))        # NoneType

"""
-----------------------------------------------------------
3.7 CONVERTING BETWEEN TYPES
-----------------------------------------------------------

Type conversion changes a value from one type to another.

Common conversion functions:
- int(value)   converts a suitable value to an integer.
- float(value) converts a suitable value to a float.
- str(value)   converts a value to text.
- bool(value)  converts a value to True or False according to truthiness.

Examples:
"""

number_text = "42"
number = int(number_text)
print("\nTYPE CONVERSION")
print(number, type(number))

decimal_text = "3.5"
decimal_number = float(decimal_text)
print(decimal_number, type(decimal_number))

marks = 85
marks_text = str(marks)
print(marks_text, type(marks_text))

print(bool(1))       # True
print(bool(0))       # False
print(bool(""))      # False: empty string
print(bool("Hello")) # True: non-empty string

"""
Important notes:
- int("42") works, but int("hello") raises ValueError.
- int(3.9) produces 3; it removes the decimal part rather than rounding.
- bool(0), bool(""), and bool(None) are False.
- Most other values, including non-empty strings and non-zero numbers, are True.

===========================================================
SECTION 4: PYTHON OPERATORS
===========================================================

An operator is a symbol or keyword that performs an operation on values.

Example:
    5 + 3

Here, + is the operator and 5 and 3 are operands.

We will learn:
1. Arithmetic operators
2. Comparison operators
3. Assignment operators
4. Logical operators
5. Membership operators
6. Identity operators
7. Operator precedence

-----------------------------------------------------------
4.1 ARITHMETIC OPERATORS
-----------------------------------------------------------

These operators perform mathematical calculations.

Operator   Meaning                  Example       Result
+          Addition                 8 + 2         10
-          Subtraction              8 - 2          6
*          Multiplication           8 * 2         16
/          Division                 8 / 2          4.0
//         Floor division           9 // 2         4
%          Modulus (remainder)      9 % 2          1
**         Exponent/power           2 ** 3         8

Notice that / normally returns a float, even when the answer is a whole number.
Floor division // gives the quotient rounded down toward negative infinity.
The modulus operator % gives the remainder.
The ** operator raises a number to a power.
"""

print("\nARITHMETIC OPERATORS")
print("Addition:", 8 + 2)
print("Subtraction:", 8 - 2)
print("Multiplication:", 8 * 2)
print("Division:", 8 / 2)
print("Floor division:", 9 // 2)
print("Remainder:", 9 % 2)
print("Power:", 2 ** 3)

"""
PRACTICAL EXAMPLE: CALCULATING A TOTAL
"""

item_price = 2500
quantity = 3
total_cost = item_price * quantity
print("Total cost:", total_cost)

"""
PRACTICAL EXAMPLE: EVEN OR ODD
The remainder when an even number is divided by 2 is 0.
"""
number = 14
print("Remainder:", number % 2)
print("Is the number even?", number % 2 == 0)

"""
-----------------------------------------------------------
4.2 COMPARISON OPERATORS
-----------------------------------------------------------

Comparison operators compare values and return True or False.

Operator   Meaning                         Example       Result
==         Equal to                        5 == 5        True
!=         Not equal to                    5 != 3        True
>          Greater than                    8 > 3         True
<          Less than                       2 < 7         True
>=         Greater than or equal to        5 >= 5        True
<=         Less than or equal to           4 <= 6        True

Important:
- = assigns a value.
- == compares two values.

Example:
    age = 18       # assignment
    age == 18      # comparison; result is True
"""

print("\nCOMPARISON OPERATORS")
print("5 == 5:", 5 == 5)
print("5 != 3:", 5 != 3)
print("8 > 3:", 8 > 3)
print("2 < 7:", 2 < 7)
print("5 >= 5:", 5 >= 5)
print("4 <= 6:", 4 <= 6)

"""
PRACTICAL EXAMPLE: CHECKING PASS MARK
"""

student_mark = 65
pass_mark = 50
print("Did the student pass?", student_mark >= pass_mark)

"""
-----------------------------------------------------------
4.3 ASSIGNMENT OPERATORS
-----------------------------------------------------------

Assignment operators store or update values in variables.

Operator   Example       Same general idea as
=          x = 5         assign 5 to x
+=         x += 2        x = x + 2
-=         x -= 2        x = x - 2
*=         x *= 2        x = x * 2
/=         x /= 2        x = x / 2
//=        x //= 2       x = x // 2
%=         x %= 2        x = x % 2
**=        x **= 2       x = x ** 2
"""

print("\nASSIGNMENT OPERATORS")
counter = 10
print("Starting value:", counter)

counter += 5
print("After counter += 5:", counter)

counter -= 3
print("After counter -= 3:", counter)

counter *= 2
print("After counter *= 2:", counter)

"""
-----------------------------------------------------------
4.4 LOGICAL OPERATORS
-----------------------------------------------------------

Logical operators combine or reverse conditions.

and: True only when both conditions are True.
or:  True when at least one condition is True.
not: Reverses a Boolean result.

Examples:
    True and True   -> True
    True and False  -> False
    True or False   -> True
    False or False  -> False
    not True        -> False
"""

print("\nLOGICAL OPERATORS")
print("True and True:", True and True)
print("True and False:", True and False)
print("True or False:", True or False)
print("False or False:", False or False)
print("not True:", not True)

"""
PRACTICAL EXAMPLE: ELIGIBILITY
A student must have a mark of at least 50 AND must have submitted the assignment.
"""

mark = 70
assignment_submitted = True
eligible = mark >= 50 and assignment_submitted
print("Eligible:", eligible)

"""
-----------------------------------------------------------
4.5 MEMBERSHIP OPERATORS: in AND not in
-----------------------------------------------------------

Membership operators check whether a value exists inside a sequence,
such as a string, list, or tuple.

Examples:
    "py" in "python"       -> True
    4 in [1, 2, 3]         -> False
    "red" not in ["blue"]  -> True
"""

print("\nMEMBERSHIP OPERATORS")
print("'py' in 'python':", "py" in "python")
print("4 in [1, 2, 3]:", 4 in [1, 2, 3])
print("'red' not in ['blue']:", "red" not in ["blue"])

"""
-----------------------------------------------------------
4.6 IDENTITY OPERATORS: is AND is not
-----------------------------------------------------------

Identity operators check whether two references point to the same object.
They are not simply another way to compare values.

- == checks whether values are equal.
- is checks whether two references identify the same object.

For beginners, a common and recommended use is:
    if result is None:
        ...

Do not normally use 'is' to compare ordinary numbers or strings for equality.
Use == for value comparisons.
"""

print("\nIDENTITY OPERATORS")
result = None
print("result is None:", result is None)
print("result is not None:", result is not None)

"""
-----------------------------------------------------------
4.7 OPERATOR PRECEDENCE
-----------------------------------------------------------

Operator precedence determines which operations happen first.

A useful beginner rule:
1. Parentheses ()
2. Exponents **
3. Multiplication, division, floor division, and modulus: *, /, //, %
4. Addition and subtraction: +, -
5. Comparisons: ==, !=, >, <, >=, <=
6. not
7. and
8. or

Use parentheses when they make an expression clearer.

Example:
    2 + 3 * 4       -> 14, because multiplication happens first.
    (2 + 3) * 4     -> 20, because parentheses happen first.
"""

print("\nOPERATOR PRECEDENCE")
print("2 + 3 * 4 =", 2 + 3 * 4)
print("(2 + 3) * 4 =", (2 + 3) * 4)

"""
===========================================================
SECTION 5: INPUT FROM THE USER
===========================================================

input() collects information typed by the user.
Important: input() returns a string, even if the user types digits.

Example:
    age_text = input("Enter your age: ")
    age = int(age_text)

The following example is inside a function so the teaching file can run
without pausing for input. Call the function when you want to demonstrate it.
"""


def demonstrate_input():
    """Ask the user for two numbers and display their sum."""
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    print("The sum is:", first_number + second_number)


"""
To run the input demonstration, remove the # from the line below:
# demonstrate_input()

===========================================================
SECTION 6: COMMON BEGINNER ERRORS
===========================================================

1. Mixing strings and numbers:
       "5" + 2
   This raises TypeError. Convert one value if appropriate.

2. Using = instead of == in a comparison:
       age = 18    # assignment
       age == 18   # comparison

3. Forgetting quotation marks around text:
       name = Ada      # NameError if Ada is not a defined variable
       name = "Ada"    # correct

4. Using lowercase true/false:
       is_ready = true     # NameError
       is_ready = True     # correct

5. Dividing by zero:
       10 / 0
   This raises ZeroDivisionError.

6. Converting invalid text to a number:
       int("hello")
   This raises ValueError.

===========================================================
SECTION 7: CLASSROOM PRACTICE
===========================================================

Ask students to write the code and predict the output before running it.

EXERCISE 1: DATA TYPES
Create variables for:
- Your name
- Your age
- Your height in metres
- Whether you enjoy Python
- A value that is currently unknown

Print each value and its type using type().

EXERCISE 2: ARITHMETIC
Create two number variables and display:
- Their sum
- Their difference
- Their product
- Their division
- Their remainder

EXERCISE 3: COMPARISON
Store a student's mark in a variable. Display whether:
- The mark is greater than or equal to 50.
- The mark is less than 50.
- The mark is exactly 100.

EXERCISE 4: LOGICAL OPERATORS
Create variables named has_id and is_registered.
Use and to check whether both are True.
Use or to check whether at least one is True.

EXERCISE 5: TYPE CONVERSION
Convert the string "120" to an integer.
Add 30 to it and print the answer.

===========================================================
SECTION 8: MULTIPLE-CHOICE / OBJECTIVE QUESTIONS
===========================================================

Instructions:
- Choose ONE correct option for each question.
- Each question carries 1 mark.
- Total: 20 marks.

1. Which data type stores a whole number?
   A. str
   B. int
   C. bool
   D. float

2. What is the data type of 4.75?
   A. int
   B. str
   C. float
   D. bool

3. Which value is a Boolean?
   A. "True"
   B. 1
   C. True
   D. "False"

4. Which of these is a string?
   A. 25
   B. 2.5
   C. False
   D. "25"

5. Which function checks the data type of a value?
   A. print()
   B. type()
   C. input()
   D. str()

6. What is the result of 7 + 3?
   A. 4
   B. 10
   C. 21
   D. 73

7. What is the result of 10 // 3?
   A. 3
   B. 3.33
   C. 1
   D. 0

8. What is the result of 10 % 3?
   A. 3
   B. 0
   C. 1
   D. 10

9. Which operator means exponentiation (power)?
   A. //
   B. %
   C. **
   D. !=

10. Which operator checks whether two values are equal?
    A. =
    B. ==
    C. =>
    D. !=

11. What is the result of 5 > 8?
    A. True
    B. False
    C. 5
    D. Error

12. Which operator means “not equal to”?
    A. ==
    B. =
    C. !=
    D. <=

13. What does x += 4 generally mean?
    A. x = 4
    B. x = x + 4
    C. x = x - 4
    D. x == 4

14. What is the result of True and False?
    A. True
    B. False
    C. None
    D. 0.5

15. What is the result of True or False?
    A. True
    B. False
    C. None
    D. Error

16. What does not True return?
    A. True
    B. False
    C. None
    D. 1

17. What type of value does input() return by default?
    A. int
    B. float
    C. str
    D. bool

18. Which expression converts the string "42" to an integer?
    A. str("42")
    B. int("42")
    C. bool("42")
    D. type("42")

19. What does None represent in Python?
    A. The number zero only
    B. An empty list
    C. The absence of a value
    D. A string

20. Which operator checks whether "a" is contained in "cat"?
    A. is
    B. ==
    C. in
    D. and

===========================================================
SECTION 9: ANSWER KEY FOR THE INSTRUCTOR
===========================================================

1. B     2. C     3. C     4. D     5. B
6. B     7. A     8. C     9. C    10. B
11. B   12. C    13. B    14. B    15. A
16. B   17. C    18. B    19. C    20. C

Suggested marking:
- 17-20: Excellent understanding
- 13-16: Good understanding; revise missed questions
- 9-12: Needs more practice
- 0-8: Review the lesson and repeat the exercises

===========================================================
LESSON SUMMARY
===========================================================

Remember:
- int stores whole numbers.
- float stores decimal numbers.
- str stores text.
- bool stores True or False.
- None represents the absence of a value.
- type() checks a value's type.
- int(), float(), str(), and bool() are common conversion functions.
- Arithmetic operators calculate.
- Comparison operators return True or False.
- Assignment operators store or update values.
- Logical operators combine or reverse conditions.
- Membership operators use in and not in.
- Use == to compare values and = to assign a value.

END OF TEACHING GUIDE
"""
