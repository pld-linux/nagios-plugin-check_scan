%define		plugin	check_scan
Summary:	A nmap scanner plugin for Nagios
Name:		nagios-plugin-%{plugin}
Version:	20051011
Release:	1
License:	GPL v2+
Group:		Networking
Source0:	http://www.altsec.info/check_scan.sh
# Source0-md5:	8e79becb95012c2aedf0b9c68373f928
Source1:	%{plugin}.cfg
Patch0:		pld.patch
URL:		http://www.altsec.info/check_scan.html
Requires:	coreutils
Requires:	grep
Requires:	nagios-common
Requires:	nmap
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		nrpeddir	/etc/nagios/nrpe.d
%define		plugindir	%{_prefix}/lib/nagios/plugins
%define		statedir	/var/lib/nagios/check_scan

%description
A nmap scanner plugin for Nagios

Here's what it does:
- On the initial scan, it creates a baseline scan for future
  comparison.
- On each subsequent check, it compares the new scan against the
  baseline.
- Changes are reported in "warning" status, showing the open port.

check_scan.sh does a "TCP connect scan", so it doesn't have to run as
root.

%prep
%setup -qcT
cp -p %{SOURCE0} %{plugin}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir},%{statedir}}
install -p %{plugin} $RPM_BUILD_ROOT%{plugindir}/%{plugin}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,nagios) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
%dir %attr(770,root,nagios) %{statedir}
