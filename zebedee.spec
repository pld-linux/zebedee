Summary:	Secure IP Tunnel
Summary(pl):	Bezpieczny tunel IP
Name:		zebedee
Version:	2.4.0
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.winton.org.uk/zebedee/%{name}-%{version}.tar.gz
URL:		http://www.winton.org.uk/zebedee/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _sysconfdir     /etc

%description
Zebedee is a simple program to establish an encrypted, compressed
"tunnel" for TCP/IP or UDP traffic between two systems. This allows
data from, for example, telnet, ftp and X sessions to be protected
from snooping. You can also use compression, either with or without
data encryption, to gain performance over low-bandwidth networks.
Adventage: Win32 version.

%description -l pl
Zebedee jest prostym programem umo¿liwiaj±cym utworzenie szyfrowanego,
kompresowanego w locie tunelu dla ruchu w protokole IP lub UDP
pomiêdzy dwoma systemami komputerowymi. Tunel umo¿liwia zabezpieczenie
przed podsluchem na linii np. sesji telneta, ftpa, sesji okienkowych
X, etc. Du¿ym atutem jest dostêpno¶æ wersji programu dla systemów
Microsoft Windows.

%prep
%setup -q

%build
%{__make}  OS=linux

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
