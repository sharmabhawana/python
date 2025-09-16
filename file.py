Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> num1=123.456
>>> num1
123.456
>>> int(num1)
123
>>> num`
SyntaxError: invalid syntax
>>> num1
123.456
>>> num1=int("1234")
>>> num1
1234
>>> num1=int("123.34")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    num1=int("123.34")
ValueError: invalid literal for int() with base 10: '123.34'
>>> num1=int("A")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    num1=int("A")
ValueError: invalid literal for int() with base 10: 'A'
