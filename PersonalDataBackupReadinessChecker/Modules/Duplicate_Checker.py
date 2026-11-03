import hashlib
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def find_duplicates(folder_path):
    file_hashes = {}
    duplicates = []

    for root, folders, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_hash = calculate_hash(file_path)
            except OSError:
                print("Warning: Could not calculate access file:", file)
                continue
            if file_hash in file_hashes:
                duplicates.append(file_path)
            else:
                file_hashes[file_hash] = file_path
    return duplicates