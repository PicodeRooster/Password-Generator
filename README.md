# Password-Generator
Custom Python script that generates a strong passwords, compliant with most industries. 

## Modules
I wanted to include the minimum requirement of dependencies to run an efficient script of this type.

**string** — Provides string constants and helpers. With `string.ascii_letters` I am able to map the entire alphabet both in uppercase and lowercase characters in a single list. This makes selecting random letters with different case sensitivities easily by finding a random index in the list that points to a letter. 

**secrets** — For generating cryptographically secure random values. Python's official documentation recommends using this module for anything involving security credentials, as opposed to the simpler, but non-cryptographic **random** library. Some programs use both **secrets** and **random** to generate characters, but I found this unnecesary for my script. The **secrets** module does essentially the same function as random, but significantly more secure. 

**re** — For regular expression matching and manipulation. I found this necessary to create the `find_consecutives` function to remove consecutive letters and numbers. I have yet to find a way to create a function like this without using another module. Using the **re** module seems to be the simplest approch to achieve this functionality in as little lines of code as possible. The imported module along with the function only takes up 3 lines of code, in its current state, whereas creating my own utility function may take up an excessive amount of lines that will slow down performance. 

**pyperclip** — Third-party library/module. A single-module package for clipboard copy/paste. While removing it would reduce load time by roughly one second, that gain is immediately offset by the user having to manually copy the generated password, which takes longer than one second on average. In other words, the performance improvement comes at the cost of usability, making the tradeoff not worth it.

## Global Variables
`alphabet = list(string.ascii_letters)`
A list containing the entire English library in both lowercase and uppercase characters. Allows the use of referencing the entire alphabet accross any point in the script. 

`symbols = ["!", "@", "#", "$", "%", "&", "*", "?", "~", "/"]`

