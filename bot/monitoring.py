import functools
import sentry_sdk

def transaction(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with sentry_sdk.start_transaction(name=func.__name__, sampled=True) as _:
            return func(*args, **kwargs)

    return wrapper