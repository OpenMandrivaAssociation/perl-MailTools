%define	real_name MailTools
%define	name	perl-%real_name
%define	version	1.77
%define	release	%mkrel 1

Summary:	A set of perl modules related to mail applications
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%real_name/
Source:		%{real_name}-%{version}.tar.bz2
Requires:	perl
BuildRequires:	perl-devel
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root

%description
This is MailTools, a set of perl modules related to mail applications.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog
%{perl_vendorlib}/Mail
%{perl_vendorlib}/auto/Mail
%{_mandir}/*/*

