%include	/usr/lib/rpm/macros.perl
Summary:	A utility for monitoring system logs files
Summary(pl):	Narzêdzie do monitorowania logów systemowych
Name:		swatch
Version:	3.0.4
Release:	2
License:	distributable
Group:		Applications/System
Source0:	ftp://ftp.stanford.edu/general/security-tools/swatch/%{name}-%{version}.tar.gz
BuildRequires:	perl-Time-HiRes >= 1.12
BuildRequires:	perl-Date-Calc
BuildRequires:	perl-File-Tail
BuildRequires:	perl-TimeDate
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Swatch utility monitors system log files, filters out unwanted
data and takes specified actions (i.e., sending email, executing a
script, etc.) based upon what it finds in the log files.

Install the swatch package if you need a program that will monitor log
files and alert you in certain situations.

%description -l pl
Swatch monitoruje pliki logów systemowych, odfiltrowuje niechciane
dane i wykonuje okre¶lone akcje (np. wysy³anie maila, wykonanie
skryptu itp.) w zalezno¶ci od zawarto¶ci logów.

%prep
%setup -q

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYRIGHT KNOWN_BUGS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
