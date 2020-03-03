import time
import functools

from django.db import connection, reset_queries


def debugger_queries(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        reset_queries()

        start = time.perf_counter()
        start_queries = len(connection.queries)

        result = func(*args, **kwargs)

        end = time.perf_counter()
        end_queries = len(connection.queries)

        print(f"Function: {func.__name__}")
        print(f"Queries: {end_queries - start_queries}")
        print(f"Time Finished: {(end - start):.2f}s")

        return result

    return wrapper
