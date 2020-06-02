# 0x02. Python - import & modules

## Resources

**Read or watch:**

- [Modules](https://docs.python.org/3.4/tutorial/modules.html)
- [Command line arguments](https://docs.python.org/3.4/tutorial/stdlib.html#command-line-arguments)
- [PEP 8 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

**man or help:**

- `python3`

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

## Quiz questions

<details>
<summary>Show</summary>
  
### Question #0

What do these lines print?

```
>>> def my_function():
>>>     print("In my function")
>>> 
>>> my_function()
```

- [ ] “In my function”
- [x] In my function
- [ ] function my_function at …
- [ ] Nothing

### Question #1

What do these lines print?

```
>>> def my_function():
>>>     print("In my function")
>>> 
>>> my_function
```

- [ ] “In my function”
- [ ] In my function
- [x] function my_function at …
- [ ] Nothing

### Question #2

What do these lines print?

```
>>> def my_function(counter):
>>>     print("Counter: {}".format(counter))
>>> 
>>> my_function(12)
```

- [ ] Counter: counter
- [ ] Counter: c
- [x] Counter: 12

### Question #3

What do these lines print?

```
>>> def my_function(counter=89):
>>>     print("Counter: {}".format(counter))
>>> 
>>> my_function(12)
```

- [x] Counter: 12
- [ ] Counter: 89
- [ ] Counter: 101

### Question #4

What do these lines print?

```
>>> def my_function(counter=89):
>>>     print("Counter: {}".format(counter))
>>> 
>>> my_function()
```

- [ ] Counter: 12
- [x] Counter: 89
- [ ] Counter: 101

### Question #5

What do these lines print?

```
>>> def my_function(counter=89):
>>>     return counter + 1
>>> 
>>> print(my_function())
```

- [ ] 1
- [ ] 89
- [x] 90
- [ ] 891

</details>

## Tasks

<details>
<summary>View Contents</summary>



</details>

## Author
### _Edgar Miguel Rodríguez G._

- **Github:** [Miguelro123](https://github.com/Miguelro123) 
- **Linkedin:** [Edgar Miguel Rodriguez Garcia](https://www.linkedin.com/in/edgar-miguel-rodriguez-garcia-20a5281a2/)
