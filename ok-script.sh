#!/bin/bash

# My data
name="Luis Saturno"
email="saturno.luis@gmail.com"

# Prompt for hostname with a default value
read -p "Enter hostname (default: jupiter): " hostname
hostname=${hostname:-jupiter}

echo -e "\e[42mProcess started...\e[0m\n"

# Function to execute a block of commands
execute_commands() {
    local description="$1"; shift

    echo -e "\e[43m$description\e[0m"
    read -p $'\e[33mContinue to this step? (Y/n): \e[0m' response
    if [[ "$response" == "n" || "$response" == "N" ]]; then
        echo ""
        return
    fi

    for cmd in "$@"; do
        if [[ "$cmd" =~ ^# ]]; then
            echo "${cmd:1}"
            continue
        fi

        echo -e "\e[32mRunning command:\e[0m $cmd"
        if $cmd; then
            echo -e "\e[42mOK\e[0m\n"
        else
            read -p $'\e[33m\nContinue executing the script? (Y/n): \e[0m' response
            if [[ "$response" == "n" || "$response" == "N" ]]; then
                echo -e "\e[41mExecution stopped\e[0m"
                exit 1
            fi
            echo ""
        fi
    done
}

execute_commands_from_file() {
    local file="commands"  # Hardcoded filename
    local description=""
    local commands=()
    
	echo -e "\e[42mReading commands file...\e[0m\n"
    while IFS= read -r line; do
        # Skip blank lines
        if [[ -z "$line" ]]; then
            continue
        fi

        # Check if line starts with >>> to indicate a description
		if [[ "${line:0:3}" == ">>>" ]]; then
            # If description is not empty, execute accumulated commands
            if [[ ! -z "$description" ]]; then
                execute_commands "$description" "${commands[@]}"
                commands=()
            fi
            description="${line:4}"  # Remove leading >>>
        else
            # Accumulate commands
            commands+=("$line")
        fi
    done < "$file"  # Read from hardcoded file

    # Handle any remaining commands
    if [[ ! -z "$description" ]]; then
        execute_commands "$description" "${commands[@]}"
    fi
}

# Call the function
execute_commands_from_file

echo -e "\e[42mEnd of process!\e[0m"
