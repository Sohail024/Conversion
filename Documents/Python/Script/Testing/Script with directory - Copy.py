import os
import pandas as pd
import re
from glob import glob
import shutil

def read_keyword_mappings(excel_file):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(excel_file)
    
    # Create a dictionary to store mappings
    mappings = {}
    
    # Iterate through the DataFrame and populate the mappings dictionary
    for _, row in df.iterrows():
        selenium_pattern = row['Selenium']
        browser_pattern = row['Browser']
        # Adjust selenium_pattern to handle multiple spaces
        selenium_pattern = re.sub(r'\s+', r'\\s+', selenium_pattern)
        mappings[selenium_pattern] = browser_pattern
    
    return mappings

def convert_script(input_file, output_file, mappings):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    with open(output_file, 'w') as file:
        for line in lines:
            for selenium_pattern, browser_pattern in mappings.items():
                # Use regex to replace Selenium keywords with Browser keywords
                line = re.sub(selenium_pattern, browser_pattern, line)
            file.write(line)

def find_robot_files(directory):
    # Use glob to find all .robot files in directory and subdirectories
    robot_files = glob(os.path.join(directory, '**', '*.robot'), recursive=True)
    return robot_files

def clear_directory(directory):
    # Clear all files in the given directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

def convert_all_robot_files(directory, mappings):
    # Create a directory for the converted files
    converted_dir = os.path.join(directory, 'converted_files')
    if os.path.exists(converted_dir):
        clear_directory(converted_dir)
    else:
        os.makedirs(converted_dir)
    
    # Find all .robot files in the given directory and subdirectories
    robot_files = find_robot_files(directory)
    
    for input_file in robot_files:
        # Create a new output file path in the converted directory
        output_file_name = os.path.basename(input_file).replace('.robot', '_converted.robot')
        output_file = os.path.join(converted_dir, output_file_name)
        
        # Convert the script
        convert_script(input_file, output_file, mappings)
        print(f'Converted script saved to {output_file}')

# Input directory containing .robot files
input_directory = r'C:\Users\z004twvj\Desktop\Practice\Testing script'
# Excel file with keyword mappings
excel_file = 'Convert.xlsx'

# Read keyword mappings from Excel
mappings = read_keyword_mappings(excel_file)

# Convert all .robot files in the specified directory
convert_all_robot_files(input_directory, mappings)
