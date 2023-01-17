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

    ">>> Uninstall packages",
    "sudo apt remove drawing -y",
    "sudo apt remove hexchat* -y",
    "sudo apt remove hypnotix -y",
    "sudo apt remove celluloid -y",
    "sudo apt remove rhythmbox* -y",
    "sudo apt remove thunderbird* -y",
    "sudo apt remove transmission* -y",
    "sudo apt remove libreoffice-* -y",
    "sudo apt remove webapp-manager -y",
    "sudo apt autoremove -y",

    ">>> Install packages",
    "sudo apt install git -y",
    "sudo apt install vim -y",
    "sudo apt install ssh -y",
    "sudo apt install curl -y",
    "sudo apt install htop -y",
    "sudo apt install ranger -y",
    "sudo apt install remmina -y",
    "sudo apt install neofetch -y",
    "sudo apt install python3-pip -y",
    "sudo apt install python3-dev -y",
    
    ">>> Install node, npm and nvm",
    "sudo apt install nodejs -y",
    "sudo apt install npm -y",
    "wget -N https://raw.githubusercontent.com/creationix/nvm/master/install.sh",
    "bash install.sh",
    "rm install.sh",

    ">>> Configure git",
    "git config --global core.editor nvim",
    "git config --global user.name \"" + name + "\"",
    "git config --global user.email \"" + email + "\"",

    ">>> Install neovim",
    "sudo apt-get install software-properties-common -y",
    "sudo add-apt-repository ppa:neovim-ppa/stable -y",
    "sudo apt-get update",
    "sudo apt-get install neovim -y",

    ">>> Import neovim config",
    "wget -N https://raw.githubusercontent.com/saturnoluis/ok-script/main/init.lua",
    "mkdir -p ~/.config/nvim",
    "mv -f init.lua ~/.config/nvim",

    ">>> Install and configure zsh",
    "sudo apt install zsh -y",
    "wget -N https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh",
    "bash install.sh --unattended",
    "wget -N https://raw.githubusercontent.com/saturnoluis/ok-script/main/zshrc",
    "mv -f zshrc ~/.zshrc",
    "rm install.sh",

    ">>> Default to zsh (enter password and hit enter to continue)",
    "chsh -s /usr/bin/zsh",

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

    # This allows to know if the script has ended
    if command == "END":
        print("\n" + "\033[42m" + "End of process!" + "\033[0m")
        break

    # Don't run the next commands if the user decided to skip
    if ignore_next == True:
        continue

    # Run the command
    print ("\033[32m" + "Running command:" + "\033[0m", command)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Show real-time output of the command
    while True:
        output = process.stdout.readline()
        if output:
            print(output.decode().strip())
        return_code = process.poll()
        if return_code is not None:
            break

    # When the command runs successfully
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

