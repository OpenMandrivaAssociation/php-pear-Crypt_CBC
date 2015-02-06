%define		_class		Crypt
%define		_subclass	CBC
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.1
Release:	2
Summary:	A class to emulate Perl's Crypt::CBC module
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Crypt_CBC/
Source0:	http://download.pear.php.net/package/Crypt_CBC-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
A class to emulate Perl's Crypt::CBC module.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-7mdv2012.0
+ Revision: 741833
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-6
+ Revision: 679272
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-5mdv2011.0
+ Revision: 613621
- the mass rebuild of 2010.1 packages

* Sun Dec 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-4mdv2010.1
+ Revision: 478299
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.0.0-3mdv2010.0
+ Revision: 440953
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdv2009.1
+ Revision: 321938
- rebuild

* Sun Oct 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-1mdv2009.1
+ Revision: 292879
- update to new version 1.0.0

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4-8mdv2009.0
+ Revision: 236814
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.4-7mdv2008.1
+ Revision: 140729
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4-7mdv2007.0
+ Revision: 81422
- Import php-pear-Crypt_CBC

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.4-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4-1mdk
- initial Mandriva package (PLD import)


