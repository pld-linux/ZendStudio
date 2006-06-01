Summary:	ZendStudio
Name:		ZendStudio
Version:	5.2.0
Release:	0.1
License:	Zend Studio License
Group:		Applications
Source0:	ZendStudio-5_2_0.tar.gz
# NoSource0-md5:	88f75c1d0576d8f3ec11386471520058
URL:		http://www.zend.com/products/zend_studio
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	%{_prefix}/share/Zend
%define		no_install_post_strip		1
%define		no_install_post_chrpath		1

%description
Includes server management tools that manage PHP based Web servers.
This module makes installation and integration seamless while
simplifying PHP and remote debugging configurations and security
maintenance.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
