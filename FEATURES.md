# 🔐 Password Manager Features

## Authentication

- Create Master Password
- Secure Login Authentication
- SHA-256 Password Hashing
- Maximum 3 Login Attempts

---

## Password Management

### ➜ Add Password

- Unique Password ID
- Website Name
- Username
- Account Password
- Duplicate ID Validation

---

### ➜ View Passwords

Displays all saved passwords including:

- Password ID
- Website
- Username
- Account Password

---

### ➜ Search Password

Search a password using its Password ID.

Displays:

- Password ID
- Website
- Username
- Account Password

---

### ➜ Update Password

Update an existing password by Password ID.

Editable fields:

- Website
- Username
- Account Password

---

### ➜ Delete Password

Delete a saved password after confirmation.

- Confirmation before deletion
- Safe deletion from JSON file

---

## File Handling

- Automatic Loading of Password Data
- Automatic Saving of Password Data
- Creates a New Password Vault if File Doesn't Exist
- Handles Corrupted JSON Files Gracefully

---

## Input Validation

- Integer Validation
- Positive ID Validation
- Duplicate ID Checking
- Empty Input Validation
- Invalid Menu Choice Validation

---

## Error Handling

- FileNotFoundError
- JSONDecodeError
- ValueError

---

## Technologies Used

- Python
- JSON
- Hashlib (SHA-256)
- File Handling