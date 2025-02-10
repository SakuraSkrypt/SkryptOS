# SkryptOS APT Repository

This is the official APT repository for SkryptOS. It provides custom packages, system updates,and enhancements while maintaining compatibility.

## Adding SkryptOS Repository to Your System

To use this repository, follow these steps:

### Import the GPG Key

Run the following command to import the repository's signing key:

'''bash
wget -qO - https://github.com/SakuraSkrypt/SkryptOS-Repo/raw/main/public.gpg | sudo tee /etc/apt/trusted.gpg.d/skryptos.gpg > /dev/null

### Add the Repository

For SkryptOS Stable users:

echo "deb [signed-by=/etc/apt/trusted.gpg.d/skryptos.gpg] https://raw.githubusercontent.com/SakuraSkrypt/SkryptOS-Repo/main dists/stable/main | sudo tee /etc/apt/sources.list.d/skryptos.list

For SkryptOS Testing users:

echo "deb [signed-by=/etc/apt/trusted.gpg.d/skryptos.gpg] https://raw.githubusercontent.com/SakuraSkrypt/SkryptOS-Repo/main dists/testing/main | sudo tee /etc/apt/sources.list.d/skryptos.list

### Update Package Lists

sudo apt update

Now you can install packages from the SkryptOS repository

### Installing Packages

After adding the repository, install packages with:
sudo apt install <package-name>
Example:
sudo apt install skryptos-desktop

## Repository Structure

dists/stable/main/binary-amd64/ -> Stable release packages

dists/testing/main/binary-amd64/ -> Testing branch packages

pool/main/ -> Main package storage

db/ -> Repository metadata

## Contributing
To contribute, fork this repo, upload .deb packages, and create a pull request.

# SkryptOS Designed for Efficiency
