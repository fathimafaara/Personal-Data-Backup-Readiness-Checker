import os
from Modules.Duplicate_Checker import find_duplicates


def categorize_files(files):
    extension = os.path.splitext(files)[1].lower()
    categories = {"Documents":
                      [".pdf",".docx",".doc",".txt",".xlsx",".pptx"],
                  "Images":
                      [".jpg",".jpeg",".png",".gif"],
                  "Videos":
                      [".mp4",".avi",".mkv"],
                  "Audio":
                      [".mp3",".wav"],
                  "Archives":
                      [".zip",".rar",".7z"],
                  "Applications":
                      [".exe",".msi"]}
    for category, extensions in categories.items():
        if extension in extensions:
            return category
    return "other"


def find_large_files(folder_path,size_limit = 100):
    large_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
               file_size = os.path.getsize(file_path)
            except OSError:
                print("Warning: Could not access file:", file)
                continue
            size_in_mb = file_size / (1024 * 1024)
            if size_in_mb > size_limit:
                large_files.append({
                    "name" : file,
                    "path" : file_path,
                    "size" : round(size_in_mb, 2)})
    return large_files


def find_empty_folders(folder_path):
    empty_folders = []
    for root, folders, files in os.walk(folder_path):
        if not folders and not files:
            empty_folders.append(root)
    return empty_folders


def calculate_storage_by_category(folder_path):
    storage = {}
    for root, folders, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_size = os.path.getsize(file_path)
            except OSError:
                print("Warning: Could not access file:", file)
                continue
            category = categorize_files(file)
            if category not in storage:
                storage[category] = 0
            storage[category] += file_size
    return storage


def calculate_backup_score(folder_path):
    score = 0
    duplicates = find_duplicates(folder_path)
    empty_folders = find_empty_folders(folder_path)
    large_files = find_large_files(folder_path)
    organisation = check_file_organisation(folder_path)

    if not duplicates:
        score += 30
    if not empty_folders:
        score += 20
    if not large_files:
        score += 20
    if organisation >= 80:
        score += 30
    return score


def check_file_organisation(folder_path):
    total_files = 0
    organised_files = 0

    for root, folders, files in os.walk(folder_path):
        for file in files:
            total_files += 1
            category = categorize_files(file)
            folder_name = os.path.basename(root)
            if folder_name.lower() == category.lower():
                organised_files += 1
    if total_files == 0:
        return 0
    organisation_percentage = (organised_files / total_files) * 100
    return round(organisation_percentage, 2)