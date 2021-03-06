# TODO
# - sync -pl
# - contains: eclipse, jre - maybe can use system pkgs
Summary:	Zend Studio - The Leading PHP IDE
Summary(pl.UTF-8):	ZendStudio - narzędzia do zarządzania serwerami WWW opartymi o PHP
Name:		ZendStudio
Version:	10.6.0
Release:	0.1
License:	Zend Studio License
Group:		Applications
Source0:	http://downloads.zend.com/studio-eclipse/%{version}/%{name}-%{version}-linux.gtk.x86.tar.gz
# NoSource0-md5:	d618f10c50d5077b1d6c72406d5a57d6
NoSource:	0
Source1:	http://downloads.zend.com/studio-eclipse/%{version}/%{name}-%{version}-linux.gtk.x86_64.tar.gz
# NoSource1-md5:	3ca8d2aa435070d8405b290875dbd610
NoSource:	1
URL:		http://www.zend.com/products/studio/
BuildRequires:	rpm-pythonprov
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_libdir}/%{name}

# no Provides for privately packaged libs
%define		_noautoprov		libpng12.so.0
%define		_noautoreq		%{_noautoprov}

# don't strip anything. strip crashes, and if it succeeds then ZS crashes
%define		_noautostrip	.*%{_appdir}/.*

# otherwise it builds this package two decades
%define		_noautoprovfiles	%{_appdir}/.*

%description
Zend Studio is our professional-grade PHP IDE (Integrated Development
Environment). It has been designed to maximize developer productivity
by enabling you to develop and maintain code faster, solve application
problems quickly and improve team collaboration.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia do zarządzania serwerami WWW opartymi o
PHP. Moduł pozwala na przezroczystą instalację i integrację,
jednocześnie upraszczając konfigurowanie PHP i zdalną diagnostykę oraz
utrzymywanie bezpieczeństwa.

%prep
%ifarch %{ix86}
%setup -qcT -b 0
%endif
%ifarch %{x8664}
%setup -qcT -b 1
%endif
mv %{name} .unp && mv .unp/* .unp/.eclipseproduct . && rmdir .unp

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

# test if we can hardlink -- %{_builddir} and $RPM_BUILD_ROOT on same partition
if cp -al notice.html $RPM_BUILD_ROOT/notice.html; then
	l=l
	rm -f $RPM_BUILD_ROOT/notice.html
fi

cp -a$l . $RPM_BUILD_ROOT%{_appdir}

rm -f $RPM_BUILD_ROOT%{_appdir}/debug*.list

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_appdir}
%attr(755,root,root) %{_appdir}/ZendStudio
%attr(755,root,root) %{_appdir}/libcairo-swt.so

# use actual file permissions from source tarball. fix this later
%defattr(-,root,root,-)

%{_appdir}/.eclipseproduct
%{_appdir}/readme
%{_appdir}/epl-v10.html
%{_appdir}/notice.html

%{_appdir}/ZendStudio.ini
%{_appdir}/icon.xpm
%{_appdir}/configuration
%{_appdir}/p2

%{_appdir}/artifacts.xml
%{_appdir}/features
%{_appdir}/plugins
