"""
ADVANCED PYTHON: PACKAGING AND PROJECT STRUCTURE
Complete beginner-friendly, step-by-step classroom guide for VS Code.

This is a teaching-notes .py file. Explanations are docstrings/comments.
Code examples are provided as strings where they belong in separate files.
Terminal commands must be run in the VS Code terminal, not as Python code.

LEARNING OBJECTIVES
1. Understand modules, packages, and project structure.
2. Organise code into multiple reusable files.
3. Use __init__.py and imports.
4. Create a virtual environment and install a local package.
5. Understand pyproject.toml and requirements.txt.
6. Write tests, build a package, and understand distribution formats.
"""

# ============================================================
# 1. UNDERSTAND THE BASIC TERMS
# ============================================================
"""
MODULE: Usually one Python file, such as greetings.py.
PACKAGE: A folder grouping related Python modules, commonly with __init__.py.
PROJECT: The complete collection of source code, tests, documentation, and
configuration files for an application or library.

Analogy: a module is one book, a package is a shelf of related books, and a
project is the whole library organised for a purpose.

Why structure a project?
- Easier to find code.
- Easier to test and maintain.
- Functions can be reused by other modules.
- Easier for teammates to understand and install.
"""

# ============================================================
# 2. CREATE THE PROJECT FROM SCRATCH
# ============================================================
"""
In VS Code, create and open a folder named student_tools_project.
Open Terminal > New Terminal. Make sure the terminal is inside the folder.

Run these commands one at a time:

    pwd
    python3 --version
    python3 -m venv .venv
    source .venv/bin/activate

On Windows PowerShell, activation is commonly:
    .venv\\Scripts\\Activate.ps1

When activated, the terminal prompt usually shows (.venv). This environment
keeps packages for this project separate from other projects.

Create the folders using VS Code Explorer or run:
    mkdir -p src/student_tools tests

Create this structure:

student_tools_project/
    pyproject.toml
    README.md
    requirements.txt
    .gitignore
    src/
        stsrcsrcudent_tools/
            __init__.py
            greetings.py
            maths.py
            cli.py
    tests/
        test_greetings.py
        test_maths.py

src/ contains the package source code. tests/ contains automated tests.
"""

# ============================================================
# 3. CREATE greetings.py
# ============================================================
GREETINGS_PY = r'''def greet(name: str) -> str:
    """Return a friendly greeting."""
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("Name cannot be empty.")
    return f"Hello, {cleaned_name}!"
'''
"""
Save the code above in src/student_tools/greetings.py.

Explanation:
- name: str is a type hint: name is expected to be a string.
- -> str indicates that the function returns a string.
- strip() removes spaces at the beginning and end.
- ValueError is raised if the name is empty.
- Returning a value makes the function easy to reuse and test.
"""

# ============================================================
# 4. CREATE maths.py
# ============================================================
MATHS_PY = r'''def add(first: float, second: float) -> float:
    """Return the sum of two numbers."""
    return first + second


def subtract(first: float, second: float) -> float:
    """Return the first number minus the second."""
    return first - second


def multiply(first: float, second: float) -> float:
    """Return the product of two numbers."""
    return first * second
'''
"""
Save this as src/student_tools/maths.py.
We separated arithmetic functions from greeting functions because each module
should have a clear responsibility.
"""

# ============================================================
# 5. CREATE __init__.py create it

# ============================================================
INIT_PY = r'''from .greetings import greet
from .maths import add, subtract, multiply

__all__ = ["greet", "add", "subtract", "multiply"]
'''
"""
Save as src/student_tools/__init__.py.

The dot in .greetings means import from this same package.
__init__.py can be empty, or it can expose selected functions as a convenient
public interface. Then users can write:
    from student_tools import greet, add
instead of importing each function from its individual module.
"""

# ============================================================
# 6. CREATE cli.py
# ============================================================
CLI_PY = r'''from . import greet, add


def main() -> None:
    """Run a small demonstration of the package."""
    print(greet("Python student"))
    print("10 + 5 =", add(10, 5))


if __name__ == "__main__":
    main()
'''
"""
Save as src/student_tools/cli.py.
The main() function is the command-line demonstration. The if __name__ block
runs it when this module is run directly as a module, not when imported.
Because it uses a package-relative import, we will run it with python -m.
"""

# ============================================================
# 7. CREATE pyproject.toml
# ============================================================
PYPROJECT_TOML = r'''[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "student-tools-class"
version = "0.1.0"
description = "A beginner-friendly example Python package"
readme = "README.md"
requires-python = ">=3.10"
dependencies = []

[project.scripts]
student-tools = "student_tools.cli:main"

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
'''
"""
Create pyproject.toml in the project root and paste the content above.

Explanation:
- [build-system] tells packaging tools what builds the package.
- [project] contains the package name, version, description and requirements.
- dependencies = [] means the package has no third-party runtime dependencies.
- [project.scripts] creates a terminal command after installation.
- package-dir and packages.find tell setuptools that source is under src/.

The distribution name student-tools-class and import name student_tools differ.
That is allowed: distribution names and Python import names need not match.
YAML and TOML are configuration formats, not Python code.
"""

# ============================================================
# 8. CREATE README.md AND .gitignore
# ============================================================
README_MD = r'''# Student Tools

A small Python package for learning project structure and packaging.

## Features
- Create a greeting.
- Add, subtract, and multiply numbers.

## Run
    python -m student_tools.cli

## Test
    python -m pip install pytest
    python -m pytest -v
'''

GITIGNORE = r'''.venv/
__pycache__/
*.py[cod]
.pytest_cache/
build/
dist/
*.egg-info/
.env
'''
"""
Create README.md and paste README_MD content into it. README explains what the
project does and how to use it.
Create .gitignore and paste GITIGNORE content into it. It tells Git to ignore
common local environments, cache files, generated build files, and .env files.
It does not remove files that Git already tracks.
"""

# ============================================================
# 9. INSTALL THE LOCAL PACKAGE IN EDITABLE MODE
# ============================================================
"""
Ensure .venv is active and the terminal is in the folder containing
pyproject.toml. Run:

    python -m pip install --upgrade pip
    python -m pip install -e .

The dot means “the current directory/project.” The -e option installs the
project in editable mode. Changes to Python source files are usually available
without reinstalling after every edit.

Now run:
    python -m student_tools.cli

Expected output:
    Hello, Python student!
    10 + 5 = 15

Try importing functions:
    python -c "from student_tools import greet, add; print(greet('Ada')); print(add(4, 6))"

Expected output:
    Hello, Ada!
    10

If imports fail, check that you activated .venv, ran pip install -e . from the
project root, and created src/student_tools/__init__.py.
"""

# ============================================================
# 10. requirements.txt: WHAT IS IT?
# ============================================================
REQUIREMENTS_TXT = r'''pytest'''
"""
Create requirements.txt with the text above.

Install packages listed in the file with:
    python -m pip install -r requirements.txt

requirements.txt is a convenient list of packages to install into an
environment. pyproject.toml describes the package, metadata, build setup, and
runtime dependencies. Here pytest is for development/testing, not needed by
someone who only uses the greeting and maths functions.
For a real library, declare runtime dependencies in pyproject.toml.
"""

# ============================================================
# 11. ADD AUTOMATED TESTS
# ============================================================
TEST_GREETINGS_PY = r'''import pytest
from student_tools import greet


def test_greet_name():
    assert greet("Ada") == "Hello, Ada!"


def test_greet_removes_outer_spaces():
    assert greet("  Ada  ") == "Hello, Ada!"


def test_greet_rejects_empty_name():
    with pytest.raises(ValueError):
        greet("   ")
'''

TEST_MATHS_PY = r'''from student_tools import add, subtract, multiply


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12
'''
"""
Save TEST_GREETINGS_PY as tests/test_greetings.py.
Save TEST_MATHS_PY as tests/test_maths.py.
Install and run tests:

    python -m pip install pytest
    python -m pytest -v

Expected: six tests pass.

assert checks whether a result matches the expected value. pytest discovers
files named test_*.py and functions whose names begin with test_.
"""

# ============================================================
# 12. BUILD A DISTRIBUTION PACKAGE
# ============================================================
"""
Packaging prepares your project for distribution to other people.
Two common distribution formats are:
- Wheel (.whl): a built distribution format commonly used for installation.
- Source distribution (.tar.gz): an archive of source files and metadata.

Install the build tool and build from the project root:

    python -m pip install build
    python -m build

After a successful build, a dist/ folder should contain a wheel and a source
archive. Exact filenames can vary. Do not edit generated files in dist/ by
hand; edit the source/metadata and rebuild.

Optional wheel installation demonstration:
1. Use a clean virtual environment if possible.
2. Build with python -m build.
3. Install the actual wheel filename inside dist/:
       python -m pip install dist/ACTUAL_WHEEL_FILENAME.whl
4. Test an import:
       python -c "from student_tools import greet; print(greet('Class'))"

Replace ACTUAL_WHEEL_FILENAME.whl with the real file name. For a clean test,
use a fresh environment so an existing editable install does not hide problems.
"""

# ============================================================
# 13. PYPI: OPTIONAL PUBLISHING CONCEPT
# ============================================================
"""
PyPI is a public index where Python packages can be published. Publishing is
not required to learn project structure or build a package.

Before publishing, run tests, inspect metadata, build the package, and choose
an appropriate unique distribution name. Use the recommended secure publishing
process; never put passwords or API tokens in source files or Git history.
TestPyPI can be used for a practice demonstration. Publishing to the real PyPI
should be optional and done only with the teacher's explicit decision.
"""

# ============================================================
# 14. COMMON ERRORS AND FIXES
# ============================================================
"""
ERROR: No module named student_tools
- Activate .venv.
- Run python -m pip install -e . from the project root.
- Check src/student_tools/__init__.py exists.

ERROR: pip install -e . fails
- Confirm pyproject.toml is in the current folder.
- Check TOML quotes and section names.
- Confirm setuptools can be installed.

ERROR: pytest command not found
    python -m pip install pytest
    python -m pytest -v

ERROR: relative import fails in cli.py
Run from the project root:
    python -m student_tools.cli
Do not run cli.py directly by file path when it uses relative imports.

ERROR: tests are not found
- Name files test_*.py.
- Name test functions test_*.
- Run pytest from the project root.

Why use src/? It helps avoid accidentally importing source directly from the
project root before the package is installed correctly.
"""

# ============================================================
# 15. FINAL PROJECT STRUCTURE
# ============================================================
"""
student_tools_project/
    .gitignore
    README.md
    pyproject.toml
    requirements.txt
    src/
        student_tools/
            __init__.py
            greetings.py
            maths.py
            cli.py
    tests/
        test_greetings.py
        test_maths.py
    .venv/       local virtual environment
    dist/        generated after building

.venv, dist, cache folders and generated metadata should normally be ignored
by Git. They may not exist until you perform the relevant steps.
"""

# ============================================================
# 16. CLASSROOM PRACTICAL ASSIGNMENT
# ============================================================
"""
PROJECT: STUDENT UTILITY PACKAGE
1. Create the project structure.
2. Implement greet(name), add(), subtract(), and multiply().
3. Expose functions through __init__.py.
4. Create cli.py with main().
5. Add pyproject.toml, README.md, requirements.txt, and .gitignore.
6. Create and activate .venv.
7. Install with python -m pip install -e .
8. Run python -m student_tools.cli.
9. Write tests and run python -m pytest -v.
10. Build with python -m build.
11. Explain what a wheel and source archive are.

Extension:
- Add divide() and raise ValueError or ZeroDivisionError for division by zero.
- Add tests for divide().
- Add a function that converts a name to uppercase.
- Update the README with examples.
- Change version 0.1.0 to 0.2.0 and rebuild.
"""

# ============================================================
# 17. LESSON SUMMARY
# ============================================================
"""
- Module = one Python file.
- Package = a group of related modules.
- Project = code plus tests, documentation, and configuration.
- .venv isolates packages for this project.
- __init__.py can expose a package's public functions.
- pyproject.toml stores modern packaging metadata/configuration.
- requirements.txt is a convenient install list.
- pip install -e . installs the local project in editable mode.
- pytest runs automated tests.
- python -m build creates distribution files.
- Publishing to PyPI is optional.
"""

# ============================================================
# 18. OBJECTIVE TEST — 20 QUESTIONS
# ============================================================
"""
Choose ONE answer (A, B, C, or D). Each question is worth 1 mark.

1. What is a Python module?
A. Usually a single Python file
B. A monitor
C. A password
D. A database

2. What is a Python package?
A. A folder grouping related modules
B. A README only
C. A terminal command
D. A browser

3. What does project structure describe?
A. How files and folders are organised
B. Wallpaper
C. Internet speed
D. Passwords

4. What is a virtual environment for?
A. Isolating packages for a project
B. Publishing every project
C. Replacing Python
D. Creating HTML

5. What can __init__.py do?
A. Help define a package and expose public functions
B. Delete modules
C. Start the computer
D. Install Git

6. What does from .maths import add mean?
A. Import add from maths in the same package
B. Download maths from the internet
C. Create a venv
D. Run all tests

7. What is pyproject.toml used for?
A. Metadata and packaging/tool configuration
B. Images only
C. Passwords
D. Replacing Python files

8. What does [build-system] describe?
A. Build tools and backend
B. Student names
C. HTML tags
D. Wallpaper

9. What is README.md usually for?
A. Project description and usage instructions
B. Bytecode only
C. Passwords
D. Drivers

10. What is .gitignore for?
A. Telling Git which untracked files/folders to ignore
B. Running tests
C. Publishing packages
D. Formatting Python

11. What does python -m pip install -e . do in the project root?
A. Installs the local project in editable mode
B. Deletes the project
C. Installs a browser
D. Runs tests automatically

12. What does the dot in pip install -e . mean?
A. The current directory/project
B. The internet
C. A password
D. A class

13. Which file commonly lists packages to install?
A. requirements.txt
B. app.png
C. index.html only
D. .git/HEAD only

14. What is pytest used for?
A. Running automated tests
B. Building a browser
C. Uploading images
D. Creating virtual machines

15. What does assert add(2, 3) == 5 check?
A. That add(2, 3) returns 5
B. That Git is installed
C. That Python is deleted
D. That the project is online

16. Which command runs tests through Python?
A. python -m pytest -v
B. git run all
C. python -m package upload
D. pip delete tests

17. Which command builds distributions when build is installed?
A. python -m build
B. python -m git
C. python -m pytest --publish
D. python -m README

18. What is a wheel file?
A. A built Python distribution format
B. A loop
C. A Git branch
D. An editor theme

19. Why use editable installation?
A. Source changes are available without reinstalling after every edit
B. It prevents all bugs
C. It automatically publishes to PyPI
D. It replaces tests

20. Must every classroom package be published to PyPI?
A. Yes, always
B. No, publishing is optional
C. Only if it has one function
D. Only if it uses a venv
"""

# ============================================================
# 19. TEACHER'S ANSWER KEY — HIDE BEFORE THE TEST
# ============================================================
"""
1. A
2. A
3. A
4. A
5. A
6. A
7. A
8. A
9. A
10. A
11. A
12. A
13. A
14. A
15. A
16. A
17. A
18. A
19. A
20. B
"""

if __name__ == "__main__":
    print("Advanced Python: Packaging and Project Structure")
    print("This file contains teaching notes and examples.")
    print("Create the described project files and run commands in the terminal.")
