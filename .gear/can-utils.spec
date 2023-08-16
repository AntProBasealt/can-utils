%define _unpackaged_files_terminate_build 1

Name: can-utils
Version: 2023.03
Release: alt1.gitcfe4196
Summary: SocketCAN userspace utilities and tools
License: %gpl2only
Group: Development/Other
Url: https://github.com/linux-can/can-utils
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses cmake gcc

%description
CAN is a message-based network protocol designed for vehicles originally
created by Robert Bosch GmbH. SocketCAN is a set of open source CAN
drivers and a networking stack contributed by Volkswagen Research to
the Linux kernel.

This package contains some user space utilities for Linux SocketCAN subsystem.

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmakeinstall_std PREFIX=%_prefix DESTDIR=%buildroot

%files
%_bindir/*
%doc README.md


%changelog
* Wed Aug 16 2023 Anton Protopopov <antpro@altlinux.org> 2023.03-alt1.gitcfe4196
- Initial package

