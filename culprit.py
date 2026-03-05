import os

file_path = r'C:\n8n-data\bens_demo.txt'

try:
    if os.path.exists(file_path):
        with open(file_path, 'r+') as f:
            print("Success: File is accessible and not locked.")
    else:
        print("Error: File does not exist at that path.")
except IOError as e:
    print(f"Locked: {e}")