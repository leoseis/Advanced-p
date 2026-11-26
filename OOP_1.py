
"""
===========================================================
ADVANCED PYTHON
TOPIC: ADVANCED OBJECT-ORIENTED PROGRAMMING (OOP)
===========================================================

This file is designed as a TEACHING FILE.

You can:
    1. Copy this entire file into VS Code.
    2. Save it as: advanced_oop.py
    3. Run it with:
           python advanced_oop.py

All explanations are written as comments so that Python
will not try to execute them.

The examples below are kept simple so that beginners can
understand what is happening.

===========================================================
WHAT WE WILL LEARN
===========================================================

1. What is Object-Oriented Programming?
2. Classes and Objects
3. Inheritance
4. Encapsulation
5. Polymorphism
6. Abstraction
7. Class Methods
8. Static Methods
9. Properties
10. Dunder (Magic) Methods
11. Composition

===========================================================
"""


# ==========================================================
# 1. WHAT IS OBJECT-ORIENTED PROGRAMMING?
# ==========================================================

# OOP means Object-Oriented Programming.
#
# It is a way of organizing our code around OBJECTS.
#
# An object can represent something from the real world.
#
# Examples:
#
#     Student
#     Teacher
#     Car
#     Bank Account
#     Product
#     Employee
#
# An object normally has:
#
#     DATA  -> attributes
#     BEHAVIOR -> methods
#
# For example:
#
# A Student can have:
#
#     name
#     age
#     course
#
# And a Student can perform actions such as:
#
#     study()
#     introduce()
#
# A CLASS is like a blueprint.
#
# An OBJECT is an actual thing created from that blueprint.


# ==========================================================
# 2. CLASSES AND OBJECTS
# ==========================================================

class Student:
    """
    This is a class.

    Think of the class as a blueprint for creating
    Student objects.
    """

    def __init__(self, name, age):
        # __init__ runs automatically when we create
        # an object from the class.

        self.name = name
        self.age = age

    def introduce(self):
        # This is a method.
        print(f"My name is {self.name} and I am {self.age} years old.")


# Create objects from the Student class.

student1 = Student("John", 20)
student2 = Student("Mary", 22)

student1.introduce()
student2.introduce()


# ==========================================================
# 3. INHERITANCE
# ==========================================================

# INHERITANCE allows one class to reuse the properties
# and methods of another class.
#
# We normally have:
#
#     Parent class
#          |
#          v
#     Child class
#
# Example:
#
# Person
#   |
#   +---- Student
#   |
#   +---- Teacher


class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")


class Teacher(Person):
    # Teacher inherits from Person.

    def teach(self):
        print(f"{self.name} is teaching Python.")


teacher1 = Teacher("Mr. David")

# introduce() belongs to Person,
# but Teacher can use it because it inherited it.

teacher1.introduce()

# teach() belongs specifically to Teacher.

teacher1.teach()


# ==========================================================
# 4. ENCAPSULATION
# ==========================================================

# Encapsulation means keeping data and the methods that
# operate on that data together inside a class.
#
# It also allows us to control how certain data is accessed.
#
# In Python, we commonly use:
#
#     _variable
#
# or
#
#     __variable
#
# to indicate that something should not be accessed directly.
#
# NOTE:
# Python does not enforce private variables in exactly the
# same way as some other programming languages.
#
# The double underscore triggers name mangling.


class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")

    def get_balance(self):
        return self.__balance


account = BankAccount("Leonard", 100000)

account.deposit(50000)

print("Balance:", account.get_balance())

# The following would normally NOT be used:
#
# print(account.__balance)
#
# It will produce an AttributeError because __balance
# is name-mangled by Python.


# ==========================================================
# 5. POLYMORPHISM
# ==========================================================

# POLYMORPHISM means "many forms".
#
# Different objects can have a method with the same name
# but behave differently.


class Dog:

    def speak(self):
        print("Dog says: Woof!")


class Cat:

    def speak(self):
        print("Cat says: Meow!")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()


# We can also use the same function with different objects.


def make_animal_speak(animal):
    animal.speak()


make_animal_speak(dog)
make_animal_speak(cat)


# The function does not need to know whether it received
# a Dog or a Cat.
#
# It simply expects the object to have a speak() method.


# ==========================================================
# 6. ABSTRACTION
# ==========================================================

# ABSTRACTION means hiding unnecessary implementation
# details and exposing only what the user needs.
#
# Python provides the abc module for creating abstract
# classes.


from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using a debit card.")


class CashPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using cash.")


card = CardPayment()
cash = CashPayment()

card.pay(5000)
cash.pay(3000)


# Notice that Payment defines WHAT a payment class must do.
#
# The child classes decide HOW the payment is performed.
#
# This is the basic idea behind abstraction.


# ==========================================================
# 7. CLASS METHODS
# ==========================================================

# A normal method works with an object.
#
# A CLASS METHOD works with the class itself.
#
# We use the @classmethod decorator.
#
# The first parameter is normally called "cls".
#
#     self -> object
#     cls  -> class


class Employee:

    company = "Tech Company"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


employee1 = Employee("John")

print(Employee.company)

Employee.change_company("New Technology Ltd")

print(Employee.company)


# ==========================================================
# 8. STATIC METHODS
# ==========================================================

# A STATIC METHOD does not need:
#
#     self
#
# or:
#
#     cls
#
# It is simply a function that logically belongs inside
# the class.


class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print(Calculator.add(10, 5))
print(Calculator.multiply(10, 5))


# ==========================================================
# 9. PROPERTIES
# ==========================================================

# A property allows us to access a method like an attribute.
#
# Instead of:
#
#     student.get_name()
#
# we can use:
#
#     student.name
#
# The @property decorator is commonly used for this.


class User:

    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username


user = User("leonard")

print(user.username)


# ==========================================================
# 10. PROPERTY WITH A SETTER
# ==========================================================

# A property can also control how a value is changed.
#
# We can use:
#
#     @property
#
# together with:
#
#     @property_name.setter


class Product:

    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):

        if value < 0:
            print("Price cannot be negative.")
            return

        self._price = value


product = Product(5000)

print(product.price)

product.price = 7500

print(product.price)

product.price = -100


# ==========================================================
# 11. DUNDER / MAGIC METHODS
# ==========================================================

# Dunder means:
#
#     Double UNDERscore
#
# Example:
#
#     __init__
#     __str__
#     __len__
#     __eq__
#
# Python automatically calls these methods in certain
# situations.


class Book:

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return self.title

    def __len__(self):
        return self.pages


book = Book("Python for Beginners", 250)

# __str__ is called when we use print().

print(book)

# __len__ is called when we use len().

print(len(book))


# ==========================================================
# 12. __EQ__ METHOD
# ==========================================================

# __eq__ controls how two objects are compared using ==.


class StudentRecord:

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __eq__(self, other):

        return self.student_id == other.student_id


student_a = StudentRecord("John", 101)
student_b = StudentRecord("Mary", 101)

print(student_a == student_b)


# The result is True because both students have the same
# student_id.


# ==========================================================
# 13. COMPOSITION
# ==========================================================

# Composition means creating a relationship where one class
# contains an object of another class.
#
# Think:
#
#     A Car HAS an Engine.
#
# rather than:
#
#     A Car IS an Engine.
#
# Composition is therefore different from inheritance.


class Engine:

    def start(self):
        print("Engine started.")


class Car:

    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car is moving.")


car = Car()

car.start_car()


# ==========================================================
# 14. INHERITANCE VS COMPOSITION
# ==========================================================

# INHERITANCE:
#
#     "IS-A" relationship
#
# Example:
#
#     Dog IS an Animal.
#
#
# COMPOSITION:
#
#     "HAS-A" relationship
#
# Example:
#
#     Car HAS an Engine.
#
#
# Simple rule:
#
#     IS-A  -> inheritance
#     HAS-A -> composition


# ==========================================================
# 15. PRACTICAL EXAMPLE
# ==========================================================

# Let's combine several OOP concepts into a small example.
#
# Imagine we are creating part of a school management
# system.


class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")


class Student(Person):

    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduce(self):
        print(
            f"My name is {self.name} "
            f"and I study {self.course}."
        )


class Teacher(Person):

    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        print(
            f"My name is {self.name} "
            f"and I teach {self.subject}."
        )


student = Student("John", "Python")

teacher = Teacher("Mrs. Jane", "Django")

student.introduce()
teacher.introduce()


# Notice that both Student and Teacher have an
# introduce() method.
#
# However, each class gives the method its own behavior.
#
# This is POLYMORPHISM.


# ==========================================================
# 16. QUICK SUMMARY FOR STUDENTS
# ==========================================================

# CLASS
# A blueprint used to create objects.
#
# OBJECT
# An actual instance created from a class.
#
# INHERITANCE
# Allows a child class to reuse functionality from a
# parent class.
#
# ENCAPSULATION
# Keeps data and behavior together and controls access
# to internal data.
#
# POLYMORPHISM
# Allows different objects to respond to the same method
# in different ways.
#
# ABSTRACTION
# Hides implementation details and exposes the important
# interface.
#
# CLASS METHOD
# A method that works with the class.
#
# STATIC METHOD
# A method inside a class that does not require self or cls.
#
# PROPERTY
# Allows a method to be accessed like an attribute.
#
# DUNDER METHOD
# Special methods surrounded by double underscores.
#
# COMPOSITION
# Building classes by including objects of other classes.


# ==========================================================
# 17. STUDENT PRACTICE
# ==========================================================

# EXERCISE 1
#
# Create a class called Student with:
#
#     name
#     age
#     course
#
# Create two student objects and print their information.


# EXERCISE 2
#
# Create a parent class called Animal.
#
# Create two child classes:
#
#     Dog
#     Cat
#
# Give both classes a speak() method.
#
# Make Dog print:
#
#     Woof
#
# Make Cat print:
#
#     Meow


# EXERCISE 3
#
# Create a BankAccount class.
#
# The class should have:
#
#     owner
#     balance
#
# Create methods:
#
#     deposit()
#     withdraw()
#     get_balance()
#
# Prevent the user from withdrawing more money than
# the available balance.


# EXERCISE 4
#
# Create a Product class with:
#
#     name
#     price
#
# Use @property to control access to price.
#
# Do not allow a negative price.


# ==========================================================
# END OF LESSON
# ==========================================================

# IMPORTANT TEACHING NOTE:
#
# Do not teach everything above at once.
#
# During class, teach one section at a time.
#
# For example:
#
#     Run Section 2
#     Explain it
#     Modify the code
#     Let students experiment
#     Then move to Section 3
#
# The file is deliberately written so that the explanations
# remain inside the Python file as comments.
#
# This makes the file both:
#
#     1. A teaching note
#     2. A runnable Python practical
#
# ==========================================================

