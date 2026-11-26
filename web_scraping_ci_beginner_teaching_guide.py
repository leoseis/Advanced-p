# WEB SCRAPING — CI TEACHING GUIDE (.py)
# All lines are Python comments so VS Code can open the file safely.
# Copy example code/YAML into the named project files.

# ======================================================================
# INTRODUCTION
# ======================================================================
# WEB SCRAPING PROJECT — BEGINNER CI GUIDE
# Project: web_scrapping (as shown in VS Code)
# This is ordinary Python, NOT Django. Do not use manage.py.
# CI = Continuous Integration: automatically install dependencies and run
# tests when code is pushed to GitHub. CI does not mean deployment.

# ======================================================================
# STEP 1 — VERIFY PROJECT ROOT
# ======================================================================
# In VS Code Terminal, run:
#     pwd
#     ls
# You should see links.py, find.py, and other scripts.
# Your (venv) prompt means the virtual environment is activated.
# Before creating the workflow, run:
#     git rev-parse --show-toplevel
# If this reports "not a git repository", initialize Git in Step 6.
# IMPORTANT: .github/workflows/ci.yml must be at the Git repository root.

# ======================================================================
# STEP 2 — INSTALL PACKAGES
# ======================================================================
# In the activated venv:
#     python -m pip install beautifulsoup4 requests pytest
#     python -m pip show beautifulsoup4 pytest
# Create requirements.txt at the project root containing:
#     beautifulsoup4
#     requests
#     pytest
# Add any other packages imported by your own scripts.
# Alternative: python -m pip freeze > requirements.txt
# Review freeze output because it includes all installed packages.

# ======================================================================
# STEP 3 — CREATE .gitignore
# ======================================================================
# Create .gitignore in project root with:
#     venv/
#     .venv/
#     __pycache__/
#     *.py[cod]
#     .pytest_cache/
#     .env
# Never commit secrets or your local virtual environment.

# ======================================================================
# STEP 4 — REFACTOR links.py FOR TESTING
# ======================================================================
# Your screenshot shows links.py parsing three sample anchor tags.
# Replace or adapt links.py to make the logic reusable:
#
#     from bs4 import BeautifulSoup
#
#     def extract_links(html):
#         soup = BeautifulSoup(html, "html.parser")
#         return [
#             (tag.get_text(strip=True), tag.get("href"))
#             for tag in soup.find_all("a")
#         ]
#
#     if __name__ == "__main__":
#         link_html = """
#         <a href="https://example.com/python">Python</a>
#         <a href="https://example.com/django">Django</a>
#         <a href="/contact">Contact</a>
#         """
#         for text, href in extract_links(link_html):
#             print(text, "->", href)
#
# WHY: tests can check returned values without requiring live websites.

# ======================================================================
# STEP 5 — CREATE TESTS
# ======================================================================
# Run from the folder containing links.py:
#     mkdir -p tests
#     touch tests/test_links.py
# Paste into tests/test_links.py:
#
#     from links import extract_links
#
#     def test_extracts_two_links():
#         html = '<a href="/a">Alpha</a><a href="/b">Beta</a>'
#         assert extract_links(html) == [("Alpha", "/a"), ("Beta", "/b")]
#
#     def test_empty_html():
#         assert extract_links("<p>No links</p>") == []
#
#     def test_missing_href():
#         assert extract_links("<a>Contact</a>") == [("Contact", None)]
#
# Run:
#     python -m pytest -v
# Expected for these examples: 3 passed.
# Use local HTML in unit tests, not network calls.

# ======================================================================
# STEP 6 — INITIALIZE GIT IF NEEDED
# ======================================================================
# Check:
#     git status
# If NOT a Git repository:
#     git init
#     git branch -M main
# If already a repository, DO NOT run git init again.
# Check root:
#     git rev-parse --show-toplevel

# ======================================================================
# STEP 7 — CREATE GITHUB ACTIONS
# ======================================================================
# From the Git repository root:
#     mkdir -p .github/workflows
#     touch .github/workflows/ci.yml
#
# Paste the following YAML into ci.yml WITHOUT Python comment markers:
#
# name: Web Scraping CI
#
# on:
#   push:
#     branches: [main]
#   pull_request:
#     branches: [main]
#
# permissions:
#   contents: read
#
# jobs:
#   test:
#     runs-on: ubuntu-latest
#     steps:
#       - name: Checkout repository
#         uses: actions/checkout@v4
#
#       - name: Set up Python
#         uses: actions/setup-python@v5
#         with:
#           python-version: "3.12"
#           cache: pip
#
#       - name: Install dependencies
#         run: |
#           python -m pip install --upgrade pip
#           python -m pip install -r requirements.txt
#
#       - name: Run automated tests
#         run: python -m pytest -v
#
# This workflow assumes requirements.txt, links.py and tests/ are at
# the repository root. If your repository root differs, adjust paths
# or working-directory before pushing.

# ======================================================================
# STEP 8 — COMMIT AND PUSH
# ======================================================================
# First create an empty repository on GitHub if needed.
# Check your remote:
#     git remote -v
# If there is no origin, add YOUR actual repository URL:
#     git remote add origin https://github.com/USERNAME/REPOSITORY.git
#
# Then:
#     git add .
#     git status
#     git commit -m "Add web scraping CI and tests"
#     git push -u origin main
#
# If origin already exists, do not add it twice.
# Do not force-push to solve errors without checking the cause.

# ======================================================================
# STEP 9 — VERIFY CI
# ======================================================================
# On GitHub, open the correct repository -> Actions.
# Select Web Scraping CI -> latest run -> test job.
# Green check: workflow succeeded.
# Red X: open the failing step and read the error.
# The workflow runs on pushes and pull requests to main.

# ======================================================================
# STEP 10 — CLASSROOM DEMONSTRATION
# ======================================================================
# 1. Run python -m pytest -v (three tests pass).
# 2. Deliberately change one expected value in a test.
# 3. Run pytest and observe the failing assertion.
# 4. Restore the correct expected value and rerun.
# 5. Commit/push and inspect the GitHub Actions run.
# 6. Ask students to explain each CI step in their own words.

# ======================================================================
# TROUBLESHOOTING
# ======================================================================
# No tests ran: name files test_*.py and functions test_*.
# No module named bs4: install beautifulsoup4; update requirements.
# No module named pytest: install pytest; update requirements.
# No module named links: run python -m pytest from project root.
# requirements.txt not found: check repository root and file location.
# Workflow not visible: verify .github/workflows/ci.yml on GitHub main.
# Network tests flaky: use sample HTML for reliable unit tests.

# ======================================================================
# STUDENT PRACTICAL ASSIGNMENT
# ======================================================================
# A. Create a function that extracts links from HTML.
# B. Write three pytest tests.
# C. Create requirements.txt and .gitignore.
# D. Create .github/workflows/ci.yml.
# E. Push to GitHub and show a green Actions run.
# F. Explain what happens when a test fails.

# ======================================================================
# OBJECTIVE QUESTIONS
# ======================================================================
# Q1. CI means: A Code Installation B Continuous Integration C Computer Input D Central Internet
# Q2. Test tool used: A React B Django C pytest D SQLite
# Q3. Workflow location: A venv/ B .github/workflows/ C tests/ D static/
# Q4. Run tests: A npm start B python manage.py test C python -m pytest -v D git status
# Q5. Dependencies file: A books.csv B requirements.txt C links.py D README.md
# Q6. Green Actions check means: A workflow passed B deployed C no tests D offline
# Q7. Why ignore venv/? A local packages B HTML C Git requires it D secret token
# Q8. Why test sample HTML? A needs internet B fast/reliable C deploy D delete data
# Q9. CI trigger in example: A open VS Code B push/PR to main C browser click D restart
# Q10. Valid pytest file: A links.csv B readme.md C test_links.py D config.json
#
# ANSWER KEY: 1-B, 2-C, 3-B, 4-C, 5-B, 6-A, 7-A, 8-B, 9-B, 10-C

