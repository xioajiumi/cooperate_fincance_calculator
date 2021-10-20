
import inspect
import functools
import time
import html
print(repr([1,23]))
print(html.escape(repr(["weqw"]),quote=False))
def my_wrapper(func):
    def wrapper(func_wrapper):
        func_wrapper.__doc__=func.__doc__
        func_wrapper.__name__=func.__name__
        return func_wrapper
    return wrapper


def clock(func):
    @my_wrapper(func)
    def timer(*args,**kwargs):
        t0=time.time()
        res=func(*args,**kwargs)
        t1=time.time()
        print(f"{t1-t0} elapsed...")
        print('{}'.format(locals()))
        return res
    return timer

t=1
@functools.lru_cache(maxsize=1)
@clock
def greet(message):
    time.sleep(.123)

    print(f"hello {message}")

greet("Mrs.Elispthse")
