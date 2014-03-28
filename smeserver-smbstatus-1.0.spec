Summary: SME server smbstatus
%define name smeserver-smbstatus
Name: %{name}
%define version 1.0
%define release 6
Version: %{version}
Release: %{release}
#Copyright: Freely distributable
Group: Apache/php/caching
Source: %{name}-%{version}.tar.gz
#Patch0: XXX.YYYYY.ZZZZZ
License: GNU GPL version 2
Packager: Michel Van hees <michel@vanhees.cc>
BuildRoot: /var/tmp/e-smith-buildroot
BuildRequires:  e-smith-devtools
BuildArchitectures: noarch
Requires: smeserver-release >= 8
AutoReqProv: no

%changelog
* Sat Feb 08 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> smeserver-smbstatus-1.0-6
- change menu heading

* Wed Feb 05 2014 Stephane de Labrusse <stephdl@de-labrusse.fr> smeserver-smbstatus-1.0-5
- adaptation to new build protocol
 
* Mon Jan 07 2008 Michel Van hees <michel@vanhees.cc>
- Thanks to Sylvain Gomez for his fix with french traduction

* Mon Mar 21 2006 Michel Van hees <michel@vanhees.cc>
- start developpement

%description
Display samba status in server-manager

%prep
%setup
#%patch0 -p1
#%patch1 -p1

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%pre
%preun
%post
/etc/e-smith/events/actions/navigation-conf > /dev/null 2>&1

%postun
/etc/e-smith/events/actions/navigation-conf > /dev/null 2>&1

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
