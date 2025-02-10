# SkryptOS APT Repository

This is the official APT repository for SkryptOS. It provides custom packages, system updates,and enhancements while maintaining compatibility.

## Adding SkryptOS Repository to Your System

To use this repository, follow these steps:

### Import the GPG Key
Run the following command to import the repository's signing key:

'''bash
wget -qO - https://github.com/SakuraSkrypt/SkryptOS-Repo/raw/main/public.gpg | sudo tee /etc/apt/trusted.gpg.d/skryptos.gpg > /dev/null
