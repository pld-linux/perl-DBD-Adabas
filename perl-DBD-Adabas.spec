%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	Adabas
Summary:	DBD::Adabas perl module
Summary(pl):	Modu� perla DBD::Adabas
Name:		perl-DBD-Adabas
Version:	0.2003
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-DBI >= 0.93
#BR: adabas libs installed in $DBROOT or %adabasroot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::Adabas - DBD module interfacing the Adabas D database.

%description -l pl
DBD::Adabas - modu� DBD komunikuj�cy si� z baz� danych Adabas D.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{?adabasroot:DBROOT=%{adabasroot}; export DBROOT}
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 

%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/DBD/Adabas.pm
%dir %{perl_vendorarch}/auto/DBD/Adabas
%{perl_vendorarch}/auto/DBD/Adabas/Adabas.bs
%attr(755,root,root) %{perl_vendorarch}/auto/DBD/Adabas/Adabas.so
%{_mandir}/man3/*