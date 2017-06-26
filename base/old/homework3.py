import functools
import time


def log(text=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if isinstance(text, str):
                print("%s begin call %s" % (text, func.__name__))
            else:
                print("begin call %s" % func.__name__)
            func(*args, **kw)
            print("end call")
            return func

        return wrapper

    if isinstance(text, str):
        return decorator
    else:
        return decorator(text)


@log('executor')
def now(s):
    print(s + time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time())))


now("时间是：")


@log
def now2():
    print(time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time())))


now2()
