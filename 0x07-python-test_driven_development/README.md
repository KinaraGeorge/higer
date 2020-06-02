# 0x07. Python - Test-driven development

## Background Context

### Important notice on intranet checks for Python projects

Starting from today:

- Based on the requirements of each task, **you should always write the documentation (module(s) + function(s)) and tests first**, before you actually code anything
- The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case. **But not in the implementation of them!**
- **Don’t trust the user**, always think about all possible edge cases

## Resources

**Read or watch:**

- [doctest — Test interactive Python examples](https://docs.python.org/3.4/library/doctest.html) (until “26.2.3.7. Warnings” included)
- [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
- [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- What’s an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

## Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Python Test Cases

- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Quiz questions

<details>
<summary>Show</summary>
  
### Question #0

Is this a standardized way to comment a function in Python?

```
/* Addition function */
def add(a, b):
    return a + b
```

- [ ] Yes
- [x] No

# Question #1

Is this a standardized way to comment a function in Python?

```
"""" Addition function """
def add(a, b):
    return a + b
```

- [ ] Yes
- [x] No

### Question #2

Is this a standardized way to comment a function in Python?

```
##########
# Addition function
##########
def add(a, b):
    return a + b
```

- [ ] Yes
- [x] No

### Question #3

Is this a standardized way to comment a function in Python?

```
def add(a, b):
    """ Addition function """
    return a + b
```

- [x] Yes
- [ ] No

### Question #4

Is this module correctly commented?

```
#!/usr/bin/python3
""" 
    My calculation module
"""
import sys
...
```

- [x] Yes
- [ ] No

### Question #5

Is this module correctly commented?

```
#!/usr/bin/python3
import sys

""" 
    My calculation module
"""
...
```

- [ ] Yes
- [x] No

```
**Tips:**
Docstring must be before import statements
```

### Question #6

Based on this code, what should all the test cases be? (select multiple)

```
def uniq(list):
    """ Returns unique values of a list """
    u_list = []
    for item in list:
        if item not in u_list:
            u_list.append(item)
    return u_list
```

- [x] empty list
- [x] list with one element (any type)
- [x] list with 2 different element (same type)
- [x] list with twice the same element (same type)
- [x] list with more than 2 times the same element (same type)
- [x] list with multiple types (integer, string, etc…)
- [x] not a list argument (ex: passing a dictionary to the method)

</details>

## Tasks

<details>
<summary>View Contents</summary>



</details>

## Author
### _Edgar Miguel Rodríguez G._

- **Github:** [Miguelro123](https://github.com/Miguelro123) 
- **Linkedin:** [Edgar Miguel Rodriguez Garcia](https://www.linkedin.com/in/edgar-miguel-rodriguez-garcia-20a5281a2/)
