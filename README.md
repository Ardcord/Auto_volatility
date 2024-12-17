# Auto_volatility

**⚠️Warning:⚠️** This program is still under development. Some features may not work as expected and could be subject to change.

## Overview

Auto_volatility is a project to set up Docker environments for **Volatility 2** and **Volatility 3**, along with an automated script for memory analysis. The goal is to simplify the process of using Volatility for forensic analysis by running it inside Docker containers, and providing an interactive Python script to automate the process.

## Docker Setup 🐳

This project includes Docker setups for both **Volatility 2** and **Volatility 3**. The Dockerfiles used in this project are inspired by existing work:

- **Volatility 2 Docker:** Built from the original [volatility2docker](https://github.com/p0dalirius/volatility2docker) repository by Podalirius.
- **Volatility 3 Docker:** Based on the official [Volatility 3 Docker setup](https://github.com/sk4la/volatility3-docker) repository by sk4la.

These Docker images allow you to run both Volatility versions in isolated environments with all required dependencies.

### Deployment

To deploy the Docker images for Volatility 2 and Volatility 3, follow the steps below:

**Clone the repository:**
   ```bash
   git clone https://github.com/Ardcord/Auto_volatility.git
   cd Auto_volatility
   chmod +x auto_volatility_setup.sh
   ./auto_volatility_setup.sh
  ```

**Run the Docker containers: You can run the Docker containers.**
  passing the necessary memory dump file for analysis:

    ```bash
    docker run -it --rm -v /path/to/dump:/mnt volatility2-docker -f /mnt/<mem_dump_file> imageinfo
    docker run -it --rm -v /path/to/dump:/mnt volatility3-docker -f /mnt/<mem_dump_file> windows.info
    ```
**Or use the next tools**
    
## vol_auto.py 

The vol_auto.py script automates the process of memory analysis using the Volatility 2 and Volatility 3 Docker containers.

### Features:

    Interactive Command Line Interface (CLI): The script prompts the user for the OS version and commands to run within the Volatility Docker containers.
    Automatic Directory Setup: The script creates an output directory (/tmp/Volatility_auto_output) for storing the results of memory analysis, with separate subdirectories for Volatility 2 and Volatility 3 outputs.
    Command Execution: Users can execute a variety of Volatility commands (both Volatility 2 and Volatility 3) through the interactive shell.

### How to Use:

**Run the Script: After building the Docker containers, you can start the script using the following command:**

  ```bash
  python3 vol_auto.py <path_to_memory_dump>
  ```

**Enter Commands: Once the script starts, it will prompt you to enter commands for Volatility 2 or Volatility 3.**

  ```bash
  File found: ch2.dmp
  Starting Volatility analysis for file: ~/Downloads/test_docker_volatility
  Created output directory: /tmp/Volatility_auto_output
  OS version detected by Volatility:


            Suggested Profile(s) : Win7SP1x86_23418, Win7SP0x86, Win7SP1x86_24000, Win7SP1x86

  Please enter the OS version detected by Volatility: Win7SP1x86_23418
  OS version set to Win7SP1x86_23418
  docker@volatility $
  ```

**For example:**

  ```bash
  docker@volatility $ --help
  # Show help menu

  docker@volatility $ --set-profil
  # To set or re-set profil

  docker@volatility $ vol3 list
  # List all available commands in Volatility 3 (depending on the detected OS version).

  docker@volatility $ vol3 all
  # Execute all tools of volatility 3
  ```

  
Notes:

    The script requires the user to specify the memory dump file path when running it.
    If the OS version is not detected by Volatility, the user will be prompted to manually enter the OS version.

