
# Lab 5: Static Code Analysis
## Reflection

Note: The supplied three-page handout did not include the four reflection questions mentioned in the repository README. The following four questions and answers are drafted based on the lab objectives and work performed.

### 1. What is static code analysis, and why is it important?

Static code analysis is the process of examining source code without executing the program. It helps identify potential bugs, security vulnerabilities and coding-style violations.

In this lab, I used Pylint, Bandit and Flake8 to analyze the address book application. These tools helped identify problems before they could affect the program during execution.

### 2. What types of issues did you identify and fix during this lab?

I identified several issues in the original Python program.

Security issues included the use of the MD5 hashing algorithm, unsafe pickle deserialization, a hard-coded password and the use of the pickle module.

Code-quality issues included missing docstrings, inconsistent naming conventions, broad exception handling and missing file encoding specifications.

Formatting issues included missing whitespace, excessive blank lines and lines exceeding the recommended length.

I fixed these issues by using SHA-256, replacing pickle with JSON, removing the unused hard-coded password, improving exception handling, adding docstrings and following Python naming and formatting conventions.

### 3. How did Pylint, Bandit and Flake8 help improve the program?

Each tool helped identify a different category of problems.

- Pylint helped improve code quality, naming conventions, documentation and exception handling.
- Bandit identified security-related problems such as weak hashing and unsafe deserialization.
- Flake8 identified formatting violations and helped enforce consistent Python coding style.

Using all three tools provided a more complete analysis of the program.

### 4. What did you learn from this lab, and how does static analysis improve software development?

Through this lab, I learned how to create a Python virtual environment, install static analysis tools, interpret their reports and correct the identified issues.

I also learned that static analysis improves security, readability, maintainability and overall code quality.

After making the corrections, I tested the address book program and reran all three tools. The final Pylint score was 10.00/10, Bandit reported no security issues, and Flake8 reported no formatting violations.

This lab demonstrated the importance of regularly using static analysis tools during software development.
