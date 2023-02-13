import subprocess

# My data
name = "Luis Saturno"
email = "saturno.luis@gmail.com"

# List of commands to be executed 
commands = [

    ">>> APT packages update",
    "sudo mkdir -p /var/lib/dpkg",
    "sudo touch -c -m /var/lib/dpkg/status",
    "sudo apt update",
    "sudo dpkg --configure -a",
    "sudo apt upgrade -y",

    ">>> Remove preinstalled applications",
    "# Remove some UI apps that are preinstalled in linux mint",
    "sudo apt remove celluloid -y",
    "sudo apt remove drawing -y",
    "sudo apt remove hexchat* -y",
    "sudo apt remove hypnotix -y",
    "sudo apt remove libreoffice-* -y",
    "sudo apt remove rhythmbox* -y",
    "sudo apt remove thunderbird* -y",
    "sudo apt remove transmission* -y",
    "sudo apt remove webapp-manager -y",
    "sudo apt autoremove -y",

    ">>> Install ubuntu-restricted-extras",
    "# sudo apt install ubuntu-restricted-extras -y",
    "echo Please run this one manually",

    ">>> Install build-essential",
    "sudo apt install build-essential -y",

    ">>> Install packages",
    "sudo apt install bat -y",
    "sudo apt install caffeine -y",
    "sudo apt install chrome-gnome-shell -y",
    "sudo apt install curl -y",
    "sudo apt install fd-find -y",
    "sudo apt install git -y",
    "sudo apt install htop -y",
    "sudo apt install neofetch -y",
    "sudo apt install python3-dev -y",
    "sudo apt install python3-pip -y",
    "sudo apt install ranger -y",
    "sudo apt install ssh -y",
    "sudo apt install vim -y",
    
    ">>> Install node, npm and nvm",
    "sudo apt install nodejs -y",
    "sudo apt install npm -y",
    "wget -N https://raw.githubusercontent.com/creationix/nvm/master/install.sh",
    "bash install.sh",
    "rm -r install.sh",

    ">>> Install rust and cargo",
    "curl --proto '=https' --tlsv1.2 -sSf -o rustup.sh https://sh.rustup.rs",
    "sh rustup.sh -yv",
       
    ">>> Install neovim",
    ".cargo/bin/cargo install --git https://github.com/MordechaiHadad/bob.git",
    ".cargo/bin/bob use 0.8.0",

    ">>> Import neovim config",
    "wget -N https://raw.githubusercontent.com/saturnoluis/nvim/main/init.lua",
    "mkdir -p ~/.config/nvim",
    "mv -f init.lua ~/.config/nvim",

    ">>> Install zsh",
    "sudo apt install zsh -y",
    "wget -N https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh",
    "bash install.sh --unattended",
    "rm -r install.sh",

    ">>> Import zsh config",
    "wget -N https://raw.githubusercontent.com/saturnoluis/ok-script/main/configs/zshrc",
    "rm -f ~/.zshrc",
    "mv -f zshrc ~/.zshrc",

    ">>> Change shell to zsh",
    "# Enter your password and hit enter to continue...",
    "chsh -s /usr/bin/zsh",

    ">>> Configure git",
    "git config --global core.editor nvim",
    "git config --global user.name \"" + name + "\"",
    "git config --global user.email \"" + email + "\"",
    "git config --global init.defaultBranch main",

    "END"
]

ignore_next = False

print("\033[42m" + "Process started..." + "\033[0m" + "\n")

# Start executing the list of commands 
for command in commands:
    # Identify the start of a command's block by the ">>>" srting
    if command[:3] == ">>>":
        # By default we're assumming we won't ignore next commands
        ignore_next = False
        print("\033[43m" + command + "\033[0m")
        # Ask the user if they want to continue executing this step
        response = input("\033[33m" + "Continue to this step? (Y/n): " + "\033[0m")
        if response.lower() == "n":
            ignore_next = True
        # Continue to the next command in the list
        continue

    # Print comments or instructions
    if command[:2] == "# ":
        print(command[2:])
        continue

    # This allows to know if the script has ended
    if command == "END":
        print("\n" + "\033[42m" + "End of process!" + "\033[0m")
        break

    # Don't run the next commands if the user decided to skip
    if ignore_next == True:
        continue

    # Print the command to run if is not an echo
    if command[:4] != "echo":
        print ("\033[32m" + "Running command:" + "\033[0m", command)

    # Run the command
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Show real-time output of the command
    while True:
        output = process.stdout.readline()
        if output:
            print(output.decode().strip())
        return_code = process.poll()
        if return_code is not None:
            break

    # Print OK when the command runs successfully
    if return_code == 0:
        print("\033[42m" + "OK" + "\033[0m" + "\n")

    # When something went wrong
    else:
        # Show the error...
        error = process.stderr.read()
        print("\033[41m" + "Error:" + "\033[0m", error)

        # And ask the user if they whish to continue
        response = input("\033[33m" + "Continue executing the the script? (Y/n): " + "\033[0m")

        if response.lower() == "n":
            # If not, then stop the execution 
            print("\033[41m" + "Execution stopped" + "\033[0m")
            break

