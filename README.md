# Password-Generator #
Custom Python script that generates a strong passwords, compliant with most industries.

## Modules ##
I wanted to include the minimum requirement of dependencies to run an efficient script of this type.

**string** — Provides string constants and helpers. With `string.ascii_letters` I am able to map the entire alphabet both in uppercase and lowercase characters in a single list. This makes selecting random letters with different case sensitivities easily by finding a random index in the list that points to a letter.

**secrets** — For generating cryptographically secure random values. Python's official documentation recommends using this module for anything involving security credentials, as opposed to the simpler, but non-cryptographic `random` library. Some programs use both `secrets` and `random` to generate characters, but I found this unnecesary for my script. The `secrets` module does essentially the same function as `random`, but significantly more secure.

**re** — For regular expression matching and manipulation. I found this necessary to create the `find_consecutives` function to remove consecutive letters and numbers. I have yet to find a way to create a function like this without using another module. Using the **re** module seems to be the simplest approch to achieve this functionality in as little lines of code as possible. The imported module along with the function only takes up 3 lines of code, in its current state, whereas creating my own utility function may take up an excessive amount of lines that will slow down performance.

**pyperclip** — Third-party library/module. A single-module package for clipboard copy/paste. While removing it would reduce load time by roughly one second, that gain is immediately offset by the user having to manually copy the generated password, which takes longer than one second on average. In other words, the performance improvement comes at the cost of usability, making the tradeoff not worth it.

## Global Variables ##

`alphabet = list(string.ascii_letters)` 
A list containing the entire English library in both lowercase and uppercase characters. Allows the use of referencing the entire alphabet accross any point in the script.

`symbols = ["!", "@", "#", "$", "%", "&", "*", "?", "~", "/"]`
A list containing specic symbols that are easy to type and do not complicate the readability of the password. Since the `string` module was imported, it's important to mention that a similar effect can be achieved with `string.symbols` to create a list of ALL available symbols in the English language, similar to how the `alphabet` variable was created. I still opted to crete my own list of symbols as I did not want to include certain ones like commas, colons or semi-colons. In addition to being more difficult to read, these characters are not allowed to be used in many password input fields. Creating a custom list of symbols allows for easier control of the characters in the password sequence.

`password = generate_sequence()`
Final output variable to store the generated password.

## Functions ##
`number_generator()`
Utility function to generate a cryptographically secure random integer. It takes a single parameter as an integer to run `secrets.below(x)` where x is the max value in the desired range of numbers. It is a wrapper function to repeatedly call `secrets.below()` with improved readability. In other words, this function can be removed and replaced in all instances with `secrets.below(x)` if needed.  

`find_consecutives()`
A utility function using the re module to find consecutive sequences of numbers or letters. Using regular expressions, it searches the given string for 3 or more letters or digits appearing consecutively in any order, and returns a boolean value. It is called on the working password sequence to determine its strength. I attempted to create the same functionality by taking in a list as a parameter, but the simplest way to find consecutives in this situation is by using a string type.

`scramble_sequence()`
A utility function that takes a single string parameter and returns a randomly scrambled version of the input string. Used to shuffle the characters of the working password to improve its strength. It immediately converts the string to a list, then returns the scrambled sequence as a string. While the string→list→string conversion is admittedly roundabout, restricting the parameter to a string is a design choice for consistency with the rest of the pipeline, as the working password sequence must be passed to `find_consecutives()` as a string. Since strings in Python are immutable, converting to a list is necessary to assign each character an index and select a new position for it in the scrambled sequence. 

`generate_sequence()`
