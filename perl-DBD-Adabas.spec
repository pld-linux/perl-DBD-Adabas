%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	Adabas
Summary:	DBD::Adabas perl module
Summary(pl):	Modu³ perla DBD::Adabas
Name:		perl-DBD-Adabas
Version:	0.2003
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-DBI >= 0.93
#BR: adabas libs installed in $DBROOT or %adabasroot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::Adabas - DBD module interfacing the Adabas D database.

%description -l pl
DBD::Adabas - modu³ DBD komunikuj±cy siê z baz± danych Adabas D.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{?adabasroot:DBROOT=%{adabasroot}; export DBROOT}
perl Makefile.PL

%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/DBD/Adabas.pm
%dir %{perl_sitearch}/auto/DBD/Adabas
%{perl_sitearch}/auto/DBD/Adabas/Adabas.bs
%attr(755,root,root) %{perl_sitearch}/auto/DBD/Adabas/Adabas.so
%{_mandir}/man3/*
