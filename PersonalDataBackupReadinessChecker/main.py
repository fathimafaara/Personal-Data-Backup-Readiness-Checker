from Modules.Scanner import scan_directory
import os
from Modules.Duplicate_Checker import find_duplicates
from Modules.Analyser import(find_large_files,
                             find_empty_folders,
                             calculate_storage_by_category,
                             calculate_backup_score,
                             check_file_organisation )
from Modules.Report_Generator import generate_report

print("-" * 45)
print("PERSONAL DATA BACKUP READINESS CHECKER")
print("-" *45)

print("\nWelcome to the Backup Readiness Checker!")

print("\nThis application helps you:")
print("\n01. Analyse your files and folders")
print("02. Identify duplicate files")
print("03. Check storage usage")
print("04. Detect empty folders")
print("05. Generate backup readiness reports")

print("\nLet's check your backup readiness!")
print("")

print("\nPlease enter the folder path you want to analyse: ")
while True:
    folder_path = input("Folder Path: ").strip().strip('"')
    if os.path.isdir(folder_path):
        print("\nValid folder Path!")
        break
    else:
        print("\nError: Invalid folder path. Please try again")
total_files, total_folders, total_size = scan_directory(folder_path)

print("-" * 45)
print("CHECKING FOR DUPLICATE FILES")
print("-" * 45)
duplicates = find_duplicates(folder_path)
if duplicates:
    print("Duplicate Files Found:")
    for file_path in duplicates:
        print(file_path)
else:
    print("No Duplicate Files Found")


print("")
print("-" * 45)
print("CHECKING FOR LARGE FILES")
print("-" * 45)
large_files = find_large_files(folder_path)
if large_files:
    print("Large Files Found:")
    for file in large_files:
        print("\nFile Name: " + file["name"])
        print("File Size: " , file["size"], "MB")
        print("File Path: " + file["path"])
else:
    print("No Large Files Found")

print("")
print("-" * 45)
print("CHECKING FOR EMPTY FOLDERS")
print("-" * 45)
empty_folders = find_empty_folders(folder_path)
if empty_folders:
    print("Empty Folders Found:")
    for folder in empty_folders:
        print(folder)
else:
    print("No Empty Folders Found")

print("")
print("-" * 45)
print("STORAGE USAGE BY CATEGORY")
print("-" * 45)
storage_report = calculate_storage_by_category(folder_path)
if storage_report:
    for category, size in storage_report.items():
        if size < 1024 * 1024:
            size_in_kb = size/1024
            print(category , ": " , round(size_in_kb,2) , " KB")
        else:
            size_in_MB = size / (1024 * 1024)
            print(category, ": " , round(size_in_MB, 2) , "MB")
else:
    print("No files available for storage analysis.")

print("")
print("-" * 45)
print("BACKUP READINESS ASSESSMENT")
print("-" * 45)
readiness_score = calculate_backup_score(folder_path)
organisation = check_file_organisation(folder_path)
print("Backup Readiness Score: ", readiness_score, "/ 100")
if readiness_score >= 80:
    print("Status: Excellent")
elif readiness_score >= 60:
    print("Status: Good")
elif readiness_score >= 40:
    print("Status: Need Improvement")
else:
    print("Status: Poor")

print("")
print("-" * 45)
print("GENERATING BACKUP REPORT")
print("-" * 45)
report_data = {
    "total_files": total_files,
    "total_folders": total_folders,
    "total_size": total_size,
    "readiness_score": readiness_score,
    "storage_report": storage_report,
    "duplicates": duplicates,
    "large_files": large_files,
    "empty_folders": empty_folders,
    "organisation": organisation }
report_path = generate_report(folder_path, report_data)
print("Report generated successfully!")
print("Report location:", report_path)
