
# File Integrity Monitoring System

## Aim
To develop a Python program that detects file modifications
using SHA-256 hashing.

## Description
The File Integrity Monitoring System checks whether files
have been modified, added, or deleted by comparing their
current hashes with a saved baseline.

## Technologies Used
- Python 3
- SHA-256 Hashing
- JSON

## Features
- Creates a file hash baseline.
- Detects modified files.
- Detects newly added files.
- Detects missing files.

## How to Run
1. Install Python 3.
2. Open Command Prompt in the project folder.
3. Create a folder named sample_files.
4. Create a sample file inside sample_files.
5. Create a baseline:

   python integrity_monitor.py baseline sample_files baseline.json

6. Check file integrity:

   python integrity_monitor.py check sample_files baseline.json

## Expected Output
PASS: No file changes detected.

If a file changes, the program reports MODIFIED.

## Security Benefits
- Helps identify unexpected file changes.
- Supports basic integrity verification.
- Uses SHA-256 cryptographic hashing.

## Limitations
This is an educational project. The baseline must be
protected from unauthorized changes.

## Result
The file integrity monitoring program can detect file
changes by comparing SHA-256 hashes.
