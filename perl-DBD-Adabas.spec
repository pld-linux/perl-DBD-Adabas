#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	DBD
%define		pnam	Adabas
Summary:	DBD::Adabas - Adabas driver for DBI
Summary(pl.UTF-8):	DBD::Adabas - sterownik Adabas dla DBI
Name:		perl-DBD-Adabas
Version:	0.2003
Release:	3
# GPL or Artistic as specified in perl README file
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DBD/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	314414fe64b48e1f9cac2cf6f1396db0
URL:		http://search.cpan.org/dist/DBD-Adabas/
BuildRequires:	perl-DBI >= 0.93
BuildRequires:	rpm-perlprov >= 4.1-13
#BR: adabas libs installed in $DBROOT or %adabasroot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::Adabas - DBD module interfacing the Adabas D database.

%description -l pl.UTF-8
DBD::Adabas - moduł DBD komunikujący się z bazą danych Adabas D.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{?adabasroot:DBROOT=%{adabasroot}; export DBROOT}
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

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
%attr(755,root,root) %{perl_vendorarch}/auto/DBD/Adabas/Adabas.so
%{_mandir}/man3/*
