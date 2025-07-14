%define		subver	2
Summary:	FDD 3000 emulator
Summary(pl.UTF-8):	Emulator FDD 3000
Name:		fdd3000e
Version:	0.1.6a
Release:	2
License:	GPL v2+
Group:		Applications/Emulators
Source0:	http://downloads.sourceforge.net/fdd3000e/%{name}_v%{version}-%{subver}.zip
# Source0-md5:	bf1d20cb68cc116dd9aa880676877ef8
Patch0:		z80ex.patch
Patch1:		tr.patch
URL:		http://fdd3000e.sourceforge.net/
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	qt4-qmake >= 4
BuildRequires:	unzip
BuildRequires:	z80ex-devel >= 1.1.20
Requires:	z80ex >= 1.1.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FDD3000 Emulator is an emulator of Timex FDD3000 floppy system
for ZX Spectrum. The current version is the alpha version
of the emulator (for testing). It requires patched fuse emulator.

%description -l pl.UTF-8
FDD3000 Emulator to emulator systemu dyskietek Timex FDD3000 dla ZX
Spectrum. Bieżąca wersja jest wersją alfa emulatora (przeznaczoną do
testów). Wymaga emulatora fuse z odpowiednią łatką.

%prep
%setup -q -c
%patch -P0 -p1
%patch -P1 -p1

%build
cd fdd3000
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install fdd3000/fdd3000 $RPM_BUILD_ROOT%{_bindir}
install fdd3000/*.qm $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc fdd3000/disk.img README
%lang(pl) %doc README_pl
%attr(755,root,root) %{_bindir}/fdd3000
%dir %{_datadir}/%{name}
%lang(pl) %{_datadir}/%{name}/fdd3000e_pl_PL.qm
