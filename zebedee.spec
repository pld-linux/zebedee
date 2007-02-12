Summary:	Secure IP Tunnel
Summary(pl.UTF-8):   Bezpieczny tunel IP
Name:		zebedee
Version:	2.4.1
Release:	2
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.winton.org.uk/zebedee/%{name}-%{version}.tar.gz
# Source0-md5:	d17a556b966b7b8b1a199b2078e32780
Patch0:		%{name}-patch
Patch1:		%{name}-LDFLAGS.patch
URL:		http://www.winton.org.uk/zebedee/
BuildRequires:	bzip2-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	perl-tools-pod
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zebedee is a simple program to establish an encrypted, compressed
"tunnel" for TCP/IP or UDP traffic between two systems. This allows
data from, for example, telnet, FTP and X sessions to be protected
from snooping. You can also use compression, either with or without
data encryption, to gain performance over low-bandwidth networks.
Adventage: Win32 version.

%description -l pl.UTF-8
Zebedee jest prostym programem umożliwiającym utworzenie szyfrowanego,
kompresowanego w locie tunelu dla ruchu w protokole IP lub UDP
pomiędzy dwoma systemami komputerowymi. Tunel umożliwia zabezpieczenie
przed podsluchem na linii np. sesji telneta, FTP-a, sesji okienkowych
X, etc. Dużym atutem jest dostępność wersji programu dla systemów
Microsoft Windows.

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
%{__make} \
	OS=linux \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	OPTIM="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	ROOTDIR=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	OS=linux

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt *.zbd
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
