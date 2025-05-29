# 📁 exceptions/ – Custom Exceptions and Validation Utilities in Python

This directory contains educational and practical examples of **custom exceptions**, **validation logic**, and **error handling techniques** in Python.

---

## 📄 Included Files 🗂️

| Description | Filename |
|-------------|----------|
| Username and password validation logic using custom exceptions. | `validators.py` |
| Custom exception classes for validating usernames. | `username_exceptions.py` |
| Custom exception classes for validating passwords. | `password_exceptions.py` |
| Demonstrates use of `__iter__`, `__next__`, and handling `StopIteration`. | `iterator_errors.py` |
| Safe file reading using `try-except-finally` blocks. | `file_reading_with_try.py` |
| Example of raising and catching a custom exception (`UnderAge`). | `custom_exception_underage.py` |
| Module initializer for importing the exceptions as a package. | `__init__.py` |

---

## ✅ How to Use

You can run each file independently for demo purposes.

### ▶️ Example: Running the validator

```bash
python validators.py

Expected output will include messages such as:

The username 1 is too short.
The password 2 is too short.
...
Ok



Expected output will include messages such as:

text
Copy
Edit
The username 1 is too short.
The password 2 is too short.
...
Ok
🛠️ Tech Notes
All files are lowercase with underscores (snake_case) – consistent with PEP8.

Classes use CamelCase and inherit from Exception.

Username is validated via regex; passwords must meet strength criteria.

Includes examples of raising, catching, and customizing exceptions.

✍️ Suggestions for Improvement
 Add unit tests (pytest / unittest)

 Support for more input types (email, phone, etc.)

 Add a logger or audit trail

 Add i18n support (multi-language error messages)

yaml
Copy
Edit

---

### הסברים:

| תיאור | הסבר |
|-------|------|
| `#` | כותרת ראשית |
| `##` | כותרת משנית |
| טבלאות עם `|` | תואם ל־GitHub Markdown ומוצג יפה |
| קוד עם שלוש backticks (```) | כך מוסיפים בלוקים של קוד (`bash`, `text`, `python`) |
| אימוג'ים (אופציונלי) | מוסיפים עיצוב ידידותי |

---

### 🧪 בדיקה

כדי לבדוק את התוצאה:
1. שמור את הקובץ כ־`README.md`.
2. העלה אותו לגיטב בפרויקט הרלוונטי.
3. פתח את הדף הראשי של הריפוזיטורי – התצוגה תופיע מעוצבת אוטומטית.

---

רוצה שאכין לך את זה בקובץ מוכן להורדה? או להוסיף גם גרסה בעברית/דו-לשונית?












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

