Name:           skryptos-welcome
Version:        1.0.0
Release:        1%{?dist}
Summary:        SkryptOS Welcome and System Information Package
License:        GPL-2.0-or-later
URL:            https://github.com/SakuraSkrypt/SkryptOS
BuildArch:      noarch

%description
Welcome package for SkryptOS providing system information and branding.
This package includes the SkryptOS welcome documentation and system identifiers.

%prep
%build

%install
mkdir -p %{buildroot}/usr/share/doc/skryptos
mkdir -p %{buildroot}/usr/share/pixmaps
mkdir -p %{buildroot}/etc

cat > %{buildroot}/usr/share/doc/skryptos/WELCOME << 'EOF'
╔═══════════════════════════════════════════════════════════════╗
║                   Welcome to SkryptOS!                        ║
║                                                               ║
║  SkryptOS is a custom Nobara-based Linux distribution         ║
║  optimized for gaming, development, and multimedia work.      ║
║                                                               ║
║  Repository: https://github.com/SakuraSkrypt/SkryptOS        ║
║  Documentation: https://github.com/SakuraSkrypt/SkryptOS     ║
╚═══════════════════════════════════════════════════════════════╝

Getting Started:
- Check /usr/share/doc/skryptos/ for documentation
- Visit the GitHub repository for updates and support
- Report issues at: https://github.com/SakuraSkrypt/SkryptOS/issues

Thank you for using SkryptOS!
EOF

cat > %{buildroot}/etc/os-release.d/skryptos.conf << 'EOF'
# SkryptOS System Information
SKRYPTOS_VERSION=1.0.0
SKRYPTOS_RELEASE_DATE=2025-05-21
EOF

%files
/usr/share/doc/skryptos/WELCOME
/etc/os-release.d/skryptos.conf

%changelog
* Thu May 21 2025 SakuraSkrypt <dev@skryptos.local> - 1.0.0-1
- Initial SkryptOS welcome package
- Added system information files
- Added documentation

%post
echo "SkryptOS installed successfully!"
cat /usr/share/doc/skryptos/WELCOME

%preun
echo "Removing SkryptOS welcome package..."
