%define	modname	MailTools
%define modver 2.22

Summary:	A set of perl modules related to mail applications
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/markov2/perl5-MailTools
Source0:	https://cpan.metacpan.org/authors/id/M/MA/MARKOV/MailTools-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)

%description
This is MailTools, a set of perl modules related to mail applications.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README ChangeLog
%{perl_vendorlib}/Mail
%{perl_vendorlib}/MailTools.*
%{_mandir}/man3/*
