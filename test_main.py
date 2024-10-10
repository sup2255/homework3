Python 3.12.6 (v3.12.6:a4a2d2b0d85, Sep  6 2024, 16:08:03) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pytest
... from main import main
... 
... def test_main(capsys, monkeypatch):
...     test_cases = [
...         (["main.py", "5", "3", "add"], "The result of 5.0 add 3.0 is equal to 8.0\n"),
...         (["main.py", "10", "2", "subtract"], "The result of 10.0 subtract 2.0 is equal to 8.0\n"),
...         (["main.py", "4", "5", "multiply"], "The result of 4.0 multiply 5.0 is equal to 20.0\n"),
...         (["main.py", "20", "4", "divide"], "The result of 20.0 divide 4.0 is equal to 5.0\n"),
...         (["main.py", "1", "0", "divide"], "An error occurred: Cannot divide by zero\n"),
...         (["main.py", "9", "3", "unknown"], "Unknown operation: unknown\n"),
...         (["main.py", "a", "3", "add"], "Invalid number input: a or 3 is not a valid number.\n"),
...         (["main.py", "5", "b", "subtract"], "Invalid number input: 5 or b is not a valid number.\n"),
...     ]
... 
...     for args, expected_output in test_cases:
...         monkeypatch.setattr(sys, 'argv', args)
...         main()
...         captured = capsys.readouterr()
