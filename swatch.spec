#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
#
%include	/usr/lib/rpm/macros.perl
Summary:	A utility for monitoring system logs files
Summary(pl.UTF-8):	Narzędzie do monitorowania logów systemowych
Name:		swatch
Version:	3.2.2
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://dl.sourceforge.net/swatch/%{name}-%{version}.tar.gz
# Source0-md5:	b7d360b01da8168b4b7d4cf45c263f55
Source1:	%{name}rc
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

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install %{SOURCE1} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT{%{perl_archlib}/perllocal.pod,%{perl_vendorarch}/auto/swatch/.packlist}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYRIGHT KNOWN_BUGS README examples
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/Swatch
%dir %{perl_vendorlib}/auto/Swatch
%dir %{perl_vendorlib}/auto/Swatch/Actions
%{perl_vendorlib}/auto/Swatch/Actions/autosplit.ix
%{_examplesdir}/%{name}-%{version}
