# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%global commit bb291f00619a63115fa649a71ea639499a9238de
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           testa
Version:        0.5
Release:        1%{?dist}
Summary:        testa man

License:        GPLv2+
URL:            https://github.com/gregswift/testa
Source0:        https://github.com/gregswift/testa/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel

%description
blah blah

%prep
%setup -qn %{name}-%{commit}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%{python_sitelib}/*

%changelog
* Thu Feb 26 2015 greg5320 <gregswift@gmail.com>
- Initial build
