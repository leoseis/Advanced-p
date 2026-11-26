# ============================================================
# ADVANCED PYTHON: TESTING WITH unittest AND pytest
# Simplified teaching guide for VS Code
# ============================================================
#
# LESSON OBJECTIVES
# By the end of this lesson, students should be able to:
# 1. Explain software testing and why it is important.
# 2. Write simple tests using Python's built-in unittest.
# 3. Understand assertions and test failures.
# 4. Write and run tests using pytest.
# 5. Test normal cases, edge cases, and invalid inputs.
#
# IMPORTANT:
# This file is a TEACHING GUIDE. The examples under each section
# are meant to be copied into separate files when practising.
# Do not run this whole guide as one test file.
#
# ------------------------------------------------------------
# 1. WHAT IS SOFTWARE TESTING?
# ------------------------------------------------------------
#
# Software testing means checking whether our code behaves as
# expected.
#
# Example: if add(2, 3) is meant to add two numbers, we expect 5.
# A test checks whether the function really returns 5.
#
# Testing helps us:
# - Find bugs early.
# - Prevent old bugs from returning.
# - Check that changes have not broken existing features.
# - Build confidence in our code.
#
# A UNIT TEST checks a small part of a program, often one function
# or one method, separately from the rest of the application.
#
# ------------------------------------------------------------
# 2. CREATE A PRACTICE FOLDER
# ------------------------------------------------------------
#
# In VS Code, create a folder named python_testing.
#
# Inside it, create these files:
#
#     python_testing/
#         calculator.py
#         test_unittest_calculator.py
#         test_calculator.py
#
# The first file contains the code we want to test.
# The other files contain tests.
#
# ------------------------------------------------------------
# 3. WRITE THE CODE WE WANT TO TEST
# ------------------------------------------------------------
#
# File: calculator.py
#
# Copy the code below into calculator.py:
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# def divide(a, b):
#     if b == 0:
#         raise ValueError("Cannot divide by zero")
#     return a / b
#
# Teaching note:
# We keep the functions in a separate file so both testing tools
# can import and test the same code.
#
# ------------------------------------------------------------
# 4. IMPORTANT TESTING WORDS
# ------------------------------------------------------------
#
# Test case:
# A check of one particular behaviour.
#
# Expected result:
# The result we believe the code should produce.
#
# Actual result:
# The result the code really produces.
#
# Assertion:
# A statement that checks whether something is true or correct.
# If the assertion fails, the test fails.
#
# Example:
#     assert add(2, 3) == 5
#
# This means: "Check that adding 2 and 3 gives 5."
#
# ------------------------------------------------------------
# 5. PYTHON'S BUILT-IN unittest
# ------------------------------------------------------------
#
# unittest is included with Python. You do not need to install it.
# It commonly uses classes that inherit from unittest.TestCase.
#
# File: test_unittest_calculator.py
#
# Copy this into test_unittest_calculator.py:
#
# import unittest
# from calculator import add, subtract, multiply, divide
#
# class CalculatorTests(unittest.TestCase):
#
#     def test_add(self):
#         self.assertEqual(add(2, 3), 5)
#
#     def test_subtract(self):
#         self.assertEqual(subtract(8, 3), 5)
#
#     def test_multiply(self):
#         self.assertEqual(multiply(4, 3), 12)
#
#     def test_divide(self):
#         self.assertEqual(divide(10, 2), 5)
#
#     def test_divide_by_zero(self):
#         with self.assertRaises(ValueError):
#             divide(10, 0)
#
# if __name__ == "__main__":
#     unittest.main()
#
# EXPLANATION:
# - import unittest: imports Python's testing framework.
# - TestCase: base class that provides testing methods.
# - test_add: test method; names normally begin with test_.
# - assertEqual(actual, expected): checks that two values match.
# - assertRaises(ValueError): checks that the code raises the
#   expected error.
# - unittest.main(): discovers and runs tests in this file.
#
# RUN IT:
# Open the VS Code terminal in the practice folder and run:
#
#     python -m unittest -v test_unittest_calculator.py
#
# Expected result: five tests should pass.
#
# ------------------------------------------------------------
# 6. COMMON unittest ASSERTIONS
# ------------------------------------------------------------
#
# self.assertEqual(a, b)       # a equals b
# self.assertNotEqual(a, b)    # a does not equal b
# self.assertTrue(condition)   # condition is True
# self.assertFalse(condition)  # condition is False
# self.assertIsNone(value)     # value is None
# self.assertIn(item, collection)  # item exists in collection
# self.assertRaises(ErrorType) # expected exception is raised
#
# Teacher demonstration:
#     self.assertTrue(5 > 2)
#     self.assertIn("py", "python")
#
# ------------------------------------------------------------
# 7. INTRODUCING pytest
# ------------------------------------------------------------
#
# pytest is a popular third-party testing framework. It often
# requires less code than unittest and uses normal assert statements.
#
# INSTALL IT IN YOUR PROJECT'S VIRTUAL ENVIRONMENT:
#
#     python -m pip install pytest
#
# Check installation:
#
#     python -m pytest --version
#
# Create or use this file:
# test_calculator.py
#
# Copy the code below into test_calculator.py:
#
# from calculator import add, subtract, multiply, divide
# import pytest
#
# def test_add():
#     assert add(2, 3) == 5
#
# def test_subtract():
#     assert subtract(8, 3) == 5
#
# def test_multiply():
#     assert multiply(4, 3) == 12
#
# def test_divide():
#     assert divide(10, 2) == 5
#
# def test_divide_by_zero():
#     with pytest.raises(ValueError):
#         divide(10, 0)
#
# RUN THE TESTS:
#
#     python -m pytest -v
#
# pytest looks for files named test_*.py or *_test.py and functions
# named test_* by default.
#
# The -v option means "verbose": it displays each test name.
#
# ------------------------------------------------------------
# 8. unittest VS pytest
# ------------------------------------------------------------
#
# unittest:
# - Comes with Python.
# - Commonly uses TestCase classes.
# - Uses methods such as self.assertEqual().
#
# pytest:
# - Must be installed separately.
# - Commonly uses ordinary functions.
# - Uses Python's assert statement.
# - Offers helpful failure details and many useful extensions.
#
# Both can test functions, classes, and many kinds of application
# behaviour. pytest can also run many unittest-style tests.
#
# ------------------------------------------------------------
# 9. TEST NORMAL CASES, EDGE CASES, AND ERRORS
# ------------------------------------------------------------
#
# Normal case:
#     add(2, 3) should return 5.
#
# Edge case:
#     add(0, 0) should return 0.
#
# Error case:
#     divide(10, 0) should raise ValueError.
#
# Good testing means checking more than one happy-path example.
# Think about empty values, zero, negative numbers, and invalid input.
#
# Example extra tests to add to test_calculator.py:
#
# def test_add_negative_numbers():
#     assert add(-2, -3) == -5
#
# def test_add_zero():
#     assert add(0, 0) == 0
#
# def test_divide_returns_decimal_when_needed():
#     assert divide(5, 2) == 2.5
#
# ------------------------------------------------------------
# 10. PRACTICAL CLASS EXERCISE
# ------------------------------------------------------------
#
# Ask students to create a file called student_utils.py containing:
#
# def is_even(number):
#     return number % 2 == 0
#
# def get_grade(score):
#     if score < 0 or score > 100:
#         raise ValueError("Score must be from 0 to 100")
#     if score >= 70:
#         return "A"
#     if score >= 60:
#         return "B"
#     if score >= 50:
#         return "C"
#     if score >= 45:
#         return "D"
#     return "F"
#
# STUDENT TASK:
# Write pytest tests for:
# - is_even(4) returning True.
# - is_even(7) returning False.
# - get_grade(75) returning "A".
# - get_grade(60) returning "B".
# - get_grade(40) returning "F".
# - get_grade(-1) raising ValueError.
# - get_grade(101) raising ValueError.
#
# Suggested command:
#
#     python -m pytest -v
#
# ------------------------------------------------------------
# 11. HOW THIS CONNECTS TO DJANGO TESTING
# ------------------------------------------------------------
#
# The principles are the same:
# - Arrange: prepare the data or conditions.
# - Act: run the function, method, or request.
# - Assert: check the result.
#
# In plain Python, we might test add(2, 3).
# In Django, we might test a model method, a view, or an API request.
#
# Django supplies extra tools for requests, test databases, clients,
# and application configuration. You do not need Django to learn the
# basic testing ideas in this lesson.
#
# ------------------------------------------------------------
# 12. OBJECTIVE QUESTIONS
# Choose ONE correct answer for each question.
# Answers are provided at the bottom for the teacher.
# ------------------------------------------------------------
#
# Q1. What is the main purpose of software testing?
# A. To make code longer
# B. To check whether code behaves as expected
# C. To delete functions
# D. To install Python
#
# Q2. Which testing framework is included with Python?
# A. pytest
# B. Django
# C. unittest
# D. Flask
#
# Q3. Which command installs pytest?
# A. python -m pip install pytest
# B. python install unittest
# C. pip remove pytest
# D. django start pytest
#
# Q4. In unittest, test classes commonly inherit from:
# A. unittest.Function
# B. unittest.TestCase
# C. unittest.Test
# D. unittest.Pytest
#
# Q5. Which unittest method checks that two values are equal?
# A. assertSame()
# B. assertTrueEqual()
# C. assertEqual()
# D. assertMatch()
#
# Q6. In pytest, which statement checks that add(2, 3) equals 5?
# A. assert add(2, 3) == 5
# B. check add(2, 3) = 5
# C. verify(add(2, 3), 5)
# D. print(add(2, 3) == 5)
#
# Q7. Which name is normally discovered as a pytest test function?
# A. calculate_total
# B. run_test_now
# C. test_add
# D. add_test_function_only
#
# Q8. What does the -v option usually do when running pytest?
# A. Deletes tests
# B. Shows more detailed test output
# C. Installs pytest
# D. Creates a Django project
#
# Q9. What does pytest.raises(ValueError) check?
# A. That a ValueError is expected to be raised
# B. That a function returns a string
# C. That all tests pass automatically
# D. That pytest is installed
#
# Q10. Which is an example of an edge case for addition?
# A. Adding zero to zero
# B. Installing Python
# C. Opening VS Code
# D. Renaming a folder
#
# Q11. What is a unit test commonly designed to test?
# A. An entire company
# B. A small unit of code such as a function
# C. The computer screen
# D. Internet speed
#
# Q12. Does basic unittest require a separate pip installation?
# A. Yes, always
# B. Only on Linux
# C. No, it is included with Python
# D. Only when using Django
#
# Q13. Which command can run the example pytest tests?
# A. python -m pytest -v
# B. python -m install tests
# C. django run pytest
# D. python --delete-tests
#
# Q14. What should a test do if divide(10, 0) is designed to raise
# ValueError?
# A. Ignore the result
# B. Check that ValueError is raised
# C. Change the function silently
# D. Print "success" without checking
#
# Q15. How does Django testing relate to Python testing?
# A. They have no shared principles
# B. Django testing applies testing principles with extra web tools
# C. Django can only test HTML colours
# D. Python tests cannot test functions
#
# ------------------------------------------------------------
# ANSWER KEY (FOR TEACHER)
# ------------------------------------------------------------
#
# 1. B
# 2. C
# 3. A
# 4. B
# 5. C
# 6. A
# 7. C
# 8. B
# 9. A
# 10. A
# 11. B
# 12. C
# 13. A
# 14. B
# 15. B
#
# END OF TEACHING GUIDE
