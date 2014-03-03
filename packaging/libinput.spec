Name:           libinput
Version:        0.1.0
Release:        0
License:        MIT
Summary:        Input devices for display servers and other applications
Url:            http://www.freedesktop.org/software/libinput/libinput-%{version}.tar.xz
Group:          System/Libraries
Source:         %{name}-%{version}.tar.gz
#X-Vcs-Url:      git://anongit.freedesktop.org/wayland/libinput

BuildRequires:  make
BuildRequires:  pkgconfig(check) >= 0.9.9
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(mtdev)


%description

libinput is a library that handles input devices for display servers and
other applications that need to directly deal with input devices.

It provides device detection, device handling, input device event
processing and abstraction so minimize the amount of custom input
code the user of libinput need to provide the common set of
functionality that users expect.


%package devel
Summary:    Input devices for display servers and other applications
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel

libinput is a library that handles input devices for display servers and
other applications that need to directly deal with input devices.

It provides device detection, device handling, input device event
processing and abstraction so minimize the amount of custom input
code the user of libinput need to provide the common set of
functionality that users expect.

%prep
%setup -q

%autogen \
    --enable-tests \
    #eol

%build
make %{?jobs:-j%jobs} V=1

%check
make %{?jobs:-j%jobs} tests check V=1

%install
%make_install
install -d %{_libdir}/%{name}/test
install -m 0755 test/test-log %{_libdir}/%{name}/test
install -m 0755 test/test-path %{_libdir}/%{name}/test
install -m 0755 test/test-pointer %{_libdir}/%{name}/test
install -m 0755 test/test-touch %{_libdir}/%{name}/test
install -m 0755 test/test-udev %{_libdir}/%{name}/test

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root)
%{_libdir}/*.so.*


%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%file test
%{_libdir}/%{name}/test/*

