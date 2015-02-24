# coding: utf-8
from functools import wraps

def tag(start, end):
    def decorator(fun_hello):
        @wraps(fun_hello)
        def inner(who):
            print "%s" % start
            fun_hello(who)
            print "%s" % end
        return inner
    return decorator

# TODO: class-based decorator


class MyDecorator(object):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, fn):
        @wraps(fn)
        def decorated(*args, **kwargs):
            print "{}".format(self.arg1)
            fn(*args, **kwargs)
            print "{}".format(self.arg2)
        return decorated


def main():
    @MyDecorator("Первый аргумент декоратора", 'Второй параметр декоратора')
    def hello(who):
        print "Hello", who

    def error_logger(decorated):
        @wraps(decorated)
        def decorator(*args, **kwargs):
            try:
                return decorated(*args, **kwargs)
            except:
                print "Ошибка в функции {}".format(decorated.__name__)
                pass
        return decorator

    @error_logger
    def a():
        l = range(10)
        print l[11]

if __name__ == "__main__":
    main()
