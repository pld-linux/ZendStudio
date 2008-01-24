Summary:	ZendStudio - server management tools for PHP-based Web serwers
Summary(pl.UTF-8):	ZendStudio - narzędzia do zarządzania serwerami WWW opartymi o PHP
Name:		ZendStudio
Version:	5.5.0a
Release:	0.1
License:	Zend Studio License
Group:		Applications
Source0:	ZendStudio-5_5_0a.tar.gz
# NoSource0-md5:	6a13b22bc6acf92dd97df1cfc5758e16
NoSource:	0
URL:		http://www.zend.com/products/zend_studio
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	%{_prefix}/share/Zend

%description
Includes server management tools that manage PHP based Web servers.
This module makes installation and integration seamless while
simplifying PHP and remote debugging configurations and security
maintenance.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia do zarządzania serwerami WWW opartymi o
PHP. Moduł pozwala na przezroczystą instalację i integrację,
jednocześnie upraszczając konfigurowanie PHP i zdalną diagnostykę oraz
utrzymywanie bezpieczeństwa.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
