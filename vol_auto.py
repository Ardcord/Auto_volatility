import os
import sys

from src.message_dysplay import *
from src.file_utils import *
from src.commands import *
from src.launch import *

class VolatilityCommandArgs:
    def __init__(self, vol_version, os_version, os_type, file_path, file_name, output_dir, usr_input, cmd, cmd_opt_1, cmd_opt_2, cmd_opt_3, cmd_opt_4, cmd_opt_5, cmd_opt_6, var_win, var_linux, var_macos):
        self.vol_version = vol_version  # Version de Volatility (vol2 ou vol3)
        self.os_version = "DEADBEEF"    # Version de l'OS (DEADBEEF si non défini)
        self.os_type = os_type          # Type d'OS (win, linux, macos)
        self.file_path = file_path      # Chemin du fichier mémoire
        self.file_name = file_name      # Nom du fichier mémoire
        self.output_dir = ""            # Répertoire de sortie
        self.usr_input = ""             # Entrée utilisateur
        self.cmd = ""                   # Commande à exécuter
        self.cmd_opt_1 = ""             # Option de la commande
        self.cmd_opt_2 = ""             # Option de la commande
        self.cmd_opt_3 = ""             # Option de la commande
        self.cmd_opt_4 = ""             # Option de la commande
        self.cmd_opt_5 = ""             # Option de la commande
        self.cmd_opt_6 = ""             # Option de la commande
        self.var_win = False            # Bool d'OS Windows
        self.var_linux = False          # Bool d'OS Linux
        self.var_macos = False          # Bool d'OS MacOS

# Function to run Volatility command
def run_volatility(struct):

    if struct.vol_version == "vol2" and struct.os_version == "DEADBEEF":
        print_message("volatility_2 not work without os version parameter", 'red')

    # volatility_2
    elif struct.vol_version == "vol2" and struct.os_version != "DEADBEEF":
        if struct.cmd == "all":
            print_message("Running all commands for volatility_2 [work in progress]", 'yellow')
            # logique all commande vol2 [ Work in progress ]
        elif struct.cmd == "list":
            print("Available commands for volatility_2:")
            commands = get_commands(struct)
            for command in commands:
                print(f"  {command}")
        elif struct.cmd == find_command(struct):
            execute_command(struct.cmd, struct)
        else:
            print_message("Invalid command. Please try again.", 'red')

    # volatility_3
    elif struct.vol_version == "vol3":
        if struct.cmd == "all":
            commands = get_commands(struct)
            count = len(commands)
            while command in commands:
                nbr+=1
                execute_command(command, struct, nbr, count)
        elif struct.cmd == "list":
            command = get_commands(struct)
            print("Available commands for volatility_3:")
            for command in get_commands(struct):
                print(f"  {command}")
        elif struct.cmd in get_commands(struct):
            execute_command(command, struct)
        else:
            print_message("Invalid command. Please try again whit --set-profil.", 'red')
    else:
        print_message("Invalid version of volatility. use \"vol2\" or \"vol3\".", 'red')

# Memo 
#
# args[1] - ‑‑dump ‑‑pid ‑‑key ‑‑virtaddr ‑‑physaddr 
# args[2] - ‑‑pid


# Function to parse input
def parse_input(struct, prompt):
    
    if prompt == 'exit' or prompt == 'quit':
        print_message("Exiting...", 'red')
        sys.exit(0)
    elif prompt == '--help':
        print_help()
    elif prompt == '--set-profil':
        funct_info()
    elif prompt == '--set-os':
        set_os_type(struct)
    elif prompt == '--show-param':
        print_parameters(struct)
    elif prompt != '':
        if prompt:
            struct.vol_version = prompt[0]
            struct.cmd = prompt[1]
        else:
            struct.vol_version = ""
            struct.cmd = ""
        options = prompt[2:]
        cmd_opts = ['cmd_opt_1', 'cmd_opt_2', 'cmd_opt_3', 'cmd_opt_4', 'cmd_opt_5', 'cmd_opt_6']

        for i, opt in enumerate(options[:6]):
            setattr(struct, cmd_opts[i], opt)
        if get_commands(struct) != "":
            run_volatility(struct)
    return

# Function main
def main():

    if len(sys.argv) != 2:
        print_message("Usage: vol_auto <file>", 'red')
        sys.exit(1)
    struct = VolatilityCommandArgs("", "DEADBEEF", "", "", "", "", "", "", "", "", "", "", "", "", False, False, False)
    print_header()
    struct.file_name = sys.argv[1]
    if not os.path.exists(struct.file_name):
        print_message(f"File {struct.file_name} not found.", 'red')
        struct.file_path = find_file_in_home(struct.file_name)
        if not struct.file_path:
            print_message(f"File {struct.file_name} not found in the home directory. Exiting...", 'red')
            sys.exit(1)
    else:
        struct.file_path = os.path.dirname(os.path.abspath(struct.file_name))
        struct.file_name = os.path.basename(struct.file_name)

    print_message(f"File found: {struct.file_name}", 'green')

    print_message(f"Starting Volatility analysis for file: {struct.file_path}", 'green')
    create_output_dir("/tmp/Volatility_auto_output", struct)

    print_message("Checking OS version of memory dump", 'yellow')
    funct_info(struct)
    while struct.os_version == "DEADBEEF":
        struct.os_version = "DEADBEEF"
        struct.os_version = input("Please enter the OS version detected by Volatility: ")
        if struct.os_version.upper() == "NONE":
            print_message(f"\033[K\033[FOS version set to \"NONE\"", 'red')
            break
        elif struct.os_version != "" and struct.os_version != "DEADBEEF":
            print_message(f"\033[K\033[FOS version set to {struct.os_version}\n", 'green')
            break
        else:
            print_message("\033[K\033[FInvalid input. Please try again.", 'red')
    set_os_type(struct)
    while True:
        prompt = input("\033[1;34mdocker\033[0m@\033[1;32mvolatility $ \033[0m")
        
        print_message(f"[ DEBUG ]Command entered: {prompt}", 'pink')
        if prompt:
            prompt = prompt.strip()
            command = parse_input(struct, prompt)
            
if __name__ == "__main__":
    main()
