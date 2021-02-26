# Working With Regular Expressions

In this task, you will encounter and use the following

- Regular Expressions
- Testing (Unittest)

## Conventions / Coding Styles

- Notice that names of modules, methods, functions and variables are `snake_cased`, while names of classes are `PascalCased`
- Ensure to have two spaces exactly between import and actual codes in modules
- Ensure to be consistent with the usage of string quotes. Always use the single quote except in situations where you need to use double quotes

## About

This task deals with implementing functionalities for parsing email addresses. Parsing in this context simply means looking through email address strings to pick out important and useful information.

## Exercises

1. Create a branch named `implement-email-parser` and only work within this branch
2. Complete implementation and testing of the email parser
3. When done, push your changes and raise a pull request on Github using the pull request template already added to the project (`.github` folder)

## Approach

- Try to not attempt to conceptualize the whole documentation and codebase at once, instead move step by step through the task
- Ensure you go through the materials provided below before attempting the task
- Make sure you conceptualize all your effort on only the topic of the week (regular expression and unittest in python)
- Ensure to understand the problem before attempting to write any code
- Ensure to write the expected unit tests for you implementation.
- Ensure to manually experiment within the modules to confirm the results of your implementations

## Running Your Tests

```bash

Machine> cd <this-project-folder>

Machine> python -m unittest tests/test_email_parser.py

```

## Parsing Email Addresses

Email addresses are usually in the format: `username@domain`. Ex. `johndoe@gmail.com`, `jane+doe@yahoo.com`, etc. This means that there are two(2) useful information we will need out of email addresses, namely `username` and `domain`

Given the email address (`johndoe@gmail.com`), we will have the dictionary below as the output of parsing

```python

{
  'username': 'johndoe',
  'domain': 'gmail.com'
}

```

Also, given the email address (`jane+doe@yahoo.com`), we will have the dictionary below as the output of parsing

```python

{
  'username': 'jane+doe',
  'domain': 'yahoo.com'
}

```

When writing the logic for parsing email addresses, below are CONSTRAINTS you need to put into consideration

- Usernames will be made up of alphabets or alphanumerics. Ex. `john`, `johndoe`, `john123`. Note that usernames cannot start with a number
- Domains will always end in `.com`, Ex. `gmail.com`, `yahoo.com`, `bz2.com`, etc.
- The part before `.com` in domains will be made up of alphabets or alphanumerics, Ex. `gmail`, `bz2`, `dom555`, etc. Note that domains cannot start with a number
- Return `None` for emails that do not match the regex pattern

## Supporting Materials

Make sure you go through and understand the following materials

- ### 1. [Regular Expression](https://realpython.com/regex-python/)
  
- ### 2. [Unittest python](https://www.datacamp.com/community/tutorials/unit-testing-python)

- ### 3. [Testing](https://www.datacamp.com/community/tutorials/unit-testing-python) **only read unittest part**

***Note if you do not understand the concept in any of the materials you are free to do your research and make sure you are within the context of what to learn for the week***
