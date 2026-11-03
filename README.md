# Personal-Data-Backup-Readiness-Checker

A Python-based tool designed to analyse directories, identify file management issues, monitor storage usage, and assess backup readiness.

Project Overview

The Personal Data Backup Readiness Checker scans a selected directory and provides useful information about files, storage usage, duplicates, and file organisation. It also generates a backup readiness report.

Key Features

- Directory Scanning – Scans folders and calculates total files, folders, and storage usage.
- File Categorisation – Categorises files based on their extensions.
- Duplicate Detection – Identifies duplicate files using SHA-256 hashing.
- Large File Detection – Finds files larger than a specified size.
- Empty Folder Detection – Identifies empty directories.
- Storage Analysis – Calculates storage usage by file category.
- Backup Readiness Score – Calculates a custom score based on file management checks.
- File Organisation Analysis – Evaluates how well files are organised.
- Report Generation – Generates a TXT report containing the analysis results.

Technologies Used

- Python
- PyCharm
- Git
- GitHub
- SHA-256 Hashing

Project Structure

PersonalDataBackupReadinessChecker/
│
├── Modules/
│   ├── Analyser.py
│   ├── Duplicate_Checker.py
│   ├── Report_Generator.py
│   └── Scanner.py
│
├── Reports/
├── Test_Data/
├── main.py
├── README.md
└── .gitignore

How to Run

1. Clone or download this repository.
2. Open the project in PyCharm.
3. Run "main.py".
4. Enter the directory path you want to analyse.
5. View the analysis results.
6. Find the generated TXT report in the Reports folder.

Safety

- Files are scanned without deleting or modifying them.
- SHA-256 hashing is used for duplicate detection.
- Reports are generated locally.

Future Improvements

- Cloud storage integration.
- Automated backup functionality.
- Advanced storage monitoring.
- Additional security features.

Author

Fathima Faara

Aspiring Cloud Engineer | Cloud Computing & Networking | Python | Software Development
