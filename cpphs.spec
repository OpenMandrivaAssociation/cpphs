Name:           cpphs
Version:        1.9
Release:       	%mkrel 1
Summary:        Liberalised re-implementation of cpp in Haskell
Group:          Development/Other
License:        LGPL
URL:            http://haskell.org/cpphs/
Source0:        http://www.cs.york.ac.uk/fp/cpphs/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  ghc

%description
cpphs is a liberalised re-implementation of cpp in Haskell.

The C pre-processor is widely used in Haskell source code for conditional
compilation and also occasionally for its macro language, However, however
the common cpp provided by gcc is changing subtly in ways that are
incompatible with Haskell's syntax. There have always been problems with, for
instance, string gaps, and prime characters in identifiers and these problems
are only going to get worse. 

So, it seemed right to provide an alternative to cpp, both more compatible
with Haskell, and written in Haskell to be distributed with compilers.

%prep
%setup -q


%build
ghc --make -o cpphs cpphs


%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 cpphs $RPM_BUILD_ROOT%{_bindir}/cpphs
install -D -m 644 docs/cpphs.1 $RPM_BUILD_ROOT%{_mandir}/man1/cpphs.1

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CHANGELOG LICENCE-LGPL README docs/design docs/index.html
%{_bindir}/*
%{_mandir}/man1/*


