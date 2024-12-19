# Auto_volatility/src/message_dysplay.py

import subprocess
import os

# Function to print a message with color
def print_message(message, color):
    colors = {
        'red'   : '\033[31m',
        'green' : '\033[32m',
        'yellow': '\033[33m',
        'blue'  : '\033[34m',
        'pink'  : '\033[35m',
        'reset' : '\033[0m' ,
    }
    print(f"{colors[color]}{message}{colors['reset']}")

def print_padding():
    commands = [
        "echo \"\n\n******************************************************************************************************\" >> /tmp/Volatility_auto_output/info_version.txt",
        "echo \"*************************                Volatility 2 result                 *************************\" >> /tmp/Volatility_auto_output/info_version.txt",
        "echo \"******************************************************************************************************\n\n\" >> /tmp/Volatility_auto_output/info_version.txt"
    ]
    for command in commands:
        try:
            result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print_message(f"Error executing command: {e.stderr}", 'red')

def print_help():
    print_header()
    print ("Vol_auto 1.0 ( https://github.com/Ardcord/Auto_volatility )\n")
    print("Usage: [--help|--set-profil|quit/exit]\n\n")
    print("List of standard commands:")
    print("    --help       : Display this help message")
    print("    --set-profil : Set the profile of the memory dump")
    print("    --set-os     : Set the OS type of the memory dump")
    print("    --show-param : Display the parameters of the memory dump")
    print("    exit/quit    : Exit the program")

    print("\nList of Volatility commands:")
    print("Usage: vol2 [list|imageinfo|pstree|psscan|pslist]")
    print("Usage: vol3 [list|imageinfo|pstree|psscan|pslist]")

def print_header():
    os.system('clear')
    print(f"****************************************************************************************")
    print(f"#    ▄█    █▄   ▄██████▄   ▄█      \033[31m    ▄████████ ███    █▄      ███      ▄██████▄       \033[0m")
    print(f"#   ███    ███ ███    ███ ███      \033[31m   ███    ███ ███    ███ ▀█████████▄ ███    ███      \033[0m")
    print(f"#   ███    ███ ███    ███ ███      \033[31m   ███    ███ ███    ███    ▀███▀▀██ ███    ███      \033[0m")
    print(f"#   ███    ███ ███    ███ ███      \033[31m   ███    ███ ███    ███     ███   ▀ ███    ███      \033[0m")
    print(f"#   ███    ███ ███    ███ ███      \033[31m ▀███████████ ███    ███     ███     ███    ███      \033[0m")
    print(f"#   ███    ███ ███    ███ ███      \033[31m   ███    ███ ███    ███     ███     ███    ███      \033[0m")
    print(f"#   ███    ███ ███    ███ ███▌    ▄\033[31m   ███    ███ ███    ███     ███     ███    ███      \033[0m")
    print(f"#    ▀██████▀   ▀██████▀  █████▄▄██\033[31m   ███    █▀  ████████▀     ▄████▀    ▀██████▀       \033[0m")
    print(f"#                         ▀        \033[31m                                                     \033[0m")
    print(f"****************************************************************************************")
    print(f"                                                                Version            1.0")
    print(f"                                                                Last update:  19/12/24")
    print(f"                                                                By             Ardcord")
    print(f"****************************************************************************************")