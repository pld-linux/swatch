Summary: A utility for monitoring system logs files.
Name: swatch
Version: 2.2
Release: 7
Copyright: Distributable
Group: Applications/System
Source: ftp://ftp.stanford.edu/general/security-tools/swatch/swatch-2.2.tar.gz
Patch0: swatch-2.2-redhat.patch
BuildArchitectures: noarch
BuildRoot: /var/tmp/swatch-root

%description
The Swatch utility monitors system log files, filters out unwanted data
and takes specified actions (i.e., sending email, executing a script,
etc.) based upon what it finds in the log files.

Install the swatch package if you need a program that will monitor log
files and alert you in certain situations.

%prep
%setup -q
%patch0 -p1 -b .redhat

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib,man/man5,man/man8}

perl install.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/swatch
/usr/lib/sw_actions.pl
/usr/lib/sw_history.pl
/usr/man/man5/swatch.5
/usr/man/man8/swatch.8
%doc *.ps config_files README Changes
