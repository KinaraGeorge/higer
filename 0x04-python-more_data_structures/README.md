# 0x04. Python - More Data Structures: Set, Dictionary

## Resources

**Read or watch:**

- [Data structures](https://docs.python.org/3.4/tutorial/datastructures.html)
- [Lambda, filter, reduce and map](https://www.python-course.eu/python3_lambda.php)
- [Learn to Program 12 Lambda Map Filter Reduce](https://www.youtube.com/watch?v=1GAC6KQUPeg)

**man or help:**

- `python3`

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- What are set and how to use them
- What are the most common methods of set and how to use them
- When to use sets versus lists
- How to iterate into a set
- What are dictionary and how to use them
- When to use dictionaries versus lists or sets
- What is a key in a dictionary
- How to iterate into a dictionary
- What is a lambda function
- What is map, reduce and map functions

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
>>> a = { 'id': 89, 'name': "John" }
>>> a['id']
```

- [ ] id
- [ ] ‘id’
- [ ] a[‘id’]
- [x] 89
- [ ] John

### Question #1

What do these lines print?

```
>>> a = { 'id': 89, 'name': "John" }
>>> a.get('id')
```

- [ ] id
- [ ] ‘id’
- [ ] a[‘id’]
- [x] 89
- [ ] John

### Question #2

What do these lines print?

```
>>> a = { 'id': 89, 'name': "John" }
>>> a.get('age')
```

- [ ] ‘age’
- [ ] Not found
- [ ] 89
- [ ] 12
- [x] Nothing

### Question #3

What do these lines print?

```
>>> a = { 'id': 89, 'name': "John" }
>>> a.get('age', 0)
```

- [ ] ‘age’
- [ ] Nothing
- [x] 0
- [ ] 89

### Question #4

What do these lines print?

```
>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
>>> a.get('projects')
```

- [ ] ‘projects’
- [x] [1, 2, 3, 4]
- [ ] [1]
- [ ] list
- [ ] Nothing

### Question #5

What do these lines print?

```
>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
>>> a.get('projects')[3]
```

- [x] 4
- [ ] [4]
- [ ] [1, 2, 3, 4]
- [ ] 3
- [ ] [3]

### Question #6

What do these lines print?

```
>>> a = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4], 'friends': [ { 'id': 82, 'name': "Bob" }, { 'id': 83, 'name': "Amy" } ] }
>>> a.get('friends')[-1].get("name")
```

- [ ] 89
- [ ] [ { ‘id’: 82, ‘name’: “Bob” }, { ‘id’: 83, ‘name’: “Amy” } ]
- [x] ‘Amy’
- [ ] ‘Bob’
- [ ] Nothing

### Question #7

What do these lines print?

```
>>> for i in range(0, 3):
>>>     print(i, end=" ")
```

- [ ] 1 2 3
- [ ] 0 1 2 3
- [x] 0 1 2

### Question #8

What do these lines print?

```
>>> for i in range(1, 4):
>>>     print(i, end=" ")
```

- [x] 1 2 3
- [ ] 0 1 2 3
- [ ] 1 2 3 4

### Question #9

What do these lines print?

```
>>> for i in [1, 2, 3, 4]:
>>>     print(i, end=" ")
```

- [ ] 0 1 2 3
- [ ] 0 1 2 3 5
- [ ] 1 2 3
- [x] 1 2 3 4

### Question #10

What do these lines print?

```
>>> for i in [1, 3, 4, 2]:
>>>     print(i, end=" ")
```

- [ ] 0 1 2 3
- [ ] 1 2 3 4
- [x] 1 3 4 2
- [ ] 1 3 4 2 0

### Question #11

What do these lines print?

```
>>> for i in ["Hello", "Holberton", "School", 98]:
>>>     print(i, end=" ")
```

- [ ] 0 1 2 3
- [ ] 1 2 3 4
- [x] Hello Holberton School 98

</details>

## Tasks

<details>
<summary>View Contents</summary>



</details>

## Author
### _Edgar Miguel Rodríguez G._

- **Github:** [Miguelro123](https://github.com/Miguelro123) 
- **Linkedin:** [Edgar Miguel Rodriguez Garcia](https://www.linkedin.com/in/edgar-miguel-rodriguez-garcia-20a5281a2/)
