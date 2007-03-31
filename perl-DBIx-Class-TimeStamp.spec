#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	Class-TimeStamp
Summary:	DBIx::Class::TimeStamp - automatically set timestamp fields in a table
Summary(pl.UTF-8):	DBIx::Class::TimeStamp - automatyczne ustawianie pól znaczników czasu w tabeli
Name:		perl-DBIx-Class-TimeStamp
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/J/JS/JSHIRLEY/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7adea1a2b8dd9fb999a5b35c287ceba4
URL:		http://search.cpan.org/dist/DBIx-Class-TimeStamp/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor-Grouped
BuildRequires:	perl-DateTime
BuildRequires:	perl-DateTime-Format-MySQL
BuildRequires:	perl-DBIx-Class
BuildRequires:	perl-SQL-Translator-DBIx-Class
BuildRequires:	perl-Time-Warp
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Works in conjunction with InflateColumn::DateTime to automatically set
update and create date and time based fields in a table.

%description -l pl.UTF-8
Ten moduł działa w połączeniu z InflateColumn::DateTime, aby
automatycznie ustawiać w tabeli pola z datą i czasem uaktualnienia
oraz utworzenia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/DBIx/Class/*.pm
%{_mandir}/man3/*
