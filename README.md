# Password-Generator

A custom Python script that generates a strong password, compliant with CISA's industry security standards while remaining simple to type. The purpose is to generate strong password sequences without sacrificing ease-of-use for end-users. It is designed to run for enterprise environments, or for personal use to quickly generate passwords on a terminal.

## Purpose

I built this script for my own help desk environment. One of our most frequent requests involves password resets. In certain cases, we need to manually create one ourselves and share it with the user having access issues. At my company, we have standard CISA compliant password policies, but in addition, we have certain preferences for how a password should be generated. They need to be compliant, but simple enough to type for users and prevent further technical difficulties.

My organization's password policy establishes:

- Minimum **12 characters**
- At least **1 uppercase** letter
- At least **1 lowercase** letter
- At least **1 digit** (0–9)
- At least **1 symbol**
- No **3 or more consecutive** letters or digits of the same type

While there are both online and offline tools that generate passwords, as a cybersecurity enthusiast, this felt like the perfect project to simultaneously train my Python coding and security awareness skills. In addition to wanting to practice Python, this was the natural language option for this kind of script. I needed something that could work cross-platform on any terminal – no GUI involved. Python's large collection of built-in modules made it the perfect tool for a script of this caliber.

It was built around two principles that directly support each other: minimal dependencies and offline availability. All modules used are part of the Python Standard Library. I wanted it to be as efficient and lightweight as possible, while maintaining a strong security posture. All you need to run this script is to have the latest version of Python and install the required modules.

Fewer dependencies mean little to no network calls; this script's online requirement is *zero*. The first response when a system is suspected of being infected with malware is to remove the machine from the network. For this reason, I've made offline capability a personal design standard. Any tool I build that does not require network connection, **should not** touch the network.

The last design principle is to facilitate the end-user's effort. The allowed symbol set is intentionally limited. Rather than drawing from every available special character, the script uses a curated list of 10 symbols that are visually distinct and easy to locate on a standard keyboard. This accounts for users who may have vision impairments or dyslexia, and avoids character combinations that are difficult to distinguish (e.g., `I|}`). Password length is also fixed at exactly 12 characters for the same reason: long enough to meet compliance and resist brute force, short enough that a non-technical user can type it without frustration.

The result is a security analyst's dream tool: compliant, offline, lightweight and designed with the end-user in mind. As long as you have the latest Python version and required modules installed, the script is run as soon as the file is on your machine.

## Password Policy

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

**re** — For regular expression matching. Used in `find_consecutives` to detect runs of 3 or more consecutive letters or digits. The pattern `r'[A-Za-z]{3,}|\d{3,}'` covers both cases in a single expression, keeping the check to a minimal footprint.

**pyperclip** — Third-party library for clipboard copy/paste. While removing it would reduce load time slightly, that gain is offset by the user having to manually copy the generated password — making the tradeoff not worth it.

## Global Variables

`alphabet = list(string.ascii_letters)`
A list containing the entire English alphabet in both lowercase and uppercase characters. Used as the source pool for all letter-based selections throughout the script.

`symbols = ["!", "@", "#", "$", "%", "&", "*", "?", "~", "/"]`
A curated list of 10 common symbols accepted by most password policies. Selecting from an explicit list avoids including symbols that some services reject (e.g. `<`, `>`, spaces).

## Functions

`number_generator(x)` — Returns a cryptographically secure random integer in the range `[0, x)` using `secrets.randbelow`. Used as the central source of randomness throughout the script.

`find_consecutives(s)` — Takes a string and returns `True` if it contains 3 or more consecutive letters (`[A-Za-z]{3,}`) or 3 or more consecutive digits (`\d{3,}`). Used to validate a generated password before returning it.

`scramble_sequence(string_item)` — Takes a string and returns a shuffled version of it. Builds the result by repeatedly picking a random index from the remaining characters and appending it — equivalent to a secure Fisher-Yates shuffle.

`generate_sequence()` — Orchestrates the full password generation pipeline: seeds the guaranteed character pool, pads it to 12 characters, scrambles it, and re-scrambles until `find_consecutives` returns `False`. Returns the final password string.

## Logs

07-02-2026: Removed the `pyperclip` module and function to make script fully offline capable, the only dependency is Python installed.

## License

MIT
