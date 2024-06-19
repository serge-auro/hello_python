import os
import json
import csv

def convert_json_to_csv(input_path, output_path):
    try:
        with open(input_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {input_path}: {e}")
        return
    except Exception as e:
        print(f"Error reading {input_path}: {e}")
        return

    rows = []
    for path, methods in data.get('paths', {}).items():
        for method, details in methods.items():
            row = {
                'type': method,
                'path': path,
                'summary': details.get('summary', '')
            }
            rows.append(row)

    try:
        with open(output_path, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['type', 'path', 'summary'], delimiter=';')
            writer.writeheader()
            writer.writerows(rows)
    except Exception as e:
        print(f"Error writing CSV to {output_path}: {e}")

def process_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, filename.replace('.txt', '.csv'))
            convert_json_to_csv(input_path, output_path)
            print(f"Converted {input_path} to {output_path}")

# Путь к директории с файлами
directory_path = r'C:\Users\SergeyIvanov\Documents\_Era_Drilling\матрица'
process_directory(directory_path)
