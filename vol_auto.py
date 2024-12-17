import os
import sys
import subprocess

# Global variables
os_version = "DEADBEEF"
file_path = ""
file_name = ""
var_win = False
var_linux = False
var_macos = False

commands_vol2 = [
    "amcache", "apihooks", "atoms", "atomscan", "auditpol", "bigpools", "bioskbd", "cachedump", "callbacks", 
    "clipboard", "cmdline", "cmdscan", "connections", "connscan", "consoles", "crashinfo", "deskscan", 
    "devicetree", "dlldump", "dlllist", "driverirp", "drivermodule", "driverscan", "dumpcerts", "dumpfiles", 
    "dumpregistry", "editbox", "envars", "eventhooks", "evtlogs", "filescan", "gahti", "gditimers", "gdt", 
    "getservicesids", "getsids", "handles", "hashdump", "hibinfo", "hivedump", "hivelist", "hivescan", 
    "hpakextract", "hpakinfo", "idt", "iehistory", "imagecopy", "imageinfo", "impscan", "joblinks", 
    "kdbgscan", "kpcrscan", "ldrmodules", "lsadump", "machoinfo", "malfind", "mbrparser", "memdump", 
    "memmap", "messagehooks", "mftparser", "moddump", "modscan", "modules", "multiscan", "mutantscan", 
    "notepad", "objtypescan", "patcher", "poolpeek", "printkey", "privs", "procdump", "pslist", "psscan", 
    "pstree", "psxview", "qemuinfo", "raw2dmp", "screenshot", "servicediff", "sessions", "shellbags", 
    "shimcache", "shutdowntime", "sockets", "sockscan", "ssdt", "strings", "svcscan", "symlinkscan", 
    "thrdscan", "threads", "timeliner", "timers", "truecryptmaster", "truecryptpassphrase", "truecryptsummary", 
    "unloadedmodules", "userassist", "userhandles", "vaddump", "vadinfo", "vadtree", "vadwalk", "vboxinfo", 
    "verinfo", "vmwareinfo", "volshell", "windows", "wintree", "wndscan", "yarascan"
]

commands_vol3_win = [
    "windows.bigpools.BigPools", "windows.cachedump.Cachedump", "windows.callbacks.Callbacks", 
    "windows.cmdline.CmdLine", "windows.crashinfo.Crashinfo", "windows.devicetree.DeviceTree", 
    "windows.dlllist.DllList", "windows.driverirp.DriverIrp", "windows.drivermodule.DriverModule", 
    "windows.driverscan.DriverScan", "windows.dumpfiles.DumpFiles", "windows.envars.Envars", 
    "windows.filescan.FileScan", "windows.getservicesids.GetServiceSIDs", "windows.getsids.GetSIDs", 
    "windows.handles.Handles", "windows.hashdump.Hashdump", "windows.hollowprocesses.HollowProcesses", 
    "windows.iat.IAT", "windows.info.Info", "windows.joblinks.JobLinks", "windows.kpcrs.KPCRs", 
    "windows.ldrmodules.LdrModules", "windows.lsadump.Lsadump", "windows.malfind.Malfind", 
    "windows.mbrscan.MBRScan", "windows.memmap.Memmap", "windows.mftscan.ADS", "windows.mftscan.MFTScan", 
    "windows.modscan.ModScan", "windows.modules.Modules", "windows.mutantscan.MutantScan", 
    "windows.netscan.NetScan", "windows.netstat.NetStat", "windows.pedump.PEDump", "windows.poolscanner.PoolScanner", 
    "windows.privileges.Privs", "windows.processghosting.ProcessGhosting", "windows.pslist.PsList", 
    "windows.psscan.PsScan", "windows.pstree.PsTree", "windows.psxview.PsXView", 
    "windows.registry.certificates.Certificates", "windows.registry.getcellroutine.GetCellRoutine", 
    "windows.registry.hivelist.HiveList", "windows.registry.hivescan.HiveScan", 
    "windows.registry.printkey.PrintKey", "windows.registry.userassist.UserAssist", "windows.sessions.Sessions", 
    "windows.shimcachemem.ShimcacheMem", "windows.skeleton_key_check.Skeleton_Key_Check", "windows.ssdt.SSDT", 
    "windows.statistics.Statistics", "windows.strings.Strings", "windows.suspicious_threads.SupsiciousThreads", 
    "windows.svcdiff.SvcDiff", "windows.svclist.SvcList", "windows.svcscan.SvcScan", 
    "windows.symlinkscan.SymlinkScan", "windows.thrdscan.ThrdScan", "windows.threads.Threads", 
    "windows.timers.Timers", "windows.truecrypt.Passphrase", "windows.unloadedmodules.UnloadedModules", 
    "windows.vadinfo.VadInfo", "windows.vadwalk.VadWalk", "windows.vadyarascan.VadYaraScan", 
    "windows.verinfo.VerInfo", "windows.virtmap.VirtMap"
]

commands_vol3_linux = [
    "linux.bash.Bash", "linux.capabilities.Capabilities", "linux.check_afinfo.Check_afinfo", 
    "linux.check_creds.Check_creds", "linux.check_idt.Check_idt", "linux.check_modules.Check_modules", 
    "linux.check_syscall.Check_syscall", "linux.elfs.Elfs", "linux.envars.Envars", "linux.iomem.IOMem", 
    "linux.keyboard_notifiers.Keyboard_notifiers", "linux.kmsg.Kmsg", "linux.library_list.LibraryList", 
    "linux.lsmod.Lsmod", "linux.lsof.Lsof", "linux.malfind.Malfind", "linux.mountinfo.MountInfo", 
    "linux.netfilter.Netfilter", "linux.proc.Maps", "linux.psaux.PsAux", "linux.pslist.PsList", "linux.psscan.PsScan", 
    "linux.pstree.PsTree", "linux.sockstat.Sockstat", "linux.tty_check.tty_check", "linux.vmayarascan.VmaYaraScan"
]

commands_vol3_mac = [
    "mac.bash.Bash", "mac.check_syscall.Check_syscall", "mac.check_sysctl.Check_sysctl", 
    "mac.check_trap_table.Check_trap_table", "mac.dmesg.Dmesg", "mac.ifconfig.Ifconfig", 
    "mac.kauth_listeners.Kauth_listeners", "mac.kauth_scopes.Kauth_scopes", "mac.kevents.Kevents", 
    "mac.list_files.List_Files", "mac.lsmod.Lsmod", "mac.lsof.Lsof", "mac.malfind.Malfind", "mac.mount.Mount", 
    "mac.netstat.Netstat", "mac.proc_maps.Maps", "mac.psaux.Psaux", "mac.pslist.PsList", "mac.pstree.PsTree", 
    "mac.socket_filters.Socket_filters", "mac.timers.Timers", "mac.trustedbsd.Trustedbsd", "mac.vfsevents.VFSevents"
]

# Header
def print_header():
    os.system('clear')
    print("******************************************************************************************************")
    print("Volatility Auto")
    print("******************************************************************************************************")

# Print padding
def print_padding():
    commande = "echo \"\n\n ******************************************************************************************************\" >> /tmp/Volatility_auto_output/info_version.txt"
    try:
        result = subprocess.run(commande, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print_message(f"Error executing command: {e.stderr}", 'red')
    commande = "echo \"************         Volatility 2 result       ******************************************\" >> /tmp/Volatility_auto_output/info_version.txt"
    try:
        result = subprocess.run(commande, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print_message(f"Error executing command: {e.stderr}", 'red')
    commande = "echo \" ******************************************************************************************************\n\n\" >> /tmp/Volatility_auto_output/info_version.txt"
    try:
        result = subprocess.run(commande, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print_message(f"Error executing command: {e.stderr}", 'red')
    

def print_help():
    print("Usage: [--help|--set-profil|quit/exit]")
    print("Usage: vol2 [list|imageinfo|pstree|psscan|pslist]")
    print("Usage: vol3 [list|imageinfo|pstree|psscan|pslist]")
    
# Function to print a message with color
def print_message(message, color):
    colors = {
        'green' : '\033[32m',
        'reset' : '\033[0m' ,
        'yellow': '\033[33m',
        'red'   : '\033[31m',
        'pink'  : '\033[35m',
        'blue'  : '\033[34m'  
    }
    print(f"{colors[color]}{message}{colors['reset']}")

# Definir le type d'OS
def set_os_type(os_type):
    while temp_os_type != "win" or temp_os_type != "linux" or temp_os_type != "macos":
        print_message("Please set the OS type of the memory dump (win/linux/macos)", 'yellow')
        temp_os_type = parse_input(os_type)
        if temp_os_type == "win":
            var_win = True
            print_message("OS type set to Windows", 'green')
            break
        elif temp_os_type == "linux":
            var_linux = True
            print_message("OS type set to Linux", 'green')
            break
        elif temp_os_type == "macos":
            var_macos = True
            print_message("OS type set to MacOS", 'green')
            break
        else:
            print_message("Invalid input. Please try again.", 'red')

# Function to find a file in the home directory
def find_file_in_home(file_name):
    home_dir = os.path.expanduser("~")
    for root, dirs, files in os.walk(home_dir):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

# Function to create the output directory
def create_output_dir(out_path):
    output_dir = out_path
    counter = 1
    while os.path.exists(output_dir):
        output_dir = f"{out_path}_{counter}"
        counter += 1
    os.makedirs(output_dir)
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

# Function to execute a command and save the output to a file
def execute_command(command, output_file):
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        with open(output_file, 'w') as f:
            f.write(result.stdout)
        print_message(f"Command executed successfully. Output saved to {output_file}", 'green')
    except subprocess.CalledProcessError as e:
        print_message(f"Error executing command: {e.stderr}", 'red')

# def win_command(cmd1, cmd2):

#     while cmd1 in commands_vol3_win:
#         command = f"docker run -it --rm -v {file_path}:/mnt volatility_2-docker -f /mnt/{file_name} {cmd1}"
#         execute_command(command, f"/tmp/Volatility_auto_output/vol2_out/{cmd1}.txt")

# Function to run Volatility command
def run_volatility(cmd):
    cmd_parts = cmd.split()
    vol_version = cmd_parts[0]
    vol_command = cmd_parts[1]
    if vol_version == "vol2" and os_version == "DEADBEEF":
        print_message("volatility_2 not work without os version parameter", 'red')

    # volatility_2
    elif vol_version == "vol2" and os_version != "DEADBEEF":
        if vol_command == "all":
            if var_win == True:
                print_message("Windows commands not implemented yet", 'red')
            elif var_linux == True:
                print_message("Linux commands not implemented yet", 'red')
            elif var_macos == True:
                print_message("MacOS commands not implemented yet", 'red')

        elif vol_command == "list":
            print("Available commands for volatility_2:")
            for command in commands_vol2:
                print(f"  {command}")
        elif vol_command in commands_vol2:
            command = f"docker run -it --rm -v {file_path}:/mnt volatility_2-docker -f /mnt/{file_name} {vol_command}"
            execute_command(command, f"/tmp/Volatility_auto_output/vol2_out/{vol_command}.txt")
        else:
            print_message("Invalid command. Please try again.", 'red')

    # volatility_3
    elif vol_version == "vol3":
        if vol_command == "all":
            while vol_command in commands_vol3_win:
                command = f"docker run -it --rm -v {file_path}:/mnt volatility_3-docker -f /mnt/{file_name} {vol_command}"
                execute_command(command, f"/tmp/Volatility_auto_output/vol3_out/{vol_command}.txt")
        elif vol_command == "list":
            print("Available commands for volatility_3:")
            for command in commands_vol3_win:
                print(f"  {command}")
        elif vol_command in commands_vol3_win:
            command = f"docker run -it --rm -v {file_path}:/mnt volatility_3-docker -f /mnt/{file_name} {vol_command}"
            execute_command(command, f"/tmp/Volatility_auto_output/vol3_out/{vol_command}.txt")
        else:
            print_message("Invalid command. Please try again whit --set-profil.", 'red')
    else:
        print_message("Invalid cersion of volatility. use \"vol2\" or \"vol3\".", 'red')

# Function to get the OS version detected by Volatility
def funct_info():
    command_vol2 = f"docker run -it --rm -v {file_path}/:/mnt volatility_2-docker -f /mnt/{file_name} imageinfo > /tmp/Volatility_auto_output/info_version.txt"
    command_vol3 = f"docker run -it --rm -v {file_path}/:/mnt volatility_3-docker -f /mnt/{file_name} windows.info >> /tmp/Volatility_auto_output/info_version.txt"
    
    print("\033[F\033[F\033[F\033[F")
    try:
        result = subprocess.run(command_vol2, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print_message(f"Error executing command: {e.stderr}", 'red')
    try:
        result = subprocess.run(command_vol3, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print_message(f"Error executing command: {e.stderr}", 'red')

    with open("/tmp/Volatility_auto_output/info_version.txt", 'r') as f:
        for line in f:
            if "Suggested Profile(s) :" in line:
                print("\033[F\033[F\033[F\033[F")
                print_message(f"\n\nOS version detected by Volatility:", 'green')
                print_message(f"\n\n{line}", 'blue')
                break
            else:
                with open("/tmp/Volatility_auto_output/vol2_out/vol2_info_version.txt", 'r') as f:
                    print(f.read())
                print_padding()
                with open("/tmp/Volatility_auto_output/vol3_out/vol3_info_version.txt", 'r') as f:
                    print(f.read())

# Function to parse input
def parse_input(cmd):
    if cmd == 'exit' or cmd == 'quit':
        print_message("Exiting...", 'red')
        sys.exit(0)
    elif cmd == '--help':
        print_help()
    elif cmd == '--set-profil':
        funct_info()
    elif cmd != '':
        run_volatility(cmd)
    return cmd

# Function main
def main():
    global os_version
    global file_path
    global file_name
    global var_win
    global var_linux
    global var_macos
    temp_os_type = ""


    if len(sys.argv) != 2:
        print_message("Usage: vol_auto <file>", 'red')
        sys.exit(1)

    print_header()
    file_name = sys.argv[1]
    if not os.path.exists(file_name):
        print_message(f"File {file_name} not found.", 'red')
        file_path = find_file_in_home(file_name)
        if not file_path:
            print_message(f"File {file_name} not found in the home directory. Exiting...", 'red')
            sys.exit(1)
    else:
        file_path = os.path.dirname(os.path.abspath(file_name))
        file_name = os.path.basename(file_name)

    print_message(f"File found: {file_name}", 'green')

    print_message(f"Starting Volatility analysis for file: {file_path}", 'green')
    create_output_dir("/tmp/Volatility_auto_output")

    print_message("Checking OS version of memory dump", 'yellow')
    funct_info()
    while os_version == "DEADBEEF":
        os_version = input("Please enter the OS version detected by Volatility: ")
        if os_version == "NONE":
            print_message("OS version set to \"NONE\"", 'red')
            break
        elif os_version != "" and os_version != "DEADBEEF":
            print_message(f"OS version set to {os_version}\n", 'green')
            break
        else:
            print_message("Invalid input. Please try again.", 'red')

    while True:
        prompt = input("\033[34mdocker\033[0m@\033[32mvolatility $ ")
        print_message(f"[ DEBUG ]Command entered: {prompt}", 'pink')
        if not prompt:
            continue
        else:
            prompt = prompt.strip()
            command = parse_input(prompt)

if __name__ == "__main__":
    main()
