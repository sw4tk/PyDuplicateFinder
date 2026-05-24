import hashlib
import os

def get_files():
    items = []
    for root,dirs,files in os.walk('.'):
        for file in files:
            items.append(os.path.join(root, file))
    return items

def get_hash(file):
    with open(file, 'rb') as f:
        file_hash = hashlib.sha256()
        while chunk := f.read(8192):
            file_hash.update(chunk)
    return file_hash.hexdigest()

def group_files(files):
    groups = {}
    for file in files:
        file_hash = get_hash(file)
        if file_hash not in groups:
            groups[file_hash] = []
        groups[file_hash].append(file)
    return groups

def get_duplicates(groups):
    duplicates = []
    for key , values in groups.items():
        if len(values) > 1:
            duplicates.append(values)
    return duplicates

def main():
    files = get_files()
    groups = group_files(files)
    duplicates = get_duplicates(groups)
    for duplicate in duplicates:
        print("Duplicate files:")
        for file in duplicate:
            print(os.path.basename(file))
            
main()