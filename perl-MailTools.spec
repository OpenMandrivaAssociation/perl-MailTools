%define	upstream_name    MailTools
%define upstream_version 2.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	A set of perl modules related to mail applications
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Mail/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is MailTools, a set of perl modules related to mail applications.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README ChangeLog
%{perl_vendorlib}/Mail
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.80.0-3mdv2012.0
+ Revision: 765466
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.80.0-2
+ Revision: 763957
- rebuilt for perl-5.14.x

* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.80.0-1
+ Revision: 684772
- update to new version 2.08

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.70.0-2
+ Revision: 667257
- mass rebuild

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.70.0-1mdv2011.0
+ Revision: 601986
- new version

* Wed Jan 27 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.60.0-1mdv2011.0
+ Revision: 497002
- update to 2.06

* Mon Dec 21 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.50.0-1mdv2010.1
+ Revision: 480725
- update to 2.05

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.40.0-1mdv2010.0
+ Revision: 403847
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.04-2mdv2009.1
+ Revision: 351853
- rebuild

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.04-1mdv2009.0
+ Revision: 270391
- update to new version 2.04

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.03-2mdv2009.0
+ Revision: 265414
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.03-1mdv2009.0
+ Revision: 193857
- update to new version 2.03

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.02-1mdv2008.1
+ Revision: 114707
- update to new version 2.02

* Thu Nov 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.01-1mdv2008.1
+ Revision: 113878
- new version

* Sat Jul 07 2007 Funda Wang <fwang@mandriva.org> 1.77-1mdv2008.0
+ Revision: 49310
- New version

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 1.76-1mdv2008.0
+ Revision: 20440
- 1.76


* Wed Mar 01 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.74-1mdk
- 1.74

* Fri Feb 17 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.73-1mdk
- 1.73
- Fix URL and license

* Mon Apr 25 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.67-1mdk
- 1.64

* Mon Jan 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.66-1mdk
- 1.66

* Mon Nov 29 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.65-1mdk
- 1.65

* Fri Apr 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.62-1mdk
- 1.62

* Wed Aug 27 2003 François Pons <fpons@mandrakesoft.com> 1.59-2mdk
- really use 1.59 (problem of robot rebuilding...)

* Thu Aug 21 2003 François Pons <fpons@mandrakesoft.com> 1.59-1mdk
- 1.59.

* Wed Aug 13 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.58-3mdk
- rebuild for new perl
- drop Prefix tag
- drop $RPM_OPT_FLAGS, noarch..
- don't use PREFIX
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.58-2mdk
- rebuild for new auto{prov,req}

