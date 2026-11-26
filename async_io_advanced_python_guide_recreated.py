# ============================================================
# ADVANCED PYTHON: ASYNC I/O (async/await)
# COMPLETE BEGINNER-FRIENDLY TEACHING GUIDE
# ============================================================
#
# This is a valid Python file for VS Code.
# Explanations are comments, and the main examples are runnable.
#
# Run from the VS Code terminal:
#     python advanced_python_async_io_guide.py
#
# Optional HTTP example:
#     python -m pip install aiohttp
#     python advanced_python_async_io_guide.py --http
#
# LEARNING OBJECTIVES
# Students should be able to:
# 1. Explain I/O and why programs have to wait.
# 2. Compare synchronous and asynchronous code.
# 3. Explain async, await, coroutine, asyncio, and event loop.
# 4. Use asyncio.gather() and asyncio.create_task().
# 5. Handle errors and timeouts.
# 6. Make asynchronous HTTP requests using aiohttp.
# 7. Complete the practical exercises and objective test.
#
# ============================================================
# LESSON 1: WHAT IS I/O?
# ============================================================
#
# I/O means Input/Output. It includes communicating with something outside
# a program's immediate calculations.
#
# Examples:
# - Requesting data from a website or API.
# - Reading or writing a file.
# - Waiting for a database response.
# - Sending or receiving data over a network socket.
#
# These operations can take time because the program must wait for another
# system to respond. Async I/O helps the program make progress on other tasks
# while an asynchronous operation is waiting.
#
# Important: Async I/O is especially useful for waiting-heavy tasks. It does
# not automatically make CPU-heavy mathematical calculations faster.
#
# ============================================================
# LESSON 2: SYNCHRONOUS VS ASYNCHRONOUS
# ============================================================
#
# Synchronous code usually finishes one operation before moving to the next.
# If three operations each wait for one second, the total is about three
# seconds, plus overhead.
#
# Asynchronous code can pause a task while it waits and allow other async
# tasks to make progress. Three one-second waits can often finish in about
# one second overall if the tasks are run concurrently.
#
# This is concurrency: the tasks' progress overlaps. It does not necessarily
# mean that Python is executing all the task code on different CPU cores.
#
# ============================================================
# LESSON 3: PROJECT SETUP
# ============================================================
#
# Create a folder called async_io_lesson and open it in VS Code.
#
# Linux / macOS terminal:
#     python3 -m venv .venv
#     source .venv/bin/activate
#
# Windows terminal:
#     py -m venv .venv
#     .venv\Scripts\activate
#
# asyncio is included with Python; do not install it separately.
#
# For the optional asynchronous HTTP example, install aiohttp:
#     python -m pip install aiohttp
#
# ============================================================
# LESSON 4: A SYNCHRONOUS EXAMPLE
# ============================================================
#
# time.sleep() blocks the current thread. The next function runs only after
# the previous function has finished.
#
# Try this example by setting RUN_SYNC_DEMO = True in main() below.
#
#     import time
#
#     def wait_for_task(name):
#         print(f"Starting {name}")
#         time.sleep(1)
#         print(f"Finished {name}")
#
#     wait_for_task("Task A")
#     wait_for_task("Task B")
#     wait_for_task("Task C")
#
# Expected: each task starts and finishes before the next starts.
# Total time is about three seconds.
#
# ============================================================
# LESSON 5: YOUR FIRST ASYNC FUNCTION
# ============================================================
#
# async def defines an asynchronous function.
# await pauses the current coroutine while an awaitable operation is pending.
# asyncio.sleep() waits without blocking the event loop.
# asyncio.run() runs the async entry point in a normal Python script.
#
# Example:
#
#     import asyncio
#
#     async def greet():
#         print("Hello")
#         await asyncio.sleep(1)
#         print("One second has passed")
#
#     asyncio.run(greet())
#
# Note: async def alone does not automatically run a function concurrently.
# In the example above, main awaits tasks one by one, so they run sequentially.
#
# ============================================================
# LESSON 6: RUN TASKS CONCURRENTLY WITH asyncio.gather()
# ============================================================
#
# asyncio.gather() lets multiple awaitables make progress concurrently.
# A task waiting for I/O can give the event loop an opportunity to run others.
#
# In the runnable demonstration below, three tasks each wait for one second.
# Their combined elapsed time should be roughly one second, not three.
#
# ============================================================
# LESSON 7: asyncio.create_task()
# ============================================================
#
# asyncio.create_task(coroutine) schedules a coroutine as an asyncio Task.
# Keep references to important tasks and await them so they can finish and
# their results or errors can be handled.
#
# ============================================================
# LESSON 8: HANDLE ERRORS
# ============================================================
#
# Use try/except around operations that may fail and for which you can provide
# a useful response. Avoid silently ignoring important errors.
#
# ============================================================
# LESSON 9: TIMEOUTS
# ============================================================
#
# asyncio.wait_for(operation, timeout=seconds) limits how long the operation
# may wait. If the timeout expires, asyncio.TimeoutError is raised.
#
# A timeout differs from a server returning an HTTP error status. It means
# the operation did not finish within the allowed time.
#
# ============================================================
# LESSON 10: ASYNCHRONOUS HTTP USING aiohttp
# ============================================================
#
# Requests is a common synchronous HTTP library. aiohttp supports asynchronous
# HTTP requests, letting multiple requests wait concurrently.
#
# Install it in your active virtual environment:
#     python -m pip install aiohttp
#
# The optional runnable example is near the bottom of this file. Run it with:
#     python advanced_python_async_io_guide.py --http
#
# It fetches test users from JSONPlaceholder. Internet access is required.
# If the network or service is unavailable, the example handles common errors.
#
# ============================================================
# LESSON 11: ASYNC I/O VS THREADING VS MULTIPROCESSING
# ============================================================
#
# Async I/O:
# Suitable for many operations that spend time waiting, especially network I/O.
#
# Threading:
# Can be useful for blocking I/O. Shared data between threads needs care.
#
# Multiprocessing:
# Can help with suitable CPU-heavy work by using separate processes.
#
# These are guidelines. Choose based on the workload and the libraries in use.
#
# ============================================================
# LESSON 12: COMMON MISTAKES
# ============================================================
#
# 1. Calling an async function without awaiting it:
#        async def greet():
#            print("Hello")
#        greet()
#    This creates a coroutine but does not run it by itself.
#
# 2. Using await at top level in a normal .py script:
#    Put await inside an async function, then call asyncio.run(main()).
#
# 3. Using time.sleep() inside an async function:
#    This blocks the event loop. Use await asyncio.sleep() for async waits.
#
# 4. Expecting async def alone to create concurrency:
#    Use gather() or create_task() when independent tasks should overlap.
#
# 5. Expecting async I/O to make CPU-heavy calculations faster:
#    Async I/O is primarily for waiting-heavy work.
#
# 6. aiohttp not installed:
#        python -m pip install aiohttp
#
# ============================================================
# LESSON 13: PRACTICAL EXERCISES
# ============================================================
#
# Exercise 1:
# Write an async function that waits one second and prints "Finished".
#
# Exercise 2:
# Create three tasks that wait for 1, 2, and 3 seconds. Run them with
# asyncio.gather() and observe which finishes first.
#
# Exercise 3:
# Compare three one-second tasks run sequentially with three tasks run using
# gather(). Measure the elapsed time using time.perf_counter().
#
# Exercise 4:
# Use asyncio.create_task() to schedule two tasks with different waiting times.
# Await both tasks.
#
# Exercise 5:
# Create an operation that waits four seconds but give it a one-second timeout.
#
# Exercise 6:
# Use the optional HTTP example to fetch users 1–5, displaying names and emails.
#
# Exercise 7:
# Extend the HTTP example to ask for user IDs and handle invalid input.
#
# ============================================================
# LESSON 14: LESSON SUMMARY
# ============================================================
#
# - I/O means input/output, including network and file operations.
# - async def defines an asynchronous function.
# - await waits for an awaitable and can suspend the current coroutine.
# - asyncio.run() runs the async entry point.
# - asyncio.sleep() is non-blocking for the event loop.
# - asyncio.gather() lets several awaitables progress concurrently.
# - asyncio.create_task() schedules a coroutine as a Task.
# - Timeouts and exception handling make programs more robust.
# - aiohttp supports asynchronous HTTP requests.
# - Async I/O is most useful for I/O-bound workloads.
#
# ============================================================
# RUNNABLE EXAMPLES
# ============================================================

import asyncio
import sys
import time


async def wait_task(name: str, seconds: float = 1.0) -> str:
    """Wait asynchronously, print progress, and return a result."""
    print(f"Starting {name}")
    await asyncio.sleep(seconds)
    print(f"Finished {name}")
    return f"{name} complete"


def run_sync_demo() -> None:
    """Show three sequential blocking waits."""
    print("\n--- SYNCHRONOUS DEMONSTRATION ---")

    def blocking_task(name: str) -> None:
        print(f"Starting {name}")
        time.sleep(1)
        print(f"Finished {name}")

    start = time.perf_counter()

    blocking_task("Task A")
    blocking_task("Task B")
    blocking_task("Task C")

    print(f"Sequential elapsed time: {time.perf_counter() - start:.2f} seconds")


async def run_async_demo() -> None:
    """Show sequential awaits, concurrent gather(), and create_task()."""
    print("\n--- ASYNC: SEQUENTIAL AWAITS ---")
    start = time.perf_counter()

    await wait_task("Task A", 1)
    await wait_task("Task B", 1)
    await wait_task("Task C", 1)

    print(f"Sequential async elapsed time: {time.perf_counter() - start:.2f} seconds")

    print("\n--- ASYNC: CONCURRENT TASKS WITH gather() ---")
    start = time.perf_counter()

    results = await asyncio.gather(
        wait_task("Task A", 1),
        wait_task("Task B", 1),
        wait_task("Task C", 1),
    )

    print("Results:", results)
    print(f"Concurrent elapsed time: {time.perf_counter() - start:.2f} seconds")

    print("\n--- ASYNC: SCHEDULING WITH create_task() ---")
    task_one = asyncio.create_task(wait_task("Task One", 2))
    task_two = asyncio.create_task(wait_task("Task Two", 1))

    await task_one
    await task_two


async def timeout_demo() -> None:
    """Demonstrate a timeout without waiting forever."""
    print("\n--- TIMEOUT DEMONSTRATION ---")

    async def slow_operation() -> str:
        await asyncio.sleep(3)
        return "Operation completed"

    try:
        result = await asyncio.wait_for(slow_operation(), timeout=1)
        print(result)
    except asyncio.TimeoutError:
        print("The operation took too long, so the timeout expired.")


async def error_demo() -> None:
    """Demonstrate handling an expected error from a coroutine."""
    print("\n--- ERROR HANDLING DEMONSTRATION ---")

    async def load_data() -> str:
        await asyncio.sleep(0.2)
        raise ValueError("Example: data could not be loaded")

    try:
        data = await load_data()
        print(data)
    except ValueError as error:
        print("Handled error:", error)


async def async_http_demo() -> None:
    """Fetch three test users asynchronously. Requires aiohttp and internet."""
    try:
        import aiohttp
    except ImportError:
        print("aiohttp is not installed.")
        print("Install it with: python -m pip install aiohttp")
        return

    print("\n--- ASYNCHRONOUS HTTP DEMONSTRATION ---")

    async def get_user(session: "aiohttp.ClientSession", user_id: int):
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

        try:
            timeout = aiohttp.ClientTimeout(total=10)
            async with session.get(url, timeout=timeout) as response:
                response.raise_for_status()
                user = await response.json()
                print(f"{user['name']} - {user['email']}")
                return user
        except (aiohttp.ClientError, asyncio.TimeoutError) as error:
            print(f"Could not load user {user_id}: {error}")
            return None

    try:
        async with aiohttp.ClientSession() as session:
            users = await asyncio.gather(
                get_user(session, 1),
                get_user(session, 2),
                get_user(session, 3),
            )

        successful_users = [user for user in users if user is not None]
        print(f"Successfully loaded {len(successful_users)} users.")
    except Exception as error:
        # This final guard is for unexpected demonstration errors.
        print("Unexpected problem in HTTP demonstration:", error)


async def main() -> None:
    """Run all local examples. No internet is required for these demos."""
    run_sync_demo()
    await run_async_demo()
    await timeout_demo()
    await error_demo()

    print("\n--- END OF LOCAL DEMONSTRATIONS ---")
    print("For asynchronous HTTP, run this file with the --http option.")


# ============================================================
# OBJECTIVE TEST — 25 MULTIPLE-CHOICE QUESTIONS
# Choose ONE answer (A, B, C, or D) for each question.
# Each question carries 1 mark. Total: 25 marks.
# Teacher's answer key is below; hide it before giving the test to students.
# ============================================================
#
# 1. What does I/O mean?
# A. Internet Order
# B. Input/Output
# C. Internal Object
# D. Integrated Operation
#
# 2. Async I/O is especially useful for:
# A. Tasks waiting for external operations
# B. Making every calculation faster
# C. Replacing all functions
# D. Removing error handling
#
# 3. Which keyword defines an asynchronous function?
# A. await
# B. async
# C. yield
# D. parallel
#
# 4. What does await do?
# A. Deletes a coroutine
# B. Waits for an awaitable result and can suspend the coroutine
# C. Installs a package
# D. Opens a browser
#
# 5. Which module is built into Python for async programming?
# A. asyncio
# B. aiohttp
# C. pandas
# D. selenium
#
# 6. What does asyncio.run(main()) do in a simple script?
# A. Runs the async entry-point coroutine
# B. Installs asyncio
# C. Converts Python to JavaScript
# D. Opens a website
#
# 7. Which call blocks the current thread while waiting?
# A. await asyncio.sleep(2)
# B. asyncio.gather()
# C. time.sleep(2)
# D. asyncio.create_task()
#
# 8. Which is suitable for non-blocking async waiting?
# A. time.sleep(2)
# B. await asyncio.sleep(2)
# C. print(2)
# D. input()
#
# 9. A coroutine is:
# A. An asynchronous unit of work defined by an async function
# B. A database table
# C. A package manager
# D. A list-only loop
#
# 10. What does asyncio.gather() help you do?
# A. Delete files
# B. Run multiple awaitables concurrently
# C. Install Python
# D. Format a disk
#
# 11. Does async def alone guarantee concurrent execution?
# A. Yes, always
# B. No; tasks must be awaited or scheduled appropriately
# C. Only on Windows
# D. Only with pandas
#
# 12. What is an event loop?
# A. A physical fan
# B. A scheduler that manages asynchronous tasks
# C. A comment
# D. A database
#
# 13. asyncio.create_task() is used to:
# A. Schedule a coroutine as a Task
# B. Create a text file
# C. Install a library
# D. Stop the operating system
#
# 14. A timeout is used to:
# A. Wait forever
# B. Limit how long an operation is allowed to wait
# C. Hide every error
# D. Increase CPU speed
#
# 15. Which block handles exceptions?
# A. if/else only
# B. try/except
# C. import/from
# D. class/def
#
# 16. Which package is used for async HTTP requests in this guide?
# A. aiohttp
# B. pytest
# C. beautifulsoup4
# D. selenium
#
# 17. Which command installs aiohttp in the active environment?
# A. python -m pip install aiohttp
# B. python aiohttp install
# C. git install aiohttp
# D. asyncio install aiohttp
#
# 18. Why use aiohttp.ClientSession()?
# A. To manage and reuse an HTTP client session
# B. To create a spreadsheet
# C. To start Django
# D. To draw a chart
#
# 19. response.raise_for_status() does what?
# A. Raises an exception for an unsuccessful HTTP status
# B. Prints every variable
# C. Starts the event loop
# D. Creates a user
#
# 20. Which workload best suits async I/O?
# A. Many network requests waiting for responses
# B. One huge CPU-heavy calculation in pure Python
# C. Drawing by hand
# D. Editing a document manually
#
# 21. Concurrency means:
# A. Managing overlapping progress of tasks
# B. Every task must run on a separate CPU core
# C. Code cannot wait
# D. All code is sequential
#
# 22. Why should important tasks be awaited?
# A. To handle their completion, results, and errors
# B. To delete them
# C. To avoid functions
# D. To turn them into strings
#
# 23. Which is correct in a normal standalone .py script?
# A. await main()
# B. asyncio.run(main())
# C. async main()
# D. run asyncio main
#
# 24. If a website is unreachable, robust code should:
# A. Assume success
# B. Handle network errors or timeouts
# C. Pretend the request succeeded
# D. Remove exception handling
#
# 25. Does async I/O automatically make CPU-heavy calculations faster?
# A. Yes, always
# B. No
# C. Only with input()
# D. Only when printing
#
# TEACHER'S ANSWER KEY
# 1. B   2. A   3. B   4. B   5. A
# 6. A   7. C   8. B   9. A   10. B
# 11. B  12. B  13. A  14. B  15. B
# 16. A  17. A  18. A  19. A  20. A
# 21. A  22. A  23. B  24. B  25. B
#
# ============================================================
# START THE PROGRAM
# ============================================================

if __name__ == "__main__":
    if "--http" in sys.argv:
        asyncio.run(async_http_demo())
    else:
        asyncio.run(main())
