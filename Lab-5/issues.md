
# Lab 5: Static Code Analysis
## Issue Identification and Documentation

The following issues were identified using Pylint, Bandit and Flake8 before modifying the original address_book.py program.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Weak MD5 hash | Security - High | 19 | MD5 is a weak hashing algorithm and is not recommended for security-sensitive hashing. | Replaced MD5 with SHA-256. |
| Unsafe pickle deserialization | Security - Medium | 67 | pickle.load() can execute malicious code when restoring untrusted data. | Replaced pickle deserialization with json.load(). |
| Broad exception handling | Bug / Code Quality | 34 | except Exception catches a wide range of errors, making debugging difficult. | Replaced it with except KeyError to handle missing contacts specifically. |
| Hard-coded password | Security - Low | 6 | A password-like string was directly stored in the source code. | Removed the unused SYNC_PASSWORD constant. |
| Unsafe pickle module import | Security - Low | 3 | Importing pickle introduces an unsafe deserialization mechanism when used with untrusted data. | Removed pickle and used the JSON module. |
| Missing docstrings | Code Quality | 1, 10, 18, 22, 30, 39, 47, 53, 60, 65, 70 | The module and functions lacked documentation explaining their purpose. | Added module-level and function-level docstrings. |
| Invalid naming convention | Code Style | 10, 18, 22, 30, 39, 47, 53, 60, 65 | Function and argument names did not follow Python snake_case conventions. | Renamed functions and arguments using snake_case. |
| Missing file encoding | Code Quality | 54 | The CSV file was opened without explicitly specifying its encoding. | Added encoding="utf-8". |
| Inefficient loop | Code Quality | 49 | Used range(len(names)) instead of directly accessing elements with enumerate(). | Replaced the loop with enumerate(names, start=1). |
| Whitespace around operator | Formatting | 23 | Missing whitespace around an assignment operator. | Added appropriate spaces around the operator. |
| Incorrect blank lines | Formatting | 47 | Too many blank lines between functions. | Corrected the spacing to two blank lines. |
| Missing blank line | Formatting | 63 | Only one blank line existed between top-level functions. | Added the required second blank line. |
| Missing whitespace after comma | Formatting | 84 | A comma was not followed by a space. | Added appropriate whitespace. |
| Line too long | Formatting | 85 | A line exceeded the 79-character limit. | Split the statement into multiple lines. |

## Conclusion

The identified security, code quality and formatting issues were corrected. The program was tested again using all three static analysis tools.

Final results:
- Bandit: No security issues identified.
- Flake8: No formatting violations.
- Pylint: 10.00/10.

The corrected program continues to perform its address book operations, including adding contacts, searching, updating cities, exporting CSV data and backing up and restoring contacts using JSON.
