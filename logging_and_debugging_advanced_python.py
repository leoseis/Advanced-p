"""
====================================================================
ADVANCED PYTHON
LOGGING AND DEBUGGING
====================================================================

Instructor: Leonard Emelieze

PURPOSE OF THIS LESSON
----------------------

This teaching file explains Logging and Debugging in Python from
the basics to practical usage.

The notes are written as Python comments so this file can be opened
directly in VS Code and used during class presentation.

IMPORTANT:
The code examples are normal Python code and are NOT commented out,
so they can be copied, run, and demonstrated.

TOPICS COVERED
--------------

1. What is debugging?
2. What is logging?
3. Why do we need logging?
4. print() versus logging
5. Python logging module
6. Logging levels
7. Basic logging
8. Log messages
9. Log levels in practice
10. Logging to a file
11. Logging format
12. Logging handlers
13. Logging exceptions
14. logging.exception()
15. try / except / finally
16. Debugging with print()
17. Debugging with breakpoint()
18. Debugging with pdb
19. Reading tracebacks
20. Finding and fixing errors
21. Practical debugging example
22. A small application with logging
23. Best practices
24. Summary
25. Student objective questions
26. Answer key

====================================================================
"""


# ==================================================================
# 1. WHAT IS DEBUGGING?
# ==================================================================

"""
Debugging means finding and fixing problems in a program.

A program can fail because of:

    - Syntax errors
    - Name errors
    - Type errors
    - Logic errors
    - Value errors
    - File errors
    - Network errors
    - Database errors

Example:

    number = 10
    result = number / 0

The program will fail because division by zero is not allowed.

Debugging is the process of asking:

    What went wrong?
    Where did it happen?
    Why did it happen?
    How can I fix it?

A simple debugging process is:

    1. Reproduce the problem.
    2. Read the error message.
    3. Find the line where the error occurred.
    4. Understand the cause.
    5. Fix the problem.
    6. Run the program again.
    7. Test the result.
"""


# ==================================================================
# 2. WHAT IS LOGGING?
# ==================================================================

"""
Logging means recording information about what is happening
inside a program.

For example, an application might record:

    User logged in.
    Database connection successful.
    File was opened.
    Payment was processed.
    An error occurred.
    Server started.

Instead of trying to guess what happened, we can look at the
log messages.

Think of logging as a diary for a program.

PROGRAM:

    Start application
          |
          v
    Connect database
          |
          v
    User logs in
          |
          v
    Process request
          |
          v
    Error occurs

LOG:

    Application started
    Database connected
    User login successful
    Processing request
    ERROR: Something went wrong
"""


# ==================================================================
# 3. WHY NOT JUST USE print()?
# ==================================================================

"""
Beginners commonly use print():

    print("Program started")
    print("User logged in")
    print("Something went wrong")

print() is useful when learning and debugging small programs.

However, professional applications normally use logging because
logging gives us more control.

Logging allows us to:

    - Separate important messages from ordinary messages.
    - Use different severity levels.
    - Save messages to files.
    - Include timestamps.
    - Include the module name.
    - Record exceptions.
    - Control what information is displayed.

Example:

    DEBUG
    INFO
    WARNING
    ERROR
    CRITICAL


SIMPLE COMPARISON:

print():

    print("User logged in")


logging:

    logger.info("User logged in")


For small classroom programs, print() is fine.

For larger applications, logging is much more useful.
"""


# ==================================================================
# 4. IMPORT THE LOGGING MODULE
# ==================================================================

"""
Python already provides a built-in logging module.

We do NOT normally need to install another package.

Use:

    import logging
"""

import logging


# ==================================================================
# 5. YOUR FIRST LOG MESSAGE
# ==================================================================

"""
The simplest way to use logging is:

    logging.basicConfig(level=logging.INFO)

Then:

    logging.info("Application started")
"""

logging.basicConfig(level=logging.INFO)

logging.info("Application started")


"""
Expected output will look similar to:

    INFO:root:Application started

The exact output can vary depending on the environment.

Notice:

    INFO

This is the logging level.

    root

This is the default logger name.

    Application started

This is our message.
"""


# ==================================================================
# 6. LOGGING LEVELS
# ==================================================================

"""
Python logging has different levels.

The main levels students should know are:

    DEBUG
    INFO
    WARNING
    ERROR
    CRITICAL


DEBUG
-----

Detailed information useful when diagnosing a problem.

Example:

    DEBUG: User ID is 25


INFO
----

Normal information about the application.

Example:

    INFO: User logged in


WARNING
-------

Something unexpected happened, but the application can continue.

Example:

    WARNING: Disk space is getting low


ERROR
-----

A problem occurred and a particular operation failed.

Example:

    ERROR: Could not open database


CRITICAL
--------

A very serious problem occurred.

Example:

    CRITICAL: Application cannot start


ORDER:

    DEBUG
       |
    INFO
       |
    WARNING
       |
    ERROR
       |
    CRITICAL

The severity increases as we move downward.
"""


# ==================================================================
# 7. DEMONSTRATING THE LOGGING LEVELS
# ==================================================================

"""
We can write messages using different methods.
"""

logging.debug("This is a debug message")
logging.info("This is an information message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")


"""
You may notice that DEBUG does not appear.

Why?

Because our logging level was configured as:

    INFO

This means logging will normally display:

    INFO
    WARNING
    ERROR
    CRITICAL

but not DEBUG.

This is an important concept.

If we change the level to DEBUG:

    logging.basicConfig(level=logging.DEBUG)

then DEBUG messages can be displayed.
"""


# ==================================================================
# 8. LOGGING LEVEL FILTERING
# ==================================================================

"""
The logging level acts like a filter.

If the level is INFO:

    DEBUG       -> hidden
    INFO        -> shown
    WARNING     -> shown
    ERROR       -> shown
    CRITICAL    -> shown


If the level is WARNING:

    DEBUG       -> hidden
    INFO        -> hidden
    WARNING     -> shown
    ERROR       -> shown
    CRITICAL    -> shown


This allows developers to control how much information
the application produces.
"""


# ==================================================================
# 9. A SIMPLE APPLICATION EXAMPLE
# ==================================================================

"""
Let's imagine a login function.
"""

def login(username):
    logging.info("Login attempt for user: %s", username)

    if username:
        logging.info("Login successful for user: %s", username)
        return True

    logging.warning("Login failed because username is empty")
    return False


login("Leonard")
login("")


"""
Notice this style:

    logging.info("User: %s", username)

The logging module inserts the value of username into %s.

This is preferred to unnecessarily building strings manually.
"""


# ==================================================================
# 10. LOGGING TO A FILE
# ==================================================================

"""
One of the biggest advantages of logging is that we can save
messages into a file.

Example:

    application.log

We can configure:

    filename="application.log"
"""

logging.basicConfig(
    filename="application.log",
    level=logging.INFO
)

logging.info("This message can be stored in the log file")


"""
After running the program, Python may create:

    application.log

The file can contain messages such as:

    INFO:root:This message can be stored in the log file


IMPORTANT:

basicConfig() should normally be configured once at the beginning
of an application.

In a classroom demonstration, if an earlier logging configuration
has already been executed in the same Python process, basicConfig()
may not change the configuration. In a fresh .py file, it will work
as expected.
"""


# ==================================================================
# 11. ADDING A TIMESTAMP AND OTHER INFORMATION
# ==================================================================

"""
A professional log is more useful when it tells us:

    - When did it happen?
    - What level was it?
    - What was the message?

We can use format=.
"""

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")


"""
Example:

    2026-10-08 16:00:00,123 - INFO - Application started

The exact date and time will be different.

The important parts are:

    %(asctime)s
        Date and time

    %(levelname)s
        Logging level

    %(message)s
        Our message
"""


# ==================================================================
# 12. COMMON LOGGING FORMAT FIELDS
# ==================================================================

"""
Useful format fields include:

    %(asctime)s
        Date and time

    %(levelname)s
        DEBUG, INFO, WARNING, ERROR, CRITICAL

    %(message)s
        The log message

    %(name)s
        Logger name

    %(filename)s
        Python file name

    %(lineno)d
        Line number

Example:

    format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s"
"""


# ==================================================================
# 13. LOGGING EXCEPTIONS
# ==================================================================

"""
Logging becomes especially useful when an error occurs.

Example:
"""

try:
    number = 10 / 0

except ZeroDivisionError:
    logging.error("A division by zero occurred")


"""
This records the error message.

But we can do even better using:

    logging.exception()
"""


# ==================================================================
# 14. logging.exception()
# ==================================================================

"""
logging.exception() is normally used inside an except block.

It records the error and traceback.

Example:
"""

try:
    number = 10 / 0

except ZeroDivisionError:
    logging.exception("An error occurred while dividing numbers")


"""
The log will contain information about the exception and traceback.

This is extremely useful when debugging real applications.
"""


# ==================================================================
# 15. TRY / EXCEPT / FINALLY
# ==================================================================

"""
Debugging and logging often work together with exception handling.

The basic structure is:

    try:
        Code that may fail

    except:
        Handle the error

    finally:
        Code that should run regardless


Example:
"""

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    logging.error("The user did not enter a valid number")

except ZeroDivisionError:
    logging.error("The user entered zero")

finally:
    logging.info("Number processing finished")


# ==================================================================
# 16. DEBUGGING WITH print()
# ==================================================================

"""
Before teaching professional logging, students should understand
the common beginner debugging technique.

Example:

    def calculate_total(price, quantity):
        total = price * quantity
        return total


If the result is wrong, we can temporarily use print():

    print(price)
    print(quantity)
    print(total)


This helps us see the values inside the program.
"""

def calculate_total(price, quantity):
    print("DEBUG price:", price)
    print("DEBUG quantity:", quantity)

    total = price * quantity

    print("DEBUG total:", total)

    return total


result = calculate_total(100, 3)

print("Result:", result)


"""
This works.

However, logging gives us a more organized and controllable
way of recording this information.
"""


# ==================================================================
# 17. DEBUGGING WITH logging.debug()
# ==================================================================

"""
Instead of:

    print("DEBUG price:", price)

we can use:

    logging.debug("price = %s", price)
"""

def calculate_total_with_logging(price, quantity):
    logging.debug("price = %s", price)
    logging.debug("quantity = %s", quantity)

    total = price * quantity

    logging.debug("total = %s", total)

    return total


calculate_total_with_logging(100, 3)


"""
DEBUG messages are particularly useful during development.

They can be hidden when the application is running normally.
"""


# ==================================================================
# 18. WHAT IS A TRACEBACK?
# ==================================================================

"""
When Python encounters an unhandled error, it displays a traceback.

Example:

    Traceback (most recent call last):
      File "app.py", line 10, in <module>
        result = 10 / 0
    ZeroDivisionError: division by zero


Students should learn to read this from the bottom upward.

The final line usually tells us the type of error:

    ZeroDivisionError

Then:

    division by zero

explains the problem.

The traceback also tells us where the error happened.
"""


# ==================================================================
# 19. COMMON PYTHON ERRORS
# ==================================================================

"""
1. SyntaxError

The Python syntax is incorrect.

Example:

    if True
        print("Hello")


2. NameError

A variable or name does not exist.

Example:

    print(username)

when username was never defined.


3. TypeError

An operation was performed on an inappropriate type.

Example:

    "10" + 5


4. ValueError

The type may be correct, but the value is invalid.

Example:

    int("hello")


5. IndexError

Trying to access a list position that does not exist.

Example:

    numbers = [1, 2, 3]
    print(numbers[10])


6. KeyError

Trying to access a dictionary key that does not exist.

Example:

    user = {"name": "Leonard"}
    print(user["email"])


7. ZeroDivisionError

Trying to divide by zero.

Example:

    10 / 0
"""


# ==================================================================
# 20. A PRACTICAL DEBUGGING EXAMPLE
# ==================================================================

"""
Suppose we have this program.
"""

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average


numbers = [10, 20, 30]

print(calculate_average(numbers))


"""
Now imagine the student changes:

    numbers = []

The program will fail because:

    len(numbers)

is zero.

Then:

    total / 0

causes ZeroDivisionError.

This is where debugging begins.
"""


# ==================================================================
# 21. DEBUGGING STEP BY STEP
# ==================================================================

"""
STEP 1
-----

Run the program.

STEP 2
-----

Read the error.

STEP 3
-----

Find the line mentioned in the traceback.

STEP 4
-----

Understand the value causing the problem.

STEP 5
-----

Add temporary debugging information.

For example:
"""

def calculate_average_debug(numbers):
    print("Numbers:", numbers)

    total = sum(numbers)
    print("Total:", total)

    count = len(numbers)
    print("Count:", count)

    average = total / count

    return average


"""
This allows us to see:

    Numbers
    Total
    Count

before the error happens.

That is the basic debugging mindset.
"""


# ==================================================================
# 22. USING breakpoint()
# ==================================================================

"""
Python has a built-in debugger.

The easiest modern way to start debugging is:

    breakpoint()

When Python reaches breakpoint(), execution pauses.

We can inspect variables and step through the program.
"""

def calculate_discount(price, discount):
    total = price - discount

    breakpoint()

    return total


calculate_discount(100, 20)


"""
When you run this file from the terminal, Python can enter the
interactive debugger.

You may see a prompt similar to:

    (Pdb)

Useful commands include:

    p variable
        Print a variable.

    n
        Execute the next line.

    c
        Continue execution.

    q
        Quit the debugger.

Example:

    p price
    p discount
    p total


IMPORTANT:

Do not leave breakpoint() statements accidentally inside production
code because they pause execution.
"""


# ==================================================================
# 23. USING pdb DIRECTLY
# ==================================================================

"""
Python also provides the pdb module.

Example:

    import pdb
    pdb.set_trace()

This performs a similar job to breakpoint().
"""

import pdb


def example_debugger():
    name = "Leonard"
    age = 30

    pdb.set_trace()

    print(name)
    print(age)


"""
To demonstrate this:

    example_debugger()

When execution reaches pdb.set_trace(), the debugger starts.

For modern Python code, breakpoint() is usually simpler.
"""


# ==================================================================
# 24. DEBUGGING IN VS CODE
# ==================================================================

"""
VS Code provides a graphical debugger.

This is very useful for students.

BASIC STEPS:

1. Open a Python file.

2. Click beside a line number.

3. A red dot appears.

That red dot is called a:

    BREAKPOINT

4. Start the program using the debugger.

5. Execution stops at the breakpoint.

Students can then inspect:

    Variables
    Call Stack
    Expressions
    Program flow


IMPORTANT DEBUGGING BUTTONS:

Continue
    Continue running the program.

Step Over
    Execute the current line and move to the next line.

Step Into
    Enter a function.

Step Out
    Leave the current function.

Restart
    Start the debugging session again.

Stop
    End debugging.
"""


# ==================================================================
# 25. BREAKPOINT DEMONSTRATION FOR VS CODE
# ==================================================================

"""
Use this simple program for your classroom demonstration.

Tell students to place a breakpoint on the line:

    total = price * quantity
"""

def calculate_price(price, quantity):
    tax = 0.075

    total = price * quantity

    final_price = total + (total * tax)

    return final_price


price = 100
quantity = 3

result = calculate_price(price, quantity)

print("Final price:", result)


"""
During the VS Code demonstration:

1. Put a breakpoint on:

       total = price * quantity

2. Start debugging.

3. When execution stops, inspect:

       price
       quantity
       tax

4. Step over the line.

5. Inspect:

       total

6. Continue.

This shows students how a debugger allows us to inspect the
program while it is running.
"""


# ==================================================================
# 26. LOGGING AND DEBUGGING WORK TOGETHER
# ==================================================================

"""
Logging and debugging are related but they are not exactly the same.

DEBUGGING:

    Finding and fixing problems.

LOGGING:

    Recording what happens in the program.

Think of it this way:

    Debugger
        |
        v
    Helps you investigate the program while it is running.

    Logging
        |
        v
    Records information that you can inspect later.
"""


# ==================================================================
# 27. PRACTICAL APPLICATION WITH LOGGING
# ==================================================================

"""
Let's build a small student registration example.

The application will:

    1. Receive a student name.
    2. Validate the name.
    3. Log the operation.
    4. Return success or failure.
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def register_student(name):
    logging.info("Registration attempt started")

    if not name:
        logging.warning("Registration failed: empty name")
        return False

    logging.info("Student '%s' registered successfully", name)

    return True


register_student("Leonard")
register_student("")


# ==================================================================
# 28. PRACTICAL APPLICATION WITH ERROR LOGGING
# ==================================================================

"""
Now let's create a small calculator.

We will deliberately handle errors.
"""

def divide_numbers(a, b):
    logging.info("Division requested: %s / %s", a, b)

    try:
        result = a / b

        logging.info("Division successful: result = %s", result)

        return result

    except ZeroDivisionError:
        logging.exception("Division failed because denominator was zero")
        return None


print(divide_numbers(10, 2))
print(divide_numbers(10, 0))


# ==================================================================
# 29. LOGGING BEST PRACTICES
# ==================================================================

"""
GOOD PRACTICES:

1. Use INFO for normal application events.

2. Use DEBUG for detailed diagnostic information.

3. Use WARNING for unusual situations that do not stop the
   application.

4. Use ERROR when an operation fails.

5. Use CRITICAL for serious application problems.

6. Log useful information.

7. Do not log passwords.

8. Do not log secret API keys.

9. Do not log sensitive user information unnecessarily.

10. Use logging.exception() inside exception handlers when a
    traceback is useful.

11. Avoid replacing every print() statement with logging without
    thinking about the purpose of the message.

12. Keep log messages clear and meaningful.
"""


# ==================================================================
# 30. A PROFESSIONAL-STYLE LOGGING SETUP
# ==================================================================

"""
For larger applications, it is common to create a named logger
instead of using the root logger.

Example:
"""

logger = logging.getLogger(__name__)

logger.info("Named logger example")
logger.warning("This is a warning")
logger.error("This is an error")


"""
__name__ gives the current module's name.

This becomes especially useful when a project contains multiple
Python files.
"""


# ==================================================================
# 31. HANDLERS - BASIC IDEA
# ==================================================================

"""
A logging handler controls where log messages go.

Examples:

    StreamHandler
        Sends logs to the console.

    FileHandler
        Sends logs to a file.

A program can have more than one handler.

For example:

    Console
       +
    File

The same event can therefore be displayed in the terminal and
saved in a log file.
"""


# ==================================================================
# 32. PRACTICAL FILE + CONSOLE LOGGING
# ==================================================================

"""
This is a useful example for advanced students.

We create a logger and two handlers:

    Console handler
    File handler
"""

logger = logging.getLogger("school_app")
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("school_app.log")

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("Debug information")
logger.info("Application started")
logger.warning("This is a warning")
logger.error("This is an error")


"""
Now the same logger can send messages to:

    Terminal
    school_app.log
"""


# ==================================================================
# 33. IMPORTANT: AVOID DUPLICATE HANDLERS
# ==================================================================

"""
When configuring custom loggers, repeatedly adding handlers can cause
the same message to appear multiple times.

In a real application, logging configuration should normally happen
once.

For classroom demonstrations, run the handler example as a fresh
Python process/file to avoid confusion caused by previous
configuration in the same process.
"""


# ==================================================================
# 34. COMPLETE MINI PROJECT
# ==================================================================

"""
MINI PROJECT:
STUDENT SCORE PROCESSOR

The program will:

    1. Receive student scores.
    2. Calculate the average.
    3. Log important events.
    4. Handle invalid data.
    5. Record errors.

This combines:

    Functions
    Exception handling
    Logging
    Debugging
"""


def calculate_average_score(scores):
    logger.info("Calculating average for %d scores", len(scores))

    try:
        total = sum(scores)
        average = total / len(scores)

        logger.info("Average calculated successfully: %.2f", average)

        return average

    except ZeroDivisionError:
        logger.exception("Cannot calculate average of an empty list")
        return None


scores = [70, 80, 90, 60]

average = calculate_average_score(scores)

print("Average:", average)


# ==================================================================
# 35. MINI PROJECT EXERCISE
# ==================================================================

"""
STUDENT TASK:

Build a simple Student Result Logger.

Requirements:

1. Create a function:

       calculate_average(scores)

2. Calculate the average score.

3. Log when calculation starts.

4. Log the number of scores.

5. Log the final average.

6. Handle an empty list.

7. Use logging.exception() when an error occurs.

8. Save logs to:

       student_results.log


Example:

    scores = [70, 80, 90]

Expected:

    Average: 80.0
"""


# ==================================================================
# 36. DEBUGGING CHECKLIST
# ==================================================================

"""
When a program fails, teach students to follow this checklist:

STEP 1
------

Read the error message.


STEP 2
------

Read the last line of the traceback.


STEP 3
------

Identify the error type.


STEP 4
------

Look at the file and line number.


STEP 5
------

Inspect the variables involved.


STEP 6
------

Use print() or logging.debug() if necessary.


STEP 7
------

Use a breakpoint if the problem is difficult.


STEP 8
------

Fix the problem.


STEP 9
------

Run the program again.


STEP 10
-------

Test other possible inputs.


IMPORTANT:

Do not immediately change random lines of code.

Understand the error first.
"""


# ==================================================================
# 37. DEBUGGING EXERCISE
# ==================================================================

"""
Give students this code and ask them to find the problem:

    numbers = [10, 20, 30]

    total = sum(numbers)

    average = total / len(number)

    print(average)


QUESTION:

What is wrong?

The list is called:

    numbers

but the code uses:

    number

This causes:

    NameError


STUDENT TASK:

1. Identify the error.
2. Explain why it happened.
3. Fix it.
4. Run the program.
"""


# ==================================================================
# 38. LOGGING EXERCISE
# ==================================================================

"""
Create a Python program that records:

    Application started
    User logged in
    User requested profile
    Profile loaded
    Application ended

Use:

    INFO

Save the logs to:

    application.log
"""


# ==================================================================
# 39. ERROR LOGGING EXERCISE
# ==================================================================

"""
Create a program that asks the user for two numbers.

Divide the first number by the second.

Requirements:

    - Use try/except.
    - Handle invalid input.
    - Handle division by zero.
    - Log successful calculations.
    - Log errors.
    - Use logging.exception() for the exception.

Example:

    Enter first number: 20
    Enter second number: 5

    Result: 4.0
"""


# ==================================================================
# 40. SUMMARY
# ==================================================================

"""
========================================================
LOGGING AND DEBUGGING SUMMARY
========================================================

DEBUGGING
---------

Debugging is the process of finding and fixing problems
in a program.


LOGGING
-------

Logging records information about what happens inside
a program.


PRINT VS LOGGING
----------------

print():

    Useful for simple temporary debugging.

logging:

    Better for structured application messages and
    long-running applications.


LOGGING LEVELS
--------------

DEBUG
    Detailed diagnostic information.

INFO
    Normal application information.

WARNING
    Something unexpected happened, but the application
    can continue.

ERROR
    An operation failed.

CRITICAL
    A serious application problem.


IMPORTANT LOGGING METHODS
--------------------------

logging.debug()

logging.info()

logging.warning()

logging.error()

logging.critical()

logging.exception()


EXCEPTION HANDLING
------------------

try
    Code that may fail

except
    Handle the error

finally
    Code that should run regardless


TRACEBACK
---------

A traceback tells us:

    - What error happened.
    - Where it happened.
    - The sequence of function calls that led to it.


DEBUGGER
--------

Python provides:

    breakpoint()

and:

    pdb

VS Code also provides a graphical debugger.


BREAKPOINT
----------

A breakpoint pauses program execution so that we can
inspect variables and program flow.


LOGGING VS DEBUGGING
--------------------

DEBUGGING:

    Find and fix problems.

LOGGING:

    Record what happens.


THE COMPLETE WORKFLOW
---------------------

Program runs
      |
      v
Something goes wrong
      |
      v
Read traceback
      |
      v
Identify error
      |
      v
Inspect variables
      |
      +------> logging.debug()
      |
      +------> print()
      |
      +------> breakpoint()
      |
      v
Find cause
      |
      v
Fix problem
      |
      v
Run tests again


========================================================
KEY TAKEAWAYS
========================================================

1. Learn to read errors instead of being afraid of them.

2. The traceback is a debugging tool.

3. Logging helps us understand what an application is doing.

4. DEBUG is for detailed diagnostic information.

5. INFO is for normal application events.

6. WARNING indicates something unusual.

7. ERROR indicates a failed operation.

8. CRITICAL indicates a serious problem.

9. logging.exception() is useful inside except blocks.

10. breakpoint() allows us to pause and inspect a program.

11. VS Code provides a graphical debugging environment.

12. Good developers do not just fix errors; they understand
    why the errors happened.
"""


# ==================================================================
# 41. OBJECTIVE QUESTIONS FOR STUDENTS
# ==================================================================

"""
========================================================
OBJECTIVE QUESTIONS
LOGGING AND DEBUGGING
========================================================

Students should choose ONE correct answer for each question.

--------------------------------------------------------
QUESTION 1
--------------------------------------------------------

What is debugging?

A. Writing HTML
B. Finding and fixing problems in a program
C. Installing Python
D. Creating a database

--------------------------------------------------------
QUESTION 2
--------------------------------------------------------

Which Python module is used for logging?

A. debug
B. log
C. logging
D. system

--------------------------------------------------------
QUESTION 3
--------------------------------------------------------

Which logging level is used for detailed diagnostic information?

A. DEBUG
B. INFO
C. ERROR
D. CRITICAL

--------------------------------------------------------
QUESTION 4
--------------------------------------------------------

Which logging level is normally used for normal application events?

A. DEBUG
B. INFO
C. ERROR
D. CRITICAL

--------------------------------------------------------
QUESTION 5
--------------------------------------------------------

Which logging level indicates an unexpected situation that may
not stop the application?

A. INFO
B. WARNING
C. DEBUG
D. CRITICAL

--------------------------------------------------------
QUESTION 6
--------------------------------------------------------

Which logging level indicates that an operation failed?

A. DEBUG
B. INFO
C. ERROR
D. WARNING

--------------------------------------------------------
QUESTION 7
--------------------------------------------------------

Which logging level represents a very serious problem?

A. DEBUG
B. INFO
C. WARNING
D. CRITICAL

--------------------------------------------------------
QUESTION 8
--------------------------------------------------------

Which method records an INFO message?

A. logging.message()
B. logging.info()
C. logging.record()
D. logging.write()

--------------------------------------------------------
QUESTION 9
--------------------------------------------------------

Which method is especially useful for recording an exception
and its traceback?

A. logging.info()
B. logging.debug()
C. logging.exception()
D. logging.warning()

--------------------------------------------------------
QUESTION 10
--------------------------------------------------------

What does a traceback help a developer identify?

A. Only the computer name
B. The error and where it happened
C. The internet speed
D. The operating system only

--------------------------------------------------------
QUESTION 11
--------------------------------------------------------

Which keyword is used to handle an exception?

A. catch
B. error
C. except
D. handle

--------------------------------------------------------
QUESTION 12
--------------------------------------------------------

Which function can pause Python execution and enter the debugger?

A. stop()
B. breakpoint()
C. pause()
D. debug()

--------------------------------------------------------
QUESTION 13
--------------------------------------------------------

What is a breakpoint?

A. A point where a program is permanently deleted
B. A point where program execution can be paused for inspection
C. A Python package
D. A database table

--------------------------------------------------------
QUESTION 14
--------------------------------------------------------

Which of these is a good use of DEBUG logging?

A. Recording detailed variable information while diagnosing a problem
B. Storing passwords
C. Deleting files
D. Installing Python

--------------------------------------------------------
QUESTION 15
--------------------------------------------------------

Which statement is TRUE?

A. Logging and debugging mean exactly the same thing.
B. Logging records application events, while debugging helps find
   and fix problems.
C. Debugging is only used for web applications.
D. Logging can only be used with Django.

--------------------------------------------------------
QUESTION 16
--------------------------------------------------------

What does this code do?

    logging.info("User logged in")

A. Creates a user
B. Deletes a user
C. Records an INFO log message
D. Starts the debugger

--------------------------------------------------------
QUESTION 17
--------------------------------------------------------

What does this code do?

    logging.basicConfig(level=logging.INFO)

A. Installs logging
B. Configures basic logging
C. Deletes all logs
D. Starts Django

--------------------------------------------------------
QUESTION 18
--------------------------------------------------------

Which of these is normally NOT recommended?

A. Logging useful application events
B. Logging exceptions
C. Logging passwords and secret API keys
D. Using appropriate logging levels

--------------------------------------------------------
QUESTION 19
--------------------------------------------------------

Which VS Code feature allows a developer to pause execution
and inspect variables?

A. Breakpoints
B. Extensions only
C. Terminal history
D. File Explorer

--------------------------------------------------------
QUESTION 20
--------------------------------------------------------

What should a developer generally do FIRST when an unexpected
error occurs?

A. Delete the project
B. Read and understand the error message
C. Reinstall Python immediately
D. Change random lines of code


========================================================
ANSWER KEY
========================================================

1.  B
2.  C
3.  A
4.  B
5.  B
6.  C
7.  D
8.  B
9.  C
10. B
11. C
12. B
13. B
14. A
15. B
16. C
17. B
18. C
19. A
20. B


========================================================
END OF LOGGING AND DEBUGGING
========================================================
"""
