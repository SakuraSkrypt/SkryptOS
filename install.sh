#!/bin/bash
set -e # Stop on errors
echo "SkryptOS Installer"

# Update System
apt update && apt upgrade -y

# Add SkryptOS Repository & GPG Key
wget -qO - https://github.com/SakuraSkrypt/SkryptOS-Repo/raw/main/public.gpg | sudo tee /etc/apt/trusted.gpg.d/skryptos > /dev/null
echo "deb [signed-by=/etc/apt/trusted.gpg.d/skryptos.gpg] https://raw.githubusercontent.com/SakuraSkrypt/SkryptOS-Repo/main dists/stable/main" | sudo tee /etc/apt/sources.list.d/skryptos.list
apt update

# Install Base System (KDE, Core Packages)
apt install -y \
    plasma-desktop sddm dolphin konsole latte-dock ark neofetch \
    flatpak pipewire pipewire-pulse wireplumber curl wget unzip \
    sudo nano xz-utils xclip network-manager kde-config-screenlocker \
    kdeplasma-addons plasma-pa plasma-nm kdeconnect firefox-esr \
    ark gwenview okular spectacle kate filelight kcalc partitionmanager \
    systemsettings synaptic ksysguard kcron krename qt5ct vlc mpv

# Install Gaming Support
apt install -y \
    steam lutris gamemode wine winetricks mesa-utils \
    libvulkan1 libgl1-mesa-dri libglx-mesa0 libx11-6 x11-utils \
    protontricks mangohud vkbasalt

# Install Development & Power Tools
apt install -y \
    build-essential cmake mkae gcc g++ python3 python3-pip \
    git-lfs gdb valgrind wget curl jq htop btop

### Install System Optimizations
apt install -y \
    preload cpufrequtils powertop tlp nvtop thermald irqbalance

### Install Virtualization & Containers
apt install -y \
    qemu-kvm libvirt-daemon-system virt-manager docker.io

### Enable Gaming & Performance Optimizations
systemctl enable gamemode
systemctl enable preload
systemctl enable tlp
systemctl enable irqbalance

### Apply SkryptOS Theming & KDE Customisation
mkdir -p /etc/skryptos
cd /etc/skryptos
wget -q https://raw.githubusercontent.com/SakuraSkrypt/SkryptOS-Repo/main/configs.tar.gz
tar -xzf configs.tar.gz
rm configs.tar.gz

mkdir -p ~/.local/share/plasma ~/.config
cp -r /etc/skryptos/plasma ~/.local/share/plasma
cp-r /etc/skryptos/config/* ~/.config/

# Set SkryptOS Branding (Boot, Login, Wallpapers)
mkdir -p /usr/share/sddm/themes
cp -r /etc/skryptos/sddm-theme /usr/share/sddm/themes/skryptos
echo -e "[Theme]\nCurrent=skryptos" > /etc/sddm.conf
systemctl enable sddm

# Set Up Flatpack & Extra Apps
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# Cleanup & Finish
apt autoremove -y && apt clean
echo "SkryptOS Installation Complete! Reboot to apply changes."
