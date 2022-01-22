## 0x07.Python - Test-driven Development

<figure>
	<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/246/giphy-4.gif"
</figure>


### Learning Objectives

At the end of this project, you are expected to be able to explain to anyone without any help...

### General

- What’s an interactive test?
- Why tests are important?
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests?
- How to find edge cases

### Resources

* [doctest -- Test interactive Python examples](https://docs.python.org/3.4/library/doctest.html) - ((until “26.2.3.7. Warnings” included))
* [doctest -- Testing through documentation)](https://pymotw.com/3/doctest/)
* [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8() - Video Tutorial VT!

### Requirements

#### Python Scripts

- Allowed editors:`vi`, `vim` & `emacs`
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python4``
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 3.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

#### Python Test Cases

- Allowed editors:`vi`, `vim` & `emacs`
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/`
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)')`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!


#### Quiz

- Question #0

```
Is this a standardized way to comment a function in Python?

/* Addition function */
def add(a, b):
    return a + b

```

`No`

- **Question #1**

```
Is this a standardized way to comment a function in Python?

"""" Addition function """
def add(a, b):
    return a + b

```

`No`

- Question #2

```
Is this a standardized way to comment a function in Python?

 ##########
 # Addition function
 ##########
 def add(a, b):
    return a + b
```

`No`

- Question #3

```
 Is this a standardized way to comment a function in Python?

 def add(a, b):
    """ Addition function """
    return a + b
```

`Yes`

- Question #4

```
Is this module correctly commented?

 #!/usr/bin/python3
 """ 
    My calculation module
 """
 import sys
 ...

```

`Yes`

- Question #5

```
Is this module correctly commented?

 #!/usr/bin/python3
import sys

 """ 
    My calculation module
 """
 ...

```

`No`

```
Tips: Docstring must be before import statements
```

- Question #6

```
 Based on this code, what should all the test cases be? (select multiple)

 def uniq(list):
    """ Returns unique values of a list """
    u_list = []
    for item in list:
        if item not in u_list:
            u_list.append(item)
    return u_list


    empty list

    list with one element (any type)

    list with 2 different element (same type)

    list with twice the same element (same type)

    list with more than 2 times the same element (same type)

    list with multiple types (integer, string, etc…)

    not a list argument (ex: passing a dictionary to the method)

```




