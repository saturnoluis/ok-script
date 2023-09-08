#!/bin/bash

echo "Hello! I will setup your Fedora install."

# System update
echo "Enable RPM fusion? (y/n)"
read input
if [ "$input" = "y" ]; then
	sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm -y
	sudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm -y
fi

echo "Update system? (y/n)"
read input
if [ "$input" = "y" ]; then
	sudo dnf update -y
fi

echo "All done!"
