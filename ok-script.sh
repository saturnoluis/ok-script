#!/bin/bash
fedora_version=$(rpm -E %fedora)

echo "Hello! I will setup your Fedora ${fedora_version} install."

# System update
echo -n "Enable RPM fusion? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$fedora_version.noarch.rpm -y
	sudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$fedora_version.noarch.rpm -y
fi

echo -n "Update system? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	sudo dnf update -y
fi

echo -n "Install media codecs? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	sudo dnf install gstreamer1-plugins-{bad-*,good-*,base} gstreamer1-plugin-openh264 gstreamer1-libav --exclude=gstreamer1-plugins-bad-free-devel -y
	sudo dnf install lame* --exclude=lame-devel -y
	sudo dnf install ffmpeg ffmpeg-libs libva libva-utils --allowerasing -y
	sudo dnf group upgrade --with-optional --allowerasing --skip-broken Multimedia -y
fi

echo -n "Install dnf packages? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	sudo dnf install bat -y
	sudo dnf install curl -y
	sudo dnf install fd-find -y
	sudo dnf install git -y
	sudo dnf install htop -y
	sudo dnf install java-latest-openjdk.x86_64 -y
	sudo dnf install neofetch -y
	sudo dnf install openssh-server -y
	sudo dnf install ranger -y
	sudo dnf install ripgrep -y
	sudo dnf install tmux -y
	sudo dnf install util-linux-user -y
	sudo dnf install vim -y
	sudo dnf install xclip -y
fi

echo -n "Install development tools? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	sudo dnf groupinstall "Development Tools" "Development Libraries" -y
	sudo dnf group install "C Development Tools and Libraries" -y
	sudo dnf install gcc-c++ -y
	sudo dnf install librsvg2-devel -y
	sudo dnf install libsoup-devel -y
	sudo dnf install openssl-devel -y
	sudo dnf install python3-pip -y
fi

echo -n "Remove libreoffice dnf packages? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	sudo dnf remove libreoffice* -y
fi

echo -n "Enable flathub repository? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
	flatpak update
fi

echo -n "Enable flatpak themes? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	mkdir -pv ~/.themes
	sudo flatpak override --filesystem=$HOME/.themes
fi

echo -n "Replace Firefox with flatpak version? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	sudo dnf remove firefox* -y
	flatpak install flathub org.mozilla.firefox -y
	sudo flatpak override org.mozilla.firefox --filesystem=home
fi

echo -n "Install flatpak applications? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	flatpak install flathub com.github.tchx84.Flatseal -y
	flatpak install flathub com.google.Chrome -y
	flatpak install flathub com.microsoft.Edge -y
	flatpak install flathub com.transmissionbt.Transmission -y
	flatpak install flathub re.sonny.Junction -y
fi

echo -n "Install wine? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	sudo dnf config-manager --add-repo https://dl.winehq.org/wine-builds/fedora/$fedora_version/winehq.repo -y
	sudo dnf update -y
	sudo dnf install winehq-stable -y
	sudo dnf install gamemode -y
fi

echo -n "Install GNOME specific packages? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	sudo dnf install gnome-tweaks -y
	sudo dnf install libappindicator-gtk3 -y
	flatpak install org.gtk.Gtk3theme.Adwaita-dark -y
	flatpak install flathub com.mattjakeman.ExtensionManager -y
fi

echo -n "Install node, npm and nvm? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	sudo dnf module install nodejs -y
	wget -N https://raw.githubusercontent.com/creationix/nvm/master/install.sh
	bash install.sh
	rm -r install.sh
	node -v
	npm -v
fi

echo -n "Install rust and cargo? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	curl --proto '=https' --tlsv1.2 -sSf -o rustup.sh https://sh.rustup.rs
	sh rustup.sh -yv
	~/.cargo/bin/cargo -V
	rm rustup.sh
fi

echo -n "Configure git? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	read -p "Enter your email: " email
	read -p "Enter your full name: " name

	git config --global core.editor nvim
	git config --global user.name "$name"
	git config --global user.email "$email"
	git config --global init.defaultBranch main

	echo "Git configuration has been updated:"
	git config --global --list | cat
	echo
fi

echo -n "Generate ssh key? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	read -p "Enter your email: " email

	ssh-keygen -t rsa -b 4096 -C "$email"

	echo "Copy the public key to use with github: https://github.com/settings/ssh/new"
	cat ~/.ssh/id_rsa.pub
	echo
fi

echo -n "Install neovim? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	echo "Be patient, it takes a while..."
	~/.cargo/bin/cargo install --git https://github.com/MordechaiHadad/bob.git
	~/.cargo/bin/bob use 0.9.2
fi

echo -n "Clone neovim config? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	git clone https://github.com/saturnoluis/nvim ~/.config/nvim
fi

echo -n "Install zsh? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	sudo dnf install zsh -y
	wget -N https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh
	bash install.sh --unattended
	rm -f install.sh
fi

echo -n "Import zsh config? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	wget -N https://raw.githubusercontent.com/saturnoluis/ok-script/main/configs/dot.zshrc
	rm -f ~/.zshrc
	mv -f dot.zshrc ~/.zshrc
fi

echo -n "Import tmux config? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	wget -N https://raw.githubusercontent.com/saturnoluis/ok-script/main/configs/dot.tmux.conf
	mv -f dot.tmux.conf ~/.tmux.conf
fi

echo -n "Change shell to zsh? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	chsh -s /usr/bin/zsh
fi

echo -n "Install kitty 🐱? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	wget -N https://sw.kovidgoyal.net/kitty/installer.sh
	bash installer.sh launch=n
	mkdir -p ~/.config/kitty
	wget -N https://raw.githubusercontent.com/saturnoluis/ok-script/main/configs/kitty.conf
	wget -N https://raw.githubusercontent.com/saturnoluis/ok-script/main/configs/theme.conf
	wget -N https://raw.githubusercontent.com/saturnoluis/ok-script/main/configs/kitty.desktop
	mv -f ./kitty.conf ~/.config/kitty/kitty.conf
	mv -f ./kitty.conf ~/.config/kitty/theme.conf
	mv -f ./kitty.desktop ~/.local/share/applications/kitty.desktop
	rm -f installer.sh
fi

echo -n "Change hostname? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	read -p "Enter the new hostname: " hostname
	hostnamectl set-hostname $hostname
fi

echo -n "Enable ssh server? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	sudo systemctl enable sshd
fi

echo "All done!"

echo -n "Reboot system? (y/n): "
read -n 1 input
echo
if [ "$input" = "y" ]; then
	sudo reboot
fi
