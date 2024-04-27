import time
from contextlib import contextmanager


@contextmanager
def estim_time():
    """
    A context manager to measure the time elapsed during the execution of a block of code.

    This function uses the `@contextmanager` decorator to simplify context management. The execution flow is:
    1. Code before the `yield` statement runs before entering the main block.
    2. The main block of code runs.
    3. Code after the `yield` statement runs upon exiting the main block, regardless of whether an exception was raised.

    The `try-finally` structure ensures that the time measurement and reporting will occur even if an exception is raised in the main block.

    Yields:
        None: This context manager does not provide a value upon yielding.

    Prints:
        The time elapsed, in seconds, formatted to two decimal places.
    """
    start = time.time()

    try:
        yield
    finally:
        end = time.time()
        print(f"Time elapsed via context manager: {end - start:.2f} seconds")



class ElapsedTime:
    def __enter__(self):
        """
        Start the timer by recording the current time.
        This method is automatically called when entering a `with` block.
        """
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Stop the timer and print the elapsed time.
        This method is automatically called when exiting a `with` block.

        Args:
            exc_type (type): The type of the exception if an exception has been raised within the `with` block.
            exc_val (Exception): The exception instance if an exception has been raised within the `with` block.
            exc_tb (traceback): A traceback object if an exception has been raised.

        Prints:
            The time elapsed since entering the `with` block.
        """
        end = time.time()
        print(f"Time elapsed via context manager class: {end - self.start:.2f} seconds")



if __name__ == "__main__":
    # Using basic timing
    start = time.time()
    print("Starting basic timing...")
    time.sleep(1)
    end = time.time()
    print(f"Time elapsed via basic timing: {end - start:.2f} seconds")

    # Using the context manager function
    with estim_time():
        print("Starting context manager timing...")
        time.sleep(1.5)

    # Using the context manager class
    with ElapsedTime():
        print("Starting context manager class timing...")
        time.sleep(2.5)
