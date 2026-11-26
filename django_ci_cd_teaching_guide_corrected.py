# """
# PRACTICAL TEACHING GUIDE: DJANGO CI/CD WITH GITHUB ACTIONS AND RENDER
# =====================================================================
#
# Purpose
# -------
# Use this file as a step-by-step teaching reference for showing a student how to:
# 1. Prepare a Django project for Git.
# 2. Push the project to GitHub.
# 3. Add automated tests with GitHub Actions (Continuous Integration / CI).
# 4. Configure Render to deploy only after CI checks pass (Continuous Deployment / CD).
# 5. Verify that the deployed website works.
#
# IMPORTANT
# ---------
# - This file is a teaching guide. It is not application code to run as a Python program.
# - Copy commands into the terminal only when the matching step tells you to.
# - Replace example names and paths with the student's actual project details.
# - Never commit passwords, secret keys, database credentials, or API tokens.
# - The exact Render dashboard labels may change slightly over time.
#
# =====================================================================
# LESSON 1 — UNDERSTAND THE WORKFLOW
# =====================================================================
#
# Explain these terms in simple language:
#
# Git
#     A tool that records changes to files on the student's computer.
#
# GitHub
#     An online place to store a Git repository and collaborate with others.
#
# Commit
#     A saved checkpoint of changes in Git.
#
# Push
#     Sending local commits to GitHub.
#
# Test
#     Code that checks whether part of the application behaves as expected.
#
# CI — CONTINUOUS INTEGRATION
#     Whenever code is pushed to GitHub, GitHub Actions can install dependencies,
#     check the Django configuration, and run tests automatically.
#
# CD — CONTINUOUS DEPLOYMENT
#     After the code passes the required checks, Render can automatically deploy
#     the new version of the website.
#
# Simple workflow:
#
#     Student edits code
#           |
#           v
#     git add / git commit
#           |
#           v
#     git push to GitHub
#           |
#           v
#     GitHub Actions runs CI checks and tests
#           |
#           +---- If checks fail: investigate and fix the code
#           |
#           v
#     If checks pass, Render deploys the new version
#           |
#           v
#     Visit the live website and verify it
#
# Teaching point:
# CI checks the code. CD publishes the code. They are connected, but they are
# not the same thing.
#
# =====================================================================
# LESSON 2 — CHECK THE DJANGO PROJECT
# =====================================================================
#
# 1. Open the project in VS Code.
# 2. Open the VS Code terminal.
# 3. Activate the project's virtual environment.
#
# Example for Linux Mint, if the environment folder is named .venv:
#
#     source .venv/bin/activate
#
# If the environment folder is named venv:
#
#     source venv/bin/activate
#
# 4. Run Django's configuration check:
#
#     python manage.py check
#
# Expected result:
#     System check identified no issues (0 silenced).
#
# 5. Run the existing tests:
#
#     python manage.py test
#
# If it reports "Found 0 test(s)", Django has not found any tests yet. That is
# not the same as having useful tests pass. Add a small test in the correct
# Django app/package and run the command again.
#
# Teaching question:
# Why should we check the project locally before asking GitHub to check it?
#
# Expected answer:
# It is faster to find and fix basic errors locally before pushing changes.
#
# =====================================================================
# LESSON 3 — MAKE SURE THE PROJECT IS TRACKED BY GIT
# =====================================================================
#
# From the project root, run:
#
#     git status
#
# This shows changed files and whether there are untracked files.
#
# If the project has not been initialized as a Git repository, and the student
# intends to use Git, run:
#
#     git init
#
# Check the branch:
#
#     git branch
#
# For a new repository, a branch can be named main:
#
#     git branch -M main
#
# Only do this when appropriate for the student's repository.
#
# Before committing, check that secrets and local-only files are excluded.
# A typical .gitignore for Django may include:
#
#     .venv/
#     venv/
#     __pycache__/
#     *.py[cod]
#     db.sqlite3
#     .env
#     staticfiles/
#     media/
#
# Note:
# Do not blindly replace an existing .gitignore. Review it and preserve any
# project-specific entries. Whether to ignore media or SQLite files depends on
# the project; do not ignore data the project intentionally needs to version.
#
# Check what Git is tracking:
#
#     git status
#
# Teaching question:
# Why should .env and virtual environment folders normally not be committed?
#
# Expected answer:
# They may contain secrets or machine-specific dependencies and files.
#
# =====================================================================
# LESSON 4 — PUSH THE PROJECT TO GITHUB
# =====================================================================
#
# If the GitHub remote is already configured, inspect it:
#
#     git remote -v
#
# Inspect the latest commits:
#
#     git log --oneline -5
#
# If the remote is not configured, create a repository on GitHub first, then
# connect it using the repository URL provided by GitHub. Example only:
#
#     git remote add origin https://github.com/USERNAME/REPOSITORY.git
#
# Check the remote again:
#
#     git remote -v
#
# Stage and commit the intended changes:
#
#     git add .
#     git status
#     git commit -m "Prepare Django project for CI"
#
# Push the branch:
#
#     git push -u origin main
#
# For later changes, a normal workflow is:
#
#     git status
#     git add path/to/changed_file.py
#     git commit -m "Describe the change"
#     git push origin main
#
# Important:
# - Do not use `git add .` without checking `git status` first when you are unsure
#   what has changed.
# - If Git says there is nothing to commit, inspect `git status`; do not invent
#   another commit.
# - If a push is rejected, read the error before trying commands such as pull,
#   rebase, reset, or force-push. Avoid force-pushing unless you understand the
#   consequences.
#
# =====================================================================
# LESSON 5 — CREATE A SIMPLE DJANGO TEST
# =====================================================================
#
# Django discovers tests in test files inside installed Django applications.
# A common filename is:
#
#     tests.py
#
# For a Django project package that contains settings.py and urls.py, a simple
# test file can look like this. Adapt it to the student's actual project.
#
# Example: portfolio/tests.py
#
#     from django.test import SimpleTestCase
#     from django.urls import resolve, get_resolver
#
#
#     class PortfolioTests(SimpleTestCase):
#
#         def test_url_configuration_loads(self):
#             resolver = get_resolver()
#             self.assertIsNotNone(resolver)
#
#         def test_admin_url_resolves(self):
#             match = resolve("/admin/")
#             self.assertEqual(match.url_name, "index")
#
# Explanation:
# - SimpleTestCase is useful for tests that do not need a database.
# - get_resolver() checks that Django can load the URL configuration.
# - resolve("/admin/") checks that the admin URL maps to a URL pattern.
# - The test does not log in to the admin or prove every page works; it is a
#   small starter test, not complete test coverage.
#
# Run the tests locally:
#
#     python manage.py test
#
# Expected result should include a result such as:
#
#     Ran 2 tests
#     OK
#
# The exact output may differ. If the tests fail, read the traceback and fix the
# cause before proceeding.
#
# Teaching question:
# What is the difference between a test passing and a website being fully tested?
#
# Expected answer:
# Passing tests only prove the specific behavior covered by those tests. More
# tests are needed for other features and real user flows.
#
# =====================================================================
# LESSON 6 — CREATE THE GITHUB ACTIONS WORKFLOW (CI)
# =====================================================================
#
# At the root of the repository, create this folder and file:
#
#     .github/workflows/ci.yml
#
# Important:
# The .github folder must be at the repository root, not inside the inner Django
# package folder.
#
# Example project layout:
#
#     project-root/
#         manage.py
#         requirements.txt
#         .github/
#             workflows/
#                 ci.yml
#         portfolio/
#             settings.py
#             urls.py
#             tests.py
#
# The following workflow is an example for a Django project that:
# - uses Python 3.12,
# - has requirements.txt at the repository root,
# - has manage.py at the repository root,
# - can run tests without production-only secrets or external services.
#
# Copy this into .github/workflows/ci.yml and adjust the Python version or setup
# if the student's project needs something different.
#
#     name: Django CI
#
#     on:
#       push:
#         branches:
#           - main
#       pull_request:
#         branches:
#           - main
#
#     permissions:
#       contents: read
#
#     jobs:
#       test:
#         name: Test Django Application
#         runs-on: ubuntu-latest
#
#         steps:
#           - name: Checkout repository
#             uses: actions/checkout@v5
#
#           - name: Set up Python
#             uses: actions/setup-python@v7
#             with:
#               python-version: "3.12"
#               cache: pip
#
#           - name: Install dependencies
#             run: |
#               python -m pip install --upgrade pip
#               pip install -r requirements.txt
#
#           - name: Check Django configuration
#             env:
#               SECRET_KEY: ci-test-secret-key
#               DEBUG: "True"
#             run: python manage.py check
#
#           - name: Run Django tests
#             env:
#               SECRET_KEY: ci-test-secret-key
#               DEBUG: "True"
#             run: python manage.py test
#
# Notes for the instructor:
# - This is a starter workflow. If settings.py requires other environment variables,
#   provide safe test values or use a dedicated CI settings configuration.
# - If the project needs PostgreSQL, Redis, external APIs, or other services,
#   configure them for CI instead of assuming they are available.
# - The example sets a test-only SECRET_KEY. Never place the real production
#   SECRET_KEY in the workflow file.
# - GitHub Actions versions can change. Use supported action versions for the
#   project and organization.
# - If requirements.txt is missing or incomplete, dependency installation fails.
#
# =====================================================================
# LESSON 7 — COMMIT AND PUSH THE CI WORKFLOW
# =====================================================================
#
# From the repository root, inspect the files:
#
#     git status
#
# Stage the workflow and test file (adjust paths to match the project):
#
#     git add .github/workflows/ci.yml portfolio/tests.py
#
# Commit:
#
#     git commit -m "Add Django CI workflow and tests"
#
# Push:
#
#     git push origin main
#
# If the test file is in another app, use its actual path instead of
# portfolio/tests.py.
#
# =====================================================================
# LESSON 8 — CHECK GITHUB ACTIONS
# =====================================================================
#
# 1. Open the repository on GitHub.
# 2. Select the Actions tab.
# 3. Open the latest "Django CI" workflow run.
# 4. Open the "Test Django Application" job.
# 5. Confirm the steps are green:
#    - Checkout repository
#    - Set up Python   
#    - Install dependencies
#    - Check Django configuration
#    - Run Django tests
#
# A successful run should show a green checkmark and a Success status.
#
# If a step fails:
# 1. Click the failed job.
# 2. Expand the red failed step.
# 3. Read the first meaningful error.
# 4. Fix the cause locally.
# 5. Run `python manage.py check` and `python manage.py test` locally.
# 6. Commit and push the fix.
# 7. Check the new workflow run.
#
# Useful extra check:
# Open the repository's Commits page. A commit with a green check means the
# configured check passed for that commit.
#
# Teaching point:
# A green check is evidence that the configured checks passed. It does not mean
# the application has no bugs or that deployment has succeeded.
#
# =====================================================================
# LESSON 9 — CONFIGURE RENDER FOR DEPLOYMENT AFTER CI
# =====================================================================
#
# Goal:
# Render should wait for GitHub CI checks to pass before deploying a new commit.
#
# 1. Open the Render Dashboard:
#        https://dashboard.render.com/
#
# 2. Open the existing Django portfolio Web Service.
#
# 3. Open Settings.
#
# 4. Find the Deploy section.
#
# 5. Find Auto-Deploy and click Edit if required.
#
# 6. Select:
#        After CI Checks Pass
#
# 7. Confirm/save the change if Render asks you to.
#
# What the options mean:
# - On Commit: Render deploys automatically when a new commit is detected.
# - After CI Checks Pass: Render waits for detected CI checks to pass before
#   deploying.
# - Off: automatic deployment is disabled; deployment is manual.
#
# Important:
# Render needs to detect the relevant GitHub checks. If it does not detect any
# checks, or if checks fail, deployment may not proceed as expected. Verify the
# setting and check Render's Events page after a new push.
#
# Do not change the service's build command, start command, environment variables,
# database settings, or production configuration as part of this step unless
# there is a separate reason to do so.
#
# Teaching question:
# Why is "After CI Checks Pass" safer than deploying every commit immediately?
#
# Expected answer:
# It helps prevent a commit with failing automated checks from being deployed.
#
# =====================================================================
# LESSON 10 — TEST THE COMPLETE CI/CD WORKFLOW
# =====================================================================
#
# Use a small, safe change such as correcting a comment or updating README.md.
#
# 1. Make the change locally.
# 2. Inspect the change:
#
#        git status
#        git diff
#
# 3. Commit and push:
#
#        git add README.md
#        git commit -m "Test CI CD workflow"
#        git push origin main
#
# Use the actual changed file path if it is not README.md.
#
# 4. Open GitHub Actions and wait for the workflow to finish.
# 5. Confirm the CI check passes.
# 6. Open Render's Events page.
# 7. Confirm Render starts a deployment after the check passes.
# 8. Wait until Render reports the deployment is live.
# 9. Open the live site and test a few important pages.
#
# Expected sequence:
#
#     Push -> GitHub CI passes -> Render deployment starts -> Deployment is live
#
# If CI fails:
# - Fix the error first.
# - Do not assume Render should deploy the failed commit.
# - Push a corrected commit and check again.
#
# If CI passes but Render does not deploy:
# - Confirm Auto-Deploy is set to "After CI Checks Pass".
# - Check GitHub Actions for a successful check on the latest commit.
# - Check Render Events for a reason the deploy did not start.
# - Confirm the service is connected to the correct repository and branch.
#
# =====================================================================
# LESSON 11 — COMMON PROBLEMS AND SIMPLE FIXES
# =====================================================================
#
# Problem: GitHub Actions says requirements.txt cannot be found.
# Possible cause:
# - requirements.txt is not at the repository root, or the workflow runs from
#   a different directory.
# Fix:
# - Check the repository file layout and update the install command or path.
#
# Problem: ModuleNotFoundError during CI.
# Possible cause:
# - A dependency is missing from requirements.txt.
# Fix:
# - Install the package in the virtual environment, update requirements.txt,
#   commit, and push.
#
# Problem: CI says "Found 0 test(s)".
# Possible cause:
# - Django did not discover a test file or test class.
# Fix:
# - Check that the test is inside an installed Django app and that the filename
#   follows Django's test discovery rules, commonly tests.py.
#
# Problem: `python manage.py check` fails only in GitHub Actions.
# Possible cause:
# - The settings module expects an environment variable that CI does not set.
# Fix:
# - Provide a safe test value or use test-specific settings. Do not expose
#   production secrets.
#
# Problem: Render deploys before checks finish.
# Possible cause:
# - Auto-Deploy is still set to "On Commit".
# Fix:
# - Change it to "After CI Checks Pass" and verify the next deployment sequence.
#
# Problem: CI passes but the live site has an error.
# Possible cause:
# - The tests do not cover the failing feature, or the deployment configuration
#   has a separate issue.
# Fix:
# - Inspect Render deployment logs, add a test for the behavior, and correct the
#   configuration or code.
#
# Problem: Local tests pass but CI tests fail.
# Possible cause:
# - Different Python versions, missing dependencies, environment variables,
#   filesystem assumptions, or external services.
# Fix:
# - Compare the local environment with the workflow configuration.
#
# =====================================================================
# LESSON 12 — STUDENT PRACTICAL EXERCISE
# =====================================================================
#
# Task:
# Set up a basic CI workflow for a Django project and demonstrate that Render
# deploys only after the checks pass.
#
# Student checklist:
# [ ] Run `python manage.py check`.
# [ ] Run `python manage.py test`.
# [ ] Confirm the project is tracked by Git.
# [ ] Confirm requirements.txt is committed.
# [ ] Add a simple Django test.
# [ ] Create .github/workflows/ci.yml.
# [ ] Commit and push the changes.
# [ ] Open GitHub Actions.
# [ ] Show a successful workflow run.
# [ ] Set Render Auto-Deploy to "After CI Checks Pass".
# [ ] Push a harmless test change.
# [ ] Show that CI passes before Render deploys.
# [ ] Open the live website and check it.
#
# Questions:
# 1. What does Git do?
# 2. What is the difference between Git and GitHub?
# 3. What is a commit?
# 4. What is the purpose of `git push`?
# 5. What does CI stand for?
# 6. What does the GitHub Actions workflow do?
# 7. Why do we run `python manage.py test`?
# 8. What does CD stand for?
# 9. Why choose "After CI Checks Pass" in Render?
# 10. If the tests fail, what should the developer do next?
#
# Suggested answers:
# 1. Git tracks file changes and versions.
# 2. Git is the version-control tool; GitHub hosts Git repositories online.
# 3. A commit is a saved checkpoint of changes.
# 4. It sends local commits to the remote repository.
# 5. Continuous Integration.
# 6. It installs dependencies and runs configured checks and tests.
# 7. To check the behaviors covered by the project's automated tests.
# 8. Continuous Deployment.
# 9. To make deployment wait for successful detected CI checks.
# 10. Read the error, fix the problem, test locally, then commit and push a fix.
#
# =====================================================================
# INSTRUCTOR SUMMARY
# =====================================================================
#
# Remember the sequence:
#
#     1. Check the Django project locally.
#     2. Write tests.
#     3. Store the code in Git.
#     4. Push the code to GitHub.
#     5. GitHub Actions runs CI.
#     6. Render waits for CI to pass.
#     7. Render deploys the application.
#     8. Test the live website.
#
# Start with a small project and a few reliable tests. Add more tests as the
# application grows. CI/CD is a repeatable workflow, not a guarantee that every
# possible bug has been caught.
