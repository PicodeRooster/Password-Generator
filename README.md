# Password-Generator

A custom Python script that generates a strong password, compliant with CISA's industry security standards while remaining simple to type. The purpose is to generate strong password sequences without sacrificing ease-of-use for end-users. It is designed to run for enterprise environments, or for personal use to quickly generate them on a terminal.

## Purpose

I built this script for my own Help Desk environment. One of our most frequent requests involves password resets. In certain cases, we need to manually create one ourselves and share it with the user having access issues. At my company, we have standard CISA compliant password policies, but in addition, we have certain preferences for how a password should be generated. They need to meet policy while having simple-enough characters for users to type. Generating a password with these specifications prevents further technical difficulties. The options are to use online password generators, but I have issues with these. My #1 problem is that it is <ins>online</ins>. When a breach happens on a computer, the first thing you need to do is take that computer offline. This is a philosophy I follow with all my scripts when possible, so I wanted to create my own password generator that follows company policy and works completely offline. Creating a tool that runs on a terminal was the natural design choice. 

The last design principle is to facilitate the end-user's effort. The allowed symbol set is intentionally limited. Rather than drawing from every available special character, the script uses a curated list of 10 symbols that are visually distinct and easy to locate on a standard keyboard. This accounts for users who may have vision impairments or dyslexia, and avoids character combinations that are difficult to distinguish (e.g., `I|}`). Password length is also fixed at exactly 12 characters for the same reason: long enough to meet compliance and resist brute force, short enough that a non-technical user can type it without frustration.

The result is a security analyst's dream tool: compliant, offline, lightweight and designed with the end-user in mind.

---

## Description

While there are both online and offline tools that generate passwords, as a cybersecurity enthusiast, this felt like the perfect project to simultaneously train my Python coding and security awareness skills. In addition to wanting to practice Python, this was the natural language option for this kind of script. I needed something that could work cross-platform on any terminal – no GUI involved. Python's large collection of built-in modules made it the perfect tool for a script of this caliber. It was built around two principles that directly support each other: minimal dependencies and offline availability. In the end, I created two nearly identical scripts with the only difference being one that includes a `pyperclip` function to copy the password to the clipboard.

**No Dependencies Version**
All modules used in this version are part of the Python Standard Library. I wanted it to be as efficient and lightweight as possible, while maintaining a strong security posture. All you need to run this script is to have the latest version of Python. No `pip install` needed.
Fewer dependencies mean little to no network calls; this script's online requirement is *zero*. Any tool I build that does not require network connection, **should not** touch the network.

**Pyperclip Version**
The only difference in this version is three lines of code: the `pyperclip` import statement, the pyperclip function, and the print statement varies in wording slightly. This version sacrifices the zero dependencies philosophy for efficiency. It copies the generated password to the clipboard directly. If you install a single package, *then* this script becomes fully offline capable, it's just doesn't meet the *fully* offline criteria because of that one module installation. Other than that, the script functions exactly the same as the No Dependencies Version. 

 
## Password Policy

My organization's password policy establishes:

- Minimum **12 characters**
- At least **1 uppercase** letter
- At least **1 lowercase** letter
- At least **1 digit** (0–9)
- At least **1 symbol**
- No **3 or more consecutive** letters or digits of the same type

I took this same model with one caveat:

Every generated password is guaranteed to have:

- Minimum **12 characters**
- At least **1 uppercase** letter
- At least **1 lowercase** letter
- At least **1 digit** (0–9)
- At least **2 symbols** (`!`, `@`, `#`, `$`, `%`, `&`, `*`, `?`, `~`, `/`)
- **No 3 or more consecutive** letters or digits of the same type
- Automatically **copied to clipboard** on generation


## Requirements

- Python 3.10+

## Usage
```
python password_generator.py
```

---OR---

```
python3 password_generator.py
```

The password is printed to the terminal and copied to your clipboard automatically.

## How It Works

1. **Seed guaranteed characters** — a pool is built with at least 1 uppercase letter, 1 lowercase letter, 1 digit, and 2 symbols to satisfy the minimum policy requirements.
2. **Pad to 12 characters** — the pool is filled with random letters or digits until it reaches 12 characters.
3. **Scramble** — the pool is shuffled using a cryptographically secure random index pick-and-remove loop (`scramble_sequence`).
4. **Validate** — if the result contains 3 or more consecutive letters or digits, it is re-scrambled until the check passes (`find_consecutives`).

In the first iteration of the script, I only included 1 symbol, aligning with my own organization's requirements. After multiple tests, however, I noticed it consistently scored one point below maximum on many password strength estimators. Increasing the sequence to require 2 symbols reliably pushed the score to the highest entropy rating across platforms, without meaningfully affecting typing difficulty.

## Modules

**string** — Provides string constants and helpers. With `string.ascii_letters` the entire English alphabet is mapped in both uppercase and lowercase into a single list, making random letter selection with controlled case sensitivity straightforward.

**secrets** — For generating cryptographically secure random values. Python's official documentation recommends using this module for anything involving security credentials, as opposed to the simpler but non-cryptographic `random` library. `secrets` provides the same functionality as `random` but is significantly more secure.

**pyperclip** — Third-party library for clipboard copy/paste. While removing it would reduce load time slightly, that gain is offset by the user having to manually copy the generated password.

## Global Variables

`alphabet = list(string.ascii_letters)`
A list containing the entire English alphabet in both lowercase and uppercase characters. Used as the source pool for all letter-based selections throughout the script.

`symbols = ["!", "@", "#", "$", "%", "&", "*", "?", "~", "/"]`
A curated list of 10 common symbols accepted by most password policies. Selecting from an explicit list avoids including symbols that some services reject (e.g. `<`, `>`, spaces).

## Functions

`number_generator(x)` — Returns a cryptographically secure random integer in the range `[0, x)` using `secrets.randbelow`. Used as the central source of randomness throughout the script.

`generate_sequence()` — Orchestrates the full password generation pipeline: seeds the guaranteed character pool, pads it to 12 characters, scrambles it and returns the final password string.

`patch_sequence()` — Patches sequenced numbers and letters, swapping their place one for the other.

# Password Generator

A script that generates a cryptographically secure 12-character password, copies it to the clipboard, and prints it.

## How it works

### Character pools
- `alphabet`: all uppercase and lowercase ASCII letters.
- `symbols`: a fixed set of 10 special characters (`! @ # $ % & * ? ~ /`).

### `number_generator(x)`
Returns a cryptographically secure random integer in `[0, x)` using `secrets.randbelow`, instead of the non-secure `random` module.

### `find_consecutives(s)`
Returns `True` if the string contains 3 or more consecutive letters, or 3 or more consecutive digits, in a row. Used as a quality check to reject passwords with predictable runs.

### `scramble_sequence(string_item)`
Manually shuffles a string using a Fisher-Yates-style approach: repeatedly picks a random remaining character and moves it into the output, until none are left. Equivalent to `random.shuffle`, but built on `secrets` for cryptographic security.

### `generate_sequence()`
Builds the final password in three stages:

1. **Guarantee character variety** — seeds the list with 1 uppercase letter, 1 lowercase letter, 1 digit, and 2 symbols (5 required characters).
2. **Fill to 12 characters** — a loop flips a random coin each iteration to add either a random letter or a random digit until the list has 12 elements.
3. **Scramble and validate** — joins the list into a string, shuffles it with `scramble_sequence`, and re-shuffles (from the same unscrambled character set) until `find_consecutives` returns `False`, guaranteeing no runs of 3+ letters or 3+ digits.

### Script execution
Calling `generate_sequence()` produces the password, which is copied to the clipboard via `pyperclip.copy()` and printed to the console.

## Notes
- `password_list` contains a mix of `str` and `int` values (letters vs. digits), which is why `"".join(map(str, password_list))` is needed to build the final string.
- The password is printed to the console in plaintext after being copied — worth considering if console output could be logged or exposed elsewhere.





## Logs

 - **07-02-2026:** Removed the `pyperclip` module and function to make script fully offline capable, the only dependency is Python installed.
 - **07-22-2026:** Split `pyperclip` and no dependencies versions. Refactored versions to be nearly identical.

## License

MIT
