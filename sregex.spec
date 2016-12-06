%define git_sha b1bf5b60c5fc8f19b2ff198225609e222abf3ea3
%define git_sha_abbrev b1bf5b6
%define git_date 20160808

Summary:        A non-backtracking regex engine matching on data streams
Name:           sregex
Version:        %{git_date}git%{git_sha_abbrev}
Release:        0
License:        BSD
Group:          Libraries
Source0:        https://github.com/openresty/sregex/archive/%{git_sha}.tar.gz#/sregex-%{git_sha}.tar.gz
URL:            https://github.com/openresty/sregex/

%description
This is a pure C library that is designed to have zero dependencies.

%package devel
Summary:        Header files for %{name} library
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%prep
%setup -q -n sregex-%{git_sha}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
    PREFIX=/usr DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/%{_libdir}
rm $RPM_BUILD_ROOT/%{_includedir}/sregex/ddebug.h

%clean
rm -rf $RPM_BUILD_ROOT

%post    -p /sbin/ldconfig
%postun    -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sregex-cli
%attr(755,root,root) %{_libdir}/libsregex.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsregex.so.0
%attr(755,root,root) %ghost %{_libdir}/libsregex.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/sregex/sregex.h

%changelog
* Tue Dec  6 2016 Frankie Dintino <fdintino@gmail.com> - 0.0.1-20160808gitb1bf5b6
- Initial version.