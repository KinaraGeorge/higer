# 0x03. Python - Data Structures: Lists, Tuples

## Resources

**Read or watch:**

- [3.1.3. Lists](https://docs.python.org/3.4/tutorial/introduction.html#lists)
- [Data structures](https://docs.python.org/3.4/tutorial/datastructures.html) (*until `5.3. Tuples and Sequences` included*)
- [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing
- What is sequence unpacking
- What is the `del` statement and how to use it

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

### C

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

## Quiz questions

<details>
<summary>Show</summary>
  
### Question #0

What do these lines print?

```
>>> a = [1, 2, 3, 4]
>>> a[0]
```

- [x] 1
- [ ] 2
- [ ] [1]
- [ ] [1, 2]
- [ ] [1, 2, 3, 4]

### Question #1

What do these lines print?

```
>>> a = [1, 2, 3, 4]
>>> a[-1]
```

- [ ] -1
- [ ] 2
- [x] 4
- [ ] [4, 3, 2, 1]

### Question #2

What do these lines print?

```
>>> a = [1, 2, 3, 4]
>>> a[-3]
```

- [ ] -3
- [ ] [4, 3]
- [x] 2

### Question #3

What do these lines print?

```
>>> a = [1, 2, 3, 4]
>>> len(a)
```

- [ ] 2
- [x] 4
- [ ] 6
- [ ] 8

### Question #4

What do these lines print?

```
>>> a = [1, 2, 3, 4]
>>> a.append(5)
>>> len(a)
```

- [ ] 2
- [x] 5
- [ ] 6

### Question #5

What do these lines print?

```
>>> a = [1, 2, 3, 4]
>>> a[1:3]
```

- [ ] [1, 2, 3]
- [ ] [1, 2]
- [x] [2, 3]

### Question #6

What do these lines print?

```
>>> a = [1, 2, 3, 4]
>>> a[2] = 10
>>> a
```

- [ ] [1, 2, 3, 4]
- [ ] [1, 10, 3, 4]
- [x] [1, 2, 10, 4]
- [ ] [1, 2, 10, 10]

### Question #7

What do these lines print?

```
>>> a = [1, 2, 3, 4]
>>> b = a
>>> b
```

- [x] [1, 2, 3, 4]
- [ ] [1]
- [ ] 1
- [ ] a

### Question #8

What do these lines print?

```
>>> a = [1, 2, 3, 4]
>>> b = a
>>> a[2] = 10
>>> a
```

- [ ] [1]
- [x] [1, 2, 10, 4]
- [ ] [1, 2, 3, 4]
- [ ] a
- [ ] b

### Question #9

What do these lines print?

```
>>> a = [1, 2, 3, 4]
>>> b = a
>>> a[2] = 10
>>> b
```

- [ ] [1]
- [x] [1, 2, 10, 4]
- [ ] [1, 2, 3, 4]
- [ ] a
- [ ] b

</details>

## Tasks

<details>
<summary>View Contents</summary>



</details>

## Author
### _Edgar Miguel Rodríguez G._

- **Github:** [Miguelro123](https://github.com/Miguelro123) 
- **Linkedin:** [Edgar Miguel Rodriguez Garcia](https://www.linkedin.com/in/edgar-miguel-rodriguez-garcia-20a5281a2/)
