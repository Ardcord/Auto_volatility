# Auto_volatility/src/launch.py

import subprocess

from src.message_dysplay import print_message, print_padding

part_1 = "docker run -it --rm -v "
part_2 = ":/mnt volatility_"
part_3 = "-docker -f /mnt/"


# Function to get the OS version detected by Volatility
def funct_info(struct):
    commands = [
        f"{part_1}{struct.file_path}/{part_2}3{part_3}{struct.file_name} windows.info > {struct.output_dir}/info_version.txt",
        f"{part_1}{struct.file_path}/{part_2}2{part_3}{struct.file_name} imageinfo >> {struct.output_dir}/info_version.txt"
    ]

    print("\033[F\033[F\033[F\033[F")  # Efface des lignes dans le terminal
    
    for i, command in enumerate(commands):
        try:
            # Exécution de la commande actuelle
            result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print_message(f"Command executed successfully: {command}", 'green')

            # Appeler print_padding après la première commande
            if i == 0:
                print_padding()
        except subprocess.CalledProcessError as e:
            print_message(f"Error executing command: {e.stderr}", 'red')

    with open(f"{struct.output_dir}/info_version.txt", 'r') as f:
        for line in f:
            if "Suggested Profile(s) :" in line:
                print("\033[F\033[F\033[F\033[F")
                print_message(f"\n\nOS version detected by Volatility:", 'green')
                print_message(f"\n\n{line}", 'blue')
                break
            else:
                with open(f"{struct.output_dir}/info_version.txt", 'r') as f:
                    print(f.read())



# Function to execute a command and save the output to a file
def execute_command(command, struct, nbr, count):
    if nbr == 0 or nbr == "":
        nbr += 1
        count += 1
    temp_cmd1 = f"{part_1}{struct.file_path}/{part_2}{struct.file_name} {command} {struct.output_dir}{struct.vol_version}_out/{struct.cmd}.txt"
    if struct.vol_version == "vol2":
        temp_cmd2 = f"2"
    elif struct.vol_version == "vol3":
        temp_cmd2 = f"3"
    temp_cmd3 = f"{struct.file_name} {command} {struct.output_dir}{struct.vol_version}_out/{struct.cmd}.txt"
    #concatenation des commandes
    command = f"{temp_cmd1}{temp_cmd2}{temp_cmd3}"
    output_file = f"{struct.output_dir}{struct.vol_version}_out/{struct.cmd}.txt"
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        with open(output_file, 'w') as f:
            f.write(result.stdout)
        print_message(f"[{nbr}/{count}] Success: {output_file}", 'green')

    except subprocess.CalledProcessError as e:
        print_message(f"Error executing command: {e.stderr}", 'red')