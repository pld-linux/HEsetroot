Summary:	Esetroot with "H" prion
Summary(pl):	Esetroot z prionem "H"
Name:		HEsetroot
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://lubuska.zapto.org/~hoppke/yellow_brown/%{name}.tar.bz2
# Source0-md5:	00ddbcb7818eaac51dfaefe20d31e8c8
URL:		http://lubuska.zapto.org/~hoppke/yellow_brown/
BuildRequires:	imlib2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program enables non-Enlightenment users to use
pseudotransparency.

%description -l pl
Program ten umo¿liwia u¿ytkownikom zarz±dców okien innych ni¿
Enlightenment korzystanie z pseudo-przezroczysto¶ci.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install HEsetroot $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
