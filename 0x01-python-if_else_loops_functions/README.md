# 0x01. Python - if/else, loops, functions

## Resources

**Read or watch:**

- [More Control Flow Tools](https://docs.python.org/3.4/tutorial/controlflow.html) (Read until “4.6. Defining Functions” included)
- [Myths about Indentation](https://files.meetup.com/1544869/Python%20Indentation%20Myths.pdf)
- [IndentationError](https://www.youtube.com/watch?v=1QXOd2ZQs-Q)
- [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
- [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
- [Learn to Program 2 : Looping](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
- [PEP 8 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

**man or help:**

- python3

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- Why indentation is so important in Python
- How to use the `if`, `if ... else` statements
- How to use comments
- How to affect values to variables
- How to use the `while` and `for` loops
- How is Python’s `for` different from `C`‘s?
- How to use the `break` and `continues` statements
- How to use `else` clauses on loops
- What does the `pass` statement do, and when to use it
- How to use `range`
- What is a function and how do you use functions
- What does return a function that does not use any `return` statement
- Scope of variables
- What’s a traceback
- What are the arithmetic operators and how to use them

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

### C Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be compiled on Ubuntu 14.04 LTS
- Your programs and functions will be compiled with `gcc 4.8.4` using the flags `-Wall` `-Werror` `-Wextra` and `-pedantic`
- All your files should end with a new line
- Your code should use the `Betty` style. It will be checked using [betty-style.pl](https://github.com/holbertonschool/Betty/blob/master/betty-style.pl) and [betty-doc.pl](https://github.com/holbertonschool/Betty/blob/master/betty-doc.pl)
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the `main.c` files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own `main.c` files at compilation. Our `main.c` files might be different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called `lists.h`
- Don’t forget to push your header file
- All your header files should be include guarded

## More Info

*Note*: you do not need to understand lists yet.

## Quiz questions

<details>
<summary>Show</summary>
  
### Question #0

What do these lines print?

```
if True:
    print("Holberton")
else:
    print("School")
```

- [x] Holberton
- [ ] School

### Question #1

What do these lines print?

```
if 12 == 48/4:
    print("Holberton")
else:
    print("School")
```

- [x] Holberton
- [ ] School

### Question #2

What do these lines print?

```
if 12 == 48/4 and False:
    print("Holberton")
else:
    print("School")
```

- [ ] Holberton
- [x] School

### Question #3

What do these lines print?

```
if 12 == 48/3 or 12 is 12:
    print("Holberton")
else:
    print("School")
```

- [x] Holberton
- [ ] School

### Question #4

What do these lines print?

```
a = 12
if a > 2:
    if a % 2 == 0:
        print("Holberton")
    else:
        print("C is fun")
else:
    print("School")
```

- [x] Holberton
- [ ] C is fun
- [ ] School

### Question #5

What do these lines print?

```
a = 12
if a < 2:
    print("Holberton")
elif a % 2 == 0:
    print("C is fun")
else:
    print("School")
```

- [ ] Holberton
- [x] C is fun
- [ ] School

### Question #6

What do these lines print?

```
for i in range(4):
    print(i, end=" ")
```

- [ ] 1 2 3 4
- [ ] 1 2 3
- [x] 0 1 2 3
- [ ] 0 1 2 3 4

### Question #7

What do these lines print?

```
for i in range(2, 4):
    print(i, end=" ")
```

- [ ] 2 4
- [x] 2 3
- [ ] 2 3 4
- [ ] 3 4

### Question #8

What do these lines print?

```
for i in range(2, 10, 2):
    print(i, end=" ")
```

- [ ] 2 3 4 5 6 7 8 9 10
- [ ] 2 3 4 5 6 7 8 9
- [ ] 4 6 8 10 12 14 16 18
- [x] 2 4 6 8

</details>

## Tasks

<details>
<summary>View Contents</summary>



</details>

## Author
### _Edgar Miguel Rodríguez G._

- **Github:** [Miguelro123](https://github.com/Miguelro123) 
- **Linkedin:** [Edgar Miguel Rodriguez Garcia](https://www.linkedin.com/in/edgar-miguel-rodriguez-garcia-20a5281a2/)
