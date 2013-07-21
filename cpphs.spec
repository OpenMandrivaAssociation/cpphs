%global debug_package %{nil}
#% define _cabal_setup Setup.lhs
%define module cpphs
Name:           %{module}
Version:        1.16
Release:        1
Summary:        A liberalised re-implementation of cpp, the C pre-processor
Group:          Development/Other
License:        LGPL
URL:            http://hackage.haskell.org/package/%{module}
Source0:        http://hackage.haskell.org/packages/archive/cpphs/1.16/%{name}-%{version}.tar.gz

BuildRequires:  ghc, ghc-devel, haskell-macros, haddock
Requires:       ghc

%description
Cpphs is a re-implementation of the C pre-processor that is both
more compatible with Haskell, and itself written in Haskell so
that it can be distributed with compilers.
.
This version of the C pre-processor is pretty-much
feature-complete and compatible with traditional (K&R)
pre-processors.  Additional features include: a plain-text mode;
an option to unlit literate code files; and an option to turn
off macro-expansion.

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

%files
%defattr(-,root,root,-)
%{_bindir}/%{module}
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%_cabal_rpm_deps_dir
%_cabal_haddoc_files


%changelog
* Tue Mar 15 2011 Stéphane Téletchéa <steletch@mandriva.org> 1.11-1mdv2011.0
+ Revision: 645079
- update to new version 1.11

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9-4mdv2011.0
+ Revision: 610168
- rebuild

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 1.9-3mdv2010.1
+ Revision: 503614
- rebuild for new gmp

* Sat Dec 05 2009 Funda Wang <fwang@mandriva.org> 1.9-2mdv2010.1
+ Revision: 473960
- use haskell scripts

* Sat Dec 05 2009 Funda Wang <fwang@mandriva.org> 1.9-1mdv2010.1
+ Revision: 473950
- new version 1.9

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.5-4mdv2010.0
+ Revision: 425092
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.5-3mdv2009.0
+ Revision: 240512
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Jul 24 2007 Gaëtan Lehmann <glehmann@mandriva.org> 1.5-1mdv2008.0
+ Revision: 55072
- 1.5


* Wed Aug 09 2006 glehmann
+ 08/09/06 19:30:11 (55019)
rebuild

* Sun Jul 30 2006 glehmann
+ 07/30/06 10:22:36 (42680)
Import cpphs

* Sat May 06 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.2-1mdk
- first mandriva release

* Tue Aug 16 2005 Jens Petersen <petersen@haskell.org> - 0.9-1
- initial build for Fedora Haskell


