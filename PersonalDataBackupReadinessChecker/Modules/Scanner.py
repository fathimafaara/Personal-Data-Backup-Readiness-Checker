import os
from Modules.Analyser import categorize_files

def scan_directory(folder_path):
    total_files = 0
    total_folders = 0
    total_size = 0

    print("-" * 45)
    print("Scanning Directory")
    print("-" * 45)
    for root, folders, files in os.walk(folder_path):
        total_folders += len(folders)
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
            except OSError:
                print("Warning: Could not access file:", file)
                continue
            total_files += 1
            total_size += file_size
            extension = os.path.splitext(file)[1]
            category = categorize_files(file)
            print("File Name: ",file)
            print("File Type:",extension if extension else "No Extension")
            print("Category:",category)
            print("File Size:", round(file_size/1024/1024,2),"KB")
            print("")

    print("-" * 45)
    print("SCAN SUMMARY")
    print("-" * 45)

    print("Total Files: ",total_files)
    print("Total Folders: ",total_folders)
    print("Total Storage: ", round(total_size/1024/1024,2),"KB")

    return total_files, total_folders, total_size

