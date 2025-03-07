import numpy as np
import pandas as pd
import os,sys
import csv

ADULT_PATH = "Data/Adults"
CHILD_PATH = "Data/Children"
SC_INSTRUCTION_PATH = "Data/SC_data.csv"
def convert_to_csv(path,output_path):
    if not os.path.exists(path):
        raise ValueError("Path does not exist")
    with open(path, 'r') as infile, open(output_path, 'w') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(['patient_id','file','start','end','duration','file_path'])
        
        for line in infile:
            data = line.strip().split(',')
            patient_id = data[0]
            i = 1
                # print(f"Incomplete data on line: {line.strip()}")
            while i+3 < len(data):
                if data[i] == '':
                    break
                file_name = data[i]
                start = data[i+1]
                end = data[i+2]
                duration = data[i+3]
                
                file_path = get_file_path(patient_id, file_name)
                if file_path:
                    csv_writer.writerow([patient_id,file_name,file_path,start,end,duration])
                else:
                    # Print a message if the file does not exist
                    print(f"File '{file_name}' not found for patient '{patient_id}'.")
                
                i = i+4
            if i < len(data):
                continue
                # print(f"Incomplete data on line: {line.strip()}")

def get_file_path(patient_id, file_name):
    # Define the base directories for Adults and Children
    base_dir_adults = os.path.join("Data", "Adults", patient_id, "PPG")
    base_dir_children = os.path.join("Data", "Children", patient_id, "PPG")
    
    # Check if the file exists in the Adults or Children directories
    file_path_adults = os.path.join(base_dir_adults, file_name)
    file_path_children = os.path.join(base_dir_children, file_name)
    
    # Check if the file exists in the Adults directory (no subfolders)
    file_path_adults = os.path.join(base_dir_adults, file_name)
    if os.path.exists(file_path_adults):
        return file_path_adults

    # Search in Children directory, including subfolders
    for root, dirs, files in os.walk(base_dir_children):
        if file_name in files:
            return os.path.join(root, file_name)
    return None


if __name__ == "__main__":
    convert_to_csv(SC_INSTRUCTION_PATH,"Data/df_data_path.csv")