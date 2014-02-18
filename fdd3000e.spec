Summary:	FDD 3000 emulator
Name:		fdd3000e
Version:	0.1.6a
Release:	1
License:	GPL v2+
Group:		Applications/Emulators
Source0:	http://downloads.sourceforge.net/fdd3000e/%{name}_v%{version}.zip
# Source0-md5:	4d1eca31e0b3787f8214b9d5302a6d7e
Patch0:		z80ex.patch
URL:		http://fdd3000e.sourceforge.net/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	qt4-qmake
BuildRequires:	unzip
BuildRequires:	z80ex-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FDD3000 Emulator is an emulator of Timex FDD3000 floppy system
for ZX Spectrum. The current version is the alpha version
of the emulator (for testing). It requires patched fuse emulator.

%prep
%setup -q -c %{name}-%{version}
%patch0 -p1

%build
cd fdd3000
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install fdd3000/fdd3000 $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc fdd3000/disk.img README README_pl
%attr(755,root,root) %{_bindir}/fdd3000
