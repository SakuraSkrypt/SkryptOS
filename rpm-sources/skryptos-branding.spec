Name:           skryptos-branding
Version:        1.0.0
Release:        1%{?dist}
Summary:        SkryptOS Branding and System Configuration
License:        GPL-2.0-or-later
URL:            https://github.com/SakuraSkrypt/SkryptOS
BuildArch:      noarch

Requires:       nobara-release-kde

%description
System branding and configuration files for SkryptOS.
Provides custom themes, wallpapers, and system settings specific to SkryptOS.

%prep
%build

%install
mkdir -p %{buildroot}/etc/skryptos
mkdir -p %{buildroot}/usr/share/skryptos
mkdir -p %{buildroot}/usr/share/backgrounds/xfce

# Create configuration files
cat > %{buildroot}/etc/skryptos/skryptos.conf << 'EOF'
# SkryptOS Configuration File
# System branding and customization options

# Desktop Environment
DE=kde
THEME=Adwaita-dark

# Performance
ENABLE_GAMEMODE=true
ENABLE_GAMESCOPE=true

# Package Management
REPO_NAME=skryptos
REPO_URL=https://SakuraSkrypt.github.io/SkryptOS/repos/x86_64/
EOF

# Create branding file
cat > %{buildroot}/usr/share/skryptos/branding.ini << 'EOF'
[General]
Name=SkryptOS
Version=1.0.0
ProductName=SkryptOS
BugURL=https://github.com/SakuraSkrypt/SkryptOS/issues
SupportURL=https://github.com/SakuraSkrypt/SkryptOS
WebsiteURL=https://github.com/SakuraSkrypt/SkryptOS
Icon=skryptos
EOF

# Create a simple text file with system info
cat > %{buildroot}/usr/share/skryptos/SYSTEM_INFO << 'EOF'
SkryptOS System Information
===========================

Built on: Nobara (Fedora-based)
Edition: Standard
Architecture: x86_64
Repository: https://github.com/SakuraSkrypt/SkryptOS

For support and issues, please visit:
https://github.com/SakuraSkrypt/SkryptOS/issues
EOF

%files
/etc/skryptos/skryptos.conf
/usr/share/skryptos/branding.ini
/usr/share/skryptos/SYSTEM_INFO

%changelog
* Thu May 21 2025 SakuraSkrypt <dev@skryptos.local> - 1.0.0-1
- Initial branding package
- Added system configuration files
- Added branding information

%post
echo "SkryptOS branding applied!"

%postun
echo "SkryptOS branding removed"
