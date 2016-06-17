Summary:	Xml2po and vice versa converters for KDE
Name:		poxml
Version:	16.04.2
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
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

%files
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
