%define	module MailTools
%define	name	perl-%module
%define	version	2.04
%define	release	%mkrel 2

Summary:	A set of perl modules related to mail applications
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%module/
Source:     http://www.cpan.org/modules/by-module/Mail/%{module}-%{version}.tar.gz
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
This is MailTools, a set of perl modules related to mail applications.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog
%{perl_vendorlib}/Mail
%{_mandir}/*/*

