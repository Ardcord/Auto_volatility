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

# Function to download the files
download_file() {
    local repos=("https://github.com/sk4la/volatility3-docker.git ${DEFAULT_PATH}/temp_volatility_3" "https://github.com/p0dalirius/volatility2docker.git ${DEFAULT_PATH}/temp_volatility_2")
    
    for repo in "${repos[@]}"; do
        repo_url=$(echo "$repo" | awk '{print $1}')
        repo_dir=$(echo "$repo" | awk '{print $2}')
        
        if [ -d "$repo_dir" ]; then
            print_message "Directory $repo_dir already exists. Skipping clone.   [ $CHECK_MARK ]" "32"
        else
            git clone "$repo_url" "$repo_dir"
            if [[ $? -ne 0 ]]; then
                print_message "Failed to clone repository $repo_url.   [ $CROSS_MARK ]" "31"
                exit 1
            else
                print_message "Repository $repo_url cloned successfully.   [ $CHECK_MARK ]" "32"
            fi
        fi
    done
}

# Patch the files and organize them
patch_file() {
    create_dir_if_not_exists "${DEFAULT_PATH}/volatility_3"
    create_dir_if_not_exists "${DEFAULT_PATH}/volatility_2"

    local temp_volatility_3="${DEFAULT_PATH}/temp_volatility_3"
    if [ ! -d "$temp_volatility_3" ]; then
        print_message "Directory temp_volatility_3 not found. Aborting." "31"
        exit 1
    fi

    cp "${temp_volatility_3}/src/volatility3/Dockerfile" "${DEFAULT_PATH}/volatility_3/"
    cp "${temp_volatility_3}/LICENSE" "${DEFAULT_PATH}/volatility_3/"
    cp "${temp_volatility_3}/README.md" "${DEFAULT_PATH}/volatility_3/README_sk4la.md"
    cp -r "${temp_volatility_3}/src/volatility3/assets" "${DEFAULT_PATH}/volatility_3/assets"

    local temp_volatility_2="${DEFAULT_PATH}/temp_volatility_2"
    if [ ! -d "$temp_volatility_2" ]; then
        print_message "Directory temp_volatility_2 not found. Aborting." "31"
        exit 1
    fi

    cp "${temp_volatility_2}/Dockerfile" "${DEFAULT_PATH}/volatility_2/"
    cp "${temp_volatility_2}/README.md" "${DEFAULT_PATH}/volatility_2/README_p0dalirius.md"

    sed -i 's|CMD /bin/bash|ENTRYPOINT ["python2", "/volatility/vol.py"]|' "${DEFAULT_PATH}/volatility_2/Dockerfile"

    rm -rf "$temp_volatility_3" "$temp_volatility_2"
}

# Build the Docker images
install_docker_images() {
    local docker_repos=("volatility_3" "volatility_2")
    
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
download_file
patch_file
install_docker_images

cp ./vol_auto.py $DEFAULT_PATH/vol_auto.py

echo "$DEFAULT_PATH/vol_auto.py" >> ~/.bashrc
source ~/.bashrc
