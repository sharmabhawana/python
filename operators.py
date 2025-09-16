Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
num1=12.3
int(num1)
12
int("1234")
1234
int("123.45")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("123.45")
ValueError: invalid literal for int() with base 10: '123.45'
num=0b101
num
5


>>> int("ob101")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    int("ob101")
ValueError: invalid literal for int() with base 10: 'ob101'
>>> int("ob101",2)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    int("ob101",2)
ValueError: invalid literal for int() with base 2: 'ob101'
>>> int("0b101",2)
5
>>> int("0o101",8)
65
>>> int("0xF",16)
15
>>> str(123)
'123'
>>> float(123)
123.0
>>> num1=1000
>>> num2="1000"
>>> num1+int(num2)
2000
>>> str(num1)+num2
'10001000'
>>> 
>>> eval("123")
123
>>> eval("123.45")
123.45
>>> eval("'name'")
'name'
>>> name=123
>>> eval("name")
123
>>> eval("12*6+7//3")
74
>>> 
===================================================================== RESTART: C:/pyon 3.13/arithmetic operators.py ====================================================================
sum= 14
sub= 6
pro= 40
div= 2.5
flor division= 2
mod= 2
exp= 10000
