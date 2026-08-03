# 🔐 Password Manager Features

## 🔑 Authentication

- Create a Master Password
- Secure Login Authentication
- Master Password protected using SHA-256 Hashing
- Maximum 3 Login Attempts
- Login Validation

---

## ➕ Add Password

Users can save account credentials by providing:

- Unique Password ID
- Website Name
- Username
- Account Password

### Validation

- Password ID must be an integer
- Password ID must be positive
- Duplicate Password IDs are not allowed
- Website cannot be empty
- Username cannot be empty
- Account Password cannot be empty

---

## 📋 View Passwords

Displays all saved passwords including:

- Password ID
- Website Name
- Username
- Account Password

---

## 🔍 Search Password

Search any saved password using its Password ID.

Displays:

- Password ID
- Website Name
- Username
- Account Password

### Validation

- Integer Validation
- Positive ID Validation
- Password Not Found Handling

---

## ✏️ Update Password

Update an existing password using its Password ID.

Editable Fields:

- Website Name
- Username
- Account Password

### Validation

- Integer Validation
- Positive ID Validation
- Password Existence Check
- Empty Input Validation

---

## 🗑️ Delete Password

Delete a saved password using its Password ID.

Features:

- Displays password details before deletion
- Confirmation before deleting
- Safe deletion from JSON file

### Validation

- Integer Validation
- Positive ID Validation
- Password Existence Check
- Deletion Confirmation (Y/N)

---

## 💾 File Handling

- Automatic Password Loading
- Automatic Password Saving
- Creates Password Vault if File Doesn't Exist
- Handles Corrupted JSON Files Gracefully

---

## ⚠️ Exception Handling

- FileNotFoundError
- JSONDecodeError
- ValueError

---

## ✅ Input Validation

- Integer Validation
- Positive Number Validation
- Duplicate ID Checking
- Empty Input Validation
- Invalid Menu Choice Validation
- Password Existence Validation

---

## 🛠️ Technologies Used

- Python 3
- PyCharm IDE
- JSON
- Hashlib (SHA-256)
- File Handling