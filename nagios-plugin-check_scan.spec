%define		plugin	check_scan
Summary:	A nmap scanner plugin for Nagios
Name:		nagios-plugin-%{plugin}
Version:	0.1
Release:	0.1
License:	GPL v2+
Group:		Networking
Source0:	http://www.altsec.info/check_scan.sh
# Source0-md5:	8e79becb95012c2aedf0b9c68373f928
URL:		http://www.altsec.info/check_scan.html
Requires:	nagios-common
Requires:	grep
Requires:	nmap
Requires:	coreutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		nrpeddir	/etc/nagios/nrpe.d
%define		plugindir	%{_prefix}/lib/nagios/plugins

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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin} $RPM_BUILD_ROOT%{plugindir}/%{plugin}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{plugindir}/%{plugin}
