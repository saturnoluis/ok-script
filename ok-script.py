import subprocess

# My data
name = "Luis Saturno"
email = "saturno.luis@gmail.com"
hostname = "jupiter"

# List of commands to be executed 
commands = [

    ">>> Update system packages",
    "sudo dnf update -y",

    ">>> Enable RPM fusion",
    "sudo rpm -Uvh http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm",
    "sudo rpm -Uvh http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm",
    "sudo dnf update -y",

    ">>> Install media codecs",
    "sudo dnf install gstreamer1-plugins-{bad-\\*,good-\\*,base} gstreamer1-plugin-openh264 gstreamer1-libav --exclude=gstreamer1-plugins-bad-free-devel -y",
    "sudo dnf install lame\\* --exclude=lame-devel -y",
    "sudo dnf install ffmpeg ffmpeg-libs libva libva-utils --allowerasing -y",
    "sudo dnf group upgrade --with-optional Multimedia -y",

    ">>> Remove libreoffice dnf packages",
    "sudo dnf remove libreoffice\\* -y",

    ">>> Install dnf packages",
    "sudo dnf copr enable zeno/scrcpy -y",
    "sudo dnf install bat -y",
    "sudo dnf install curl -y",
    "sudo dnf install fd-find -y",
    "sudo dnf install git -y",
    "sudo dnf install gnome-tweaks -y",
    "sudo dnf install htop -y",
    "sudo dnf install java-latest-openjdk.x86_64 -y",
    "sudo dnf install libappindicator-gtk3 -y",
    "sudo dnf install neofetch -y",
    "sudo dnf install openssh-server -y",
    "sudo dnf install python3-pip -y",
    "sudo dnf install ranger -y",
    "sudo dnf install ripgrep -y",
    "sudo dnf install scrcpy -y",
    "sudo dnf install util-linux-user -y",
    "sudo dnf install vim -y",

    ">>> Install development tools and libraries",
    "sudo dnf groupinstall \"Development Tools\" \"Development Libraries\" -y",
    "sudo dnf group install \"C Development Tools and Libraries\" -y",
    "sudo dnf install gcc-c++ -y",
    "sudo dnf install gtk3-devel -y",
    "sudo dnf install javascriptcoregtk4.0 -y",
    "sudo dnf install javascriptcoregtk4.0-devel -y",
    "sudo dnf install librsvg2-devel -y",
    "sudo dnf install libsoup-devel -y",
    "sudo dnf install openssl-devel -y",
    "sudo dnf install webkit2gtk4.0 webkit2gtk4.0-devel -y",

    ">>> Install nice-looking fonts",
    "sudo dnf install -y 'google-roboto*' 'mozilla-fira*' fira-code-fonts",

    ">>> Enable flathub repository",
    "flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo",
    "flatpak update",

    ">>> Enable flatpak themes",
    "mkdir -pv ~/.themes",
    "sudo flatpak override --filesystem=$HOME/.themes", 
    "flatpak install org.gtk.Gtk3theme.Adwaita-dark -y",

    ">>> Replace Firefox with flatpak version",
    "sudo dnf remove firefox\\* -y",
    "flatpak install flathub org.mozilla.firefox -y",
    "sudo flatpak override org.mozilla.firefox --filesystem=home",

    ">>> Install flatpak applications",
    "flatpak install flathub com.github.tchx84.Flatseal -y",
    "flatpak install flathub com.google.Chrome -y",
    "flatpak install flathub com.mattjakeman.ExtensionManager -y",
    "flatpak install flathub com.microsoft.Edge -y",
    "flatpak install flathub com.transmissionbt.Transmission -y",
    "flatpak install flathub re.sonny.Junction -y",

    ">>> Install wine",
    "sudo dnf config-manager --add-repo https://dl.winehq.org/wine-builds/fedora/38/winehq.repo -y",
    "sudo dnf update -y",
    "sudo dnf install winehq-stable -y",
    "sudo dnf install gamemode -y",

    ">>> Install node, npm and nvm",
    "sudo dnf module install nodejs:18/common -y",
    "wget -N https://raw.githubusercontent.com/creationix/nvm/master/install.sh",
    "bash install.sh",
    "rm -r install.sh",
    "node -v",
    "npm -v",

    ">>> Install rust and cargo",
    "curl --proto '=https' --tlsv1.2 -sSf -o rustup.sh https://sh.rustup.rs",
    "sh rustup.sh -yv",
    "~/.cargo/bin/cargo -V",
    "rm rustup.sh",

    ">>> Configure git",
    "git config --global core.editor nvim",
    "git config --global user.name \"" + name + "\"",
    "git config --global user.email \"" + email + "\"",
    "git config --global init.defaultBranch main",

    ">>> Generate ssh keys",
    "ssh-keygen -t rsa -b 4096 -C \"" + email + "\"",
    "# Copy the public key to use with github...",
    "# https://github.com/settings/ssh/new",
    "cat ~/.ssh/id_rsa.pub",

    ">>> Install neovim",
    "~/.cargo/bin/cargo install --git https://github.com/MordechaiHadad/bob.git",
    "~/.cargo/bin/bob use 0.9.0",

    ">>> Clone neovim config",
    "git clone https://github.com/saturnoluis/nvim ~/.config/nvim", 

    ">>> Install zsh",
    "sudo dnf install zsh -y",
    "wget -N https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh",
    "bash install.sh --unattended",
    "rm -r install.sh",

    ">>> Import zsh config",
    "wget -N https://raw.githubusercontent.com/saturnoluis/ok-script/main/configs/dot.zshrc",
    "rm -f ~/.zshrc",
    "mv -f dot.zshrc ~/.zshrc",

    ">>> Import tmux config",
    "wget -N https://raw.githubusercontent.com/saturnoluis/ok-script/main/configs/dot.tmux.conf",
    "mv -f dot.tmux.conf ~/.tmux.conf", 

    ">>> Change shell to zsh",
    "# Enter your password and hit enter to continue...",
    "chsh -s /usr/bin/zsh",

    ">>> Set hostname to " + hostname,
    "hostnamectl set-hostname " + hostname,

    ">>> Enable ssh server",
    "sudo systemctl enable sshd",

    ">>> Reboot system",
    "sudo reboot",

    "END"
]

ignore_next = False

print("\033[42m" + "Process started..." + "\033[0m" + "\n")

# Start executing the list of commands 
for command in commands:

    # Identify the start of a block of commands by the ">>>" srting
    if command[:3] == ">>>":
        # By default we're assumming we won't ignore commands in the block
        ignore_next = False
        print("\033[43m" + command + "\033[0m")

        # Ask the user if they want to continue executing this block
        response = input("\033[33m" + "Continue to this step? (Y/n): " + "\033[0m")
        if response.lower() == "n":
            print("\n")
            ignore_next = True

        # Continue to the next command in the list
        continue

    # Print comments or instructions
    if command[:2] == "# " and ignore_next != True:
        print(command[2:])
        continue

    # This allows to know if the script has ended
    if command == "END":
        print("\033[42m" + "End of process!" + "\033[0m")
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
        if process.stdout is not None:
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
        if process.stderr is not None:
            error = process.stderr.read()
            print("\033[41m" + "Error:" + "\033[0m", error)

        # And ask the user if they whish to continue
        response = input("\033[33m" + "\nContinue executing the the script? (Y/n): " + "\033[0m")

        if response.lower() == "n":
            # If not, then stop the execution 
            print("\033[41m" + "Execution stopped" + "\033[0m")
            break
        else:
            print("\n")

