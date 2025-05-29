📁 exceptions/ – Custom Exceptions and Validation Utilities in Python
This directory contains educational and practical examples of custom exceptions, validation logic, and error handling techniques in Python.

📄 Included Files
Filename	Description
validators.py	Username and password validation logic using custom exceptions.
username_exceptions.py	Custom exception classes for validating usernames.
password_exceptions.py	Custom exception classes for validating passwords.
iterator_errors.py	Demonstrates use of __iter__, __next__, and handling StopIteration.
file_reading_with_try.py	Safe file reading using try-except-finally blocks.
custom_exception_underage.py	Example of raising and catching a custom exception (UnderAge).
__init__.py	Module initializer for importing the exceptions as a package.

✅ How to Use
You can run each file independently for demo purposes.

Example: Running the validator
bash
Copy
Edit
python validators.py
Expected output will include messages such as:

csharp
Copy
Edit
The username 1 is too short.
The password 2 is too short.
...
Ok
Example: Using UnderAge exception
bash
Copy
Edit
python custom_exception_underage.py
Output:

pgsql
Copy
Edit
Function Expected positive integer, and instead got 17.
You should send an invite to name
🧠 Highlights and Learning Points
✅ Modular Design: Each exception is split into logical modules (username, password, etc.)

🔐 Strong Validation: Includes pattern matching using re, character checks, and full password policies.

📚 Educational Use: Good examples of exception inheritance, override of __str__, and try-except structures.

♻️ Reusable Code: You can import these classes into other projects.

🛠️ Tech Notes
All filenames are lowercase and use underscores (PEP8).

Classes use CamelCase, and exception classes inherit from Python's Exception.

Regex-based character validation for username.

Password validation includes uppercase, lowercase, digit, special character requirements, and length boundaries.

📦 Example Folder Usage as a Module
If you want to import this as a module:

python
Copy
Edit
from exceptions.validators import check_input
You may need to include the folder in your PYTHONPATH or use relative imports if integrated in a larger project.

✍️ Suggestions for Further Enhancement
 Add tests/ folder with unittest or pytest tests.

 Support multi-language exception messages (i18n).

 Expand validators.py to support email and phone validation.

 Add logging for invalid input attempts.

