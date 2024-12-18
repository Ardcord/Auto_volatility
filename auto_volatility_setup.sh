#!/bin/bash

DEFAULT_PATH="${HOME}/.Programs_test" # a remplacer par Volatility_docker apres les tests
CHECK_MARK="\u2713"
CROSS_MARK="\u2717"

# Function to clear the terminal
clear_lines() {
    local num_lines=$1
    for ((i=0; i<num_lines; i++)); do
        echo -e "\033[H\033[J"
    done
}

# Function to print a message with color
print_message() {
    local message=$1
    local color=$2
    echo -e "\033[${color}m${message}\033[0m"
}

# Function to create a directory if it does not exist
create_dir_if_not_exists() {
    local dir_path=$1
    if [ ! -d "$dir_path" ]; then
        print_message "Creating directory $dir_path" "34"
        mkdir -p "$dir_path"
    else
        print_message "Directory $dir_path already exists" "32"
    fi
}

copy_files()
    cp ./vol_auto.py $DEFAULT_PATH/vol_auto.py
    cp ./volatility2_Docker/Dockerfile $DEFAULT_PATH/volatility_2/Dockerfile
    cp ./volatility3_Docker/Dockerfile $DEFAULT_PATH/volatility_3/Dockerfile
    echo "$DEFAULT_PATH/vol_auto.py" >> ~/.bashrc
    source ~/.bashrc

# Build the Docker images
install_docker_images() {
    local docker_repos=("volatility_2" "volatility_3")
    
    for repo in "${docker_repos[@]}"; do
        cd "${DEFAULT_PATH}/${repo}" || exit 1

        print_message "Building Docker image for $repo" "34"

        if ! docker build -t "${repo}-docker" .; then
            print_message "Failed to build Docker image for $repo.   [ $CROSS_MARK ]" "31"
            exit 1
        else
            print_message "Docker image for $repo built successfully.   [ $CHECK_MARK ]" "32"
        fi
    done
}

# Main script logic
clear
print_message "Install in $DEFAULT_PATH" "31"
create_dir_if_not_exists "$DEFAULT_PATH"

install_docker_images

cp ./vol_auto.py $DEFAULT_PATH/vol_auto.py

echo "$DEFAULT_PATH/vol_auto.py" >> ~/.bashrc
source ~/.bashrc
