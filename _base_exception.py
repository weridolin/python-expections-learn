# -*- encoding: utf-8 -*-



class BaseException(object):
    """ Common base class for all exceptions """
    def with_traceback(self, tb): # real signature unknown; restored from __doc__
        """
        Exception.with_traceback(tb) --
            set self.__traceback__ to tb and return self.
        """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    args = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __cause__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception cause"""

    __context__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception context"""

    __suppress_context__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __traceback__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'__repr__': <slot wrapper '__repr__' of 'BaseException' objects>, '__str__': <slot wrapper '__str__' of 'BaseException' objects>, '__getattribute__': <slot wrapper '__getattribute__' of 'BaseException' objects>, '__setattr__': <slot wrapper '__setattr__' of 'BaseException' objects>, '__delattr__': <slot wrapper '__delattr__' of 'BaseException' objects>, '__init__': <slot wrapper '__init__' of 'BaseException' objects>, '__new__': <built-in method __new__ of type object at 0x00007FFC49400810>, '__reduce__': <method '__reduce__' of 'BaseException' objects>, '__setstate__': <method '__setstate__' of 'BaseException' objects>, 'with_traceback': <method 'with_traceback' of 'BaseException' objects>, '__suppress_context__': <member '__suppress_context__' of 'BaseException' objects>, '__dict__': <attribute '__dict__' of 'BaseException' objects>, 'args': <attribute 'args' of 'BaseException' objects>, '__traceback__': <attribute '__traceback__' of 'BaseException' objects>, '__context__': <attribute '__context__' of 'BaseException' objects>, '__cause__': <attribute '__cause__' of 'BaseException' objects>, '__doc__': 'Common base class for all exceptions'})"



# __context__ :当在except子异常或finally子异常中引发(或重新引发)异常时，(既有多个try)
# __context__ 被自动设置为捕获的最后一个异常;如果没有处理新的异常，最终显示的回溯将包括最初的异常和最终的异常


# try:
#     try:
#         raise ValueError("ValueError")
#     except ValueError as first:
#         raise TypeError("TypeError") from first
# except TypeError as second:
#     print("The exception was", repr(second))
#     print("Its __context__ was", repr(second.__context__))
#     print("Its __cause__ was", repr(second.__cause__))
#
# The exception was TypeError('TypeError')
# Its __context__ was ValueError('ValueError')
# Its __cause__ was ValueError('ValueError')


## 必须要有raise from
## context 为raise from 的 excepton

# try:
#     try:
#         raise AttributeError("1")
#     except Exception as e1:
#         raise  AttributeError from e1
# except AttributeError as exc_1:
#     print("context::",repr(exc_1.__context__))
#     print("cause::",repr(exc_1.__cause__))

    # AttributeError 是raise from e1 即context,cause为 e1
    # print("context::",repr(exc_1.__context__))
    # print("cause::",repr(exc_1.__cause__))

# try:
#     try:
#         try:
#             raise AttributeError("1")
#         except Exception as e1:
#             raise  AttributeError("2") from e1
#     except AttributeError as e2:
#         print("context::",repr(e2.__context__))
#         print("cause::",repr(e2.__cause__))
#         # context:: AttributeError('1')
#         # cause:: AttributeError('1')
#         raise AttributeError("3") from e2
# except AttributeError as e3:
#     print("context::", repr(e3.__context__))
#     print("cause::", repr(e3.__cause__))
    # context:: AttributeError('2')
    # cause:: AttributeError('2')


# with_traceback(tb)

# This method sets tb as the new traceback for the exception and returns the exception object.
# 即设置异常 的trackback

# try:
#     raise AttributeError("1")
# except AttributeError as exc:
#     import sys
#     tb = sys.exc_info()[2]
#     raise AttributeError("2")

# Traceback (most recent call last):
#   File "F:/PYTHON_CODE/python-expections-learn/_base_exception.py", line 125, in <module>
#     raise AttributeError("1")
# AttributeError: 1
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
#   File "F:/PYTHON_CODE/python-expections-learn/_base_exception.py", line 129, in <module>
#     raise AttributeError("2")
# AttributeError: 2


# try:
#     raise AttributeError("1")
# except AttributeError as exc:
#     import sys
#     tb = sys.exc_info()[2]
#     raise AttributeError("2").with_traceback(tb)

# Traceback (most recent call last):
#   File "F:/PYTHON_CODE/python-expections-learn/_base_exception.py", line 125, in <module>
#     raise AttributeError("1")
# AttributeError: 1
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
#   File "F:/PYTHON_CODE/python-expections-learn/_base_exception.py", line 129, in <module>
#     raise AttributeError("2").with_traceback(tb)
#   File "F:/PYTHON_CODE/python-expections-learn/_base_exception.py", line 125, in <module>
#     raise AttributeError("1")
# AttributeError: 2

try:
    try:
        raise AttributeError("1")
    except AttributeError as exc1:
        raise AttributeError("2")
except AttributeError as exc2:
    import sys
    tb = sys.exc_info()[2]
    raise AttributeError("3").with_traceback(tb)

# Traceback (most recent call last):
#   File "F:/PYTHON_CODE/python-expections-learn/_base_exception.py", line 173, in <module>
#     raise AttributeError("3").with_traceback(tb)
#   File "F:/PYTHON_CODE/python-expections-learn/_base_exception.py", line 169, in <module>
#     raise AttributeError("2") from exc1
# AttributeError: 3
