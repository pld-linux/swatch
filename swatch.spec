#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
#
%include	/usr/lib/rpm/macros.perl
Summary:	A utility for monitoring system logs files
Summary(pl.UTF-8):	Narzędzie do monitorowania logów systemowych
Name:		swatch
Version:	3.2.3
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/swatch/%{name}-%{version}.tar.gz
# Source0-md5:	1162f1024cf07fc750ed4960d61ac4e8
Source1:    sample.rc
Source2:    sample.conf
Source3:    sample.prestart
Source4:    sample.poststop
Source5:    swatch.sysconfig
Source6:    swatch-service-generator
Source7:    swatch.target
Source8:    swatch@.service
Patch0:     fix_echo.patch
URL:		http://swatch.sourceforge.net/
BuildRequires:	perl-base
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
%if %{with autodeps}
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-Date-Manip
BuildRequires:	perl-File-Tail
BuildRequires:	perl-Time-HiRes >= 1.12
BuildRequires:	perl-TimeDate
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Swatch utility monitors system log files, filters out unwanted
data and takes specified actions (i.e., sending email, executing a
script, etc.) based upon what it finds in the log files.

Install the swatch package if you need a program that will monitor log
files and alert you in certain situations.

%description -l pl.UTF-8
Swatch monitoruje pliki logów systemowych, odfiltrowuje niechciane
dane i wykonuje określone akcje (np. wysyłanie maila, wykonanie
skryptu itp.) w zależności od zawartości logów.

%prep
%setup -q
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name} \
    $RPM_BUILD_ROOT/etc/sysconfig \
    $RPM_BUILD_ROOT{%{systemdtmpfilesdir},%{systemdunitdir}} \
    $RPM_BUILD_ROOT/lib/systemd/system-generators

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/sample.rc
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/sample.conf
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/sample.prestart
install %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/sample.poststop
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/%{name}

install -p %{SOURCE6} $RPM_BUILD_ROOT/lib/systemd/system-generators/%{name}-service-generator
install -p %{SOURCE7} $RPM_BUILD_ROOT%{systemdunitdir}/%{name}.target
install -p %{SOURCE8} $RPM_BUILD_ROOT%{systemdunitdir}/%{name}@.service


%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT{%{perl_archlib}/perllocal.pod,%{perl_vendorarch}/auto/swatch/.packlist}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYRIGHT KNOWN_BUGS README examples
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%attr(755,root,root) /lib/systemd/system-generators/%{name}-service-generator
%{systemdunitdir}/%{name}.target
%{systemdunitdir}/%{name}@.service
%attr(770,root,root) %dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/sample.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/sample.rc
%config(noreplace) %verify(not md5 mtime size) %attr(755,root,root) %{_sysconfdir}/%{name}/sample.p*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/Swatch
%dir %{perl_vendorlib}/auto/Swatch
%dir %{perl_vendorlib}/auto/Swatch/Actions
%{perl_vendorlib}/auto/Swatch/Actions/autosplit.ix
