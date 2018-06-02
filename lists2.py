Python 3.7.0b4 (v3.7.0b4:eb96c37699, May  2 2018, 18:05:41) [MSC v.1913 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> my_list=['eunice',21.'kenyan']
SyntaxError: invalid syntax
>>> my_list=['eunice',21,'kenyan']
>>> print(my_list[1])
21
>>> print(my_list[4])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(my_list[4])
IndexError: list index out of range
>>> print(my_list[3])
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(my_list[3])
IndexError: list index out of range
>>> print(my_list[kenyan])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(my_list[kenyan])
NameError: name 'kenyan' is not defined
>>> print(my_list[5])
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(my_list[5])
IndexError: list index out of range
>>> my_list:append('Dandora')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    my_list:append('Dandora')
NameError: name 'append' is not defined
>>> my_list.append('Dandora')
>>> print(my_list)
['eunice', 21, 'kenyan', 'Dandora']
>>> 
clear
Traceback (most recent call last):
  File "<pyshell#10>", line 2, in <module>
    clear
NameError: name 'clear' is not defined
>>> git push list2
SyntaxError: invalid syntax
>>> git status
SyntaxError: invalid syntax
>>> 
