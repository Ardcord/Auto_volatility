# Auto_volatility/src/file_utils.py

from src.message_dysplay import *

import os
import subprocess

# Function to find a file in the home directory
def find_file_in_home(file_name):
    home_dir = os.path.expanduser("~")
    for root, dirs, files in os.walk(home_dir):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

# Function to create the output directory
def create_output_dir(out_path, struct):
    output_dir = out_path
    counter = 1
    while os.path.exists(output_dir):
        output_dir = f"{out_path}_{counter}"
        counter += 1
    os.makedirs(output_dir)
    struct.output_dir = output_dir
    dir_vol2 = os.path.join(output_dir, "vol2_out")
    dir_vol3 = os.path.join(output_dir, "vol3_out")
    os.makedirs(dir_vol2)
    os.makedirs(dir_vol3)
    command = f"tree {output_dir}"
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print_message(f"Error executing command: {e.stderr}", 'red')
    print_message(f"Created output directory: {output_dir}", 'green')
    return output_dir

# Define the OS version
def set_os_type(struct):
    while True:
        temp_os_type = ""
        temp_os_type = input("Enter the OS type (win, linux, macos): ")
        if temp_os_type.lower() == "win" or temp_os_type.lower() == "windows":
            struct.var_win = True
            struct.os_type = "win"
            print_message("OS type set to Windows", 'green')
            break
        elif temp_os_type.lower() == "linux":
            struct.var_linux = True
            struct.os_type = "linux"
            print_message("OS type set to Linux", 'green')
            break
        elif temp_os_type.lower() == "macos" or temp_os_type.lower() == "mac":
            struct.var_macos = True
            struct.os_type = "mac"
            print_message("OS type set to MacOS", 'green')
            break
        else:
            print_message("Invalid input. Please try again.", 'red')

def print_parameters(struct):
    print(f"Volatility: {struct.vol_version}")
    print(f"OS version: {struct.os_version}")
    print(f"OS type   : {struct.os_type}")
    print(f"File path : {struct.file_path}")
    print(f"File name : {struct.file_name}")
    print(f"Output dir: {struct.output_dir}")
    print(f"Windows OS: {struct.var_win}")
    print(f"Linux OS  : {struct.var_linux}")
    print(f"MacOS OS  : {struct.var_macos}")
    print("\n")