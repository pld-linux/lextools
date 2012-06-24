Summary:	Toolkit for finite-state linguistic analysis
Summary(pl):	Zestaw narz�dzi do analizy j�zyk�w stan�w sko�czonych
Name:		lextools
Version:	1.0
Release:	1
License:	Free for educational use, non-distributable
# from http://www.research.att.com/cgi-bin/access.cgi/as/vt/ext-software/www-ne-license.cgi?table.lextools.binary
Source0:	%{name}.linux.i386.tar.gz
Group:		Applications/Text
URL:		http://www.research.att.com/sw/tools/lextools/
ExclusiveArch:	i686 athlon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lextools is a package of tools for creating weighted finite-state
transducers from high-level linguistic descriptions.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5},%{_datadir}}
install bin-i686/* $RPM_BUILD_ROOT%{_bindir}
install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install man/*.5 $RPM_BUILD_ROOT%{_mandir}/man5
cp -r lextools-3 $RPM_BUILD_ROOT%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/%{name}-3
