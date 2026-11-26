"""
COMPLETE BEGINNER'S PRACTICAL GUIDE: GIT, GITHUB, WORKFLOWS, CI AND CD

Teaching notes for VS Code on Linux Mint. Explanations are comments/docstrings.
Commands belong in the VS Code TERMINAL, not in a Python file. YAML belongs in
.github/workflows/python-ci.yml, not in app.py.

PROJECT WE WILL BUILD:
- A tiny Python app tracked by Git.
- A GitHub repository.
- A feature branch and Pull Request.
- Automated tests with pytest and GitHub Actions.
- A simple explanation of Continuous Integration, Delivery and Deployment.

NEVER upload passwords, API keys, access tokens, or private information.
"""

# ============================================================
# LESSON 1 — SIMPLE DEFINITIONS
# ============================================================
"""
GIT: A version-control tool that records changes to project files. It works
locally on your computer.

GITHUB: An online service for hosting Git repositories and collaborating.

REPOSITORY (REPO): A project and its tracked history.

COMMIT: A named checkpoint in the history, e.g. "Add greeting function".

BRANCH: A separate line of work for a change or feature.

PULL REQUEST (PR): A request to review and merge changes from one branch into
another on GitHub.

WORKFLOW: Automated steps that GitHub Actions runs after an event, such as a
push or a Pull Request.

CI — CONTINUOUS INTEGRATION: Automatically checking changes, commonly by
installing dependencies and running tests.

CD has two common meanings:
- CONTINUOUS DELIVERY: code is built/tested and kept ready to release; a person
  may approve the final production release.
- CONTINUOUS DEPLOYMENT: every change that passes required checks is deployed
  automatically to production without a manual approval for each release.

Git is not GitHub. A push does not automatically deploy a website. CI/CD does
not guarantee bug-free software; it automates checks and release steps.
"""

# ============================================================
# LESSON 2 — CHECK INSTALLATION AND CONFIGURE GIT
# ============================================================
"""
Open VS Code > Terminal > New Terminal. Run each command in the terminal:

    git --version
    python3 --version

If Git is missing on Linux Mint / Ubuntu-based Linux, normally run:

    sudo apt update
    sudo apt install git

Configure the name and email that should appear on your commits:

    git config --global user.name "Your Name"
    git config --global user.email "your-email@example.com"
    git config --global --list

Use your own name and email. If you prefer privacy on GitHub, you can use the
GitHub-provided noreply email shown in your account settings.
"""

# ============================================================
# LESSON 3 — CREATE A SMALL PYTHON PROJECT
# ============================================================
"""
Create and open a folder named git_github_class in VS Code. Create app.py and
put the following code in it, then save:
"""

def greet(name):
    """Return a greeting for a person's name."""
    return f"Hello, {name}!"


def add_numbers(first, second):
    """Return the sum of two numbers."""
    return first + second


if __name__ == "__main__":
    print(greet("Python student"))
    print("2 + 3 =", add_numbers(2, 3))

"""
Run it in the terminal:

    python3 app.py

Expected output:
    Hello, Python student!
    2 + 3 = 5

Make sure the terminal is in the project folder. Check with pwd and ls.
If needed, use cd to enter the folder, for example:
    cd ~/Desktop/git_github_class
Use your actual folder path.
"""

# ============================================================
# LESSON 4 — START GIT TRACKING
# ============================================================
"""
In the project folder, run:

    git init
    git status

git init starts a local Git repository. git status shows which files are
untracked, modified, staged, or committed. A hidden .git folder stores the
repository history; normally you do not edit it manually.
"""

# ============================================================
# LESSON 5 — STAGE, COMMIT AND VIEW HISTORY
# ============================================================
"""
Git's simple sequence is: EDIT -> STAGE -> COMMIT.

    git add app.py
    git status
    git commit -m "Add starter Python application"
    git log --oneline

- git add selects changes for the next commit (staging).
- git commit saves staged changes as a checkpoint.
- git log --oneline shows compact commit history.

Edit app.py, save it, and try:

    git status
    git diff

git diff shows unstaged edits. After staging, use git diff --staged to inspect
the changes selected for the next commit.
"""

# ============================================================
# LESSON 6 — CREATE .gitignore
# ============================================================
"""
Create a file named .gitignore in the project root. Put this text in it:
"""
GITIGNORE_EXAMPLE = r"""

venv/
__pycache__/
*.py[cod].venv/
.env
.pytest_cache/
"""
"""
A .gitignore tells Git which untracked files to ignore. Save it, then run:

    git add .gitignore
    git commit -m "Add Python gitignore"

Important: .gitignore does not remove a secret already committed. If a secret
was uploaded, revoke/rotate it and follow GitHub's guidance for cleanup.
"""

# ============================================================
# LESSON 7 — CREATE A GITHUB REPOSITORY
# ============================================================
"""
In the browser:
1. Sign in at https://github.com/
2. Click + and choose New repository.
3. Name it git-github-class.
4. Add a short description.
5. Choose Public only if you are comfortable making the code visible; otherwise
   choose Private.
6. Because you already have a local repo and commit, for this demonstration
   leave README, .gitignore and license initialisation unchecked.
7. Create the repository.

Copy the URL shown for YOUR repository. It will resemble:
    https://github.com/YOUR-USERNAME/git-github-class.git
Replace YOUR-USERNAME with your real GitHub username.
"""

# ============================================================
# LESSON 8 — CONNECT TO GITHUB AND PUSH
# ============================================================
"""
In the terminal, replace the URL with your actual repository URL:

    git remote add origin https://github.com/YOUR-USERNAME/git-github-class.git
    git remote -v
    git branch -M main
    git push -u origin main

remote add connects the local repository to GitHub. branch -M main names the
current branch main. push uploads commits. Refresh GitHub to see app.py.

GitHub may ask you to authenticate. Follow the supported browser/credential
flow. Your GitHub account password generally cannot be used as a normal HTTPS
Git password. Never paste a token into this guide or share it with students.

If you see "remote origin already exists", check git remote -v. If the URL is
wrong, update it with:
    git remote set-url origin ACTUAL_REPOSITORY_URL
"""

# ============================================================
# LESSON 9 — EVERYDAY COMMANDS
# ============================================================
"""
    git status                    # See current file state
    git add app.py                # Stage one file
    git add .                     # Stage current-folder changes
    git commit -m "Describe it"  # Save staged changes
    git log --oneline             # Show history
    git diff                      # Show unstaged changes
    git remote -v                 # Show remote URLs
    git push                      # Upload local commits
    git pull                      # Fetch and integrate remote changes
    git clone REPOSITORY_URL      # Copy an existing remote repository
    git branch                    # List local branches

Check git status before pulling if you have local edits. Commit or safely
save your work first so you do not accidentally lose changes.
"""

# ============================================================
# LESSON 10 — BRANCHES AND FEATURE WORK
# ============================================================
"""
Create a separate branch for a new greeting feature:

    git switch -c feature/better-greeting

Change the return line in greet() to:
    return f"Welcome to the class, {name}!"

Save app.py and run:
    python3 app.py
    git status
    git diff
    git add app.py
    git commit -m "Improve greeting message"
    git push -u origin feature/better-greeting

A branch lets you develop separately from main. If this is your first branch,
the push command also sets the remote tracking branch.
"""

# ============================================================
# LESSON 11 — PULL REQUEST
# ============================================================
"""
After pushing the branch:
1. Open your repository on GitHub.
2. Choose the prompt to compare/create a Pull Request, or open Pull requests.
3. Set base to main and compare to feature/better-greeting.
4. Add a title and short description, then create the PR.
5. Review Files changed and any automated checks.
6. For class, merge it if the changes are correct.
7. Back in the terminal, synchronise main:

    git switch main
    git pull origin main
    git branch -d feature/better-greeting

A Pull Request is a review-and-merge request. It is not the same as git pull.
"""

# ============================================================
# LESSON 12 — ADD TESTS WITH PYTEST
# ============================================================
"""
Create test_app.py in the project root and paste this code:
"""
TEST_APP_EXAMPLE = r"""
from app import greet, add_numbers


def test_greet():
    assert greet("Ada") == "Hello, Ada!"


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_add_zero():
    assert add_numbers(10, 0) == 10
"""
"""
Install pytest in the Python environment you are using:

    python3 -m pip install pytest

Run tests:
    python3 -m pytest -v

Expected: three tests pass. If you changed greet() in the previous lesson,
update the expected result in test_app.py to match the current code.

A test uses assert to compare the actual result with the expected result.
Commit and push the test file when ready:
    git add test_app.py
    git commit -m "Add application tests"
    git push
"""

# ============================================================
# LESSON 13 — GITHUB ACTIONS TERMS
# ============================================================
"""
GitHub Actions automates tasks in a repository.

- Event/trigger: what starts a workflow, e.g. push or pull_request.
- Workflow: the complete automation definition.
- Job: a group of steps.
- Runner: the machine that executes a job, e.g. ubuntu-latest.
- Step: one command or action inside a job.
- Action: reusable automation code.
- Artifact: a file saved from a workflow run.

Workflow files are normally saved in .github/workflows/ and use YAML.
Pushing code does not create a workflow automatically; you must add the YAML.
"""

# ============================================================
# LESSON 14 — CREATE A PYTHON CI WORKFLOW
# ============================================================
"""
Create this file path inside the project:
    .github/workflows/python-ci.yml

In VS Code Explorer, create .github, then workflows inside it, then the file
python-ci.yml. Paste the YAML below into that file. It is YAML, NOT Python.
"""
PYTHON_CI_WORKFLOW = r"""
name: Python CI

on:
  push:
  pull_request:

permissions:
  contents: read

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          python -m pip install pytest

      - name: Run tests
        run: python -m pytest -v
"""
"""
Explanation:
- name gives the workflow a display name.
- on tells GitHub which events trigger it: pushes and Pull Requests.
- permissions limits the workflow to read repository contents.
- jobs defines jobs; this workflow has one named test.
- runs-on chooses a hosted Linux runner.
- checkout downloads the repository files onto the runner.
- setup-python installs/selects Python 3.12.
- the install step installs pytest.
- the final step runs tests. A failing test makes the workflow fail.

This uses commonly used major versions of the official checkout and setup-
python actions. Check the official GitHub documentation for current versions
and your organisation's security policy before using workflows in production.

YAML uses indentation. Use spaces consistently, not tabs. Do not paste this
YAML into app.py. It must be saved under .github/workflows/.
"""

# ============================================================
# LESSON 15 — COMMIT, PUSH AND VIEW THE WORKFLOW
# ============================================================
"""
After saving the workflow, run in the project terminal:

    git status
    git add app.py test_app.py .gitignore .github/workflows/python-ci.yml
    git commit -m "Add automated Python CI workflow"
    git push

If working on a feature branch, push that branch and use its Pull Request.

On GitHub:
1. Open the repository.
2. Click Actions.
3. Open Python CI and choose the latest run.
4. Open the test job and inspect each step.

A green check means the workflow completed successfully. A red cross means a
step failed. Open the failed step and read its logs.
"""

# ============================================================
# LESSON 16 — DEMONSTRATE A FAILING TEST
# ============================================================
"""
1. Open test_app.py.
2. Temporarily change:
       assert add_numbers(2, 3) == 5
   to:
       assert add_numbers(2, 3) == 999
3. Run locally:
       python3 -m pytest -v
4. Observe the failing test and its error message.
5. Restore the expected value 5 and rerun tests.

For a GitHub demonstration, do this only on a classroom feature branch: commit
and push the intentionally failing test, observe a red workflow, fix it, then
push again and observe a green workflow. Do not leave main broken.

This demonstrates why CI is useful: it automatically checks changes and helps
find mistakes before code is merged.
"""

# ============================================================
# LESSON 17 — CI VS CONTINUOUS DELIVERY VS CONTINUOUS DEPLOYMENT
# ============================================================
"""
CI: Changes trigger automated checks, such as running tests.

CONTINUOUS DELIVERY: Code is automatically built/tested and kept ready for
release. A person may approve the final production release.

CONTINUOUS DEPLOYMENT: Every change that passes required checks is deployed
automatically to production without a manual approval for each release.

FLOW:
Edit -> git add -> git commit -> git push -> GitHub -> CI tests
                                               |
                            tests fail --------+------ tests pass
                               |                       |
                            fix code              review / merge
                                                       |
                                             delivery/deployment
                                             if separately configured

The workflow in this lesson only runs CI tests. It does not deploy an app.
Deployment needs a host, deployment commands/actions, secure credentials, and
appropriate permissions. Start with CI before attempting production deployment.

Never put passwords, API keys, tokens, or private keys directly in code or
workflow YAML. Use appropriately configured GitHub Actions secrets, limit
permissions, and avoid printing secret values in logs.
"""

# ============================================================
# LESSON 18 — TROUBLESHOOTING
# ============================================================
"""
git: command not found
    Install Git and restart the terminal.

Git asks for user.name or user.email
    git config --global user.name "Your Name"
    git config --global user.email "your-email@example.com"

Authentication fails on push
    Follow GitHub's supported browser/credential flow. Never share tokens.

remote origin already exists
    Check git remote -v; update with git remote set-url origin ACTUAL_URL.

Nothing to commit
    Run git status, save the file, stage changes, and check whether it changed.

Workflow does not run
    Confirm YAML is committed under .github/workflows/, filename ends in .yml
    or .yaml, trigger matches the event, and indentation is correct.

pytest not found locally
    python3 -m pip install pytest
    python3 -m pytest -v

No tests found
    Name test files test_*.py or *_test.py and test functions test_*. Ensure
    the workflow runs from the project root.
"""

# ============================================================
# LESSON 19 — CLASSROOM CHECKLIST
# ============================================================
"""
[ ] Check Git and Python installation.
[ ] Configure Git name and email.
[ ] Create app.py and run it.
[ ] Run git init and inspect git status.
[ ] Stage and commit the initial code.
[ ] Add .gitignore.
[ ] Create a GitHub repository.
[ ] Add remote and push main.
[ ] Confirm files are visible on GitHub.
[ ] Create a feature branch and make a change.
[ ] Commit and push the branch.
[ ] Open and merge a Pull Request.
[ ] Add test_app.py and run pytest.
[ ] Add .github/workflows/python-ci.yml.
[ ] Push the workflow and find its run under Actions.
[ ] Demonstrate a failing test safely on a branch, then fix it.
[ ] Explain CI, Continuous Delivery, and Continuous Deployment.
"""

# ============================================================
# LESSON 20 — QUICK COMMAND REFERENCE
# ============================================================
"""
    git --version
    git config --global user.name "Your Name"
    git config --global user.email "your-email@example.com"
    git init
    git status
    git add .
    git commit -m "Describe the change"
    git log --oneline
    git diff
    git remote -v
    git remote add origin REPOSITORY_URL
    git branch -M main
    git push -u origin main
    git switch -c feature/name
    git push -u origin feature/name
    git switch main
    git pull origin main
    python3 -m pip install pytest
    python3 -m pytest -v

Replace placeholders with your actual repository URL and branch names.
"""

# ============================================================
# LESSON 21 — OBJECTIVE TEST: 20 QUESTIONS
# ============================================================
"""
Choose ONE answer (A, B, C, or D). Each question is worth one mark.

1. What is Git?
A. A version-control tool  B. A browser  C. A database  D. A language

2. What is GitHub?
A. A Python function  B. An online Git hosting/collaboration service
C. A text editor only  D. A Linux command

3. What does git status show?
A. Weather  B. File and staging state  C. Password  D. Package versions only

4. What does git add do?
A. Stages changes  B. Deletes history  C. Deploys a site  D. Installs Python

5. What is a commit?
A. A saved checkpoint  B. A password  C. A browser tab  D. A package

6. What is a branch useful for?
A. Separate work  B. Turning Git off  C. Deleting files  D. Installing YAML

7. What does git push do?
A. Uploads local commits to a remote repo  B. Deletes the repo
C. Runs all programs  D. Creates a password

8. What does git pull generally do?
A. Fetches and integrates remote changes  B. Removes branches
C. Creates a list  D. Installs pytest

9. What is a Pull Request used for?
A. Review and merge proposed changes  B. Print text
C. Download a venv  D. Rename the computer

10. What is GitHub Actions?
A. Repository automation platform  B. Python data type
C. Spreadsheet formula  D. Database table

11. Where are workflow files normally stored?
A. .github/workflows/  B. .venv/  C. Downloads/  D. __pycache__/

12. What format is commonly used for workflow files?
A. YAML  B. MP3  C. PNG  D. DOCX

13. What is a workflow trigger?
A. Event that starts it, such as push  B. Python variable
C. Commit message  D. Keyboard

14. What is a runner?
A. Machine executing a workflow job  B. Profile photo
C. Python string  D. HTML tag

15. What does CI commonly automate?
A. Build/check/test steps  B. Buying computers
C. Typing all code  D. Guaranteeing no bugs

16. Which command runs pytest through Python?
A. python3 -m pytest -v  B. git pytest install
C. python3 --test-github  D. pip push pytest

17. A green Actions check usually means:
A. Workflow succeeded  B. Internet is always secure
C. App was deployed  D. No future bugs exist

18. What is Continuous Delivery?
A. Code is built/tested and ready to release, often with approval
B. Code is never tested  C. Git is removed  D. Branch always deleted

19. What is Continuous Deployment?
A. Qualifying changes automatically deploy after checks without manual
   production approval for each release
B. Manual file copying only  C. Tests disabled  D. Laptop-only storage

20. Where should workflow deployment secrets be stored?
A. Public Python file  B. Plain text in YAML
C. Properly configured GitHub Actions secrets  D. Commit message
"""

# ============================================================
# LESSON 22 — TEACHER'S ANSWER KEY
# ============================================================
"""
Hide this section before distributing the test to students.
1. A   2. B   3. B   4. A   5. A
6. A   7. A   8. A   9. A   10. A
11. A  12. A  13. A  14. A  15. A
16. A  17. A  18. A  19. A  20. C
"""

if __name__ == "__main__":
    print("Git, GitHub, Workflows, CI and CD — teaching guide")
    print("Run terminal commands in VS Code Terminal, not in this file.")
