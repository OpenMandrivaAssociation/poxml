%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	Xml2po and vice versa converters for KDE
Name:		poxml
Version:	19.12.1
Release:	2
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	gettext-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Xml)
Suggests:	md5deep
Conflicts:	kdesdk4-po2xml < 1:4.11.0
Obsoletes:	kdesdk4-po2xml < 1:4.11.0

%description
Xml2po and vice versa converters for KDE.

%files -f all.lang
%{_bindir}/po2xml
%{_bindir}/split2po
%{_bindir}/swappo
%{_bindir}/xml2pot
%{_mandir}/man1/po2xml.1.*
%{_mandir}/man1/split2po.1.*
%{_mandir}/man1/swappo.1.*
%{_mandir}/man1/xml2pot.1.*

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang po2xml --with-man
%find_lang split2po --with-man
%find_lang swappo --with-man
%find_lang xml2pot --with-man
cat *.lang >all.lang
