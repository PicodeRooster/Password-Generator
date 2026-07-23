# Password-Generator

A custom Python script that generates a strong password, compliant with CISA's industry security standards while remaining simple to type. The purpose is to generate strong password sequences without sacrificing ease-of-use for end-users. It is designed to run for enterprise environments, or for personal use to quickly generate passwords on a terminal.

## Purpose

I built this script for my own Help Desk environment. One of our most frequent requests involves password resets. In certain cases, we need to manually create a temporary one ourselves and share it with the user having access issues. At my company, we have standard CISA compliant password policies, but in addition, we have certain preferences for how a passwords should be generated. They need to meet policy while having simple-enough characters for users to type. Generating a password with these specifications prevents further technical difficulties. The quickest option is to use an online password generator, but I take issue with this. My #1 concern is that these tools are available <ins>online</ins>.

When a breach occurs, the first thing you need to do is to take the affected computer off the network. As a security enthusiast, I believe technicians should always have a set of offline tools available to them. This is a philosophy I follow when creating my scripts. If there is no need for the tool to touch the network, it should not touch the network. The second issue is that external tools do not know our password preferences. This leads to technicians manually verifying each generated password to ensure it is easy to type – a complete waste of time.

These problems led to creating my own password generator that follows company policy, follows our generation preferences and works completely offline. The result is a security analyst's dream tool: compliant, offline, lightweight and designed with the end-user in mind.

---

## Description

While there are both online and offline tools that generate passwords, as a cybersecurity enthusiast, this felt like the perfect project to simultaneously train my Python coding and security awareness skills. In addition to wanting to practice Python, this was the natural language option for this kind of script. I needed something that could work cross-platform on any terminal – no GUI involved. Python's large collection of built-in modules made it the perfect tool for a script of this caliber. It was built around two principles that directly support each other: minimal dependencies and offline availability. In the end, I created two nearly identical scripts with the only difference being one that includes a `pyperclip` function to copy the password to the clipboard.

**No Dependencies Version**
All modules used in this version are part of the Python Standard Library. I wanted it to be as efficient and lightweight as possible, while maintaining a strong security posture. All you need to run this script is to have the latest version of Python. No `pip install` needed.

Fewer dependencies mean little to no network calls; this script's online requirement is *zero*. 

**Pyperclip Version**
The only difference in this version is three lines of code: the `pyperclip` import statement, the pyperclip function, and the print statement that varies in wording slightly. This version sacrifices the "zero dependencies" philosophy for efficiency. It copies the generated password to the clipboard directly. If you install a single package, *then* this script becomes fully offline capable, it just doesn't meet the *fully* offline criteria because of that one module installation. Other than that, the script functions exactly the same as the first version. 

To install pyperclip:

```
pip install pyperclip
```

## Password Policy

Every generated password is guaranteed to have:

- Minimum **12 characters**
- At least **1 uppercase** letter
- At least **1 lowercase** letter
- At least **1 digit** (0–9)
- At least **2 symbols** from this list: `!`, `@`, `#`, `$`, `%`, `&`, `*`, `?`, `~`, `/`
- **No 3 or more consecutive** letters or digits of the same type
- Automatically **copied to clipboard** on generation

**Dev Note:** Most enterprise password policies require only 1 symbol, and this was my original design as well. After multiple tests, I realized an additional symbol made password strength scores the strongest on most scales. Therefore, my own policy is to include 2 symbols out of the set of characters listed. 

## Requirements

- Python 3.10+

## Usage

```
python3 password_generator.py
```

## How it works

### Character pools
- `alphabet`: all uppercase and lowercase ASCII letters.
  
- `symbols`: a fixed set of 10 special characters (`! @ # $ % & * ? ~ /`).

The allowed symbol set is intentionally limited. Rather than drawing from every available special character, the script uses a curated list of 10 symbols that are visually distinct and easy to locate on a standard keyboard. This accounts for users who may have vision impairments or dyslexia, and avoids character combinations that are difficult to distinguish (e.g., `I|}`). Password length is also fixed at exactly 12 characters for the same reason: long enough to meet compliance and resist brute force, short enough that a non-technical user can type it without frustration.


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
Calling `generate_sequence()` produces the password and prints to the console.

## Notes
- `password_list` contains a mix of `str` and `int` values (letters vs. digits), which is why `"".join(map(str, password_list))` is needed to build the final string.
- The password is printed to the console in plaintext. If installed the pyperclip version, it will also copy the password to the clipboard.

## Logs

 - **07-02-2026:** Removed the `pyperclip` module and function to make script fully offline capable, the only dependency is Python installed.
 - **07-22-2026:** Split `pyperclip` and no dependencies versions. Refactored versions to be nearly identical.

## License

MIT
