# /Auto_volatility/src/commands.py

# Colors
RED = '\033[91m'
NC = '\033[0m'

################################################################################################
#                                                                                              #
#   Volatility 2 commands list                                                                 #
#                                                                                              #
#       - Windows                                                                              #
#       - Linux                                                                                #
#       - Mac                                                                                  #
#                                                                                              #
#                                                                                              #
################################################################################################

commands_vol2 = [
    'gdt'    , 'handles' , 'verinfo'  , 'printkey'  , 'mbrparser'   , 'evtlogs'             ,
    'idt'    , 'hibinfo' , 'windows'  , 'procdump'  , 'mftparser'   , 'vadtree'             ,
    'ssdt'   , 'impscan' , 'wintree'  , 'qemuinfo'  , 'multiscan'   , 'getsids'             ,
    'atoms'  , 'lsadump' , 'wndscan'  , 'sessions'  , 'shellbags'   , 'vadwalk'             ,
    'gahti'  , 'malfind' , 'apihooks' , 'sockscan'  , 'shimcache'   , 'poolpeek'            ,
    'privs'  , 'memdump' , 'atomscan' , 'thrdscan'  , 'timeliner'   , 'kpcrscan'            , 
    'envars' , 'moddump' , 'auditpol' , 'vboxinfo'  , 'devicetree'  , 'imageinfo'           ,
    'memmap' , 'modscan' , 'bigpools' , 'volshell'  , 'driverscan'  , 'machoinfo'           ,
    'pslist' , 'modules' , 'connscan' , 'yarascan'  , 'eventhooks'  , 'userhandles'         ,
    'psscan' , 'notepad' , 'consoles' , 'cachedump' , 'ldrmodules'  , 'drivermodule'        ,
    'pstree' , 'patcher' , 'deskscan' , 'callbacks' , 'mutantscan'  , 'dumpregistry'        ,
    'timers' , 'psxview' , 'filescan' , 'clipboard' , 'screenshot'  , 'messagehooks'        ,
    'amcache', 'raw2dmp' , 'hashdump' , 'crashinfo' , 'userassist'  , 'shutdowntime'        ,
    'bioskbd', 'sockets' , 'hivedump' , 'driverirp' , 'vmwareinfo'  , 'getservicesids'      ,
    'cmdline', 'strings' , 'hivelist' , 'dumpcerts' , 'connections' , 'truecryptmaster'     ,
    'cmdscan', 'svcscan' , 'hivescan' , 'dumpfiles' , 'hpakextract' , 'unloadedmodules'     ,
    'dlldump', 'threads' , 'hpakinfo' , 'gditimers' , 'objtypescan' , 'truecryptsummary'    ,
    'dlllist', 'vaddump' , 'joblinks' , 'iehistory' , 'servicediff' , 'truecryptpassphrase' ,
    'editbox', 'vadinfo' , 'kdbgscan' , 'imagecopy' , 'symlinkscan'      
]

commands_vol2_all = [
    'memmap' , 'cmdline' , 'cmdscan' , 'vaddump' , 'filescan' , 'hivescan' ,'cachedump' ,
    'pslist' , 'lsadump' , 'notepad' , 'vadinfo' , 'hashdump' , 'kdbgscan' ,'clipboard' ,
    'psscan' , 'malfind' , 'strings' , 'verinfo' , 'hivedump' , 'printkey' ,'iehistory' , 
    'pstree' , 'memdump' , 'svcscan' , 'windows' , 'hivelist' , 'procdump' ,'imagecopy' ,
    'screenshot'  ,'connections' ,'symlinkscan','dumpregistry' ,'truecryptmaster' ,'truecryptsummary' , 'truecryptpassphrase'
]

################################################################################################
#                                                                                              #
#   Volatility 3 commands list                                                                 #
#                                                                                              #
#       - Windows                                                                              #
#       - Linux                                                                                #
#       - Mac                                                                                  #
#                                                                                              #
#                                                                                              #
################################################################################################

commands_vol3_win = [
    'windows.iat.IAT'         , 'windows.mbrscan.MBRScan'     , 'windows.crashinfo.Crashinfo'             , 'windows.handles.Handles'                        ,
    'windows.ssdt.SSDT'       , 'windows.modscan.ModScan'     , 'windows.driverirp.DriverIrp'             , 'windows.vadinfo.VadInfo'                        ,
    'windows.info.Info'       , 'windows.getsids.GetSIDs'     , 'windows.dumpfiles.DumpFiles'             , 'windows.mftscan.MFTScan'                        ,
    'windows.kpcrs.KPCRs'     , 'windows.netscan.NetScan'     , 'windows.callbacks.Callbacks'             , 'windows.hashdump.Hashdump'                      ,
    'windows.mftscan.ADS'     , 'windows.verinfo.VerInfo'     , 'windows.truecrypt.Passphrase'            , 'windows.joblinks.JobLinks'                      ,
    'windows.pslist.PsList'   , 'windows.malfind.Malfind'     , 'windows.driverscan.DriverScan'           , 'windows.sessions.Sessions'                      ,
    'windows.pedump.PEDump'   , 'windows.vadwalk.VadWalk'     , 'windows.ldrmodules.LdrModules'           , 'windows.cachedump.Cachedump'                    ,
    'windows.psscan.PsScan'   , 'windows.virtmap.VirtMap'     , 'windows.mutantscan.MutantScan'           , 'windows.registry.hivelist.HiveList'             ,
    'windows.pstree.PsTree'   , 'windows.modules.Modules'     , 'windows.devicetree.DeviceTree'           , 'windows.getservicesids.GetServiceSIDs'          ,
    'windows.envars.Envars'   , 'windows.svcdiff.SvcDiff'     , 'windows.statistics.Statistics'           , 'windows.registry.userassist.UserAssist'         ,  
    'windows.timers.Timers'   , 'windows.threads.Threads'     , 'windows.poolscanner.PoolScanner'         , 'windows.processghosting.ProcessGhosting'        ,  
    'windows.memmap.Memmap'   , 'windows.lsadump.Lsadump'     , 'windows.vadyarascan.VadYaraScan'         , 'windows.unloadedmodules.UnloadedModules'        ,
    'windows.cmdline.CmdLine' , 'windows.svcscan.SvcScan'     , 'windows.symlinkscan.SymlinkScan'         , 'windows.hollowprocesses.HollowProcesses'        ,
    'windows.netstat.NetStat' , 'windows.privileges.Privs'    , 'windows.drivermodule.DriverModule'       , 'windows.registry.certificates.Certificates'     ,
    'windows.dlllist.DllList' , 'windows.bigpools.BigPools'   , 'windows.shimcachemem.ShimcacheMem'       , 'windows.suspicious_threads.SupsiciousThreads'   ,
    'windows.strings.Strings' , 'windows.thrdscan.ThrdScan'   , 'windows.registry.hivescan.HiveScan'      , 'windows.skeleton_key_check.Skeleton_Key_Check'  ,
    'windows.svclist.SvcList' , 'windows.filescan.FileScan'   , 'windows.registry.printkey.PrintKey'      , 'windows.registry.getcellroutine.GetCellRoutine' ,
    'windows.psxview.PsXView' 
]

commandes_vol3_win_all = [
    'windows.info.Info'       ,'windows.netscan.NetScan'   , 'windows.mftscan.MFTScan'            ,
    'windows.envars.Envars'   ,'windows.verinfo.VerInfo'   , 'windows.sessions.Sessions'          ,
    'windows.timers.Timers'   ,'windows.malfind.Malfind'   , 'windows.cachedump.Cachedump'        ,
    'windows.pslist.PsList'   ,'windows.lsadump.Lsadump'   , 'windows.truecrypt.Passphrase'       ,
    'windows.psscan.PsScan'   ,'windows.svcscan.SvcScan'   , 'windows.registry.hivescan.HiveScan' ,
    'windows.pstree.PsTree'   ,'windows.filescan.FileScan' , 'windows.registry.printkey.PrintKey' ,
    'windows.cmdline.CmdLine' ,'windows.hashdump.Hashdump' , 'windows.registry.hivelist.HiveList'
]

commands_vol3_linux = [
    'linux.bash.Bash'   , 'linux.psaux.PsAux'       , 'linux.check_idt.Check_idt'      , 'linux.library_list.LibraryList'              ,
    'linux.elfs.Elfs'   , 'linux.envars.Envars'     , 'linux.mountinfo.MountInfo'      , 'linux.capabilities.Capabilities'             ,
    'linux.kmsg.Kmsg'   , 'linux.pslist.PsList'     , 'linux.netfilter.Netfilter'      , 'linux.check_afinfo.Check_afinfo'             ,
    'linux.lsof.Lsof'   , 'linux.psscan.PsScan'     , 'linux.tty_check.tty_check'      , 'linux.check_modules.Check_modules'           ,
    'linux.proc.Maps'   , 'linux.pstree.PsTree'     , 'linux.check_creds.Check_creds'  , 'linux.check_syscall.Check_syscall'           ,
    'linux.iomem.IOMem' , 'linux.malfind.Malfind'   , 'linux.vmayarascan.VmaYaraScan'  , 'linux.keyboard_notifiers.Keyboard_notifiers' ,
    'linux.lsmod.Lsmod' , 'linux.sockstat.Sockstat'
]

commandes_vol3_linux_all = [
    'linux.bash.Bash'   , 'linux.psaux.PsAux'       , 'linux.check_idt.Check_idt'      , 'linux.library_list.LibraryList'              ,
    'linux.elfs.Elfs'   , 'linux.envars.Envars'     , 'linux.mountinfo.MountInfo'      , 'linux.capabilities.Capabilities'             ,
    'linux.kmsg.Kmsg'   , 'linux.pslist.PsList'     , 'linux.netfilter.Netfilter'      , 'linux.check_afinfo.Check_afinfo'             ,
    'linux.lsof.Lsof'   , 'linux.psscan.PsScan'     , 'linux.tty_check.tty_check'      , 'linux.check_modules.Check_modules'           ,
    'linux.proc.Maps'   , 'linux.pstree.PsTree'     , 'linux.check_creds.Check_creds'  , 'linux.check_syscall.Check_syscall'           ,
    'linux.iomem.IOMem' , 'linux.malfind.Malfind'   , 'linux.vmayarascan.VmaYaraScan'  , 'linux.keyboard_notifiers.Keyboard_notifiers' ,
    'linux.lsmod.Lsmod' , 'linux.sockstat.Sockstat'
]

commands_vol3_mac = [
    'mac.bash.Bash'    , 'mac.pslist.PsList'   , 'mac.netstat.Netstat'           , 'mac.kauth_scopes.Kauth_scopes'         ,
    'mac.lsof.Lsof'    , 'mac.pstree.PsTree'   , 'mac.ifconfig.Ifconfig'         , 'mac.check_syscall.Check_syscall'       ,
    'mac.dmesg.Dmesg'  , 'mac.timers.Timers'   , 'mac.vfsevents.VFSevents'       , 'mac.socket_filters.Socket_filters'     ,
    'mac.lsmod.Lsmod'  , 'mac.proc_maps.Maps'  , 'mac.list_files.List_Files'     , 'mac.kauth_listeners.Kauth_listeners'   ,
    'mac.mount.Mount'  , 'mac.kevents.Kevents' , 'mac.trustedbsd.Trustedbsd'     , 'mac.check_trap_table.Check_trap_table' ,
    'mac.psaux.Psaux'  , 'mac.malfind.Malfind' , 'mac.check_sysctl.Check_sysctl'
]

commandes_vol3_mac_all = [
    'mac.bash.Bash'    , 'mac.pslist.PsList'   , 'mac.netstat.Netstat'           , 'mac.kauth_scopes.Kauth_scopes'         ,
    'mac.lsof.Lsof'    , 'mac.pstree.PsTree'   , 'mac.ifconfig.Ifconfig'         , 'mac.check_syscall.Check_syscall'       ,
    'mac.dmesg.Dmesg'  , 'mac.timers.Timers'   , 'mac.vfsevents.VFSevents'       , 'mac.socket_filters.Socket_filters'     ,
    'mac.lsmod.Lsmod'  , 'mac.proc_maps.Maps'  , 'mac.list_files.List_Files'     , 'mac.kauth_listeners.Kauth_listeners'   ,
    'mac.mount.Mount'  , 'mac.kevents.Kevents' , 'mac.trustedbsd.Trustedbsd'     , 'mac.check_trap_table.Check_trap_table' ,
    'mac.psaux.Psaux'  , 'mac.malfind.Malfind' , 'mac.check_sysctl.Check_sysctl'
]

def find_command(struct):
    if struct.vol_version == "vol2":
        for command in commands_vol2:
            if struct.cmd.lower() in command.lower():
                return command

    elif struct.vol_version == "vol3":
        if struct.os_type == "win":
            for command in commands_vol3_win:
                if struct.cmd.lower() in command.lower():
                    return command
        elif struct.os_type == "linux":
            for command in commands_vol3_linux:
                if struct.cmd.lower() in command.lower():
                    return command
        elif struct.os_type == "macos":
            for command in commands_vol3_mac:
                if struct.cmd.lower() in command.lower():
                    return command
    return []


def get_commands(struct):
    if struct.vol_version == "vol2":
        if struct.cmd == "all":
            return commands_vol2_all
        elif struct.cmd != "all" and struct.cmd != "":
            return [find_command(struct.vol_version, struct.os_type, struct.cmd)]
    elif struct.vol_version == "vol3":
        if struct.cmd == "all":
            if struct.os_type == "win":
                return commandes_vol3_win_all
            elif struct.os_type == "linux":
                return commandes_vol3_linux_all
            elif struct.os_type == "macos":
                return commandes_vol3_mac_all
        if struct.cmd != "all" and struct.cmd != "" and struct.os_type == "win":
            return [find_command(struct.vol_version, struct.os_type, struct.cmd)]
        elif struct.cmd != "all" and struct.cmd != "" and struct.os_type == "linux":
            return [find_command(struct.vol_version, struct.os_type, struct.cmd)]
        elif struct.cmd != "all" and struct.cmd != "" and struct.os_type == "macos":
            return [find_command(struct.vol_version, struct.os_type, struct.cmd)]
    else:
        print("${RED}Error: ${NC}Command not found")
        exit(1)
