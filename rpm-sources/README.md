# SkryptOS RPM Sources

This directory contains RPM spec files and sources for building SkryptOS packages.

## Repository Structure

```
rpm-sources/
├── *.spec              # RPM spec files
├── *.tar.gz            # Source tarballs (if needed)
└── README.md           # This file
```

## Building Locally

```bash
# Install build dependencies
sudo dnf install -y rpm-build fedora-packager rpmdevtools

# Setup build environment
rpmdev-setuptree

# Build a package
rpmbuild -ba rpm-sources/skryptos-welcome.spec
```

## Adding New Packages

1. Create a new `.spec` file in this directory
2. Push to main branch
3. GitHub Actions will automatically build and deploy to the repository

### Spec File Template

```spec
Name:           package-name
Version:        1.0.0
Release:        1%{?dist}
Summary:        Short description
License:        GPL-2.0-or-later
URL:            https://example.com
BuildArch:      noarch

%description
Longer description of the package.

%prep
%build
%install
# Installation steps

%files
# Files to include in package

%changelog
* Thu May 21 2025 SakuraSkrypt - 1.0.0-1
- Initial release
```

## Repository URLs

- **x86_64 packages**: `https://SakuraSkrypt.github.io/SkryptOS/repos/x86_64/`
- **Source RPMs**: `https://SakuraSkrypt.github.io/SkryptOS/repos/SRPMS/`

## Usage in Kickstart

Add to your `.ks` file:

```kickstart
repo --name="skryptos" --baseurl=https://SakuraSkrypt.github.io/SkryptOS/repos/x86_64/ --cost=99
```

Then install packages:

```kickstart
%packages
skryptos-welcome
skryptos-branding
@your-other-packages
%end
```

## Current Packages

- **skryptos-welcome**: Welcome and system information
- **skryptos-branding**: System branding and configuration

## Building Status

See [GitHub Actions](https://github.com/SakuraSkrypt/SkryptOS/actions) for build logs.
