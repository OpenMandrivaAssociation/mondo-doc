#
# $Id: mondo-doc.spec 755 2006-08-06 23:15:58Z bruno $
#

Summary:	Documentation for Mondo Rescue
Summary(fr):	Documentation pour Mondo Rescue

Name:		mondo-doc
Version:	2.21
Packager:	Bruno Cornec <bcornec@mandriva.org>
Release:	%mkrel 1
License:	GPL
Group:		Archiving/Backup
Url:		http://www.mondorescue.org
Source:		ftp://ftp.mondorescue.org/src/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)
BuildRequires:	docbook-utils
BuildArch: noarch

%description
Documentation for Mondo Rescue

%description -l fr
Documentation pour Mondo Rescue

%prep
%setup -q -n %name-%{version}

%build
%{__make} -f Makefile.man VERSION=%{version}
%{__make} -f Makefile.howto VERSION=%{version}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} -f Makefile.man install INSTALLDIR=${RPM_BUILD_ROOT}/%{_defaultdocdir}/%{name}-%{version}
%{__make} -f Makefile.howto install INSTALLDIR=${RPM_BUILD_ROOT}/%{_defaultdocdir}/%{name}-%{version}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc %{_defaultdocdir}/%{name}-%{version}


